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
	G.flags["torch"] = 1
	G.flags["curse"] = 1
	G.flags["potion"] = 2
	G.event = G.by_id["e002"]
	main.show_game(false)
	await _wait(3.0)
	await _shot("03_game")
	var ch: Array = G.visible_choices()
	G.cur["b"] = 10
	main._choose(ch[1]["c"])
	await _wait(0.3)
	await _shot("04a_gauge_damage")
	await _wait(3.0)
	await _shot("04_result")
	# previews of already-seen outcomes
	G.event = G.by_id["e002"]
	for c in G.event["c"]:
		for br in ["r", "ok", "ng"]:
			G.save["known"]["e002:%d:%s" % [G.event["c"].find(c), br]] = true
	main._present_event()
	await _wait(3.0)
	await _shot("03b_preview")
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
	main._collection_detail(G.by_id["e002"], 2)
	await _wait(0.4)
	await _shot("09b_collection_result")
	main.show_help()
	await _wait(0.5)
	await _shot("10_help")
	main.show_help(1)
	await _wait(0.5)
	await _shot("10b_help2")
	# --- v1.4: item row paging, checkpoints, rewarded ad
	G.start_run(false)
	for f in ["torch", "rope", "key", "holy", "dog", "map", "sword", "amulet", "potion", "curse", "mark", "eye"]:
		G.add_item(f)
	G.add_item("potion")
	G.event = G.by_id["e009"]
	main.show_game(false)
	await _wait(2.5)
	await _shot("11_items_paged")
	main.item_scroll = 3
	main._build_items()
	await _wait(0.2)
	await _shot("11b_items_scrolled")
	G.save["checkpoints"] = [25, 50]
	G.save["coins"] = 60
	main.show_title()
	await _wait(0.4)
	main._choose_start(false)
	await _wait(0.4)
	await _shot("12_start_picker")
	main.show_gameover({"cleared": false, "score": 31, "depth_coins": 40, "gold": 12, "bonus": 0, "coins": 52, "new_best": false, "newly": [], "first_clear": false, "start": 26})
	await _wait(0.5)
	await _shot("13_gameover_ad")
	var sum2 := {"cleared": false, "score": 31, "depth_coins": 40, "gold": 12, "bonus": 0, "coins": 52, "new_best": false, "newly": [], "first_clear": false, "start": 26}
	main.show_gameover(sum2)
	await _wait(0.3)
	root.get_node("Ads").show_rewarded(main, func():
		G.grant_ad_bonus(52)
		sum2["ad_bonus"] = 52
		sum2["ad_used"] = true, func(): main.show_gameover(sum2))
	await _wait(1.5)
	await _shot("14_dummy_ad")
	await _wait(5.0)
	for n in main.get_children():
		if n is ColorRect and n.z_index == 90:
			for b in n.get_children():
				if b is Button:
					b.pressed.emit()
	await _wait(0.6)
	await _shot("15_after_ad")
	G.reset_save()
	quit()
