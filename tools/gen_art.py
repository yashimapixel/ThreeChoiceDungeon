"""Procedural 3-colour (black / white / red) pixel-art generator for event scenes.

Usage: python3 -I tools/gen_art.py            -> writes art/events/<id>.png (336x200)
       python3 -I tools/gen_art.py --sheet    -> also writes a contact sheet to /tmp
Each event's "a" field is "<background>:<prop>".
"""
import json, glob, math, os, random, sys
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 168, 100
K = (14, 12, 14)
WH = (232, 226, 212)
R = (196, 28, 40)
B4 = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


S = 2                      # output scale: drawing code uses 168x100 coords,
PW, PH = W * S, H * S      # images are rendered at the game's native 336x200


def dith(x, y, lv):
    return B4[int(y) & 3][int(x) & 3] < lv * 16


def _pt(v):
    return v * S + (S - 1) / 2


def _box(b):
    x0, y0, x1, y1 = b
    return (x0 * S, y0 * S, x1 * S + S - 1, y1 * S + S - 1)


def _pts(xy):
    xy = list(xy)
    if xy and not isinstance(xy[0], (tuple, list)):
        xy = list(zip(xy[0::2], xy[1::2]))
    return [(_pt(x), _pt(y)) for x, y in xy]


class SD:
    """ImageDraw proxy: takes 168x100 logical coordinates, draws at native resolution."""
    def __init__(s, im):
        s.d = ImageDraw.Draw(im)

    def line(s, xy, fill=None, width=1):
        s.d.line(_pts(xy), fill=fill, width=width)

    def polygon(s, xy, fill=None, outline=None):
        s.d.polygon(_pts(xy), fill=fill, outline=outline)

    def ellipse(s, box, fill=None, outline=None):
        s.d.ellipse(_box(box), fill=fill, outline=outline)

    def rectangle(s, box, fill=None, outline=None):
        s.d.rectangle(_box(box), fill=fill, outline=outline)

    def arc(s, box, a0, a1, fill=None, width=1):
        s.d.arc(_box(box), a0, a1, fill=fill, width=width)


class C:
    def __init__(s, seed):
        s.im = Image.new('RGB', (PW, PH), K)
        s.d = SD(s.im)
        s.r = random.Random(seed)

    @classmethod
    def from_image(cls, img, seed):
        c = cls(seed)
        c.im = img.copy()
        c.d = SD(c.im)
        return c

    def reset_draw(s):
        s.d = SD(s.im)

    # --- primitives (logical coordinates) ----------------------------------
    def p(s, x, y, c=WH):
        """One logical pixel = an SxS block (keeps tiny details like eyes readable)."""
        x, y = int(round(x)), int(round(y))
        if 0 <= x < W and 0 <= y < H:
            s.im.paste(c, (x * S, y * S, x * S + S, y * S + S))

    def px1(s, x, y, c=WH):
        """A single native pixel at a (fractional) logical position."""
        X, Y = int(round(x * S)), int(round(y * S))
        if 0 <= X < PW and 0 <= Y < PH:
            s.im.putpixel((X, Y), c)

    def g(s, x, y):
        X, Y = int(x) * S, int(y) * S
        if 0 <= X < PW and 0 <= Y < PH:
            return s.im.getpixel((X, Y))
        return K

    def clear(s, box, c=K):
        x0, y0, x1, y1 = box
        s.im.paste(c, (int(x0 * S), int(y0 * S), int(x1 * S), int(y1 * S)))

    def line(s, a, b, c=WH, w=1):
        s.d.line([tuple(a), tuple(b)], fill=c, width=w)

    def poly(s, pts, fill=K, out=WH):
        s.d.polygon([tuple(p) for p in pts], fill=fill, outline=out)

    def ell(s, box, fill=K, out=WH):
        s.d.ellipse(box, fill=fill, outline=out)

    def rect(s, box, fill=K, out=WH):
        s.d.rectangle(box, fill=fill, outline=out)

    def arc(s, box, a0, a1, c=WH):
        s.d.arc(box, a0, a1, fill=c)

    def mask(s, draw_fn):
        m = Image.new('L', (PW, PH), 0)
        draw_fn(SD(m))
        return m

    def dpoly(s, pts, lv, c=WH, fn=None):
        m = s.mask(lambda d: d.polygon([tuple(p) for p in pts], fill=255))
        s.dmask(m, lv, c, fn)

    def dell(s, box, lv, c=WH):
        m = s.mask(lambda d: d.ellipse(box, fill=255))
        s.dmask(m, lv, c)

    def dmask(s, m, lv, c=WH, fn=None):
        mp = m.load()
        ip = s.im.load()
        for Y in range(PH):
            for X in range(PW):
                if mp[X, Y]:
                    l = fn(X / S, Y / S) if fn else lv
                    if dith(X, Y, l):
                        ip[X, Y] = c

    def drect(s, box, lv, c=WH, fn=None):
        x0, y0, x1, y1 = box
        ip = s.im.load()
        for Y in range(max(0, int(y0 * S)), min(PH, int(y1 * S) + S)):
            for X in range(max(0, int(x0 * S)), min(PW, int(x1 * S) + S)):
                l = fn(X / S, Y / S) if fn else lv
                if dith(X, Y, l):
                    ip[X, Y] = c

    def glow(s, cx, cy, r, lv, c=WH, only_black=True):
        ip = s.im.load()
        for Y in range(max(0, int((cy - r) * S)), min(PH, int((cy + r) * S) + 1)):
            for X in range(max(0, int((cx - r) * S)), min(PW, int((cx + r) * S) + 1)):
                dd = math.hypot(X / S - cx, (Y / S - cy) * 1.2)
                if dd < r:
                    l = lv * (1 - dd / r) ** 1.4
                    if dith(X, Y, l) and (not only_black or ip[X, Y] == K):
                        ip[X, Y] = c

    def speck(s, box, n, c=WH):
        x0, y0, x1, y1 = box
        for _ in range(n):
            s.px1(s.r.uniform(x0, x1), s.r.uniform(y0, y1), c)

    def fade(s, fn):
        """Darkness: keep a non-black pixel only where dither < visibility."""
        ip = s.im.load()
        for Y in range(PH):
            for X in range(PW):
                if ip[X, Y] != K and not dith(X, Y, fn(X / S, Y / S)):
                    ip[X, Y] = K

    def vignette(s, k=1.0):
        s.fade(lambda x, y: 1.6 - k * 1.25 * max(abs(x - W / 2) / (W / 2), abs(y - H / 2) / (H / 2)) ** 3)

    def eyes(s, x, y, gap=2, c=R):
        s.p(x - gap // 2 - (gap % 2), y, c)
        s.p(x + gap // 2, y, c)

    def drip(s, x, y, n, c=R):
        s.line((x, y), (x, y + n), c, 2)
        s.p(x, y + n, c)


# --- reusable figures ----------------------------------------------------------

def figure(c, x, yb, h, head='hood', body='robe', arms='down', eyes=R, out=WH, fill=K, face=True):
    hs = max(2.0, h * 0.11)
    top = yb - h
    hy = top + hs
    neck = top + hs * 2
    sh = top + hs * 2.5
    sw = max(3.0, h * 0.15)
    hip = yb - h * 0.42
    # body
    if body in ('robe', 'dress'):
        flare = h * (0.24 if body == 'robe' else 0.27)
        c.poly([(x - sw * 0.5, neck), (x + sw * 0.5, neck), (x + sw, sh + 2), (x + flare, yb), (x - flare, yb), (x - sw, sh + 2)], fill, out)
        if body == 'robe':
            c.line((x, sh + 4), (x, yb - 1), out if fill == K else K)
    elif body in ('legs', 'armor'):
        k = 1.25 if body == 'armor' else 1.0
        c.poly([(x - sw * 0.5, neck), (x + sw * 0.5, neck), (x + sw * k, sh + 1), (x + sw * 0.75, hip), (x - sw * 0.75, hip), (x - sw * k, sh + 1)], fill, out)
        c.poly([(x - sw * 0.75, hip), (x - 0.5, hip), (x - 1, yb), (x - sw * 0.85, yb)], fill, out)
        c.poly([(x + 0.5, hip), (x + sw * 0.75, hip), (x + sw * 0.85, yb), (x + 1, yb)], fill, out)
        if body == 'armor':
            c.ell((x - sw * 1.6, sh - 1, x - sw * 0.6, sh + 4), fill, out)
            c.ell((x + sw * 0.6, sh - 1, x + sw * 1.6, sh + 4), fill, out)
            c.line((x - sw * 0.75, hip - 2), (x + sw * 0.75, hip - 2))
    elif body == 'bones':
        c.line((x, neck), (x, hip))
        for i in range(3):
            yy = sh + 1 + i * 2
            c.line((x - sw * 0.7, yy), (x + sw * 0.7, yy))
        c.line((x - sw * 0.5, hip), (x + sw * 0.5, hip))
        c.line((x - 1, hip), (x - sw * 0.7, yb))
        c.line((x + 1, hip), (x + sw * 0.7, yb))
    # arms (2px sleeves for clothed bodies)
    thick = body not in ('bones',)
    ax = sw * (1.35 if body == 'armor' else 1.0)
    ln = h * 0.34
    def limb(x0, y0, x1, y1):
        if thick:
            c.poly([(x0 - 1, y0), (x0 + 1, y0), (x1 + 1, y1), (x1 - 1, y1)], fill, out)
        else:
            c.line((x0, y0), (x1, y1))
    if arms == 'down':
        limb(x - ax, sh + 1, x - ax - 1.5, sh + ln); limb(x + ax, sh + 1, x + ax + 1.5, sh + ln)
    elif arms == 'up':
        limb(x - ax, sh + 1, x - ax - h * 0.12, top - 1); limb(x + ax, sh + 1, x + ax + h * 0.12, top - 1)
    elif arms == 'out':
        limb(x - ax, sh + 1, x - ax - h * 0.25, sh + h * 0.12); limb(x + ax, sh + 1, x + ax + h * 0.25, sh + h * 0.12)
    elif arms == 'pray':
        limb(x - ax, sh + 1, x - 1, sh + h * 0.2); limb(x + ax, sh + 1, x + 1, sh + h * 0.2)
    # head
    if head == 'hood':
        c.poly([(x - hs * 1.6, sh + 2), (x - hs * 1.5, hy), (x - hs * 0.8, top - hs * 0.3), (x + hs * 0.2, top - hs * 0.8),
                (x + hs * 1.1, top - hs * 0.1), (x + hs * 1.6, hy + hs * 0.4), (x + hs * 1.6, sh + 2)], fill, out)
        if face:
            c.ell((x - hs * 0.85, hy - hs * 0.5, x + hs * 0.85, hy + hs * 1.1), K, K)
            if eyes:
                c.eyes(x, int(round(hy + hs * 0.2)), 2, eyes)
    elif head == 'witch':
        c.ell((x - hs, hy - hs, x + hs, hy + hs), fill, out)
        c.poly([(x - hs * 2.4, hy - hs * 0.7), (x + hs * 2.4, hy - hs * 0.7), (x + hs * 0.9, hy - hs * 1.1),
                (x + hs * 2.2, top - hs * 3.2), (x - hs * 0.9, hy - hs * 1.1)], fill, out)
        c.ell((x - hs * 0.6, hy - hs * 0.4, x + hs * 0.6, hy + hs * 0.8), K, K)
        if eyes:
            c.eyes(x, int(round(hy + hs * 0.1)), 2, eyes)
    elif head == 'helm':
        c.ell((x - hs * 1.05, top - 1, x + hs * 1.05, top + hs * 1.6), fill, out)
        c.rect((x - hs * 1.05, top + hs * 0.8, x + hs * 1.05, neck + 1), fill, out)
        c.line((x - hs * 1.05 + 1, top + hs * 0.8), (x + hs * 1.05 - 1, top + hs * 0.8), fill)
        c.line((x - hs * 0.7, hy + 1), (x + hs * 0.7, hy + 1), eyes or out)
        c.line((x, top - 1), (x - hs, top - hs * 1.5), out)
    elif head == 'skull':
        c.ell((x - hs, top, x + hs, top + hs * 2), WH, WH)
        c.p(x - 1, hy, K); c.p(x + 1, hy, K); c.p(x, hy + hs * 0.8, K)
        if eyes and eyes != K:
            c.p(x - 1, hy, eyes); c.p(x + 1, hy, eyes)
    elif head == 'none':
        c.line((x - 2, neck), (x + 2, neck), R)
        c.drip(x - 1, neck - 2, 1); c.drip(x + 1, neck - 3, 2)
    elif head == 'girl':
        c.poly([(x - hs - 1, hy - hs * 0.2), (x + hs + 1, hy - hs * 0.2), (x + hs + 1.5, sh + 4), (x - hs - 1.5, sh + 4)], fill, out)
        c.ell((x - hs, top, x + hs, top + hs * 2), fill, out)
        c.ell((x - hs * 0.7, top + hs * 0.6, x + hs * 0.7, top + hs * 2.1), K, K)
        if eyes:
            c.p(x - 1, hy + 1, eyes); c.p(x + 1, hy + 1, eyes)
    elif head == 'mask':
        c.ell((x - hs, top, x + hs, top + hs * 2.2), WH, out)
        c.p(x - 1, hy, K); c.p(x + 1, hy, K)
        c.line((x - 1, top + hs * 1.6), (x + 1, top + hs * 1.6), R)
    else:
        c.ell((x - hs, top, x + hs, top + hs * 2), fill, out)
        if eyes:
            c.eyes(x, int(round(hy)), 2, eyes)


def skull(c, x, y, eyes=K):
    c.ell((x - 2, y - 2, x + 2, y + 1), WH, WH)
    c.rect((x - 1, y + 1, x + 1, y + 2), WH, WH)
    c.p(x - 1, y - 1, eyes); c.p(x + 1, y - 1, eyes)


def candle(c, x, yb, h=5, flame=R):
    c.rect((x - 1, yb - h, x + 1, yb), WH, WH)
    c.p(x, yb - h - 1, flame); c.p(x, yb - h - 2, flame)
    c.glow(x, yb - h - 2, 9, 0.35)


def torch_wall(c, x, y):
    c.line((x, y), (x, y + 6))
    c.p(x, y - 1, R); c.p(x - 1, y - 2, R); c.p(x + 1, y - 2, R); c.p(x, y - 3, R)
    c.glow(x, y - 2, 16, 0.4)


def door(c, x0, y0, x1, y1, fill=K, out=WH, arch=True, bands=True):
    if arch:
        r = (x1 - x0) / 2
        c.ell((x0, y0, x1, y0 + 2 * r), fill, out)
        c.rect((x0, y0 + r, x1, y1), fill, out)
        c.line((x0 + 1, y0 + r), (x1 - 1, y0 + r), fill)
    else:
        c.rect((x0, y0, x1, y1), fill, out)
    if bands:
        for yy in range(int(y0 + (x1 - x0) / 2 + 3), int(y1), 6):
            c.line((x0, yy), (x1, yy))
        c.line(((x0 + x1) / 2, y0 + 3), ((x0 + x1) / 2, y1))


def rock(c, x, yb, w, h):
    pts = [(x - w / 2, yb), (x - w / 2 + 1, yb - h * 0.6), (x - w / 4, yb - h), (x + w / 5, yb - h * 0.9), (x + w / 2, yb - h * 0.4), (x + w / 2, yb)]
    c.poly(pts, K, WH)


def mushroom(c, x, yb, h, w, spots=True):
    c.rect((x - max(1, w // 8), yb - h, x + max(1, w // 8), yb), K, WH)
    c.ell((x - w / 2, yb - h - w / 3, x + w / 2, yb - h + w / 6), K, WH)
    c.line((x - w / 2 + 1, yb - h + w / 12), (x + w / 2 - 1, yb - h + w / 12), K)
    if spots:
        for _ in range(max(1, w // 6)):
            c.p(x + c.r.randint(-w // 3, w // 3), yb - h - c.r.randint(1, max(1, w // 5)))


def chain(c, x, y0, y1):
    for yy in range(int(y0), int(y1), 3):
        c.p(x, yy); c.p(x, yy + 1)


# --- backgrounds ---------------------------------------------------------------

def bg_corridor(c, lit=0.32, back=(66, 30, 102, 58)):
    ix0, iy0, ix1, iy1 = back
    def L(t, a, b):
        return a + (b - a) * t
    ts = [1 - 0.68 ** k for k in range(1, 8)]
    for t in [0] + ts:
        xl, xr = L(t, 0, ix0), L(t, W - 1, ix1)
        yt, yb = L(t, 0, iy0), L(t, H - 1, iy1)
        c.line((xl, yt), (xl, yb)); c.line((xr, yt), (xr, yb))
        c.line((xl, yb), (xr, yb))
        if t > 0:
            c.line((xl, yt), (xr, yt))
    for fr in [0.2, 0.4, 0.6]:
        c.line((0, H * fr), (ix0, iy0 + (iy1 - iy0) * fr))
        c.line((W - 1, H * fr), (ix1, iy0 + (iy1 - iy0) * fr))
    for fx in [0.2, 0.4, 0.6, 0.8]:
        c.line((W * fx, H - 1), (ix0 + (ix1 - ix0) * fx, iy1))
    c.line((0, 0), (ix0, iy0)); c.line((0, H - 1), (ix0, iy1))
    c.line((W - 1, 0), (ix1, iy0)); c.line((W - 1, H - 1), (ix1, iy1))
    c.rect((ix0, iy0, ix1, iy1), K, K)
    cx, cy = (ix0 + ix1) / 2, (iy0 + iy1) / 2
    c.fade(lambda x, y: (max(abs(x - cx) / (W / 2), abs(y - cy) / (H / 2)) - 0.18) * 1.6)
    


def bg_room(c, lit=0.3):
    bx0, by0, bx1, by1 = 18, 8, 150, 68
    c.line((0, 0), (bx0, by0)); c.line((W - 1, 0), (bx1, by0))
    c.line((0, H - 1), (bx0, by1)); c.line((W - 1, H - 1), (bx1, by1))
    c.rect((bx0, by0, bx1, by1), K, WH)
    for i, yy in enumerate(range(by0 + 8, by1, 8)):
        c.line((bx0, yy), (bx1, yy))
        off = 0 if i % 2 else 9
        for xx in range(bx0 + off, bx1, 18):
            c.line((xx, yy - 8), (xx, yy))
    for _ in range(5):
        x0, y0 = c.r.randint(bx0 + 4, bx1 - 20), c.r.randint(by0 + 2, by1 - 14)
        c.clear((x0, y0, x0 + c.r.randint(8, 22), y0 + c.r.randint(5, 12)))
    for yy in [by1 + 6, by1 + 14, by1 + 25]:
        t = (yy - by1) / (H - by1)
        c.line((bx0 * (1 - t), yy), (bx1 + (W - 1 - bx1) * t, yy))
    for fx in [0.25, 0.5, 0.75]:
        c.line((bx0 + (bx1 - bx0) * fx, by1), (W * fx, H - 1))
    for yy in range(14, H, 14):
        t = yy / H
        c.line((0, yy), (bx0, by0 + (by1 - by0) * t))
        c.line((W - 1, yy), (bx1, by0 + (by1 - by0) * t))
    c.fade(lambda x, y: 0.55 + 0.5 * (abs(x - 84) / 84) ** 2 - 0.25 * (y < by0) - 0.1 * (y > by1))
    


def bg_cave(c, lit=0.3):
    r = c.r
    # back darkness, ceiling and floor rock masses
    top = [(0, 0)]
    for x in range(0, W + 8, 8):
        top.append((x, r.randint(8, 22)))
    top.append((W, 0))
    c.poly(top, K, WH)
    for x in range(6, W, r.randint(9, 14)):
        yb = [p for p in top if p[0] >= x][0][1]
        ln = r.randint(4, 14)
        c.poly([(x - 3, yb - 1), (x + 3, yb - 1), (x, yb + ln)], K, WH)
    bot = [(0, H)]
    for x in range(0, W + 8, 8):
        bot.append((x, r.randint(70, 82)))
    bot.append((W, H))
    c.poly(bot, K, WH)
    
    for _ in range(6):
        rock(c, r.randint(0, W), r.randint(88, 100), r.randint(10, 24), r.randint(6, 14))
    c.speck((0, 0, W - 1, 20), 15)
    c.fade(lambda x, y: 0.4 + 0.9 * abs(x - 84) / 84 + 0.4 * abs(y - 50) / 50)


def bg_stairs(c, lit=0.3, flip=False):
    n = 9
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        def yy(t):
            return H - 1 - (H * 0.62) * (1 - (1 - t) ** 1.6)
        def hw(t):
            return 70 * (1 - t) + 14
        y0, y1 = yy(t0), yy(t1)
        c.poly([(84 - hw(t0), y0), (84 + hw(t0), y0), (84 + hw(t1), y1), (84 - hw(t1), y1)], K, WH)
        c.drect((84 - hw(t0) + 1, y1 + 1, 84 + hw(t0) - 1, y1 + 2), 0.5 * (1 - t0))
    for side in (-1, 1):
        c.line((84 + side * 84, H - 1), (84 + side * 14, H * 0.38))
        c.line((84 + side * 84, 0), (84 + side * 14, H * 0.12))
        for yy2 in range(4, 60, 8):
            c.line((84 + side * 84, yy2 * 1.6), (84 + side * 14, H * 0.12 + yy2 * 0.45))
    c.rect((70, 12, 98, 38), K, K)
    c.fade(lambda x, y: (abs(x - 84) / 84 * 1.2 + (y - 30) / 70) * 1.1)
    if flip:
        c.im = c.im.transpose(Image.FLIP_TOP_BOTTOM)
        c.reset_draw()


def bg_lake(c, lit=0.3, horizon=56):
    r = c.r
    top = [(0, 0)]
    for x in range(0, W + 8, 8):
        top.append((x, r.randint(6, 18)))
    top.append((W, 0))
    c.poly(top, K, WH)
    for x in range(4, W, r.randint(8, 13)):
        c.poly([(x - 2, 10), (x + 2, 10), (x, 10 + r.randint(4, 16))], K, WH)
    # far shore
    sh = [(0, horizon)]
    for x in range(0, W + 6, 6):
        sh.append((x, horizon - r.randint(2, 10)))
    sh.append((W, horizon))
    c.poly(sh, K, WH)
    c.line((0, horizon), (W, horizon))
    for i, yy in enumerate(range(horizon + 3, H, 3)):
        t = (yy - horizon) / (H - horizon)
        for x in range(0, W, 1):
            if r.random() < 0.18 + 0.3 * t and (x // (3 + i % 4)) % 2 == 0:
                c.p(x, yy)
    c.fade(lambda x, y: 0.55 + 0.6 * abs(x - 84) / 84 * (y < horizon) + 0.4 * (y - horizon) / 44 * (y > horizon))


def bg_chasm(c, lit=0.3):
    c.poly([(0, 30), (52, 36), (60, 58), (44, H), (0, H)], K, WH)
    c.poly([(W, 28), (118, 34), (108, 60), (124, H), (W, H)], K, WH)
    for x0, sgn in ((0, 1), (W, -1)):
        for yy in range(40, H, 7):
            c.line((x0, yy), (x0 + sgn * c.r.randint(20, 46), yy + c.r.randint(-2, 2)))
    c.drect((50, 50, 118, H - 1), 0, WH, lambda x, y: 0.12 * (1 - (y - 50) / 50) * (1 - abs(x - 84) / 40))
    for _ in range(25):
        c.p(c.r.randint(56, 110), c.r.randint(40, 99))
    top = [(0, 0)] + [(x, c.r.randint(4, 12)) for x in range(0, W + 8, 8)] + [(W, 0)]
    c.poly(top, K, WH)
    c.fade(lambda x, y: 0.5 + 0.8 * abs(x - 84) / 84 + 0.3 * (1 - y / H))


def bg_library(c, lit=0.3):
    def shelf(x0, x1, y0, y1):
        c.rect((x0, y0, x1, y1), K, WH)
        for yy in range(y0 + 10, y1, 10):
            c.line((x0, yy), (x1, yy))
            x = x0 + 1
            while x < x1 - 1:
                bw = c.r.randint(1, 3)
                bh = c.r.randint(5, 9)
                if c.r.random() < 0.85:
                    c.rect((x, yy - bh, x + bw - 1, yy - 1), K, WH)
                    if c.r.random() < 0.06:
                        c.rect((x, yy - bh, x + bw - 1, yy - 1), R, R)
                x += bw + (1 if c.r.random() < 0.3 else 0)
    shelf(26, 142, 4, 72)
    shelf(0, 22, 0, 90)
    shelf(146, W - 1, 0, 90)
    c.line((22, 90), (0, H)); c.line((146, 90), (W, H))
    c.fade(lambda x, y: 0.65 + 0.35 * abs(x - 84) / 84 - 0.25 * (y < 20))


def bg_crypt(c, lit=0.3):
    bg_room(c, lit)
    for row, yy in enumerate((14, 30, 46)):
        for x in range(26, 146, 16):
            c.ell((x, yy, x + 11, yy + 14), K, WH)
            c.rect((x, yy + 6, x + 11, yy + 13), K, WH)
            c.line((x + 1, yy + 6), (x + 10, yy + 6), K)
            if c.r.random() < 0.8:
                skull(c, x + 6, yy + 10)
    c.fade(lambda x, y: 0.7 + 0.4 * abs(x - 84) / 84)


def bg_shrine(c, lit=0.3):
    bg_room(c, lit * 0.6)
    for x, h in ((10, 100), (40, 80), (128, 80), (158, 100)):
        w = 8 if h == 100 else 6
        c.rect((x - w, 0, x + w, H * h / 100 - 1), K, WH)
        c.rect((x - w - 2, H * h / 100 - 5, x + w + 2, H * h / 100 - 1), K, WH)
        for xx in range(x - w + 3, x + w - 1, 4):
            c.line((xx, 0), (xx, H * h / 100 - 6))
    c.fade(lambda x, y: 0.75 + 0.3 * abs(x - 84) / 84)


def bg_fungus(c, lit=0.3):
    c.drect((0, 0, W - 1, H - 1), 0, WH, lambda x, y: 0.05 * (1 - abs(x - 84) / 84))
    for x, h, w in ((14, 70, 40), (150, 80, 46), (40, 44, 22), (128, 50, 26), (64, 30, 14), (104, 34, 16)):
        mushroom(c, x, 86, h, w)
    c.line((0, 86), (W, 86))
    for _ in range(80):
        c.p(c.r.randint(0, W - 1), c.r.randint(0, 85))
    for x in range(0, W, 6):
        c.line((x, 86), (x + c.r.randint(-2, 2), 86 + c.r.randint(2, 6)))
    c.fade(lambda x, y: 0.6 + 0.4 * abs(x - 84) / 84)


def bg_ruins(c, lit=0.3):
    top = [(0, 0)] + [(x, c.r.randint(2, 9)) for x in range(0, W + 8, 8)] + [(W, 0)]
    c.poly(top, K, WH)
    x = -4
    while x < W:
        bw = c.r.randint(18, 30)
        bh = c.r.randint(26, 52)
        yb = 80
        pts = [(x, yb), (x, yb - bh), (x + bw * 0.3, yb - bh - c.r.randint(0, 8)), (x + bw * 0.6, yb - bh + c.r.randint(0, 6)), (x + bw, yb - bh), (x + bw, yb)]
        c.poly(pts, K, WH)
        for wy in range(yb - bh + 6, yb - 6, 9):
            for wx in range(x + 4, x + bw - 4, 7):
                c.rect((wx, wy, wx + 2, wy + 3), K, WH)
                if c.r.random() < 0.08:
                    c.rect((wx + 1, wy + 1, wx + 1, wy + 2), R, R)
        x += bw + c.r.randint(1, 6)
    c.line((0, 80), (W, 80))
    for yy in (84, 90, 98):
        c.line((0, yy), (W, yy))
    c.fade(lambda x, y: 0.55 + 0.45 * abs(x - 84) / 84 - 0.2 * (y < 30))


def bg_prison(c, lit=0.3):
    bg_room(c, lit)
    for x in range(26, 146, 30):
        c.rect((x, 26, x + 22, 68), K, WH)
        for bx in range(x + 3, x + 22, 4):
            c.line((bx, 26), (bx, 68))
    chain(c, 10, 0, 50); chain(c, 158, 0, 40)
    c.fade(lambda x, y: 0.7 + 0.35 * abs(x - 84) / 84)


def bg_flesh(c, lit=0.3):
    for i in range(14):
        rr = 8 + i * 7
        c.arc((84 - rr * 1.3, 48 - rr, 84 + rr * 1.3, 48 + rr), 0, 360)
    for _ in range(18):
        x, y = c.r.randint(0, W), c.r.randint(0, H)
        pts = [(x, y)]
        for _ in range(6):
            x += c.r.randint(-6, 6); y += c.r.randint(-6, 6)
            pts.append((x, y))
        c.d.line(pts, fill=R)
    for _ in range(40):
        c.p(c.r.randint(0, W - 1), c.r.randint(0, H - 1))
    c.ell((74, 40, 94, 56), K, K)
    c.fade(lambda x, y: (math.hypot((x - 84) / 1.3, y - 48) / 60) * 1.2)


def bg_void(c, lit=0.3):
    for _ in range(60):
        c.p(c.r.randint(0, W - 1), c.r.randint(0, H - 1))
    for _ in range(6):
        x, y = c.r.randint(0, W), c.r.randint(0, H)
        c.poly([(x, y), (x + c.r.randint(3, 8), y + c.r.randint(-2, 2)), (x + c.r.randint(1, 5), y + c.r.randint(3, 6))], K, WH)
    c.fade(lambda x, y: 0.4 + 0.6 * math.hypot(x - 84, y - 50) / 90)


BGS = dict(corridor=bg_corridor, room=bg_room, cave=bg_cave, stairs=bg_stairs, lake=bg_lake, chasm=bg_chasm,
           library=bg_library, crypt=bg_crypt, shrine=bg_shrine, fungus=bg_fungus, ruins=bg_ruins,
           prison=bg_prison, flesh=bg_flesh, void=bg_void)


# --- props -----------------------------------------------------------------------
P = {}


def prop(name):
    def deco(fn):
        P[name] = fn
        return fn
    return deco


@prop('door')
def _(c):
    door(c, 70, 34, 98, 70)
    c.rect((88, 52, 90, 54), R, R)
    for x in range(72, 98, 3):
        if c.r.random() < 0.5:
            c.p(x, 70, R); c.p(x, 69, R)


@prop('reddoor')
def _(c):
    door(c, 72, 32, 96, 70, fill=R, out=WH, bands=False)
    c.rect((89, 50, 90, 51), WH, WH)
    for x in (66, 102):
        c.drect((x - 3, 30, x + 3, 70), 0.3, R)


@prop('mawdoor')
def _(c):
    door(c, 66, 28, 102, 72, bands=True)
    c.ell((76, 46, 92, 58), R, WH)
    for x in range(78, 92, 3):
        c.poly([(x, 47), (x + 2, 47), (x + 1, 51)], WH, WH)
        c.poly([(x, 57), (x + 2, 57), (x + 1, 53)], WH, WH)
    c.drip(84, 59, 6)


@prop('twindoors')
def _(c):
    door(c, 60, 34, 80, 70, bands=False)
    door(c, 88, 34, 108, 70, bands=False)
    figure(c, 70, 84, 16, head='girl', body='dress', eyes=R)
    figure(c, 98, 84, 16, head='girl', body='dress', eyes=R)


@prop('rats')
def _(c):
    for _ in range(46):
        x, y = c.r.randint(10, 158), c.r.randint(66, 96)
        c.ell((x - 3, y - 2, x + 3, y + 1), K, WH)
        c.p(x - 4 if c.r.random() < 0.5 else x + 4, y - 1, R)
        c.line((x + 3, y), (x + 6, y + 1))


@prop('skeleton')
def _(c):
    x, y = 30, 90
    c.line((x, y - 22), (x, y - 8))
    for i in range(4):
        c.line((x - 4, y - 20 + i * 3), (x + 4, y - 20 + i * 3))
    skull(c, x, y - 25)
    c.line((x, y - 8), (x + 12, y - 8)); c.line((x + 12, y - 8), (x + 14, y))
    c.line((x, y - 8), (x + 10, y - 6)); c.line((x + 10, y - 6), (x + 18, y))
    c.line((x + 4, y - 19), (x + 10, y - 12)); c.line((x + 10, y - 12), (x + 14, y - 4))
    c.p(x + 15, y - 3, R); c.p(x + 15, y - 1, R)
    c.rect((x - 12, y - 14, x - 4, y - 2), K, WH)


@prop('chest')
def _(c):
    c.glow(84, 76, 26, 0.35)
    c.rect((66, 68, 102, 86), K, WH)
    c.ell((66, 58, 102, 76), K, WH)
    c.rect((67, 67, 101, 69), K, WH)
    c.line((66, 76), (102, 76))
    c.rect((82, 70, 86, 76), R, WH)
    for x in (70, 98):
        c.line((x, 62), (x, 86))


@prop('well')
def _(c):
    c.ell((60, 60, 108, 72), K, WH)
    c.rect((60, 66, 108, 86), K, WH)
    c.ell((60, 80, 108, 92), K, WH)
    c.ell((64, 62, 104, 70), K, K)
    for yy in (72, 78):
        c.line((60, yy), (108, yy))
    c.line((64, 62), (64, 36)); c.line((104, 62), (104, 36)); c.line((60, 36), (108, 36))
    chain(c, 84, 37, 60)
    c.p(80, 65, R); c.p(88, 65, R)


@prop('goblin')
def _(c):
    rock(c, 60, 88, 30, 10)
    x, yb = 62, 80
    c.ell((x - 9, yb - 14, x + 9, yb), K, WH)
    c.ell((x - 6, yb - 24, x + 6, yb - 12), K, WH)
    c.poly([(x - 6, yb - 20), (x - 13, yb - 24), (x - 5, yb - 17)], K, WH)
    c.poly([(x + 6, yb - 20), (x + 13, yb - 24), (x + 5, yb - 17)], K, WH)
    c.line((x - 3, yb - 18), (x - 1, yb - 18)); c.line((x + 1, yb - 18), (x + 3, yb - 18))
    c.line((x + 12, yb + 6), (x + 22, yb - 34))
    c.poly([(x + 22, yb - 34), (x + 20, yb - 29), (x + 25, yb - 31)], WH, WH)
    for i in range(5):
        c.ell((96 + i * 7, 84 + (i % 2) * 3, 100 + i * 7, 87 + (i % 2) * 3), K, WH)
    c.p(110, 85, R)


@prop('altar')
def _(c):
    c.rect((62, 60, 106, 84), K, WH)
    c.rect((58, 56, 110, 60), K, WH)
    c.drect((64, 62, 104, 82), 0.15)
    for x in (68, 80, 92, 100):
        c.drip(x, 60, c.r.randint(3, 12))
    c.ell((78, 54, 90, 57), R, R)
    candle(c, 62, 55); candle(c, 106, 55)


@prop('blackaltar')
def _(c):
    c.rect((62, 60, 106, 84), K, WH)
    c.rect((58, 56, 110, 60), K, WH)
    for i in range(14):
        x = 84 + c.r.randint(-8, 8)
        c.line((x, 55), (x + c.r.randint(-2, 2), 55 - c.r.randint(6, 20)), WH)
    c.ell((76, 40, 92, 56), K, K)
    c.eyes(84, 48, 4)
    for x in (34, 50, 118, 134):
        figure(c, x, 92, 18, head='hood', body='robe', arms='pray', eyes=None, fill=K, out=WH)
        c.drect((x - 5, 74, x + 5, 92), 0.3, K)


@prop('bloodfountain')
def _(c):
    c.ell((52, 70, 116, 88), K, WH)
    c.ell((56, 72, 112, 85), R, R)
    c.rect((80, 44, 88, 76), K, WH)
    c.ell((70, 38, 98, 48), K, WH)
    for dx in (-10, -5, 5, 10):
        for i in range(10):
            c.p(84 + dx * i / 9, 42 + i * 2 + abs(dx) * 0.2, R)
    c.drect((56, 72, 112, 85), 0.2, WH)


@prop('girl')
def _(c):
    c.glow(84, 64, 22, 0.25)
    figure(c, 84, 88, 30, head='girl', body='dress', arms='pray', eyes=None, fill=WH, out=WH)
    c.ell((80, 59, 88, 67), K, K)
    c.drect((70, 70, 98, 88), 0.4, K)


@prop('campfire')
def _(c):
    c.glow(84, 74, 40, 0.5)
    for i in range(8):
        a = i * math.pi / 4
        rock(c, 84 + math.cos(a) * 14, 86 + math.sin(a) * 4, 6, 4)
    c.line((74, 86), (94, 80)); c.line((74, 80), (94, 86))
    c.poly([(76, 82), (84, 58), (92, 82)], R, R)
    c.poly([(80, 82), (84, 68), (88, 82)], WH, WH)
    for _ in range(10):
        c.p(84 + c.r.randint(-10, 10), c.r.randint(40, 60), R)


@prop('merchant')
def _(c):
    c.glow(108, 56, 30, 0.45)
    figure(c, 84, 90, 46, head='hood', body='robe', arms='out', eyes=WH)
    c.line((108, 56), (108, 50))
    c.rect((105, 56, 111, 63), K, WH)
    c.rect((107, 58, 109, 61), R, R)
    c.rect((46, 76, 66, 90), K, WH)
    c.ell((48, 72, 54, 77), K, WH); c.ell((57, 71, 63, 77), R, WH)


@prop('pit')
def _(c):
    c.poly([(52, 62), (116, 62), (138, 96), (30, 96)], K, WH)
    c.poly([(54, 63), (114, 63), (128, 90), (40, 90)], K, K)
    for yy in range(64, 90, 5):
        c.line((54 - (yy - 63) * 0.5, yy), (54 - (yy - 63) * 0.5 + 3, yy))
    c.p(84, 80, R); c.p(87, 80, R)


@prop('spider')
def _(c):
    for a in range(0, 360, 30):
        x = 84 + math.cos(math.radians(a)) * 80
        y = 40 + math.sin(math.radians(a)) * 60
        c.line((84, 40), (x, y))
    for rr in range(10, 80, 12):
        pts = [(84 + math.cos(math.radians(a)) * rr, 40 + math.sin(math.radians(a)) * rr * 0.75) for a in range(0, 361, 30)]
        c.d.line(pts, fill=WH)
    for x, y in ((40, 60), (128, 70), (60, 30)):
        c.ell((x - 4, y - 7, x + 4, y + 7), WH, WH)
        c.line((x - 3, y - 2), (x + 3, y - 2), K)
    x, y = 100, 22
    c.ell((x - 8, y - 6, x + 8, y + 6), K, WH)
    c.ell((x - 4, y + 4, x + 4, y + 10), K, WH)
    for s in (-1, 1):
        for i in range(4):
            c.line((x + s * 4, y + i * 2 - 2), (x + s * (14 + i), y - 6 + i * 6))
            c.line((x + s * (14 + i), y - 6 + i * 6), (x + s * (18 + i), y + 2 + i * 6))
    for i in range(4):
        c.p(x - 3 + i * 2, y + 7, R)


@prop('mirror')
def _(c):
    for x in (34, 84, 134):
        c.rect((x - 14, 16, x + 14, 70), K, WH)
        c.rect((x - 12, 18, x + 12, 68), K, WH)
        c.drect((x - 11, 19, x + 11, 67), 0.12)
        figure(c, x, 66, 30, head='plain', body='legs', eyes=R if x == 84 else None)
    c.line((126, 22), (140, 50)); c.line((140, 50), (132, 64))


@prop('slime')
def _(c):
    c.ell((52, 64, 116, 92), K, WH)
    c.drect((54, 66, 114, 90), 0.2)
    c.rect((52, 82, 116, 92), K, K)
    c.line((52, 86), (116, 86))
    skull(c, 74, 76); c.line((90, 74), (98, 80)); c.line((94, 72), (90, 80))
    c.ell((80, 70, 86, 75), R, R)
    for x in (60, 72, 100, 108):
        c.line((x, 0), (x, c.r.randint(10, 40)))
        c.p(x, c.r.randint(44, 60))


@prop('priest')
def _(c):
    c.glow(84, 50, 30, 0.3)
    figure(c, 84, 88, 44, head='hood', body='robe', arms='pray', eyes=None)
    c.ell((80, 52, 88, 58), K, K)
    c.p(82, 54); c.p(86, 54)
    c.line((84, 22), (84, 34), R); c.line((80, 26), (88, 26), R)


@prop('abysspriest')
def _(c):
    figure(c, 84, 90, 48, head='hood', body='robe', arms='up', eyes=R)
    for i in range(7):
        x0 = 72 + i * 4
        pts = [(x0, 44)]
        for k in range(5):
            pts.append((x0 + math.sin(k + i) * 3, 44 - k * 4))
        c.d.line(pts, fill=WH)
        c.p(pts[-1][0], pts[-1][1], R)
    rect_y = 90
    c.rect((40, rect_y - 6, 128, rect_y), K, WH)


@prop('rubble')
def _(c):
    for _ in range(14):
        rock(c, c.r.randint(20, 150), c.r.randint(62, 100), c.r.randint(8, 22), c.r.randint(5, 14))
    c.poly([(60, 50), (100, 54), (96, 58), (64, 56)], K, WH)
    c.p(84, 30, R); c.p(87, 30, R)


@prop('inverted')
def _(c):
    figure(c, 84, 90, 22, head='plain', body='legs', eyes=None)
    c.eyes(84, 22, 4)


@prop('face')
def _(c):
    x, y = 40, 48
    c.ell((x - 14, y - 18, x + 14, y + 18), K, WH)
    c.ell((x - 9, y - 8, x - 3, y - 3), WH, WH); c.ell((x + 3, y - 8, x + 9, y - 3), WH, WH)
    c.p(x - 6, y - 5, R); c.p(x + 6, y - 5, R)
    c.line((x, y - 4), (x - 2, y + 4)); c.line((x - 2, y + 4), (x + 1, y + 4))
    c.ell((x - 5, y + 7, x + 5, y + 13), K, WH)
    for dx in (-10, 10):
        c.drip(x + dx, y + 10, 6, WH)


@prop('mushroom')
def _(c):
    for x, h, w in ((50, 18, 16), (70, 12, 10), (96, 22, 20), (118, 10, 9), (84, 8, 7), (134, 16, 13)):
        c.glow(x, 86 - h, w + 6, 0.35)
        mushroom(c, x, 88, h, w)


@prop('cage')
def _(c):
    chain(c, 84, 0, 18)
    c.ell((66, 16, 102, 30), K, WH)
    c.rect((66, 23, 102, 70), K, WH)
    figure(c, 84, 68, 26, head='plain', body='legs', arms='up', eyes=WH)
    for x in range(66, 103, 6):
        c.line((x, 23), (x, 70))
    c.line((66, 46), (102, 46))
    c.drip(78, 71, 8)


@prop('dog')
def _(c):
    x, y = 84, 78
    c.ell((x - 16, y - 8, x + 12, y + 2), K, WH)
    c.poly([(x + 8, y - 6), (x + 20, y - 14), (x + 26, y - 10), (x + 20, y - 2)], K, WH)
    c.poly([(x + 16, y - 12), (x + 17, y - 19), (x + 20, y - 13)], K, WH)
    for lx in (x - 12, x - 7, x + 4, x + 9):
        c.line((lx, y), (lx, y + 10))
    c.line((x - 16, y - 4), (x - 24, y - 12))
    c.p(x + 21, y - 10, R)


@prop('book')
def _(c):
    c.rect((50, 66, 118, 70), K, WH)
    c.line((56, 70), (56, 90)); c.line((112, 70), (112, 90))
    c.poly([(66, 64), (84, 60), (84, 66), (66, 66)], WH, WH)
    c.poly([(84, 60), (102, 64), (102, 66), (84, 66)], WH, WH)
    for yy in (62, 64):
        c.line((70, yy + 1), (80, yy - 1), K); c.line((88, yy - 1), (98, yy + 1), K)
    c.drip(100, 66, 4)
    candle(c, 112, 65)


@prop('stream')
def _(c):
    c.poly([(70, 0), (96, 0), (92, 56), (76, 56)], K, WH)
    for yy in range(4, 56, 4):
        c.line((78, yy), (90, yy + 2))
    c.ell((60, 70, 108, 86), K, WH)
    c.ell((82, 76, 86, 79), WH, WH)


@prop('knight')
def _(c):
    figure(c, 84, 90, 50, head='helm', body='armor', arms='down', eyes=R)
    c.line((104, 90), (100, 56)); c.line((97, 62), (103, 62))
    c.drect((60, 40, 108, 90), 0.15, K)


@prop('knightghost')
def _(c):
    c.glow(84, 56, 34, 0.25)
    figure(c, 84, 90, 50, head='helm', body='armor', arms='down', eyes=R, fill=K, out=WH)
    c.line((104, 90), (100, 56), WH); c.line((97, 62), (103, 62))
    c.fade(lambda x, y: 0.7 if 50 < x < 120 else 1)


@prop('bats')
def _(c):
    for _ in range(40):
        x, y = c.r.randint(4, 164), c.r.randint(8, 70)
        c.line((x - 3, y - 1), (x, y + 1)); c.line((x + 3, y - 1), (x, y + 1))
        if c.r.random() < 0.4:
            c.p(x, y, R)


@prop('dice')
def _(c):
    c.rect((40, 66, 128, 72), K, WH)
    c.line((46, 72), (46, 92)); c.line((122, 72), (122, 92))
    figure(c, 98, 66, 34, head='skull', body='bones', arms='out', eyes=R)
    c.rect((70, 60, 75, 65), WH, WH); c.p(72, 62, K)
    c.rect((78, 61, 83, 66), WH, WH); c.p(79, 62, R); c.p(82, 65, R)
    for i in range(4):
        c.ell((52 + i * 3, 64 - i, 56 + i * 3, 66 - i), WH, WH)


@prop('cradle')
def _(c):
    c.arc((60, 70, 108, 96), 0, 180)
    c.poly([(64, 70), (104, 70), (100, 84), (68, 84)], K, WH)
    for x in range(66, 104, 4):
        c.line((x, 60), (x, 72))
    c.line((64, 60), (104, 60))
    for i in range(4):
        c.p(120 + i * 6, 40 - i * 4, WH); c.p(121 + i * 6, 39 - i * 4, WH)
    c.drect((66, 62, 102, 70), 0.25, R)


@prop('statue')
def _(c):
    c.rect((66, 76, 102, 92), K, WH)
    figure(c, 84, 76, 54, head='girl', body='dress', arms='pray', eyes=None, fill=K, out=WH)
    c.drip(82, 30, 16); c.drip(86, 30, 14)
    c.line((70, 82), (98, 82))


@prop('thief')
def _(c):
    rock(c, 40, 92, 40, 30)
    figure(c, 96, 90, 42, head='hood', body='legs', arms='out', eyes=WH)
    c.line((112, 62), (118, 56)); c.p(118, 56, R)


@prop('crystal')
def _(c):
    c.glow(84, 50, 30, 0.5)
    c.rect((76, 64, 92, 72), K, WH)
    c.poly([(72, 74), (96, 74), (92, 64), (76, 64)], K, WH)
    c.ell((70, 38, 98, 64), K, WH)
    c.drect((72, 40, 96, 62), 0.25)
    figure(c, 84, 60, 14, head='plain', body='legs', eyes=None, fill=R, out=R)


@prop('bell')
def _(c):
    c.line((40, 10), (128, 10)); c.line((84, 10), (84, 18))
    c.poly([(70, 20), (98, 20), (106, 58), (62, 58)], K, WH)
    c.ell((66, 14, 102, 28), K, WH)
    c.rect((60, 56, 108, 60), K, WH)
    for yy in range(26, 54, 5):
        for xx in range(70, 100, 5):
            if c.r.random() < 0.5:
                c.p(xx, yy)
    c.p(84, 40, R); c.p(85, 40, R)
    c.ell((81, 60, 87, 66), K, WH)


@prop('swordstone')
def _(c):
    c.glow(84, 50, 30, 0.35)
    rock(c, 84, 90, 44, 22)
    c.line((84, 70), (84, 36)); c.line((85, 70), (85, 36))
    c.line((78, 38), (91, 38)); c.rect((83, 30, 86, 36), K, WH); c.p(84, 29, R)
    for x in (40, 128):
        skull(c, x, 88)
        c.line((x + 3, 90), (x + 14, 86))


@prop('bonegate')
def _(c):
    c.rect((40, 10, 128, 92), K, WH)
    c.rect((66, 44, 102, 92), K, WH)
    for yy in range(14, 90, 7):
        for xx in range(44, 126, 7):
            if 66 <= xx <= 102 and yy >= 44:
                continue
            skull(c, xx, yy, R if c.r.random() < 0.1 else K)
    skull(c, 84, 28, R)
    for x in range(70, 100, 6):
        c.line((x, 44), (x, 92))


@prop('bones')
def _(c):
    for _ in range(30):
        x, y = c.r.randint(20, 148), c.r.randint(70, 96)
        if c.r.random() < 0.5:
            skull(c, x, y)
        else:
            c.line((x - 4, y), (x + 4, y + c.r.randint(-2, 2)))
    c.drect((20, 90, 148, 99), 0.3, R)


@prop('ghost')
def _(c):
    c.glow(84, 54, 30, 0.3)
    pts = [(70, 40), (76, 26), (84, 22), (92, 26), (98, 40), (100, 70), (94, 64), (90, 74), (84, 66), (78, 76), (74, 64), (68, 72)]
    c.poly(pts, WH, WH)
    c.drect((68, 50, 100, 76), 0.6, K)
    c.ell((78, 32, 90, 44), K, K)
    c.line((70, 46), (60, 56)); c.line((98, 46), (108, 54))


@prop('coffin')
def _(c):
    pts = [(76, 30), (92, 30), (100, 46), (94, 90), (74, 90), (68, 46)]
    c.poly(pts, K, WH)
    for (x, y) in ((76, 34), (92, 34), (72, 50), (96, 50), (76, 86), (92, 86), (84, 60), (80, 70), (88, 70)):
        c.p(x, y)
    c.line((78, 52), (90, 52), R); c.line((84, 44), (84, 64), R)
    for i in range(4):
        c.line((66 - i * 3, 70 + i * 3), (64 - i * 3, 74 + i * 3))


@prop('flooded')
def _(c):
    c.clear((0, 56, W, H))
    for yy in range(58, H, 3):
        for x in range(0, W):
            if c.r.random() < 0.2 and (x // 4) % 2:
                c.p(x, yy)
    c.line((40, 70), (60, 72)); c.line((60, 72), (80, 70))
    c.p(110, 66, R); c.p(113, 66, R)


@prop('boatman')
def _(c):
    c.poly([(52, 68), (116, 68), (106, 78), (60, 78)], K, WH)
    figure(c, 90, 68, 34, head='hood', body='robe', arms='down', eyes=R)
    c.line((104, 30), (70, 84))
    c.glow(62, 52, 16, 0.4)
    c.line((62, 54), (62, 66)); c.rect((60, 50, 64, 54), R, R)


@prop('ghoul')
def _(c):
    x, y = 84, 80
    c.ell((x - 18, y - 12, x + 10, y + 2), K, WH)
    c.ell((x + 4, y - 16, x + 18, y - 4), K, WH)
    c.p(x + 10, y - 11, R); c.p(x + 14, y - 11, R)
    c.line((x + 9, y - 7), (x + 15, y - 7), R)
    for lx, ly in ((x - 14, y), (x - 6, y + 1), (x + 4, y), (x + 10, y)):
        c.line((lx, ly), (lx - 2, y + 10))
    c.ell((x - 50, y + 4, x - 24, y + 12), K, WH)
    c.drect((x - 50, y + 8, x - 24, y + 12), 0.5, R)


@prop('witch')
def _(c):
    c.glow(84, 70, 34, 0.4)
    c.ell((76, 72, 116, 92), K, WH)
    c.line((76, 78), (116, 78))
    c.drect((78, 74, 114, 77), 0.6, R)
    for i in range(6):
        c.p(90 + c.r.randint(-8, 8), 66 - i * 3)
    c.poly([(84, 92), (92, 86), (100, 92)], R, R)
    figure(c, 62, 92, 44, head='witch', body='robe', arms='out', eyes=WH)
    c.line((80, 64), (96, 74))


@prop('doll')
def _(c):
    c.rect((70, 60, 98, 64), K, WH)
    c.line((72, 64), (72, 90)); c.line((96, 64), (96, 90)); c.line((96, 60), (96, 30))
    c.line((96, 30), (72, 30)); c.line((72, 30), (72, 60))
    figure(c, 84, 60, 20, head='mask', body='dress', arms='down', eyes=None, fill=K)
    c.line((86, 42), (88, 50), K)


@prop('painting')
def _(c):
    for x, w in ((32, 22), (84, 30), (136, 22)):
        c.rect((x - w // 2 - 2, 14, x + w // 2 + 2, 62), K, WH)
        c.rect((x - w // 2, 16, x + w // 2, 60), K, WH)
        figure(c, x, 60, 36, head='plain' if x != 84 else 'mask', body='robe', eyes=R if x == 84 else None)
    c.line((84, 16), (84, 4))


@prop('bridge')
def _(c):
    c.line((52, 40), (118, 38)); c.line((52, 54), (118, 52))
    for i in range(16):
        x = 54 + i * 4
        y = 54 - i * 0.13 + math.sin(i / 15 * math.pi) * 6
        c.line((x, y), (x + 2, y))
        c.line((x, y), (x, 40 - i * 0.13 + math.sin(i / 15 * math.pi) * 2))
    for _ in range(8):
        hx = c.r.randint(60, 110)
        c.line((hx, 99), (hx + c.r.randint(-3, 3), 70 + c.r.randint(0, 10)))
        c.p(hx, 70, R)


@prop('potion')
def _(c):
    for yy in (30, 50, 70):
        c.line((20, yy), (148, yy))
        for x in range(26, 146, 10):
            if c.r.random() < 0.7:
                col = [WH, R, K][c.r.randint(0, 2)]
                c.rect((x - 2, yy - 6, x + 2, yy - 1), col, WH)
                c.rect((x - 1, yy - 8, x + 1, yy - 6), K, WH)
    c.rect((60, 80, 108, 84), K, WH)
    for x, col in ((72, R), (84, WH), (96, K)):
        c.ell((x - 4, 72, x + 4, 80), col, WH)
        c.rect((x - 1, 68, x + 1, 72), K, WH)


@prop('feast')
def _(c):
    c.rect((20, 64, 148, 70), K, WH)
    for x in range(30, 146, 18):
        figure(c, x, 64, 22, head='skull', body='bones', arms='out', eyes=R if c.r.random() < 0.4 else K)
        c.ell((x + 5, 60, x + 12, 64), K, WH)
    c.ell((76, 56, 92, 64), R, WH)
    c.line((84, 70), (84, 92))


@prop('grave')
def _(c):
    c.glow(84, 60, 30, 0.3)
    c.ell((70, 38, 98, 56), K, WH)
    c.rect((70, 47, 98, 84), K, WH)
    c.line((71, 47), (97, 47), K)
    c.line((84, 52), (84, 62)); c.line((80, 56), (88, 56))
    for yy in (66, 70, 74):
        c.line((76, yy), (92, yy))
    c.ell((64, 82, 104, 90), K, WH)
    c.p(78, 86, R); c.p(80, 85, R); c.p(82, 86, R)
    figure(c, 112, 88, 22, head='girl', body='dress', arms='down', eyes=None, fill=WH, out=WH)
    c.drect((104, 70, 120, 88), 0.4, K)


@prop('prisoner')
def _(c):
    figure(c, 84, 90, 40, head='plain', body='legs', arms='up', eyes=None)
    c.line((81, 56), (87, 56), R)
    chain(c, 70, 40, 52); chain(c, 98, 40, 52)


@prop('jailer')
def _(c):
    figure(c, 84, 92, 52, head='none', body='armor', arms='down', eyes=None)
    for i in range(5):
        c.ell((96 + i * 2, 66 + (i % 2) * 2, 99 + i * 2, 70 + (i % 2) * 2), K, WH)
    c.drect((76, 40, 92, 50), 0.5, R)


@prop('candles')
def _(c):
    for i in range(10):
        t = i / 10
        for side in (-1, 1):
            x = 84 + side * (80 * (1 - t) ** 1.2 + 14)
            yb = 100 - 40 * (1 - (1 - t) ** 1.3)
            candle(c, x, yb, h=int(6 * (1 - t)) + 2)


@prop('eye')
def _(c):
    c.ell((40, 24, 128, 76), K, WH)
    c.ell((44, 28, 124, 72), WH, WH)
    c.ell((66, 30, 102, 70), R, R)
    c.ell((78, 38, 90, 62), K, K)
    c.drect((44, 28, 124, 72), 0.25, K)
    for x in range(48, 124, 6):
        c.line((x, 26), (x - 2, 20))


@prop('map')
def _(c):
    c.rect((40, 64, 128, 70), K, WH)
    c.poly([(62, 56), (108, 54), (110, 64), (60, 64)], WH, WH)
    for _ in range(14):
        x, y = c.r.randint(64, 104), c.r.randint(56, 62)
        c.p(x, y, K)
    c.p(96, 58, R); c.p(97, 59, R)
    figure(c, 50, 64, 26, head='skull', body='bones', arms='out', eyes=None)


@prop('siren')
def _(c):
    rock(c, 84, 66, 30, 12)
    figure(c, 84, 56, 26, head='girl', body='dress', arms='up', eyes=R, fill=K, out=WH)
    for i in range(5):
        c.p(60 - i * 4, 40 + (i % 2) * 2, WH); c.p(108 + i * 4, 40 + (i % 2) * 2, WH)
    for x in range(56, 112, 7):
        c.line((x, 74), (x + 3, 80))


@prop('reaper')
def _(c):
    figure(c, 108, 90, 50, head='hood', body='robe', arms='out', eyes=R)
    c.line((126, 92), (126, 30)); c.arc((100, 22, 136, 50), 180, 300)
    c.rect((40, 70, 84, 74), K, WH)
    for i in range(4):
        for j in range(3):
            if (i + j) % 2:
                c.rect((46 + i * 8, 64 + j * 2, 50 + i * 8, 65 + j * 2), WH, WH)
    c.line((44, 74), (44, 92)); c.line((80, 74), (80, 92))


@prop('worms')
def _(c):
    c.ell((40, 58, 128, 92), K, WH)
    c.drect((42, 60, 126, 90), 0.2)
    for _ in range(140):
        x, y = c.r.randint(10, 158), c.r.randint(62, 99)
        c.line((x, y), (x + 1, y))
    c.drip(84, 92, 4)


@prop('corridor')
def _(c):
    pass


@prop('forest')
def _(c):
    for x, h, w in ((84, 60, 30), (60, 34, 14)):
        mushroom(c, x, 88, h, w)
    for _ in range(80):
        c.p(c.r.randint(0, W - 1), c.r.randint(0, 99))
    for x in (30, 140):
        figure(c, x, 90, 18, head='plain', body='robe', eyes=R)


@prop('street')
def _(c):
    for x in (50, 118):
        c.line((x, 84), (x, 52)); c.rect((x - 2, 48, x + 2, 52), R, WH)
        c.glow(x, 50, 12, 0.4)
    figure(c, 84, 92, 18, head='plain', body='robe', eyes=None)


@prop('golem')
def _(c):
    c.rect((60, 24, 108, 70), K, WH)
    c.rect((72, 10, 96, 26), K, WH)
    c.line((76, 18), (92, 18), R)
    c.rect((40, 26, 58, 72), K, WH); c.rect((110, 26, 128, 72), K, WH)
    c.rect((64, 70, 80, 98), K, WH); c.rect((88, 70, 104, 98), K, WH)
    c.ell((78, 38, 90, 50), R, WH)
    c.glow(84, 44, 16, 0.4, R)
    for yy in range(30, 70, 8):
        c.line((60, yy), (66, yy)); c.line((102, yy), (108, yy))


@prop('throne')
def _(c):
    c.rect((62, 20, 106, 78), K, WH)
    c.rect((56, 54, 112, 84), K, WH)
    for x in (62, 106):
        c.poly([(x - 4, 20), (x, 10), (x + 4, 20)], K, WH)
    figure(c, 84, 74, 40, head='skull', body='robe', arms='down', eyes=R)
    c.poly([(78, 34), (80, 30), (82, 33), (84, 29), (86, 33), (88, 30), (90, 34)], R, R)


@prop('moth')
def _(c):
    c.glow(84, 46, 40, 0.3)
    for s in (-1, 1):
        c.poly([(84, 40), (84 + s * 60, 12), (84 + s * 70, 40), (84 + s * 40, 54)], K, WH)
        c.poly([(84, 48), (84 + s * 44, 58), (84 + s * 30, 80)], K, WH)
        for (fx, fy) in ((40, 30), (55, 34), (26, 46)):
            x = 84 + s * fx
            c.ell((x - 3, fy - 3, x + 3, fy + 3), WH, WH)
            c.p(x - 1, fy - 1, K); c.p(x + 1, fy - 1, K); c.p(x, fy + 1, K)
    c.ell((80, 34, 88, 70), K, WH)
    c.p(82, 38, R); c.p(86, 38, R)
    c.line((82, 34), (76, 22)); c.line((86, 34), (92, 22))


@prop('fungalman')
def _(c):
    figure(c, 84, 92, 50, head='plain', body='legs', arms='out', eyes=None)
    for (x, y, w) in ((80, 42, 8), (90, 46, 10), (76, 58, 7), (92, 62, 6), (84, 36, 12)):
        mushroom(c, x, y, 3, w, spots=False)
    for i in range(6):
        c.line((84, 60), (120 + i * 6, 50 + i * 6))


@prop('clock')
def _(c):
    c.rect((60, 6, 108, 92), K, WH)
    c.poly([(56, 8), (84, -10), (112, 8)], K, WH)
    c.ell((64, 14, 104, 54), K, WH)
    for i in range(12):
        a = i / 12 * 2 * math.pi
        c.p(84 + math.cos(a) * 17, 34 + math.sin(a) * 17)
    c.line((84, 34), (76, 24), R); c.line((84, 34), (94, 36))
    door(c, 76, 64, 92, 92, bands=False)


@prop('dragonbones')
def _(c):
    for i in range(9):
        x = 30 + i * 13
        c.arc((x - 10, 16, x + 10, 96), 180, 360)
    c.line((20, 56), (150, 56))
    skull(c, 20, 60, R)
    c.ell((4, 48, 36, 70), K, WH)
    c.p(14, 56, R); c.p(18, 56, R)
    for _ in range(40):
        c.p(c.r.randint(60, 120), c.r.randint(76, 92))
    c.ell((60, 80, 120, 96), K, WH)
    c.drect((62, 82, 118, 94), 0.4)


@prop('shadow')
def _(c):
    figure(c, 70, 92, 40, head='plain', body='legs', arms='down', eyes=None, fill=K, out=WH)
    figure(c, 100, 92, 40, head='plain', body='legs', arms='out', eyes=R, fill=K, out=K)
    c.drect((84, 50, 120, 92), 0.5)
    c.poly([(70, 92), (100, 92), (100, 94), (70, 94)], K, WH)


@prop('maskmerchant')
def _(c):
    figure(c, 84, 90, 46, head='mask', body='robe', arms='out', eyes=None)
    for x in range(40, 130, 12):
        c.ell((x - 4, 74, x + 4, 84), WH, WH)
        c.p(x - 2, 78, K); c.p(x + 2, 78, K)
        if c.r.random() < 0.4:
            c.line((x - 1, 81), (x + 1, 81), R)
    c.rect((34, 84, 134, 88), K, WH)


@prop('egg')
def _(c):
    c.glow(84, 54, 34, 0.25)
    c.ell((62, 22, 106, 86), K, WH)
    for i in range(4):
        c.arc((64 + i * 4, 24 + i * 4, 104 - i * 4, 84 - i * 4), 200, 340)
    c.line((84, 30), (80, 40), R); c.line((80, 40), (86, 48), R)
    for _ in range(14):
        x = c.r.randint(40, 128)
        c.line((x, 99), (84 + (x - 84) // 3, 80))


@prop('army')
def _(c):
    for row, (yb, h) in enumerate(((80, 22), (92, 30))):
        for x in range(14 + row * 8, 160, 20 + row * 6):
            figure(c, x, yb, h, head='helm', body='armor', arms='down', eyes=R if c.r.random() < 0.3 else None)
            c.line((x + h * 0.3, yb), (x + h * 0.3, yb - h * 1.2))
    c.line((30, 92), (30, 40)); c.rect((30, 40, 46, 52), R, WH)


@prop('librarian')
def _(c):
    figure(c, 84, 90, 46, head='plain', body='robe', arms='pray', eyes=None)
    for i in range(5):
        c.line((80 + i * 2, 59), (80 + i * 2, 61), R)
    c.line((79, 60), (89, 60), R)


@prop('hanged')
def _(c):
    for x in (40, 66, 102, 128):
        yy = c.r.randint(24, 40)
        c.line((x, 0), (x, yy))
        figure(c, x, yy + 30, 28, head='plain', body='legs', arms='down', eyes=R if x == 102 else None)


@prop('river')
def _(c):
    for yy in range(58, H, 2):
        for x in range(0, W):
            if c.r.random() < 0.35:
                c.p(x, yy)
    for x in range(10, 160, 30):
        c.ell((x, 70 + (x % 3) * 6, x + 10, 76 + (x % 3) * 6), K, WH)
        figure(c, x + 5, 76 + (x % 3) * 6, 8, head='plain', body='robe', eyes=None, fill=K, out=WH)


@prop('maiden')
def _(c):
    c.poly([(70, 20), (98, 20), (104, 40), (100, 92), (68, 92), (64, 40)], K, WH)
    c.ell((74, 10, 94, 30), K, WH)
    c.p(80, 18); c.p(88, 18); c.line((81, 24), (87, 24))
    c.line((84, 32), (84, 92))
    for y in range(40, 90, 10):
        c.drip(84, y, 3)
    c.drect((60, 90, 108, 99), 0.4, R)


@prop('giant')
def _(c):
    c.clear((0, 0, W, H))
    for x in range(0, W, 14):
        c.poly([(x, 0), (x + 12, 0), (x + 10, 16), (x + 2, 16)], WH, K)
        c.poly([(x, 99), (x + 12, 99), (x + 10, 86), (x + 2, 86)], WH, K)
    c.ell((20, 60, 148, 120), K, R)
    c.ell((76, 30, 92, 56), K, WH)
    for x in (50, 110):
        c.rect((x, 74, x + 8, 80), K, WH)


@prop('heart')
def _(c):
    c.ell((52, 24, 90, 64), R, WH)
    c.ell((78, 24, 116, 64), R, WH)
    c.poly([(54, 50), (114, 50), (84, 92)], R, WH)
    c.drect((56, 28, 112, 88), 0.2, K)
    c.line((70, 20), (70, 8)); c.line((96, 20), (100, 4))
    c.ell((80, 44, 88, 52), WH, WH)


@prop('eyes')
def _(c):
    for _ in range(26):
        x, y = c.r.randint(8, 160), c.r.randint(6, 94)
        w = c.r.randint(3, 8)
        c.ell((x - w, y - w // 2, x + w, y + w // 2), WH, WH)
        c.ell((x - w // 3, y - w // 3, x + w // 3, y + w // 3), R, R)
        c.p(x, y, K)


@prop('corpse')
def _(c):
    figure(c, 84, 84, 10, head='plain', body='robe', eyes=None)
    c.clear((60, 60, 110, 90))
    c.poly([(54, 80), (110, 78), (112, 84), (56, 86)], K, WH)
    c.ell((106, 76, 116, 86), K, WH)
    c.p(109, 80, WH); c.p(113, 80, WH)
    c.drect((50, 84, 120, 92), 0.5, R)
    c.p(58, 82, R)


@prop('maw')
def _(c):
    c.ell((14, 14, 154, 96), R, WH)
    c.ell((34, 30, 134, 82), K, K)
    for i in range(11):
        x = 34 + i * 9
        c.poly([(x, 30), (x + 6, 30), (x + 3, 44)], WH, K)
        c.poly([(x, 82), (x + 6, 82), (x + 3, 70)], WH, K)
    c.ell((64, 60, 104, 80), R, K)


@prop('womb')
def _(c):
    figure(c, 84, 90, 14, head='girl', body='dress', eyes=None, fill=WH, out=WH)


@prop('hands')
def _(c):
    for _ in range(40):
        x, y = c.r.randint(4, 164), c.r.randint(46, 98)
        c.line((x, y + 8), (x, y), WH)
        for k in range(-2, 3):
            c.p(x + k, y - abs(k) % 2 - 1)
    c.line((0, 50), (W, 50))
    c.p(84, 30, R); c.p(87, 30, R)


@prop('angel')
def _(c):
    c.glow(84, 46, 40, 0.3)
    for s in (-1,):
        for i in range(5):
            c.line((84, 36), (84 + s * (20 + i * 8), 10 + i * 6))
    c.line((84, 36), (104, 30)); c.line((104, 30), (110, 44))
    figure(c, 84, 82, 46, head='plain', body='robe', arms='down', eyes=None, fill=K, out=WH)
    c.p(82, 46, WH); c.p(86, 46, R)
    c.drect((84, 40, 92, 82), 0.5, R)
    chain(c, 70, 0, 36); chain(c, 98, 0, 36)


@prop('voice')
def _(c):
    for i in range(5):
        r = 10 + i * 12
        c.arc((84 - r, 50 - r, 84 + r, 50 + r), 200, 340)
        c.arc((84 - r, 50 - r, 84 + r, 50 + r), 20, 160)
    c.ell((80, 46, 88, 54), K, WH)
    c.line((82, 50), (86, 50), R)


@prop('well2')
def _(c):
    pass


@prop('moon')
def _(c):
    c.glow(84, 38, 50, 0.3, R)
    c.ell((54, 8, 114, 68), R, WH)
    c.d.line([(70, 14), (76, 30), (72, 44), (82, 56)], fill=K)
    c.d.line([(100, 20), (92, 34), (98, 50)], fill=K)
    c.drect((56, 10, 112, 66), 0.2, K)
    figure(c, 84, 98, 16, head='plain', body='legs', eyes=None)


@prop('mirror2')
def _(c):
    pass


@prop('dragon')
def _(c):
    c.glow(84, 40, 40, 0.25, R)
    for s_ in (-1, 1):
        pts = [(84 + s_ * 10, 40), (84 + s_ * 40, 8), (84 + s_ * 78, 14), (84 + s_ * 66, 30), (84 + s_ * 74, 46), (84 + s_ * 50, 44), (84 + s_ * 40, 58)]
        c.poly(pts, K, WH)
        for k in range(3):
            c.line((84 + s_ * 40, 8), (84 + s_ * (52 + k * 8), 44 - k * 6))
    c.ell((72, 34, 96, 66), K, WH)
    for i in range(4):
        c.line((76, 42 + i * 5), (92, 42 + i * 5))
    c.poly([(78, 36), (84, 14), (90, 36)], K, WH)
    c.poly([(80, 18), (84, 6), (88, 18), (86, 26), (82, 26)], K, WH)
    c.p(82, 16, R); c.p(86, 16, R)
    c.line((76, 66), (70, 90)); c.line((92, 66), (98, 90))
    c.d.line([(84, 66), (90, 80), (80, 92), (60, 96)], fill=WH)


@prop('memory')
def _(c):
    c.rect((24, 20, 64, 52), K, WH)
    c.line((44, 20), (44, 52)); c.line((24, 36), (64, 36))
    c.rect((96, 66, 150, 80), K, WH)
    c.rect((96, 60, 106, 66), WH, WH)
    c.line((98, 80), (98, 92)); c.line((148, 80), (148, 92))
    c.rect((40, 70, 70, 74), K, WH)
    c.rect((50, 66, 58, 70), WH, WH)
    c.p(54, 68, R)


@prop('thing')
def _(c):
    for i in range(10):
        r = 6 + i * 9
        c.arc((84 - r * 1.4, 50 - r, 84 + r * 1.4, 50 + r), 0, 360, WH if i % 3 else R)
    c.fade(lambda x, y: 0.75)
    c.ell((60, 36, 108, 64), WH, WH)
    c.ell((74, 38, 94, 62), R, R)
    c.ell((81, 42, 87, 58), K, K)
    figure(c, 84, 98, 14, head='plain', body='legs', eyes=None)


# props with alternative names in data
P['knightghost'] = P['knightghost']


def void_well(c):
    c.ell((60, 54, 108, 66), K, WH)
    c.rect((60, 60, 108, 84), K, WH)
    c.ell((60, 78, 108, 90), K, WH)
    c.ell((64, 56, 104, 64), K, K)
    for _ in range(10):
        c.p(c.r.randint(66, 102), c.r.randint(57, 63))
    c.p(84, 40); c.p(84, 30); c.p(85, 20)


def void_mirror(c):
    for i, x in enumerate(range(16, 168, 26)):
        c.rect((x - 10, 20, x + 10, 76), K, WH)
        figure(c, x, 74, 26, head='plain', body='legs', eyes=R if i % 2 else None)
        c.drect((x - 9, 21, x + 9, 75), 0.15)


def void_merchant(c):
    P['merchant'](c)


def room_merchant(c):
    P['merchant'](c)


BG_DIM = dict(corridor=0.5, room=0.45, cave=0.6, stairs=0.6, lake=0.6, chasm=0.65, library=0.5, crypt=0.5,
              shrine=0.5, fungus=0.6, ruins=0.55, prison=0.5, flesh=0.6, void=0.8)

SPECIAL = {('void', 'well'): void_well, ('void', 'mirror'): void_mirror}


def frame(c):
    c.rect((0, 0, W - 1, H - 1), None, WH) if False else None


def render(art, seed):
    bg, pr = art.split(':')
    c = C(seed)
    if bg == 'stairs':
        bg_stairs(c, flip=(pr == 'inverted'))
    elif not (bg == 'lake' and pr == 'flooded'):
        BGS[bg](c)
    if pr == 'flooded':
        bg_corridor(c)
    c.fade(lambda x, y: BG_DIM.get(bg, 0.5))
    fn = SPECIAL.get((bg, pr)) or P.get(pr)
    if fn:
        fn(c)
    else:
        print('missing prop', pr, file=sys.stderr)
    c.vignette(0.9)
    return c.im


EXTRA = {
    'title': 'stairs:title',
    'gameover': 'crypt:gameover',
    'clear': 'void:clear',
}


@prop('title')
def _(c):
    c.ell((76, 14, 92, 30), K, K)
    c.ell((78, 20, 90, 25), R, R)
    c.p(84, 22, K)
    c.glow(84, 22, 18, 0.3, R)


@prop('gameover')
def _(c):
    c.clear((40, 20, 128, 96))
    c.ell((60, 22, 108, 70), WH, WH)
    c.rect((70, 64, 98, 82), WH, WH)
    c.ell((68, 38, 80, 52), K, K); c.ell((88, 38, 100, 52), K, K)
    c.p(74, 45, R); c.p(94, 45, R)
    c.poly([(84, 54), (81, 61), (87, 61)], K, K)
    for x in range(72, 98, 4):
        c.line((x, 70), (x, 82), K)
    c.drip(76, 82, 8); c.drip(92, 82, 12)


@prop('clear')
def _(c):
    c.clear((0, 0, W, H))
    c.drect((0, 0, W - 1, H - 1), 0, WH, lambda x, y: 0.9 * max(0, 1 - math.hypot(x - 84, (y - 20) * 1.3) / 90))
    figure(c, 84, 96, 30, head='plain', body='legs', arms='up', eyes=None)


def main():
    out = os.path.join(ROOT, 'art', 'events')
    os.makedirs(out, exist_ok=True)
    ev = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data/events/*.json'))):
        ev += json.load(open(f))
    items = [(e['id'], e['a']) for e in ev] + list(EXTRA.items())
    imgs = []
    for i, (eid, art) in enumerate(items):
        seed = sum(ord(ch) * (k + 1) for k, ch in enumerate(eid))
        im = render(art, seed)
        im.save(os.path.join(out, eid + '.png'))
        imgs.append((eid, im))
    print('wrote', len(imgs))
    if '--sheet' in sys.argv:
        cols = 8
        rows = (len(imgs) + cols - 1) // cols
        sheet = Image.new('RGB', (cols * (PW + 4), rows * (PH + 14)), (60, 60, 60))
        d = ImageDraw.Draw(sheet)
        for i, (eid, im) in enumerate(imgs):
            x, y = (i % cols) * (PW + 4), (i // cols) * (PH + 14)
            sheet.paste(im, (x, y))
            d.text((x + 2, y + PH), eid, fill=(255, 255, 255))
        dest = sys.argv[sys.argv.index('--sheet') + 1]
        sheet.save(dest)
        # split into parts for viewing
        part_rows = 4
        for p in range(0, rows, part_rows):
            sheet.crop((0, p * (PH + 14), sheet.width, min(sheet.height, (p + part_rows) * (PH + 14)))).save(dest.replace('.png', f'_{p // part_rows}.png'))


if __name__ == '__main__':
    main()
