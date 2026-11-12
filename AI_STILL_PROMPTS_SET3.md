# Codex 向け作業指示：画像50枚の一括生成（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の50枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e011.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e011」のように1枚1行の短い報告だけにする。
9. 50枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_set3.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（50枚）

| # | name | 内容 |
| --- | --- | --- |
| 1 | `e011` | 落とし穴 |
| 2 | `e014` | 這い寄る粘液 |
| 3 | `e015` | 祈る修道士 |
| 4 | `e016` | 崩れた階段 |
| 5 | `e017` | 壁の顔 |
| 6 | `e018` | 光るキノコ |
| 7 | `e019` | 吊るされた檻 |
| 8 | `e022` | 地下水脈 |
| 9 | `e024` | コウモリの嵐 |
| 10 | `e025` | 骸骨の賭博師 |
| 11 | `e026` | 赤い扉 |
| 12 | `e028` | 泣く石像 |
| 13 | `e029` | 盗賊の待ち伏せ |
| 14 | `e030` | 水晶玉 |
| 15 | `e032` | 岩に刺さった剣 |
| 16 | `n06` | 迷宮の中の街角 |
| 17 | `e033` | 納骨堂 |
| 18 | `e034` | さまよう亡霊 |
| 19 | `e035` | 釘打たれた棺 |
| 20 | `e036` | 水没した回廊 |
| 21 | `e038` | 屍喰らい |
| 22 | `e040` | 囁く人形 |
| 23 | `e041` | 肖像画の回廊 |
| 24 | `e042` | 朽ちた吊り橋 |
| 25 | `e043` | 錬金術師の工房 |
| 26 | `e044` | 死者の宴 |
| 27 | `e047` | 鎖の囚人 |
| 28 | `e048` | 牢番 |
| 29 | `e049` | 蝋燭の道 |
| 30 | `e050` | 闇の中の目 |
| 31 | `e051` | 地図職人の亡骸 |
| 32 | `e052` | 禁書庫 |
| 33 | `e053` | 湖の歌声 |
| 34 | `e054` | 死神の賭け |
| 35 | `e055` | 蛆の床 |
| 36 | `e056` | メモの続き |
| 37 | `e057` | 喰らう扉 |
| 38 | `e058` | 胞子の森 |
| 39 | `e059` | 地下都市の大通り |
| 40 | `e061` | 蛾の女王 |
| 41 | `e062` | 菌糸の人 |
| 42 | `e063` | 逆さ時計の塔 |
| 43 | `e064` | 黒い聖堂 |
| 44 | `e065` | 双子の扉 |
| 45 | `e066` | 竜の骨 |
| 46 | `e067` | 影の自分 |
| 47 | `e068` | 仮面の商人 |
| 48 | `e069` | 脈打つ卵 |
| 49 | `e070` | 亡者の行進 |
| 50 | `e071` | 魔女の再訪 |

---

### 1. e011：落とし穴

保存名：`generated/e011.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A stone corridor where the floor has collapsed into a wide black pit with no visible bottom. The far edge looks reachable with a running jump. the hooded adventurer stands at the near edge, looking across. Red only: a faint red glow deep down in the pit.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 2. e014：這い寄る粘液

保存名：`generated/e014.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Black slime drips from the cave ceiling and gathers into one glistening, oozing mass on the floor. Half-dissolved bones and pieces of armour float inside it. the hooded adventurer steps back at the left. Red only: a glowing core inside the slime.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 3. e015：祈る修道士

保存名：`generated/e015.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A collapsed chapel with broken pews. A monk in a ragged hooded habit kneels in prayer before a cracked altar and has just turned his head toward the viewer; his eyes are clouded milky white. Large in the frame. Red only: a small votive candle flame on the altar.
```

### 4. e016：崩れた階段

保存名：`generated/e016.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A stone staircase leading down breaks off halfway, collapsed into rubble. Through the gaps between the fallen blocks an even deeper darkness is visible. the hooded adventurer stands at the top of the remaining steps. Red only: a faint red glow far below in the gaps.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 5. e017：壁の顔

保存名：`generated/e017.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A human face pushes out of a stone wall, as if part of the stone itself; not a carving. Its eyelids twitch and its lips move, pleading. the hooded adventurer holds up the lantern toward it. The face is large in the frame. Red only: a thin trickle of blood from the corner of the face's mouth.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 6. e018：光るキノコ

保存名：`generated/e018.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A cave floor covered with a cluster of glowing pale mushrooms of many sizes, their light the brightest thing in the scene, with sweet-looking spores drifting up. the hooded adventurer crouches nearby, reaching toward one. Red only: the spotted cap of the single largest mushroom.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 7. e019：吊るされた檻

保存名：`generated/e019.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: An iron cage hangs from the ceiling of a dark stone room on a heavy chain. Inside, a gaunt, starving man crouches, reaching a bony hand through the bars toward the viewer. the hooded adventurer stands below. Red only: the rusted padlock on the cage door.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 8. e022：地下水脈

保存名：`generated/e022.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Cold water flows from a crack in the rock and forms a small clear pool in a cave. On the bottom of the pool something glows white. the hooded adventurer kneels at the edge, looking in. Red only: a small red stone glinting next to the white glow at the bottom of the pool.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 9. e024：コウモリの嵐

保存名：`generated/e024.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A cave ceiling covered by thousands of bats; at the moment one takes flight, the whole swarm erupts into the air like a storm of black wings. the hooded adventurer shields their face below. Red only: the eyes of the nearest bats, a few bold dots.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 10. e025：骸骨の賭博師

保存名：`generated/e025.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Across a small wooden table, a grinning skeleton in a battered tricorn hat throws dice from a bony hand, coins piled before it, inviting the viewer to play. A single candle lights the table. Large in the frame. Red only: the dice, mid-roll.
```

### 11. e026：赤い扉

保存名：`generated/e026.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A long grey stone corridor, entirely grey, and in its wall a single door painted a vivid, unnaturally bright red. The door seems to pulse slightly. the hooded adventurer stands before it, hand raised to touch it. Red only: the door; this is the one scene where the red element may be large.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 12. e028：泣く石像

保存名：`generated/e028.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A stone statue of a goddess with a serene face in a ruined shrine; tears flow continuously from both of her eyes and run down her cheeks and robes onto a plinth. The plinth has a carved inscription shown only as worn, illegible marks. Large in the frame. Red only: the tears running from her eyes.
```

### 13. e029：盗賊の待ち伏せ

保存名：`generated/e029.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: From behind a boulder in a cave, a rough bandit with a scarf over the lower half of his face steps out, pointing a dagger at the viewer, with a menacing stance. Large in the frame. Red only: the scarf over his face.
```

### 14. e030：水晶玉

保存名：`generated/e030.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A crystal ball glows faintly on a stone pedestal in a dark room. Inside the ball a tiny image can be seen: a hooded figure lying dead on the ground. the hooded adventurer leans over it, the glow lighting the edge of the hood. Red only: a small pool of blood beside the tiny dead figure inside the ball.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 15. e032：岩に刺さった剣

保存名：`generated/e032.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In the centre of a room, a shining silver sword is stuck in a large rock, lit from above. Around the rock lie several skeletons, still reaching toward the sword's hilt. No living people. Red only: a gem in the sword's pommel.
```

### 16. n06：迷宮の中の街角

保存名：`generated/n06.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In the middle of a stone dungeon passage there is suddenly a city street corner: cobblestones, an iron street lamp and shuttered windows of a royal capital, as if cut out and placed here. The edges of the street fade into dungeon rock. On a wall there is a scrawled message shown only as illegible scratches. the hooded adventurer stands under the street lamp. Red only: the flame of the street lamp.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 17. e033：納骨堂

保存名：`generated/e033.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: An ossuary whose walls are stacked from floor to ceiling with skulls, every one with its jaw wide open as if screaming. A narrow passage runs between them. the hooded adventurer walks through, small. Red only: the eye sockets of a single skull in the centre glow faintly red.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 18. e034：さまよう亡霊

保存名：`generated/e034.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A pale, drifting ghost in a long tattered shroud wanders down a crypt corridor. It has no face, only a smooth blank surface where the face should be, and it tilts its head slowly toward the viewer. Large in the frame. Red only: a red ribbon tied around the ghost's wrist.
```

### 19. e035：釘打たれた棺

保存名：`generated/e035.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A black coffin on a stone slab in a crypt, nailed shut with dozens of nails driven in at all angles. Scratch marks are visible at its edges, as if from inside. On its lid a warning is smeared in blood, shown only as a rough illegible smear, not letters. Red only: the blood smear on the lid.
```

### 20. e036：水没した回廊

保存名：`generated/e036.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A vaulted corridor flooded with black water up to chest height. Just beneath the surface a long, thin, serpent-like shape glides past. the hooded adventurer wades through, lantern held high. Red only: a single eye of the shape under the water.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 21. e038：屍喰らい

保存名：`generated/e038.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A thin, emaciated ghoul crouches on all fours in a crypt, devouring a carcass, and slowly turns its head to grin at the viewer with a dripping mouth. Grotesque and realistic. Large in the frame. Red only: the blood on its mouth and hands.
```

### 22. e040：囁く人形

保存名：`generated/e040.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A porcelain doll in an old-fashioned dress sits on a small wooden chair in an empty dark room, its head turned toward the viewer, cracked face, glass eyes. Lit by a single beam. Large in the frame. Red only: the doll's painted lips.
```

### 23. e041：肖像画の回廊

保存名：`generated/e041.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A long gallery lined with portraits in ornate frames. At the end hangs a final portrait showing a hooded figure, the same as the adventurer but very old and withered. the hooded adventurer stands before it, looking up. Red only: the eyes of the old figure in the last portrait.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 24. e042：朽ちた吊り橋

保存名：`generated/e042.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A rotting rope bridge spans a bottomless chasm, swaying though there is no wind, as if something below is shaking it. Pale hands reach up from the darkness below toward the planks. the hooded adventurer stands at the near end. Red only: a red cloth tied to the near post of the bridge.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 25. e043：錬金術師の工房

保存名：`generated/e043.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: An abandoned alchemist's workshop: shelves crowded with bottles of many shapes, glass tubes and a cold furnace. On the empty desk stand three bottles side by side next to a note whose writing is only illegible scratches. No people. Red only: the liquid in one of the three bottles on the desk.
```

### 26. e044：死者の宴

保存名：`generated/e044.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A long banquet table laden with a lavish feast, with skeletons seated in every chair, some raising goblets. One chair is empty and turned toward the viewer, with a name card on the plate in front of it (no readable letters). Candelabras. Red only: the wine in the goblets.
```

### 27. e047：鎖の囚人

保存名：`generated/e047.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Deep inside a dungeon cell, a man chained to the wall hangs his head; he has just raised his face, and where his eyes should be there are only empty dark hollows. Large in the frame. Red only: the rusted shackles on his wrists.
```

### 28. e048：牢番

保存名：`generated/e048.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A huge jailer patrols in front of iron bars, a giant ring of keys hanging from his belt. Above his shoulders there is nothing: he has no head. He carries a lantern. Large in the frame. Red only: the light of his lantern.
```

### 29. e049：蝋燭の道

保存名：`generated/e049.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A corridor lined on both sides with countless lit candles of all sizes stretching into the distance, wax dripping onto the floor. A few candles have just gone out, trailing smoke. the hooded adventurer walks down the middle, small. Red only: the flames of the candles nearest to the viewer.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 30. e050：闇の中の目

保存名：`generated/e050.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In the darkness at the back of a cave, a gigantic eye the size of a house has opened, its pupil slowly focusing on the viewer. the hooded adventurer stands tiny before it, seen from behind. Red only: the veins around the eye.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 31. e051：地図職人の亡骸

保存名：`generated/e051.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Between tall bookshelves, a dried, mummified man still gripping a pen sits slumped over a desk. On the desk lies an unfinished map of the labyrinth drawn as maze-like lines, no writing. No living people. Red only: the last line of the map, drawn in blood.
```

### 32. e052：禁書庫

保存名：`generated/e052.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A forbidden library where books are bound to the shelves with chains. One book thrashes violently against its chains, its cover made of stretched leather bearing a human face. the hooded adventurer watches from the aisle. Red only: the open mouth of the face on the book's cover.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 33. e053：湖の歌声

保存名：`generated/e053.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On a rock in the middle of an underground lake sits a beautiful pale woman in a long tattered dress with long wet hair, singing. Her reflection in the water is a drowned skeleton. the hooded adventurer stands on the shore, drawn toward her. Red only: her lips.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 34. e054：死神の賭け

保存名：`generated/e054.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A black-robed figure with a large scythe sits at a chessboard on a table in a crypt; under the hood is a skull. It gestures for the viewer to take the empty seat. Large in the frame. Red only: one chess piece, a king, on the board.
```

### 35. e055：蛆の床

保存名：`generated/e055.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A crypt floor entirely covered by a white, writhing carpet of maggots. Beneath them lies the vast carcass of some creature, its swollen belly slowly rising and falling as if still breathing. the hooded adventurer stands at the edge, small. Red only: a gash in the carcass.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 36. e056：メモの続き

保存名：`generated/e056.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: On a stone floor in a corridor lies another handwritten note, the writing shown only as illegible scratches, with a pressed flower tucked into it. Far down the corridor, in the darkness, a faint silhouette of armour can be seen. the hooded adventurer kneels to pick up the note. Red only: the pressed flower.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 37. e057：喰らう扉

保存名：`generated/e057.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A heavy wooden door where the handle should be, there is a wet, fleshy mouth with teeth, open and speaking, drool running down the wood. the hooded adventurer stands before it. Large in the frame. Red only: the tongue inside the mouth.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 38. e058：胞子の森

保存名：`generated/e058.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A forest of giant mushrooms reaching up to the cave ceiling, spores falling like snow and piling on the ground. Deep in the forest, dim shapes. the hooded adventurer walks in with a cloth over their mouth, small. Red only: one small glowing light deep in the forest.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 39. e059：地下都市の大通り

保存名：`generated/e059.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A grand avenue of an underground city lined with stone houses exactly like a royal capital, but drained of all colour. Every window is lit and shows the silhouette of a person moving, yet the doors stand open on empty rooms. the hooded adventurer walks down the middle of the avenue, small. Red only: one single lit window.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 40. e061：蛾の女王

保存名：`generated/e061.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A gigantic moth descends with its wings spread, glowing with a ghostly light. The patterns on its wings are made of countless human faces. the hooded adventurer stands below, small. Red only: the moth's two large eyes.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 41. e062：菌糸の人

保存名：`generated/e062.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A man with mushrooms growing all over his body walks slowly toward the viewer with open arms; thread-like fungal tendrils reach out from his chest. Grotesque and realistic. Large in the frame. Red only: the caps of a few mushrooms on his shoulders.
```

### 42. e063：逆さ時計の塔

保存名：`generated/e063.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The huge clock face of a ruined clock tower in an underground city, its hands turning the wrong way. Below the clock face is a small door with a carved inscription shown only as illegible marks. the hooded adventurer stands before the door, small. Red only: the hands of the clock.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 43. e064：黒い聖堂

保存名：`generated/e064.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A cathedral built of black obsidian. On the altar a black flame burns with a dark glow. The pews are empty of people, but shadows sit in them, praying. the hooded adventurer stands in the aisle. Red only: the outline of the black flame.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 44. e065：双子の扉

保存名：`generated/e065.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Two identical doors side by side in a corridor; one is carved with an open eye, the other with a closed eye (no words). In front of them stand pale twin children in identical old-fashioned clothes, speaking at the same time, with unsettling smiles. Large in the frame. Red only: the ribbons in the twins' hair.
```

### 45. e066：竜の骨

保存名：`generated/e066.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The enormous skeleton of a dragon lies across a whole cave. Inside its ribcage, a pile of treasure glints dully. Hot air shimmers up from gaps between the bones. the hooded adventurer stands small at the dragon's skull. Red only: a large gem at the top of the treasure pile.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 46. e067：影の自分

保存名：`generated/e067.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the hooded adventurer stands in a ruin, and their own shadow on the floor has risen up by itself into a standing black figure with the same shape, facing them. The shadow speaks. Both large in the frame. Red only: the shadow's two eyes.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 47. e068：仮面の商人

保存名：`generated/e068.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A merchant wearing many masks layered over one another runs a small stall in a ruined street; the stall is covered with hanging masks of human faces. The merchant leans forward to greet the viewer. Large in the frame. Red only: the mouth of the outermost mask.
```

### 48. e069：脈打つ卵

保存名：`generated/e069.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A huge egg wrapped in fungal threads, pulsing like a heart, in a fungus-filled cave. Cracks run across its shell, and something is knocking from inside. the hooded adventurer stands small before it. Red only: the light leaking out of the cracks.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### 49. e070：亡者の行進

保存名：`generated/e070.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A column of dead soldiers in rusted armour marches toward the viewer through a ruined street, none of them alive, empty helmets. The standard-bearer at the front has stopped and looks straight at the viewer. Large in the frame. Red only: the tattered banner carried by the standard-bearer.
```

### 50. e071：魔女の再訪

保存名：`generated/e071.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The same swamp witch as before, a hunched old crone with wild grey hair, stirs her bubbling cauldron in a cave hut and looks up with a knowing, crooked grin, as if remembering the viewer. Hourglasses and bones hang around her. Realistic and grotesque. Large in the frame. Red only: the sand in one hourglass.
```
