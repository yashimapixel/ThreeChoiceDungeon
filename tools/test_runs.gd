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
			if res.get("retire", false):
				G.end_run(false, true); scores.append(G.floor_n); break
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
	# item stacking
	for s in G.STATS:
		G.save["lv"][s] = 0
	G.start_run(false)
	G.add_item("potion"); G.add_item("potion"); G.add_item("dog"); G.add_item("dog")
	assert(G.item_count("potion") == 2 and G.item_count("dog") == 1)
	G.use_potion()
	assert(G.item_count("potion") == 1)
	G.remove_item("potion")
	assert(not G.flags.has("potion"))
	G.add_item("curse"); G.add_item("curse")
	var c := {"chk": "f", "p": 0.5}
	var p2: float = G.chance(c)
	G.remove_item("curse")
	assert(G.chance(c) > p2)
	print("stacking OK")
	# checkpoints
	G.reset_save()
	G.start_run(false)
	G.floor_n = 25
	G.event = G.by_id["g025"]
	for s in G.STATS:
		G.cur[s] = 999; G.mx[s] = 999
	var res: Dictionary = G.resolve(G.event["c"][4])   # pay toll with fate
	assert(res.get("checkpoint", 0) == 25 and G.unlocked_checkpoints() == [25])
	G.save["coins"] = 5
	assert(not G.start_from_checkpoint(25))        # cannot afford 20
	G.save["coins"] = 30
	assert(G.start_from_checkpoint(25) and G.floor_n == 26 and int(G.save["coins"]) == 10)
	G.floor_n = 30
	var sm: Dictionary = G.end_run(false)
	assert(sm["depth_coins"] == G.depth_reward(30) - G.depth_reward(25))
	assert(int(G.save["total"]) == 5)
	print("checkpoints OK: depth reward from B26 to B30 =", sm["depth_coins"])
	# finale: which endings are offered, and truth-dependent epilogues
	var fin := func(fl: Array, meta: Array) -> Array:
		G.reset_save()
		for m in meta:
			G.save["meta"].append(m)
		G.start_run(false)
		for f in fl:
			G.add_item(f)
		G.floor_n = 100
		G.event = G.by_id["g100"]
		var ends := []
		for ch in G.visible_choices():
			ends.append(ch["c"]["r"]["end"])
		return ends
	assert(fin.call([], []) == ["slay", "wish", "throne"])
	assert(fin.call(["girl", "oath"], []) == ["true", "reunion", "oath"])
	assert(fin.call(["girl"], ["diary3"]) == ["reunion", "release", "slay"])
	assert(fin.call([], ["knight_truth"]) == ["release", "slay", "wish"])
	fin.call([], ["heart_truth"])
	var r2: Dictionary = G.resolve(G.event["c"][4])
	assert(r2["end"] == "slay" and r2["text"].contains("届かなかった"))
	fin.call([], [])
	var r3: Dictionary = G.resolve(G.event["c"][4])
	assert(not r3["text"].contains("届かなかった"))
	var sm3: Dictionary = G.end_run(true)
	assert(G.save["endings"] == ["slay"] and sm3["cleared"])
	# resting the girl at her grave: she leaves this run, endings change
	G.reset_save()
	G.start_run(false)
	G.add_item("girl"); G.add_item("oath")
	G.floor_n = 40
	G.event = G.by_id["e046"]
	G.resolve(G.event["c"][0])
	assert(not G.flags.has("girl") and G.flags.has("_girl_rested"))
	G.floor_n = 100
	G.event = G.by_id["g100"]
	var ends2 := []
	for ch in G.visible_choices():
		ends2.append(ch["c"]["r"]["end"])
	assert(ends2 == ["oath", "slay", "wish"])
	var ro: Dictionary = G.resolve(G.event["c"][2])
	assert(ro["text"].contains("先に行ったのね"))
	# letting the knight's ghost rest drops the oath
	G.start_run(false)
	G.add_item("oath")
	G.save["meta"].append("met_knight")
	G.floor_n = 30
	G.event = G.by_id["e045"]
	G.resolve(G.event["c"][2])
	assert(not G.flags.has("oath") and G.item_count("amulet") == 1)
	print("endings OK")
	# girl never comes back after resting / fleeing in the same run
	G.reset_save()
	G.start_run(false)
	G.add_item("_girl_rested")
	G.floor_n = 10
	var cand: Array = G._candidates(true, true)
	assert(not cand.any(func(e): return e["id"] == "e008"))
	# endless-only events: never in normal mode, available below B100 in endless
	G.start_run(false)
	G.floor_n = 99
	assert(not G._candidates(true, true).any(func(e): return e.get("endless", false)))
	G.start_run(true)
	G.floor_n = 120
	assert(G._candidates(false, false).any(func(e): return e.get("endless", false)))
	# retire ends the run alive
	G.event = G.by_id["x08"]
	var rr: Dictionary = G.resolve(G.event["c"][0])
	assert(rr.get("retire", false) and not rr["dead"])
	var smr: Dictionary = G.end_run(false, true)
	assert(smr["retired"] and smr["score"] == 120)
	print("endless OK")
	# chapter beats: in the last floors of a chapter an unseen beat is guaranteed
	G.reset_save()
	G.start_run(false)
	G.floor_n = 22
	G.pick_event()
	assert(int(G.event.get("beat", 0)) == 1)
	G.start_run(false)
	G.floor_n = 72
	G.pick_event()
	assert(int(G.event.get("beat", 0)) == 3)
	# death count in dialogue, epilogue variants, journal
	G.save["runs"] = 6
	G.event = G.by_id["n05"]
	assert(G.event_text().contains("7度目"))
	G.meta_new = {}
	assert(not G.epilogue("true").contains("隔離塔"))
	G.save["meta"].append("decree_truth")
	assert(G.epilogue("true").contains("隔離塔"))
	assert(G.journal_count()[0] == 1)
	print("story OK")
	G.reset_save()
	quit()
