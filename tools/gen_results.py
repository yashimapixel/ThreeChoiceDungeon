"""Result stills: one image per choice outcome -> art/results/<event>_<choice>_<branch>.png

Most results are the event's scene re-drawn with effect overlays chosen from the
outcome (wounds, madness, doom, light, gold, item icons, shortcuts...).
Key story / gate / ending outcomes get bespoke drawings (BESPOKE below).

Usage: python3 -I tools/gen_results.py [--sheet out.png]
"""
import glob, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_art as G
from gen_art import C, K, WH, R, W, H, figure, skull, dith
from PIL import Image, ImageDraw

ROOT = G.ROOT
BAD = {'curse', 'mark', 'eye'}


def seed_of(s):
    return sum(ord(ch) * (k + 1) for k, ch in enumerate(s))


def canvas_from(img, seed):
    return C.from_image(img, seed)


def scene(c, bg):
    """Background only (dimmed), for bespoke drawings."""
    G.BGS[bg](c)
    c.fade(lambda x, y: G.BG_DIM.get(bg, 0.5))


# ------------------------------------------------------------------ item icons
def icon(c, name, cx, cy, lost=False):
    c.glow(cx, cy, 16, 0.35)
    c.rect((cx - 10, cy - 10, cx + 10, cy + 10), K, R if name in BAD else WH)
    x, y = cx, cy
    if name == 'torch':
        c.line((x, y + 7), (x, y - 2)); c.line((x + 1, y + 7), (x + 1, y - 2))
        c.poly([(x - 3, y - 2), (x, y - 8), (x + 4, y - 2)], R, R); c.p(x, y - 4, WH)
    elif name == 'rope':
        for r_ in (7, 5, 3):
            c.arc((x - r_, y - r_, x + r_, y + r_), 0, 360)
        c.line((x + 7, y), (x + 8, y + 7))
    elif name == 'key':
        c.ell((x - 7, y - 4, x - 1, y + 2), K, WH); c.line((x - 1, y - 1), (x + 7, y - 1))
        c.line((x + 5, y - 1), (x + 5, y + 3)); c.line((x + 7, y - 1), (x + 7, y + 2))
    elif name == 'holy':
        c.rect((x - 1, y - 8, x + 1, y - 5), K, WH); c.ell((x - 5, y - 5, x + 5, y + 7), K, WH)
        c.line((x, y - 2), (x, y + 4)); c.line((x - 2, y), (x + 2, y))
    elif name == 'dog':
        c.poly([(x - 6, y + 6), (x - 5, y - 3), (x - 3, y - 8), (x - 1, y - 3), (x + 1, y - 3), (x + 3, y - 8), (x + 5, y - 3), (x + 6, y + 6)], K, WH)
        c.p(x - 2, y, R); c.p(x + 2, y, WH)
    elif name == 'map':
        c.poly([(x - 7, y - 6), (x + 7, y - 7), (x + 7, y + 6), (x - 7, y + 7)], WH, WH)
        c.d.line([(x - 5, y + 4), (x - 2, y - 1), (x + 1, y + 2), (x + 4, y - 3)], fill=K); c.p(x + 4, y - 3, R)
    elif name == 'sword':
        c.line((x - 6, y + 6), (x + 6, y - 6)); c.line((x - 5, y + 6), (x + 6, y - 5))
        c.line((x - 6, y + 2), (x - 2, y + 6)); c.p(x - 7, y + 7, R)
    elif name == 'amulet':
        c.arc((x - 6, y - 9, x + 6, y + 2), 200, 340)
        c.poly([(x, y - 2), (x + 5, y + 3), (x, y + 8), (x - 5, y + 3)], R, WH)
    elif name == 'potion':
        c.rect((x - 1, y - 8, x + 1, y - 5), K, WH); c.ell((x - 5, y - 5, x + 5, y + 7), R, WH)
        c.p(x - 2, y - 1, WH)
    elif name == 'girl':
        c.poly([(x - 4, y - 4), (x + 4, y - 4), (x + 6, y + 8), (x - 6, y + 8)], WH, WH)
        c.ell((x - 4, y - 9, x + 4, y - 1), WH, WH); c.ell((x - 2, y - 7, x + 2, y - 3), K, K)
    elif name == 'oath':
        c.poly([(x - 6, y - 7), (x + 6, y - 7), (x + 6, y + 1), (x, y + 8), (x - 6, y + 1)], K, WH)
        c.line((x, y - 5), (x, y + 5), R); c.line((x - 3, y - 2), (x + 3, y - 2), R)
    elif name == 'crown':
        c.poly([(x - 7, y + 5), (x - 7, y - 3), (x - 4, y + 1), (x, y - 6), (x + 4, y + 1), (x + 7, y - 3), (x + 7, y + 5)], K, WH)
        c.p(x, y + 2, R)
    elif name == 'curse':
        c.ell((x - 7, y - 7, x + 7, y + 7), K, R)
        for a in range(5):
            a0, a1 = a * 144, a * 144 + 144
            c.line((x + 6 * math.sin(math.radians(a0)), y - 6 * math.cos(math.radians(a0))),
                   (x + 6 * math.sin(math.radians(a1)), y - 6 * math.cos(math.radians(a1))), R)
    elif name == 'mark':
        c.line((x - 5, y - 5), (x + 5, y + 5), R); c.line((x + 5, y - 5), (x - 5, y + 5), R)
        c.arc((x - 7, y - 7, x + 7, y + 7), 0, 360, R)
    elif name == 'eye':
        c.ell((x - 8, y - 4, x + 8, y + 4), WH, WH); c.ell((x - 3, y - 3, x + 3, y + 3), R, R); c.p(x, y, K)
    if lost:
        c.line((cx - 10, cy - 10), (cx + 10, cy + 10), R)
        c.line((cx + 10, cy - 10), (cx - 10, cy + 10), R)


# ------------------------------------------------------------------ effect transforms
def t_wound(c, sev):
    if sev >= 3:
        c.drect((0, 0, W - 1, H - 1), 0, R, lambda x, y: 0.01 * sev * (1 - abs(x - 84) / 84) if c.g(x, y) == K else 0)
    x0 = c.r.randint(50, 100)
    for k in range(0 if sev <= 1 else 1 + min(sev, 3)):
        pts = []
        for i in range(14):
            t = i / 13
            pts.append((x0 + k * 7 + t * 46 - 23 + c.r.randint(-1, 1), 8 + t * 84))
        c.d.line(pts, fill=R, width=2 if sev >= 2 else 1)
        c.d.line([(p[0] + 2, p[1]) for p in pts[2:-2]], fill=WH)
    for _ in range(4 + sev * 3):
        cx, cy = c.r.randint(10, W - 10), c.r.randint(10, H - 10)
        for _ in range(c.r.randint(3, 9)):
            c.p(cx + c.r.randint(-3, 3), cy + c.r.randint(-2, 2), R)
    for _ in range(sev + 2):
        c.drip(c.r.randint(4, W - 4), 0, c.r.randint(4, 10 + sev * 4))


def t_madness(c, sev):
    S, PW, PH = G.S, G.PW, G.PH
    src = c.im.copy()
    amp = min(4, 1 + sev) * S
    ph = c.r.random() * 6
    for Y in range(PH):
        sh = int(round(amp * math.sin(Y / (4.0 * S) + ph)))
        c.im.paste(src.crop((0, Y, PW, Y + 1)), (sh, Y))
    if sev >= 3:
        y0 = c.r.randint(20, 70) * S
        px = c.im.load()
        for Y in range(y0, min(PH, y0 + (8 + sev * 2) * S)):
            for X in range(PW):
                if px[X, Y] == K:
                    px[X, Y] = WH
                elif px[X, Y] == WH:
                    px[X, Y] = K
    for _ in range(2 + sev * 2):
        for _try in range(20):
            x, y = c.r.randint(8, W - 8), c.r.randint(6, H - 6)
            if all(c.g(x + dx, y) == K for dx in (-4, 0, 4)):
                c.ell((x - 4, y - 2, x + 4, y + 2), WH, WH)
                c.p(x, y, R); c.p(x - 1, y, R)
                break


def t_doom(c, sev):
    for k in range(3 + sev):
        x, y = 84 + c.r.randint(-10, 10), 50 + c.r.randint(-8, 8)
        a = c.r.random() * math.tau
        pts = [(x, y)]
        for _ in range(8 + sev * 2):
            a += c.r.uniform(-0.6, 0.6)
            x += math.cos(a) * 6
            y += math.sin(a) * 4
            pts.append((x, y))
        c.d.line(pts, fill=R, width=3)
        c.d.line(pts, fill=K, width=1)
    # faint sigil
    cx, cy, rr = 84, 50, 22
    pts = [(cx + rr * math.sin(math.radians(a)), cy - rr * math.cos(math.radians(a))) for a in range(0, 721, 144)]
    for i in range(5):
        for t in range(0, 20):
            if t % 2 == 0:
                p0, p1 = pts[i], pts[i + 1]
                c.p(p0[0] + (p1[0] - p0[0]) * t / 20, p0[1] + (p1[1] - p0[1]) * t / 20, R)
    c.vignette(1.0 + 0.15 * sev)


def t_heal(c, sev):
    c.glow(84, -6, 70 + sev * 8, 0.3 + 0.05 * sev, WH)
    for _ in range(3 + sev * 2):
        x, y = c.r.randint(10, W - 10), c.r.randint(6, H - 20)
        c.p(x, y); c.p(x - 1, y); c.p(x + 1, y); c.p(x, y - 1); c.p(x, y + 1)


def t_bless(c, sev):
    for k in range(9):
        a = math.radians(-60 + k * 15)
        for t in range(0, 110, 2):
            x, y = 84 + math.sin(a) * t, -8 + math.cos(a) * t
            if dith(x, y, 0.55 - t / 220) and 0 <= x < W and 0 <= y < H and c.g(int(x), int(y)) == K:
                c.p(x, y)
    for _ in range(2 + sev):
        x, y = c.r.randint(14, W - 14), c.r.randint(10, H - 30)
        c.p(x, y, R); c.p(x, y - 1, R); c.p(x, y + 1, R); c.p(x - 1, y, R); c.p(x + 1, y, R)


def o_gold(c, amount):
    n = min(26, 6 + amount)
    c.glow(84, 88, 28, 0.35)
    for i in range(n):
        x = 84 + c.r.randint(-16, 16) * (1 - i / (n * 1.6))
        y = 94 - i * 0.55 + c.r.randint(-1, 1)
        c.ell((x - 3, y - 2, x + 3, y + 1), WH, K)
    for _ in range(6):
        x, y = 84 + c.r.randint(-24, 24), c.r.randint(66, 86)
        c.p(x, y); c.p(x, y - 1); c.p(x, y + 1); c.p(x - 1, y); c.p(x + 1, y)


def o_skip(c, n):
    for _ in range(26 + 8 * abs(n)):
        x = c.r.randint(4, W - 4)
        y0 = c.r.randint(0, 70)
        for t in range(c.r.randint(6, 18)):
            if t % 2 == 0:
                c.p(x, y0 + t)
    if n > 0:
        c.ell((56, 84, 112, 99), K, WH)
        c.poly([(80, 60), (88, 60), (84, 68)], R, R)
        c.poly([(80, 70), (88, 70), (84, 78)], R, R)
    else:
        c.poly([(80, 40), (88, 40), (84, 32)], R, R)
        c.poly([(80, 30), (88, 30), (84, 22)], R, R)


def o_items(c, gained, lost):
    names = [(n, False) for n in gained] + [(n, True) for n in lost]
    names = [x for x in names if x[0] in ICON_NAMES][:3]
    for i, (n, l) in enumerate(names):
        cx = 84 + (i - (len(names) - 1) / 2) * 26
        icon(c, n, int(cx), 76, l)


ICON_NAMES = {'torch', 'rope', 'key', 'holy', 'dog', 'map', 'sword', 'amulet', 'potion', 'girl', 'oath', 'crown', 'curse', 'mark', 'eye'}


def generic(base_img, r, seed):
    c = canvas_from(base_img, seed)
    b, m, f = r.get('b', 0), r.get('m', 0), r.get('f', 0)
    gained = [x for x in r.get('set', []) if not x.startswith('_')]
    lost = [x for x in r.get('clr', []) if not x.startswith('_')]
    bad = [x for x in gained if x in BAD]
    effects = []
    if b < 0:
        effects.append(('wound', -b))
    if m < 0:
        effects.append(('madness', -m))
    if f < 0 or bad:
        effects.append(('doom', -min(f, 0) + 3 * len(bad)))
    heal = max(0, b) + max(0, m) + 2 * (r.get('mb', 0) + r.get('mm', 0))
    if heal > 0:
        effects.append(('heal', heal))
    bless = max(0, f) + 2 * r.get('mf', 0)
    if bless > 0:
        effects.append(('bless', bless))
    effects.sort(key=lambda e: -e[1])
    effects = effects[:2]
    order = ['madness', 'doom', 'heal', 'bless', 'wound']
    effects.sort(key=lambda e: order.index(e[0]))
    g = r.get('g', 0)
    sk = r.get('skip', 0)
    if not effects and g <= 0 and not gained and not lost and not sk:
        c.fade(lambda x, y: 0.45)   # quiet: nothing happened
        return c.im
    for kind, mag in effects:
        sev = max(1, min(4, round(mag / 1.5)))
        {'wound': t_wound, 'madness': t_madness, 'doom': t_doom, 'heal': t_heal, 'bless': t_bless}[kind](c, sev)
    if sk:
        o_skip(c, sk)
    if g > 0:
        o_gold(c, g)
    if gained or lost:
        o_items(c, gained, lost)
    return c.im


# ------------------------------------------------------------------ bespoke results
BESPOKE = {}


def bespoke(*keys):
    def deco(fn):
        for k in keys:
            BESPOKE[k] = fn
        return fn
    return deco


@bespoke('e004:0:ok', 'e004:1:ok')
def _(c):
    scene(c, 'room')
    c.glow(84, 66, 40, 0.5)
    c.rect((66, 68, 102, 86), K, WH)
    c.poly([(66, 68), (102, 68), (98, 48), (70, 48)], K, WH)
    for i in range(18):
        x = 84 + c.r.randint(-14, 14)
        c.ell((x - 3, 64 - i % 4, x + 3, 67 - i % 4), WH, K)
    for _ in range(12):
        x, y = 84 + c.r.randint(-30, 30), c.r.randint(30, 62)
        c.p(x, y); c.p(x, y - 1); c.p(x - 1, y); c.p(x + 1, y); c.p(x, y + 1)


@bespoke('e004:0:ng', 'e004:1:ng')
def _(c):
    scene(c, 'room')
    c.drect((0, 0, W - 1, H - 1), 0, R, lambda x, y: 0.03 if c.g(x, y) == K else 0)
    c.rect((60, 70, 108, 90), K, WH)
    c.poly([(60, 70), (108, 70), (112, 36), (56, 36)], K, WH)
    c.ell((64, 56, 104, 76), R, R)
    for x in range(62, 106, 5):
        c.poly([(x, 70), (x + 4, 70), (x + 2, 62)], WH, K)
        c.poly([(x, 38), (x + 4, 38), (x + 2, 47)], WH, K)
    c.d.line([(84, 66), (90, 78), (80, 88), (92, 96)], fill=R, width=3)
    c.p(66, 42, R); c.p(70, 42, R)
    for _ in range(14):
        c.p(c.r.randint(40, 128), c.r.randint(20, 99), R)


@bespoke('e008:0:r')
def _(c):
    scene(c, 'corridor')
    figure(c, 70, 90, 46, head='plain', body='legs', arms='down', eyes=None)
    c.glow(100, 66, 18, 0.3)
    figure(c, 100, 90, 28, head='girl', body='dress', arms='down', eyes=None, fill=WH, out=WH)
    c.drect((90, 64, 112, 90), 0.4, K)
    c.line((77, 72), (91, 76))


@bespoke('e008:1:r')
def _(c):
    scene(c, 'corridor')
    c.glow(84, 60, 40, 0.5)
    figure(c, 84, 88, 30, head='girl', body='dress', arms='up', eyes=None, fill=WH, out=WH)
    c.fade(lambda x, y: 0.35 + 0.65 * (y < 70))
    for _ in range(60):
        x, y = 84 + c.r.randint(-26, 26), c.r.randint(10, 80)
        c.p(x, y)


@bespoke('e008:2:ng')
def _(c):
    c.ell((34, 6, 134, 112), WH, WH)
    c.poly([(30, 30), (138, 30), (150, 100), (18, 100)], WH, WH)
    c.ell((44, 18, 124, 104), K, K)
    c.ell((58, 42, 78, 56), WH, WH); c.ell((90, 42, 110, 56), WH, WH)
    c.ell((64, 45, 72, 53), R, R); c.ell((96, 45, 104, 53), R, R)
    c.ell((76, 70, 92, 92), R, K)
    c.drip(68, 56, 14); c.drip(100, 56, 18)
    c.vignette(1.2)


@bespoke('e019:0:r')
def _(c):
    scene(c, 'room')
    G.chain(c, 120, 0, 18)
    c.ell((102, 16, 138, 30), K, WH)
    c.rect((102, 23, 138, 70), K, WH)
    for x in range(102, 139, 6):
        c.line((x, 23), (x, 70))
    c.poly([(102, 70), (90, 60), (90, 26), (102, 23)], K, WH)
    figure(c, 60, 90, 38, head='plain', body='legs', arms='out', eyes=WH)
    G.P['dog'](c)


@bespoke('e020:0:r', 'e020:1:ok')
def _(c):
    scene(c, 'corridor')
    figure(c, 66, 92, 48, head='plain', body='legs', arms='down', eyes=None)
    x, y = 100, 84
    c.ell((x - 12, y - 6, x + 8, y + 4), K, WH)
    c.poly([(x + 4, y - 4), (x + 8, y - 16), (x + 16, y - 14), (x + 14, y - 4)], K, WH)
    c.poly([(x + 9, y - 14), (x + 10, y - 20), (x + 13, y - 15)], K, WH)
    c.line((x - 8, y + 4), (x - 8, y + 8)); c.line((x + 4, y + 4), (x + 4, y + 8))
    c.line((x - 12, y - 2), (x - 18, y - 8))
    c.p(x + 12, y - 11, R)
    c.glow(84, 70, 30, 0.2)


@bespoke('e023:0:r')
def _(c):
    scene(c, 'corridor')
    figure(c, 84, 92, 52, head='helm', body='armor', arms='up', eyes=R)
    c.line((97, 40), (102, 6)); c.line((98, 40), (103, 6)); c.line((94, 36), (102, 37))
    c.glow(102, 10, 16, 0.5)


@bespoke('e032:0:ok', 'e032:1:ok')
def _(c):
    scene(c, 'room')
    c.glow(84, 26, 46, 0.55)
    G.rock(c, 84, 98, 44, 12)
    figure(c, 84, 90, 46, head='plain', body='legs', arms='up', eyes=None)
    c.line((84, 44), (84, 6)); c.line((85, 44), (85, 6))
    c.line((78, 42), (91, 42)); c.p(84, 46, R)


@bespoke('e039:0:r')
def _(c):
    c.poly([(30, 100), (50, 40), (80, 20), (120, 22), (140, 60), (150, 100)], K, WH)
    c.arc((60, 6, 120, 46), 180, 360)
    for k in range(3):
        c.arc((76 + k, 44 + k, 116 - k, 84 - k), 0, 360, R)
    for a in range(0, 360, 60):
        x, y = 96 + 14 * math.cos(math.radians(a)), 64 + 14 * math.sin(math.radians(a))
        c.line((96, 64), (x, y), R)
    c.glow(96, 64, 30, 0.3, R)
    c.drip(90, 80, 10); c.drip(104, 78, 14)


@bespoke('e045:0:r', 'e045:2:r')
def _(c):
    scene(c, 'crypt')
    x, y = 70, 92
    c.poly([(x - 14, y), (x - 10, y - 26), (x + 8, y - 28), (x + 14, y)], K, WH)
    c.ell((x - 8, y - 40, x + 8, y - 24), K, WH)
    c.line((x - 5, y - 32), (x + 5, y - 32), R)
    c.drect((x - 30, y - 4, x + 40, y + 4), 0.6, R)
    c.line((x + 14, y - 14), (x + 46, y - 30)); c.line((x + 14, y - 13), (x + 46, y - 29))
    c.glow(x + 46, y - 30, 14, 0.5)
    figure(c, 128, 92, 44, head='plain', body='legs', arms='out', eyes=None)


@bespoke('e046:0:r')
def _(c):
    scene(c, 'crypt')
    c.glow(84, 20, 70, 0.55)
    c.ell((70, 50, 98, 66), K, WH); c.rect((70, 57, 98, 92), K, WH); c.line((71, 57), (97, 57), K)
    for i, x in enumerate((76, 82, 88, 92)):
        c.line((x, 92), (x - 2, 86)); c.p(x - 2, 85, R)
    figure(c, 84, 40, 24, head='girl', body='dress', arms='up', eyes=None, fill=WH, out=WH)
    c.fade(lambda x, y: 0.5 + 0.5 * (y > 44))


@bespoke('e050:0:ok')
def _(c):
    scene(c, 'cave')
    c.arc((40, 10, 128, 70), 20, 160)
    c.arc((40, 12, 128, 72), 20, 160)
    for x in range(52, 120, 6):
        c.line((x, 64 + abs(x - 84) // 12), (x - 1, 70 + abs(x - 84) // 12))
    c.glow(84, 50, 30, 0.2)


@bespoke('e050:0:ng')
def _(c):
    c.ell((6, 4, 162, 98), WH, WH)
    for _ in range(30):
        x, y = c.r.randint(10, 158), c.r.randint(8, 92)
        pts = [(x, y)]
        for _ in range(5):
            x += c.r.randint(-6, 6); y += c.r.randint(-4, 4); pts.append((x, y))
        c.d.line(pts, fill=R)
    c.ell((50, 12, 118, 90), R, R)
    c.ell((70, 26, 98, 76), K, K)
    c.vignette(1.3)


@bespoke('e060:0:ok', 'e060:1:ok')
def _(c):
    scene(c, 'ruins')
    c.rect((62, 20, 106, 78), K, WH)
    c.rect((56, 54, 112, 84), K, WH)
    for _ in range(60):
        c.p(84 + c.r.randint(-12, 12), c.r.randint(36, 54))
    figure(c, 140, 94, 40, head='plain', body='legs', arms='up', eyes=None)
    c.glow(146, 46, 18, 0.5)
    c.poly([(138, 50), (140, 44), (143, 48), (146, 42), (149, 48), (152, 44), (154, 50)], R, R)


@bespoke('e069:1:ok')
def _(c):
    scene(c, 'fungus')
    c.glow(84, 70, 34, 0.45)
    c.arc((60, 60, 108, 100), 200, 340)
    c.poly([(62, 84), (70, 76), (74, 86), (80, 78), (84, 88)], K, WH)
    c.poly([(88, 88), (94, 78), (98, 86), (104, 76), (106, 84)], K, WH)
    x, y = 84, 70
    c.ell((x - 9, y - 6, x + 9, y + 8), WH, WH)
    c.ell((x + 2, y - 14, x + 14, y - 4), WH, WH)
    c.poly([(x - 4, y - 4), (x - 18, y - 14), (x - 8, y + 2)], WH, K)
    c.p(x + 10, y - 10, R)
    c.line((x - 8, y + 6), (x - 16, y + 10))


@bespoke('e069:1:ng')
def _(c):
    scene(c, 'fungus')
    c.drect((0, 0, W - 1, H - 1), 0, R, lambda x, y: 0.03 if c.g(x, y) == K else 0)
    c.poly([(60, 96), (64, 60), (76, 50), (92, 50), (104, 60), (108, 96)], K, WH)
    for k in range(9):
        a = math.radians(-160 + k * 18)
        x, y = 84, 56
        pts = [(x, y)]
        for t in range(10):
            x += math.cos(a + math.sin(t + k) * 0.5) * 6
            y += math.sin(a + math.sin(t + k) * 0.5) * 6
            pts.append((x, y))
        c.d.line(pts, fill=WH, width=2)
        c.p(pts[-1][0], pts[-1][1], R)
    for _ in range(10):
        x, y = 84 + c.r.randint(-14, 14), c.r.randint(56, 90)
        c.ell((x - 2, y - 1, x + 2, y + 1), WH, WH); c.p(x, y, R)


@bespoke('e085:0:ok')
def _(c):
    c.glow(84, 50, 70, 0.45)
    figure(c, 84, 96, 56, head='plain', body='dress', arms='out', eyes=None, fill=WH, out=WH)
    c.fade(lambda x, y: 0.6 + 0.4 * (abs(x - 84) < 20))


@bespoke('e085:0:ng')
def _(c):
    c.ell((30, 4, 138, 120), WH, WH)
    c.ell((40, 30, 128, 96), K, K)
    for x in range(44, 126, 6):
        c.poly([(x, 34), (x + 5, 34), (x + 2, 46)], WH, K)
        c.poly([(x, 92), (x + 5, 92), (x + 2, 80)], WH, K)
    c.ell((64, 56, 104, 76), R, K)
    c.vignette(1.3)


@bespoke('g025:0:r', 'g025:1:r')
def _(c):
    scene(c, 'crypt')
    for _ in range(70):
        G.skull(c, c.r.randint(20, 148), c.r.randint(60, 98), R if c.r.random() < 0.05 else K)
    for _ in range(30):
        x, y = c.r.randint(30, 138), c.r.randint(56, 98)
        c.line((x - 4, y), (x + 4, y + c.r.randint(-2, 2)))
    figure(c, 84, 70, 30, head='plain', body='legs', arms='down', eyes=None)
    c.glow(84, 30, 40, 0.3)


@bespoke('g050:0:r')
def _(c):
    scene(c, 'ruins')
    for (x0, y0, x1, y1) in ((30, 80, 60, 98), (62, 74, 100, 98), (104, 82, 140, 98), (70, 60, 92, 76)):
        c.rect((x0, y0, x1, y1), K, WH)
    c.ell((76, 64, 88, 74), K, R)
    for _ in range(10):
        c.p(c.r.randint(60, 108), c.r.randint(30, 60), R)
    figure(c, 84, 60, 26, head='plain', body='legs', arms='up', eyes=None)


@bespoke('g050:1:r')
def _(c):
    scene(c, 'ruins')
    c.rect((84, 50, 132, 82), K, WH)
    c.rect((96, 34, 120, 50), K, WH)
    c.line((100, 42), (116, 42), WH)
    c.rect((80, 82, 96, 98), K, WH); c.rect((116, 82, 136, 98), K, WH)
    c.ell((102, 58, 114, 70), K, WH)
    figure(c, 46, 92, 44, head='plain', body='legs', arms='up', eyes=None)
    c.glow(52, 44, 14, 0.5)
    c.poly([(44, 48), (46, 42), (49, 46), (52, 40), (55, 46), (58, 42), (60, 48)], R, R)


@bespoke('g075:0:r')
def _(c):
    scene(c, 'chasm')
    for s in (-1, 1):
        c.poly([(84, 54), (84 + s * 30, 34), (84 + s * 50, 44), (84 + s * 22, 62)], K, WH)
    c.ell((74, 44, 94, 74), K, WH)
    c.poly([(80, 74), (84, 98), (88, 74)], K, WH)
    c.line((84, 30), (84, 58), WH); c.line((85, 30), (85, 58), WH)
    c.drect((76, 46, 92, 72), 0.3, R)
    for _ in range(20):
        c.p(c.r.randint(60, 108), c.r.randint(30, 99), R)


@bespoke('g075:1:r')
def _(c):
    scene(c, 'chasm')
    G.P['dragon'](c)
    c.glow(130, 70, 20, 0.35)
    figure(c, 130, 98, 34, head='helm', body='armor', arms='up', eyes=R)
    c.line((140, 66), (120, 30)); c.line((141, 66), (121, 30))
    figure(c, 30, 98, 24, head='plain', body='legs', arms='down', eyes=None)


def ending_base(c):
    G.bg_void(c)
    c.fade(lambda x, y: 0.8)


@bespoke('g100:0:r')
def _(c):
    ending_base(c)
    c.glow(84, 0, 110, 0.6)
    figure(c, 72, 70, 50, head='plain', body='dress', arms='out', eyes=None, fill=WH, out=WH)
    figure(c, 92, 70, 28, head='girl', body='dress', arms='up', eyes=None, fill=WH, out=WH)
    c.fade(lambda x, y: 0.55 + 0.45 * (y > 30))
    figure(c, 84, 100, 14, head='plain', body='legs', eyes=None)


@bespoke('g100:1:r')
def _(c):
    ending_base(c)
    c.glow(84, 50, 50, 0.4)
    figure(c, 76, 96, 46, head='plain', body='legs', arms='out', eyes=None)
    figure(c, 98, 96, 42, head='girl', body='dress', arms='down', eyes=None, fill=WH, out=WH)
    c.poly([(92, 56), (94, 51), (97, 54), (100, 50), (103, 54), (106, 51), (108, 56)], R, R)
    c.ell((20, 74, 38, 92), K, WH); c.line((24, 82), (34, 82), R)


@bespoke('g100:2:r')
def _(c):
    ending_base(c)
    for k in range(14):
        a = k / 14 * math.tau
        x, y = 84, 50
        pts = [(x, y)]
        for _ in range(9):
            a += c.r.uniform(-0.3, 0.3)
            x += math.cos(a) * 9; y += math.sin(a) * 7
            pts.append((x, y))
        c.d.line(pts, fill=WH, width=2)
    c.glow(84, 50, 40, 0.7)
    figure(c, 84, 100, 30, head='plain', body='legs', arms='up', eyes=None)


@bespoke('g100:3:r')
def _(c):
    c.im.paste(K, (0, 0, W, H))
    c.drect((0, 0, W - 1, 59), 0, WH, lambda x, y: 0.75 - y / 90)
    c.poly([(0, 60), (40, 40), (70, 52), (110, 36), (168, 56), (168, 100), (0, 100)], K, WH)
    door(c) if False else None
    c.ell((70, 62, 98, 90), K, WH); c.rect((70, 76, 98, 100), K, WH)
    figure(c, 120, 96, 30, head='plain', body='legs', arms='up', eyes=None)


@bespoke('g100:4:r')
def _(c):
    ending_base(c)
    c.rect((62, 30, 106, 84), K, WH)
    c.rect((54, 60, 114, 90), K, WH)
    for x in (62, 106):
        c.poly([(x - 4, 30), (x, 16), (x + 4, 30)], K, WH)
    figure(c, 84, 82, 40, head='hood', body='robe', arms='down', eyes=R)
    for i in range(10):
        r_ = 30 + i * 9
        c.arc((84 - r_ * 1.4, 56 - r_, 84 + r_ * 1.4, 56 + r_), 200, 340, R if i % 3 == 0 else WH)


# ------------------------------------------------------------------ main
def door(c):
    pass


def effects_for(r, light=False):
    """[(kind, severity)] derived from a result's numbers."""
    b, m, f = r.get('b', 0), r.get('m', 0), r.get('f', 0)
    bad = [x for x in r.get('set', []) if x in BAD]
    eff = []
    if b < 0: eff.append(('wound', -b))
    if m < 0: eff.append(('mad', -m))
    if f < 0 or bad: eff.append(('doom', -min(f, 0) + 3 * len(bad)))
    heal = max(0, b) + max(0, m) + 2 * (r.get('mb', 0) + r.get('mm', 0))
    if heal > 0: eff.append(('heal', heal))
    bless = max(0, f) + 2 * r.get('mf', 0)
    if bless > 0: eff.append(('bless', bless))
    eff.sort(key=lambda e: -e[1])
    out = []
    for kind, mag in eff[:2]:
        sev = max(1, min(4, round(mag / 1.5)))
        if light:
            sev = max(1, sev - 1)
        out.append((kind, sev))
    return out


FXFN = {'wound': t_wound, 'mad': t_madness, 'doom': t_doom, 'heal': t_heal, 'bless': t_bless}
FX_ORDER = ['mad', 'doom', 'heal', 'bless', 'wound']


def apply_fx(c, fx):
    fx.sort(key=lambda e: FX_ORDER.index(e[0]) if e[0] in FX_ORDER else 9)
    for kind, sev in fx:
        if kind in FXFN:
            FXFN[kind](c, sev)
        elif kind == 'quiet':
            c.fade(lambda x, y: 0.5)
        elif kind == 'dark':
            c.vignette(1.6)
        elif kind == 'red':
            c.drect((0, 0, W - 1, H - 1), 0, R, lambda x, y: 0.04 if c.g(x, y) == K else 0)


def corner_icons(c, r):
    gained = [x for x in r.get('set', []) if x in ICON_NAMES]
    lost = [x for x in r.get('clr', []) if x in ICON_NAMES]
    for i, (n, l) in enumerate([(g, False) for g in gained] + [(g, True) for g in lost]):
        icon(c, n, W - 14 - i * 24, 13, l)


def render_result(e, ci, br, base, bg_only):
    import scene_kit, result_scenes
    ch = e['c'][ci]
    r = ch[br]
    key = '%s:%d:%s' % (e['id'], ci, br)
    sd = seed_of(key)
    if key in BESPOKE:
        c = C(sd)
        BESPOKE[key](c)
        c.vignette(0.9)
        return c.im, 'bespoke'
    spec = result_scenes.SCENES.get(key)
    if spec:
        c, fxs, auto, icons = scene_kit.compose(spec, e, sd, base, bg_only)
        fx = []
        for f in fxs:
            if f in ('quiet', 'dark', 'red'):
                fx.append((f, 1))
            else:
                fx.append((f.rstrip('0123456789'), int(f[len(f.rstrip('0123456789')):] or 2)))
        if auto and not fxs:
            fx = effects_for(r, light=True)
        apply_fx(c, fx)
        if icons:
            corner_icons(c, r)
        c.vignette(0.9)
        return c.im, 'scene'
    return generic(base, r, sd), 'generic'


def bg_only_img(e):
    bg, pr = e['a'].split(':')
    c = C(seed_of(e['id']))
    if bg == 'stairs':
        G.bg_stairs(c, flip=(pr == 'inverted'))
    else:
        G.BGS[bg](c)
    c.fade(lambda x, y: G.BG_DIM.get(bg, 0.5))
    return c.im


def main():
    out = os.path.join(ROOT, 'art', 'results')
    os.makedirs(out, exist_ok=True)
    ev = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data/events/*.json'))):
        ev += json.load(open(f))
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
    imgs = []
    kinds = {}
    for e in ev:
        if only and e['id'] not in only:
            continue
        base = G.render(e['a'], seed_of(e['id']))
        bgi = bg_only_img(e)
        for ci, ch in enumerate(e['c']):
            for br in ('r', 'ok', 'ng'):
                if br not in ch:
                    continue
                im, kind = render_result(e, ci, br, base, bgi)
                kinds[kind] = kinds.get(kind, 0) + 1
                name = '%s_%d_%s' % (e['id'], ci, br)
                im.save(os.path.join(out, name + '.png'))
                imgs.append((name, im))
    print('wrote', len(imgs), kinds)
    if '--sheet' in sys.argv:
        dest = sys.argv[sys.argv.index('--sheet') + 1]
        pick = imgs[:60]
        cols = 4
        rows = (len(pick) + cols - 1) // cols
        PW, PH = G.PW, G.PH
        sheet = Image.new('RGB', (cols * (PW + 4), rows * (PH + 14)), (60, 60, 60))
        d = ImageDraw.Draw(sheet)
        for i, (n, im) in enumerate(pick):
            x, y = (i % cols) * (PW + 4), (i // cols) * (PH + 14)
            sheet.paste(im, (x, y))
            d.text((x + 2, y + PH), n, fill=(255, 255, 255))
        sheet.save(dest)


if __name__ == '__main__':
    main()
