extends Control
## All UI screens, built in code for a fixed 360x640 pixel-art canvas.
## The window uses the "canvas_items" stretch mode so text renders at the
## device resolution (crisp at 14/16px) while the art stays nearest-filtered.

const K := Color(0.055, 0.047, 0.055)
const W := Color(0.91, 0.886, 0.83)
const R := Color(0.77, 0.11, 0.157)
const WD := Color(0.91, 0.886, 0.83, 0.38)
const SW := 360
const SH := 640
const FS := 16      # body text size
const FS_S := 14    # small text size
const FS_L := 24    # headings

var font: FontFile
var font_b: FontFile
var screen: Control
var overlay: Control
var flash: ColorRect
var sfx: Sfx

# game-screen widgets
var g_floor: Label
var g_gold: Label
var g_bars := {}
var g_img: TextureRect
var g_title: Label
var g_desc: RichTextLabel
var g_items: HFlowContainer
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
		var wc := Color(0.91, 0.886, 0.83)
		var rc := Color(0.77, 0.11, 0.157)
		var low: bool = value <= maxi(1, int(max_value * 0.3))
		draw_string(fnt, Vector2(0, 14), label, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, wc)
		draw_string(fnt, Vector2(0, 14), "%d/%d" % [value, max_value], HORIZONTAL_ALIGNMENT_RIGHT, size.x, 16, rc if low else wc)
		var by := 19.0
		draw_rect(Rect2(0, by, size.x, 9), rc if low else wc, false, 1.0)
		var inner := size.x - 4
		var mxv := float(maxi(1, max_value))
		var ws := floorf(inner * clampf(shown / mxv, 0, 1))
		var wg := floorf(inner * clampf(ghost / mxv, 0, 1))
		if ws > 0:
			draw_rect(Rect2(2, by + 2, ws, 5), wc, true)
		if wg > ws:
			draw_rect(Rect2(2 + ws, by + 2, wg - ws, 5), rc, true)


class Sfx extends Node:
	## Tiny procedural sound effects (no audio assets needed).
	var players := {}

	func _ready() -> void:
		players["click"] = _make(_tone(880, 0.03, 0.25))
		players["hurt"] = _make(_noise(0.18, 0.35))
		players["good"] = _make(_sweep(440, 880, 0.12, 0.2))
		players["step"] = _make(_sweep(220, 70, 0.35, 0.35))
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
	var bg := ColorRect.new()
	bg.color = K
	bg.size = Vector2(SW, SH)
	add_child(bg)
	sfx = Sfx.new()
	add_child(sfx)
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
	t.set_stylebox("normal", "Button", _sb(K, W))
	t.set_stylebox("hover", "Button", _sb(K, W))
	t.set_stylebox("pressed", "Button", _sb(K, R, 2))
	t.set_stylebox("hover_pressed", "Button", _sb(K, R, 2))
	t.set_stylebox("disabled", "Button", _sb(K, WD))
	t.set_stylebox("focus", "Button", StyleBoxEmpty.new())
	t.set_color("font_color", "Button", W)
	t.set_color("font_hover_color", "Button", W)
	t.set_color("font_pressed_color", "Button", R)
	t.set_color("font_hover_pressed_color", "Button", R)
	t.set_color("font_focus_color", "Button", W)
	t.set_color("font_disabled_color", "Button", WD)
	t.set_stylebox("panel", "PanelContainer", _sb(K, W))
	theme = t


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


# ================================================================ helpers
func _new_screen(nm: String) -> Control:
	_close_overlay()
	if screen:
		screen.queue_free()
	screen = Control.new()
	screen.name = nm
	screen.size = Vector2(SW, SH)
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


func _image(parent: Node, id: String, pos: Vector2) -> TextureRect:
	var frame := Panel.new()
	frame.position = pos - Vector2(1, 1)
	frame.size = Vector2(338, 202)
	frame.add_theme_stylebox_override("panel", _sb(K, W))
	frame.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(frame)
	var tr := TextureRect.new()
	tr.texture = _tex(id)
	tr.position = Vector2(1, 1)
	tr.size = Vector2(336, 200)
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.stretch_mode = TextureRect.STRETCH_SCALE
	tr.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	frame.add_child(tr)
	return tr


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


func _overlay_panel(h: int) -> PanelContainer:
	_close_overlay()
	overlay = Control.new()
	overlay.size = Vector2(SW, SH)
	overlay.z_index = 50
	add_child(overlay)
	var dim := ColorRect.new()
	dim.color = Color(K, 0.85)
	dim.size = Vector2(SW, SH)
	dim.gui_input.connect(func(ev):
		if ev is InputEventMouseButton and ev.pressed:
			_close_overlay())
	overlay.add_child(dim)
	var p := PanelContainer.new()
	p.position = Vector2(16, (SH - h) / 2)
	p.size = Vector2(328, h)
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
	_label(c, msg, Vector2(8, 8), Vector2(304, 100))
	_button(c, "はい", Vector2(8, 124), Vector2(144, 38), func():
		_close_overlay()
		yes.call())
	_button(c, "いいえ", Vector2(168, 124), Vector2(144, 38), func(): _close_overlay())


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
func show_title() -> void:
	var s := _new_screen("Title")
	_image(s, "title", Vector2(12, 24))
	_label(s, "三択ダンジョン", Vector2(0, 234), Vector2(SW, 30), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "― 地下百階を目指せ ―", Vector2(0, 266), Vector2(SW, 20), FS, R, HORIZONTAL_ALIGNMENT_CENTER)
	var sv: Dictionary = Game.save
	_label(s, "最高到達 B%dF　探索 %d回" % [sv["best"], sv["runs"]], Vector2(0, 294), Vector2(SW, 20), FS, W, HORIZONTAL_ALIGNMENT_CENTER)
	_label(s, "累計 %d階　魂の欠片 %d" % [sv["total"], sv["coins"]], Vector2(0, 314), Vector2(SW, 20), FS, W, HORIZONTAL_ALIGNMENT_CENTER)
	var y := 344
	if Game.has_run():
		var r: Dictionary = sv["run"]
		_button(s, "続きから（%sB%dF）" % ["無限 " if r["endless"] else "", r["floor"]], Vector2(50, y), Vector2(260, 38), func():
			Game.resume_run()
			show_game(true))
		y += 44
	_button(s, "迷宮へ潜る", Vector2(50, y), Vector2(260, 38), func(): _start(false))
	y += 44
	if sv["cleared"]:
		_button(s, "無限迷宮（エンドレス）", Vector2(50, y), Vector2(260, 38), func(): _start(true))
		y += 44
	_button(s, "強化", Vector2(50, y), Vector2(126, 38), show_shop)
	_button(s, "図鑑", Vector2(184, y), Vector2(126, 38), show_collection)
	y += 44
	_button(s, "遊び方", Vector2(50, y), Vector2(126, 38), show_help)
	_button(s, "データ消去", Vector2(184, y), Vector2(126, 38), func():
		_confirm("全てのセーブデータを消去しますか？\nこの操作は取り消せません。", func():
			Game.reset_save()
			show_title()))
	if sv["cleared"]:
		_label(s, "★ 踏破済み　無限迷宮 最高 B%dF" % sv["best_endless"], Vector2(0, 596), Vector2(SW, 18), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER)
	_label(s, "v1.1.1　Font: PixelMplus (M+ FONTS)", Vector2(0, 618), Vector2(SW, 16), 12, WD, HORIZONTAL_ALIGNMENT_CENTER)


func _start(is_endless: bool) -> void:
	if Game.has_run():
		_confirm("中断中の探索は失われます。\n新しく潜りますか？", func(): _begin(is_endless))
	else:
		_begin(is_endless)


func _begin(is_endless: bool) -> void:
	Game.start_run(is_endless)
	Game.save_run()
	show_game(true)


# ================================================================ help
func show_help(page := 0) -> void:
	var s := _new_screen("Help")
	_label(s, "遊び方", Vector2(0, 12), Vector2(SW, 30), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var h := _hex(R)
	var pages := [
		"[color=%s]■ 目的[/color]\n地下百階の迷宮を一階ずつ降り、最深部を目指す。\n\n" % h +
		"[color=%s]■ 三つの力[/color]\n[b]肉体[/b]…傷や戦いに耐える力\n[b]精神[/b]…恐怖や狂気に耐える力\n[b]運命[/b]…幸運と罠を避ける力\nどれか一つでも0になると力尽きる。\n\n" % h +
		"[color=%s]■ 選択[/color]\n各階で出来事が起き、三つの選択肢から一つを選ぶ。［判定］のついた選択は、表示された確率で成否が決まる。確率は今の能力値と所持品で上下する。深く潜るほど出来事は苛烈になる。" % h,
		"[color=%s]■ 結果の記憶[/color]\n一度見た結果は、選択肢に「成功→肉体-2」のように表示される。\n\n" % h +
		"[color=%s]■ 所持品[/color]\n〈 〉は所持品が必要な選択肢。所持品をタップすると効果がわかる。薬瓶はタップで使える。\n\n" % h +
		"[color=%s]■ 死と継承[/color]\n探索中に拾う金貨は、その探索の中での支払いに使う。力尽きると、到達した深さと残った金貨が「魂の欠片」に換わる。魂の欠片で初期能力を強化できる。累計で潜った階数が増えるほど、新たな出来事が解放される。\n\n" % h +
		"[color=%s]■ 門番[/color]\n地下25・50・75階には門番が待つ。そして地下100階には――。" % h,
	]
	var r := _rich(s, Vector2(16, 52), Vector2(328, 470))
	_set_fit(r, pages[page])
	_label(s, "%d / %d" % [page + 1, pages.size()], Vector2(0, 538), Vector2(SW, 20), FS, W, HORIZONTAL_ALIGNMENT_CENTER)
	var prev := _button(s, "◀ 前", Vector2(16, 532), Vector2(100, 34), func(): show_help(page - 1))
	prev.disabled = page == 0
	var nxt := _button(s, "次 ▶", Vector2(244, 532), Vector2(100, 34), func(): show_help(page + 1))
	nxt.disabled = page >= pages.size() - 1
	_button(s, "戻る", Vector2(90, 584), Vector2(180, 38), show_title)


# ================================================================ shop
func show_shop() -> void:
	var s := _new_screen("Shop")
	_label(s, "強化", Vector2(0, 10), Vector2(SW, 30), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "魂の欠片 %d" % Game.save["coins"], Vector2(0, 44), Vector2(SW, 20), FS, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	var desc := {"b": "傷や戦いに耐える力。", "m": "恐怖や狂気に耐える力。", "f": "幸運と、罠を避ける力。"}
	var y := 72
	for st in Game.STATS:
		var box := Panel.new()
		box.position = Vector2(12, y)
		box.size = Vector2(336, 120)
		box.add_theme_stylebox_override("panel", _sb(K, W))
		s.add_child(box)
		var lv: int = Game.save["lv"][st]
		_label(box, "%s　Lv.%d" % [Game.STAT_NAME[st], lv], Vector2(10, 6), Vector2(316, 20), FS, W, HORIZONTAL_ALIGNMENT_LEFT, true)
		_label(box, desc[st], Vector2(10, 28), Vector2(316, 20))
		var now := Game.stat_max_base(st)
		_label(box, "初期値 %d → %d" % [now, now + int(Game.B["stat_per_level"])], Vector2(10, 50), Vector2(316, 20))
		var cost := Game.upgrade_cost(st)
		var b := _button(box, "強化する（魂の欠片 %d）" % cost, Vector2(10, 76), Vector2(316, 36), func():
			if Game.buy_upgrade(st):
				sfx.play("good")
				show_shop())
		b.disabled = int(Game.save["coins"]) < cost
		y += 128
	var nxt := Game.next_unlock_total()
	var hint := "累計 %d階 潜ると新たな出来事が解放される（現在 %d階）" % [nxt, Game.save["total"]] if nxt > 0 else "全ての出来事が解放されている"
	_label(s, hint, Vector2(16, 460), Vector2(328, 40), FS_S, W, HORIZONTAL_ALIGNMENT_CENTER)
	_button(s, "迷宮へ潜る", Vector2(50, 512), Vector2(260, 38), func(): _start(false))
	_button(s, "戻る", Vector2(50, 560), Vector2(260, 38), show_title)


# ================================================================ game
func show_game(intro := false) -> void:
	var s := _new_screen("Game")
	g_floor = _label(s, "", Vector2(12, 2), Vector2(200, 28), FS_L, W, HORIZONTAL_ALIGNMENT_LEFT, true)
	g_gold = _label(s, "", Vector2(160, 8), Vector2(188, 20), FS, W, HORIZONTAL_ALIGNMENT_RIGHT)
	g_bars.clear()
	for i in 3:
		var st: String = Game.STATS[i]
		var b := StatBar.new()
		b.fnt = font
		b.label = Game.STAT_NAME[st]
		b.position = Vector2(12 + i * 116, 32)
		b.size = Vector2(104, 30)
		b.mouse_filter = Control.MOUSE_FILTER_IGNORE
		s.add_child(b)
		g_bars[st] = b
	g_img = _image(s, Game.event["id"], Vector2(12, 67))
	g_title = _label(s, "", Vector2(12, 271), Vector2(336, 20), FS, W, HORIZONTAL_ALIGNMENT_LEFT, true)
	g_desc = _rich(s, Vector2(12, 292), Vector2(336, 120))
	g_desc.gui_input.connect(func(ev):
		if ev is InputEventMouseButton and ev.pressed:
			g_desc.visible_ratio = 1.0)
	g_items = HFlowContainer.new()
	g_items.position = Vector2(12, 414)
	g_items.size = Vector2(336, 22)
	g_items.add_theme_constant_override("h_separation", 4)
	s.add_child(g_items)
	g_choices = VBoxContainer.new()
	g_choices.position = Vector2(12, 440)
	g_choices.size = Vector2(336, 194)
	g_choices.add_theme_constant_override("separation", 4)
	s.add_child(g_choices)
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
	for c in g_items.get_children():
		c.queue_free()
	for f in Game.item_list():
		var it: Dictionary = Game.ITEMS[f]
		var b := Button.new()
		b.text = it["name"]
		b.add_theme_font_size_override("font_size", FS_S)
		var bad: bool = it.get("bad", false)
		var st := _sb(K, R if bad else W)
		st.set_content_margin_all(1)
		st.content_margin_left = 4
		st.content_margin_right = 4
		b.add_theme_stylebox_override("normal", st)
		b.add_theme_stylebox_override("hover", st)
		b.add_theme_stylebox_override("pressed", st)
		if bad:
			b.add_theme_color_override("font_color", R)
			b.add_theme_color_override("font_hover_color", R)
		b.pressed.connect(func(): _item_popup(f))
		g_items.add_child(b)


func _item_popup(f: String) -> void:
	sfx.play("click")
	var it: Dictionary = Game.ITEMS[f]
	var p := _overlay_panel(170)
	var c := Control.new()
	p.add_child(c)
	_label(c, it["name"], Vector2(8, 8), Vector2(304, 20), FS, R if it.get("bad", false) else W, HORIZONTAL_ALIGNMENT_LEFT, true)
	_label(c, it["desc"], Vector2(8, 34), Vector2(304, 76))
	if f == "potion" and not busy:
		_button(c, "使う", Vector2(8, 120), Vector2(144, 36), func():
			var h := Game.use_potion()
			_close_overlay()
			sfx.play("good")
			_flash(W, 0.25)
			_refresh_hud()
			Game.save_run()
			g_desc.text += "\n[color=%s]薬瓶を飲んだ。肉体 +%d[/color]" % [_hex(W), h])
		_button(c, "閉じる", Vector2(168, 120), Vector2(144, 36), func(): _close_overlay())
	else:
		_button(c, "閉じる", Vector2(88, 120), Vector2(144, 36), func(): _close_overlay())


## Black floor card ("地下 N 階"). The next event's image is swapped in while the
## card fully covers the screen, so the previous still never flashes.
func _floor_card(then: Callable) -> void:
	busy = true
	var card := ColorRect.new()
	card.color = K
	card.size = Vector2(SW, SH)
	card.z_index = 40
	add_child(card)
	_clear_event_view()
	var gate: bool = Game.event.has("fixed")
	var l := _label(card, "地下 %d 階" % Game.floor_n, Vector2(0, 290), Vector2(SW, 30), FS_L, R if gate else W, HORIZONTAL_ALIGNMENT_CENTER, true)
	if gate:
		_label(card, "― 門 ―" if Game.floor_n < 100 or Game.endless else "― 最深部 ―", Vector2(0, 328), Vector2(SW, 20), FS, R, HORIZONTAL_ALIGNMENT_CENTER)
		sfx.play("bell")
	else:
		sfx.play("step")
	l.modulate.a = 0
	var tw := create_tween()
	tw.tween_property(l, "modulate:a", 1.0, 0.25)
	tw.tween_interval(0.55 if not gate else 1.1)
	tw.tween_property(card, "modulate:a", 0.0, 0.3)
	tw.tween_callback(func():
		card.queue_free()
		busy = false
		then.call())


func _clear_event_view() -> void:
	g_img.modulate.a = 0.0
	g_img.texture = _tex(Game.event["id"])
	g_title.text = ""
	g_desc.text = ""
	for c in g_choices.get_children():
		c.queue_free()


func _present_event() -> void:
	var e: Dictionary = Game.event
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
func _effect_text(r: Dictionary) -> String:
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
		if Game.ITEMS.has(f) and not Game.flags.has(f):
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
		return "変化なし"
	return " ".join(parts)


## Preview of already-seen outcomes for a choice ("" if none seen yet).
func _preview(c: Dictionary) -> String:
	if c.has("chk"):
		var ok := Game.is_known(c, "ok")
		var ng := Game.is_known(c, "ng")
		if not ok and not ng:
			return ""
		return "成功→%s／失敗→%s" % [_effect_text(c["ok"]) if ok else "？", _effect_text(c["ng"]) if ng else "？"]
	if Game.is_known(c, "r"):
		return "結果→" + _effect_text(c["r"])
	return ""


func _build_choices() -> void:
	for c in g_choices.get_children():
		c.queue_free()
	for info in Game.visible_choices():
		var c: Dictionary = info["c"]
		var b := Button.new()
		b.custom_minimum_size = Vector2(336, 62)
		b.clip_contents = true
		b.disabled = not info["enabled"]
		g_choices.add_child(b)
		var en: bool = info["enabled"]
		var col: Color = W if en else WD
		var l1 := _label(b, c["t"], Vector2(8, 5), Vector2(322, 20), FS, col, HORIZONTAL_ALIGNMENT_LEFT, true)
		l1.mouse_filter = Control.MOUSE_FILTER_IGNORE
		var tag := ""
		var tagcol := W
		if info["chance"] >= 0:
			tag = "［%s判定 成功率 %d%%］" % [Game.STAT_NAME[c["chk"]], roundi(info["chance"] * 100)]
			if info["chance"] < 0.35:
				tagcol = R
		if info["tag"] != "":
			tag = info["tag"] + (" " + tag if tag != "" else "")
			if info["locked"]:
				tag = info["tag"] + " が必要"
			tagcol = R
		var y := 25
		if tag != "":
			var l2 := _label(b, tag, Vector2(8, y), Vector2(0, 18), FS_S, tagcol if en else Color(tagcol, 0.45))
			l2.mouse_filter = Control.MOUSE_FILTER_IGNORE
			y += 17
		var pv := _preview(c) if not info["locked"] else ""
		if pv != "":
			var r := RichTextLabel.new()
			r.bbcode_enabled = true
			r.autowrap_mode = TextServer.AUTOWRAP_OFF
			r.scroll_active = false
			r.position = Vector2(8, y)
			r.size = Vector2(322, 18)
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
		parts.append("[color=%s]〈%s〉を得た[/color]" % [_hex(R if Game.ITEMS.get(f, {}).get("bad", false) else W), Game.ITEMS.get(f, {"name": f})["name"]])
	for f in res["lost"]:
		parts.append("〈%s〉を失った" % Game.ITEMS.get(f, {"name": f})["name"])
	if res["skip"] > 0:
		parts.append("[color=%s]近道を見つけた[/color]" % _hex(R))
	elif res["skip"] < 0:
		parts.append("[color=%s]上の階へ戻された[/color]" % _hex(R))
	if not parts.is_empty():
		t += "\n" + "　".join(parts)
	if res.get("amulet", false):
		t += "\n[color=%s]赤い護符が砕け散り、死を免れた！[/color]" % _hex(R)
	_set_fit(g_desc, t)
	_typewrite()
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
	elif res.get("dead", false):
		label = "力尽きた……"
	var b := Button.new()
	b.custom_minimum_size = Vector2(336, 62)
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
	elif res.get("dead", false):
		show_gameover(pending["summary"], res)
	else:
		_floor_card(func(): _present_event())
		_refresh_hud(false)


# ================================================================ end screens
func show_gameover(sum: Dictionary, _res := {}) -> void:
	var s := _new_screen("GameOver")
	if sum["cleared"]:
		_image(s, "clear", Vector2(12, 20))
		_label(s, "迷宮踏破", Vector2(0, 228), Vector2(SW, 30), FS_L, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	else:
		_image(s, "gameover", Vector2(12, 20))
		_label(s, "地下 %d 階で力尽きた" % sum["score"], Vector2(0, 228), Vector2(SW, 30), FS_L, R, HORIZONTAL_ALIGNMENT_CENTER, true)
	var cause := ""
	if not sum["cleared"]:
		for st in Game.STATS:
			if int(Game.cur[st]) <= 0:
				cause = {"b": "肉体が限界を迎えた", "m": "精神が闇に呑まれた", "f": "運命に見放された"}[st]
				break
	_label(s, cause, Vector2(0, 262), Vector2(SW, 20), FS, W, HORIZONTAL_ALIGNMENT_CENTER)
	var rows := [["深さの報酬", str(sum["depth_coins"]), W], ["残った金貨", str(sum["gold"]), W]]
	if sum["bonus"] > 0:
		rows.append(["踏破ボーナス", str(sum["bonus"]), W])
	rows.append(["得た魂の欠片", "+%d" % sum["coins"], R])
	rows.append(["魂の欠片 合計", str(Game.save["coins"]), W])
	var y := 290
	for row in rows:
		_label(s, row[0], Vector2(60, y), Vector2(150, 20), FS, row[2], HORIZONTAL_ALIGNMENT_LEFT, row[2] == R)
		_label(s, row[1], Vector2(190, y), Vector2(110, 20), FS, row[2], HORIZONTAL_ALIGNMENT_RIGHT, row[2] == R)
		y += 21
	var r := _rich(s, Vector2(24, y + 4), Vector2(312, 540 - y - 4))
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
	_button(s, "強化", Vector2(12, 548), Vector2(108, 40), show_shop)
	_button(s, "再び潜る", Vector2(126, 548), Vector2(108, 40), func(): _begin(Game.endless))
	_button(s, "タイトル", Vector2(240, 548), Vector2(108, 40), show_title)
	if sum["first_clear"]:
		_label(s, "無限迷宮（エンドレス）が解放された！", Vector2(0, 600), Vector2(SW, 20), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER, true)


func _tease(title: String) -> String:
	# hide half the characters of a newly unlocked event's name
	var out := ""
	for i in title.length():
		out += title[i] if i % 2 == 0 else "？"
	return out


func show_ending(res: Dictionary, sum: Dictionary) -> void:
	var s := _new_screen("Ending")
	sfx.play("bell")
	_image(s, "clear", Vector2(12, 20))
	var nm: String = Game.ENDINGS.get(res["end"], "")
	_label(s, "ENDING", Vector2(0, 228), Vector2(SW, 20), FS_S, R, HORIZONTAL_ALIGNMENT_CENTER)
	_label(s, "「%s」" % nm, Vector2(0, 248), Vector2(SW, 30), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	var r := _rich(s, Vector2(16, 290), Vector2(328, 260))
	_set_fit(r, res["text"] + "\n\n[color=%s]エンディング %d / %d[/color]" % [_hex(R), Game.save["endings"].size(), Game.ENDINGS.size()])
	r.visible_ratio = 0
	create_tween().tween_property(r, "visible_ratio", 1.0, 3.0)
	_button(s, "次へ", Vector2(90, 576), Vector2(180, 40), func(): show_gameover(sum, res))


# ================================================================ collection
var coll_page := 0
const PER_PAGE := 20


func show_collection(page := -1) -> void:
	if page >= 0:
		coll_page = page
	var s := _new_screen("Collection")
	var seen: Array = Game.save["seen"]
	var unl := Game.unlocked_ids()
	_label(s, "図鑑", Vector2(0, 6), Vector2(SW, 30), FS_L, W, HORIZONTAL_ALIGNMENT_CENTER, true)
	_label(s, "発見 %d / %d　解放 %d / %d" % [seen.size(), Game.events.size(), unl.size(), Game.events.size()],
		Vector2(0, 38), Vector2(SW, 20), FS, R, HORIZONTAL_ALIGNMENT_CENTER)
	var list: Array = Game.events.duplicate()
	list.sort_custom(func(a, b): return _sort_key(a) < _sort_key(b))
	var pages := int(ceil(list.size() / float(PER_PAGE)))
	coll_page = clampi(coll_page, 0, pages - 1)
	var y := 62
	for i in range(coll_page * PER_PAGE, mini(list.size(), (coll_page + 1) * PER_PAGE)):
		var e: Dictionary = list[i]
		var b := Button.new()
		b.position = Vector2(12, y)
		b.size = Vector2(336, 22)
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		var st := _sb(K, W)
		st.content_margin_top = 1
		st.content_margin_bottom = 1
		b.add_theme_stylebox_override("normal", st)
		b.add_theme_stylebox_override("hover", st)
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
		y += 23
	_label(s, "%d / %d" % [coll_page + 1, pages], Vector2(0, 538), Vector2(SW, 20), FS, W, HORIZONTAL_ALIGNMENT_CENTER)
	var prev := _button(s, "◀ 前", Vector2(12, 532), Vector2(100, 34), func(): show_collection(coll_page - 1))
	prev.disabled = coll_page == 0
	var nxt := _button(s, "次 ▶", Vector2(248, 532), Vector2(100, 34), func(): show_collection(coll_page + 1))
	nxt.disabled = coll_page >= pages - 1
	_button(s, "結末 %d/%d" % [Game.save["endings"].size(), Game.ENDINGS.size()], Vector2(12, 584), Vector2(162, 40), _endings_popup)
	_button(s, "戻る", Vector2(186, 584), Vector2(162, 40), show_title)


func _endings_popup() -> void:
	var p := _overlay_panel(220)
	var c := Control.new()
	p.add_child(c)
	_label(c, "到達した結末", Vector2(8, 8), Vector2(304, 20), FS, R, HORIZONTAL_ALIGNMENT_LEFT, true)
	var y := 34
	for en in Game.ENDINGS:
		var got: bool = Game.save["endings"].has(en)
		_label(c, ("「%s」" % Game.ENDINGS[en]) if got else "「？？？？」", Vector2(8, y), Vector2(304, 20), FS, W if got else WD)
		y += 23
	_button(c, "閉じる", Vector2(88, 166), Vector2(144, 36), func(): _close_overlay())


func _sort_key(e: Dictionary) -> float:
	if e.has("fixed"):
		return float(e["fixed"]) - 0.5
	return float(e.get("min", 1)) + float(int(str(e["id"]).substr(1))) * 0.001


func _collection_detail(e: Dictionary) -> void:
	sfx.play("click")
	var p := _overlay_panel(440)
	var c := Control.new()
	p.add_child(c)
	var tr := TextureRect.new()
	tr.texture = _tex(e["id"])
	tr.position = Vector2(0, 0)
	tr.size = Vector2(320, 190)
	tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	c.add_child(tr)
	_label(c, e["t"], Vector2(4, 196), Vector2(312, 20), FS, R if e.has("fixed") else W, HORIZONTAL_ALIGNMENT_LEFT, true)
	var r := _rich(c, Vector2(4, 220), Vector2(312, 160))
	_set_fit(r, e["d"])
	_button(c, "閉じる", Vector2(86, 390), Vector2(148, 36), func(): _close_overlay())
