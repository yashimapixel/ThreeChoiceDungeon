"""Scene kit for result stills: a posable protagonist, positionable scene parts,
shifted prop layers and a tiny scene-spec language.

Spec tokens (space separated, in drawing order):
  B                 event scene (background + event prop)
  BG                event background only
  bg=<name>         another background (corridor, room, cave, ...); bg=black for none
  P:<prop>[@dx,dy][f]   an existing event prop, shifted (and f = mirrored)
  H:<pose>[@x[,yb[,h]]][f][+sword][+lantern]   the protagonist
  X:<part>[@x,y[,n]][f] a scene part (see PARTS)
  FX:<effect><level>    wound / mad / doom / heal / bless (1-4), quiet, dark, red
  nofx              do not add automatic effects from the result
  noicons           do not add item icons
"""
import math
import gen_art as G
from gen_art import C, K, WH, R, W, H, S, PW, PH, figure, skull
from PIL import Image

MAGIC = (1, 2, 3)

# ------------------------------------------------------------------ protagonist
# joints in units of height, origin = feet centre, y negative = up
_STAND = dict(head=(0, -.90), neck=(0, -.80), hip=(0, -.46), lk=(-.05, -.23), lf=(-.07, 0), rk=(.05, -.23), rf=(.07, 0),
              le=(-.13, -.62), lh=(-.14, -.45), re=(.13, -.62), rh=(.14, -.45))


def _pose(**kw):
    d = dict(_STAND)
    d.update(kw)
    return d


POSES = {
    'stand': _pose(),
    'back': _pose(),
    'walk': _pose(lk=(-.08, -.24), lf=(-.15, 0), rk=(.08, -.24), rf=(.13, 0), le=(-.1, -.62), lh=(-.05, -.46), re=(.12, -.62), rh=(.18, -.48)),
    'run': _pose(head=(.13, -.86), neck=(.09, -.76), hip=(0, -.44), rk=(.15, -.30), rf=(.12, -.06), lk=(-.08, -.22), lf=(-.22, -.06),
                 re=(.2, -.62), rh=(.27, -.53), le=(-.04, -.6), lh=(-.14, -.52)),
    'fight': _pose(lk=(-.1, -.23), lf=(-.16, 0), rk=(.1, -.23), rf=(.16, 0), le=(-.08, -.88), lh=(.0, -1.0), re=(.08, -.88), rh=(.02, -1.0)),
    'slash': _pose(rf=(.2, 0), rk=(.15, -.22), lf=(-.15, 0), lk=(-.09, -.22), hip=(.02, -.42), neck=(.06, -.78), head=(.08, -.88),
                   re=(.2, -.68), rh=(.33, -.66), le=(-.1, -.62), lh=(-.15, -.48)),
    'hurt': _pose(head=(.11, -.78), neck=(.07, -.70), hip=(0, -.42), lk=(-.07, -.2), rk=(.09, -.2), lf=(-.08, 0), rf=(.1, 0),
                  re=(.1, -.6), rh=(.03, -.56), le=(-.08, -.58), lh=(-.12, -.38)),
    'kneel': _pose(hip=(0, -.32), neck=(.02, -.66), head=(.03, -.76), rk=(.15, -.3), rf=(.17, 0), lk=(-.04, 0), lf=(-.22, 0),
                   le=(-.1, -.5), lh=(-.11, -.34), re=(.12, -.5), rh=(.16, -.34)),
    'pray': _pose(hip=(0, -.32), neck=(.02, -.66), head=(.03, -.76), rk=(.15, -.3), rf=(.17, 0), lk=(-.04, 0), lf=(-.22, 0),
                  le=(-.08, -.5), lh=(.03, -.56), re=(.12, -.5), rh=(.04, -.57)),
    'reach': _pose(re=(.19, -.67), rh=(.34, -.67)),
    'point': _pose(re=(.18, -.72), rh=(.3, -.82)),
    'cower': _pose(hip=(0, -.25), neck=(.05, -.5), head=(.07, -.58), lk=(-.11, -.25), rk=(.13, -.28), lf=(-.1, 0), rf=(.13, 0),
                   le=(-.06, -.66), lh=(.05, -.68), re=(.15, -.62), rh=(.09, -.7)),
    'jump': _pose(hip=(0, -.62), neck=(0, -.96), head=(0, -1.06), lk=(-.1, -.46), lf=(-.06, -.3), rk=(.1, -.48), rf=(.15, -.33),
                  le=(-.12, -.98), lh=(-.15, -1.12), re=(.12, -.98), rh=(.15, -1.12)),
    'climb': _pose(le=(-.1, -.95), lh=(-.08, -1.1), re=(.1, -.92), rh=(.12, -1.05), rk=(.08, -.34), rf=(.11, -.2)),
    'sit': _pose(hip=(0, -.2), neck=(0, -.55), head=(0, -.65), lk=(-.18, -.22), lf=(-.22, 0), rk=(.18, -.22), rf=(.22, 0),
                 le=(-.12, -.4), lh=(-.16, -.24), re=(.12, -.4), rh=(.16, -.24)),
    'drink': _pose(re=(.12, -.62), rh=(.04, -.79)),
    'listen': _pose(head=(.06, -.89), re=(.12, -.66), rh=(.08, -.84)),
    'arms_up': _pose(le=(-.12, -.88), lh=(-.18, -1.02), re=(.12, -.88), rh=(.18, -1.02)),
    'swim': _pose(head=(0, -.9), neck=(0, -.8), le=(-.16, -.8), lh=(-.3, -.82), re=(.16, -.8), rh=(.3, -.82)),
    'push': _pose(head=(.1, -.86), neck=(.07, -.77), hip=(-.02, -.44), lf=(-.18, 0), lk=(-.1, -.22), rf=(.08, 0), rk=(.06, -.22),
                  re=(.2, -.7), rh=(.32, -.7), le=(.14, -.64), lh=(.28, -.62)),
    'carry': _pose(le=(-.08, -.6), lh=(.02, -.56), re=(.1, -.6), rh=(.18, -.56)),
}


def _rot(p, ang, piv):
    ca, sa = math.cos(ang), math.sin(ang)
    out = {}
    for k, (x, y) in p.items():
        dx, dy = x - piv[0], y - piv[1]
        out[k] = (piv[0] + dx * ca - dy * sa, piv[1] + dx * sa + dy * ca)
    lo = max(v[1] for v in out.values())
    return {k: (v[0], v[1] - lo) for k, v in out.items()}


POSES['down'] = _rot(POSES['stand'], math.radians(-90), (0, -.46))
POSES['sleep'] = POSES['down']
POSES['fall'] = _rot(POSES['arms_up'], math.radians(150), (0, -.5))
POSES['dead'] = _rot(POSES['hurt'], math.radians(-95), (0, -.42))


def _limb(c, a, b, t, fill=K, out=WH):
    dx, dy = b[0] - a[0], b[1] - a[1]
    ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / ln * t, dx / ln * t
    c.poly([(a[0] + nx, a[1] + ny), (b[0] + nx, b[1] + ny), (b[0] - nx, b[1] - ny), (a[0] - nx, a[1] - ny)], fill, out)


FRONT_HANDS = {'pray', 'drink', 'listen', 'carry', 'hurt', 'cower', 'reach', 'slash', 'push', 'point'}


def hero(c, x, yb=92, h=40, pose='stand', flip=False, sword=False, lantern=False, eyes=WH, fill=K, out=WH):
    P = POSES.get(pose, POSES['stand'])
    sx = -1 if flip else 1
    J = {k: (x + sx * v[0] * h, yb + v[1] * h) for k, v in P.items()}
    t = max(1.2, h * 0.04)
    nk, hp = J['neck'], J['hip']
    dx, dy = hp[0] - nk[0], hp[1] - nk[1]
    ln = math.hypot(dx, dy) or 1
    ux, uy = dx / ln, dy / ln          # down the body
    px, py = -uy, ux
    sw, hw, hem = h * 0.11, h * 0.15, h * 0.2
    # back arm, legs
    _limb(c, J['neck'], J['le'], t, fill, out); _limb(c, J['le'], J['lh'], t * 0.9, fill, out)
    _limb(c, J['hip'], J['lk'], t, fill, out); _limb(c, J['lk'], J['lf'], t, fill, out)
    _limb(c, J['hip'], J['rk'], t, fill, out); _limb(c, J['rk'], J['rf'], t, fill, out)
    front_over = pose in FRONT_HANDS
    if not front_over:
        _limb(c, J['neck'], J['re'], t, fill, out); _limb(c, J['re'], J['rh'], t * 0.9, fill, out)
    # cloak covers upper limbs
    pts = [(nk[0] + px * sw * 0.45, nk[1] + py * sw * 0.45), (nk[0] + px * sw + ux * h * .06, nk[1] + py * sw + uy * h * .06),
           (hp[0] + px * hw + ux * hem, hp[1] + py * hw + uy * hem), (hp[0] + ux * hem * 1.1, hp[1] + uy * hem * 1.1),
           (hp[0] - px * hw + ux * hem, hp[1] - py * hw + uy * hem),
           (nk[0] - px * sw + ux * h * .06, nk[1] - py * sw + uy * h * .06), (nk[0] - px * sw * 0.45, nk[1] - py * sw * 0.45)]
    c.poly(pts, fill, out)
    c.line((nk[0] + ux * h * .1, nk[1] + uy * h * .1), (hp[0] + ux * hem * 0.9, hp[1] + uy * hem * 0.9), out)
    if front_over:
        _limb(c, J['neck'], J['re'], t, fill, out); _limb(c, J['re'], J['rh'], t * 0.9, fill, out)
    # hood with a dark face opening
    hx, hy = J['head']
    r = h * 0.095
    bx, by = -ux, -uy                  # up
    back = (hx - sx * px * 0 - bx * 0 , hy)
    peak = (hx + bx * r * 1.6 - sx * (-py) * 0 - sx * r * 0.9 * (1 if abs(ux) < 0.5 else 0), hy + by * r * 1.6)
    c.poly([(hx + px * r * 1.35 + ux * r * 0.9, hy + py * r * 1.35 + uy * r * 0.9), (hx + px * r * 1.4, hy + py * r * 1.4), peak,
            (hx - px * r * 1.4, hy - py * r * 1.4), (hx - px * r * 1.35 + ux * r * 0.9, hy - py * r * 1.35 + uy * r * 0.9)], fill, out)
    c.ell((hx - r * 1.25, hy - r * 1.25, hx + r * 1.25, hy + r * 1.25), fill, out)
    if pose != 'back':
        fx_, fy_ = hx + sx * r * 0.25 + ux * r * 0.15, hy + uy * r * 0.15
        c.ell((fx_ - r * 0.8, fy_ - r * 0.7, fx_ + r * 0.8, fy_ + r * 0.8), K, K)
        if eyes and pose not in ('down', 'sleep', 'dead'):
            c.p(fx_ - 1 + sx * 0.5, fy_, eyes); c.p(fx_ + 1 + sx * 0.5, fy_, eyes)
    if pose in ('sleep',):
        PARTS['zzz'](c, hx + 4, hy - 6, 3)
    if sword:
        hx2, hy2 = J['rh']
        ex, ey = J['re']
        vx, vy = hx2 - ex, hy2 - ey
        vl = math.hypot(vx, vy) or 1
        vx, vy = vx / vl, vy / vl
        L = h * 0.5
        c.line((hx2, hy2), (hx2 + vx * L, hy2 + vy * L), WH, 2)
        c.line((hx2 - vy * 3, hy2 + vx * 3), (hx2 + vy * 3, hy2 - vx * 3), WH)
    if lantern:
        lx, ly = J['lh']
        c.glow(lx, ly + 4, 18, 0.35)
        c.line((lx, ly), (lx, ly + 2))
        c.rect((lx - 2, ly + 2, lx + 2, ly + 7), K, WH)
        c.p(lx, ly + 4, R)


# ------------------------------------------------------------------ scene parts
PARTS = {}


def part(name):
    def deco(fn):
        PARTS[name] = fn
        return fn
    return deco


@part('coins')
def _(c, x=84, y=90, n=14):
    c.glow(x, y - 4, 22, 0.3)
    for i in range(int(n)):
        xx = x + c.r.randint(-12, 12) * (1 - i / (n * 1.6))
        yy = y - i * 0.5 + c.r.randint(-1, 1)
        c.ell((xx - 3, yy - 2, xx + 3, yy + 1), WH, K)


@part('door_open')
def _(c, x=84, y=70):
    c.rect((x - 14, y - 36, x + 14, y), K, WH)
    c.poly([(x + 14, y - 36), (x + 24, y - 40), (x + 24, y + 4), (x + 14, y)], K, WH)
    c.glow(x, y - 16, 16, 0.3)


@part('door_fallen')
def _(c, x=84, y=86):
    c.poly([(x - 22, y), (x + 22, y), (x + 30, y + 8), (x - 30, y + 8)], K, WH)
    for k in (-10, 0, 10):
        c.line((x + k - 2, y + 1), (x + k * 1.3 - 2, y + 7))
    c.rect((x - 14, y - 40, x + 14, y), K, K)


@part('chest_open')
def _(c, x=84, y=84):
    c.glow(x, y - 10, 24, 0.4)
    c.rect((x - 16, y - 12, x + 16, y + 4), K, WH)
    c.poly([(x - 16, y - 12), (x + 16, y - 12), (x + 12, y - 28), (x - 12, y - 28)], K, WH)


@part('flame')
def _(c, x=84, y=80, n=10):
    n = float(n)
    c.glow(x, y - n, n * 2.5, 0.45)
    c.poly([(x - n * 0.6, y), (x - n * 0.2, y - n * 1.4), (x, y - n * 0.8), (x + n * 0.3, y - n * 1.8), (x + n * 0.6, y)], R, R)
    c.poly([(x - n * 0.3, y), (x, y - n), (x + n * 0.3, y)], WH, WH)


@part('fire')
def _(c, x=84, y=96, n=8):
    for i in range(int(n)):
        PARTS['flame'](c, c.r.randint(8, W - 8), y + c.r.randint(-4, 2), c.r.randint(5, 12))


@part('hands')
def _(c, x=84, y=99, n=6):
    for i in range(int(n)):
        hx = x + (i - n / 2) * 10 + c.r.randint(-3, 3)
        top = y - c.r.randint(14, 28)
        c.line((hx, y), (hx, top), WH, 2)
        for k in (-2, -1, 0, 1, 2):
            c.line((hx, top), (hx + k * 1.5, top - 4 + abs(k)))


@part('hand')
def _(c, x=84, y=60, n=1):
    c.line((x, y + 30), (x, y), WH, 2)
    for k in (-2, -1, 0, 1, 2):
        c.line((x, y), (x + k * 2, y - 7 + abs(k)))


@part('eyes')
def _(c, x=84, y=50, n=8):
    for _ in range(int(n)):
        for _t in range(20):
            ex, ey = c.r.randint(6, W - 6), c.r.randint(4, H - 4)
            if c.g(ex, ey) == K:
                c.ell((ex - 3, ey - 1, ex + 3, ey + 1), WH, WH)
                c.p(ex, ey, R)
                break


@part('hole')
def _(c, x=84, y=92, n=26):
    c.ell((x - n, y - n * 0.25, x + n, y + n * 0.25), K, WH)
    for _ in range(18):
        lx = x + c.r.randint(-int(n), int(n))
        ly = c.r.randint(10, 70)
        c.line((lx, ly), (lx, ly + c.r.randint(4, 12)))


@part('water')
def _(c, x=84, y=72, n=0):
    c.clear((0, y, W, H))
    for yy in range(int(y), H, 3):
        for xx in range(0, W, 1):
            if c.r.random() < 0.25 and (xx // 4) % 2:
                c.p(xx, yy)
    c.line((0, y), (W, y))


@part('light')
def _(c, x=84, y=-6, n=70):
    c.glow(x, y, n, 0.45)


@part('rays')
def _(c, x=84, y=-8, n=9):
    for k in range(int(n)):
        a = math.radians(-60 + k * 120 / max(1, n - 1))
        for t in range(0, 110, 2):
            xx, yy = x + math.sin(a) * t, y + math.cos(a) * t
            if G.dith(xx * 2, yy * 2, 0.6 - t / 200) and 0 <= xx < W and 0 <= yy < H and c.g(int(xx), int(yy)) == K:
                c.p(xx, yy)


@part('blood')
def _(c, x=84, y=94, n=22):
    c.ell((x - n, y - n * 0.18, x + n, y + n * 0.18), R, R)


@part('splat')
def _(c, x=84, y=50, n=10):
    for _ in range(int(n)):
        cx, cy = x + c.r.randint(-30, 30), y + c.r.randint(-20, 20)
        for _ in range(c.r.randint(3, 8)):
            c.p(cx + c.r.randint(-3, 3), cy + c.r.randint(-2, 2), R)


@part('skull')
def _(c, x=84, y=88, n=1):
    for i in range(int(n)):
        skull(c, x + i * 7, y)


@part('bones')
def _(c, x=84, y=92, n=10):
    for _ in range(int(n)):
        bx, by = x + c.r.randint(-24, 24), y + c.r.randint(-4, 4)
        if c.r.random() < 0.4:
            skull(c, bx, by)
        else:
            c.line((bx - 4, by), (bx + 4, by + c.r.randint(-2, 2)))


@part('cup')
def _(c, x=84, y=80, n=0):
    c.poly([(x - 3, y - 6), (x + 3, y - 6), (x + 1, y - 1), (x - 1, y - 1)], K, WH)
    c.line((x, y - 1), (x, y + 2)); c.line((x - 2, y + 2), (x + 2, y + 2))


@part('book')
def _(c, x=84, y=78, n=0):
    c.poly([(x - 10, y), (x, y - 3), (x, y + 3), (x - 10, y + 5)], WH, WH)
    c.poly([(x, y - 3), (x + 10, y), (x + 10, y + 5), (x, y + 3)], WH, WH)
    for k in range(3):
        c.line((x - 8, y + 1 + k), (x - 2, y - 1 + k), K)


@part('item')
def _(c, x=84, y=78, n='potion'):
    import gen_results
    gen_results.icon(c, n, int(x), int(y))


@part('web')
def _(c, x=84, y=40, n=60):
    for a in range(0, 360, 40):
        c.line((x, y), (x + math.cos(math.radians(a)) * n, y + math.sin(math.radians(a)) * n * 0.7))
    for rr in range(10, int(n), 12):
        c.d.line([(x + math.cos(math.radians(a)) * rr, y + math.sin(math.radians(a)) * rr * 0.7) for a in range(0, 361, 40)], fill=WH)


@part('ghost')
def _(c, x=84, y=60, n=24):
    n = float(n)
    c.glow(x, y, n, 0.25)
    pts = [(x - n * .4, y), (x - n * .3, y - n * .5), (x, y - n * .65), (x + n * .3, y - n * .5), (x + n * .4, y), (x + n * .45, y + n * .6),
           (x + n * .2, y + n * .45), (x, y + n * .6), (x - n * .2, y + n * .45), (x - n * .45, y + n * .6)]
    c.poly(pts, WH, WH)
    c.drect((x - n * .5, y, x + n * .5, y + n * .6), 0.55, K)
    c.ell((x - n * .2, y - n * .4, x + n * .2, y - n * .05), K, K)


@part('rats')
def _(c, x=84, y=90, n=10):
    for _ in range(int(n)):
        rx, ry = x + c.r.randint(-40, 40), y + c.r.randint(-6, 6)
        c.ell((rx - 3, ry - 2, rx + 3, ry + 1), K, WH)
        c.p(rx + 3, ry - 1, R)
        c.line((rx - 3, ry), (rx - 6, ry + 1))


@part('bats')
def _(c, x=84, y=30, n=14):
    for _ in range(int(n)):
        bx, by = x + c.r.randint(-70, 70), y + c.r.randint(-22, 22)
        c.line((bx - 3, by - 1), (bx, by + 1)); c.line((bx + 3, by - 1), (bx, by + 1))


@part('spider')
def _(c, x=84, y=30, n=1):
    c.ell((x - 8, y - 6, x + 8, y + 6), K, WH)
    for s_ in (-1, 1):
        for i in range(4):
            c.line((x + s_ * 4, y + i * 2 - 2), (x + s_ * (14 + i), y - 6 + i * 6))
    c.p(x - 2, y + 2, R); c.p(x + 2, y + 2, R)


@part('slime')
def _(c, x=84, y=94, n=20):
    c.ell((x - n, y - n * 0.6, x + n, y + n * 0.2), K, WH)
    c.drect((x - n, y - n * 0.6, x + n, y), 0.2)
    c.p(x - 4, y - n * 0.3, R); c.p(x + 4, y - n * 0.3, R)


@part('goblin')
def _(c, x=84, y=92, n=26):
    figure(c, x, y, n, head='plain', body='legs', arms='out', eyes=R)
    c.poly([(x - 3, y - n * 0.85), (x - 9, y - n * 1.0), (x - 3, y - n * 0.78)], K, WH)
    c.poly([(x + 3, y - n * 0.85), (x + 9, y - n * 1.0), (x + 3, y - n * 0.78)], K, WH)


@part('monster')
def _(c, x=84, y=94, n=40):
    n = float(n)
    c.poly([(x - n * .5, y), (x - n * .4, y - n * .7), (x, y - n), (x + n * .4, y - n * .7), (x + n * .5, y)], K, WH)
    c.p(x - n * .12, y - n * .7, R); c.p(x + n * .12, y - n * .7, R)
    for k in range(-2, 3):
        c.poly([(x + k * n * .08, y - n * .5), (x + k * n * .08 + 2, y - n * .5), (x + k * n * .08 + 1, y - n * .42)], WH, WH)


@part('figure')
def _(c, x=84, y=92, n=36):
    figure(c, x, y, n, head='plain', body='robe', arms='down', eyes=R)


@part('hooded')
def _(c, x=84, y=92, n=40):
    figure(c, x, y, n, head='hood', body='robe', arms='out', eyes=R)


@part('knight')
def _(c, x=84, y=92, n=44):
    figure(c, x, y, n, head='helm', body='armor', arms='down', eyes=R)


@part('girl')
def _(c, x=84, y=92, n=28):
    c.glow(x, y - n / 2, n * 0.8, 0.25)
    figure(c, x, y, n, head='girl', body='dress', arms='down', eyes=None, fill=WH, out=WH)
    c.drect((x - n / 3, y - n / 2, x + n / 3, y), 0.4, K)


@part('dog')
def _(c, x=100, y=86, n=0):
    c.ell((x - 12, y - 6, x + 8, y + 4), K, WH)
    c.poly([(x + 4, y - 4), (x + 8, y - 16), (x + 16, y - 14), (x + 14, y - 4)], K, WH)
    c.poly([(x + 9, y - 14), (x + 10, y - 20), (x + 13, y - 15)], K, WH)
    c.line((x - 8, y + 4), (x - 8, y + 8)); c.line((x + 4, y + 4), (x + 4, y + 8))
    c.line((x - 12, y - 2), (x - 18, y - 8))
    c.p(x + 12, y - 11, R)


@part('stairs')
def _(c, x=84, y=96, n=6):
    for i in range(int(n)):
        w = 34 - i * 4
        yy = y - i * 5
        c.rect((x - w, yy - 5, x + w, yy), K, WH)


@part('rope')
def _(c, x=84, y=0, n=60):
    c.line((x, y), (x + 2, y + n), WH)
    for yy in range(int(y), int(y + n), 4):
        c.p(x + (yy - y) / n * 2, yy, WH)


@part('cracks')
def _(c, x=84, y=50, n=5):
    for k in range(int(n)):
        a = c.r.random() * math.tau
        px_, py_ = x, y
        pts = [(px_, py_)]
        for _ in range(9):
            a += c.r.uniform(-0.6, 0.6)
            px_ += math.cos(a) * 6
            py_ += math.sin(a) * 4
            pts.append((px_, py_))
        c.d.line(pts, fill=R, width=3)
        c.d.line(pts, fill=K, width=1)


@part('zzz')
def _(c, x=84, y=40, n=3):
    for i in range(int(n)):
        zx, zy = x + i * 5, y - i * 5
        c.line((zx, zy), (zx + 3, zy)); c.line((zx + 3, zy), (zx, zy + 3)); c.line((zx, zy + 3), (zx + 3, zy + 3))


@part('sparkle')
def _(c, x=84, y=50, n=8):
    for _ in range(int(n)):
        sx_, sy_ = x + c.r.randint(-40, 40), y + c.r.randint(-24, 24)
        c.px1(sx_, sy_); c.px1(sx_ - 1, sy_); c.px1(sx_ + 1, sy_); c.px1(sx_, sy_ - 1); c.px1(sx_, sy_ + 1)


@part('mouth')
def _(c, x=84, y=50, n=30):
    n = float(n)
    c.ell((x - n, y - n * .5, x + n, y + n * .5), R, WH)
    c.ell((x - n * .8, y - n * .32, x + n * .8, y + n * .32), K, K)
    for k in range(-4, 5):
        xx = x + k * n * .18
        c.poly([(xx - 2, y - n * .32), (xx + 2, y - n * .32), (xx, y - n * .12)], WH, K)
        c.poly([(xx - 2, y + n * .32), (xx + 2, y + n * .32), (xx, y + n * .12)], WH, K)


@part('tentacles')
def _(c, x=84, y=99, n=6):
    for k in range(int(n)):
        bx = x + (k - n / 2) * 14
        pts = [(bx, y)]
        xx, yy = bx, y
        for t in range(9):
            xx += math.sin(t * 0.8 + k) * 4
            yy -= 6
            pts.append((xx, yy))
        c.d.line(pts, fill=WH, width=2)
        c.p(pts[-1][0], pts[-1][1], R)


@part('shadow')
def _(c, x=84, y=92, n=40):
    hero(c, x, y, n, 'stand', eyes=R)
    c.drect((x - n * .3, y - n, x + n * .3, y), 0.5, K)


# ------------------------------------------------------------------ prop layers
def prop_layer(c, name, dx=0, dy=0, flip=False, seed=1):
    lay = C(seed)
    lay.im = Image.new('RGB', (PW, PH), MAGIC)
    lay.reset_draw()
    fn = G.P.get(name)
    if not fn:
        return
    fn(lay)
    im = lay.im.transpose(Image.FLIP_LEFT_RIGHT) if flip else lay.im
    src = im.load()
    dst = c.im.load()
    ox, oy = int(dx * S), int(dy * S)
    for Y in range(PH):
        ty = Y + oy
        if not 0 <= ty < PH:
            continue
        for X in range(PW):
            v = src[X, Y]
            if v != MAGIC:
                tx = X + ox
                if 0 <= tx < PW:
                    dst[tx, ty] = v


# ------------------------------------------------------------------ spec composer
def _args(tok):
    """'name@1,2,3f+sword' -> (name, [nums], flags)"""
    flags = set()
    while '+' in tok:
        tok, fl = tok.rsplit('+', 1)
        flags.add(fl)
    if tok.endswith('f') and '@' in tok:
        tok = tok[:-1]
        flags.add('f')
    name, _, rest = tok.partition('@')
    if name.endswith('f') and not rest and name[:-1] in PARTS:
        name = name[:-1]
        flags.add('f')
    nums = []
    for v in rest.split(',') if rest else []:
        try:
            nums.append(float(v))
        except ValueError:
            nums.append(v)
    return name, nums, flags


def compose(spec, event, seed, base_img, bg_img):
    import gen_results as GR
    c = C(seed)
    toks = spec.split()
    auto_fx = True
    icons = True
    fxs = []
    for tok in toks:
        if tok == 'B':
            c.im = base_img.copy(); c.reset_draw()
        elif tok == 'BG':
            c.im = bg_img.copy(); c.reset_draw()
        elif tok.startswith('bg='):
            name = tok[3:]
            if name != 'black':
                G.BGS[name](c)
                c.fade(lambda x, y, n=name: G.BG_DIM.get(n, 0.5))
        elif tok.startswith('P:'):
            name, nums, flags = _args(tok[2:])
            dx = nums[0] if len(nums) > 0 else 0
            dy = nums[1] if len(nums) > 1 else 0
            prop_layer(c, name, dx, dy, 'f' in flags, seed)
        elif tok.startswith('H:'):
            name, nums, flags = _args(tok[2:])
            x = nums[0] if len(nums) > 0 else 84
            yb = nums[1] if len(nums) > 1 else 94
            h = nums[2] if len(nums) > 2 else 40
            hero(c, x, yb, h, name, 'f' in flags, 'sword' in flags, 'lantern' in flags)
        elif tok.startswith('X:'):
            name, nums, flags = _args(tok[2:])
            fn = PARTS.get(name)
            if fn:
                fn(c, *nums)
            else:
                raise KeyError('unknown part ' + name)
        elif tok.startswith('FX:'):
            fxs.append(tok[3:])
        elif tok == 'nofx':
            auto_fx = False
        elif tok == 'noicons':
            icons = False
    return c, fxs, auto_fx, icons


@part('spiderlings')
def _(c, x=84, y=90, n=30):
    for _ in range(int(n)):
        sx_, sy_ = x + c.r.randint(-50, 50), y + c.r.randint(-30, 8)
        c.ell((sx_ - 1, sy_ - 1, sx_ + 1, sy_ + 1), K, WH)
        for k in (-1, 1):
            c.line((sx_ + k, sy_), (sx_ + k * 3, sy_ - 1)); c.line((sx_ + k, sy_), (sx_ + k * 3, sy_ + 2))


@part('tightrope')
def _(c, x=84, y=62, n=70):
    c.d.line([(x - n, y - 2), (x, y + 3), (x + n, y - 2)], fill=WH)


@part('text')
def _(c, x=84, y=40, n=6):
    """scribbled whispers"""
    for i in range(int(n)):
        tx, ty = x + c.r.randint(-50, 40), y + c.r.randint(-20, 20)
        for k in range(c.r.randint(3, 6)):
            c.line((tx + k * 3, ty + c.r.randint(-1, 1)), (tx + k * 3 + 2, ty + c.r.randint(-1, 1)), R if i % 3 == 0 else WH)


@part('memo')
def _(c, x=84, y=70, n=0):
    c.poly([(x - 10, y - 2), (x + 10, y - 4), (x + 11, y + 1), (x - 9, y + 2)], WH, WH)
    for k in range(2):
        c.line((x - 6, y - 2 + k * 1.5), (x + 7, y - 3 + k * 1.5), K)
    c.p(x + 9, y, R)
