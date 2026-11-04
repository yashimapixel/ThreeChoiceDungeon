extends SceneTree
## Renders screenshots of each screen. Run under xvfb:
## xvfb-run -s "-screen 0 800x1400x24" godot --rendering-driver opengl3 -s tools/screenshots.gd -- <outdir>

var out := "user://shots"
var main: Node
var G: Node

func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		out = args[0]
	DirAccess.make_dir_recursive_absolute(out)
	process_frame.connect(_go, CONNECT_ONE_SHOT)

func _wait(sec: float) -> void:
	await create_timer(sec).timeout

func _shot(name: String) -> void:
	await process_frame
	await process_frame
	var img := root.get_texture().get_image()
	img.save_png(out + "/" + name + ".png")
	print("shot ", name, " ", img.get_size())

func _go() -> void:
	G = root.get_node("Game")
	G.reset_save()
	G.save["coins"] = 137
	G.save["best"] = 23
	G.save["total"] = 120
	G.save["runs"] = 6
	main = load("res://scenes/main.tscn").instantiate()
	root.add_child(main)
	await _wait(0.6)
	await _shot("01_title")
	main.show_shop()
	await _wait(0.5)
	await _shot("02_shop")
	G.start_run(false)
	G.flags["torch"] = true
	G.flags["curse"] = true
	G.flags["potion"] = true
	G.event = G.by_id["e002"]
	main.show_game(false)
	await _wait(3.0)
	await _shot("03_game")
	var ch: Array = G.visible_choices()
	main._choose(ch[1]["c"])
	await _wait(3.0)
	await _shot("04_result")
	G.floor_n = 25
	G.event = G.by_id["g025"]
	main._present_event()
	main._refresh_hud()
	await _wait(3.0)
	await _shot("05_gate")
	G.floor_n = 100
	G.flags["girl"] = true
	G.event = G.by_id["g100"]
	main._present_event()
	await _wait(3.0)
	await _shot("06_final")
	var res: Dictionary = G.resolve(G.visible_choices()[0]["c"])
	var sm: Dictionary = G.end_run(true)
	main.show_ending(res, sm)
	await _wait(3.5)
	await _shot("07_ending")
	main.show_gameover({"cleared": false, "score": 17, "depth_coins": 28, "gold": 21, "bonus": 0, "coins": 49, "new_best": true, "newly": ["e025", "e026", "e033"], "first_clear": false})
	await _wait(0.5)
	await _shot("08_gameover")
	main.show_collection()
	await _wait(0.5)
	await _shot("09_collection")
	main.show_help()
	await _wait(0.5)
	await _shot("10_help")
	G.reset_save()
	quit()
