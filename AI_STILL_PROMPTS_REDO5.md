# Codex 向け作業指示：画像45枚の作り直し（統合レビュー反映）（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の45枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプトは、下の「プロンプトの組み立て方」どおりに組み立て、**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e031.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e031」のように1枚1行の短い報告だけにする。
9. 45枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_redo5.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（45枚）

| # | name | 内容 |
| --- | --- | --- |
| 1 | `e031` | 弔いの鐘 |
| 2 | `e062` | 菌糸の人 |
| 3 | `e068` | 仮面の商人 |
| 4 | `e070` | 亡者の行進 |
| 5 | `n03` | 騎士の告白 |
| 6 | `e039_0_r` | 沼の魔女→取引に応じる |
| 7 | `n03_1_ok` | 騎士の告白→「あなたのせいではない」（成功） |
| 8 | `e079_0_r` | 少女の記憶→歌を聞かせてもらう |
| 9 | `g050_1_r` | 都市の番人→王冠を掲げる |
| 10 | `e041_0_ok` | 肖像画の回廊→絵の自分に触れる（成功） |
| 11 | `e041_0_ng` | 肖像画の回廊→絵の自分に触れる（失敗） |
| 12 | `e041_1_r` | 肖像画の回廊→絵を切り裂く |
| 13 | `e007` | 古い祭壇 |
| 14 | `e004_0_ng` | 宝箱→迷わず開ける（失敗） |
| 15 | `e008_2_ng` | 迷子の少女→気づかないふりをする（失敗） |
| 16 | `e034_2_ok` | さまよう亡霊→気配を消してやり過ごす（成功） |
| 17 | `e043` | 錬金術師の工房 |
| 18 | `e052_1_r` | 禁書庫→本を焼き払う |
| 19 | `e069_1_ok` | 脈打つ卵→孵るのを見届ける（成功） |
| 20 | `e082_0_ng` | 心臓の間→結晶をえぐり取る（失敗） |
| 21 | `e093_1_r` | 最後の商人→心と引き換えに体を癒す |
| 22 | `n05_2_r` | 何度目の挑戦者→亡霊の装備をもらう |
| 23 | `x04_2_ok` | 子守唄の残響→旋律の源を探す（成功） |
| 24 | `x04_2_ng` | 子守唄の残響→旋律の源を探す（失敗） |
| 25 | `e025_1_ok` | 骸骨の賭博師→イカサマを見破る（成功） |
| 26 | `e015` | 祈る修道士 |
| 27 | `e037` | 渡し守 |
| 28 | `e020` | 黒い犬 |
| 29 | `e084` | 堕ちた天使 |
| 30 | `e084_0_ok` | 堕ちた天使→鎖を断つ（成功） |
| 31 | `e084_1_ng` | 堕ちた天使→天使の正体を見極める（失敗） |
| 32 | `e084_2_r` | 堕ちた天使→聖水を捧げる |
| 33 | `x06_0_ok` | 鏡の中の踏破者→「願いのために」と答える（成功） |
| 34 | `x06_0_ng` | 鏡の中の踏破者→「願いのために」と答える（失敗） |
| 35 | `e074_0_ok` | 血の泉→泉の血を飲む（成功） |
| 36 | `e074_0_ng` | 血の泉→泉の血を飲む（失敗） |
| 37 | `e074_1_r` | 血の泉→傷口を泉に浸す |
| 38 | `e074_2_r` | 血の泉→泉に聖水を注ぐ |
| 39 | `e093_0_r` | 最後の商人→体と引き換えに心を癒す |
| 40 | `e093_3_r` | 最後の商人→金貨で全てを少しずつ |
| 41 | `e027_0_ok` | 子守唄→一緒に歌う（成功） |
| 42 | `e027_0_ng` | 子守唄→一緒に歌う（失敗） |
| 43 | `e027_1_ng` | 子守唄→揺りかごを止める（失敗） |
| 44 | `e027_3_r` | 子守唄→耳を塞いで通り抜ける |
| 45 | `e055_1_r` | 蛆の床→火を放つ |

---

## プロンプトの組み立て方（全画像共通）

この指示書は長くなりすぎないよう、共通部分を一度だけ書いています。各画像のプロンプトは、次の順に**そのままつなげて**作ってください（書き換えない）。

1. 下の「共通の画風指定」の文章全体
2. 空行1つ
3. `Scene: ` に続けて、その画像の「Scene」の文章
4. その画像に「Characters」の指定がある場合だけ：空行1つ、`Characters (keep them consistent across images):` の1行、続けて指定された人物の行を、下の「登場人物」からそのまま1行ずつ

### 共通の画風指定

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Draw a royal crest only where the scene or a character description mentions one; it is always a simple crown shape. Do not add crowns or crests anywhere else. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).
```

### 登場人物

```
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
- the queen: a woman with long loose hair in a long pale gown
- the faceless peddler: a tall figure in a long dark hooded robe; under the hood there is no face at all, only darkness; long bony hands; carries a lantern and a huge pack of strange goods
- the black dog: a thin, gaunt dog with pitch-black fur; one eye glows red, the other is dark
```

---

### 1. e031：弔いの鐘

保存名：`generated/e031.png`

- Scene: A ruined bell tower. A huge bell hangs from a cracked wooden beam, and countless names are engraved all around its rim, shown only as rows of tiny scratches, never as readable letters. the hooded adventurer stands below, looking up at it. Red only: a red glow on one small spot of the bell's rim, a glowing smudge with no letters or symbols in it. Absolutely no writing, letters or alphabet anywhere in the image. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere.
- Characters: the hooded adventurer

### 2. e062：菌糸の人

保存名：`generated/e062.png`

- Scene: A man with mushrooms growing all over his body walks slowly toward the viewer with open arms; thread-like fungal tendrils reach out from his chest. Grotesque and realistic. Large in the frame. Red only: the caps of a few mushrooms on his shoulders. He walks through a damp fungal cave. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere.

### 3. e068：仮面の商人

保存名：`generated/e068.png`

- Scene: A merchant wearing many masks layered over one another runs a small stall in a ruined street; the stall is covered with hanging masks of human faces. The merchant leans forward to greet the viewer. Large in the frame. Red only: the mouth of the outermost mask. The ruined street lies inside a vast cavern. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere.

### 4. e070：亡者の行進

保存名：`generated/e070.png`

- Scene: A column of dead soldiers in rusted armour marches toward the viewer through a ruined street, none of them alive, empty helmets. The standard-bearer at the front has stopped and looks straight at the viewer. Large in the frame. Red only: the tattered banner carried by the standard-bearer. The ruined street lies inside a vast cavern. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere.

### 5. n03：騎士の告白

保存名：`generated/n03.png`

- Scene: In a corner of a ruin, the ghost knight has taken off his helmet and holds it in both hands against his chest. Above the neck of the armour there is no head at all, only empty darkness. Side view, quiet and sorrowful, large in the frame. Red only: the crown crest on the tabard. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere.
- Characters: the ghost knight

### 6. e039_0_r：沼の魔女→取引に応じる

保存名：`generated/e039_0_r.png`

- Scene: Inside a witch's hut built into a cave, rock walls behind, a swamp witch presses a glowing finger to the neck of the hooded adventurer, burning a mark. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: the mark on the neck.
- Characters: the hooded adventurer

### 7. n03_1_ok：騎士の告白→「あなたのせいではない」（成功）

保存名：`generated/n03_1_ok.png`

- Scene: the ghost knight, his helmet at his side, sits on a fallen stone in a ruin with his head lowered, and the hooded adventurer sits beside him in silence. A long, quiet moment. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 8. e079_0_r：少女の記憶→歌を聞かせてもらう

保存名：`generated/e079_0_r.png`

- Scene: the ghost girl sits on a stone and sings softly with her eyes closed; around her, faint pale ribbons of melody drift up into the darkness and are joined by another melody coming from far away. the hooded adventurer sits nearby, listening. They sit in a ruined underground street. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 9. g050_1_r：都市の番人→王冠を掲げる

保存名：`generated/g050_1_r.png`

- Scene: Inside a vast cavern, before the broken gate of a ruined underground city, the colossal stone-and-iron guardian kneels and bows its head before the hooded adventurer, who holds a crown high above their head. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: the furnace core in the guardian's chest, dimming.
- Characters: the hooded adventurer

### 10. e041_0_ok：肖像画の回廊→絵の自分に触れる（成功）

保存名：`generated/e041_0_ok.png`

- Scene: In a gallery of portraits, the hooded adventurer touches the last portrait, which shows the same hooded adventurer grown very old and withered, the face still hidden in the shadow of the hood. The painted old figure reaches out from the canvas and a soft glow flows into the adventurer's hand. Red only: the two eyes of the painted figure.
- Characters: the hooded adventurer

### 11. e041_0_ng：肖像画の回廊→絵の自分に触れる（失敗）

保存名：`generated/e041_0_ng.png`

- Scene: the hooded adventurer touches the last portrait in a gallery, which shows the same hooded adventurer grown very old, the face hidden in the shadow of the hood. The adventurer's own hand withers and ages where it touches the canvas. Red only: the two eyes of the painted figure.
- Characters: the hooded adventurer

### 12. e041_1_r：肖像画の回廊→絵を切り裂く

保存名：`generated/e041_1_r.png`

- Scene: the hooded adventurer slashes the last portrait in a gallery with a short sword; the portrait shows the same hooded adventurer grown very old, the face hidden in the shadow of the hood, and the canvas splits open as if screaming. Red only: the gash in the canvas.
- Characters: the hooded adventurer

### 13. e007：古い祭壇

保存名：`generated/e007.png`

- Scene: Moss-covered pillars surround an old black stone altar in a ruined underground shrine, with a few candle stubs. The altar top is covered with layered, old, dried dark stains: overlapping dark rings and a few old streaks that stop at the edge. Nothing is wet or dripping. No people. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: the dried stains on the altar top, dark red, old and dry.

### 14. e004_0_ng：宝箱→迷わず開ける（失敗）

保存名：`generated/e004_0_ng.png`

- Scene: A treasure chest has split open into a mimic with rows of fangs and a long tongue. the hooded adventurer flees from it, clutching a torn sleeve on one forearm where the mimic has just bitten. Red only: the mimic's tongue.
- Characters: the hooded adventurer

### 15. e008_2_ng：迷子の少女→気づかないふりをする（失敗）

保存名：`generated/e008_2_ng.png`

- Scene: In a dark stone corridor, the hooded adventurer has just walked one step past the ghost girl. The girl's body and bare feet still face away down the corridor, but her head alone has turned all the way around to face the adventurer, her face hidden by her dark hair. Unsettling. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 16. e034_2_ok：さまよう亡霊→気配を消してやり過ごす（成功）

保存名：`generated/e034_2_ok.png`

- Scene: In a crypt corridor, the hooded adventurer hides motionless behind a stone pillar, holding their breath, while a faceless ghost in a tattered shroud drifts past just beside them; there is a clear gap between the two, they do not touch. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 17. e043：錬金術師の工房

保存名：`generated/e043.png`

- Scene: An abandoned alchemist's workshop: shelves crowded with bottles, glass tubes and a cold furnace. On the empty desk stand three clearly different bottles side by side next to a note whose writing is only illegible scratches: a round milky-white flask, a square bottle of red liquid in the middle, and a tall slender bottle of black liquid with a bright rim. No people. Red only: the liquid in the square middle bottle.

### 18. e052_1_r：禁書庫→本を焼き払う

保存名：`generated/e052_1_r.png`

- Scene: In a forbidden library, the chained book with a human face has burned down to glowing embers and ash; in front of the crumbled cover lies one bright metal clasp, and the hooded adventurer reaches down toward it, torch in the other hand. Red only: the last embers.
- Characters: the hooded adventurer

### 19. e069_1_ok：脈打つ卵→孵るのを見届ける（成功）

保存名：`generated/e069_1_ok.png`

- Scene: A tiny white dragon hatchling sits beside a broken fungal egg. In the open palm of the hooded adventurer lies a single white scale tied with a small red cord, made into a little charm. Red only: the red cord.
- Characters: the hooded adventurer

### 20. e082_0_ng：心臓の間→結晶をえぐり取る（失敗）

保存名：`generated/e082_0_ng.png`

- Scene: In a chamber of flesh, a gigantic heart convulses. A glowing crystal is still half-embedded in the folds of the heart, and a flood of dark fluid pushes back the outstretched hand of the hooded adventurer, sweeping them away. Red only: the glowing crystal in the heart.
- Characters: the hooded adventurer

### 21. e093_1_r：最後の商人→心と引き換えに体を癒す

保存名：`generated/e093_1_r.png`

- Scene: In a black void, the hooded adventurer hands an empty potion bottle back to the faceless peddler, standing straight and strong again. The peddler holds the lantern with the red flame; the adventurer's own lantern shows a plain white light. Red only: the small flame inside the peddler's lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 22. n05_2_r：何度目の挑戦者→亡霊の装備をもらう

保存名：`generated/n05_2_r.png`

- Scene: The fading ghost of an old adventurer, a red scarf on his shoulders, hands the hooded adventurer a coiled rope with the neck of a corked potion bottle poking out from the centre of the coil. Red only: the ghost's scarf.
- Characters: the hooded adventurer

### 23. x04_2_ok：子守唄の残響→旋律の源を探す（成功）

保存名：`generated/x04_2_ok.png`

- Scene: In a black void, the hooded adventurer finds a small cradle at the source of a melody; by its pillow lies a small open drawstring purse with a few coins peeking out of its mouth. Red only: the crown crest carved on the cradle.
- Characters: the hooded adventurer

### 24. x04_2_ng：子守唄の残響→旋律の源を探す（失敗）

保存名：`generated/x04_2_ng.png`

- Scene: the hooded adventurer searches a black void; thin pale ribbons of light drift in from every direction, break apart and fade into separate patches of darkness, impossible to follow. No musical notes, no staff lines. Red only: one thin ribbon.
- Characters: the hooded adventurer

### 25. e025_1_ok：骸骨の賭博師→イカサマを見破る（成功）

保存名：`generated/e025_1_ok.png`

- Scene: the hooded adventurer holds up one large die toward the viewer; all three visible faces clearly show six pips in two rows of three. Across the table, the skeleton gambler in a tricorn hat laughs and tosses a coin. Red only: the die.
- Characters: the hooded adventurer

### 26. e015：祈る修道士

保存名：`generated/e015.png`

- Scene: A collapsed underground chapel with broken pews. A bald, elderly monk with a short grey beard and milky white clouded eyes, in a ragged robe with the hood down, kneels in prayer before a cracked altar and has just turned his head toward the viewer. Large in the frame. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: a small votive candle flame on the altar.

### 27. e037：渡し守

保存名：`generated/e037.png`

- Scene: The shore of a black underground lake inside a vast cavern. A tall ferryman in a long hooded robe stands beside a small wooden boat; under his hood there is no face at all, only darkness. He holds a long oar and holds out an open bony hand toward the viewer to ask for payment. Mist on the water. Enclosed underground: a rock or stone ceiling overhead; no sky, no moon, no stars and no windows to the outside anywhere. Red only: a small lantern hanging at the boat's bow.

### 28. e020：黒い犬

保存名：`generated/e020.png`

- Scene: the black dog emerges from the darkness of a stone corridor and stands still, staring at the viewer without growling. It is the size of an ordinary medium dog, thin and gaunt, not a large hound. Red only: the dog's one glowing eye.
- Characters: the black dog

### 29. e084：堕ちた天使

保存名：`generated/e084.png`

- Scene: A fallen angel with broken wings floats in the air, bound by chains. Its face is split down the middle: the left half beautiful and serene, the right half clearly rotted away to bare skull and torn flesh, plainly visible. It looks down at the viewer. Large in the frame. Red only: the eye on the rotted half.

### 30. e084_0_ok：堕ちた天使→鎖を断つ（成功）

保存名：`generated/e084_0_ok.png`

- Scene: A freed fallen angel, chains broken, wraps its one remaining wing around the hooded adventurer; its face is split down the middle, one half beautiful, the other half clearly rotted to bare skull. Red only: the eye on the rotted half.
- Characters: the hooded adventurer

### 31. e084_1_ng：堕ちた天使→天使の正体を見極める（失敗）

保存名：`generated/e084_1_ng.png`

- Scene: the hooded adventurer gazes enchanted at the beautiful left half of a fallen angel's face while a glowing wisp is drawn from their chest; the right half of the angel's face is clearly rotted to bare skull. Red only: the eye on the rotted half.
- Characters: the hooded adventurer

### 32. e084_2_r：堕ちた天使→聖水を捧げる

保存名：`generated/e084_2_r.png`

- Scene: A fallen angel whose face is half beautiful and half rotted to bare skull dissolves into light as the hooded adventurer offers holy water. Red only: the eye on the rotted half, fading.
- Characters: the hooded adventurer

### 33. x06_0_ok：鏡の中の踏破者→「願いのために」と答える（成功）

保存名：`generated/x06_0_ok.png`

- Scene: In a maze of mirrors, the reflection in a large mirror is the same hooded adventurer as a battle-worn veteran, the face completely hidden in the black shadow of the hood; it steps aside to open a path for the hooded adventurer. Red only: the reflection's two eyes.
- Characters: the hooded adventurer

### 34. x06_0_ng：鏡の中の踏破者→「願いのために」と答える（失敗）

保存名：`generated/x06_0_ng.png`

- Scene: the hooded adventurer stands silent before a large mirror; the reflection is the same hooded adventurer as a battle-worn veteran, the face completely hidden in the black shadow of the hood, waiting for an answer. Red only: the reflection's two eyes.
- Characters: the hooded adventurer

### 35. e074_0_ok：血の泉→泉の血を飲む（成功）

保存名：`generated/e074_0_ok.png`

- Scene: the hooded adventurer drinks blood with cupped hands from a round stone basin fountain on a low pedestal in the centre of a great underground hall, with a short central spout welling up dark blood into the basin (no statue, no lion, no carved figure); wounds on their arms close. Red only: the blood.
- Characters: the hooded adventurer

### 36. e074_0_ng：血の泉→泉の血を飲む（失敗）

保存名：`generated/e074_0_ng.png`

- Scene: the hooded adventurer drinks from a round stone basin fountain on a low pedestal in the centre of a great underground hall, with a short central spout welling up dark blood into the basin (no statue, no lion, no carved figure), eyes hungry. Red only: the blood.
- Characters: the hooded adventurer

### 37. e074_1_r：血の泉→傷口を泉に浸す

保存名：`generated/e074_1_r.png`

- Scene: the hooded adventurer kneels at the rim of a round stone basin fountain on a low pedestal in the centre of a great underground hall, with a short central spout welling up dark blood into the basin (no statue, no lion, no carved figure) and dips one forearm into it; thin red threads curl from the arm into the pool, as if the fountain is drinking. Red only: the blood in the basin.
- Characters: the hooded adventurer

### 38. e074_2_r：血の泉→泉に聖水を注ぐ

保存名：`generated/e074_2_r.png`

- Scene: The same round stone basin fountain on a low pedestal in a great underground hall (no statue, no lion) now runs with clear water after holy water is poured in; the hooded adventurer drinks from it. Red only: a last drop of blood on the rim.
- Characters: the hooded adventurer

### 39. e093_0_r：最後の商人→体と引き換えに心を癒す

保存名：`generated/e093_0_r.png`

- Scene: the faceless peddler nods contentedly to the hooded adventurer in a black void as a glowing wisp flows from the adventurer's body. The peddler holds the lantern with the red flame; the adventurer's own lantern shows a plain white light. Red only: the small flame inside the peddler's lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 40. e093_3_r：最後の商人→金貨で全てを少しずつ

保存名：`generated/e093_3_r.png`

- Scene: the faceless peddler accepts coins from the hooded adventurer with a shrug in a black void. The peddler holds the lantern with the red flame; the adventurer's own lantern shows a plain white light. Red only: the small flame inside the peddler's lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 41. e027_0_ok：子守唄→一緒に歌う（成功）

保存名：`generated/e027_0_ok.png`

- Scene: In a dark stone room with no windows, the hooded adventurer stands by an ornate wooden cradle that has stopped rocking, a calm soft light filling the room. A simple crown crest is carved on the cradle's headboard. Red only: the crown crest.
- Characters: the hooded adventurer

### 42. e027_0_ng：子守唄→一緒に歌う（失敗）

保存名：`generated/e027_0_ng.png`

- Scene: In a dark stone room with no windows, the hooded adventurer backs away from an ornate wooden cradle as a pale small shape stirs inside it, crying. A simple crown crest is carved on the headboard. Red only: the crown crest.
- Characters: the hooded adventurer

### 43. e027_1_ng：子守唄→揺りかごを止める（失敗）

保存名：`generated/e027_1_ng.png`

- Scene: In a dark stone room with no windows, a small pale ghostly hand grips the wrist of the hooded adventurer as they try to stop a rocking ornate cradle. A simple crown crest is carved on the headboard. Red only: the crown crest.
- Characters: the hooded adventurer

### 44. e027_3_r：子守唄→耳を塞いで通り抜ける

保存名：`generated/e027_3_r.png`

- Scene: the hooded adventurer walks through a dark stone room with no windows, hands pressed over their ears, while an ornate cradle rocks by itself behind them. A simple crown crest is carved on the headboard. Red only: the crown crest.
- Characters: the hooded adventurer

### 45. e055_1_r：蛆の床→火を放つ

保存名：`generated/e055_1_r.png`

- Scene: In an underground crypt with a stone vault overhead, a floor of maggots and a vast carcass burn; the hooded adventurer holds up a huge fang from the ashes. Red only: the flames.
- Characters: the hooded adventurer
