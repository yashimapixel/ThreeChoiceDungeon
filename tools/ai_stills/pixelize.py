"""Turn a generated illustration into a 336x200 still in the game's 6-colour palette.

python3 pixelize.py RAW.png OUT.png [--px 1|2] [--dither 0.0-1.0] [--red-sat 0.42]
  --px 1 : 336x200 native pixels (finest)
  --px 2 : drawn at 168x100, then doubled to 336x200 (chunkier)
"""
import argparse
import colorsys
from PIL import Image

W, H = 336, 200
K, DG, LG, WH = (14, 12, 14), (74, 70, 70), (152, 146, 136), (232, 226, 212)
R, DR = (206, 36, 46), (110, 20, 28)
PALETTE = [K, DG, LG, WH, R, DR]
GREYS = [K, DG, LG, WH]
BAYER4 = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def lum(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


GREY_L = [lum(c) for c in GREYS]


def crop_to_aspect(im):
    w, h = im.size
    target = W / H
    if w / h > target:
        nw = round(h * target)
        x0 = (w - nw) // 2
        return im.crop((x0, 0, x0 + nw, h))
    nh = round(w / target)
    y0 = (h - nh) // 2
    return im.crop((0, y0, w, y0 + nh))


def levels(px, w, h):
    """Stretch luminance so the darkest 1% is black and the brightest 1% is white."""
    ls = sorted(lum(px[x, y]) for y in range(h) for x in range(w))
    lo, hi = ls[int(len(ls) * 0.01)], ls[int(len(ls) * 0.99) - 1]
    return lo, max(hi, lo + 1)


def quantize(im, dither, red_sat):
    w, h = im.size
    src = im.load()
    lo, hi = levels(src, w, h)
    out = Image.new('RGB', (w, h))
    dst = out.load()
    span = GREY_L[-1] - GREY_L[0]
    for y in range(h):
        for x in range(w):
            r, g, b = src[x, y]
            hh, ss, vv = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            hue = hh * 360
            if (hue < 22 or hue > 338) and ss >= red_sat and vv >= 0.18:
                dst[x, y] = R if vv >= 0.55 else DR
                continue
            l = (lum((r, g, b)) - lo) / (hi - lo)
            l = GREY_L[0] + min(1.0, max(0.0, l)) * span
            # position between the two nearest grey levels, then ordered dither
            for i in range(3):
                if l <= GREY_L[i + 1] or i == 2:
                    break
            t = (l - GREY_L[i]) / (GREY_L[i + 1] - GREY_L[i])
            thr = 0.5 + dither * ((BAYER4[y % 4][x % 4] + 0.5) / 16 - 0.5)
            dst[x, y] = GREYS[i + 1] if t > thr else GREYS[i]
    return out


def despeckle(im):
    """Replace single pixels whose four neighbours all agree on another colour."""
    w, h = im.size
    src = im.load()
    out = im.copy()
    dst = out.load()
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            n = [src[x - 1, y], src[x + 1, y], src[x, y - 1], src[x, y + 1]]
            if n[0] == n[1] == n[2] == n[3] != src[x, y] and src[x, y] not in (R, DR):
                dst[x, y] = n[0]
    return out


def pixelize(raw, px=1, dither=0.6, red_sat=0.42):
    im = crop_to_aspect(raw.convert('RGB'))
    small = im.resize((W // px, H // px), Image.Resampling.BOX)
    q = despeckle(quantize(small, dither, red_sat))
    if px > 1:
        q = q.resize((W, H), Image.Resampling.NEAREST)
    return q


def check(im):
    assert im.size == (W, H), im.size
    extra = {c for _, c in im.getcolors(W * H)} - set(PALETTE)
    assert not extra, 'off-palette colours: %s' % sorted(extra)[:5]


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('raw')
    ap.add_argument('out')
    ap.add_argument('--px', type=int, default=1, choices=(1, 2))
    ap.add_argument('--dither', type=float, default=0.6)
    ap.add_argument('--red-sat', type=float, default=0.42)
    a = ap.parse_args()
    res = pixelize(Image.open(a.raw), a.px, a.dither, a.red_sat)
    check(res)
    res.save(a.out)
    print('wrote', a.out)
