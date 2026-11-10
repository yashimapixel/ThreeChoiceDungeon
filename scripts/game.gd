extends Node
## Core game state & rules (autoload "Game").
## Rules are mirrored in tools/sim.py for balancing — keep them in sync.

const SAVE_PATH := "user://save.json"
const EVENT_FILES := ["res://data/events/tier1.json", "res://data/events/tier2.json",
		"res://data/events/tier3.json", "res://data/events/tier4.json", "res://data/events/endless.json"]
const STATS := ["b", "m", "f"]
const STAT_NAME := {"b": "肉体", "m": "精神", "f": "運命"}
const GATES := [25, 50, 75, 100]
const CHECKPOINTS := [25, 50, 75]   # clearing these gates lets later runs start just below them

## Run flags shown as items. Flags starting with "_" are hidden.
## Items stack (flags[f] = count); "unique" ones are held at most once.
const ITEMS := {
	"torch": {"name": "たいまつ", "desc": "闇を払う灯り。精神判定+5%。火を使う選択肢が選べる。"},
	"rope": {"name": "ロープ", "desc": "丈夫な縄。危険な場所を安全に渡れる。"},
	"key": {"name": "錆びた鍵", "desc": "どこかの扉や檻を開けられそうだ。"},
	"holy": {"name": "聖水", "desc": "清められた水。亡者や呪いに効く。使うと無くなる。"},
	"dog": {"name": "黒い犬", "desc": "忠実な相棒。肉体判定+10%。", "unique": true},
	"map": {"name": "古地図", "desc": "迷宮の抜け道が記された地図。"},
	"sword": {"name": "銀の剣", "desc": "魔を断つ銀の刃。肉体判定+10%。強敵に有効。", "unique": true},
	"amulet": {"name": "赤いお守り", "desc": "死を免れる。1回ごとに1つ壊れる。"},
	"potion": {"name": "薬瓶", "desc": "タップで1つ使用。肉体を最大値の40%回復する。"},
	"girl": {"name": "少女の霊", "desc": "母を探す少女の霊がついてくる。", "unique": true},
	"oath": {"name": "騎士の誓い", "desc": "王女を救うと誓った証。", "unique": true},
	"crown": {"name": "王冠", "desc": "地下都市の王の冠。精神判定+10%。", "unique": true},
	"curse": {"name": "呪い", "desc": "運命判定-15%（重なるほど悪化）。祓う方法があるはずだ。", "bad": true},
	"mark": {"name": "魔女の印", "desc": "肉体・精神判定+10%、運命判定-10%。いずれ代償を求められる。", "bad": true, "unique": true},
	"eye": {"name": "第三の眼", "desc": "見えないものが見える。運命判定+15%。", "bad": true, "unique": true},
}

## Four chapters (起承転結), one per depth band; gates sit at the chapter ends.
const CHAPTERS := {1: "第一章　降下", 26: "第二章　弔い", 51: "第三章　引き離された夜", 76: "第四章　子守唄"}

## Journal: truth fragments, unlocked by meta flags (written as the adventurer's notes).
const JOURNAL := [
	{"ch": 1, "meta": "replica_rule", "t": "迷宮は、呑み込んだ場所と、誰かの記憶を写し取るらしい。写しは、どこか少しだけ間違っている。"},
	{"ch": 1, "meta": "girl_met", "t": "影のない、白い服の少女。胸元に王家の紋章。「お母さまのところに連れてって」"},
	{"ch": 1, "meta": "diary1", "t": "封蝋の跡のあるメモ。『病で逝ったあの子に、もう一度会いたい』"},
	{"ch": 1, "meta": "met_knight", "t": "錆びた甲冑の亡霊。「……三年。まだ、底へは届かぬ。あの方々を、お救いせねば」"},
	{"ch": 2, "meta": "diary2", "t": "二枚目のメモ。追ってくる鎧の音。降りるほどに聞こえる、子どもの泣き声。"},
	{"ch": 2, "meta": "grave_seen", "t": "作り物めいた小さな墓。王家の紋章。隣には、何も刻まれていない空の墓。"},
	{"ch": 2, "meta": "witch_truth", "t": "魔女の話。三年前、泣き腫らした目の女が底へ降りた。「喰らって、形にして返した。この迷宮が、その形さ」"},
	{"ch": 2, "meta": "knight_truth", "t": "騎士の最後の戦い。底のものに敗れた。「あの眼を潰さねば」"},
	{"ch": 3, "meta": "decree_truth", "t": "滲んだ命令書。罹患者は隔離塔へ。例外は認めない。余白に一言、『……娘も』。"},
	{"ch": 3, "meta": "tower_truth", "t": "沈んだ隔離塔。壁いっぱいの落書き。『おかあさまに あいたい』"},
	{"ch": 3, "meta": "knight_guilt", "t": "騎士の告白。熱に浮かされた姫を母の腕から引き剥がし、塔へ運んだのは、自分だった。"},
	{"ch": 3, "meta": "king_letters", "t": "毎晩、迷宮に投げ入れられる王の手紙。『あの子に最後の子守唄を歌わせてやれなかった』"},
	{"ch": 3, "meta": "diary3", "t": "最後のメモ。底のものに願った。『もう二度と、離れたくない』"},
	{"ch": 3, "meta": "loop_truth", "t": "死ぬたび、あの子守唄が自分を入口へ連れ戻している。歌の主は、挑む者を手放せない。"},
	{"ch": 4, "meta": "heart_truth", "t": "迷宮の心臓。内側を歩く小さな足音を、愛おしむような鼓動。"},
	{"ch": 4, "meta": "sickroom", "t": "あの夜の部屋。白い寝台、窓辺の花、枕元の椅子。甲冑の足音。"},
]

const EPI_KNOWN := ["decree_truth", "king_letters", "knight_guilt", "tower_truth"]

const ENDINGS := {
	"slay": "闇を斬る者",
	"wish": "生還",
	"throne": "底の主",
	"release": "願いの終わり",
	"oath": "果たされた誓い",
	"reunion": "母と娘",
	"true": "還る光",
}

var B: Dictionary = {}
var events: Array = []
var by_id: Dictionary = {}
var fixed: Dictionary = {}

# --- persistent ---
var save := {}

# --- run state ---
var floor_n := 1
var cur := {}
var mx := {}
var flags := {}
var seen_run := {}
var gold := 0
var endless := false
var start_floor := 1
var event: Dictionary = {}
var meta_new := {}
var last_ending := ""
var rng := RandomNumberGenerator.new()


func _ready() -> void:
	rng.randomize()
	B = _load_json("res://data/balance.json")
	for p in EVENT_FILES:
		for e in _load_json(p):
			events.append(e)
			by_id[e["id"]] = e
			if e.has("fixed"):
				fixed[int(e["fixed"])] = e
	load_save()


func _load_json(path: String) -> Variant:
	var f := FileAccess.open(path, FileAccess.READ)
	return JSON.parse_string(f.get_as_text())


# ============================================================ persistence
func default_save() -> Dictionary:
	return {"coins": 0, "lv": {"b": 0, "m": 0, "f": 0}, "best": 0, "best_endless": 0, "total": 0,
		"runs": 0, "meta": [], "seen": [], "cleared": false, "endings": [], "unlocked_seen": [], "known": {}, "checkpoints": [], "recent1": [], "recent2": []}


func load_save() -> void:
	save = default_save()
	if FileAccess.file_exists(SAVE_PATH):
		var f := FileAccess.open(SAVE_PATH, FileAccess.READ)
		var d = JSON.parse_string(f.get_as_text())
		if d is Dictionary:
			for k in d:
				save[k] = d[k]
	for s in STATS:
		save["lv"][s] = int(save["lv"].get(s, 0))
	if not save["known"] is Dictionary:
		save["known"] = {}
	var cps := []
	for g in save.get("checkpoints", []):
		cps.append(int(g))
	save["checkpoints"] = cps
	# baseline of unlocked events so the first game over doesn't list starters as "new"
	if save["unlocked_seen"].is_empty():
		save["unlocked_seen"] = unlocked_ids()


func write_save() -> void:
	var f := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	f.store_string(JSON.stringify(save))


func reset_save() -> void:
	save = default_save()
	save["unlocked_seen"] = unlocked_ids()
	write_save()


# ============================================================ meta helpers
func is_unlocked(e: Dictionary) -> bool:
	var u = e.get("u", 0)
	if u is String:
		return save["meta"].has(u.substr(2))
	return int(u) <= int(save["total"])


func unlocked_ids() -> Array:
	var out := []
	for e in events:
		if is_unlocked(e):
			out.append(e["id"])
	return out


func next_unlock_total() -> int:
	var best := -1
	for e in events:
		var u = e.get("u", 0)
		if u is String:
			continue
		if int(u) > int(save["total"]) and (best < 0 or int(u) < best):
			best = int(u)
	return best


func stat_max_base(s: String) -> int:
	return int(B["base_stat"]) + int(B["stat_per_level"]) * int(save["lv"][s])


func upgrade_cost(s: String) -> int:
	var L := int(save["lv"][s])
	return int(float(B["cost_base"]) + float(B["cost_lin"]) * L + float(B["cost_quad"]) * L * L)


func buy_upgrade(s: String) -> bool:
	var c := upgrade_cost(s)
	if int(save["coins"]) < c:
		return false
	save["coins"] = int(save["coins"]) - c
	save["lv"][s] = int(save["lv"][s]) + 1
	write_save()
	return true


# ============================================================ run
func start_run(is_endless: bool, from_floor := 1) -> void:
	endless = is_endless
	floor_n = from_floor
	start_floor = from_floor
	flags = {}
	seen_run = {}
	gold = 0
	meta_new = {}
	last_ending = ""
	for s in STATS:
		mx[s] = stat_max_base(s)
		cur[s] = mx[s]
	pick_event()


func checkpoint_cost(g: int) -> int:
	return int(B["checkpoint_cost"].get(str(g), 0))


func unlocked_checkpoints() -> Array:
	var out := []
	for g in CHECKPOINTS:
		if save["checkpoints"].has(g):
			out.append(g)
	return out


## Pays the checkpoint fee and starts a normal run just below gate g.
func start_from_checkpoint(g: int) -> bool:
	if g > 1:
		var c := checkpoint_cost(g)
		if not save["checkpoints"].has(g) or int(save["coins"]) < c:
			return false
		save["coins"] = int(save["coins"]) - c
		start_run(false, g + 1)
	else:
		start_run(false)
	return true


## Rewarded ad: doubles the souls earned by the last run.
func grant_ad_bonus(amount: int) -> void:
	save["coins"] = int(save["coins"]) + amount
	write_save()


func depth_reward(n: int) -> int:
	return int(n * (1.0 + float(n) / float(B["coin_div"])))


func depth_scale() -> float:
	return 1.0 + float(floor_n - 1) / float(B["depth_div"])


func sv(v: int, fixed_val := false) -> int:
	if fixed_val or v == 0:
		return v
	var m: float = float(B["neg_mult"]) if v < 0 else float(B["pos_mult"])
	var a := maxi(1, roundi(absf(v) * m * depth_scale()))
	return a if v > 0 else -a


func _flags_ok(o: Dictionary) -> bool:
	for r in o.get("req", []):
		if not flags.has(r):
			return false
	for n in o.get("no", []):
		if flags.has(n):
			return false
	return _meta_ok(o)


## "mreq_any": satisfied if any listed meta flag is known (from earlier runs or this one).
func _meta_ok(o: Dictionary) -> bool:
	if not o.has("mreq_any"):
		return true
	for m in o["mreq_any"]:
		if save["meta"].has(m) or meta_new.has(m):
			return true
	return false


func pick_event() -> void:
	if fixed.has(floor_n) and (floor_n < 100 or not endless):
		event = fixed[floor_n]
	elif endless and floor_n > 100 and floor_n % 25 == 0:
		event = fixed[[25, 50, 75][(floor_n / 25) % 3]]
	else:
		var cands := []
		# guarantee: in the last 4 floors of a chapter, an unseen beat of that chapter comes first
		var ch := chapter_of(floor_n)
		if not endless and floor_n >= ch * 25 - 4 and floor_n < ch * 25:
			for e in _candidates(false, false):
				if int(e.get("beat", 0)) == ch:
					cands.append(e)
		for mode in [[false, false], [true, false], [false, true], [true, true]]:
			if not cands.is_empty():
				break
			cands = _candidates(mode[0], mode[1])
			if not cands.is_empty():
				break
		var tot := 0.0
		for e in cands:
			tot += _weight(e)
		var x := rng.randf() * tot
		event = cands[-1]
		for e in cands:
			x -= _weight(e)
			if x <= 0.0:
				event = e
				break
	seen_run[event["id"]] = true
	if not save["seen"].has(event["id"]):
		save["seen"].append(event["id"])


static func chapter_of(f: int) -> int:
	return 1 if f <= 25 else (2 if f <= 50 else (3 if f <= 75 else 4))


## Event weight, lowered for events seen in the last two runs (less early repetition).
## Story beats are boosted and exempt from the recency penalty.
func _weight(e: Dictionary) -> float:
	var w := float(e.get("w", 5))
	if e.has("beat"):
		return w * float(B["beat_mult"])
	if save["recent1"].has(e["id"]):
		w *= float(B["recent_mult"][0])
	elif save["recent2"].has(e["id"]):
		w *= float(B["recent_mult"][1])
	return w


func _candidates(relax_seen: bool, relax_max: bool) -> Array:
	var out := []
	for e in events:
		if e.has("fixed") or not is_unlocked(e):
			continue
		if e.get("endless", false) and not (endless and floor_n > 100):
			continue
		if floor_n < int(e.get("min", 1)):
			continue
		if not relax_max and not endless and floor_n > int(e.get("max", 99)):
			continue
		if not _flags_ok(e):
			continue
		if seen_run.has(e["id"]) and (not relax_seen or e.get("once", false)):
			continue
		out.append(e)
	return out


func event_text() -> String:
	var t: String = String(event["d"]).replace("{runs}", str(int(save["runs"]) + 1))
	for x in event.get("dx", []):
		if _flags_ok(x):
			t += "\n" + x["d"]
	return t


## Returns up to 3 choice descriptors: {c, enabled, locked, tag, chance}
func visible_choices() -> Array:
	var avail := []
	var locked := []
	for c in event["c"]:
		var hidden := false
		for n in c.get("no", []):
			if flags.has(n):
				hidden = true
		if not _meta_ok(c):
			hidden = true   # secret choices only appear once the player knows the truth
		if hidden:
			continue
		var req_ok := true
		for r in c.get("req", []):
			if not flags.has(r):
				req_ok = false
		var info := {"c": c, "enabled": req_ok, "locked": not req_ok, "tag": "", "chance": -1.0}
		if c.has("req") and not c["req"].is_empty():
			var names := []
			for r in c["req"]:
				names.append(ITEMS.get(r, {"name": r})["name"])
			info["tag"] = "〈" + "・".join(names) + "〉"
		if c.has("chk"):
			info["chance"] = chance(c)
		var r: Dictionary = c.get("r", {})
		if req_ok and r.get("g", 0) < 0 and gold < sv(-int(r["g"])):
			info["enabled"] = false
			info["tag"] += "金貨%d枚が必要" % sv(-int(r["g"]))
		if req_ok:
			avail.append(info)
		else:
			locked.append(info)
	var out := avail.slice(0, 3)
	var i := 0
	while out.size() < 3 and i < locked.size():
		out.append(locked[i])
		i += 1
	return out


func chance(c: Dictionary) -> float:
	var s: String = c["chk"]
	var p: float = float(c["p"]) + float(B["chk_per"]) * (float(cur[s]) - float(B["chk_ref"]) - floor_n * float(B["chk_floor"]))
	for fl in B["item_bonus"]:
		if flags.has(fl):
			# bonuses apply once; only curses stack
			var mult: int = int(flags[fl]) if fl == "curse" else 1
			p += float(B["item_bonus"][fl].get(s, 0.0)) * mult
	return clampf(p, float(B["chk_min"]), float(B["chk_max"]))


## Resolve a choice. Returns a summary dictionary for the UI.
func resolve(c: Dictionary) -> Dictionary:
	var res := {"check": "", "success": true}
	var r: Dictionary
	var branch := "r"
	if c.has("chk"):
		var p := chance(c)
		var ok := rng.randf() < p
		res["check"] = c["chk"]
		res["success"] = ok
		res["chance"] = p
		branch = "ok" if ok else "ng"
		r = c[branch]
	else:
		r = c["r"]
	save["known"][_known_key(c, branch)] = true
	res["key"] = "%s_%d_%s" % [event["id"], event["c"].find(c), branch]
	res["text"] = r.get("d", "")
	for x in r.get("dx", []):
		if _flags_ok(x):
			res["text"] += "\n" + x["d"]
	var fx: bool = r.get("fixed", false)
	var deltas := {}
	for s in STATS:
		var before: int = cur[s]
		var mk: String = "m" + s
		if r.has(mk):
			var inc := int(r[mk])
			mx[s] = maxi(1, int(mx[s]) + inc)
			res["max_" + s] = inc
			if inc > 0:
				cur[s] = mini(int(mx[s]), int(cur[s]) + inc)
			cur[s] = mini(int(cur[s]), int(mx[s]))
		if r.has(s):
			cur[s] = mini(int(mx[s]), int(cur[s]) + sv(int(r[s]), fx))
		if int(cur[s]) != before:
			deltas[s] = int(cur[s]) - before
	res["deltas"] = deltas
	if r.has("g"):
		var g := sv(int(r["g"]), fx)
		gold = maxi(0, gold + g)
		res["gold"] = g
	var gained := []
	var lost := []
	for f in r.get("set", []):
		if add_item(f) and not f.begins_with("_"):
			gained.append(f)
	for f in r.get("clr", []):
		if remove_item(f) and not f.begins_with("_"):
			lost.append(f)
	res["gained"] = gained
	res["lost"] = lost
	for m in r.get("meta", []):
		meta_new[m] = true
	res["skip"] = int(r.get("skip", 0))
	if r.get("retire", false):
		res["retire"] = true
		res["dead"] = false
		return res
	if r.has("end"):
		res["end"] = r["end"]
		last_ending = r["end"]
		return res
	# death check (amulet saves once)
	res["dead"] = false
	if is_dead():
		if flags.has("amulet"):
			remove_item("amulet")
			for s in STATS:
				if int(cur[s]) <= 0:
					cur[s] = maxi(1, roundi(float(mx[s]) * float(B["amulet_revive"])))
			res["amulet"] = true
		else:
			res["dead"] = true
	if not res["dead"] and event.has("fixed") and int(event["fixed"]) in CHECKPOINTS:
		var g := int(event["fixed"])
		if not save["checkpoints"].has(g):
			save["checkpoints"].append(g)
			res["checkpoint"] = g
	return res


func _known_key(c: Dictionary, branch: String) -> String:
	return "%s:%d:%s" % [event["id"], event["c"].find(c), branch]


## Has the player already seen this outcome ("r", "ok" or "ng") of choice c in the current event?
func is_known(c: Dictionary, branch: String) -> bool:
	return save["known"].has(_known_key(c, branch))


## Adds one of an item. Unique items (and hidden flags) are held at most once.
## Returns true if something was actually added.
func add_item(f: String) -> bool:
	var unique: bool = f.begins_with("_") or ITEMS.get(f, {}).get("unique", false)
	if unique and flags.has(f):
		return false
	flags[f] = int(flags.get(f, 0)) + 1
	return true


## Removes one of an item. Returns true if one was removed.
func remove_item(f: String) -> bool:
	if not flags.has(f):
		return false
	flags[f] = int(flags[f]) - 1
	if int(flags[f]) <= 0:
		flags.erase(f)
	return true


func item_count(f: String) -> int:
	return int(flags.get(f, 0))


func is_dead() -> bool:
	for s in STATS:
		if int(cur[s]) <= 0:
			return true
	return false


func use_potion() -> int:
	if not flags.has("potion"):
		return 0
	remove_item("potion")
	var before: int = cur["b"]
	cur["b"] = mini(int(mx["b"]), int(cur["b"]) + roundi(float(mx["b"]) * float(B["potion_heal"])))
	return int(cur["b"]) - before


func next_floor(skip: int) -> int:
	var nf := maxi(1, floor_n + 1 + skip)
	if not endless:
		for g in GATES:
			if floor_n < g and g < nf:
				return g
	return nf


func advance(skip: int) -> void:
	floor_n = next_floor(skip)
	pick_event()


## Called when the run ends (death or clear). Returns summary for UI.
func end_run(cleared: bool, retired := false) -> Dictionary:
	var score := 100 if cleared and not endless else floor_n
	# starting from a checkpoint only pays for the floors actually descended
	var depth_coins := maxi(0, depth_reward(score) - depth_reward(start_floor - 1))
	var bonus := int(B["clear_bonus"]) if cleared else 0
	var total_coins := depth_coins + gold + bonus
	var before_unlocked: Array = save["unlocked_seen"]
	save["coins"] = int(save["coins"]) + total_coins
	save["total"] = int(save["total"]) + maxi(1, score - start_floor + 1)
	save["runs"] = int(save["runs"]) + 1
	var new_best := false
	if endless:
		if score > int(save["best_endless"]):
			save["best_endless"] = score
			new_best = true
	elif score > int(save["best"]):
		save["best"] = score
		new_best = true
	for m in meta_new:
		if not save["meta"].has(m):
			save["meta"].append(m)
	var first_clear := false
	if cleared:
		if not save["cleared"]:
			first_clear = true
		save["cleared"] = true
		if last_ending != "" and not save["endings"].has(last_ending):
			save["endings"].append(last_ending)
	var now := unlocked_ids()
	var newly := []
	for id in now:
		if not before_unlocked.has(id):
			newly.append(id)
	save["unlocked_seen"] = now
	save["recent2"] = save["recent1"]
	save["recent1"] = seen_run.keys()
	write_save()
	return {"score": score, "depth_coins": depth_coins, "gold": gold, "bonus": bonus, "coins": total_coins,
		"new_best": new_best, "newly": newly, "first_clear": first_clear, "cleared": cleared,
		"start": start_floor, "retired": retired}


## Mid-run snapshot so a killed app can resume (taken after each advance).
func save_run() -> void:
	save["run"] = {"floor": floor_n, "cur": cur, "mx": mx, "flags": flags, "seen": seen_run.keys(),
		"gold": gold, "endless": endless, "event": event["id"], "meta_new": meta_new.keys(), "start": start_floor}
	write_save()


func clear_run() -> void:
	save.erase("run")
	write_save()


func has_run() -> bool:
	return save.has("run") and save["run"] is Dictionary


func resume_run() -> void:
	var r: Dictionary = save["run"]
	floor_n = int(r["floor"])
	endless = bool(r["endless"])
	start_floor = int(r.get("start", 1))
	gold = int(r["gold"])
	for s in STATS:
		cur[s] = int(r["cur"][s])
		mx[s] = int(r["mx"][s])
	flags = {}
	if r["flags"] is Dictionary:
		for f in r["flags"]:
			flags[f] = int(r["flags"][f])
	else:  # v1.0 saves stored a plain list
		for f in r["flags"]:
			flags[f] = 1
	seen_run = {}
	for f in r["seen"]:
		seen_run[f] = true
	meta_new = {}
	for f in r["meta_new"]:
		meta_new[f] = true
	event = by_id.get(r["event"], events[0])
	last_ending = ""


func knows(m: String) -> bool:
	return save["meta"].has(m) or meta_new.has(m)


## Epilogue after an ending: what the king hears (depends on the truths you learned).
func epilogue(end_id: String) -> String:
	var known := false
	for m in EPI_KNOWN:
		if knows(m):
			known = true
	if end_id == "wish":
		return "あなたは地上へ戻った。王の問いに、あなたは答えられなかった。\n今夜も、王都の地下には、言葉のない子守唄が響いている。"
	if end_id == "throne":
		return "あなたは、地上へ戻らなかった。\n王都の地下の子守唄は、いつしか、二つの声で歌われるようになったという。"
	if known:
		return "地上に戻ったあなたは、玉座の間ですべてを話した。隔離塔のこと。命令書の一行のこと。底で見たもののこと。\n孤独な王は長いあいだ黙って聞き、やがて、三年ぶりに二人の名を呼んで泣いた。\nその夜から、王都の地下に子守唄は響かなくなった。王は、三年ぶりに静かな眠りについた。"
	return "地上に戻ったあなたの報告を、王は黙って聞いた。迷宮の底に何があったのか、あなたにもすべてはわからない。\nただ、その夜から、王都の地下に子守唄は響かなくなった。"


func journal_count() -> Array:
	var n := 0
	for j in JOURNAL:
		if save["meta"].has(j["meta"]):
			n += 1
	return [n, JOURNAL.size()]


func item_list() -> Array:
	var out := []
	for f in flags:
		if ITEMS.has(f):
			out.append(f)
	return out
