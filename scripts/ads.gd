extends Node
## Rewarded-ad facade (autoload "Ads").
##
## The game only calls `is_rewarded_ready()` and `show_rewarded()`.
## For now this shows a 5-second DUMMY ad drawn in the game's own style.
## To ship real ads, replace the body of `show_rewarded()` with an ad SDK
## (e.g. an AdMob plugin for Godot): call `on_reward` from the SDK's
## "user earned reward" callback and `on_closed` when the ad is dismissed.

const DUMMY := true
const DUMMY_SECONDS := 5

var _busy := false


func is_rewarded_ready() -> bool:
	return not _busy


## host: a Control to draw the dummy ad into (inherits its theme/fonts).
func show_rewarded(host: Control, on_reward: Callable, on_closed: Callable) -> void:
	if _busy:
		return
	_busy = true
	_show_dummy(host, on_reward, on_closed)


func _show_dummy(host: Control, on_reward: Callable, on_closed: Callable) -> void:
	var W := Color8(232, 226, 212)
	var R := Color8(206, 36, 46)
	var root := ColorRect.new()
	root.color = Color8(14, 12, 14)
	root.size = host.size
	var top := roundf(((host.size.y - 264.0) / 2.0 - 40.0) / 8.0) * 8.0
	root.z_index = 90
	root.mouse_filter = Control.MOUSE_FILTER_STOP
	host.add_child(root)
	var frame := Panel.new()
	frame.position = Vector2(24, top)
	frame.size = Vector2(312, 264)
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color8(14, 12, 14)
	sb.border_color = Color8(152, 146, 136)
	sb.set_border_width_all(1)
	frame.add_theme_stylebox_override("panel", sb)
	root.add_child(frame)
	var tag := _label(frame, "広告（ダミー）", Vector2(0, 16), 16, R)
	tag.size.x = 312
	var body := _label(frame, "ここに本物の広告が\n表示されます", Vector2(0, 80), 24, W)
	body.size.x = 312
	var cnt := _label(root, "", Vector2(0, top + 280), 16, W)
	cnt.size.x = 360
	var close := Button.new()
	close.text = "報酬を受け取って閉じる"
	close.position = Vector2(56, top + 320)
	close.size = Vector2(248, 40)
	close.disabled = true
	root.add_child(close)
	var left := [DUMMY_SECONDS]
	cnt.text = "あと %d 秒" % left[0]
	var timer := Timer.new()
	timer.wait_time = 1.0
	root.add_child(timer)
	timer.timeout.connect(func():
		left[0] -= 1
		if left[0] > 0:
			cnt.text = "あと %d 秒" % left[0]
		else:
			timer.stop()
			cnt.text = "視聴完了"
			close.disabled = false)
	timer.start()
	close.pressed.connect(func():
		root.queue_free()
		_busy = false
		on_reward.call()
		on_closed.call())


func _label(parent: Node, text: String, pos: Vector2, size: int, col: Color) -> Label:
	var l := Label.new()
	l.text = text
	l.position = pos
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", col)
	parent.add_child(l)
	return l
