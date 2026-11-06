"""Balance simulator mirroring scripts/game.gd rules. Run: python3 -I tools/sim.py"""
import json, glob, random, math, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = json.load(open(os.path.join(ROOT, 'data/balance.json')))
EV = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data/events/*.json'))):
    EV += json.load(open(f))
FIXED = {e['fixed']: e for e in EV if 'fixed' in e}
STATS = 'bmf'

def scale(F): return 1 + (F - 1) / B['depth_div']
def sv(v, F, fixed=False):
    if fixed or v == 0: return v
    m = B['neg_mult'] if v < 0 else B['pos_mult']
    return int(math.copysign(max(1, round(abs(v) * m * scale(F))), v))

def unlocked(e, meta):
    u = e.get('u', 0)
    if isinstance(u, str): return u[2:] in meta['flags']
    return u <= meta['total']

def chance(c, st, F):
    s = c['chk']
    p = c['p'] + B['chk_per'] * (st['cur'][s] - B['chk_ref'] - F * B['chk_floor'])
    for fl, bon in B['item_bonus'].items():
        if fl in st['flags']: p += bon.get(s, 0) * (st['flags'][fl] if fl == 'curse' else 1)
    return min(B['chk_max'], max(B['chk_min'], p))

def ok_flags(o, flags, meta=None):
    if 'mreq_any' in o and not (meta and any(m in meta for m in o['mreq_any'])):
        return False
    return all(r in flags for r in o.get('req', [])) and not any(n in flags for n in o.get('no', []))


def weight(e, meta):
    w = e.get('w', 5)
    if e['id'] in meta.get('recent1', ()):
        w *= B['recent_mult'][0]
    elif e['id'] in meta.get('recent2', ()):
        w *= B['recent_mult'][1]
    return w

def pick_event(F, st, meta, rng):
    if F in FIXED and (F < 100 or not st['endless']): return FIXED[F]
    if st['endless'] and F > 100 and F % 25 == 0: return FIXED[[25, 50, 75][(F // 25) % 3]]
    def cands(relax_seen, relax_max):
        out = []
        for e in EV:
            if 'fixed' in e or not unlocked(e, meta): continue
            if e.get('endless') and not (st['endless'] and F > 100): continue
            if F < e.get('min', 1): continue
            if not relax_max and not st['endless'] and F > e.get('max', 99): continue
            if not ok_flags(e, st['flags']): continue
            if e['id'] in st['seen'] and (not relax_seen or e.get('once')): continue
            out.append(e)
        return out
    for rs, rm in [(False, False), (True, False), (False, True), (True, True)]:
        c = cands(rs, rm)
        if c: break
    tot = sum(weight(e, meta) for e in c); x = rng.random() * tot
    for e in c:
        x -= weight(e, meta)
        if x <= 0: return e
    return c[-1]

def visible_choices(e, st, F, meta=None):
    known = (meta or {}).get('flags', set()) | st['meta_new']
    av = [c for c in e['c'] if ok_flags(c, st['flags'], known) and gold_ok(c, st, F)]
    return av[:3]

def gold_ok(c, st, F):
    r = c.get('r')
    if r and r.get('g', 0) < 0: return st['gold'] >= sv(-r['g'], F)
    return True

def apply(r, st, F):
    fx = r.get('fixed', False)
    for s in STATS:
        if s in r: st['cur'][s] = min(st['max'][s], st['cur'][s] + sv(r[s], F, fx))
        k = 'm' + s
        if k in r:
            st['max'][s] = max(1, st['max'][s] + r[k]); st['cur'][s] = min(st['max'][s], st['cur'][s] + max(0, r[k]))
    if 'g' in r: st['gold'] = max(0, st['gold'] + sv(r['g'], F, fx))
    for f in r.get('set', []): add_item(st, f)
    for f in r.get('clr', []): remove_item(st, f)
    st['meta_new'] |= set(r.get('meta', []))
    return r.get('skip', 0), r.get('end')

UNIQUE = {'dog', 'sword', 'girl', 'oath', 'crown', 'mark', 'eye'}

def add_item(st, f):
    if (f in UNIQUE or f.startswith('_')) and f in st['flags']: return
    st['flags'][f] = st['flags'].get(f, 0) + 1

def remove_item(st, f):
    if f in st['flags']:
        st['flags'][f] -= 1
        if st['flags'][f] <= 0: del st['flags'][f]

def dead(st):
    if all(st['cur'][s] > 0 for s in STATS): return False
    if 'amulet' in st['flags']:
        remove_item(st, 'amulet')
        for s in STATS:
            if st['cur'][s] <= 0: st['cur'][s] = max(1, round(st['max'][s] * B['amulet_revive']))
        return False
    return True

def util(r, st, F):
    u = 0.0
    tmp = {s: st['cur'][s] for s in STATS}
    for s in STATS:
        if s in r:
            d = sv(r[s], F, r.get('fixed'))
            nv = min(st['max'][s], tmp[s] + d)
            u += (nv - tmp[s]) * (3.0 / (tmp[s] + 2))
            if nv <= 0 and 'amulet' not in st['flags']: u -= 1000
        if 'm' + s in r: u += r['m' + s] * 2
    u += r.get('skip', 0) * 0.8 + len(r.get('set', [])) * 0.8 + r.get('g', 0) * 0.02
    return u

def choose(ch, st, F, rng, policy):
    if policy == 'random': return rng.choice(ch)
    best, bu = None, -1e9
    for c in ch:
        if 'chk' in c:
            p = chance(c, st, F); u = p * util(c['ok'], st, F) + (1 - p) * util(c['ng'], st, F)
        else: u = util(c['r'], st, F)
        u += rng.random() * 0.3
        if u > bu: best, bu = c, u
    return best

def run(meta, levels, rng, endless=False, policy='smart'):
    mx = {s: B['base_stat'] + B['stat_per_level'] * levels[s] for s in STATS}
    st = dict(cur=dict(mx), max=dict(mx), flags={}, seen=set(), gold=0, endless=endless, meta_new=set())
    F = 1
    while True:
        e = pick_event(F, st, meta, rng); st['seen'].add(e['id'])
        ch = visible_choices(e, st, F, meta)
        c = choose(ch, st, F, rng, policy)
        if 'potion' in st['flags'] and min(st['cur'][s] / st['max'][s] for s in 'b') < 0.4:
            remove_item(st, 'potion'); st['cur']['b'] = min(st['max']['b'], st['cur']['b'] + round(st['max']['b'] * B['potion_heal']))
        r = c['r'] if 'r' in c else (c['ok'] if rng.random() < chance(c, st, F) else c['ng'])
        skip, end = apply(r, st, F)
        if end: return 100, st, True
        if r.get('retire'): return F, st, False
        if dead(st): return F, st, False
        F = next_floor(F, skip, endless)
        if endless and F > 300: return F, st, False

def next_floor(F, skip, endless):
    nf = max(1, F + 1 + skip)
    if not endless:
        for g in (25, 50, 75, 100):
            if F < g < nf: return g
    return nf

def coins_for(score, gold, clear):
    return int(score * (1 + score / B['coin_div'])) + gold + (B['clear_bonus'] if clear else 0)

def cost(L): return int(B['cost_base'] + B['cost_lin'] * L + B['cost_quad'] * L * L)

def campaign(seed, maxruns=200, verbose=False):
    rng = random.Random(seed)
    meta = dict(total=0, flags=set(), coins=0)
    lv = {s: 0 for s in STATS}
    hist = []
    for i in range(1, maxruns + 1):
        score, st, clear = run(meta, lv, rng)
        meta['total'] += score; meta['flags'] |= st['meta_new']
        meta['recent2'], meta['recent1'] = meta.get('recent1', set()), set(st['seen'])
        meta['coins'] += coins_for(score, st['gold'], clear)
        while True:
            s = min(STATS, key=lambda k: lv[k])
            if meta['coins'] >= cost(lv[s]): meta['coins'] -= cost(lv[s]); lv[s] += 1
            else: break
        hist.append(score)
        if clear: return i, hist, lv
    return None, hist, lv

if __name__ == '__main__':
    rng = random.Random(1)
    meta0 = dict(total=0, flags=set())
    for L in [0, 2, 5, 8, 12, 16, 20]:
        sc = [run(dict(total=10**6, flags=set()) if L >= 5 else meta0, {s: L for s in STATS}, rng)[0] for _ in range(300)]
        rs = [run(meta0, {s: L for s in STATS}, rng, policy='random')[0] for _ in range(300)]
        print(f'L={L:2d} max={B["base_stat"]+B["stat_per_level"]*L:3d} smart avg={sum(sc)/len(sc):6.1f} med={sorted(sc)[150]:3d} p90={sorted(sc)[270]:3d} | random avg={sum(rs)/len(rs):5.1f}')
    res = [campaign(s) for s in range(30)]
    runs = [r[0] for r in res if r[0]]
    print('clear runs:', sorted(runs), 'fails', sum(1 for r in res if not r[0]))
    i, hist, lv = res[0]
    print('example hist', hist[:60], lv)
