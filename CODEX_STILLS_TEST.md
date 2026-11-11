# Codex 向け作業指示：イベントスチル画像のテスト生成（5枚）

あなた（Codex）への依頼です。このリポジトリは縦画面のスマホゲーム「三択ダンジョン」（Godot 4）です。
ゲーム内のイベント画像は今、プログラムで描いた仮画像です。画像生成AIで描き直す前に、**テストとして5枚**を作ってください。
画像生成 → 6色への減色 → ピクセルアート化（縮小）まで、すべてこの文書の手順どおりに行ってください。

---

## 1. 完成条件

- 下の「4. 画像リスト」にある5枚すべてについて、次のファイルがそろっている。
  - `art_ai/test/raw/<name>.jpg`：生成した元画像（横長、1536×1024 前後）
  - `art_ai/test/px1/<out>`：336×200 ピクセルの完成画像（細かいドット）
  - `art_ai/test/px2/<out>`：168×100 で作って2倍に拡大した 336×200 の完成画像（粗いドット）
  - `art_ai/test/preview.png`：元画像・px1・px2・今の仮画像を横に並べた比較表
- px1/px2 の画像は、**ちょうど 336×200 ピクセル**で、**下の6色以外の色を1ピクセルも含まない**（`preview.py` が自動で確認する）。
- 画像に文字・枠・UI・署名が入っていない。
- ゲーム本体のファイル（`art/`、`scripts/`、`data/` など）は**一切変更しない**。

## 2. ゲーム側の決まり（必ず守る）

| 項目 | 内容 |
| --- | --- |
| 画像の大きさ | 336×200 ピクセル（ゲーム画面と同じ等倍で表示される） |
| 使える色 | 次の6色だけ |
| 黒 | `#0E0C0E`（14,12,14） |
| 暗いグレー | `#4A4646`（74,70,70） |
| 明るいグレー | `#989288`（152,146,136） |
| 白 | `#E8E2D4`（232,226,212） |
| 明るい赤 | `#CE242E`（206,36,46） |
| 暗い赤 | `#6E141C`（110,20,28） |
| 赤の使い方 | 大事な部分（目の光、血、紋章など）だけに使う。各画像の「Red only:」に書いた部分以外は赤にしない |
| 雰囲気 | 剣と魔法のダークファンタジー、少しホラー。画面の大半は闇で、光は弱い |
| ファイル名 | イベント画像は `events/<イベントID>.png`、選択の結果画像は `results/<イベントID>_<選択肢番号>_<r/ok/ng>.png` |

登場人物（どの画像でも同じ見た目にする）：
- **主人公**：フード付きの長い黒マントの冒険者。顔はフードの影で真っ黒、白い小さな目の光が2つだけ見える。小さなランタンと短剣。
- **少女の霊**：6歳くらい。青白く少し透けている。白い寝間着、裸足、肩までの黒髪、胸に小さな王冠の紋章。影がない。
- **騎士の亡霊**：半透明。錆びた板金鎧、破れた陣羽織に王冠の紋章。兜の中は空っぽで顔がない。長剣。
- **王妃**：長い髪をおろした、裾の長い淡い色のドレスの女性。

## 3. 手順

### 3.1 準備
1. 付録のファイルを、書いてあるパスにそのまま作る（内容を変えない）。
   - `tools/ai_stills/jobs.json`（5枚の指定とプロンプト）
   - `tools/ai_stills/pixelize.py`（減色・縮小）
   - `tools/ai_stills/gen_images.py`（OpenAI Images API で生成。プロンプトの表示もできる）
   - `tools/ai_stills/preview.py`（全画像の減色・縮小と比較表づくり）
2. 空のファイル `art_ai/.gdignore` を作る（Godot がこのフォルダを読み込まないようにするため。アプリの容量が増えない）。
3. Pillow が必要：`pip install pillow`（API で生成する場合は `pip install openai` も）。

### 3.2 元画像の生成（5枚）
次のどちらかの方法で、各画像を `art_ai/test/raw/<name>.jpg` に保存する（PNG なら `<name>.png` でもよい）。

**タイムアウト対策**：1枚生成したらすぐ保存し、次の1枚に進む（まとめて生成しない）。途中で接続が切れても、`art_ai/test/raw/` に既にある画像は作り直さず、残りの画像から続ける。

- **方法A：あなたが画像生成ツールを使える場合**
  1. `python3 tools/ai_stills/gen_images.py --print` で、5枚分の完成プロンプト（共通の画風指定＋場面＋登場人物）が表示される。
  2. 各プロンプトを**一字一句そのまま**使って、横長（1536×1024 などの 3:2 か、それより横長）で1枚ずつ生成する。
  3. 表示された保存先に保存する。
- **方法B：画像生成ツールがない場合**
  - 環境変数 `OPENAI_API_KEY` を使って `python3 tools/ai_stills/gen_images.py` を実行する（1536×1024、quality high）。
  - モデルは `IMAGE_MODEL` で変えられる（初期値 `gpt-image-1`）。もっと新しい画像モデルが使えるならそれでよい。
  - 既にある画像は飛ばす。1枚だけ作り直すときは `--only <name> --force`。

生成した元画像を1枚ずつ目で確認し、次に当てはまるときは**最大2回まで作り直す**：
- 文字・記号・枠・署名が入っている
- 赤以外の色（青・茶・セピアなど）がはっきり付いている
- 「Red only:」以外の部分に赤が大きく使われている
- 主要な被写体が上下の端（各6%）にかかって切れてしまう
- 登場人物の見た目が上の設定と明らかに違う（例：主人公の顔が見えている、騎士の兜の中に顔がある）

### 3.3 減色・縮小と比較表
```sh
python3 tools/ai_stills/preview.py
```
- px1（336×200）と px2（168×100 を2倍）の両方を作り、`art_ai/test/preview.png` に並べる。
- 仕組み：中央を 336:200 に切り抜く → 面積平均で縮小 → 明るさを伸ばす → 赤い部分は赤2色、それ以外は4段階のグレーに置き換える（軽いディザ）→ 孤立した1ピクセルを掃除 → 6色以外がないか確認。
- 調整できる値：
  - `--dither 0.6`：グレーの中間を市松状の点で表す強さ（0＝なし、1＝最大）
  - `--red-sat 0.42`：どのくらい鮮やかな赤を赤とみなすか（下げると赤が増え、上げると減る）
- preview.png を見て、赤にしたい部分が消えていたり、赤が出すぎたりしたら値を変えて全体を作り直す。使った値は報告に書く。値は全画像で同じにする。

### 3.4 コミットと報告
- コミットするもの：`tools/ai_stills/` の4ファイル、`art_ai/.gdignore`、`art_ai/test/` の中身すべて（raw・px1・px2・preview.png）。
- `art/` の仮画像は上書きしない（採用するかどうかは、比較表を見て人間が決める）。
- 作業ブランチやプルリクエストについて別の指示があれば、それに従う。
- **ゲームのリポジトリが作業環境に無い場合**：確認の質問はせずにそのまま進める。比較表の「今の仮画像」の列は空欄でよい。コミットの代わりに `art_ai/` と `tools/ai_stills/` をまとめた zip をダウンロードできる形で出力する。
- 最後に次の内容を報告する：
  1. 使った生成方法（A／B）とモデル名
  2. 減色の値（dither、red-sat）
  3. 5枚それぞれの結果（問題なし／作り直した回数／気になる点）を表で
  4. px1 と px2 のどちらがゲームに合いそうか、あなたの意見

## 4. 画像リスト（5枚）

| # | name | 保存先（px1/px2 の下） | 内容 |
| --- | --- | --- | --- |
| 1 | `e008` | `events/e008.png` | 迷子の少女 |
| 2 | `g025` | `events/g025.png` | 骨の門番（地下25階の門番） |
| 3 | `n02` | `events/n02.png` | 隔離塔 |
| 4 | `e020_0_r` | `results/e020_0_r.png` | 黒い犬→干し肉をやる：犬が隣を歩く |
| 5 | `g100_0_r` | `results/g100_0_r.png` | 迷宮の底→真の結末：母と娘の再会 |

各画像の詳しい場面指定（英語のプロンプト）は付録の `jobs.json` にあります。全画像に共通の画風指定（`style`）と登場人物の設定（`characters`）が自動で付け足されます。

---

## 付録：作成するファイル

### `tools/ai_stills/jobs.json`

```json
{
 "style": "Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not pixel art and no pixel grid (it will be pixelized afterwards).",
 "characters": {
  "HERO": {
   "name": "the hooded adventurer",
   "look": "a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size"
  },
  "GIRL": {
   "name": "the ghost girl",
   "look": "a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow"
  },
  "KNIGHT": {
   "name": "the ghost knight",
   "look": "half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword"
  },
  "QUEEN": {
   "name": "the queen",
   "look": "a woman with long loose hair in a long pale gown"
  }
 },
 "jobs": [
  {
   "name": "e008",
   "out": "events/e008.png",
   "ja": "迷子の少女",
   "prompt": "In a dark stone corridor, {GIRL} stands facing the wall, crying with her hands over her face. Her small body glows faintly white against the darkness, and the floor beneath her shows no shadow at all. Red only: the tiny crest pendant on her chest."
  },
  {
   "name": "g025",
   "out": "events/g025.png",
   "ja": "骨の門番（地下25階の門番）",
   "prompt": "A colossal gate built entirely from countless human bones and skulls fills the whole width of a crypt. Skeletal hands reach out from the gate. At its centre a huge skull with glowing eye sockets looks down. {HERO} is tiny at the bottom centre, seen from behind. Red only: the glowing eye sockets of the skulls."
  },
  {
   "name": "n02",
   "out": "events/n02.png",
   "ja": "隔離塔",
   "prompt": "An old round stone tower that has sunk into the ground and leans to one side, standing alone in darkness. A small iron-barred window. A plague mark is painted on its heavy wooden door, which stands half open, and inside a small empty bed is visible. No people. Red only: the painted plague mark on the door."
  },
  {
   "name": "e020_0_r",
   "out": "results/e020_0_r.png",
   "ja": "黒い犬→干し肉をやる：犬が隣を歩く",
   "prompt": "Side view: {HERO} walks to the right down a dark corridor with a thin black dog trotting at their side. The dog has one glowing eye. Red only: the dog's one eye."
  },
  {
   "name": "g100_0_r",
   "out": "results/g100_0_r.png",
   "ja": "迷宮の底→真の結末：母と娘の再会",
   "prompt": "In a column of soft light rising out of darkness, {QUEEN} kneels and embraces {GIRL} tightly; both have their eyes closed, peaceful. Behind them {KNIGHT} kneels with his sword planted, head bowed. In the background the giant eye is cracked and crumbling into dust. Red only: the cracks of the broken eye."
  }
 ]
}
```

### `tools/ai_stills/pixelize.py`

```python
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
```

### `tools/ai_stills/gen_images.py`

```python
"""Generate the raw illustrations with the OpenAI Images API (fallback when no built-in image tool).

python3 tools/ai_stills/gen_images.py [--only NAME ...] [--force]
python3 tools/ai_stills/gen_images.py --print [--only NAME ...]   # just print the full prompts
Needs OPENAI_API_KEY. Model: $IMAGE_MODEL (default gpt-image-1).
Writes art_ai/test/raw/<name>.jpg (1536x1024).
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
    ap.add_argument('--only', nargs='*')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--print', action='store_true')
    a = ap.parse_args()
    spec = json.load(open(os.path.join(HERE, 'jobs.json'), encoding='utf-8'))
    if a.print:
        for job in spec['jobs']:
            if not a.only or job['name'] in a.only:
                print('=== %s -> art_ai/test/raw/%s.jpg\n%s\n' % (job['name'], job['name'], build_prompt(spec, job)))
        return
    from openai import OpenAI
    client = OpenAI()
    model = os.environ.get('IMAGE_MODEL', 'gpt-image-1')
    os.makedirs(RAW, exist_ok=True)
    for job in spec['jobs']:
        if a.only and job['name'] not in a.only:
            continue
        dst = os.path.join(RAW, job['name'] + '.jpg')
        if os.path.exists(dst) and not a.force:
            print('skip', job['name']); continue
        for attempt in range(4):
            try:
                r = client.images.generate(model=model, prompt=build_prompt(spec, job),
                                           size='1536x1024', quality='high', n=1)
                im = Image.open(io.BytesIO(base64.b64decode(r.data[0].b64_json))).convert('RGB')
                im.save(dst, quality=92)
                print('wrote', dst); break
            except Exception as e:  # rate limits, transient errors
                print('retry', job['name'], e, file=sys.stderr)
                time.sleep(5 * 2 ** attempt)
        else:
            print('FAILED', job['name'], file=sys.stderr)


if __name__ == '__main__':
    main()
```

### `tools/ai_stills/preview.py`

```python
"""Pixelize every raw image (two densities) and build a comparison sheet.

python3 tools/ai_stills/preview.py [--dither 0.6] [--red-sat 0.42]
Reads  art_ai/test/raw/<name>.jpg|png
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
        print('missing raw:', ' '.join(missing))


if __name__ == '__main__':
    main()
```
