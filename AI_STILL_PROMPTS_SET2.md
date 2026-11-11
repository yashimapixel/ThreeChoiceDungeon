# Codex 向け作業指示：画像30枚の一括生成（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の30枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存し、zip にまとめることだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e002.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e002」のように1枚1行の短い報告だけにする。
9. 30枚すべて保存したら、`generated/` の PNG を **`stills_set2.zip`** にまとめ、ダウンロードできる形で出力して終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。

## 画像リスト（30枚）

| # | name | 内容 |
| --- | --- | --- |
| 1 | `e002` | ネズミの群れ |
| 2 | `e003` | 先客の亡骸 |
| 3 | `e004` | 宝箱 |
| 4 | `e005` | 囁く井戸 |
| 5 | `e006` | ゴブリンの見張り |
| 6 | `e007` | 古い祭壇 |
| 7 | `e009` | 燃え残りの焚き火 |
| 8 | `e010` | 闇の行商人 |
| 9 | `e012` | 蜘蛛の巣 |
| 10 | `e013` | 鏡の間 |
| 11 | `e020` | 黒い犬 |
| 12 | `e021` | 走り書きのメモ |
| 13 | `e031` | 弔いの鐘 |
| 14 | `e037` | 渡し守 |
| 15 | `e039` | 沼の魔女 |
| 16 | `e045` | 薄れゆく亡霊 |
| 17 | `e046` | 少女の墓 |
| 18 | `g050` | 都市の番人（地下50階の門番） |
| 19 | `e060` | 王の亡骸 |
| 20 | `n01` | 王の命令書 |
| 21 | `n03` | 騎士の告白 |
| 22 | `n04` | 王の手紙 |
| 23 | `e082` | 心臓の間 |
| 24 | `e095` | 胎動する闇 |
| 25 | `clear` | クリア画面：地上の光 |
| 26 | `e012_2_ng` | 蜘蛛の巣→繭を切り開く（失敗）：子蜘蛛があふれ出す |
| 27 | `e045_0_r` | 薄れゆく亡霊→剣を受け継ぐ：騎士が剣に宿る |
| 28 | `e027_2_r` | 子守唄→少女の霊に任せる：少女が揺りかごに歌う |
| 29 | `g100_1_r` | 迷宮の底→少女を母のもとへ還す：母と娘 |
| 30 | `g100_4_r` | 迷宮の底→闇そのものを討つ：地上の光の中で目覚める |

---

### 1. e002：ネズミの群れ

保存名：`generated/e002.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A narrow stone corridor whose floor is flooded by a river of hundreds of grey rats flowing toward the viewer. the hooded adventurer stands at the right with the lantern raised as the rats part around their boots. Red only: the eyes of the rats, drawn as many bold bright dots all turned toward the viewer.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 2. e003：先客の亡骸

保存名：`generated/e003.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The skeleton of a dead adventurer sits slumped against a dungeon wall, still wearing a rusted helmet and a tattered cloak, a broken sword and a pack beside it. One bony finger points down at a particular floor stone. Lantern light from the left. No living people. Red only: a large red smear on the floor stone the finger points at.
```

### 3. e004：宝箱

保存名：`generated/e004.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A bare, empty stone room. In the very centre stands a magnificent ornate treasure chest, far too splendid for such a place, lit by a single shaft of light, with heavy iron bands and a big lock. No people. Red only: a large gem set into the lock of the chest.
```

### 4. e005：囁く井戸

保存名：`generated/e005.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: An old round stone well in the middle of a dark room, its rim cracked and mossy, a rope and bucket hanging above it. Pale mist rises from the black depth. the hooded adventurer leans over the rim, looking down into it. Red only: a red glow deep inside the well.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 5. e006：ゴブリンの見張り

保存名：`generated/e006.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A fork in a cave with two dark tunnels. A gaunt, grotesque goblin with long ears and a hooked nose sleeps sitting against the rock, hugging a crude spear. Stolen goods are scattered at its feet: coins, a boot, a helmet and a large sack. Not cute. Red only: the large stolen sack at its feet.
```

### 6. e007：古い祭壇

保存名：`generated/e007.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Moss-covered pillars surround an old black stone altar in a ruined shrine, with a few candle stubs. The altar top is covered in layers of dried stains running down its sides. No people. Red only: the dried blood stains on the altar, large and dripping down its sides.
```

### 7. e009：燃え残りの焚き火

保存名：`generated/e009.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A small campfire still smouldering in a cave: glowing embers, a thin trail of smoke, a log seat and an abandoned bedroll beside it, and nobody around. The firelight is the only light. Red only: the glowing embers and the small flames.
```

### 8. e010：闇の行商人

保存名：`generated/e010.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A tall hooded peddler with no visible face, only darkness under the hood, holds up a lantern and beckons with a long bony hand. A huge pack of strange goods is strapped to their back: bottles, bundles and hanging trinkets. Dark stone room. Large in the frame. Red only: the light of the peddler's lantern.
```

### 9. e012：蜘蛛の巣

保存名：`generated/e012.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A stone corridor blocked by a huge, thick white spider web. Several silk-wrapped cocoons hang in it, and one bulges as if something is moving inside. In the darkness of the ceiling, the long hairy legs of a giant spider are barely visible. the hooded adventurer stands small in the foreground, facing the web. Red only: a cluster of eight large glowing spider eyes in the ceiling darkness.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 10. e013：鏡の間

保存名：`generated/e013.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A hall lined with tall mirrors. the hooded adventurer stands in the centre, exhausted. In the largest mirror the reflection is slightly out of step: its hand is raised while the real adventurer's hand is down, and its head is tilted differently. Red only: the two eye dots of the reflection glow red instead of white.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 11. e020：黒い犬

保存名：`generated/e020.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A thin, gaunt black dog emerges from the darkness of a stone corridor and stands still, staring straight at the viewer without growling. Low camera, the dog large in the frame. Red only: one of the dog's eyes glows red; the other eye is dark and normal.
```

### 12. e021：走り書きのメモ

保存名：`generated/e021.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A rotting wooden desk in a dark abandoned room, with a single sheet of note paper on it, lit by a candle stub. The writing on the paper is only blurred, illegible scribbles with no readable letters. A broken wax seal is stuck at the corner of the paper. No people. Red only: the broken wax seal, large.
```

### 13. e031：弔いの鐘

保存名：`generated/e031.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A ruined bell tower. A huge bell hangs from a cracked wooden beam, and countless names are engraved all around its rim, shown as rows of illegible marks. the hooded adventurer stands below, looking up at it. Red only: one single engraved name on the rim glows red.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 14. e037：渡し守

保存名：`generated/e037.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The shore of a black underground lake. A tall hooded ferryman stands beside a small wooden boat moored at the water's edge, holding a long oar and holding out an open bony hand toward the viewer to ask for payment. Mist on the water. Red only: a small lantern hanging at the boat's bow.
```

### 15. e039：沼の魔女

保存名：`generated/e039.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A swamp witch in a cave hut: a hunched old crone with wild grey hair and a crooked toothy grin stirs a big bubbling cauldron, with herbs and bones hanging from the low ceiling. Realistic and grotesque, not cartoonish. Large in the frame. Red only: the glowing liquid in the cauldron.
```

### 16. e045：薄れゆく亡霊

保存名：`generated/e045.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the ghost knight, now very faint and flickering, far more transparent than before, leans against a dungeon wall with one hand on the stone and his head lowered; the edges of the armour dissolve into mist. Large in the frame. Red only: the crown crest on the tabard.

Characters (keep them consistent across images):
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```

### 17. e046：少女の墓

保存名：`generated/e046.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A small, crude gravestone carved with a crown crest stands in a dark crypt; it looks artificial, like a stage prop. the ghost girl stands before it, looking down at the darkness at her feet. the hooded adventurer stands a little behind her. Red only: the crest carved on the gravestone, large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
```

### 18. g050：都市の番人（地下50階の門番）

保存名：`generated/g050.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Before the broken great gate of a ruined underground city stands a colossal guardian built of stone blocks and iron plates, towering over everything. In the middle of its chest a furnace core glows through an iron grille. the hooded adventurer is tiny at its feet, seen from behind. Red only: the glowing furnace core in its chest.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 19. e060：王の亡骸

保存名：`generated/e060.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A crumbled throne room with dust and fallen pillars. On a broken throne sits a dried, mummified king, head slightly bowed, and on his head a crown still shines, untarnished. Large in the frame. Red only: the jewels set in the crown.
```

### 20. n01：王の命令書

保存名：`generated/n01.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The cracked wall of a collapsed government hall. A single large proclamation is pasted on it, faded and torn, its text blurred into illegible grey smudges with no readable letters, and a royal seal at the bottom. the hooded adventurer holds up the lantern to read it. Red only: the wax royal seal at the bottom of the proclamation, large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 21. n03：騎士の告白

保存名：`generated/n03.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a corner of a ruin, the ghost knight has taken off his helmet and holds it in both hands against his chest. Above the neck of the armour there is no head at all, only empty darkness. Side view, quiet and sorrowful, large in the frame. Red only: the crown crest on the tabard.

Characters (keep them consistent across images):
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```

### 22. n04：王の手紙

保存名：`generated/n04.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The bottom of a deep crevice, where thousands of sealed envelopes lie piled like snow while more flutter down one by one from the darkness above. the hooded adventurer stands knee-deep among them, holding one envelope. Red only: the wax seals on the envelopes nearest the viewer, all the same seal, drawn large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 23. e082：心臓の間

保存名：`generated/e082.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A chamber made of organic flesh. In its centre a gigantic heart beats, its veins spreading across the walls and floor. A large glowing crystal is embedded in the heart's surface. the hooded adventurer stands small before it. Red only: the glowing crystal and the veins closest to it.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 24. e095：胎動する闇

保存名：`generated/e095.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Pure darkness that seems to pulse like the inside of a living body, with faint curved membranes. In the centre the darkness bulges as if something small is moving inside, and faint small bare footprints on the floor lead into it. the hooded adventurer stands at the edge with the lantern lowered. Red only: a red heartbeat glow at the centre of the darkness.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 25. clear：クリア画面：地上の光

保存名：`generated/clear.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A wide shaft of pale light pours down from far above into the darkness. the hooded adventurer stands in the light with both arms raised, seen from behind, looking up toward the surface, dust drifting in the light. Red only: a single small red flower blooming at the adventurer's feet, drawn large enough to see.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 26. e012_2_ng：蜘蛛の巣→繭を切り開く（失敗）：子蜘蛛があふれ出す

保存名：`generated/e012_2_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Close-up: a silk cocoon has burst open and a flood of countless small spiders pours out over the hooded adventurer, who recoils and slashes with the short sword. Red only: the eyes of the spiders, shown as many bold red dots.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 27. e045_0_r：薄れゆく亡霊→剣を受け継ぐ：騎士が剣に宿る

保存名：`generated/e045_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the ghost knight dissolves into streams of light that flow into a sword held up by the hooded adventurer; the blade begins to glow. Light trails run from the fading armour into the blade. Red only: the crown crest on the tabard of the fading knight.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```

### 28. e027_2_r：子守唄→少女の霊に任せる：少女が揺りかごに歌う

保存名：`generated/e027_2_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the ghost girl leans over an ornate wooden cradle and sings softly to it, both hands on its edge, a faint glow around her. the hooded adventurer stands back in the shadows, watching. Red only: the crown crest carved on the cradle's headboard, large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
```

### 29. g100_1_r：迷宮の底→少女を母のもとへ還す：母と娘

保存名：`generated/g100_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark chamber of flesh, the queen emerges from the flesh wall, her body unravelling free of it, and embraces the ghost girl; both sing with their eyes closed and begin to rise as motes of light. Their faces are clearly lit and readable. Behind them the giant eye withers and shrivels. Red only: the iris of the withering giant eye.

Characters (keep them consistent across images):
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
- the queen: a woman with long loose hair in a long pale gown
```

### 30. g100_4_r：迷宮の底→闇そのものを討つ：地上の光の中で目覚める

保存名：`generated/g100_4_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be large, bold and clearly visible, because small red details disappear when shrunk. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the hooded adventurer lies collapsed on grass just outside the dark mouth of the labyrinth, under the bright light of the surface, the sword still in hand, dust drifting in the air. Red only: a red wildflower blooming next to the adventurer's hand, drawn large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```
