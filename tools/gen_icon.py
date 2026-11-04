"""Generates icon.png (192) and Android adaptive icon layers (432)."""
import os
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K, W, R = (14, 12, 14), (232, 226, 212), (196, 28, 40)

def doors(size=48):
    im = Image.new('RGB', (size, size), K)
    d = ImageDraw.Draw(im)
    # three arched doors, the middle one red
    for i, x in enumerate((6, 19, 32)):
        col = R if i == 1 else W
        top = 14 if i == 1 else 18
        d.ellipse((x, top, x + 10, top + 10), outline=col)
        d.rectangle((x, top + 5, x + 10, 40), outline=col)
        d.line((x + 1, top + 5, x + 9, top + 5), fill=K)
        if i == 1:
            d.point((x + 7, 28), fill=W)
    d.line((2, 41, 45, 41), fill=W)
    for x in range(4, 44, 3):
        d.point((x, 43), fill=W)
    return im

ic = doors().resize((192, 192), Image.NEAREST)
ic.save(os.path.join(ROOT, 'icon.png'))
fg = Image.new('RGBA', (432, 432), (0, 0, 0, 0))
fg.paste(doors().resize((240, 240), Image.NEAREST), (96, 96))
fg.save(os.path.join(ROOT, 'art', 'icon_fg.png'))
Image.new('RGB', (432, 432), K).save(os.path.join(ROOT, 'art', 'icon_bg.png'))
print('icons ok')
