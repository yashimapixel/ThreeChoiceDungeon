extends SceneTree
## Headless smoke test: plays many random runs through the Game API.
## godot --headless -s tools/test_runs.gd

func _initialize() -> void:
	process_frame.connect(_run, CONNECT_ONE_SHOT)


func _run() -> void:
	var G = root.get_node("Game")
	G.reset_save()
	var scores := []
	var clears := 0
	var ev_seen := {}
	for run in 300:
		# give meta progress so deeper content gets exercised
		if run % 3 == 0:
			for s in G.STATS:
				G.save["lv"][s] = mini(25, run / 10)
		G.start_run(run % 10 == 9 and G.save["cleared"])
		var guard := 0
		while guard < 400:
			guard += 1
			ev_seen[G.event["id"]] = true
			var ch: Array = G.visible_choices()
			assert(ch.size() >= 2, "too few choices in " + G.event["id"])
			var en := ch.filter(func(i): return i["enabled"])
			if en.is_empty():
				push_error("no enabled choice in " + G.event["id"])
				break
			var c: Dictionary = en[G.rng.randi() % en.size()]["c"]
			var res: Dictionary = G.resolve(c)
			if res.has("end"):
				G.end_run(true); clears += 1; scores.append(100); break
			if res["dead"]:
				var sm: Dictionary = G.end_run(false); scores.append(sm["score"]); break
			G.advance(res["skip"])
			G.save_run()
			if G.endless and G.floor_n > 160:
				G.end_run(false); scores.append(G.floor_n); break
	var avg := 0.0
	for s in scores: avg += s
	print("runs=%d avg=%.1f max=%d clears=%d distinct_events=%d total=%d meta=%s" % [scores.size(), avg / scores.size(), scores.max(), clears, ev_seen.size(), G.save["total"], str(G.save["meta"])])
	# force-unlock everything and exercise all events once more
	G.save["total"] = 100000
	for m in ["met_knight", "witch_pact", "diary1", "diary2", "girl_saved", "knight_dead"]:
		if not G.save["meta"].has(m): G.save["meta"].append(m)
	for run in 200:
		G.start_run(true)
		for s in G.STATS:
			G.cur[s] = 999; G.mx[s] = 999
		for i in 120:
			ev_seen[G.event["id"]] = true
			var ch: Array = G.visible_choices()
			var en := ch.filter(func(x): return x["enabled"])
			if en.is_empty(): break
			var res: Dictionary = G.resolve(en[G.rng.randi() % en.size()]["c"])
			if res.has("end") or res["dead"]: break
			G.advance(res["skip"])
	var missing := []
	for e in G.events:
		if not ev_seen.has(e["id"]): missing.append(e["id"])
	print("events never seen: ", missing)
	G.reset_save()
	quit()
