# Codex 向け作業指示：安全判定で止まった3枚の書き出し直し（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の3枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e053_1_ng.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e053_1_ng」のように1枚1行の短い報告だけにする。
9. 3枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_redo4.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（3枚）

| # | name | 内容 | 作り直す理由 |
| --- | --- | --- | --- |
| 1 | `e053_1_ng` | 湖の歌声→歌に合わせて歌い返す（失敗） | 「喉を押さえる」表現を外し、声が光になって流れていく表現に |
| 2 | `e074_1_r` | 血の泉→傷口を泉に浸す | 「傷口」「自分の血を吸われる」を外し、腕を浸すと赤い糸が泉へ流れる表現に |
| 3 | `e075_1_ng` | 吊るされた人々→せめて楽にしてやる（失敗） | 「吊るされた」「息絶える」を外し、菌糸の繭に包まれた人が手を伸ばす表現に |

---

### 1. e053_1_ng：湖の歌声→歌に合わせて歌い返す（失敗）

保存名：`generated/e053_1_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Draw a royal crest only where the scene or a character description mentions one; it is always a simple crown shape. Do not add crowns or crests anywhere else. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On the rocky shore of an underground lake, the hooded adventurer sings toward a pale woman sitting on a rock in the water; faint wisps of light drift from the adventurer's open mouth across the water to her, as if their voice is being carried away. One hand is raised in surprise. Red only: the woman's lips.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 2. e074_1_r：血の泉→傷口を泉に浸す

保存名：`generated/e074_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Draw a royal crest only where the scene or a character description mentions one; it is always a simple crown shape. Do not add crowns or crests anywhere else. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a great underground hall, the hooded adventurer kneels at the rim of a stone fountain filled with dark red liquid and dips one forearm into it; thin red threads curl from the arm into the pool, as if the fountain is drinking. Red only: the liquid in the fountain.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 3. e075_1_ng：吊るされた人々→せめて楽にしてやる（失敗）

保存名：`generated/e075_1_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Draw a royal crest only where the scene or a character description mentions one; it is always a simple crown shape. Do not add crowns or crests anywhere else. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Beneath a gigantic mushroom in a dark cave, people are wrapped like cocoons in pale fungal threads that hold them up under its cap. One of them stretches a weak hand toward the hooded adventurer, who reaches back sorrowfully. Not gory. Red only: that person's eyes.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```
