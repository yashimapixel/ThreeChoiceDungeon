extends Control
## All UI screens, built in code for a fixed 360x640 pixel-art canvas.
## The window uses the "canvas_items" stretch mode so text renders at the
## device resolution (crisp at 14/16px) while the art stays nearest-filtered.

# 6-colour palette: black / dark grey / light grey / white, bright red / dark red
const K := Color8(14, 12, 14)
const DG := Color8(74, 70, 70)
const LG := Color8(152, 146, 136)
const W := Color8(232, 226, 212)
const R := Color8(206, 36, 46)
const DR := Color8(110, 20, 28)
const WD := DG   # disabled
const G8 := 8    # layout grid
const SW := 360
const SH := 640
const FS := 16      # body text size
const FS_S := 14    # small text size
const FS_L := 24    # headings

# vertical layout (header / center / footer bands), see _layout()
var view_h := 640.0
var safe_top := 0.0
var safe_bot := 0.0
var bg_rect: ColorRect

var font: FontFile
var font_b: FontFile
var screen: Control
var overlay: Control
var flash: ColorRect
var sfx: Sfx
var music: Music
const LULLABY_EVENTS := ["e027", "e079", "e095", "g100", "x04"]

# game-screen widgets
var g_floor: Label
var g_gold: Label
var g_bars := {}
var g_img: TextureRect
var g_res: TextureRect   # result still, cross-faded over g_img
var g_title: Label
var g_desc: RichTextLabel
var g_items: Control
var item_scroll := 0   # index of the first item shown in the one-line item row
var g_choices: VBoxContainer
var busy := false
var pending: Dictionary = {}


class StatBar extends Control:
	## Gauge with animated changes: on damage the lost part turns red first,
	## then the red part shrinks away; on recovery the fill grows.
	var label := ""
	var fnt: Font
	var value := 10
	var max_value := 10
	var shown := 10.0   # white fill
	var ghost := 10.0   # end of the red "damage" segment (>= shown)
	var tw: Tween

	func set_stat(v: int, mx: int, animate := true) -> void:
		var old := shown
		value = v
		max_value = mx
		if tw:
			tw.kill()
		if not animate or is_equal_approx(old, float(v)):
			shown = v
			ghost = v
			queue_redraw()
			return
		if v < old:
			ghost = maxf(ghost, old)
			shown = v
			tw = create_tween()
			tw.tween_interval(0.45)
			tw.tween_method(_set_ghost, ghost, float(v), 0.6).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_IN_OUT)
		else:
			ghost = old
			tw = create_tween()
			tw.tween_method(_set_shown, old, float(v), 0.55).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_OUT)
		queue_redraw()

	func _set_ghost(x: float) -> void:
		ghost = x
		queue_redraw()

	func _set_shown(x: float) -> void:
		shown = x
		ghost = maxf(ghost, x) if ghost > x else x
		queue_redraw()

	func _draw() -> void:
		var wc := Color8(232, 226, 212)
		var rc := Color8(206, 36, 46)
		var lg := Color8(152, 146, 136)
		var low: bool = value <= maxi(1, int(max_value * 0.3))
		draw_string(fnt, Vector2(0, 14), label, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, lg)
		draw_string(fnt, Vector2(0, 14), "%d/%d" % [value, max_value], HORIZONTAL_ALIGNMENT_RIGHT, size.x, 16, rc if low else wc)
		var by := 19.0
		draw_rect(Rect2(0, by, size.x, 9), rc if low else lg, false, 1.0)
		var inner := size.x - 4
		var mxv := float(maxi(1, max_value))
		var ws := floorf(inner * clampf(shown / mxv, 0, 1))
		var wg := floorf(inner * clampf(ghost / mxv, 0, 1))
		if ws > 0:
			draw_rect(Rect2(2, by + 2, ws, 5), wc, true)
		if wg > ws:
			draw_rect(Rect2(2 + ws, by + 2, wg - ws, 5), rc, true)


class Music extends Node:
	## Cross-fading background music + a hummed lullaby overlay layer.
	var a: AudioStreamPlayer
	var b: AudioStreamPlayer
	var lull: AudioStreamPlayer
	var current := ""
	const BASE_DB := -7.0
	const LULL_DB := -9.0

	func _ready() -> void:
		a = _player()
		b = _player()
		lull = _player()
		lull.stream = _load("lullaby")

	func _player() -> AudioStreamPlayer:
		var p := AudioStreamPlayer.new()
		p.volume_db = -60
		add_child(p)
		return p

	func _load(n: String) -> AudioStream:
		var s = load("res://audio/%s.ogg" % n)
		if s is AudioStreamOggVorbis:
			s.loop = n != "gameover"
		return s

	func play(n: String, fade := 1.5) -> void:
		if n == current:
			return
		current = n
		var old := a
		a = b
		b = old
		a.stream = _load(n)
		a.volume_db = -40
		a.play()
		var tw := create_tween().set_parallel(true)
		tw.tween_property(a, "volume_db", BASE_DB, fade)
		tw.tween_property(b, "volume_db", -60.0, fade)
		tw.chain().tween_callback(b.stop)

	func lullaby(on: bool) -> void:
		var target := LULL_DB if on else -60.0
		if on and not lull.playing:
			lull.volume_db = -60
			lull.play()
		var tw := create_tween()
		tw.tween_property(lull, "volume_db", target, 2.0)
		if not on:
			tw.tween_callback(lull.stop)


class Sfx extends Node:
	## Tiny procedural sound effects (no audio assets needed).
	var players := {}

	func _ready() -> void:
		players["click"] = _make(_tone(880, 0.03, 0.25))
		players["hurt"] = _make(_noise(0.18, 0.35))
		players["good"] = _make(_sweep(440, 880, 0.12, 0.2))
		var steps := AudioStreamPlayer.new()
		steps.stream = load("res://audio/sfx_steps.ogg")
		steps.volume_db = -2
		add_child(steps)
		players["step"] = steps
		players["death"] = _make(_sweep(300, 40, 1.2, 0.4))
		players["bell"] = _make(_bell(0.9))

	func play(n: String) -> void:
		if players.has(n):
			players[n].play()

	func _make(data: PackedByteArray) -> AudioStreamPlayer:
		var s := AudioStreamWAV.new()
		s.format = AudioStreamWAV.FORMAT_16_BITS
		s.mix_rate = 22050
		s.data = data
		var p := AudioStreamPlayer.new()
		p.stream = s
		p.volume_db = -8
		add_child(p)
		return p

	func _pack(samples: PackedFloat32Array) -> PackedByteArray:
		var b := PackedByteArray()
		b.resize(samples.size() * 2)
		for i in samples.size():
			b.encode_s16(i * 2, int(clampf(samples[i], -1, 1) * 32000))
		return b

	func _tone(f: float, dur: float, vol: float) -> PackedByteArray:
		var n := int(22050 * dur)
		var s := PackedFloat32Array()
		s.resize(n)
		for i in n:
			var t := float(i) / 22050.0
			s[i] = (1.0 if fmod(t * f, 1.0) < 0.5 else -1.0) * vol * (1.0 - float(i) / n)
		return _pack(s)

	func _sweep(f0: float, f1: float, dur: float, vol: float) -> PackedByteArray:
		var n := int(22050 * dur)
		var s := PackedFloat32Array()
		s.resize(n)
		var ph := 0.0
		for i in n:
			var k := float(i) / n
			ph += lerpf(f0, f1, k) / 22050.0
			s[i] = (1.0 if fmod(ph, 1.0) < 0.5 else -1.0) * vol * (1.0 - k)
		return _pack(s)

	func _noise(dur: float, vol: float) -> PackedByteArray:
		var n := int(22050 * dur)
		var s := PackedFloat32Array()
		s.resize(n)
		var v := 0.0
		for i in n:
			if i % 6 == 0:
				v = randf_range(-1, 1)
			s[i] = v * vol * pow(1.0 - float(i) / n, 2)
		return _pack(s)

	func _bell(dur: float) -> PackedByteArray:
		var n := int(22050 * dur)
		var s := PackedFloat32Array()
		s.resize(n)
		for i in n:
			var t := float(i) / 22050.0
			s[i] = (sin(TAU * 220 * t) * 0.5 + sin(TAU * 331 * t) * 0.3 + sin(TAU * 523 * t) * 0.2) * 0.4 * exp(-t * 4)
		return _pack(s)


# ================================================================ setup
func _ready() -> void:
	get_tree().set_auto_accept_quit(false)
	get_tree().set_quit_on_go_back(false)
	_setup_theme()
	bg_rect = ColorRect.new()
	bg_rect.color = K
	bg_rect.size = Vector2(SW, SH)
	add_child(bg_rect)
	sfx = Sfx.new()
	add_child(sfx)
	music = Music.new()
	add_child(music)
	AudioServer.set_bus_mute(0, not Game.save.get("sound", true))
	flash = ColorRect.new()
	flash.color = Color(R, 0)
	flash.size = Vector2(SW, SH)
	flash.mouse_filter = Control.MOUSE_FILTER_IGNORE
	flash.z_index = 100
	add_child(flash)
	show_title()


func _setup_theme() -> void:
	font = load("res://fonts/PixelMplus12-Regular.ttf")
	font_b = load("res://fonts/PixelMplus12-Bold.ttf")
	for f in [font, font_b]:
		f.antialiasing = TextServer.FONT_ANTIALIASING_NONE
		f.hinting = TextServer.HINTING_NONE
		f.subpixel_positioning = TextServer.SUBPIXEL_POSITIONING_DISABLED
		f.generate_mipmaps = false
	var t := Theme.new()
	t.default_font = font
	t.default_font_size = FS
	t.set_color("font_color", "Label", W)
	t.set_color("default_color", "RichTextLabel", W)
	t.set_font("bold_font", "RichTextLabel", font_b)
	t.set_constant("line_separation", "RichTextLabel", 3)
	t.set_constant("line_spacing", "Label", 3)
	t.set_stylebox("normal", "Button", _skin("btn_normal", 4, 6))
	t.set_stylebox("hover", "Button", _skin("btn_normal", 4, 6))
	t.set_stylebox("pressed", "Button", _skin("btn_pressed", 6, 4))
	t.set_stylebox("hover_pressed", "Button", _skin("btn_pressed", 6, 4))
	t.set_stylebox("disabled", "Button", _skin("btn_disabled", 5, 5))
	t.set_stylebox("focus", "Button", StyleBoxEmpty.new())
	t.set_color("font_color", "Button", W)
	t.set_color("font_hover_color", "Button", W)
	t.set_color("font_pressed_color", "Button", LG)
	t.set_color("font_hover_pressed_color", "Button", LG)
	t.set_color("font_focus_color", "Button", W)
	t.set_color("font_disabled_color", "Button", WD)
	var ps := _sb(K, LG)
	ps.set_content_margin_all(0)
	t.set_stylebox("panel", "PanelContainer", ps)
	theme = t


## 9-patch pixel button skin from art/ui (12x12, patch margins 3/3/3/4).
## top/bottom are the content margins: the pressed skin sinks the label by 2px.
func _skin(name: String, top := 4, bottom := 6, patch := Vector4(3, 3, 3, 4)) -> StyleBoxTexture:
	var t := StyleBoxTexture.new()
	t.texture = load("res://art/ui/%s.png" % name)
	t.texture_margin_left = patch.x
	t.texture_margin_top = patch.y
	t.texture_margin_right = patch.z
	t.texture_margin_bottom = patch.w
	t.content_margin_left = 8
	t.content_margin_right = 8
	t.content_margin_top = top
	t.content_margin_bottom = bottom
	return t


## Overlay backdrop: the screen behind stays visible, every pixel one palette step darker
## (white > light grey > dark grey > black, bright red > dark red > black).
const DIM_SHADER := """
shader_type canvas_item;
uniform sampler2D screen_tex : hint_screen_texture, filter_nearest;
void fragment() {
	vec3 c = texture(screen_tex, SCREEN_UV).rgb;
	vec3 pk = vec3(14.0, 12.0, 14.0) / 255.0;
	vec3 pdg = vec3(74.0, 70.0, 70.0) / 255.0;
	vec3 plg = vec3(152.0, 146.0, 136.0) / 255.0;
	vec3 pw = vec3(232.0, 226.0, 212.0) / 255.0;
	vec3 pr = vec3(206.0, 36.0, 46.0) / 255.0;
	vec3 pdr = vec3(110.0, 20.0, 28.0) / 255.0;
	vec3 o = pk;
	float bd = distance(c, pk);
	float d = distance(c, pdg); if (d < bd) { bd = d; o = pk; }
	d = distance(c, plg); if (d < bd) { bd = d; o = pdg; }
	d = distance(c, pw); if (d < bd) { bd = d; o = plg; }
	d = distance(c, pr); if (d < bd) { bd = d; o = pdr; }
	d = distance(c, pdr); if (d < bd) { bd = d; o = pk; }
	COLOR = vec4(o, 1.0);
}
"""
var _dim_mat: ShaderMaterial


func _dim_material() -> ShaderMaterial:
	if _dim_mat == null:
		var sh := Shader.new()
		sh.code = DIM_SHADER
		_dim_mat = ShaderMaterial.new()
		_dim_mat.shader = sh
	return _dim_mat


func _sb(bg: Color, border: Color, bw := 1) -> StyleBoxFlat:
	var s := StyleBoxFlat.new()
	s.bg_color = bg
	s.border_color = border
	s.set_border_width_all(bw)
	s.set_content_margin_all(4)
	s.anti_aliasing = false
	return s


func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_GO_BACK_REQUEST or what == NOTIFICATION_WM_CLOSE_REQUEST:
		_on_back()


func _on_back() -> void:
	if overlay:
		_close_overlay()
		return
	if screen and screen.name == "Title":
		get_tree().quit()
	elif screen and screen.name == "Game":
		_confirm("探索を中断してタイトルに戻りますか？\n（「続きから」で再開できます）", func(): show_title())
	else:
		show_title()


# ================================================================ layout
## Logical screen is 360 wide; on screens taller than 9:16 it grows in height.
## Safe-area insets (notch / rounded corners) are converted to logical units.
func _metrics() -> void:
	var vs := get_viewport().get_visible_rect().size
	view_h = maxf(float(SH), vs.y)
	position = Vector2(floorf(maxf(0.0, vs.x - SW) / 2.0), 0)
	size = Vector2(SW, view_h)
	bg_rect.position = Vector2(-position.x, 0)
	bg_rect.size = Vector2(maxf(vs.x, SW), view_h)
	flash.size = Vector2(SW, view_h)
	safe_top = 0.0
	safe_bot = 0.0
	if OS.has_feature("mobile"):
		var sa := DisplayServer.get_display_safe_area()
		var ss := DisplayServer.screen_get_size()
		var k := float(ss.x) / maxf(1.0, vs.x)
		if k > 0.0:
			safe_top = maxf(0.0, float(sa.position.y)) / k
			safe_bot = maxf(0.0, float(ss.y - sa.end.y)) / k


static func _snap(v: float) -> float:
	return roundf(v / G8) * G8


## Moves a screen built in the 360x640 base layout into header / center / footer bands:
## children whose top is above header_h stick to the top of the safe area, children
## below 640 - footer_h stick to the bottom, everything else is centred in between.
func _layout(s: Control, header_h: int, footer_h: int) -> void:
	var top := safe_top
	var bottom := view_h - safe_bot
	var base_center := float(SH - header_h - footer_h)
	var avail := bottom - top - header_h - footer_h
	var c_off := top + _snap((avail - base_center) / 2.0)
	var f_off := bottom - SH
	for ch in s.get_children():
		if not ch is Control:
			continue
		var y: float = ch.position.y
		if y < header_h:
			ch.position.y = y + top
		elif y >= SH - footer_h:
			ch.position.y = y + f_off
		else:
			ch.position.y = y + c_off


# ================================================================ helpers
func _new_screen(nm: String) -> Control:
	_close_overlay()
	_metrics()
	if screen:
		screen.queue_free()
	screen = Control.new()
	screen.name = nm
	screen.size = Vector2(SW, view_h)
	add_child(screen)
	move_child(flash, -1)
	screen.modulate = Color(1, 1, 1, 0)
	create_tween().tween_property(screen, "modulate:a", 1.0, 0.25)
	return screen


func _label(parent: Node, text: String, pos: Vector2, sz: Vector2, size := FS, col := W, align := HORIZONTAL_ALIGNMENT_LEFT, bold := false) -> Label:
	var l := Label.new()
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART if sz.x > 0 else TextServer.AUTOWRAP_OFF
	l.text = text
	l.position = pos
	l.size = sz
	l.horizontal_alignment = align
	l.add_theme_color_override("font_color", col)
	l.add_theme_font_size_override("font_size", size)
	# 24px kanji headings read better in the regular weight
	if bold and not (size >= FS_L and _has_kanji(text)):
		l.add_theme_font_override("font", font_b)
	parent.add_child(l)
	return l


static func _has_kanji(t: String) -> bool:
	for i in t.length():
		if t.unicode_at(i) >= 0x4E00:
			return true
	return false


func _button(parent: Node, text: String, pos: Vector2, sz: Vector2, cb: Callable, size := FS) -> Button:
	var b := Button.new()
	b.text = text
	b.position = pos
	b.size = sz
	b.add_theme_font_size_override("font_size", size)
	b.pressed.connect(func():
		sfx.play("click")
		cb.call())
	parent.add_child(b)
	return b


## Grid-aligned 344x208 frame at pos; the 336x200 still sits 4px inside it.
func _image(parent: Node, id: String, pos: Vector2) -> TextureRect:
	var frame := Panel.new()
	frame.position = pos
	frame.size = Vector2(344, 208)
	frame.add_theme_stylebox_override("panel", _sb(K, DG))
	frame.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(frame)
	var tr := TextureRect.new()
	tr.texture = _tex(id)
	tr.position = Vector2(4, 4)
	tr.size = Vector2(336, 200)
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.stretch_mode = TextureRect.STRETCH_SCALE
	tr.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	frame.add_child(tr)
	return tr


func _res_tex(key: String) -> Texture2D:
	var p := "res://art/results/%s.png" % key
	if ResourceLoader.exists(p):
		return load(p)
	return null


func _tex(id: String) -> Texture2D:
	var p := "res://art/events/%s.png" % id
	if ResourceLoader.exists(p):
		return load(p)
	return null


func _flash(col: Color, a := 0.35) -> void:
	flash.color = Color(col, a)
	create_tween().tween_property(flash, "color:a", 0.0, 0.35)


func _shake() -> void:
	if not screen:
		return
	var tw := create_tween()
	for i in 6:
		tw.tween_property(screen, "position", Vector2(randi_range(-3, 3), randi_range(-2, 2)), 0.03)
	tw.tween_property(screen, "position", Vector2.ZERO, 0.03)


func _overlay_panel(h: int, w := 328) -> PanelContainer:
	_close_overlay()
	overlay = Control.new()
	overlay.size = Vector2(SW, view_h)
	overlay.z_index = 50
	add_child(overlay)
	var dim := ColorRect.new()
	dim.color = K
	dim.material = _dim_material()
	dim.position = Vector2(-position.x, 0)
	dim.size = Vector2(maxf(SW, get_viewport().get_visible_rect().size.x), view_h)
	dim.gui_input.connect(func(ev):
		if ev is InputEventMouseButton and ev.pressed:
			_close_overlay())
	overlay.add_child(dim)
	var p := PanelContainer.new()
	p.position = Vector2(_snap((SW - w) / 2.0), _snap((view_h - h) / 2.0))
	p.size = Vector2(w, h)
	overlay.add_child(p)
	return p


func _close_overlay() -> void:
	if overlay:
		overlay.queue_free()
		overlay = null


func _confirm(msg: String, yes: Callable) -> void:
	var p := _overlay_panel(176)
	var c := Control.new()
	p.add_child(c)
	_label(c, msg, Vector2(8, 8), Vector2(312, 104))
	_button(c, "はい", Vector2(8, 128), Vector2(152, 40), func():
		_close_overlay()
		yes.call())
	_button(c, "いいえ", Vector2(168, 128), Vector2(152, 40), func(): _close_overlay())


func _rich(parent: Node, pos: Vector2, sz: Vector2, size := FS) -> RichTextLabel:
	var r := RichTextLabel.new()
	r.bbcode_enabled = true
	r.position = pos
	r.size = sz
	r.scroll_active = false
	r.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	r.mouse_filter = Control.MOUSE_FILTER_PASS
	_rich_size(r, size)
	parent.add_child(r)
	return r


func _rich_size(r: RichTextLabel, size: int) -> void:
	r.add_theme_font_size_override("normal_font_size", size)
	r.add_theme_font_size_override("bold_font_size", size)


## Set bbcode text, shrinking the font (16 -> 14 -> 12) until it fits the box.
func _set_fit(r: RichTextLabel, text: String, sizes := [FS, FS_S, 12]) -> void:
	for sz in sizes:
		_rich_size(r, sz)
		r.text = text
		if r.get_content_height() <= r.size.y:
			return


static func _hex(c: Color) -> String:
	return "#" + c.to_html(false)


# ================================================================ title
func _music_menu() -> void:
	music.lullaby(false)
	music.play("title")


func show_title() -> void:
	var s := _new_screen("Title")
	_music_menu()
	var snd := _button(s, "", Vector2(272, 8), Vector2(80, 24), func():
		Game.save["sound"] = not Game.save.get("sound", true)
		Game.write_save()
		AudioServer.set_bus_mute(0, not Game.save["sound"])
		show_title(), FS_S)
	snd.text = "♪ 音 ON" if Game.save.get("sound", true) else "♪ 音 OFF"
	_image(s, "title", Vector2(8, 40))
	_label(s, "三択ダンジョン", Vector2(0, 256), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var sv: Dictionary = Game.save
	_label(s, "最高到達 B%dF　魂の欠片 %d" % [sv["best"], sv["coins"]], Vector2(0, 296), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	var y := 336
	if Game.has_run():
		var r: Dictionary = sv["run"]
		_button(s, "続きから（%sB%dF）" % ["無限 " if r["endless"] else "", r["floor"]], Vector2(48, y), Vector2(264, 40), func():
			Game.resume_run()
			show_game(true))
		y += 48
	_button(s, "迷宮へ潜る", Vector2(48, y), Vector2(264, 40), func(): _start(false))
	y += 48
	if sv["cleared"]:
		_button(s, "無限迷宮（エンドレス）", Vector2(48, y), Vector2(264, 40), func(): _start(true))
		y += 48
	_button(s, "強化", Vector2(48, y), Vector2(128, 40), show_shop)
	_button(s, "図鑑", Vector2(184, y), Vector2(128, 40), show_collection)
	y += 48
	var jc: Array = Game.journal_count()
	_button(s, "手記 %d/%d" % [jc[0], jc[1]], Vector2(48, y), Vector2(128, 40), show_journal)
	_button(s, "遊び方", Vector2(184, y), Vector2(128, 40), show_help)
	_button(s, "データ消去", Vector2(8, 608), Vector2(96, 24), func():
		_confirm("全てのセーブデータを消去しますか？\nこの操作は取り消せません。", func():
			Game.reset_save()
			show_title()), 12)
	if sv["cleared"]:
		_label(s, "★ 踏破済み　無限迷宮 最高 B%dF" % sv["best_endless"], Vector2(0, 576), Vector2(SW, 16), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER)
	_label(s, "v1.10.1　Font: PixelMplus (M+ FONTS)", Vector2(112, 608), Vector2(240, 24), 12, DG, HORIZONTAL_ALIGNMENT_RIGHT)
	_layout(s, 32, 40)


func _start(is_endless: bool) -> void:
	if Game.has_run():
		_confirm("中断中の探索は失われます。\n新しく潜りますか？", func(): _choose_start(is_endless))
	else:
		_choose_start(is_endless)


## Normal runs can start below a cleared gate (25/50/75) for a soul fee.
func _choose_start(is_endless: bool) -> void:
	var cps := Game.unlocked_checkpoints()
	if is_endless or cps.is_empty():
		_begin(is_endless)
		return
	var h := 160 + cps.size() * 48
	var p := _overlay_panel(h)
	var c := Control.new()
	p.add_child(c)
	_label(c, "どこから潜る？", Vector2(8, 8), Vector2(312, 24), FS, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(c, "魂の欠片 %d" % Game.save["coins"], Vector2(8, 32), Vector2(312, 24), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER)
	var y := 64
	_button(c, "地下1階から", Vector2(8, y), Vector2(312, 40), func():
		_close_overlay()
		_begin_from(1))
	for g in cps:
		y += 48
		var cost := Game.checkpoint_cost(g)
		var b := _button(c, "地下%d階から（魂の欠片 %d）" % [g + 1, cost], Vector2(8, y), Vector2(312, 40), func():
			_close_overlay()
			_begin_from(g))
		b.disabled = int(Game.save["coins"]) < cost
	y += 48
	_label(c, "途中から始めると、深さの報酬は開始した階より先の分だけになる。", Vector2(8, y), Vector2(312, 40), 12, LG, HORIZONTAL_ALIGNMENT_LEFT)


func _begin_from(g: int) -> void:
	if Game.start_from_checkpoint(g):
		Game.save_run()
		_enter_game()


func _begin(is_endless: bool) -> void:
	Game.start_run(is_endless)
	Game.save_run()
	_enter_game()


## The prologue is shown once, before the very first descent.
func _enter_game() -> void:
	if not Game.save.get("prologue_seen", false):
		Game.save["prologue_seen"] = true
		Game.write_save()
		show_prologue(func(): show_game(true))
	else:
		show_game(true)


const PROLOGUE := "王都の地下に、底知れぬ迷宮がある。\nその百階の底では、どんな願いも叶うという。\n\n三年前、病で幼い王女を亡くした王妃が、ひとりで迷宮へ降りて行ったが、二度と戻ることはなかった。\n\nそして今――夜ごと、王都の地下から、言葉のない子守唄が響く。\n\n孤独な王は布告を出した。\n「迷宮の底に潜り、真実を明らかにできる勇者を求む」\n\nそして、今日も一人の冒険者が深淵に挑んでゆく……"


func show_prologue(then: Callable) -> void:
	var s := _new_screen("Prologue")
	_image(s, "title", Vector2(8, 24))
	var r := _rich(s, Vector2(16, 240), Vector2(328, 328))
	_set_fit(r, PROLOGUE)
	r.visible_ratio = 0
	var tw := create_tween()
	tw.tween_property(r, "visible_ratio", 1.0, 6.0)
	r.gui_input.connect(func(ev):
		if ev is InputEventMouseButton and ev.pressed:
			tw.kill()
			r.visible_ratio = 1.0)
	_button(s, "降りる", Vector2(88, 592), Vector2(184, 40), then)
	_layout(s, 0, 64)


# ================================================================ help
func show_help(page := 0) -> void:
	var s := _new_screen("Help")
	_music_menu()
	_label(s, "遊び方", Vector2(0, 16), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var h := _hex(R)
	var pages := [
		"[color=%s]■ はじまり[/color]\n" % h + PROLOGUE,
		"[color=%s]■ 目的[/color]\n地下百階の迷宮を一階ずつ降り、最深部を目指す。\n\n" % h +
		"[color=%s]■ 三つの力[/color]\n[b]肉体[/b]…傷や戦いに耐える力\n[b]精神[/b]…恐怖や狂気に耐える力\n[b]運命[/b]…幸運と罠を避ける力\nどれか一つでも0になると力尽きる。\n\n" % h +
		"[color=%s]■ 選択[/color]\n各階で出来事が起き、三つの選択肢から一つを選ぶ。［判定］のついた選択は、表示された確率で成否が決まる。確率は今の能力値と所持品で上下する。深く潜るほど出来事は苛烈になる。" % h,
		"[color=%s]■ 結果の記憶[/color]\n一度見た結果は、選択肢に「成功→肉体-2」のように表示される。\n\n" % h +
		"[color=%s]■ 所持品[/color]\n〈 〉は所持品が必要な選択肢。所持品をタップすると効果がわかる。薬瓶はタップで使える。\n\n" % h +
		"[color=%s]■ 死と継承[/color]\n探索中に拾う金貨は、その探索の中での支払いに使う。力尽きると、到達した深さと残った金貨が「魂の欠片」に換わる。魂の欠片で初期能力を強化できる。累計で潜った階数が増えるほど、新たな出来事が解放される。\n\n" % h +
		"[color=%s]■ 門番[/color]\n地下25・50・75階には門番が待つ。門番を越えると、次からは魂の欠片を払ってその先の階から潜れる。そして地下100階には――。" % h,
	]
	var r := _rich(s, Vector2(16, 56), Vector2(328, 464))
	_set_fit(r, pages[page])
	_label(s, "%d / %d" % [page + 1, pages.size()], Vector2(0, 536), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	var prev := _button(s, "◀ 前", Vector2(8, 528), Vector2(96, 40), func(): show_help(page - 1))
	prev.disabled = page == 0
	var nxt := _button(s, "次 ▶", Vector2(256, 528), Vector2(96, 40), func(): show_help(page + 1))
	nxt.disabled = page >= pages.size() - 1
	_button(s, "戻る", Vector2(88, 584), Vector2(184, 40), show_title)
	_layout(s, 56, 112)


# ================================================================ shop
func show_shop() -> void:
	var s := _new_screen("Shop")
	_music_menu()
	_label(s, "強化", Vector2(0, 8), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "魂の欠片 %d" % Game.save["coins"], Vector2(0, 40), Vector2(SW, 24), FS, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	var desc := {"b": "傷や戦いに耐える力。", "m": "恐怖や狂気に耐える力。", "f": "幸運と、罠を避ける力。"}
	var y := 72
	for st in Game.STATS:
		var box := Panel.new()
		box.position = Vector2(8, y)
		box.size = Vector2(344, 120)
		box.add_theme_stylebox_override("panel", _sb(K, DG))
		s.add_child(box)
		var lv: int = Game.save["lv"][st]
		_label(box, "%s　Lv.%d" % [Game.STAT_NAME[st], lv], Vector2(8, 8), Vector2(328, 24), FS, W, HORIZONTAL_ALIGNMENT_LEFT, true)
		_label(box, desc[st], Vector2(8, 32), Vector2(328, 24), FS, LG)
		var now := Game.stat_max_base(st)
		_label(box, "初期値 %d → %d" % [now, now + int(Game.B["stat_per_level"])], Vector2(8, 56), Vector2(328, 24))
		var cost := Game.upgrade_cost(st)
		var b := _button(box, "強化する（魂の欠片 %d）" % cost, Vector2(8, 80), Vector2(328, 32), func():
			if Game.buy_upgrade(st):
				sfx.play("good")
				show_shop())
		b.disabled = int(Game.save["coins"]) < cost
		y += 128
	var nxt := Game.next_unlock_total()
	var hint := "累計 %d階 潜ると新たな出来事が解放される（現在 %d階）" % [nxt, Game.save["total"]] if nxt > 0 else "全ての出来事が解放されている"
	_label(s, hint, Vector2(16, 456), Vector2(328, 40), FS_S, LG, HORIZONTAL_ALIGNMENT_CENTER)
	_button(s, "迷宮へ潜る", Vector2(48, 512), Vector2(264, 40), func(): _start(false))
	_button(s, "戻る", Vector2(48, 560), Vector2(264, 40), show_title)
	_layout(s, 72, 136)


# ================================================================ game
func show_game(intro := false) -> void:
	var s := _new_screen("Game")
	g_floor = _label(s, "", Vector2(8, 8), Vector2(200, 24), FS_L, W, HORIZONTAL_ALIGNMENT_LEFT, true)
	g_gold = _label(s, "", Vector2(176, 8), Vector2(176, 24), FS, LG, HORIZONTAL_ALIGNMENT_RIGHT)
	g_bars.clear()
	for i in 3:
		var st: String = Game.STATS[i]
		var b := StatBar.new()
		b.fnt = font
		b.label = Game.STAT_NAME[st]
		b.position = Vector2(8 + i * 120, 32)
		b.size = Vector2(104, 32)
		b.mouse_filter = Control.MOUSE_FILTER_IGNORE
		s.add_child(b)
		g_bars[st] = b
	g_img = _image(s, Game.event["id"], Vector2(8, 64))
	g_res = g_img.duplicate()
	g_res.texture = null
	g_res.modulate.a = 0.0
	g_img.get_parent().add_child(g_res)
	g_title = _label(s, "", Vector2(8, 280), Vector2(344, 24), FS, W, HORIZONTAL_ALIGNMENT_LEFT, true)
	g_desc = _rich(s, Vector2(8, 304), Vector2(344, 104))
	g_desc.gui_input.connect(func(ev):
		if ev is InputEventMouseButton and ev.pressed:
			g_desc.visible_ratio = 1.0)
	g_items = Control.new()
	g_items.position = Vector2(8, 416)
	g_items.size = Vector2(344, 24)
	g_items.clip_contents = true
	s.add_child(g_items)
	item_scroll = 0
	g_choices = VBoxContainer.new()
	g_choices.position = Vector2(8, 448)
	g_choices.size = Vector2(344, 184)
	g_choices.add_theme_constant_override("separation", 8)
	s.add_child(g_choices)
	_layout(s, 64, 0)
	_refresh_hud(false)
	if intro:
		_floor_card(func(): _present_event())
	else:
		_present_event()


func _refresh_hud(animate := true) -> void:
	g_floor.text = "B%dF" % Game.floor_n
	g_floor.add_theme_color_override("font_color", R if Game.event.has("fixed") else W)
	g_gold.text = ("無限　" if Game.endless else "") + "金貨 %d" % Game.gold
	for st in Game.STATS:
		var b: StatBar = g_bars[st]
		b.set_stat(int(Game.cur[st]), int(Game.mx[st]), animate)
	_build_items()


const ARW := 24   # width of the ◀ ▶ buttons of the item row


func _item_style(col: Color) -> StyleBoxFlat:
	var st := _sb(K, col)
	st.set_content_margin_all(1)
	st.content_margin_left = 4
	st.content_margin_right = 4
	return st


## One-line item row of 24x24 icon buttons. When they don't fit, ◀ ▶ page through them.
func _build_items() -> void:
	for c in g_items.get_children():
		g_items.remove_child(c)
		c.queue_free()
	var names: Array = Game.item_list()
	if names.is_empty():
		return
	var gap := 8.0
	var cell := 24.0
	var total := names.size() * (cell + gap) - gap
	var arrows: bool = total > g_items.size.x
	var x0 := (ARW + gap) if arrows else 0.0
	var x1 := g_items.size.x - ((ARW + gap) if arrows else 0.0)
	var per := int(floor((x1 - x0 + gap) / (cell + gap)))
	item_scroll = clampi(item_scroll, 0, maxi(0, names.size() - per)) if arrows else 0
	var x := x0
	for i in range(item_scroll, mini(names.size(), item_scroll + per)):
		var f: String = names[i]
		var it: Dictionary = Game.ITEMS[f]
		var b := Button.new()
		b.icon = load("res://art/items/%s.png" % f)
		b.icon_alignment = HORIZONTAL_ALIGNMENT_CENTER
		b.position = Vector2(x, 0)
		b.size = Vector2(cell, cell)
		var bad: bool = it.get("bad", false)
		var frame := _skin("item_frame_bad" if bad else "item_frame", 2, 2, Vector4(2, 2, 2, 2))
		frame.content_margin_left = 2
		frame.content_margin_right = 2
		b.add_theme_stylebox_override("normal", frame)
		b.add_theme_stylebox_override("hover", frame)
		b.add_theme_stylebox_override("pressed", _skin("item_frame_down", 2, 2, Vector4(2, 2, 2, 2)))
		b.pressed.connect(func(): _item_popup(f))
		g_items.add_child(b)
		b.position = Vector2(x, 0)
		b.size = Vector2(cell, cell)
		var n := Game.item_count(f)
		if n > 1:
			var l := _label(b, str(n), Vector2(12, 10), Vector2(14, 14), 12, W, HORIZONTAL_ALIGNMENT_RIGHT)
			l.add_theme_constant_override("outline_size", 3)
			l.add_theme_color_override("font_outline_color", K)
			l.mouse_filter = Control.MOUSE_FILTER_IGNORE
		x += cell + gap
	if arrows:
		_item_arrow("◀", 0, item_scroll > 0, -1)
		_item_arrow("▶", g_items.size.x - ARW, item_scroll + per < names.size(), 1)


func _item_arrow(t: String, x: float, enabled: bool, step: int) -> Button:
	var b := Button.new()
	b.text = t
	b.position = Vector2(x, 0)
	b.size = Vector2(ARW, g_items.size.y)
	b.add_theme_font_size_override("font_size", FS_S)
	for k in ["normal", "hover", "pressed", "disabled"]:
		var sk: StyleBoxTexture = theme.get_stylebox(k, "Button").duplicate()
		sk.content_margin_left = 0
		sk.content_margin_right = 0
		sk.content_margin_top = 0
		sk.content_margin_bottom = 2
		b.add_theme_stylebox_override(k, sk)
	b.disabled = not enabled
	b.pressed.connect(func():
		sfx.play("click")
		item_scroll += step
		_build_items())
	g_items.add_child(b)
	b.position = Vector2(x, 0)
	b.size = Vector2(ARW, g_items.size.y)
	return b


func _item_popup(f: String) -> void:
	sfx.play("click")
	var it: Dictionary = Game.ITEMS[f]
	var p := _overlay_panel(176)
	var c := Control.new()
	p.add_child(c)
	var cnt := Game.item_count(f)
	var ic := TextureRect.new()
	ic.texture = load("res://art/items/%s.png" % f)
	ic.position = Vector2(8, 8)
	ic.size = Vector2(24, 24)
	ic.stretch_mode = TextureRect.STRETCH_KEEP_CENTERED
	c.add_child(ic)
	_label(c, it["name"] + ("　×%d" % cnt if cnt > 1 else ""), Vector2(40, 8), Vector2(280, 24), FS, R if it.get("bad", false) else W, HORIZONTAL_ALIGNMENT_LEFT, true)
	_label(c, it["desc"], Vector2(8, 40), Vector2(312, 80), FS, LG)
	if f == "potion" and not busy:
		_button(c, "使う", Vector2(8, 128), Vector2(152, 40), func():
			var h := Game.use_potion()
			_close_overlay()
			sfx.play("good")
			_flash(W, 0.25)
			_refresh_hud()
			Game.save_run()
			g_desc.text += "\n[color=%s]薬瓶を飲んだ。肉体 +%d[/color]" % [_hex(W), h])
		_button(c, "閉じる", Vector2(168, 128), Vector2(152, 40), func(): _close_overlay())
	else:
		_button(c, "閉じる", Vector2(88, 128), Vector2(152, 40), func(): _close_overlay())


## Black floor card ("地下 N 階"). The next event's image is swapped in while the
## card fully covers the screen, so the previous still never flashes.
func _floor_card(then: Callable) -> void:
	busy = true
	var card := ColorRect.new()
	card.color = K
	card.size = Vector2(SW, view_h)
	card.z_index = 40
	add_child(card)
	_clear_event_view()
	var gate: bool = Game.event.has("fixed")
	var cy := _snap(view_h / 2.0) - 24
	var l := _label(card, "地下 %d 階" % Game.floor_n, Vector2(0, cy), Vector2(SW, 32), FS_L, R if gate else W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var chapter := ""
	if not Game.endless and Game.CHAPTERS.has(Game.floor_n):
		chapter = Game.CHAPTERS[Game.floor_n]
		_label(card, chapter, Vector2(0, cy - 48), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	if gate:
		_label(card, "― 門 ―" if Game.floor_n < 100 or Game.endless else "― 最深部 ―", Vector2(0, cy + 40), Vector2(SW, 24), FS, DR, HORIZONTAL_ALIGNMENT_CENTER)
		sfx.play("bell")
	else:
		sfx.play("step")
	l.modulate.a = 0
	var tw := create_tween()
	tw.tween_property(l, "modulate:a", 1.0, 0.25)
	tw.tween_interval(1.1 if gate else (1.5 if chapter != "" else 0.55))
	tw.tween_property(card, "modulate:a", 0.0, 0.3)
	tw.tween_callback(func():
		card.queue_free()
		busy = false
		then.call())


func _clear_event_view() -> void:
	g_res.modulate.a = 0.0
	g_res.texture = null
	g_img.modulate.a = 0.0
	g_img.texture = _tex(Game.event["id"])
	g_title.text = ""
	g_desc.text = ""
	for c in g_choices.get_children():
		c.queue_free()


func _game_music() -> void:
	var e: Dictionary = Game.event
	var n := "upper"
	if e.has("fixed") and int(e["fixed"]) < 100:
		n = "gate"
	elif Game.floor_n >= 75:
		n = "abyss"
	elif Game.floor_n >= 50:
		n = "deep"
	music.play(n, 2.5)
	music.lullaby(e["id"] in LULLABY_EVENTS)


func _present_event() -> void:
	var e: Dictionary = Game.event
	_game_music()
	g_res.modulate.a = 0.0
	g_res.texture = null
	g_img.texture = _tex(e["id"])
	g_img.modulate.a = 0.0
	create_tween().tween_property(g_img, "modulate:a", 1.0, 0.4)
	g_title.text = e["t"]
	g_title.add_theme_color_override("font_color", R if e.has("fixed") else W)
	_set_fit(g_desc, Game.event_text())
	_typewrite()
	_build_choices()


func _typewrite() -> void:
	g_desc.visible_ratio = 0.0
	var n := g_desc.get_total_character_count()
	create_tween().tween_property(g_desc, "visible_ratio", 1.0, clampf(n * 0.018, 0.2, 2.0))


## Compact bbcode summary of a result, scaled to the current floor (for previews).
func _effect_text(r: Dictionary, tint := "") -> String:
	var parts := []
	var fx: bool = r.get("fixed", false)
	for st in Game.STATS:
		if r.has("m" + st):
			var mv := int(r["m" + st])
			parts.append("[color=%s]最大%s%+d[/color]" % [_hex(R if mv < 0 else W), Game.STAT_NAME[st], mv])
		if r.has(st) and int(r[st]) != 0:
			var d := Game.sv(int(r[st]), fx)
			parts.append("[color=%s]%s%+d[/color]" % [_hex(R if d < 0 else W), Game.STAT_NAME[st], d])
	if r.has("g") and int(r["g"]) != 0:
		var g := Game.sv(int(r["g"]), fx)
		parts.append("[color=%s]金貨%+d[/color]" % [_hex(R if g < 0 else W), g])
	for f in r.get("set", []):
		if Game.ITEMS.has(f) and not (Game.ITEMS[f].get("unique", false) and Game.flags.has(f)):
			parts.append("[color=%s]〈%s〉[/color]" % [_hex(R if Game.ITEMS[f].get("bad", false) else W), Game.ITEMS[f]["name"]])
	for f in r.get("clr", []):
		if Game.ITEMS.has(f) and Game.flags.has(f):
			parts.append("〈%s〉喪失" % Game.ITEMS[f]["name"])
	var sk := int(r.get("skip", 0))
	if sk > 0:
		parts.append("[color=%s]近道[/color]" % _hex(R))
	elif sk < 0:
		parts.append("[color=%s]後退[/color]" % _hex(R))
	if parts.is_empty():
		parts = ["変化なし"]
	var t := " ".join(parts)
	if tint != "":
		# one colour for the whole outcome: strip per-value colours
		var re := RegEx.new()
		re.compile("\\[/?color[^\\]]*\\]")
		t = "[color=%s]%s[/color]" % [tint, re.sub(t, "", true)]
	return t


## Preview of already-seen outcomes for a choice ("" if none seen yet).
func _preview(c: Dictionary) -> String:
	if c.has("chk"):
		var ok := Game.is_known(c, "ok")
		var ng := Game.is_known(c, "ng")
		if not ok and not ng:
			return ""
		var a := "[color=%s]成功→[/color]%s" % [_hex(W), _effect_text(c["ok"], _hex(W)) if ok else "[color=%s]？[/color]" % _hex(W)]
		var b := "[color=%s]失敗→[/color]%s" % [_hex(R), _effect_text(c["ng"], _hex(R)) if ng else "[color=%s]？[/color]" % _hex(R)]
		return a + "　　" + b
	if Game.is_known(c, "r"):
		return "結果→" + _effect_text(c["r"])
	return ""


func _build_choices() -> void:
	for c in g_choices.get_children():
		c.queue_free()
	for info in Game.visible_choices():
		var c: Dictionary = info["c"]
		var b := Button.new()
		b.custom_minimum_size = Vector2(344, 56)
		b.clip_contents = true
		b.disabled = not info["enabled"]
		g_choices.add_child(b)
		var en: bool = info["enabled"]
		var col: Color = W if en else WD
		var l1 := _label(b, c["t"], Vector2(8, 3), Vector2(328, 20), FS, col, HORIZONTAL_ALIGNMENT_LEFT, true)
		l1.mouse_filter = Control.MOUSE_FILTER_IGNORE
		var tag := ""
		var tagcol := LG
		if info["chance"] >= 0:
			tag = "［%s判定 成功率 %d%%］" % [Game.STAT_NAME[c["chk"]], roundi(info["chance"] * 100)]
			if info["chance"] < 0.35:
				tagcol = R
		if info["tag"] != "":
			tag = info["tag"] + (" " + tag if tag != "" else "")
			if info["locked"]:
				tag = info["tag"] + " が必要"
			tagcol = R
		var y := 22
		if tag != "":
			var l2 := _label(b, tag, Vector2(8, y), Vector2(0, 16), FS_S, tagcol if en else DG)
			l2.mouse_filter = Control.MOUSE_FILTER_IGNORE
			y += 15
		var pv := _preview(c) if not info["locked"] else ""
		if pv != "":
			var r := RichTextLabel.new()
			r.bbcode_enabled = true
			r.autowrap_mode = TextServer.AUTOWRAP_OFF
			r.scroll_active = false
			r.position = Vector2(8, y)
			r.size = Vector2(328, 16)
			r.mouse_filter = Control.MOUSE_FILTER_IGNORE
			_rich_size(r, FS_S)
			r.text = pv
			if not en:
				r.modulate.a = 0.45
			b.add_child(r)
		b.pressed.connect(func(): _choose(c))


func _choose(c: Dictionary) -> void:
	if busy:
		return
	busy = true
	sfx.play("click")
	var old_floor := Game.floor_n
	var res := Game.resolve(c)
	var summary := {}
	if res.has("end"):
		Game.clear_run()
		summary = Game.end_run(true)
	elif res.get("retire", false):
		Game.clear_run()
		summary = Game.end_run(false, true)
	elif res["dead"]:
		Game.clear_run()
		summary = Game.end_run(false)
	else:
		Game.advance(res["skip"])
		Game.save_run()
	pending = {"res": res, "summary": summary, "old_floor": old_floor}
	_show_result(res)
	busy = false


func _show_result(res: Dictionary) -> void:
	var t := ""
	if res["check"] != "":
		var nm: String = Game.STAT_NAME[res["check"]]
		if res["success"]:
			t += "[color=%s]◆ %s判定 成功[/color]\n" % [_hex(W), nm]
		else:
			t += "[color=%s]◆ %s判定 失敗[/color]\n" % [_hex(R), nm]
	t += res["text"]
	var parts := []
	var hurt := false
	for st in Game.STATS:
		if res.has("max_" + st):
			var mv: int = res["max_" + st]
			parts.append("[color=%s]最大%s%+d[/color]" % [_hex(R if mv < 0 else W), Game.STAT_NAME[st], mv])
		if res["deltas"].has(st):
			var d: int = res["deltas"][st]
			if d < 0:
				hurt = true
			parts.append("[color=%s]%s%+d[/color]" % [_hex(R if d < 0 else W), Game.STAT_NAME[st], d])
	if res.has("gold") and res["gold"] != 0:
		parts.append("[color=%s]金貨%+d[/color]" % [_hex(R if res["gold"] < 0 else W), res["gold"]])
	for f in res["gained"]:
		var n := Game.item_count(f)
		parts.append("[color=%s]〈%s〉を得た%s[/color]" % [_hex(R if Game.ITEMS.get(f, {}).get("bad", false) else W), Game.ITEMS.get(f, {"name": f})["name"], "（×%d）" % n if n > 1 else ""])
	for f in res["lost"]:
		parts.append("〈%s〉を失った" % Game.ITEMS.get(f, {"name": f})["name"])
	if res["skip"] > 0:
		parts.append("[color=%s]近道を見つけた[/color]" % _hex(R))
	elif res["skip"] < 0:
		parts.append("[color=%s]上の階へ戻された[/color]" % _hex(R))
	if not parts.is_empty():
		t += "\n" + "　".join(parts)
	if res.get("amulet", false):
		t += "\n[color=%s]赤いお守りがほどけ、死を免れた！[/color]" % _hex(R)
	if res.has("checkpoint"):
		t += "\n[color=%s]◆ 次回から地下%d階から潜れるようになった[/color]" % [_hex(R), int(res["checkpoint"]) + 1]
	_set_fit(g_desc, t)
	_typewrite()
	var rt := _res_tex(res.get("key", ""))
	if rt:
		g_res.texture = rt
		g_res.modulate.a = 0.0
		create_tween().tween_property(g_res, "modulate:a", 1.0, 0.35)
	_refresh_hud()
	# the floor label still shows the floor the event happened on
	g_floor.text = "B%dF" % pending["old_floor"]
	if res.get("dead", false):
		sfx.play("death")
		_flash(R, 0.6)
		_shake()
	elif hurt:
		sfx.play("hurt")
		_flash(R, 0.3)
		_shake()
	elif res["check"] != "" and res["success"]:
		sfx.play("good")
	for c in g_choices.get_children():
		c.queue_free()
	var label := "さらに深く ▼"
	if res.has("end"):
		label = "……"
	elif res.get("retire", false):
		label = "地上へ ▲"
	elif res.get("dead", false):
		label = "力尽きた……"
	var b := Button.new()
	b.custom_minimum_size = Vector2(344, 56)
	b.text = label
	b.add_theme_font_override("font", font_b)
	g_choices.add_child(b)
	b.pressed.connect(_after_result)


func _after_result() -> void:
	if busy:
		return
	sfx.play("click")
	var res: Dictionary = pending["res"]
	if res.has("end"):
		show_ending(res, pending["summary"])
	elif res.get("retire", false):
		show_gameover(pending["summary"], res)
	elif res.get("dead", false):
		show_gameover(pending["summary"], res)
	else:
		_floor_card(func(): _present_event())
		_refresh_hud(false)


# ================================================================ end screens
func show_gameover(sum: Dictionary, _res := {}) -> void:
	var s := _new_screen("GameOver")
	music.lullaby(false)
	music.play("ending" if sum["cleared"] else ("title" if sum.get("retired", false) else "gameover"), 0.8)
	if sum["cleared"]:
		_image(s, "clear", Vector2(8, 16))
		_label(s, "迷宮踏破", Vector2(0, 232), Vector2(SW, 32), FS_L, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	elif sum.get("retired", false):
		_image(s, "clear", Vector2(8, 16))
		_label(s, "地下 %d 階から帰還した" % sum["score"], Vector2(0, 232), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	else:
		_image(s, "gameover", Vector2(8, 16))
		_label(s, "地下 %d 階で力尽きた" % sum["score"], Vector2(0, 232), Vector2(SW, 32), FS_L, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	var cause := ""
	if not sum["cleared"] and not sum.get("retired", false):
		for st in Game.STATS:
			if int(Game.cur[st]) <= 0:
				cause = {"b": "肉体が限界を迎えた", "m": "精神が闇に呑まれた", "f": "運命に見放された"}[st]
				break
	_label(s, cause, Vector2(0, 264), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	var rows := [["深さの報酬", str(sum["depth_coins"]), W], ["残った金貨", str(sum["gold"]), W]]
	if sum["bonus"] > 0:
		rows.append(["踏破ボーナス", str(sum["bonus"]), W])
	if sum.get("start", 1) > 1:
		rows.insert(0, ["開始", "地下%d階" % sum["start"], W])
	if sum.get("ad_bonus", 0) > 0:
		rows.append(["広告ボーナス", "+%d" % sum["ad_bonus"], W])
	rows.append(["得た魂の欠片", "+%d" % (int(sum["coins"]) + int(sum.get("ad_bonus", 0))), R])
	rows.append(["魂の欠片 合計", str(Game.save["coins"]), W])
	var y := 288
	for row in rows:
		_label(s, row[0], Vector2(56, y), Vector2(152, 24), FS, row[2] if row[2] == R else LG, HORIZONTAL_ALIGNMENT_LEFT, row[2] == R)
		_label(s, row[1], Vector2(192, y), Vector2(112, 24), FS, row[2], HORIZONTAL_ALIGNMENT_RIGHT, row[2] == R)
		y += 24
	var ad_ok: bool = int(sum["coins"]) > 0 and not sum.get("ad_used", false)
	var bottom := 488 if ad_ok else 536
	var r := _rich(s, Vector2(16, y + 8), Vector2(328, bottom - y - 8))
	if ad_ok:
		var ab := _button(s, "▶ 広告を見て魂の欠片を2倍（+%d）" % int(sum["coins"]), Vector2(8, 496), Vector2(344, 40), func():
			Ads.show_rewarded(self, func():
				Game.grant_ad_bonus(int(sum["coins"]))
				sum["ad_bonus"] = int(sum["coins"])
				sum["ad_used"] = true
				sfx.play("good"),
				func(): show_gameover(sum)), FS_S)
		ab.add_theme_color_override("font_color", R)
		ab.add_theme_color_override("font_hover_color", R)
		ab.disabled = not Ads.is_rewarded_ready()
	var t := ""
	if sum["new_best"]:
		t += "[center][color=%s]★ 最高記録更新！[/color][/center]\n" % _hex(R)
	if not sum["newly"].is_empty():
		t += "[color=%s]新たな出来事が %d 件解放された[/color]\n" % [_hex(R), sum["newly"].size()]
		var names := []
		for id in sum["newly"].slice(0, 3):
			names.append("・" + _tease(Game.by_id[id]["t"]))
		t += "\n".join(names)
		if sum["newly"].size() > 3:
			t += "\n　ほか %d 件" % (sum["newly"].size() - 3)
	else:
		var nxt := Game.next_unlock_total()
		if nxt > 0:
			t += "[center]次の解放まで あと累計 %d 階[/center]" % (nxt - int(Game.save["total"]))
	_set_fit(r, t)
	_button(s, "強化", Vector2(8, 552), Vector2(104, 40), show_shop)
	_button(s, "再び潜る", Vector2(128, 552), Vector2(104, 40), func(): _start(Game.endless))
	_button(s, "タイトル", Vector2(248, 552), Vector2(104, 40), show_title)
	if sum["first_clear"]:
		_label(s, "無限迷宮（エンドレス）が解放された！", Vector2(0, 600), Vector2(SW, 24), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	_layout(s, 0, 96)


func _tease(title: String) -> String:
	# hide half the characters of a newly unlocked event's name
	var out := ""
	for i in title.length():
		out += title[i] if i % 2 == 0 else "？"
	return out


func show_ending(res: Dictionary, sum: Dictionary) -> void:
	var s := _new_screen("Ending")
	music.lullaby(false)
	music.play("ending", 2.0)
	sfx.play("bell")
	var still := _image(s, "clear", Vector2(8, 16))
	var et := _res_tex(res.get("key", ""))
	if et:
		still.texture = et
	var nm: String = Game.ENDINGS.get(res["end"], "")
	_label(s, "ENDING", Vector2(0, 232), Vector2(SW, 24), FS_S, DR, HORIZONTAL_ALIGNMENT_CENTER)
	_label(s, "「%s」" % nm, Vector2(0, 256), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var r := _rich(s, Vector2(16, 296), Vector2(328, 264))
	_set_fit(r, res["text"] + "\n\n[color=%s]エンディング %d / %d[/color]" % [_hex(R), Game.save["endings"].size(), Game.ENDINGS.size()])
	r.visible_ratio = 0
	create_tween().tween_property(r, "visible_ratio", 1.0, 3.0)
	_button(s, "次へ", Vector2(88, 584), Vector2(184, 40), func():
		show_epilogue(Game.epilogue(res["end"]), func(): show_gameover(sum, res)))
	_layout(s, 0, 64)


func show_epilogue(text: String, then: Callable) -> void:
	var s := _new_screen("Epilogue")
	_label(s, "後日談", Vector2(0, 16), Vector2(SW, 32), FS_L, LG, HORIZONTAL_ALIGNMENT_CENTER, true)
	var r := _rich(s, Vector2(24, 160), Vector2(312, 336))
	_set_fit(r, text)
	r.visible_ratio = 0
	create_tween().tween_property(r, "visible_ratio", 1.0, 4.0)
	_button(s, "次へ", Vector2(88, 584), Vector2(184, 40), then)
	_layout(s, 56, 64)


# ================================================================ journal
func show_journal(ch := 1) -> void:
	var s := _new_screen("Journal")
	_music_menu()
	var jc: Array = Game.journal_count()
	_label(s, "手記", Vector2(0, 8), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "真相の断片 %d / %d" % [jc[0], jc[1]], Vector2(0, 40), Vector2(SW, 24), FS, R, HORIZONTAL_ALIGNMENT_CENTER)
	var names := {1: "第一章　降下", 2: "第二章　弔い", 3: "第三章　引き離された夜", 4: "第四章　子守唄"}
	var t := "[color=%s]%s[/color]\n\n" % [_hex(LG), names[ch]]
	for j in Game.JOURNAL:
		if int(j["ch"]) != ch:
			continue
		if Game.save["meta"].has(j["meta"]):
			t += "・%s\n\n" % j["t"]
		else:
			t += "[color=%s]・……………………[/color]\n\n" % _hex(DG)
	var r := _rich(s, Vector2(16, 72), Vector2(328, 448))
	_set_fit(r, t)
	_label(s, "%d / 4" % ch, Vector2(0, 536), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	var prev := _button(s, "◀ 前", Vector2(8, 528), Vector2(96, 40), func(): show_journal(ch - 1))
	prev.disabled = ch == 1
	var nxt := _button(s, "次 ▶", Vector2(256, 528), Vector2(96, 40), func(): show_journal(ch + 1))
	nxt.disabled = ch == 4
	_button(s, "戻る", Vector2(88, 584), Vector2(184, 40), show_title)
	_layout(s, 64, 112)


# ================================================================ collection
var coll_page := 0
const PER_PAGE := 18


func show_collection(page := -1) -> void:
	if page >= 0:
		coll_page = page
	var s := _new_screen("Collection")
	_music_menu()
	var seen: Array = Game.save["seen"]
	var unl := Game.unlocked_ids()
	_label(s, "図鑑", Vector2(0, 8), Vector2(SW, 32), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "発見 %d / %d　解放 %d / %d" % [seen.size(), Game.events.size(), unl.size(), Game.events.size()],
		Vector2(0, 40), Vector2(SW, 24), FS, R, HORIZONTAL_ALIGNMENT_CENTER)
	var list: Array = Game.events.duplicate()
	list.sort_custom(func(a, b): return _sort_key(a) < _sort_key(b))
	var pages := int(ceil(list.size() / float(PER_PAGE)))
	coll_page = clampi(coll_page, 0, pages - 1)
	var y := 64
	for i in range(coll_page * PER_PAGE, mini(list.size(), (coll_page + 1) * PER_PAGE)):
		var e: Dictionary = list[i]
		var b := Button.new()
		b.position = Vector2(8, y)
		b.size = Vector2(344, 24)
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		var st := _sb(K, DG)
		st.content_margin_top = 1
		st.content_margin_bottom = 1
		b.add_theme_stylebox_override("disabled", st)
		var sk := _skin("btn_normal", 2, 3)
		b.add_theme_stylebox_override("normal", sk)
		b.add_theme_stylebox_override("hover", sk)
		b.add_theme_stylebox_override("pressed", _skin("btn_pressed", 3, 2))
		var no := "%03d " % (i + 1)
		if seen.has(e["id"]):
			b.text = no + e["t"]
			if e.has("fixed"):
				b.add_theme_color_override("font_color", R)
				b.add_theme_color_override("font_hover_color", R)
			b.pressed.connect(func(): _collection_detail(e))
		elif unl.has(e["id"]):
			b.text = no + "？？？？（未発見）"
			b.disabled = true
		else:
			b.text = no + "―― 未解放 ――"
			b.disabled = true
		s.add_child(b)
		y += 24
	_label(s, "%d / %d" % [coll_page + 1, pages], Vector2(0, 536), Vector2(SW, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
	var prev := _button(s, "◀ 前", Vector2(8, 528), Vector2(96, 40), func(): show_collection(coll_page - 1))
	prev.disabled = coll_page == 0
	var nxt := _button(s, "次 ▶", Vector2(256, 528), Vector2(96, 40), func(): show_collection(coll_page + 1))
	nxt.disabled = coll_page >= pages - 1
	_button(s, "結末 %d/%d" % [Game.save["endings"].size(), Game.ENDINGS.size()], Vector2(8, 584), Vector2(168, 40), _endings_popup)
	_button(s, "戻る", Vector2(184, 584), Vector2(168, 40), show_title)
	_layout(s, 64, 112)


func _endings_popup() -> void:
	var p := _overlay_panel(264)
	var c := Control.new()
	p.add_child(c)
	_label(c, "到達した結末", Vector2(8, 8), Vector2(312, 24), FS, R, HORIZONTAL_ALIGNMENT_LEFT, true)
	var y := 40
	for en in Game.ENDINGS:
		var got: bool = Game.save["endings"].has(en)
		_label(c, ("「%s」" % Game.ENDINGS[en]) if got else "「？？？？」", Vector2(8, y), Vector2(312, 24), FS, W if got else DG)
		y += 24
	_button(c, "閉じる", Vector2(88, 216), Vector2(152, 40), func(): _close_overlay())


func _sort_key(e: Dictionary) -> float:
	if e.has("fixed"):
		return float(e["fixed"]) - 0.5
	return float(e.get("min", 1)) + float(int(str(e["id"]).substr(1))) * 0.001


func _collection_detail(e: Dictionary, page := 0) -> void:
	sfx.play("click")
	# page 0 = the event itself, then every outcome the player has seen
	var pages := [{"tex": _tex(e["id"]), "title": e["t"], "text": e["d"]}]
	for ci in e["c"].size():
		var ch: Dictionary = e["c"][ci]
		for br in ["r", "ok", "ng"]:
			if ch.has(br) and Game.save["known"].has("%s:%d:%s" % [e["id"], ci, br]):
				var tag: String = {"r": "", "ok": "（成功）", "ng": "（失敗）"}[br]
				pages.append({"tex": _res_tex("%s_%d_%s" % [e["id"], ci, br]), "title": "▶ " + ch["t"] + tag, "text": ch[br]["d"]})
	page = clampi(page, 0, pages.size() - 1)
	var pg: Dictionary = pages[page]
	var p := _overlay_panel(496, 344)
	var c := Control.new()
	p.add_child(c)
	var tr := TextureRect.new()
	tr.texture = pg["tex"]
	tr.position = Vector2(4, 4)
	tr.size = Vector2(336, 200)
	tr.stretch_mode = TextureRect.STRETCH_SCALE
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	c.add_child(tr)
	var tl := _label(c, pg["title"], Vector2(8, 216), Vector2(328, 24), FS, R if e.has("fixed") or page > 0 else W, HORIZONTAL_ALIGNMENT_LEFT, true)
	tl.clip_text = true
	var r := _rich(c, Vector2(8, 240), Vector2(328, 152))
	_set_fit(r, pg["text"])
	if pages.size() > 1:
		_label(c, "%d / %d" % [page + 1, pages.size()], Vector2(120, 408), Vector2(104, 24), FS, LG, HORIZONTAL_ALIGNMENT_CENTER)
		var pv := _button(c, "◀", Vector2(8, 400), Vector2(72, 40), func(): _collection_detail(e, page - 1))
		pv.disabled = page == 0
		var nx := _button(c, "▶", Vector2(264, 400), Vector2(72, 40), func(): _collection_detail(e, page + 1))
		nx.disabled = page >= pages.size() - 1
	else:
		_label(c, "結果はまだ見ていない", Vector2(8, 408), Vector2(328, 24), FS_S, DG, HORIZONTAL_ALIGNMENT_CENTER)
	_button(c, "閉じる", Vector2(96, 448), Vector2(152, 40), func(): _close_overlay())
