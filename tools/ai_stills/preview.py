"""Pixelize every raw image (two densities) and build a comparison sheet.

python3 tools/ai_stills/preview.py [--dither 0.6] [--red-sat 0.42]
Reads  every art_ai/test/raw/<name>.jpg|png that exists so far (all batches)
Writes art_ai/test/px1/<out>, art_ai/test/px2/<out>, art_ai/test/preview.png
"""
import argparse, json, os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from pixelize import pixelize, check, W, H  # noqa: E402

TEST = os.path.join(ROOT, 'art_ai', 'test')


def find_raw(name):
    for ext in ('.jpg', '.png', '.webp'):
        p = os.path.join(TEST, 'raw', name + ext)
        if os.path.exists(p):
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dither', type=float, default=0.6)
    ap.add_argument('--red-sat', type=float, default=0.42)
    a = ap.parse_args()
    spec = json.load(open(os.path.join(HERE, 'jobs.json'), encoding='utf-8'))
    rows, missing = [], []
    for job in spec['jobs']:
        raw = find_raw(job['name'])
        if not raw:
            missing.append(job['name']); continue
        src = Image.open(raw)
        cells = [src.convert('RGB').resize((W, H), Image.Resampling.LANCZOS)]
        for px in (1, 2):
            im = pixelize(src, px, a.dither, a.red_sat)
            check(im)
            dst = os.path.join(TEST, 'px%d' % px, job['out'])
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im.save(dst)
            cells.append(im)
        old = os.path.join(ROOT, 'art', job['out'])
        cells.append(Image.open(old).convert('RGB') if os.path.exists(old) else Image.new('RGB', (W, H)))
        rows.append((job['name'], cells))
    if rows:
        gap, head = 8, 14
        sheet = Image.new('RGB', (4 * W + 5 * gap, len(rows) * (H + head + gap) + head + gap), (40, 40, 40))
        d = ImageDraw.Draw(sheet)
        for i, t in enumerate(('raw', 'px1 (336x200)', 'px2 (168x100 x2)', 'current placeholder')):
            d.text((gap + i * (W + gap), 4), t, fill=(255, 255, 255))
        for r, (name, cells) in enumerate(rows):
            y = head + gap + r * (H + head + gap)
            d.text((gap, y), name, fill=(255, 255, 255))
            for i, c in enumerate(cells):
                sheet.paste(c, (gap + i * (W + gap), y + head))
        sheet.save(os.path.join(TEST, 'preview.png'))
        print('wrote preview with', len(rows), 'rows')
    if missing:
        print('not generated yet:', ' '.join(missing))


if __name__ == '__main__':
    main()
