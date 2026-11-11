"""Generate the raw illustrations with the OpenAI Images API (fallback when no built-in image tool).

python3 tools/ai_stills/gen_images.py --batch N [--only NAME ...] [--force]
python3 tools/ai_stills/gen_images.py --print --batch N       # just print the full prompts
Needs OPENAI_API_KEY. Model: $IMAGE_MODEL (default gpt-image-1).
Writes art_ai/test/raw/<name>.png (1536x1024). Never JPEG.
"""
import argparse, base64, io, json, os, sys, time
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RAW = os.path.join(ROOT, 'art_ai', 'test', 'raw')


def build_prompt(spec, job):
    p, cast = job['prompt'], []
    for k, c in spec['characters'].items():
        if '{%s}' % k in p:
            p = p.replace('{%s}' % k, c['name'])
            cast.append('- %s: %s' % (c['name'], c['look']))
    out = spec['style'] + '\n\nScene: ' + p
    if cast:
        out += '\n\nCharacters (keep them consistent across images):\n' + '\n'.join(cast)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', type=int, help='only this batch (5 images each)')
    ap.add_argument('--only', nargs='*')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--print', action='store_true')
    a = ap.parse_args()
    spec = json.load(open(os.path.join(HERE, 'jobs.json'), encoding='utf-8'))
    spec['jobs'] = [j for j in spec['jobs'] if (a.batch is None or j['batch'] == a.batch)
                    and (not a.only or j['name'] in a.only)]
    if a.print:
        for job in spec['jobs']:
            print('=== %s -> art_ai/test/raw/%s.png\n%s\n' % (job['name'], job['name'], build_prompt(spec, job)))
        return
    from openai import OpenAI
    client = OpenAI()
    model = os.environ.get('IMAGE_MODEL', 'gpt-image-1')
    os.makedirs(RAW, exist_ok=True)
    for job in spec['jobs']:
        dst = os.path.join(RAW, job['name'] + '.png')
        done = any(os.path.exists(os.path.join(RAW, job['name'] + e)) for e in ('.png', '.webp'))
        if done and not a.force:
            print('skip', job['name']); continue
        for attempt in range(4):
            try:
                r = client.images.generate(model=model, prompt=build_prompt(spec, job),
                                           size='1536x1024', quality='high', n=1)
                im = Image.open(io.BytesIO(base64.b64decode(r.data[0].b64_json))).convert('RGB')
                im.save(dst)
                print('wrote', dst); break
            except Exception as e:  # rate limits, transient errors
                print('retry', job['name'], e, file=sys.stderr)
                time.sleep(5 * 2 ** attempt)
        else:
            print('FAILED', job['name'], file=sys.stderr)


if __name__ == '__main__':
    main()
