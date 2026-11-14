# Codex 向け作業指示：画像23枚の作り直し（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の23枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e005_1_ng.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e005_1_ng」のように1枚1行の短い報告だけにする。
9. 23枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_redo3.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（23枚）

| # | name | 内容 | 作り直す理由 |
| --- | --- | --- | --- |
| 1 | `e005_1_ng` | 囁く井戸→水を汲んで飲む（失敗） | 空と月が描かれた → 地下の部屋に |
| 2 | `e009_1_r` | 燃え残りの焚き火→火を絶やさぬよう番をする | 夜の森になった → 洞窟の中に |
| 3 | `e009_2_r` | 燃え残りの焚き火→火の中から薪を一本拝借する | 夜の森とテント → 洞窟の中に |
| 4 | `e009_3_r` | 燃え残りの焚き火→火の傍で装備を手入れする | 夜の森になった → 洞窟の中に |
| 5 | `e010_0_r` | 闇の行商人→血で聖水を買う | 行商人に顔があった → 顔のない行商人に |
| 6 | `e010_1_r` | 闇の行商人→記憶で薬瓶を買う | 行商人に顔があった → 顔のない行商人に |
| 7 | `e010_2_r` | 闇の行商人→運を売って古地図を買う | 行商人に顔があった → 顔のない行商人に |
| 8 | `e020_2_r` | 黒い犬→追い払う | 犬が白っぽかった → 真っ黒な犬に |
| 9 | `e023_1_ok` | 甲冑の亡霊→手合わせを願う（成功） | 背景に月 → 地下の回廊に |
| 10 | `e024_2_r` | コウモリの嵐→黒い犬に追い払わせる | 犬が白っぽかった → 真っ黒な犬に |
| 11 | `e027_1_ok` | 子守唄→揺りかごを止める（成功） | 窓に月、紋章が獅子 → 窓のない部屋、王冠の紋章に |
| 12 | `e029_0_ng` | 盗賊の待ち伏せ→戦う（失敗） | 背景に城と空 → 洞窟の中に |
| 13 | `e029_3_r` | 盗賊の待ち伏せ→大人しく荷物を渡す | 背景に月 → 洞窟の中に |
| 14 | `e030_2_ok` | 水晶玉→水晶玉を持ち去る（成功） | 月と廃墟の屋外 → 地下の部屋に |
| 15 | `e031_0_ng` | 弔いの鐘→鐘を鳴らす（失敗） | 空と雲 → 地下の鐘楼に |
| 16 | `e031_1_ng` | 弔いの鐘→自分の名前を削り取る（失敗） | 窓に月 → 窓のない鐘楼に |
| 17 | `e031_2_r` | 弔いの鐘→静かに通り過ぎる | 空と月 → 地下の大洞窟に |
| 18 | `n06_2_r` | 迷宮の中の街角→街灯の火をもらう | 空と月と城 → 岩の天井の下に |
| 19 | `e037_1_r` | 渡し守→思い出を一つ払う | 湖の上に月と城 → 地下の湖に |
| 20 | `e037_2_ok` | 渡し守→渡し守を突き落として舟を奪う（成功） | 湖の上に月 → 地下の湖に |
| 21 | `e037_2_ng` | 渡し守→渡し守を突き落として舟を奪う（失敗） | 湖の上に月 → 地下の湖に |
| 22 | `e039_1_r` | 沼の魔女→薬だけ売ってもらう | 窓に月 → 窓のない洞窟の小屋に |
| 23 | `e039_2_ng` | 沼の魔女→鍋をひっくり返して逃げる（失敗） | 空と月 → 洞窟の中に |

---

### 1. e005_1_ng：囁く井戸→水を汲んで飲む（失敗）

保存名：`generated/e005_1_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room underground, the hooded adventurer spits out a mouthful of dark liquid from a bucket at an old stone well, recoiling. Red only: the liquid, which is blood.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 2. e009_1_r：燃え残りの焚き火→火を絶やさぬよう番をする

保存名：`generated/e009_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave, the hooded adventurer sits awake beside a small campfire, feeding it a stick and warming their hands; rock walls all around. Red only: the small flames.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 3. e009_2_r：燃え残りの焚き火→火の中から薪を一本拝借する

保存名：`generated/e009_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave, the hooded adventurer walks away from a small campfire holding up a burning branch as a torch; rock walls all around. Red only: the flame on the branch.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 4. e009_3_r：燃え残りの焚き火→火の傍で装備を手入れする

保存名：`generated/e009_3_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave, the hooded adventurer sits beside a small campfire sharpening a short sword on a whetstone, boots laced tight; rock walls all around. Red only: the embers.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 5. e010_0_r：闇の行商人→血で聖水を買う

保存名：`generated/e010_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room, the faceless peddler makes a thin cut on the forearm of the hooded adventurer with a small blade and hands over a little vial. Red only: the thin cut.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the faceless peddler: a tall figure in a long dark hooded robe; under the hood there is no face at all, only darkness; long bony hands; carries a lantern and a huge pack of strange goods
```

### 6. e010_1_r：闇の行商人→記憶で薬瓶を買う

保存名：`generated/e010_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room, the hooded adventurer stands dazed holding a small potion bottle while the faceless peddler draws a glowing wisp of memory out of their head. Red only: the liquid in the bottle.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the faceless peddler: a tall figure in a long dark hooded robe; under the hood there is no face at all, only darkness; long bony hands; carries a lantern and a huge pack of strange goods
```

### 7. e010_2_r：闇の行商人→運を売って古地図を買う

保存名：`generated/e010_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room, the faceless peddler nods and hands an old map to the hooded adventurer. Red only: a route marked on the map.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the faceless peddler: a tall figure in a long dark hooded robe; under the hood there is no face at all, only darkness; long bony hands; carries a lantern and a huge pack of strange goods
```

### 8. e020_2_r：黒い犬→追い払う

保存名：`generated/e020_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone corridor, the black dog glances back once at the hooded adventurer as it walks away into the darkness. Red only: the dog's one glowing eye.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the black dog: a thin, gaunt dog with pitch-black fur; one eye glows red, the other is dark
```

### 9. e023_1_ok：甲冑の亡霊→手合わせを願う（成功）

保存名：`generated/e023_1_ok.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a ruined underground corridor, the ghost knight swings his sword clean through the body of the hooded adventurer, who stands unharmed, the arc of the ghostly blade glowing. Red only: the crown crest on the tabard.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```

### 10. e024_2_r：コウモリの嵐→黒い犬に追い払わせる

保存名：`generated/e024_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave, the black dog barks at a swarm of bats, which flees in all directions; the hooded adventurer stands behind it. Red only: the dog's one glowing eye.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the black dog: a thin, gaunt dog with pitch-black fur; one eye glows red, the other is dark
```

### 11. e027_1_ok：子守唄→揺りかごを止める（成功）

保存名：`generated/e027_1_ok.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room with no windows, the hooded adventurer holds a stilled ornate wooden cradle and finds coins hidden under its floorboard. Red only: the crown crest carved on the cradle's headboard.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 12. e029_0_ng：盗賊の待ち伏せ→戦う（失敗）

保存名：`generated/e029_0_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave with rock walls all around, the hooded adventurer clutches their side, wounded, while a bandit with a red scarf runs off into a tunnel with their pack. Red only: the wound.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 13. e029_3_r：盗賊の待ち伏せ→大人しく荷物を渡す

保存名：`generated/e029_3_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark cave with rock walls all around, the hooded adventurer hands over their pack to a bandit holding a dagger. Red only: the bandit's scarf.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 14. e030_2_ok：水晶玉→水晶玉を持ち去る（成功）

保存名：`generated/e030_2_ok.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone room underground, the hooded adventurer wraps a glowing crystal ball in cloth and tucks it under their arm, beside an empty pedestal. Red only: a small red glint in the ball.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 15. e031_0_ng：弔いの鐘→鐘を鳴らす（失敗）

保存名：`generated/e031_0_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Inside a ruined underground bell tower enclosed by rock and stone, the hooded adventurer has rung a huge bell; in the darkness beyond, giant eyes open. Red only: the eyes.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 16. e031_1_ng：弔いの鐘→自分の名前を削り取る（失敗）

保存名：`generated/e031_1_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Inside a ruined underground bell tower with no windows, the hooded adventurer scrapes at a bell's rim with a knife but the glowing mark keeps reappearing. Red only: the glowing mark, with no letters or symbols in it.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 17. e031_2_r：弔いの鐘→静かに通り過ぎる

保存名：`generated/e031_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Inside a vast underground cavern, the hooded adventurer walks away from a ruined bell tower as the bell swings once behind them; cave ceiling above, no sky. Red only: the glow on the bell's rim.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 18. n06_2_r：迷宮の中の街角→街灯の火をもらう

保存名：`generated/n06_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On a city street corner standing inside a dungeon passage, its edges fading into cave rock and a rock ceiling above with no sky, the hooded adventurer lights a torch from an iron street lamp; the new flame burns oddly white. Red only: the street lamp's flame.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 19. e037_1_r：渡し守→思い出を一つ払う

保存名：`generated/e037_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On a still black lake in a vast underground cavern with a rock ceiling above, the hooded adventurer sits in a small boat with empty eyes as a faint memory image of a village drifts away over the water like mist. Red only: the lantern at the bow.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 20. e037_2_ok：渡し守→渡し守を突き落として舟を奪う（成功）

保存名：`generated/e037_2_ok.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On a black lake in a vast underground cavern with a rock ceiling above, the hooded adventurer rows a stolen boat while pale hands reach up from the water behind. Red only: the lantern at the bow.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 21. e037_2_ng：渡し守→渡し守を突き落として舟を奪う（失敗）

保存名：`generated/e037_2_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On the rocky shore of an underground lake in a vast cavern, the hooded adventurer drags themselves out soaking wet while the hooded ferryman stands in his boat behind. Red only: the lantern at the bow.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 22. e039_1_r：沼の魔女→薬だけ売ってもらう

保存名：`generated/e039_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a witch's hut built inside a cave, with no windows and rock walls behind, a swamp witch counts coins and hands the hooded adventurer a small potion bottle. Red only: the liquid in the cauldron.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 23. e039_2_ng：沼の魔女→鍋をひっくり返して逃げる（失敗）

保存名：`generated/e039_2_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Inside a dark cave, with rock walls and a low rock ceiling, a witch's curse, a dark streak of light from her outstretched hand, strikes the hooded adventurer in the back as they flee. Red only: the curse.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```
