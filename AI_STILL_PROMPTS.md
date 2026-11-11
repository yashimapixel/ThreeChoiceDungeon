# 画像生成プロンプト集（20枚）

画像生成AI（ChatGPT や Codex など）には**元画像を描くことだけ**を頼み、減色とピクセルアート化はこちら（Claude）で行います。

> 2026-11-11：全プロンプトに「アニメ調にしない」を追加しました。バッチ1の5枚はこの追加の前に生成したものです。

> 全プロンプトに「アニメ調にしない」（Not anime or manga style ...）を入れてあります。

## 使い方

1. **1回の依頼で1枚だけ**生成してもらいます（新しいスレッドで、下の依頼文をそのまま貼る）。
2. できた画像をダウンロードし、ファイル名を `<name>.png`（例：`e008.png`）にします。**必ず PNG のまま保存してください（JPEG は画質が落ちるので厳禁）。**
3. 何枚かたまったら Claude に渡してください。6色への減色・336×200 への縮小・比較表づくりはこちらで行います。

依頼文（毎回これを最初に付ける）：

```
次のプロンプトで、横長（1536×1024）の画像を1枚だけ生成してください。説明やコードは不要です。画像だけ出してください。
```

---

## バッチ1（生成済み。作り直すかどうかは下の注記を参照）

### e008：迷子の少女

保存名：`e008.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a dark stone corridor, the ghost girl stands facing the wall, crying with her hands over her face. Her small body glows faintly white against the darkness, and the floor beneath her shows no shadow at all. Red only: the tiny crest pendant on her chest.

Characters (keep them consistent across images):
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
```

### g025：骨の門番（地下25階の門番）

保存名：`g025.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A colossal gate built entirely from countless human bones and skulls fills the whole width of a crypt. Skeletal hands reach out from the gate. At its centre a huge skull with glowing eye sockets looks down. the hooded adventurer is tiny at the bottom centre, seen from behind. Red only: the glowing eye sockets of the skulls.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### n02：隔離塔（作り直し：扉の印が現代のバイオハザードマークになったため、プロンプトを修正済み）

保存名：`n02.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: An old round stone tower that has sunk into the ground and leans to one side, standing alone in darkness. A small iron-barred window. A crude medieval plague cross is daubed in paint on its heavy wooden door (a simple rough cross, NOT a biohazard symbol, nothing modern), which stands half open, and inside a small empty bed is visible. No people. Red only: the painted cross on the door.
```

### e020_0_r：黒い犬→干し肉をやる：犬が隣を歩く

保存名：`e020_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Side view: the hooded adventurer walks to the right down a dark corridor with a thin black dog trotting at their side. The dog has one glowing eye. Red only: the dog's one eye.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### g100_0_r：迷宮の底→真の結末：母と娘の再会

保存名：`g100_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: In a column of soft light rising out of darkness, the queen kneels and embraces the ghost girl tightly; both have their eyes closed, peaceful. Behind them the ghost knight kneels with his sword planted, head bowed. In the background the giant eye is cracked and crumbling into dust. Red only: the cracks of the broken eye.

Characters (keep them consistent across images):
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
- the queen: a woman with long loose hair in a long pale gown
```

---

## バッチ2

### title：タイトル画面：深淵へ続く螺旋階段と赤い眼

保存名：`title.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A worn stone staircase spiralling down into a bottomless black abyss, seen from above at a steep angle; the steps fade into darkness. Far above the depth, a single huge eye opens in the dark. No people. Red only: the iris of the eye and its faint glow.
```

### e001：錆びた扉

保存名：`e001.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the hooded adventurer stands small at the left of a narrow stone corridor, facing a massive iron door at the dead end. The door is heavy, studded, slightly ajar with a thin black gap. Light from the adventurer's lantern. Red only: the rust streaks on the door.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### e023：甲冑の亡霊

保存名：`e023.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the ghost knight stands motionless in a ruined corridor with his head bowed, both hands resting on the pommel of a longsword planted point-down. the hooded adventurer is small in the left foreground, seen from behind, looking at him. Red only: the crown crest on the knight's tabard.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```

### e027：子守唄（ひとりでに揺れる揺りかご）

保存名：`e027.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A dark, empty stone room. In the corner an ornate wooden baby cradle rocks by itself, surrounded by a faint pale glow. The wood grain of the cradle looks subtly alive, like veins. A crown crest is carved on the headboard. Nobody is there. Red only: the carved crest on the cradle.
```

### gameover：ゲームオーバー：髑髏

保存名：`gameover.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A large human skull lying on a dark crypt floor, lit from above, dust and darkness all around, blood dripping from the jaw. Red only: two tiny lights deep in the eye sockets and the dripping blood.
```

---

## バッチ3

### g075：深淵の竜（地下75階の門番）

保存名：`g075.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A huge dragon made of bones and rotting flesh spreads its tattered wings over a bottomless chasm. the hooded adventurer is tiny on a rock ledge at the bottom, facing it. Red only: the fire burning in the dragon's eye sockets and a faint glow inside its ribcage.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### e096：あの夜の部屋（記憶の病室）

保存名：`e096.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A small quiet sickroom remembered from long ago: a child's white bed with rumpled sheets, a single flower in a vase on the windowsill, and a wooden chair beside the pillow. The window shows only pure black nothingness. Soft light falls only on the bed. No people. Red only: the flower.
```

### g100：迷宮の底（地下100階）

保存名：`g100.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: The bottom of the labyrinth: a gigantic single eye opens at the centre of the darkness. The surrounding walls are made of organic flesh, and set into the flesh above is one large serene face of a sleeping woman with her eyes closed. the hooded adventurer stands small at the bottom centre, seen from behind. Red only: the iris of the giant eye and the veins around it.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### e001_2_ng：錆びた扉→耳を当てる（失敗）：扉の向こうから「開けて」

保存名：`e001_2_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Close-up: the hooded adventurer had pressed an ear to a rusted iron door and is now recoiling in fear. From the thin black gap of the door, long pale thin fingers are reaching out of the darkness. Red only: the rust on the door.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### e011_1_ng：落とし穴→跳ぶ（失敗）：縁にしがみつく

保存名：`e011_1_ng.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the hooded adventurer clings to the crumbling edge of a black pit in a stone corridor floor, hanging by the hands with legs dangling over bottomless darkness, small pieces of stone falling. Red only: blood on one knee.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

---

## バッチ4

### e008_0_r：迷子の少女→手を差し伸べる：少女が手を握る

保存名：`e008_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the hooded adventurer kneels in a dark corridor holding the small hand of the ghost girl, who looks up at the adventurer. A gentle faint glow surrounds the girl. Red only: the tiny crest pendant on her chest.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
```

### e037_0_r：渡し守→金貨を払う：舟で地底湖を渡る

保存名：`e037_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A small wooden boat on a still black underground lake. A tall hooded ferryman stands at the stern rowing with a long oar, and the hooded adventurer sits in the boat. Thin mist on the water, distant cave walls. Red only: a small lantern hanging at the bow.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### e046_0_r：少女の墓→花を手向ける：少女が光に溶ける

保存名：`e046_0_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: A small crude gravestone carved with a crown crest in a dark crypt. the ghost girl stands before it holding a small flower to her chest and smiling, her body dissolving upward into motes of light. the hooded adventurer kneels nearby. Red only: the flower.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
```

### n02_1_r：隔離塔→落書きを読む

保存名：`n02_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: Inside a cramped round stone tower cell, the walls are covered with a small child's simple chalk drawings: a mother and child holding hands, a house, a moon, stars (no letters, no writing). A small empty bed. the hooded adventurer holds up a lantern, looking at the wall. Red only: the drawing of the mother and child.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
```

### g075_1_r：深淵の竜→騎士を呼ぶ：騎士の亡霊が竜に斬りかかる

保存名：`g075_1_r.png`

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).

Scene: the ghost knight leaps from beside the adventurer at a huge skeletal dragon above a chasm, sword raised high, glowing ghostly white. the hooded adventurer stands in the foreground watching. Red only: the fire in the dragon's eye sockets.

Characters (keep them consistent across images):
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
```
