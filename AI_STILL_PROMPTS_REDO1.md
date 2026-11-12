# Codex 向け作業指示：画像4枚の作り直し（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像のうち、下の4枚を作り直してください。プロンプトは修正済みです。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存し、zip にまとめることだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e006.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい。
7. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e006」のように1枚1行の短い報告だけにする。
8. 4枚すべて保存したら、`generated/` の PNG を **`stills_redo1.zip`** にまとめ、ダウンロードできる形で出力して終了する。

## 画像リスト（4枚）

| # | name | 内容 | 作り直す理由 |
| --- | --- | --- | --- |
| 1 | `e006` | ゴブリンの見張り | 盗品の袋の赤が大きすぎた → 赤は槍に結んだ小さな布だけに |
| 2 | `e010` | 闇の行商人 | ランタンの赤が袖まで広がった → 赤はランタンの炎だけ、服は黒とグレー |
| 3 | `e013` | 鏡の間 | 鏡の中の目の赤が小さすぎた → 鏡像を大きく、目の赤を大きくはっきり |
| 4 | `e031` | 弔いの鐘 | 赤い名前が文字に見えた → 文字を一切入れず、赤は光るしみだけに |

---

### 1. e006：ゴブリンの見張り

保存名：`generated/e006.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A fork in a cave with two dark tunnels. A gaunt, grotesque goblin with long ears and a hooked nose sleeps sitting against the rock, hugging a crude spear. Stolen goods are scattered at its feet: coins, a boot, a helmet and a sack, all in greys. Not cute. Red only: a small strip of red cloth tied just below the spearhead, clearly visible but covering only a small part of the image; everything else, including the sack, is grey.
```

### 2. e010：闇の行商人

保存名：`generated/e010.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A tall hooded peddler with no visible face, only darkness under the hood, holds up a lantern and beckons with a long bony hand. A huge pack of strange goods is strapped to their back: bottles, bundles and hanging trinkets. Dark stone room. Large in the frame. Red only: the small flame inside the lantern glass. The peddler's robe, sleeves, arms and hands are black and grey with no red on them at all.
```

### 3. e013：鏡の間

保存名：`generated/e013.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A hall lined with tall mirrors. the hooded adventurer stands in the left half of the frame, exhausted. The largest mirror fills the right half, and the reflection in it is slightly out of step: its hand is raised while the real adventurer's hand is down, and its head is tilted differently. The reflection is large and close. Red only: the two eyes of the reflection glow bright red, drawn big and bold with a red glow around them, instead of white.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 4. e031：弔いの鐘

保存名：`generated/e031.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A ruined bell tower. A huge bell hangs from a cracked wooden beam, and countless names are engraved all around its rim, shown only as rows of tiny scratches, never as readable letters. the hooded adventurer stands below, looking up at it. Red only: a red glow on one small spot of the bell's rim, a glowing smudge with no letters or symbols in it. Absolutely no writing, letters or alphabet anywhere in the image.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```
