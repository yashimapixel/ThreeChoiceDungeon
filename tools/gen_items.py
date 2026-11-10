"""Item icons: art/items/<item>.png, 20x20 pixels, 6-colour palette.

Usage: python3 -I tools/gen_items.py [--sheet out.png]
"""
import os, sys
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K, DG, LG, W, R, DR = (14, 12, 14), (74, 70, 70), (152, 146, 136), (232, 226, 212), (206, 36, 46), (110, 20, 28)
N = 20


def new():
    im = Image.new('RGB', (N, N), K)
    return im, ImageDraw.Draw(im)


def torch(d):
    d.rectangle((9, 9, 10, 18), fill=LG); d.line((9, 9, 9, 18), fill=W)
    d.rectangle((8, 8, 11, 9), fill=DG)
    d.polygon([(6, 8), (10, 1), (13, 8)], fill=R)
    d.polygon([(8, 8), (10, 4), (11, 8)], fill=W)
    d.point((7, 3), fill=DR); d.point((13, 4), fill=DR)


def rope(d):
    for r_, c in ((7, LG), (5, W), (3, LG)):
        d.ellipse((10 - r_, 9 - r_, 10 + r_, 9 + r_), outline=c)
    d.line((16, 10, 17, 18), fill=LG); d.point((17, 18), fill=W)


def key(d):
    d.ellipse((2, 6, 9, 13), outline=W); d.point((5, 9), fill=DG)
    d.line((9, 9, 18, 9), fill=W); d.line((9, 10, 18, 10), fill=LG)
    d.line((15, 10, 15, 14), fill=W); d.line((18, 10, 18, 13), fill=W)
    d.point((12, 8), fill=DR)


def holy(d):
    d.rectangle((9, 1, 11, 4), fill=LG)
    d.ellipse((4, 4, 16, 18), fill=DG, outline=W)
    d.line((10, 7, 10, 15), fill=W); d.line((7, 10, 13, 10), fill=W)
    d.point((7, 7), fill=LG)


def dog(d):
    d.polygon([(4, 18), (4, 7), (6, 2), (8, 7), (12, 7), (14, 2), (16, 7), (16, 18)], fill=DG, outline=LG)
    d.point((8, 11), fill=R); d.point((12, 11), fill=W)
    d.line((9, 15, 11, 15), fill=K)


def map_(d):
    d.polygon([(2, 4), (18, 2), (18, 16), (2, 18)], fill=LG, outline=W)
    d.line((5, 14, 8, 9), fill=DG); d.line((8, 9, 11, 12), fill=DG); d.line((11, 12, 15, 6), fill=DG)
    d.line((14, 5, 16, 7), fill=R); d.line((16, 5, 14, 7), fill=R)


def sword(d):
    d.line((3, 17, 16, 4), fill=W); d.line((4, 17, 17, 4), fill=LG)
    d.line((2, 12, 8, 18), fill=LG)
    d.point((2, 18), fill=R); d.point((17, 3), fill=W)


def amulet(d):
    d.arc((4, 1, 16, 12), 200, 340, fill=LG)
    d.polygon([(10, 6), (16, 12), (10, 18), (4, 12)], fill=R, outline=W)
    d.polygon([(10, 9), (13, 12), (10, 15), (7, 12)], fill=DR)
    d.point((8, 10), fill=W)


def potion(d):
    d.rectangle((8, 1, 12, 5), fill=DG, outline=LG)
    d.ellipse((4, 5, 16, 18), fill=R, outline=W)
    d.rectangle((5, 6, 15, 10), fill=K)
    d.ellipse((4, 5, 16, 18), outline=W)
    d.point((7, 12), fill=W); d.point((7, 13), fill=W)


def girl(d):
    d.polygon([(6, 8), (14, 8), (17, 19), (3, 19)], fill=W)
    d.ellipse((6, 1, 14, 9), fill=W)
    d.ellipse((8, 3, 12, 8), fill=DG)
    d.rectangle((3, 15, 17, 19), fill=LG)


def oath(d):
    d.polygon([(4, 3), (16, 3), (16, 11), (10, 18), (4, 11)], fill=DG, outline=W)
    d.line((10, 5, 10, 15), fill=R); d.line((7, 8, 13, 8), fill=R)


def crown(d):
    d.polygon([(3, 15), (3, 6), (7, 10), (10, 4), (13, 10), (17, 6), (17, 15)], fill=LG, outline=W)
    d.point((10, 12), fill=R); d.point((6, 13), fill=DR); d.point((14, 13), fill=DR)
    d.line((3, 16, 17, 16), fill=W)


def curse(d):
    d.ellipse((2, 2, 18, 18), outline=R)
    pts = [(10, 3), (14, 16), (4, 8), (16, 8), (6, 16), (10, 3)]
    d.line(pts, fill=DR)
    d.ellipse((8, 8, 12, 12), fill=R)


def mark(d):
    d.line((4, 4, 16, 16), fill=R); d.line((16, 4, 4, 16), fill=R)
    d.ellipse((3, 3, 17, 17), outline=DR)
    d.point((10, 10), fill=W)


def eye(d):
    d.ellipse((1, 5, 19, 15), fill=W, outline=LG)
    d.ellipse((6, 5, 14, 15), fill=R)
    d.ellipse((8, 7, 12, 13), fill=K)
    d.point((9, 8), fill=W)


ICONS = dict(torch=torch, rope=rope, key=key, holy=holy, dog=dog, map=map_, sword=sword, amulet=amulet,
             potion=potion, girl=girl, oath=oath, crown=crown, curse=curse, mark=mark, eye=eye)


def ui_textures():
    """9-patch button skins (12x12, patch margins 3/3/3/4) and item frames (6x6)."""
    out = os.path.join(ROOT, 'art', 'ui')
    os.makedirs(out, exist_ok=True)

    def make(rows, name):
        cmap = {'.': K, 'd': DG, 'l': LG, 'w': W, 'r': R, 'x': DR}
        im = Image.new('RGB', (len(rows[0]), len(rows)))
        for y, row in enumerate(rows):
            for x, ch in enumerate(row):
                im.putpixel((x, y), cmap[ch])
        im.save(os.path.join(out, name + '.png'))

    make(['.llllllllll.',
          'lwllllllllll',
          'lldddddddddl',
          'lldddddddddl',
          'lldddddddddl',
          'lldddddddddl',
          'lldddddddddl',
          'lldddddddddl',
          'lldddddddddl',
          'ld........dl',
          'llllllllllll',
          '.dddddddddd.'], 'btn_normal')
    make(['............',
          '.rrrrrrrrrr.',
          'r..........r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r.dddddddd.r',
          'r..........r',
          '.rrrrrrrrrr.'], 'btn_pressed')
    make(['.dddddddddd.',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          'd..........d',
          '.dddddddddd.'], 'btn_disabled')
    make(['.llll.', 'l....l', 'l....l', 'l....l', 'l....l', '.llll.'], 'item_frame')
    make(['.rrrr.', 'r....r', 'r....r', 'r....r', 'r....r', '.rrrr.'], 'item_frame_bad')
    make(['.wwww.', 'w....w', 'w....w', 'w....w', 'w....w', '.wwww.'], 'item_frame_down')
    print('wrote ui textures')


def main():
    ui_textures()
    out = os.path.join(ROOT, 'art', 'items')
    os.makedirs(out, exist_ok=True)
    ims = []
    for name, fn in ICONS.items():
        im, d = new()
        fn(d)
        im.save(os.path.join(out, name + '.png'))
        ims.append(im)
    print('wrote', len(ims), 'icons')
    if '--sheet' in sys.argv:
        s = Image.new('RGB', (len(ims) * 26, 26), (60, 60, 60))
        for i, im in enumerate(ims):
            s.paste(im, (i * 26 + 3, 3))
        s.resize((s.width * 4, s.height * 4), Image.NEAREST).save(sys.argv[sys.argv.index('--sheet') + 1])


if __name__ == '__main__':
    main()
