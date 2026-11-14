# Codex 向け作業指示：画像200枚の一括生成（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の200枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプトは、下の「プロンプトの組み立て方」どおりに組み立て、**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e001_0_r.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e001_0_r」のように1枚1行の短い報告だけにする。
9. 200枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_set5.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（200枚）

| # | name | 内容 |
| --- | --- | --- |
| 1 | `e001_0_r` | 錆びた扉→錆びた鍵で開ける |
| 2 | `e001_1_ok` | 錆びた扉→体当たりで押し開ける（成功） |
| 3 | `e001_1_ng` | 錆びた扉→体当たりで押し開ける（失敗） |
| 4 | `e001_2_ok` | 錆びた扉→耳を当てて様子をうかがう（成功） |
| 5 | `e001_3_r` | 錆びた扉→扉には触れず迂回する |
| 6 | `e002_0_r` | ネズミの群れ→たいまつを振りかざす |
| 7 | `e002_1_ok` | ネズミの群れ→踏みつけて突っ切る（成功） |
| 8 | `e002_1_ng` | ネズミの群れ→踏みつけて突っ切る（失敗） |
| 9 | `e002_2_ok` | ネズミの群れ→息を殺して通り過ぎるのを待つ（成功） |
| 10 | `e002_2_ng` | ネズミの群れ→息を殺して通り過ぎるのを待つ（失敗） |
| 11 | `e002_3_r` | ネズミの群れ→携帯食を投げて気を逸らす |
| 12 | `e003_0_ok` | 先客の亡骸→荷物を漁る（成功） |
| 13 | `e003_0_ng` | 先客の亡骸→荷物を漁る（失敗） |
| 14 | `e003_1_r` | 先客の亡骸→指し示す先の床を調べる |
| 15 | `e003_2_r` | 先客の亡骸→祈りを捧げて弔う |
| 16 | `e004_0_ok` | 宝箱→迷わず開ける（成功） |
| 17 | `e004_0_ng` | 宝箱→迷わず開ける（失敗） |
| 18 | `e004_1_ok` | 宝箱→剣で叩いてから開ける（成功） |
| 19 | `e004_1_ng` | 宝箱→剣で叩いてから開ける（失敗） |
| 20 | `e004_2_r` | 宝箱→触らずに立ち去る |
| 21 | `e005_0_ok` | 囁く井戸→金貨を一枚投げ入れる（成功） |
| 22 | `e005_0_ng` | 囁く井戸→金貨を一枚投げ入れる（失敗） |
| 23 | `e005_1_ok` | 囁く井戸→水を汲んで飲む（成功） |
| 24 | `e005_1_ng` | 囁く井戸→水を汲んで飲む（失敗） |
| 25 | `e005_2_ok` | 囁く井戸→声に応える（成功） |
| 26 | `e005_2_ng` | 囁く井戸→声に応える（失敗） |
| 27 | `e006_0_ok` | ゴブリンの見張り→寝込みを襲う（成功） |
| 28 | `e006_0_ng` | ゴブリンの見張り→寝込みを襲う（失敗） |
| 29 | `e006_1_ok` | ゴブリンの見張り→忍び足で横を抜ける（成功） |
| 30 | `e006_1_ng` | ゴブリンの見張り→忍び足で横を抜ける（失敗） |
| 31 | `e006_2_ok` | ゴブリンの見張り→話しかけてみる（成功） |
| 32 | `e006_2_ng` | ゴブリンの見張り→話しかけてみる（失敗） |
| 33 | `e007_0_r` | 古い祭壇→血を一滴捧げる |
| 34 | `e007_1_ok` | 古い祭壇→静かに祈る（成功） |
| 35 | `e007_1_ng` | 古い祭壇→静かに祈る（失敗） |
| 36 | `e007_2_ok` | 古い祭壇→供物の金貨をくすねる（成功） |
| 37 | `e007_2_ng` | 古い祭壇→供物の金貨をくすねる（失敗） |
| 38 | `e008_1_r` | 迷子の少女→聖水を振りかける |
| 39 | `e008_2_ok` | 迷子の少女→気づかないふりをする（成功） |
| 40 | `e008_2_ng` | 迷子の少女→気づかないふりをする（失敗） |
| 41 | `e008_3_r` | 迷子の少女→走って逃げる |
| 42 | `e009_0_ok` | 燃え残りの焚き火→火にあたって眠る（成功） |
| 43 | `e009_0_ng` | 燃え残りの焚き火→火にあたって眠る（失敗） |
| 44 | `e009_1_r` | 燃え残りの焚き火→火を絶やさぬよう番をする |
| 45 | `e009_2_r` | 燃え残りの焚き火→火の中から薪を一本拝借する |
| 46 | `e009_3_r` | 燃え残りの焚き火→火の傍で装備を手入れする |
| 47 | `e010_0_r` | 闇の行商人→血で聖水を買う |
| 48 | `e010_1_r` | 闇の行商人→記憶で薬瓶を買う |
| 49 | `e010_2_r` | 闇の行商人→運を売って古地図を買う |
| 50 | `e010_3_r` | 闇の行商人→何も買わない |
| 51 | `e011_0_r` | 落とし穴→ロープを使って渡る |
| 52 | `e011_1_ok` | 落とし穴→助走をつけて跳ぶ（成功） |
| 53 | `e011_2_ok` | 落とし穴→穴に飛び込む（成功） |
| 54 | `e011_2_ng` | 落とし穴→穴に飛び込む（失敗） |
| 55 | `e012_0_r` | 蜘蛛の巣→たいまつで巣を焼く |
| 56 | `e012_1_ok` | 蜘蛛の巣→剣で切り裂いて進む（成功） |
| 57 | `e012_1_ng` | 蜘蛛の巣→剣で切り裂いて進む（失敗） |
| 58 | `e012_2_ok` | 蜘蛛の巣→動く繭を切り開く（成功） |
| 59 | `e013_0_ok` | 鏡の間→鏡の自分に話しかける（成功） |
| 60 | `e013_0_ng` | 鏡の間→鏡の自分に話しかける（失敗） |
| 61 | `e013_1_r` | 鏡の間→鏡を叩き割る |
| 62 | `e013_2_r` | 鏡の間→目を伏せて通り抜ける |
| 63 | `e014_0_ok` | 這い寄る粘液→核を狙って斬る（成功） |
| 64 | `e014_0_ng` | 這い寄る粘液→核を狙って斬る（失敗） |
| 65 | `e014_1_r` | 這い寄る粘液→火で追い払う |
| 66 | `e014_2_ok` | 這い寄る粘液→壁際をすり抜ける（成功） |
| 67 | `e014_2_ng` | 這い寄る粘液→壁際をすり抜ける（失敗） |
| 68 | `e015_0_ok` | 祈る修道士→祝福を乞う（成功） |
| 69 | `e015_0_ng` | 祈る修道士→祝福を乞う（失敗） |
| 70 | `e015_1_r` | 祈る修道士→呪いを祓ってもらう |
| 71 | `e015_2_ok` | 祈る修道士→聖水を分けてもらう（成功） |
| 72 | `e015_2_ng` | 祈る修道士→聖水を分けてもらう（失敗） |
| 73 | `e015_3_r` | 祈る修道士→邪魔をせず立ち去る |
| 74 | `e016_0_ok` | 崩れた階段→瓦礫を伝って一気に降りる（成功） |
| 75 | `e016_0_ng` | 崩れた階段→瓦礫を伝って一気に降りる（失敗） |
| 76 | `e016_1_r` | 崩れた階段→古地図で別の階段を探す |
| 77 | `e016_2_r` | 崩れた階段→遠回りして別の道を探す |
| 78 | `e017_0_ok` | 壁の顔→壁を砕いて助け出す（成功） |
| 79 | `e017_0_ng` | 壁の顔→壁を砕いて助け出す（失敗） |
| 80 | `e017_1_ok` | 壁の顔→顔の話を聞く（成功） |
| 81 | `e017_1_ng` | 壁の顔→顔の話を聞く（失敗） |
| 82 | `e017_2_r` | 壁の顔→足早に通り過ぎる |
| 83 | `e018_0_ok` | 光るキノコ→食べてみる（成功） |
| 84 | `e018_0_ng` | 光るキノコ→食べてみる（失敗） |
| 85 | `e018_1_ok` | 光るキノコ→摘んで薬を作る（成功） |
| 86 | `e018_1_ng` | 光るキノコ→摘んで薬を作る（失敗） |
| 87 | `e018_2_r` | 光るキノコ→踏まないように進む |
| 88 | `e019_0_r` | 吊るされた檻→錆びた鍵で檻を開ける |
| 89 | `e019_1_ok` | 吊るされた檻→檻を揺らして壊す（成功） |
| 90 | `e019_1_ng` | 吊るされた檻→檻を揺らして壊す（失敗） |
| 91 | `e019_2_r` | 吊るされた檻→見なかったことにする |
| 92 | `e020_1_ok` | 黒い犬→撫でようと手を伸ばす（成功） |
| 93 | `e020_1_ng` | 黒い犬→撫でようと手を伸ばす（失敗） |
| 94 | `e020_2_r` | 黒い犬→追い払う |
| 95 | `e021_0_r` | 走り書きのメモ→最後まで読む |
| 96 | `e021_1_r` | 走り書きのメモ→メモを持っていく |
| 97 | `e021_2_r` | 走り書きのメモ→火にくべる |
| 98 | `e022_0_ok` | 地下水脈→水を飲んで休む（成功） |
| 99 | `e022_0_ng` | 地下水脈→水を飲んで休む（失敗） |
| 100 | `e022_1_ok` | 地下水脈→水底の光を拾う（成功） |
| 101 | `e022_1_ng` | 地下水脈→水底の光を拾う（失敗） |
| 102 | `e022_2_r` | 地下水脈→顔を洗って気を引き締める |
| 103 | `e023_1_ok` | 甲冑の亡霊→手合わせを願う（成功） |
| 104 | `e023_1_ng` | 甲冑の亡霊→手合わせを願う（失敗） |
| 105 | `e023_2_r` | 甲冑の亡霊→関わらずに先へ行く |
| 106 | `e024_0_ok` | コウモリの嵐→伏せてやり過ごす（成功） |
| 107 | `e024_0_ng` | コウモリの嵐→伏せてやり過ごす（失敗） |
| 108 | `e024_1_ok` | コウモリの嵐→顔を庇って走り抜ける（成功） |
| 109 | `e024_1_ng` | コウモリの嵐→顔を庇って走り抜ける（失敗） |
| 110 | `e024_2_r` | コウモリの嵐→黒い犬に追い払わせる |
| 111 | `e024_3_ok` | コウモリの嵐→群れが去った後の巣を漁る（成功） |
| 112 | `e024_3_ng` | コウモリの嵐→群れが去った後の巣を漁る（失敗） |
| 113 | `e025_0_ok` | 骸骨の賭博師→運命を賭ける（成功） |
| 114 | `e025_0_ng` | 骸骨の賭博師→運命を賭ける（失敗） |
| 115 | `e025_1_ok` | 骸骨の賭博師→イカサマを見破る（成功） |
| 116 | `e025_1_ng` | 骸骨の賭博師→イカサマを見破る（失敗） |
| 117 | `e025_2_r` | 骸骨の賭博師→断ってテーブルをひっくり返す |
| 118 | `e026_0_ok` | 赤い扉→開けて中に入る（成功） |
| 119 | `e026_0_ng` | 赤い扉→開けて中に入る（失敗） |
| 120 | `e026_1_ok` | 赤い扉→ノックする（成功） |
| 121 | `e026_1_ng` | 赤い扉→ノックする（失敗） |
| 122 | `e026_2_r` | 赤い扉→見なかったことにする |
| 123 | `e027_0_ok` | 子守唄→一緒に歌う（成功） |
| 124 | `e027_0_ng` | 子守唄→一緒に歌う（失敗） |
| 125 | `e027_1_ok` | 子守唄→揺りかごを止める（成功） |
| 126 | `e027_1_ng` | 子守唄→揺りかごを止める（失敗） |
| 127 | `e027_3_r` | 子守唄→耳を塞いで通り抜ける |
| 128 | `e028_0_r` | 泣く石像→体力を捧げる |
| 129 | `e028_1_r` | 泣く石像→心を捧げる |
| 130 | `e028_2_ok` | 泣く石像→涙を拭ってやる（成功） |
| 131 | `e028_2_ng` | 泣く石像→涙を拭ってやる（失敗） |
| 132 | `e029_0_ok` | 盗賊の待ち伏せ→戦う（成功） |
| 133 | `e029_0_ng` | 盗賊の待ち伏せ→戦う（失敗） |
| 134 | `e029_1_ok` | 盗賊の待ち伏せ→言いくるめる（成功） |
| 135 | `e029_1_ng` | 盗賊の待ち伏せ→言いくるめる（失敗） |
| 136 | `e029_2_r` | 盗賊の待ち伏せ→黒い犬をけしかける |
| 137 | `e029_3_r` | 盗賊の待ち伏せ→大人しく荷物を渡す |
| 138 | `e030_0_ok` | 水晶玉→未来を見届ける（成功） |
| 139 | `e030_0_ng` | 水晶玉→未来を見届ける（失敗） |
| 140 | `e030_1_r` | 水晶玉→水晶玉を砕く |
| 141 | `e030_2_ok` | 水晶玉→水晶玉を持ち去る（成功） |
| 142 | `e030_2_ng` | 水晶玉→水晶玉を持ち去る（失敗） |
| 143 | `e031_0_ok` | 弔いの鐘→鐘を鳴らす（成功） |
| 144 | `e031_0_ng` | 弔いの鐘→鐘を鳴らす（失敗） |
| 145 | `e031_1_ok` | 弔いの鐘→自分の名前を削り取る（成功） |
| 146 | `e031_1_ng` | 弔いの鐘→自分の名前を削り取る（失敗） |
| 147 | `e031_2_r` | 弔いの鐘→静かに通り過ぎる |
| 148 | `e032_0_ok` | 岩に刺さった剣→渾身の力で引き抜く（成功） |
| 149 | `e032_0_ng` | 岩に刺さった剣→渾身の力で引き抜く（失敗） |
| 150 | `e032_1_ok` | 岩に刺さった剣→運命に任せて引き抜く（成功） |
| 151 | `e032_1_ng` | 岩に刺さった剣→運命に任せて引き抜く（失敗） |
| 152 | `e032_2_r` | 岩に刺さった剣→骸骨たちの持ち物を漁る |
| 153 | `n06_0_ok` | 迷宮の中の街角→窓を覗く（成功） |
| 154 | `n06_0_ng` | 迷宮の中の街角→窓を覗く（失敗） |
| 155 | `n06_1_r` | 迷宮の中の街角→走り書きの続きを読む |
| 156 | `n06_2_r` | 迷宮の中の街角→街灯の火をもらう |
| 157 | `g025_1_r` | 骨の門番→聖水を浴びせる |
| 158 | `g025_2_ok` | 骨の門番→門をよじ登って越える（成功） |
| 159 | `g025_2_ng` | 骨の門番→門をよじ登って越える（失敗） |
| 160 | `g025_3_ok` | 骨の門番→門と問答する（成功） |
| 161 | `g025_3_ng` | 骨の門番→門と問答する（失敗） |
| 162 | `g025_4_r` | 骨の門番→通行料として運を払う |
| 163 | `e033_0_ok` | 納骨堂→骨の山を漁る（成功） |
| 164 | `e033_0_ng` | 納骨堂→骨の山を漁る（失敗） |
| 165 | `e033_1_r` | 納骨堂→死者に祈りを捧げる |
| 166 | `e033_2_ok` | 納骨堂→息を止めて走り抜ける（成功） |
| 167 | `e033_2_ng` | 納骨堂→息を止めて走り抜ける（失敗） |
| 168 | `e034_0_r` | さまよう亡霊→聖水で浄化する |
| 169 | `e034_1_ok` | さまよう亡霊→一緒に死に場所を探す（成功） |
| 170 | `e034_1_ng` | さまよう亡霊→一緒に死に場所を探す（失敗） |
| 171 | `e034_2_ok` | さまよう亡霊→気配を消してやり過ごす（成功） |
| 172 | `e034_2_ng` | さまよう亡霊→気配を消してやり過ごす（失敗） |
| 173 | `e035_0_ok` | 釘打たれた棺→棺を開ける（成功） |
| 174 | `e035_0_ng` | 釘打たれた棺→棺を開ける（失敗） |
| 175 | `e035_1_ok` | 釘打たれた棺→釘をさらに打ち込む（成功） |
| 176 | `e035_1_ng` | 釘打たれた棺→釘をさらに打ち込む（失敗） |
| 177 | `e035_2_ok` | 釘打たれた棺→棺に話しかける（成功） |
| 178 | `e035_2_ng` | 釘打たれた棺→棺に話しかける（失敗） |
| 179 | `e036_0_ok` | 水没した回廊→泳いで渡る（成功） |
| 180 | `e036_0_ng` | 水没した回廊→泳いで渡る（失敗） |
| 181 | `e036_1_r` | 水没した回廊→ロープを渡して進む |
| 182 | `e036_2_ok` | 水没した回廊→水が引くのを待つ（成功） |
| 183 | `e036_2_ng` | 水没した回廊→水が引くのを待つ（失敗） |
| 184 | `e037_1_r` | 渡し守→思い出を一つ払う |
| 185 | `e037_2_ok` | 渡し守→渡し守を突き落として舟を奪う（成功） |
| 186 | `e037_2_ng` | 渡し守→渡し守を突き落として舟を奪う（失敗） |
| 187 | `e037_3_r` | 渡し守→湖岸を歩いて回り込む |
| 188 | `e038_0_ok` | 屍喰らい→先手を取って斬りかかる（成功） |
| 189 | `e038_0_ng` | 屍喰らい→先手を取って斬りかかる（失敗） |
| 190 | `e038_1_r` | 屍喰らい→銀の剣を抜く |
| 191 | `e038_2_ok` | 屍喰らい→死骸を差し出して後ずさる（成功） |
| 192 | `e038_2_ng` | 屍喰らい→死骸を差し出して後ずさる（失敗） |
| 193 | `e039_0_r` | 沼の魔女→取引に応じる |
| 194 | `e039_1_r` | 沼の魔女→薬だけ売ってもらう |
| 195 | `e039_2_ok` | 沼の魔女→鍋をひっくり返して逃げる（成功） |
| 196 | `e039_2_ng` | 沼の魔女→鍋をひっくり返して逃げる（失敗） |
| 197 | `e040_0_ok` | 囁く人形→遊んであげる（成功） |
| 198 | `e040_0_ng` | 囁く人形→遊んであげる（失敗） |
| 199 | `e040_1_ok` | 囁く人形→人形を叩き壊す（成功） |
| 200 | `e040_1_ng` | 囁く人形→人形を叩き壊す（失敗） |

---

## プロンプトの組み立て方（全画像共通）

この指示書は長くなりすぎないよう、共通部分を一度だけ書いています。各画像のプロンプトは、次の順に**そのままつなげて**作ってください（書き換えない）。

1. 下の「共通の画風指定」の文章全体
2. 空行1つ
3. `Scene: ` に続けて、その画像の「Scene」の文章
4. その画像に「Characters」の指定がある場合だけ：空行1つ、`Characters (keep them consistent across images):` の1行、続けて指定された人物の行を、下の「登場人物」からそのまま1行ずつ

### 共通の画風指定

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).
```

### 登場人物

```
- the hooded adventurer: a lone adventurer in a long dark hooded cloak; the face is completely hidden in black shadow inside the hood except for two tiny white glowing dots for eyes; carries a small lantern and a short sword; slim, ordinary human size
- the ghost girl: a girl about six years old, pale and faintly translucent, in a long plain white nightgown, barefoot, shoulder-length dark hair, a small crown-shaped royal crest pendant on her chest; she casts no shadow
- the ghost knight: half-transparent and faintly glowing, in battered rusted plate armour with a torn tabard bearing a crown crest; the open helmet is empty inside, no face; carries a longsword
- the queen: a woman with long loose hair in a long pale gown
```

---

### 1. e001_0_r：錆びた扉→錆びた鍵で開ける

保存名：`generated/e001_0_r.png`

- Scene: Behind an opened rusted iron door, a tiny storeroom: the hooded adventurer kneels by shelves of dry rations and a small scatter of coins, a rusty key still in the lock. Red only: a small red cloth sack among the rations.
- Characters: the hooded adventurer

### 2. e001_1_ok：錆びた扉→体当たりで押し開ける（成功）

保存名：`generated/e001_1_ok.png`

- Scene: A heavy rusted iron door has crashed flat onto the floor in a cloud of dust; the hooded adventurer pulls a coil of rope from an old backpack lying beyond it. Red only: rust streaks on the fallen door.
- Characters: the hooded adventurer

### 3. e001_1_ng：錆びた扉→体当たりで押し開ける（失敗）

保存名：`generated/e001_1_ng.png`

- Scene: the hooded adventurer rebounds from a rusted iron door that has not moved at all, clutching their bruised shoulder in pain. Red only: a few rust streaks on the door.
- Characters: the hooded adventurer

### 4. e001_2_ok：錆びた扉→耳を当てて様子をうかがう（成功）

保存名：`generated/e001_2_ok.png`

- Scene: A rusted iron door stands open; beyond it only a chain sways gently in the draft, and the hooded adventurer walks calmly through. Red only: a small rust patch on the chain.
- Characters: the hooded adventurer

### 5. e001_3_r：錆びた扉→扉には触れず迂回する

保存名：`generated/e001_3_r.png`

- Scene: the hooded adventurer trudges along a long, damp, dark detour passage, shoulders slumped with fatigue, water dripping from the ceiling. Red only: a faint red glow at the far end of the passage.
- Characters: the hooded adventurer

### 6. e002_0_r：ネズミの群れ→たいまつを振りかざす

保存名：`generated/e002_0_r.png`

- Scene: the hooded adventurer thrusts a blazing torch forward and a flood of grey rats scatters away squealing into the dark corners of a stone corridor. Red only: the flame of the torch.
- Characters: the hooded adventurer

### 7. e002_1_ok：ネズミの群れ→踏みつけて突っ切る（成功）

保存名：`generated/e002_1_ok.png`

- Scene: the hooded adventurer charges through a river of rats in a corridor, stamping through them, the boots slipping. Red only: small splashes of blood under the boots.
- Characters: the hooded adventurer

### 8. e002_1_ng：ネズミの群れ→踏みつけて突っ切る（失敗）

保存名：`generated/e002_1_ng.png`

- Scene: the hooded adventurer has fallen on the floor of a corridor and is swarmed by hundreds of rats biting at their arms and legs. Red only: the rats' eyes as small bold dots.
- Characters: the hooded adventurer

### 9. e002_2_ok：ネズミの群れ→息を殺して通り過ぎるのを待つ（成功）

保存名：`generated/e002_2_ok.png`

- Scene: the hooded adventurer stands pressed silently against a corridor wall as the last of a river of rats flows away into the distance; stillness returns. Red only: the eyes of the last few rats.
- Characters: the hooded adventurer

### 10. e002_2_ng：ネズミの群れ→息を殺して通り過ぎるのを待つ（失敗）

保存名：`generated/e002_2_ng.png`

- Scene: the hooded adventurer sits huddled and exhausted against a corridor wall while rats still crawl over their boots and around them in the dark. Red only: the rats' eyes as small dots.
- Characters: the hooded adventurer

### 11. e002_3_r：ネズミの群れ→携帯食を投げて気を逸らす

保存名：`generated/e002_3_r.png`

- Scene: A swarm of rats piles onto a tossed bundle of food in a corridor while the hooded adventurer slips past, a hand on their empty stomach. Red only: the rats' eyes as small dots.
- Characters: the hooded adventurer

### 12. e003_0_ok：先客の亡骸→荷物を漁る（成功）

保存名：`generated/e003_0_ok.png`

- Scene: the hooded adventurer kneels beside a skeleton slumped against a wall and pulls a usable torch and a few coins out of its old backpack. Red only: the head of the torch.
- Characters: the hooded adventurer

### 13. e003_0_ng：先客の亡骸→荷物を漁る（失敗）

保存名：`generated/e003_0_ng.png`

- Scene: the hooded adventurer leaps back in fright from a slumped skeleton whose jaw has just clacked open, the backpack left untouched. Red only: a faint glow in the skeleton's eye sockets.
- Characters: the hooded adventurer

### 14. e003_1_r：先客の亡骸→指し示す先の床を調べる

保存名：`generated/e003_1_r.png`

- Scene: the hooded adventurer has lifted a floor stone where a skeleton's finger points, revealing a rusty key hidden underneath. Red only: the rusty key.
- Characters: the hooded adventurer

### 15. e003_2_r：先客の亡骸→祈りを捧げて弔う

保存名：`generated/e003_2_r.png`

- Scene: the hooded adventurer kneels in prayer before a skeleton slumped against a dungeon wall, head bowed; a gentle light falls on them. Red only: a small red cloth tied on the skeleton's broken sword.
- Characters: the hooded adventurer

### 16. e004_0_ok：宝箱→迷わず開ける（成功）

保存名：`generated/e004_0_ok.png`

- Scene: An ornate treasure chest thrown open, overflowing with gold coins that spill onto the floor; the hooded adventurer stares in surprise. Red only: a large gem among the coins.
- Characters: the hooded adventurer

### 17. e004_0_ng：宝箱→迷わず開ける（失敗）

保存名：`generated/e004_0_ng.png`

- Scene: A treasure chest has split open into a mimic with rows of fangs and a long tongue, biting at the hooded adventurer, who flees clutching their arm. Red only: the mimic's tongue.
- Characters: the hooded adventurer

### 18. e004_1_ok：宝箱→剣で叩いてから開ける（成功）

保存名：`generated/e004_1_ok.png`

- Scene: A dead mimic chest lies limp after being struck; coins spill from its open mouth as the hooded adventurer lowers the sword. Red only: the mimic's lolling tongue.
- Characters: the hooded adventurer

### 19. e004_1_ng：宝箱→剣で叩いてから開ける（失敗）

保存名：`generated/e004_1_ng.png`

- Scene: the hooded adventurer fights a thrashing mimic chest with fangs, sword raised, a wound on their arm. Red only: the mimic's tongue.
- Characters: the hooded adventurer

### 20. e004_2_r：宝箱→触らずに立ち去る

保存名：`generated/e004_2_r.png`

- Scene: the hooded adventurer walks away from an ornate treasure chest in an empty room; behind them the chest lid has opened a crack, showing teeth. Red only: a tongue tip peeking from the lid.
- Characters: the hooded adventurer

### 21. e005_0_ok：囁く井戸→金貨を一枚投げ入れる（成功）

保存名：`generated/e005_0_ok.png`

- Scene: A warm glow rises from a stone well like a column of soft light; the hooded adventurer stands at the rim, bathed in it. Red only: a coin glinting as it falls.
- Characters: the hooded adventurer

### 22. e005_0_ng：囁く井戸→金貨を一枚投げ入れる（失敗）

保存名：`generated/e005_0_ng.png`

- Scene: the hooded adventurer leans over a stone well; from the darkness below, a mouth full of teeth grins up. Red only: the grinning mouth's gums.
- Characters: the hooded adventurer

### 23. e005_1_ok：囁く井戸→水を汲んで飲む（成功）

保存名：`generated/e005_1_ok.png`

- Scene: the hooded adventurer drinks clear water from a bucket at a stone well, eyes closed in relief. Red only: a small red flower growing from a crack in the well.
- Characters: the hooded adventurer

### 24. e005_1_ng：囁く井戸→水を汲んで飲む（失敗）

保存名：`generated/e005_1_ng.png`

- Scene: the hooded adventurer spits out a mouthful of dark liquid from a bucket at a stone well, recoiling. Red only: the liquid, which is blood.
- Characters: the hooded adventurer

### 25. e005_2_ok：囁く井戸→声に応える（成功）

保存名：`generated/e005_2_ok.png`

- Scene: the hooded adventurer leans over a stone well as a faint pale figure deep below raises a hand as if waving them away; peaceful. Red only: none except a faint red glow far down.
- Characters: the hooded adventurer

### 26. e005_2_ng：囁く井戸→声に応える（失敗）

保存名：`generated/e005_2_ng.png`

- Scene: the hooded adventurer runs away from a stone well as long pale arms crawl up over its rim behind them. Red only: the fingernails of the arms.
- Characters: the hooded adventurer

### 27. e006_0_ok：ゴブリンの見張り→寝込みを襲う（成功）

保存名：`generated/e006_0_ok.png`

- Scene: A goblin lies knocked out against the rock while the hooded adventurer picks a small potion bottle and coins from its stolen goods. Red only: the potion in the bottle.
- Characters: the hooded adventurer

### 28. e006_0_ng：ゴブリンの見張り→寝込みを襲う（失敗）

保存名：`generated/e006_0_ng.png`

- Scene: A goblin wakes and screeches, more goblin eyes appearing in the dark tunnels, while the hooded adventurer flees wounded. Red only: the goblins' eyes.
- Characters: the hooded adventurer

### 29. e006_1_ok：ゴブリンの見張り→忍び足で横を抜ける（成功）

保存名：`generated/e006_1_ok.png`

- Scene: the hooded adventurer tiptoes silently past a sleeping goblin hugging its spear at a cave fork. Red only: the red cloth tied on the goblin's spear.
- Characters: the hooded adventurer

### 30. e006_1_ng：ゴブリンの見張り→忍び足で横を抜ける（失敗）

保存名：`generated/e006_1_ng.png`

- Scene: A goblin's thrown spear grazes the hooded adventurer's shoulder as they run past, a pebble skittering on the floor. Red only: a thin cut on the shoulder.
- Characters: the hooded adventurer

### 31. e006_2_ok：ゴブリンの見張り→話しかけてみる（成功）

保存名：`generated/e006_2_ok.png`

- Scene: A frightened goblin points a long finger toward a narrow side tunnel while the hooded adventurer crouches to listen. Red only: a small red cloth on the goblin's spear.
- Characters: the hooded adventurer

### 32. e006_2_ng：ゴブリンの見張り→話しかけてみる（失敗）

保存名：`generated/e006_2_ng.png`

- Scene: A goblin screams shrilly at the hooded adventurer, who covers their ears in pain. Red only: the goblin's open mouth.
- Characters: the hooded adventurer

### 33. e007_0_r：古い祭壇→血を一滴捧げる

保存名：`generated/e007_0_r.png`

- Scene: the hooded adventurer lets a drop of blood fall from a fingertip onto an old black stone altar, where it soaks into the stone. Red only: the drop of blood.
- Characters: the hooded adventurer

### 34. e007_1_ok：古い祭壇→静かに祈る（成功）

保存名：`generated/e007_1_ok.png`

- Scene: the hooded adventurer kneels in prayer at an old stone altar, enveloped in soft pale light from above. Red only: old dried stains on the altar, small.
- Characters: the hooded adventurer

### 35. e007_1_ng：古い祭壇→静かに祈る（失敗）

保存名：`generated/e007_1_ng.png`

- Scene: the hooded adventurer kneels at an old stone altar while huge eyes open in the darkness behind the pillars, watching. Red only: the eyes in the dark.
- Characters: the hooded adventurer

### 36. e007_2_ok：古い祭壇→供物の金貨をくすねる（成功）

保存名：`generated/e007_2_ok.png`

- Scene: the hooded adventurer slips a coin from an offering bowl on an old altar into a pouch, glancing around. Red only: the coin in hand.
- Characters: the hooded adventurer

### 37. e007_2_ng：古い祭壇→供物の金貨をくすねる（失敗）

保存名：`generated/e007_2_ng.png`

- Scene: the hooded adventurer stares at their own fingertips, turned black, holding a coin taken from an altar. Red only: dark red veins spreading from the fingertips.
- Characters: the hooded adventurer

### 38. e008_1_r：迷子の少女→聖水を振りかける

保存名：`generated/e008_1_r.png`

- Scene: the ghost girl smiles gently and dissolves into motes of light as drops of holy water sparkle in the air before the hooded adventurer. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 39. e008_2_ok：迷子の少女→気づかないふりをする（成功）

保存名：`generated/e008_2_ok.png`

- Scene: the hooded adventurer walks on down a dark corridor without looking back; far behind, the small white figure of the ghost girl grows distant. Red only: the crest pendant on the girl.
- Characters: the hooded adventurer, the ghost girl

### 40. e008_2_ng：迷子の少女→気づかないふりをする（失敗）

保存名：`generated/e008_2_ng.png`

- Scene: As the hooded adventurer passes, the ghost girl's head has turned all the way around to face them, her face hidden by her dark hair. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 41. e008_3_r：迷子の少女→走って逃げる

保存名：`generated/e008_3_r.png`

- Scene: the hooded adventurer runs breathlessly down a dark corridor while the small pale figure of the ghost girl follows far behind. Red only: the crest pendant on the girl.
- Characters: the hooded adventurer, the ghost girl

### 42. e009_0_ok：燃え残りの焚き火→火にあたって眠る（成功）

保存名：`generated/e009_0_ok.png`

- Scene: the hooded adventurer sleeps peacefully curled by a smouldering campfire in a cave. Red only: the embers of the fire.
- Characters: the hooded adventurer

### 43. e009_0_ng：燃え残りの焚き火→火にあたって眠る（失敗）

保存名：`generated/e009_0_ng.png`

- Scene: the hooded adventurer wakes by a burnt-out campfire to find countless small footprints in the dust all around where they slept. Red only: the last embers.
- Characters: the hooded adventurer

### 44. e009_1_r：燃え残りの焚き火→火を絶やさぬよう番をする

保存名：`generated/e009_1_r.png`

- Scene: the hooded adventurer sits awake by a campfire, feeding it a stick, warming their hands. Red only: the flames.
- Characters: the hooded adventurer

### 45. e009_2_r：燃え残りの焚き火→火の中から薪を一本拝借する

保存名：`generated/e009_2_r.png`

- Scene: the hooded adventurer walks away from a campfire holding a burning branch up as a torch. Red only: the flame on the branch.
- Characters: the hooded adventurer

### 46. e009_3_r：燃え残りの焚き火→火の傍で装備を手入れする

保存名：`generated/e009_3_r.png`

- Scene: the hooded adventurer sits by a campfire sharpening a short sword on a whetstone, boots laced tight. Red only: the embers.
- Characters: the hooded adventurer

### 47. e010_0_r：闇の行商人→血で聖水を買う

保存名：`generated/e010_0_r.png`

- Scene: The hooded faceless peddler makes a thin cut on the hooded adventurer's forearm with a small blade and hands over a little vial. Red only: the thin cut.
- Characters: the hooded adventurer

### 48. e010_1_r：闇の行商人→記憶で薬瓶を買う

保存名：`generated/e010_1_r.png`

- Scene: the hooded adventurer stands dazed holding a small potion bottle while the hooded peddler pockets a glowing wisp drawn from their head. Red only: the liquid in the bottle.
- Characters: the hooded adventurer

### 49. e010_2_r：闇の行商人→運を売って古地図を買う

保存名：`generated/e010_2_r.png`

- Scene: The hooded faceless peddler nods and hands an old map to the hooded adventurer. Red only: a route marked on the map.
- Characters: the hooded adventurer

### 50. e010_3_r：闇の行商人→何も買わない

保存名：`generated/e010_3_r.png`

- Scene: The hooded peddler's lantern goes out and only darkness remains where they stood; the hooded adventurer stands alone. Red only: the last ember in the lantern.
- Characters: the hooded adventurer

### 51. e011_0_r：落とし穴→ロープを使って渡る

保存名：`generated/e011_0_r.png`

- Scene: the hooded adventurer crosses a black pit in a corridor by a rope tied to a pillar, hand over hand. Red only: a red cloth tied on the pillar.
- Characters: the hooded adventurer

### 52. e011_1_ok：落とし穴→助走をつけて跳ぶ（成功）

保存名：`generated/e011_1_ok.png`

- Scene: the hooded adventurer lands safely on the far side of a black pit after a running jump, cloak flaring. Red only: a faint red glow deep in the pit.
- Characters: the hooded adventurer

### 53. e011_2_ok：落とし穴→穴に飛び込む（成功）

保存名：`generated/e011_2_ok.png`

- Scene: the hooded adventurer lands softly in a big pile of straw on a lower floor after falling through a hole far above. Red only: a small red flower in the straw.
- Characters: the hooded adventurer

### 54. e011_2_ng：落とし穴→穴に飛び込む（失敗）

保存名：`generated/e011_2_ng.png`

- Scene: the hooded adventurer lies sprawled on a hard stone floor after a long fall, a hole far above. Red only: a small bloody scrape.
- Characters: the hooded adventurer

### 55. e012_0_r：蜘蛛の巣→たいまつで巣を焼く

保存名：`generated/e012_0_r.png`

- Scene: A huge spider web blazes up in flames; a scorched cocoon drops a ring that rolls toward the hooded adventurer's feet. Red only: the flames.
- Characters: the hooded adventurer

### 56. e012_1_ok：蜘蛛の巣→剣で切り裂いて進む（成功）

保存名：`generated/e012_1_ok.png`

- Scene: the hooded adventurer slashes through thick white spider web with a short sword and steps through. Red only: the spider's eyes far up in the dark.
- Characters: the hooded adventurer

### 57. e012_1_ng：蜘蛛の巣→剣で切り裂いて進む（失敗）

保存名：`generated/e012_1_ng.png`

- Scene: A giant spider drops from the ceiling onto the hooded adventurer, fangs sinking in; the world tilts. Red only: the spider's eyes.
- Characters: the hooded adventurer

### 58. e012_2_ok：蜘蛛の巣→動く繭を切り開く（成功）

保存名：`generated/e012_2_ok.png`

- Scene: the hooded adventurer helps a weak, starving adventurer out of a cut-open cocoon; the adventurer offers a small charm. Red only: the charm.
- Characters: the hooded adventurer

### 59. e013_0_ok：鏡の間→鏡の自分に話しかける（成功）

保存名：`generated/e013_0_ok.png`

- Scene: In a tall mirror, the reflection of the hooded adventurer grins and points to the right, while the real adventurer stares. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 60. e013_0_ng：鏡の間→鏡の自分に話しかける（失敗）

保存名：`generated/e013_0_ng.png`

- Scene: In a tall mirror, the reflection of the hooded adventurer has its mouth stretched wide open in a silent scream. Red only: the inside of the reflection's mouth.
- Characters: the hooded adventurer

### 61. e013_1_r：鏡の間→鏡を叩き割る

保存名：`generated/e013_1_r.png`

- Scene: A shattered mirror; the hooded adventurer holds a cut hand among the shards on the floor. Red only: the cut on the hand.
- Characters: the hooded adventurer

### 62. e013_2_r：鏡の間→目を伏せて通り抜ける

保存名：`generated/e013_2_r.png`

- Scene: the hooded adventurer walks with eyes down through a hall of mirrors; in every mirror the reflections have turned their heads to watch. Red only: the reflections' eyes.
- Characters: the hooded adventurer

### 63. e014_0_ok：這い寄る粘液→核を狙って斬る（成功）

保存名：`generated/e014_0_ok.png`

- Scene: A black slime collapses into a puddle after its core is cut; the hooded adventurer picks a coin out of the goo. Red only: the shattered core.
- Characters: the hooded adventurer

### 64. e014_0_ng：這い寄る粘液→核を狙って斬る（失敗）

保存名：`generated/e014_0_ng.png`

- Scene: the hooded adventurer's sword and arm sink into a black slime that burns and smokes, the hooded adventurer recoiling in pain. Red only: the glowing core.
- Characters: the hooded adventurer

### 65. e014_1_r：這い寄る粘液→火で追い払う

保存名：`generated/e014_1_r.png`

- Scene: A black slime flees from a torch, oozing into cracks in the floor, as the hooded adventurer holds the fire out. Red only: the torch flame.
- Characters: the hooded adventurer

### 66. e014_2_ok：這い寄る粘液→壁際をすり抜ける（成功）

保存名：`generated/e014_2_ok.png`

- Scene: the hooded adventurer edges along a cave wall past a black slime that does not notice. Red only: the slime's glowing core.
- Characters: the hooded adventurer

### 67. e014_2_ng：這い寄る粘液→壁際をすり抜ける（失敗）

保存名：`generated/e014_2_ng.png`

- Scene: Black slime wraps the hooded adventurer's ankle, the boot melting and smoking. Red only: the slime's core.
- Characters: the hooded adventurer

### 68. e015_0_ok：祈る修道士→祝福を乞う（成功）

保存名：`generated/e015_0_ok.png`

- Scene: A monk with clouded eyes traces a sign on the hooded adventurer's forehead with a finger; a soft glow. Red only: the sign on the forehead.
- Characters: the hooded adventurer

### 69. e015_0_ng：祈る修道士→祝福を乞う（失敗）

保存名：`generated/e015_0_ng.png`

- Scene: A monk with clouded eyes grips the hooded adventurer's forehead with an icy hand, frost spreading. Red only: the votive candle flame behind.
- Characters: the hooded adventurer

### 70. e015_1_r：祈る修道士→呪いを祓ってもらう

保存名：`generated/e015_1_r.png`

- Scene: A monk prays over the hooded adventurer's blackened hand; the black fades from the fingers. Red only: the last dark red mark fading.
- Characters: the hooded adventurer

### 71. e015_2_ok：祈る修道士→聖水を分けてもらう（成功）

保存名：`generated/e015_2_ok.png`

- Scene: A monk silently holds out a small vial of holy water to the hooded adventurer. Red only: the candle flame on the altar.
- Characters: the hooded adventurer

### 72. e015_2_ng：祈る修道士→聖水を分けてもらう（失敗）

保存名：`generated/e015_2_ng.png`

- Scene: A monk shakes his head and turns his back on the hooded adventurer in a ruined chapel. Red only: the candle flame on the altar.
- Characters: the hooded adventurer

### 73. e015_3_r：祈る修道士→邪魔をせず立ち去る

保存名：`generated/e015_3_r.png`

- Scene: the hooded adventurer walks away from a ruined chapel; behind them the kneeling monk's shadow on the wall has become something inhuman. Red only: the shadow's eyes.
- Characters: the hooded adventurer

### 74. e016_0_ok：崩れた階段→瓦礫を伝って一気に降りる（成功）

保存名：`generated/e016_0_ok.png`

- Scene: the hooded adventurer leaps down from broken stair blocks into the darkness, landing two levels lower. Red only: a faint red glow below.
- Characters: the hooded adventurer

### 75. e016_0_ng：崩れた階段→瓦礫を伝って一気に降りる（失敗）

保存名：`generated/e016_0_ng.png`

- Scene: the hooded adventurer tumbles down a collapsing staircase among falling rubble. Red only: a small bloody scrape.
- Characters: the hooded adventurer

### 76. e016_1_r：崩れた階段→古地図で別の階段を探す

保存名：`generated/e016_1_r.png`

- Scene: the hooded adventurer holds an old map and finds a hidden staircase behind a loose wall. Red only: a route marked on the map.
- Characters: the hooded adventurer

### 77. e016_2_r：崩れた階段→遠回りして別の道を探す

保存名：`generated/e016_2_r.png`

- Scene: the hooded adventurer walks a long winding detour passage, small in the frame. Red only: a faint glow far ahead.
- Characters: the hooded adventurer

### 78. e017_0_ok：壁の顔→壁を砕いて助け出す（成功）

保存名：`generated/e017_0_ok.png`

- Scene: A gaunt man tumbles out of a broken stone wall and presses an old key into the hooded adventurer's hand before vanishing into the dark. Red only: the key.
- Characters: the hooded adventurer

### 79. e017_0_ng：壁の顔→壁を砕いて助け出す（失敗）

保存名：`generated/e017_0_ng.png`

- Scene: the hooded adventurer has smashed a stone wall open to find nothing inside; a laughing face has risen out of the wall further along. Red only: the laughing face's mouth.
- Characters: the hooded adventurer

### 80. e017_1_ok：壁の顔→顔の話を聞く（成功）

保存名：`generated/e017_1_ok.png`

- Scene: A face in a stone wall speaks while the hooded adventurer listens closely; faint visions of a deep labyrinth and a weeping figure appear around it. Red only: the tear on the face.
- Characters: the hooded adventurer

### 81. e017_1_ng：壁の顔→顔の話を聞く（失敗）

保存名：`generated/e017_1_ng.png`

- Scene: A face in a stone wall babbles while the hooded adventurer clutches their head, dizzy. Red only: the face's mouth.
- Characters: the hooded adventurer

### 82. e017_2_r：壁の顔→足早に通り過ぎる

保存名：`generated/e017_2_r.png`

- Scene: the hooded adventurer hurries past while a face in the wall turns to follow them, mouth open. Red only: the face's eyes.
- Characters: the hooded adventurer

### 83. e018_0_ok：光るキノコ→食べてみる（成功）

保存名：`generated/e018_0_ok.png`

- Scene: the hooded adventurer bites into a glowing mushroom and stands taller, strength surging. Red only: the cap of the largest mushroom.
- Characters: the hooded adventurer

### 84. e018_0_ng：光るキノコ→食べてみる（失敗）

保存名：`generated/e018_0_ng.png`

- Scene: the hooded adventurer staggers in a cave where the walls seem to breathe and the floor grins, warped and swirling. Red only: the grinning mouth in the floor.
- Characters: the hooded adventurer

### 85. e018_1_ok：光るキノコ→摘んで薬を作る（成功）

保存名：`generated/e018_1_ok.png`

- Scene: the hooded adventurer grinds glowing mushrooms in a small bowl and fills a potion bottle. Red only: the potion.
- Characters: the hooded adventurer

### 86. e018_1_ng：光るキノコ→摘んで薬を作る（失敗）

保存名：`generated/e018_1_ng.png`

- Scene: the hooded adventurer coughs violently in a cloud of glowing spores. Red only: the cap of the largest mushroom.
- Characters: the hooded adventurer

### 87. e018_2_r：光るキノコ→踏まないように進む

保存名：`generated/e018_2_r.png`

- Scene: the hooded adventurer steps carefully between glowing mushrooms on a cave floor, avoiding them. Red only: the cap of the largest mushroom.
- Characters: the hooded adventurer

### 88. e019_0_r：吊るされた檻→錆びた鍵で檻を開ける

保存名：`generated/e019_0_r.png`

- Scene: A freed gaunt man hands a small whistle to the hooded adventurer; from the darkness a thin black dog appears. Red only: the dog's one eye.
- Characters: the hooded adventurer

### 89. e019_1_ok：吊るされた檻→檻を揺らして壊す（成功）

保存名：`generated/e019_1_ok.png`

- Scene: A hanging iron cage has broken its chain and fallen; a gaunt man crawls out free, pointing a warning finger at the hooded adventurer. Red only: the broken padlock.
- Characters: the hooded adventurer

### 90. e019_1_ng：吊るされた檻→檻を揺らして壊す（失敗）

保存名：`generated/e019_1_ng.png`

- Scene: A hanging iron cage swings wildly while the man inside screams and the hooded adventurer clutches a hurt arm. Red only: the padlock.
- Characters: the hooded adventurer

### 91. e019_2_r：吊るされた檻→見なかったことにする

保存名：`generated/e019_2_r.png`

- Scene: the hooded adventurer walks away while the gaunt man in a hanging cage curses after them, fist through the bars. Red only: the padlock.
- Characters: the hooded adventurer

### 92. e020_1_ok：黒い犬→撫でようと手を伸ばす（成功）

保存名：`generated/e020_1_ok.png`

- Scene: A thin black dog leans its head into the hooded adventurer's hand, eyes half closed. Red only: the dog's one eye.
- Characters: the hooded adventurer

### 93. e020_1_ng：黒い犬→撫でようと手を伸ばす（失敗）

保存名：`generated/e020_1_ng.png`

- Scene: A thin black dog bites the hooded adventurer's hand and darts away into the dark. Red only: the dog's one eye.
- Characters: the hooded adventurer

### 94. e020_2_r：黒い犬→追い払う

保存名：`generated/e020_2_r.png`

- Scene: A thin black dog glances back once at the hooded adventurer as it walks away into darkness. Red only: the dog's one eye.
- Characters: the hooded adventurer

### 95. e021_0_r：走り書きのメモ→最後まで読む

保存名：`generated/e021_0_r.png`

- Scene: the hooded adventurer holds a handwritten note whose bottom half is torn away; the writing is illegible scratches. Red only: the broken wax seal.
- Characters: the hooded adventurer

### 96. e021_1_r：走り書きのメモ→メモを持っていく

保存名：`generated/e021_1_r.png`

- Scene: the hooded adventurer folds a note and tucks it inside their cloak, standing by a rotting desk. Red only: the wax seal.
- Characters: the hooded adventurer

### 97. e021_2_r：走り書きのメモ→火にくべる

保存名：`generated/e021_2_r.png`

- Scene: A note burns in a candle flame held by the hooded adventurer; in the smoke, the faint shape of a screaming woman's face. Red only: the flame.
- Characters: the hooded adventurer

### 98. e022_0_ok：地下水脈→水を飲んで休む（成功）

保存名：`generated/e022_0_ok.png`

- Scene: the hooded adventurer kneels at a small clear pool in a cave, drinking cold water from cupped hands. Red only: a small red stone at the bottom of the pool.
- Characters: the hooded adventurer

### 99. e022_0_ng：地下水脈→水を飲んで休む（失敗）

保存名：`generated/e022_0_ng.png`

- Scene: the hooded adventurer doubles over in pain beside a small cave pool, clutching their stomach. Red only: a small red stone at the bottom of the pool.
- Characters: the hooded adventurer

### 100. e022_1_ok：地下水脈→水底の光を拾う（成功）

保存名：`generated/e022_1_ok.png`

- Scene: the hooded adventurer climbs out of an icy cave pool, holding up a small dripping pouch of silver coins. Red only: the pouch's drawstring.
- Characters: the hooded adventurer

### 101. e022_1_ng：地下水脈→水底の光を拾う（失敗）

保存名：`generated/e022_1_ng.png`

- Scene: A pale hand from the bottom of a cave pool grips the hooded adventurer's ankle as they struggle to pull free. Red only: the fingernails of the hand.
- Characters: the hooded adventurer

### 102. e022_2_r：地下水脈→顔を洗って気を引き締める

保存名：`generated/e022_2_r.png`

- Scene: the hooded adventurer splashes cold water on their face at a cave pool, eyes sharp. Red only: a small red stone at the bottom of the pool.
- Characters: the hooded adventurer

### 103. e023_1_ok：甲冑の亡霊→手合わせを願う（成功）

保存名：`generated/e023_1_ok.png`

- Scene: the ghost knight swings his sword clean through the hooded adventurer's body, who stands unharmed, the ghostly blade's arc glowing. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 104. e023_1_ng：甲冑の亡霊→手合わせを願う（失敗）

保存名：`generated/e023_1_ng.png`

- Scene: the ghost knight lowers his sword as the hooded adventurer reels back, a chill wound in their spirit, the knight fading away. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 105. e023_2_r：甲冑の亡霊→関わらずに先へ行く

保存名：`generated/e023_2_r.png`

- Scene: the hooded adventurer walks away down a ruined corridor while the ghost knight stands silently watching them go. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 106. e024_0_ok：コウモリの嵐→伏せてやり過ごす（成功）

保存名：`generated/e024_0_ok.png`

- Scene: the hooded adventurer lies flat on a cave floor as a storm of bats rushes overhead. Red only: the eyes of the nearest bats.
- Characters: the hooded adventurer

### 107. e024_0_ng：コウモリの嵐→伏せてやり過ごす（失敗）

保存名：`generated/e024_0_ng.png`

- Scene: the hooded adventurer clutches their head as bats swirl all around them in a cave. Red only: the eyes of the nearest bats.
- Characters: the hooded adventurer

### 108. e024_1_ok：コウモリの嵐→顔を庇って走り抜ける（成功）

保存名：`generated/e024_1_ok.png`

- Scene: the hooded adventurer runs through a swarm of bats with an arm shielding their face, unharmed. Red only: the eyes of the nearest bats.
- Characters: the hooded adventurer

### 109. e024_1_ng：コウモリの嵐→顔を庇って走り抜ける（失敗）

保存名：`generated/e024_1_ng.png`

- Scene: A swarm of bats tears at the hooded adventurer with claws and teeth; scratches on the arms. Red only: the scratches.
- Characters: the hooded adventurer

### 110. e024_2_r：コウモリの嵐→黒い犬に追い払わせる

保存名：`generated/e024_2_r.png`

- Scene: A thin black dog barks at a swarm of bats, which flees in all directions; the hooded adventurer stands behind it. Red only: the dog's one eye.
- Characters: the hooded adventurer

### 111. e024_3_ok：コウモリの嵐→群れが去った後の巣を漁る（成功）

保存名：`generated/e024_3_ok.png`

- Scene: the hooded adventurer digs in a heap of bat droppings on a cave floor and holds up a gemstone. Red only: the gemstone.
- Characters: the hooded adventurer

### 112. e024_3_ng：コウモリの嵐→群れが去った後の巣を漁る（失敗）

保存名：`generated/e024_3_ng.png`

- Scene: the hooded adventurer is ambushed by returning bats while digging in a cave nest. Red only: the eyes of the bats.
- Characters: the hooded adventurer

### 113. e025_0_ok：骸骨の賭博師→運命を賭ける（成功）

保存名：`generated/e025_0_ok.png`

- Scene: A skeleton gambler in a tricorn hat shrugs and pushes a pile of coins across the table toward the hooded adventurer. Red only: the dice on the table.
- Characters: the hooded adventurer

### 114. e025_0_ng：骸骨の賭博師→運命を賭ける（失敗）

保存名：`generated/e025_0_ng.png`

- Scene: A skeleton gambler grins as its eye sockets flash red across the table from the hooded adventurer. Red only: the skeleton's eye sockets.
- Characters: the hooded adventurer

### 115. e025_1_ok：骸骨の賭博師→イカサマを見破る（成功）

保存名：`generated/e025_1_ok.png`

- Scene: the hooded adventurer holds up a die showing six pips on every face; the skeleton gambler laughs and tosses a coin. Red only: the die.
- Characters: the hooded adventurer

### 116. e025_1_ng：骸骨の賭博師→イカサマを見破る（失敗）

保存名：`generated/e025_1_ng.png`

- Scene: the hooded adventurer slumps at a gambling table as the skeleton gambler sweeps up all the coins, laughing. Red only: the dice.
- Characters: the hooded adventurer

### 117. e025_2_r：骸骨の賭博師→断ってテーブルをひっくり返す

保存名：`generated/e025_2_r.png`

- Scene: A table is flipped over and a skeleton gambler has collapsed into scattered bones; the hooded adventurer gathers coins from the floor. Red only: the dice on the floor.
- Characters: the hooded adventurer

### 118. e026_0_ok：赤い扉→開けて中に入る（成功）

保存名：`generated/e026_0_ok.png`

- Scene: the hooded adventurer steps through an open red door into a corridor that leads far down a stairway. Red only: the door.
- Characters: the hooded adventurer

### 119. e026_0_ng：赤い扉→開けて中に入る（失敗）

保存名：`generated/e026_0_ng.png`

- Scene: Beyond an open red door lies a heap of corpses all wearing the same hooded cloak as the hooded adventurer, who recoils. Red only: the door frame.
- Characters: the hooded adventurer

### 120. e026_1_ok：赤い扉→ノックする（成功）

保存名：`generated/e026_1_ok.png`

- Scene: An old map is pushed out through the gap under a red door; the hooded adventurer bends to take it. Red only: the door.
- Characters: the hooded adventurer

### 121. e026_1_ng：赤い扉→ノックする（失敗）

保存名：`generated/e026_1_ng.png`

- Scene: A red door shakes violently as something pounds on it from inside; the hooded adventurer backs away. Red only: the door.
- Characters: the hooded adventurer

### 122. e026_2_r：赤い扉→見なかったことにする

保存名：`generated/e026_2_r.png`

- Scene: the hooded adventurer walks away down a grey corridor, glancing back at a red door that pulses. Red only: the door.
- Characters: the hooded adventurer

### 123. e027_0_ok：子守唄→一緒に歌う（成功）

保存名：`generated/e027_0_ok.png`

- Scene: the hooded adventurer stands by an ornate wooden cradle that has stopped rocking, a calm soft light filling the dark room. Red only: the carved crest on the cradle.
- Characters: the hooded adventurer

### 124. e027_0_ng：子守唄→一緒に歌う（失敗）

保存名：`generated/e027_0_ng.png`

- Scene: the hooded adventurer backs away from an ornate cradle as a pale shape stirs inside it, crying. Red only: the carved crest on the cradle.
- Characters: the hooded adventurer

### 125. e027_1_ok：子守唄→揺りかごを止める（成功）

保存名：`generated/e027_1_ok.png`

- Scene: the hooded adventurer holds a stilled cradle and finds coins hidden under its floorboard. Red only: the carved crest on the cradle.
- Characters: the hooded adventurer

### 126. e027_1_ng：子守唄→揺りかごを止める（失敗）

保存名：`generated/e027_1_ng.png`

- Scene: A small pale ghostly hand grips the hooded adventurer's wrist as they try to stop a rocking cradle. Red only: the carved crest on the cradle.
- Characters: the hooded adventurer

### 127. e027_3_r：子守唄→耳を塞いで通り抜ける

保存名：`generated/e027_3_r.png`

- Scene: the hooded adventurer walks through a dark room with hands pressed over their ears, a cradle rocking behind them. Red only: the carved crest on the cradle.
- Characters: the hooded adventurer

### 128. e028_0_r：泣く石像→体力を捧げる

保存名：`generated/e028_0_r.png`

- Scene: the hooded adventurer touches a veiled weeping stone statue, kneeling weakly, but with a calm, clear face. Red only: the statue's tears.
- Characters: the hooded adventurer

### 129. e028_1_r：泣く石像→心を捧げる

保存名：`generated/e028_1_r.png`

- Scene: the hooded adventurer stands stronger before a veiled weeping statue as a faint wisp of memory drifts from their head into the stone. Red only: the statue's tears.
- Characters: the hooded adventurer

### 130. e028_2_ok：泣く石像→涙を拭ってやる（成功）

保存名：`generated/e028_2_ok.png`

- Scene: The veiled stone statue's tears have stopped; a red amulet falls from its clasped hands into the hooded adventurer's palm. Red only: the amulet.
- Characters: the hooded adventurer

### 131. e028_2_ng：泣く石像→涙を拭ってやる（失敗）

保存名：`generated/e028_2_ng.png`

- Scene: the hooded adventurer stares at a stain burned into their fingers after wiping the veiled statue's tears. Red only: the stain on the fingers.
- Characters: the hooded adventurer

### 132. e029_0_ok：盗賊の待ち伏せ→戦う（成功）

保存名：`generated/e029_0_ok.png`

- Scene: the hooded adventurer stands over a defeated bandit in a cave, holding up the bandit's heavy purse. Red only: the bandit's scarf.
- Characters: the hooded adventurer

### 133. e029_0_ng：盗賊の待ち伏せ→戦う（失敗）

保存名：`generated/e029_0_ng.png`

- Scene: the hooded adventurer clutches their side, wounded, while a bandit runs off with their pack. Red only: the wound.
- Characters: the hooded adventurer

### 134. e029_1_ok：盗賊の待ち伏せ→言いくるめる（成功）

保存名：`generated/e029_1_ok.png`

- Scene: A bandit turns pale and runs away in fear as the hooded adventurer points down a dark tunnel. Red only: the bandit's scarf.
- Characters: the hooded adventurer

### 135. e029_1_ng：盗賊の待ち伏せ→言いくるめる（失敗）

保存名：`generated/e029_1_ng.png`

- Scene: A bandit punches the hooded adventurer in a cave. Red only: the bandit's scarf.
- Characters: the hooded adventurer

### 136. e029_2_r：盗賊の待ち伏せ→黒い犬をけしかける

保存名：`generated/e029_2_r.png`

- Scene: A black dog lunges at a bandit, who flees screaming and drops coins; the hooded adventurer stands behind. Red only: the bandit's scarf.
- Characters: the hooded adventurer

### 137. e029_3_r：盗賊の待ち伏せ→大人しく荷物を渡す

保存名：`generated/e029_3_r.png`

- Scene: the hooded adventurer hands over their pack to a bandit holding a dagger. Red only: the bandit's scarf.
- Characters: the hooded adventurer

### 138. e030_0_ok：水晶玉→未来を見届ける（成功）

保存名：`generated/e030_0_ok.png`

- Scene: the hooded adventurer stares into a crystal ball with resolve; inside it a tiny vision of death is shown clearly. Red only: a small pool of blood in the vision.
- Characters: the hooded adventurer

### 139. e030_0_ng：水晶玉→未来を見届ける（失敗）

保存名：`generated/e030_0_ng.png`

- Scene: the hooded adventurer kneels before a crystal ball showing endless visions of their own death, head in hands. Red only: blood in the visions.
- Characters: the hooded adventurer

### 140. e030_1_r：水晶玉→水晶玉を砕く

保存名：`generated/e030_1_r.png`

- Scene: A crystal ball shatters on the floor; the hooded adventurer stands among the glittering shards. Red only: one glowing shard.
- Characters: the hooded adventurer

### 141. e030_2_ok：水晶玉→水晶玉を持ち去る（成功）

保存名：`generated/e030_2_ok.png`

- Scene: the hooded adventurer wraps a glowing crystal ball in cloth and tucks it under their arm. Red only: a small red glint in the ball.
- Characters: the hooded adventurer

### 142. e030_2_ng：水晶玉→水晶玉を持ち去る（失敗）

保存名：`generated/e030_2_ng.png`

- Scene: A crystal ball cracks apart in the hooded adventurer's hands, shards piercing the palm. Red only: the cuts on the palm.
- Characters: the hooded adventurer

### 143. e031_0_ok：弔いの鐘→鐘を鳴らす（成功）

保存名：`generated/e031_0_ok.png`

- Scene: the hooded adventurer rings a huge bell in a ruined tower; rings of sound ripple out and dark wisps peel away from their body. Red only: the glow on the bell's rim.
- Characters: the hooded adventurer

### 144. e031_0_ng：弔いの鐘→鐘を鳴らす（失敗）

保存名：`generated/e031_0_ng.png`

- Scene: the hooded adventurer has rung a huge bell; in the darkness beyond the tower, giant eyes open. Red only: the eyes.
- Characters: the hooded adventurer

### 145. e031_1_ok：弔いの鐘→自分の名前を削り取る（成功）

保存名：`generated/e031_1_ok.png`

- Scene: the hooded adventurer scrapes at the rim of a huge bell with a knife, shoulders relaxing. Red only: the glow on the bell's rim.
- Characters: the hooded adventurer

### 146. e031_1_ng：弔いの鐘→自分の名前を削り取る（失敗）

保存名：`generated/e031_1_ng.png`

- Scene: the hooded adventurer scrapes at a bell's rim but the glowing mark keeps reappearing. Red only: the glowing mark.
- Characters: the hooded adventurer

### 147. e031_2_r：弔いの鐘→静かに通り過ぎる

保存名：`generated/e031_2_r.png`

- Scene: the hooded adventurer walks away from a ruined bell tower as the bell swings once behind them. Red only: the glow on the bell's rim.
- Characters: the hooded adventurer

### 148. e032_0_ok：岩に刺さった剣→渾身の力で引き抜く（成功）

保存名：`generated/e032_0_ok.png`

- Scene: the hooded adventurer pulls a shining silver sword free from a rock with a burst of light, skeletons around the rock. Red only: the gem in the sword's pommel.
- Characters: the hooded adventurer

### 149. e032_0_ng：岩に刺さった剣→渾身の力で引き抜く（失敗）

保存名：`generated/e032_0_ng.png`

- Scene: the hooded adventurer strains at a sword stuck fast in a rock; the skeletons around seem to grin. Red only: the gem in the sword's pommel.
- Characters: the hooded adventurer

### 150. e032_1_ok：岩に刺さった剣→運命に任せて引き抜く（成功）

保存名：`generated/e032_1_ok.png`

- Scene: A silver sword slides easily from a rock into the hooded adventurer's hand as if it was waiting. Red only: the gem in the pommel.
- Characters: the hooded adventurer

### 151. e032_1_ng：岩に刺さった剣→運命に任せて引き抜く（失敗）

保存名：`generated/e032_1_ng.png`

- Scene: A sword crumbles into sand in the hooded adventurer's hand, a black bruise spreading across the palm. Red only: the gem falling with the sand.
- Characters: the hooded adventurer

### 152. e032_2_r：岩に刺さった剣→骸骨たちの持ち物を漁る

保存名：`generated/e032_2_r.png`

- Scene: the hooded adventurer kneels among skeletons around a sword in a rock, gathering coins and a dirty rope. Red only: the gem in the sword's pommel.
- Characters: the hooded adventurer

### 153. n06_0_ok：迷宮の中の街角→窓を覗く（成功）

保存名：`generated/n06_0_ok.png`

- Scene: Through a window on a colourless city street corner, a family sits around a dinner table; the hooded adventurer peers in from outside. Red only: the flame of the street lamp.
- Characters: the hooded adventurer

### 154. n06_0_ng：迷宮の中の街角→窓を覗く（失敗）

保存名：`generated/n06_0_ng.png`

- Scene: Through a window, a figure inside has turned toward the hooded adventurer; it has no face. Red only: the flame of the street lamp.
- Characters: the hooded adventurer

### 155. n06_1_r：迷宮の中の街角→走り書きの続きを読む

保存名：`generated/n06_1_r.png`

- Scene: the hooded adventurer reads a scrawled message on a wall under a street lamp; the scrawl is illegible scratches. Red only: the flame of the street lamp.
- Characters: the hooded adventurer

### 156. n06_2_r：迷宮の中の街角→街灯の火をもらう

保存名：`generated/n06_2_r.png`

- Scene: the hooded adventurer lights a torch from a street lamp; the new flame burns oddly white. Red only: the street lamp's flame.
- Characters: the hooded adventurer

### 157. g025_1_r：骨の門番→聖水を浴びせる

保存名：`generated/g025_1_r.png`

- Scene: A colossal gate of bones smokes and crumbles where holy water splashes on it; the hooded adventurer holds an empty vial. Red only: the dying glow in the great skull's eyes.
- Characters: the hooded adventurer

### 158. g025_2_ok：骨の門番→門をよじ登って越える（成功）

保存名：`generated/g025_2_ok.png`

- Scene: the hooded adventurer climbs over the top of a colossal gate of bones, kicking away grasping skeletal hands. Red only: the glow in the great skull's eyes.
- Characters: the hooded adventurer

### 159. g025_2_ng：骨の門番→門をよじ登って越える（失敗）

保存名：`generated/g025_2_ng.png`

- Scene: Countless skeletal hands drag the hooded adventurer down from a gate of bones. Red only: the glow in the great skull's eyes.
- Characters: the hooded adventurer

### 160. g025_3_ok：骨の門番→門と問答する（成功）

保存名：`generated/g025_3_ok.png`

- Scene: A colossal gate of bones unravels, its bones parting to open a path before the hooded adventurer. Red only: the glow in the great skull's eyes.
- Characters: the hooded adventurer

### 161. g025_3_ng：骨の門番→門と問答する（失敗）

保存名：`generated/g025_3_ng.png`

- Scene: the hooded adventurer kneels before a gate of bones as faint wisps of memory are drawn from their head into the great skull. Red only: the skull's eyes.
- Characters: the hooded adventurer

### 162. g025_4_r：骨の門番→通行料として運を払う

保存名：`generated/g025_4_r.png`

- Scene: A gate of bones creaks open; the hooded adventurer walks through, a faint glow drained from their body. Red only: the great skull's eyes.
- Characters: the hooded adventurer

### 163. e033_0_ok：納骨堂→骨の山を漁る（成功）

保存名：`generated/e033_0_ok.png`

- Scene: the hooded adventurer digs among skulls in an ossuary and holds up old coins. Red only: one skull's eye sockets.
- Characters: the hooded adventurer

### 164. e033_0_ng：納骨堂→骨の山を漁る（失敗）

保存名：`generated/e033_0_ng.png`

- Scene: A wall of skulls collapses onto the hooded adventurer, half burying them. Red only: one skull's eye sockets.
- Characters: the hooded adventurer

### 165. e033_1_r：納骨堂→死者に祈りを捧げる

保存名：`generated/e033_1_r.png`

- Scene: the hooded adventurer kneels in prayer in an ossuary; the screaming skulls around have begun to close their jaws. Red only: one skull's eye sockets.
- Characters: the hooded adventurer

### 166. e033_2_ok：納骨堂→息を止めて走り抜ける（成功）

保存名：`generated/e033_2_ok.png`

- Scene: the hooded adventurer sprints through an ossuary corridor holding their breath. Red only: one skull's eye sockets.
- Characters: the hooded adventurer

### 167. e033_2_ng：納骨堂→息を止めて走り抜ける（失敗）

保存名：`generated/e033_2_ng.png`

- Scene: the hooded adventurer slips and falls into a pile of skulls in an ossuary. Red only: one skull's eye sockets.
- Characters: the hooded adventurer

### 168. e034_0_r：さまよう亡霊→聖水で浄化する

保存名：`generated/e034_0_r.png`

- Scene: A faceless ghost dissolves with a sigh in a mist of holy water; a silver ring drops to the floor before the hooded adventurer. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 169. e034_1_ok：さまよう亡霊→一緒に死に場所を探す（成功）

保存名：`generated/e034_1_ok.png`

- Scene: A faceless ghost lies down peacefully over its own bones in a crypt niche while the hooded adventurer watches. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 170. e034_1_ng：さまよう亡霊→一緒に死に場所を探す（失敗）

保存名：`generated/e034_1_ng.png`

- Scene: A faceless ghost wraps itself around the hooded adventurer, who shivers, frost on their cloak. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 171. e034_2_ok：さまよう亡霊→気配を消してやり過ごす（成功）

保存名：`generated/e034_2_ok.png`

- Scene: A faceless ghost passes straight through the hooded adventurer, who stands still and calm. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 172. e034_2_ng：さまよう亡霊→気配を消してやり過ごす（失敗）

保存名：`generated/e034_2_ng.png`

- Scene: A faceless ghost passes through the hooded adventurer, pulling a faint glowing wisp out of their chest. Red only: the ribbon on the ghost's wrist.
- Characters: the hooded adventurer

### 173. e035_0_ok：釘打たれた棺→棺を開ける（成功）

保存名：`generated/e035_0_ok.png`

- Scene: An opened black coffin holds a dried noble corpse wearing a jewelled necklace; the hooded adventurer leans in. Red only: the jewels of the necklace.
- Characters: the hooded adventurer

### 174. e035_0_ng：釘打たれた棺→棺を開ける（失敗）

保存名：`generated/e035_0_ng.png`

- Scene: A white arm shoots out of a nailed coffin and grips the hooded adventurer's throat. Red only: the blood smear on the lid.
- Characters: the hooded adventurer

### 175. e035_1_ok：釘打たれた棺→釘をさらに打ち込む（成功）

保存名：`generated/e035_1_ok.png`

- Scene: the hooded adventurer hammers another nail into a black coffin; the scratching has stopped. Red only: the blood smear on the lid.
- Characters: the hooded adventurer

### 176. e035_1_ng：釘打たれた棺→釘をさらに打ち込む（失敗）

保存名：`generated/e035_1_ng.png`

- Scene: A nail springs back out of a coffin and cuts the hooded adventurer's cheek. Red only: the cut on the cheek.
- Characters: the hooded adventurer

### 177. e035_2_ok：釘打たれた棺→棺に話しかける（成功）

保存名：`generated/e035_2_ok.png`

- Scene: the hooded adventurer leans close to a nailed coffin, listening; a crack of light shows a hidden passage in the wall. Red only: the blood smear on the lid.
- Characters: the hooded adventurer

### 178. e035_2_ng：釘打たれた棺→棺に話しかける（失敗）

保存名：`generated/e035_2_ng.png`

- Scene: the hooded adventurer recoils from a nailed coffin, from which their own voice answered. Red only: the blood smear on the lid.
- Characters: the hooded adventurer

### 179. e036_0_ok：水没した回廊→泳いで渡る（成功）

保存名：`generated/e036_0_ok.png`

- Scene: the hooded adventurer climbs out of black water onto the far end of a flooded corridor, dripping. Red only: the eye of the shape beneath the water.
- Characters: the hooded adventurer

### 180. e036_0_ng：水没した回廊→泳いで渡る（失敗）

保存名：`generated/e036_0_ng.png`

- Scene: the hooded adventurer struggles in black water as a long serpent-like shape coils around their leg. Red only: the shape's eye.
- Characters: the hooded adventurer

### 181. e036_1_r：水没した回廊→ロープを渡して進む

保存名：`generated/e036_1_r.png`

- Scene: the hooded adventurer crosses a flooded corridor on a rope strung between pillars, above the black water. Red only: the eye of the shape beneath the water.
- Characters: the hooded adventurer

### 182. e036_2_ok：水没した回廊→水が引くのを待つ（成功）

保存名：`generated/e036_2_ok.png`

- Scene: the hooded adventurer stands in a corridor whose black water has drained away, puddles left on the stones. Red only: a small red glint in a puddle.
- Characters: the hooded adventurer

### 183. e036_2_ng：水没した回廊→水が引くのを待つ（失敗）

保存名：`generated/e036_2_ng.png`

- Scene: the hooded adventurer waits shivering in chest-deep black water in the dark. Red only: the eye of the shape beneath the water.
- Characters: the hooded adventurer

### 184. e037_1_r：渡し守→思い出を一つ払う

保存名：`generated/e037_1_r.png`

- Scene: the hooded adventurer sits in a small boat on a black lake, eyes empty, as a faint memory image of a village drifts away over the water. Red only: the lantern at the bow.
- Characters: the hooded adventurer

### 185. e037_2_ok：渡し守→渡し守を突き落として舟を奪う（成功）

保存名：`generated/e037_2_ok.png`

- Scene: the hooded adventurer rows a stolen boat across a black lake while pale hands reach up from the water behind. Red only: the lantern at the bow.
- Characters: the hooded adventurer

### 186. e037_2_ng：渡し守→渡し守を突き落として舟を奪う（失敗）

保存名：`generated/e037_2_ng.png`

- Scene: the hooded adventurer drags themselves soaking wet onto a lake shore, the ferryman standing in his boat behind. Red only: the lantern at the bow.
- Characters: the hooded adventurer

### 187. e037_3_r：渡し守→湖岸を歩いて回り込む

保存名：`generated/e037_3_r.png`

- Scene: the hooded adventurer walks a long underground lakeshore path in mist, small in the frame. Red only: the distant boat's lantern.
- Characters: the hooded adventurer

### 188. e038_0_ok：屍喰らい→先手を取って斬りかかる（成功）

保存名：`generated/e038_0_ok.png`

- Scene: the hooded adventurer stands over a beheaded ghoul in a crypt, sword lowered. Red only: the blood on the ghoul.
- Characters: the hooded adventurer

### 189. e038_0_ng：屍喰らい→先手を取って斬りかかる（失敗）

保存名：`generated/e038_0_ng.png`

- Scene: A ghoul's claws slash the hooded adventurer's arm in a crypt. Red only: the wound.
- Characters: the hooded adventurer

### 190. e038_1_r：屍喰らい→銀の剣を抜く

保存名：`generated/e038_1_r.png`

- Scene: A ghoul shrinks back from the gleam of a silver sword held by the hooded adventurer and flees. Red only: the blood on the ghoul's mouth.
- Characters: the hooded adventurer

### 191. e038_2_ok：屍喰らい→死骸を差し出して後ずさる（成功）

保存名：`generated/e038_2_ok.png`

- Scene: A ghoul returns to its meal while the hooded adventurer backs quietly away. Red only: the blood on the ghoul's hands.
- Characters: the hooded adventurer

### 192. e038_2_ng：屍喰らい→死骸を差し出して後ずさる（失敗）

保存名：`generated/e038_2_ng.png`

- Scene: A ghoul leaps at the hooded adventurer the moment they look away. Red only: the blood on the ghoul's mouth.
- Characters: the hooded adventurer

### 193. e039_0_r：沼の魔女→取引に応じる

保存名：`generated/e039_0_r.png`

- Scene: A swamp witch presses a glowing finger to the hooded adventurer's neck, burning a mark. Red only: the mark on the neck.
- Characters: the hooded adventurer

### 194. e039_1_r：沼の魔女→薬だけ売ってもらう

保存名：`generated/e039_1_r.png`

- Scene: A swamp witch counts coins and hands the hooded adventurer a small potion bottle. Red only: the liquid in the cauldron.
- Characters: the hooded adventurer

### 195. e039_2_ok：沼の魔女→鍋をひっくり返して逃げる（成功）

保存名：`generated/e039_2_ok.png`

- Scene: the hooded adventurer flees a cave hut as a cauldron tips over behind them and the witch shrieks. Red only: the spilled liquid.
- Characters: the hooded adventurer

### 196. e039_2_ng：沼の魔女→鍋をひっくり返して逃げる（失敗）

保存名：`generated/e039_2_ng.png`

- Scene: A witch's curse, a dark streak of light, strikes the hooded adventurer in the back as they flee. Red only: the curse.
- Characters: the hooded adventurer

### 197. e040_0_ok：囁く人形→遊んであげる（成功）

保存名：`generated/e040_0_ok.png`

- Scene: A porcelain doll sits still on a chair, a coin in its hand; the hooded adventurer sits on the floor beside it. Red only: the doll's lips.
- Characters: the hooded adventurer

### 198. e040_0_ng：囁く人形→遊んであげる（失敗）

保存名：`generated/e040_0_ng.png`

- Scene: the hooded adventurer sits exhausted on the floor before a porcelain doll, in a room that seems to stretch. Red only: the doll's lips.
- Characters: the hooded adventurer

### 199. e040_1_ok：囁く人形→人形を叩き壊す（成功）

保存名：`generated/e040_1_ok.png`

- Scene: A porcelain doll lies shattered on the floor, dried flower petals spilling from inside; the hooded adventurer stands over it. Red only: the petals.
- Characters: the hooded adventurer

### 200. e040_1_ng：囁く人形→人形を叩き壊す（失敗）

保存名：`generated/e040_1_ng.png`

- Scene: Shards of a broken porcelain doll crawl up the hooded adventurer's fingers, cutting them. Red only: the cuts.
- Characters: the hooded adventurer
