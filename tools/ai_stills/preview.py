"""Pixelize the raw images into the game's still format (px1: 336x200, 6 colours) and build review sheets.

python3 tools/ai_stills/preview.py [--batch N] [--dither 0.6] [--red-sat 0.42]
Reads  art_ai/test/raw/<name>.png (raw images are kept outside git; JPEG is refused)
Writes art_ai/test/px1/<out>                 the finished stills
       art_ai/test/preview_b<batch>.png      raw | px1 | current placeholder, one sheet per batch
A job whose raw image is not here keeps its existing px1 file and still appears on its sheet.
"""
import argparse, json, os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from pixelize import pixelize, check, W, H  # noqa: E402

TEST = os.path.join(ROOT, 'art_ai', 'test')


def find_raw(name):
    for ext in ('.jpg', '.jpeg'):
        if os.path.exists(os.path.join(TEST, 'raw', name + ext)):
            sys.exit('JPEG is not allowed (lossy): use the original PNG for %s' % name)
    for ext in ('.png', '.webp'):
        p = os.path.join(TEST, 'raw', name + ext)
        if os.path.exists(p):
            return p
    return None


def sheet(rows, path):
    gap, head = 8, 14
    im = Image.new('RGB', (3 * W + 4 * gap, len(rows) * (H + head + gap) + head + gap), (40, 40, 40))
    d = ImageDraw.Draw(im)
    for i, t in enumerate(('raw', 'px1 (336x200, in game)', 'current placeholder')):
        d.text((gap + i * (W + gap), 4), t, fill=(255, 255, 255))
    for r, (name, cells) in enumerate(rows):
        y = head + gap + r * (H + head + gap)
        d.text((gap, y), name, fill=(255, 255, 255))
        for i, c in enumerate(cells):
            if c is not None:
                im.paste(c, (gap + i * (W + gap), y + head))
    im.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', type=int, help='only this batch')
    ap.add_argument('--dither', type=float, default=0.6)
    ap.add_argument('--red-sat', type=float, default=0.42)
    a = ap.parse_args()
    spec = json.load(open(os.path.join(HERE, 'jobs.json'), encoding='utf-8'))
    batches, made, missing = {}, 0, []
    for job in spec['jobs']:
        if a.batch is not None and job['batch'] != a.batch:
            continue
        dst = os.path.join(TEST, 'px1', job['out'])
        raw = find_raw(job['name'])
        thumb = None
        if raw:
            src = Image.open(raw)
            im = pixelize(src, 1, a.dither, a.red_sat)
            check(im)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im.save(dst)
            made += 1
            thumb = src.convert('RGB').resize((W, H), Image.Resampling.LANCZOS)
        elif not os.path.exists(dst):
            missing.append(job['name'])
            continue
        old = os.path.join(ROOT, 'art', job['out'])
        cells = [thumb, Image.open(dst).convert('RGB'),
                 Image.open(old).convert('RGB') if os.path.exists(old) else None]
        batches.setdefault(job['batch'], []).append((job['name'], cells))
    for b, rows in sorted(batches.items()):
        sheet(rows, os.path.join(TEST, 'preview_b%d.png' % b))
    print('pixelized', made, 'raw images; sheets for batches', sorted(batches))
    if missing:
        print('not generated yet:', ' '.join(missing))


if __name__ == '__main__':
    main()
