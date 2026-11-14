# Codex 向け作業指示：画像345枚の一括生成（元画像のみ）

ゲーム「三択ダンジョン」のイベント画像の元絵を、下の345枚分、まとめて生成してください。
減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**

## ルール

1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。
2. 各画像のプロンプトは、下の「プロンプトの組み立て方」どおりに組み立て、**一字一句そのまま**使う。書き換え・要約・翻訳はしない。
3. サイズは横長の **1536×1024**（3:2）。
4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/e040_2_r.png`）。
5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。
6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。
7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。
8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK e040_2_r」のように1枚1行の短い報告だけにする。
9. 345枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。クラウド環境で作業している場合は、`generated/` の PNG を **`stills_set6.zip`** にまとめてダウンロードできる形で出力する（自分のPCで作業している場合は zip は不要）。

## 画像リスト（345枚）

| # | name | 内容 |
| --- | --- | --- |
| 1 | `e040_2_r` | 囁く人形→人形を後ろ向きにして去る |
| 2 | `e041_0_ok` | 肖像画の回廊→絵の自分に触れる（成功） |
| 3 | `e041_0_ng` | 肖像画の回廊→絵の自分に触れる（失敗） |
| 4 | `e041_1_r` | 肖像画の回廊→絵を切り裂く |
| 5 | `e041_2_ok` | 肖像画の回廊→額縁を外して持ち去る（成功） |
| 6 | `e041_2_ng` | 肖像画の回廊→額縁を外して持ち去る（失敗） |
| 7 | `e042_0_ok` | 朽ちた吊り橋→慎重に渡る（成功） |
| 8 | `e042_0_ng` | 朽ちた吊り橋→慎重に渡る（失敗） |
| 9 | `e042_1_ok` | 朽ちた吊り橋→一気に駆け抜ける（成功） |
| 10 | `e042_1_ng` | 朽ちた吊り橋→一気に駆け抜ける（失敗） |
| 11 | `e042_2_r` | 朽ちた吊り橋→ロープで体を繋いで渡る |
| 12 | `e042_3_ok` | 朽ちた吊り橋→裂け目へ飛び降りる（成功） |
| 13 | `e042_3_ng` | 朽ちた吊り橋→裂け目へ飛び降りる（失敗） |
| 14 | `e043_0_ok` | 錬金術師の工房→赤い薬を飲む（成功） |
| 15 | `e043_0_ng` | 錬金術師の工房→赤い薬を飲む（失敗） |
| 16 | `e043_1_ok` | 錬金術師の工房→白い薬を飲む（成功） |
| 17 | `e043_1_ng` | 錬金術師の工房→白い薬を飲む（失敗） |
| 18 | `e043_2_ok` | 錬金術師の工房→黒い薬を飲む（成功） |
| 19 | `e043_2_ng` | 錬金術師の工房→黒い薬を飲む（失敗） |
| 20 | `e044_0_ok` | 死者の宴→席に着いて食べる（成功） |
| 21 | `e044_0_ng` | 死者の宴→席に着いて食べる（失敗） |
| 22 | `e044_1_ok` | 死者の宴→乾杯の音頭を取る（成功） |
| 23 | `e044_1_ng` | 死者の宴→乾杯の音頭を取る（失敗） |
| 24 | `e044_2_r` | 死者の宴→丁重に辞退する |
| 25 | `e045_1_r` | 薄れゆく亡霊→最後の戦いの話を聞く |
| 26 | `e045_2_r` | 薄れゆく亡霊→安らかに眠らせる |
| 27 | `e046_1_ng` | 少女の墓→墓を掘り起こす（失敗） |
| 28 | `e047_0_ok` | 鎖の囚人→男の願いを聞く（成功） |
| 29 | `e047_0_ng` | 鎖の囚人→男の願いを聞く（失敗） |
| 30 | `e047_1_r` | 鎖の囚人→鍵で鎖を外す |
| 31 | `e047_2_r` | 鎖の囚人→放っておく |
| 32 | `e048_0_ok` | 牢番→背後から鍵束を盗む（成功） |
| 33 | `e048_0_ng` | 牢番→背後から鍵束を盗む（失敗） |
| 34 | `e048_1_ok` | 牢番→正面から倒す（成功） |
| 35 | `e048_1_ng` | 牢番→正面から倒す（失敗） |
| 36 | `e048_2_ok` | 牢番→囚人のふりをしてやり過ごす（成功） |
| 37 | `e048_2_ng` | 牢番→囚人のふりをしてやり過ごす（失敗） |
| 38 | `e049_0_ok` | 蝋燭の道→蝋燭を消さないよう慎重に進む（成功） |
| 39 | `e049_0_ng` | 蝋燭の道→蝋燭を消さないよう慎重に進む（失敗） |
| 40 | `e049_1_r` | 蝋燭の道→一本持っていく |
| 41 | `e049_2_ok` | 蝋燭の道→全部吹き消す（成功） |
| 42 | `e049_2_ng` | 蝋燭の道→全部吹き消す（失敗） |
| 43 | `e049_3_r` | 蝋燭の道→足早に通り抜ける |
| 44 | `e050_0_ok` | 闇の中の目→目を見つめ返す（成功） |
| 45 | `e050_0_ng` | 闇の中の目→目を見つめ返す（失敗） |
| 46 | `e050_1_r` | 闇の中の目→第三の眼で見返す |
| 47 | `e050_2_ok` | 闇の中の目→視線から逃げる（成功） |
| 48 | `e050_2_ng` | 闇の中の目→視線から逃げる（失敗） |
| 49 | `e051_0_ok` | 地図職人の亡骸→地図を持っていく（成功） |
| 50 | `e051_0_ng` | 地図職人の亡骸→地図を持っていく（失敗） |
| 51 | `e051_1_ok` | 地図職人の亡骸→地図を描き足してやる（成功） |
| 52 | `e051_1_ng` | 地図職人の亡骸→地図を描き足してやる（失敗） |
| 53 | `e051_2_r` | 地図職人の亡骸→男のポケットを探る |
| 54 | `e052_0_ok` | 禁書庫→暴れる本を読む（成功） |
| 55 | `e052_0_ng` | 禁書庫→暴れる本を読む（失敗） |
| 56 | `e052_1_r` | 禁書庫→本を焼き払う |
| 57 | `e052_2_ok` | 禁書庫→静かな本を一冊選ぶ（成功） |
| 58 | `e052_2_ng` | 禁書庫→静かな本を一冊選ぶ（失敗） |
| 59 | `e053_0_ok` | 湖の歌声→耳を塞いで立ち去る（成功） |
| 60 | `e053_0_ng` | 湖の歌声→耳を塞いで立ち去る（失敗） |
| 61 | `e053_1_ok` | 湖の歌声→歌に合わせて歌い返す（成功） |
| 62 | `e053_1_ng` | 湖の歌声→歌に合わせて歌い返す（失敗） |
| 63 | `e053_2_ok` | 湖の歌声→湖に飛び込む（成功） |
| 64 | `e053_2_ng` | 湖の歌声→湖に飛び込む（失敗） |
| 65 | `e054_0_ok` | 死神の賭け→命を賭けて挑む（成功） |
| 66 | `e054_0_ng` | 死神の賭け→命を賭けて挑む（失敗） |
| 67 | `e054_1_ok` | 死神の賭け→知略で挑む（成功） |
| 68 | `e054_1_ng` | 死神の賭け→知略で挑む（失敗） |
| 69 | `e054_2_ok` | 死神の賭け→盤をひっくり返して逃げる（成功） |
| 70 | `e054_2_ng` | 死神の賭け→盤をひっくり返して逃げる（失敗） |
| 71 | `e055_0_ok` | 蛆の床→死骸を踏み越えて進む（成功） |
| 72 | `e055_0_ng` | 蛆の床→死骸を踏み越えて進む（失敗） |
| 73 | `e055_1_r` | 蛆の床→火を放つ |
| 74 | `e055_2_ok` | 蛆の床→目を閉じて走り抜ける（成功） |
| 75 | `e055_2_ng` | 蛆の床→目を閉じて走り抜ける（失敗） |
| 76 | `e056_0_r` | メモの続き→続きを読む |
| 77 | `e056_1_r` | メモの続き→挟まれた押し花を手に取る |
| 78 | `e056_2_r` | メモの続き→メモを置いて先を急ぐ |
| 79 | `e057_0_r` | 喰らう扉→薬瓶を食わせる |
| 80 | `e057_1_ok` | 喰らう扉→腕を差し出す（成功） |
| 81 | `e057_1_ng` | 喰らう扉→腕を差し出す（失敗） |
| 82 | `e057_2_ok` | 喰らう扉→扉をこじ開ける（成功） |
| 83 | `e057_2_ng` | 喰らう扉→扉をこじ開ける（失敗） |
| 84 | `e057_3_r` | 喰らう扉→別の道を探す |
| 85 | `g050_0_r` | 都市の番人→銀の剣で炉心を貫く |
| 86 | `g050_2_ok` | 都市の番人→足元をすり抜ける（成功） |
| 87 | `g050_2_ng` | 都市の番人→足元をすり抜ける（失敗） |
| 88 | `g050_3_ok` | 都市の番人→正面から打ち倒す（成功） |
| 89 | `g050_3_ng` | 都市の番人→正面から打ち倒す（失敗） |
| 90 | `g050_4_ok` | 都市の番人→市民になりすます（成功） |
| 91 | `g050_4_ng` | 都市の番人→市民になりすます（失敗） |
| 92 | `e058_0_ok` | 胞子の森→布で口を覆って進む（成功） |
| 93 | `e058_0_ng` | 胞子の森→布で口を覆って進む（失敗） |
| 94 | `e058_1_ok` | 胞子の森→笑い声の方へ行く（成功） |
| 95 | `e058_1_ng` | 胞子の森→笑い声の方へ行く（失敗） |
| 96 | `e058_2_r` | 胞子の森→森を焼き払う |
| 97 | `e059_0_ok` | 地下都市の大通り→家の中を探索する（成功） |
| 98 | `e059_0_ng` | 地下都市の大通り→家の中を探索する（失敗） |
| 99 | `e059_1_ok` | 地下都市の大通り→大通りを堂々と歩く（成功） |
| 100 | `e059_1_ng` | 地下都市の大通り→大通りを堂々と歩く（失敗） |
| 101 | `e059_2_ok` | 地下都市の大通り→裏路地を抜ける（成功） |
| 102 | `e059_2_ng` | 地下都市の大通り→裏路地を抜ける（失敗） |
| 103 | `e060_0_ok` | 王の亡骸→王冠を奪う（成功） |
| 104 | `e060_0_ng` | 王の亡骸→王冠を奪う（失敗） |
| 105 | `e060_1_ok` | 王の亡骸→跪いて臣従を誓う（成功） |
| 106 | `e060_1_ng` | 王の亡骸→跪いて臣従を誓う（失敗） |
| 107 | `e060_2_r` | 王の亡骸→玉座の裏の宝物庫を探す |
| 108 | `e061_0_r` | 蛾の女王→たいまつを差し出す |
| 109 | `e061_1_r` | 蛾の女王→命の光を分け与える |
| 110 | `e061_2_ok` | 蛾の女王→羽を斬り落とす（成功） |
| 111 | `e061_2_ng` | 蛾の女王→羽を斬り落とす（失敗） |
| 112 | `e062_0_ok` | 菌糸の人→誘いを受け入れる(ふりをする)（成功） |
| 113 | `e062_0_ng` | 菌糸の人→誘いを受け入れる(ふりをする)（失敗） |
| 114 | `e062_1_r` | 菌糸の人→焼き払う |
| 115 | `e062_2_ok` | 菌糸の人→殴り倒す（成功） |
| 116 | `e062_2_ng` | 菌糸の人→殴り倒す（失敗） |
| 117 | `e063_0_ok` | 逆さ時計の塔→扉に入る（成功） |
| 118 | `e063_0_ng` | 逆さ時計の塔→扉に入る（失敗） |
| 119 | `e063_1_ok` | 逆さ時計の塔→時計の針を止める（成功） |
| 120 | `e063_1_ng` | 逆さ時計の塔→時計の針を止める（失敗） |
| 121 | `e063_2_ok` | 逆さ時計の塔→針を正しい向きに直す（成功） |
| 122 | `e063_2_ng` | 逆さ時計の塔→針を正しい向きに直す（失敗） |
| 123 | `e064_0_ok` | 黒い聖堂→影と共に祈る（成功） |
| 124 | `e064_0_ng` | 黒い聖堂→影と共に祈る（失敗） |
| 125 | `e064_1_ok` | 黒い聖堂→黒い炎に手をかざす（成功） |
| 126 | `e064_1_ng` | 黒い聖堂→黒い炎に手をかざす（失敗） |
| 127 | `e064_2_r` | 黒い聖堂→聖水で炎を消す |
| 128 | `e065_0_ok` | 双子の扉→「真実」の扉を開ける（成功） |
| 129 | `e065_0_ng` | 双子の扉→「真実」の扉を開ける（失敗） |
| 130 | `e065_1_ok` | 双子の扉→「嘘」の扉を開ける（成功） |
| 131 | `e065_1_ng` | 双子の扉→「嘘」の扉を開ける（失敗） |
| 132 | `e065_2_ok` | 双子の扉→双子に問いかける（成功） |
| 133 | `e065_2_ng` | 双子の扉→双子に問いかける（失敗） |
| 134 | `e066_0_ok` | 竜の骨→宝の山に潜り込む（成功） |
| 135 | `e066_0_ng` | 竜の骨→宝の山に潜り込む（失敗） |
| 136 | `e066_1_ok` | 竜の骨→竜の牙を削り取る（成功） |
| 137 | `e066_1_ng` | 竜の骨→竜の牙を削り取る（失敗） |
| 138 | `e066_2_r` | 竜の骨→骨の前で黙祷する |
| 139 | `e067_0_ok` | 影の自分→影と戦う（成功） |
| 140 | `e067_0_ng` | 影の自分→影と戦う（失敗） |
| 141 | `e067_1_ok` | 影の自分→影を受け入れる（成功） |
| 142 | `e067_1_ng` | 影の自分→影を受け入れる（失敗） |
| 143 | `e067_2_r` | 影の自分→影を光で消し去る |
| 144 | `e068_0_r` | 仮面の商人→金貨で薬を買う |
| 145 | `e068_1_r` | 仮面の商人→顔の一部と引き換えに力を買う |
| 146 | `e068_2_ok` | 仮面の商人→商人の仮面を一枚剥がす（成功） |
| 147 | `e068_2_ng` | 仮面の商人→商人の仮面を一枚剥がす（失敗） |
| 148 | `e069_0_ok` | 脈打つ卵→孵る前に壊す（成功） |
| 149 | `e069_0_ng` | 脈打つ卵→孵る前に壊す（失敗） |
| 150 | `e069_1_ok` | 脈打つ卵→孵るのを見届ける（成功） |
| 151 | `e069_1_ng` | 脈打つ卵→孵るのを見届ける（失敗） |
| 152 | `e069_2_r` | 脈打つ卵→そっと離れる |
| 153 | `e070_0_ok` | 亡者の行進→隊列に紛れ込む（成功） |
| 154 | `e070_0_ng` | 亡者の行進→隊列に紛れ込む（失敗） |
| 155 | `e070_1_r` | 亡者の行進→騎士の誓いを示す |
| 156 | `e070_2_ok` | 亡者の行進→物陰に隠れる（成功） |
| 157 | `e070_2_ng` | 亡者の行進→物陰に隠れる（失敗） |
| 158 | `e071_0_r` | 魔女の再訪→印を返す |
| 159 | `e071_1_r` | 魔女の再訪→薬の調合を頼む |
| 160 | `e071_2_ok` | 魔女の再訪→迷宮の底について訊く（成功） |
| 161 | `e071_2_ng` | 魔女の再訪→迷宮の底について訊く（失敗） |
| 162 | `e072_1_r` | 最後のメモ→メモを胸に抱く |
| 163 | `e072_2_r` | 最後のメモ→破り捨てる |
| 164 | `e073_0_ok` | 沈黙の司書→筆談で道を尋ねる（成功） |
| 165 | `e073_0_ng` | 沈黙の司書→筆談で道を尋ねる（失敗） |
| 166 | `e073_1_ok` | 沈黙の司書→音を立てずに本を盗む（成功） |
| 167 | `e073_1_ng` | 沈黙の司書→音を立てずに本を盗む（失敗） |
| 168 | `e073_2_ok` | 沈黙の司書→静かに通り抜ける（成功） |
| 169 | `e073_2_ng` | 沈黙の司書→静かに通り抜ける（失敗） |
| 170 | `e074_0_ok` | 血の泉→泉の血を飲む（成功） |
| 171 | `e074_0_ng` | 血の泉→泉の血を飲む（失敗） |
| 172 | `e074_1_r` | 血の泉→傷口を泉に浸す |
| 173 | `e074_2_r` | 血の泉→泉に聖水を注ぐ |
| 174 | `e075_0_ok` | 吊るされた人々→助け下ろす（成功） |
| 175 | `e075_0_ng` | 吊るされた人々→助け下ろす（失敗） |
| 176 | `e075_1_ok` | 吊るされた人々→せめて楽にしてやる（成功） |
| 177 | `e075_1_ng` | 吊るされた人々→せめて楽にしてやる（失敗） |
| 178 | `e075_2_r` | 吊るされた人々→見なかったことにする |
| 179 | `e076_0_ok` | 忘却の川→一口だけ飲む（成功） |
| 180 | `e076_0_ng` | 忘却の川→一口だけ飲む（失敗） |
| 181 | `e076_1_r` | 忘却の川→記憶を一つ川に流す |
| 182 | `e076_2_ok` | 忘却の川→川を渡る（成功） |
| 183 | `e076_2_ng` | 忘却の川→川を渡る（失敗） |
| 184 | `e077_0_ok` | 鉄の処女→扉を開ける（成功） |
| 185 | `e077_0_ng` | 鉄の処女→扉を開ける（失敗） |
| 186 | `e077_1_ok` | 鉄の処女→歌声に耳を傾ける（成功） |
| 187 | `e077_1_ng` | 鉄の処女→歌声に耳を傾ける（失敗） |
| 188 | `e077_2_ok` | 鉄の処女→部屋の拷問具を壊して回る（成功） |
| 189 | `e077_2_ng` | 鉄の処女→部屋の拷問具を壊して回る（失敗） |
| 190 | `e078_0_ok` | 眠る巨人→荷物を回収する（成功） |
| 191 | `e078_0_ng` | 眠る巨人→荷物を回収する（失敗） |
| 192 | `e078_1_ok` | 眠る巨人→喉の奥へ進む（成功） |
| 193 | `e078_1_ng` | 眠る巨人→喉の奥へ進む（失敗） |
| 194 | `e078_2_ok` | 眠る巨人→息を潜めて口から出る（成功） |
| 195 | `e078_2_ng` | 眠る巨人→息を潜めて口から出る（失敗） |
| 196 | `e079_1_r` | 少女の記憶→手を握ってやる |
| 197 | `e079_2_r` | 少女の記憶→先を急ぐ |
| 198 | `n01_0_ok` | 王の命令書→布告を最後まで読む（成功） |
| 199 | `n01_0_ng` | 王の命令書→布告を最後まで読む（失敗） |
| 200 | `n01_1_r` | 王の命令書→封蝋を剥がして持ち帰る |
| 201 | `n01_2_r` | 王の命令書→布告を破り捨てる |
| 202 | `n02_0_r` | 隔離塔→少女の手を握る |
| 203 | `n02_2_r` | 隔離塔→寝台を整える |
| 204 | `n02_3_r` | 隔離塔→塔に入らず立ち去る |
| 205 | `n03_0_r` | 騎士の告白→話を聞く |
| 206 | `n03_1_ng` | 騎士の告白→「あなたのせいではない」と言う（失敗） |
| 207 | `n03_2_r` | 騎士の告白→黙って隣に立つ |
| 208 | `g075_2_ok` | 深淵の竜→竜の背に飛び乗る（成功） |
| 209 | `g075_2_ng` | 深淵の竜→竜の背に飛び乗る（失敗） |
| 210 | `g075_3_ok` | 深淵の竜→竜の怒りを鎮める（成功） |
| 211 | `g075_3_ng` | 深淵の竜→竜の怒りを鎮める（失敗） |
| 212 | `g075_4_ok` | 深淵の竜→影に紛れて裂溝を降りる（成功） |
| 213 | `g075_4_ng` | 深淵の竜→影に紛れて裂溝を降りる（失敗） |
| 214 | `e080_0_ok` | 肉の回廊→肉を切り裂いて近道を作る（成功） |
| 215 | `e080_0_ng` | 肉の回廊→肉を切り裂いて近道を作る（失敗） |
| 216 | `e080_1_ok` | 肉の回廊→心音に合わせて歩く（成功） |
| 217 | `e080_1_ng` | 肉の回廊→心音に合わせて歩く（失敗） |
| 218 | `e080_2_r` | 肉の回廊→何も考えずに進む |
| 219 | `e081_0_r` | 眼の群れ→第三の眼で睨み返す |
| 220 | `e081_1_ok` | 眼の群れ→目を閉じて手探りで進む（成功） |
| 221 | `e081_1_ng` | 眼の群れ→目を閉じて手探りで進む（失敗） |
| 222 | `e081_2_ok` | 眼の群れ→眼を潰して回る（成功） |
| 223 | `e081_2_ng` | 眼の群れ→眼を潰して回る（失敗） |
| 224 | `e081_3_ok` | 眼の群れ→見つめられることを受け入れる（成功） |
| 225 | `e081_3_ng` | 眼の群れ→見つめられることを受け入れる（失敗） |
| 226 | `e082_0_ok` | 心臓の間→結晶をえぐり取る（成功） |
| 227 | `e082_0_ng` | 心臓の間→結晶をえぐり取る（失敗） |
| 228 | `e082_1_ng` | 心臓の間→心臓に手を当てる（失敗） |
| 229 | `e082_2_r` | 心臓の間→静かに部屋を出る |
| 230 | `e083_0_ok` | 手の海→手の上を渡る（成功） |
| 231 | `e083_0_ng` | 手の海→手の上を渡る（失敗） |
| 232 | `e083_1_ok` | 手の海→手に身を委ねる（成功） |
| 233 | `e083_1_ng` | 手の海→手に身を委ねる（失敗） |
| 234 | `e083_2_ok` | 手の海→手を一つずつ握り返す（成功） |
| 235 | `e083_2_ng` | 手の海→手を一つずつ握り返す（失敗） |
| 236 | `e084_0_ok` | 堕ちた天使→鎖を断つ（成功） |
| 237 | `e084_0_ng` | 堕ちた天使→鎖を断つ（失敗） |
| 238 | `e084_1_ok` | 堕ちた天使→天使の正体を見極める（成功） |
| 239 | `e084_1_ng` | 堕ちた天使→天使の正体を見極める（失敗） |
| 240 | `e084_2_r` | 堕ちた天使→聖水を捧げる |
| 241 | `e085_0_ok` | 名前を呼ぶ声→振り向く（成功） |
| 242 | `e085_0_ng` | 名前を呼ぶ声→振り向く（失敗） |
| 243 | `e085_1_ok` | 名前を呼ぶ声→振り向かずに進む（成功） |
| 244 | `e085_1_ng` | 名前を呼ぶ声→振り向かずに進む（失敗） |
| 245 | `e085_2_ok` | 名前を呼ぶ声→耳を塞いで走る（成功） |
| 246 | `e085_2_ng` | 名前を呼ぶ声→耳を塞いで走る（失敗） |
| 247 | `e086_0_ok` | 逆さまの階段→逆立ちで登る（成功） |
| 248 | `e086_0_ng` | 逆さまの階段→逆立ちで登る（失敗） |
| 249 | `e086_1_ok` | 逆さまの階段→目を閉じて足の感覚に従う（成功） |
| 250 | `e086_1_ng` | 逆さまの階段→目を閉じて足の感覚に従う（失敗） |
| 251 | `e086_2_ok` | 逆さまの階段→手すりを乗り越えて飛び降りる（成功） |
| 252 | `e086_2_ng` | 逆さまの階段→手すりを乗り越えて飛び降りる（失敗） |
| 253 | `e087_0_ok` | 自分の死体→死体の手から取る（成功） |
| 254 | `e087_0_ng` | 自分の死体→死体の手から取る（失敗） |
| 255 | `e087_1_ok` | 自分の死体→死因を調べる（成功） |
| 256 | `e087_1_ng` | 自分の死体→死因を調べる（失敗） |
| 257 | `e087_2_r` | 自分の死体→埋葬する |
| 258 | `e088_0_ok` | 深淵の司祭→司祭を斬る（成功） |
| 259 | `e088_0_ng` | 深淵の司祭→司祭を斬る（失敗） |
| 260 | `e088_1_ok` | 深淵の司祭→信者のふりをする（成功） |
| 261 | `e088_1_ng` | 深淵の司祭→信者のふりをする（失敗） |
| 262 | `e088_2_ok` | 深淵の司祭→祭壇を叩き壊す（成功） |
| 263 | `e088_2_ng` | 深淵の司祭→祭壇を叩き壊す（失敗） |
| 264 | `e089_0_ok` | 星の落ちる井戸→星に願う（成功） |
| 265 | `e089_0_ng` | 星の落ちる井戸→星に願う（失敗） |
| 266 | `e089_1_ok` | 星の落ちる井戸→井戸に飛び込む（成功） |
| 267 | `e089_1_ng` | 星の落ちる井戸→井戸に飛び込む（失敗） |
| 268 | `e089_2_ok` | 星の落ちる井戸→井戸の水を汲む（成功） |
| 269 | `e089_2_ng` | 星の落ちる井戸→井戸の水を汲む（失敗） |
| 270 | `e090_0_ok` | 喰らうもの→歯の間を駆け抜ける（成功） |
| 271 | `e090_0_ng` | 喰らうもの→歯の間を駆け抜ける（失敗） |
| 272 | `e090_1_ok` | 喰らうもの→口の主に話しかける（成功） |
| 273 | `e090_1_ng` | 喰らうもの→口の主に話しかける（失敗） |
| 274 | `e090_2_ok` | 喰らうもの→口に何かを食わせる（成功） |
| 275 | `e090_2_ng` | 喰らうもの→口に何かを食わせる（失敗） |
| 276 | `e091_0_ok` | 鏡の迷宮→自分たちの声に従う（成功） |
| 277 | `e091_0_ng` | 鏡の迷宮→自分たちの声に従う（失敗） |
| 278 | `e091_1_ok` | 鏡の迷宮→鏡を全て割る（成功） |
| 279 | `e091_1_ng` | 鏡の迷宮→鏡を全て割る（失敗） |
| 280 | `e091_2_ok` | 鏡の迷宮→自分の直感だけを信じる（成功） |
| 281 | `e091_2_ng` | 鏡の迷宮→自分の直感だけを信じる（失敗） |
| 282 | `e092_1_ok` | 騎士の亡霊→安らかに眠らせる（成功） |
| 283 | `e092_1_ng` | 騎士の亡霊→安らかに眠らせる（失敗） |
| 284 | `e092_2_r` | 騎士の亡霊→最後の戦いの話を聞く |
| 285 | `e093_0_r` | 最後の商人→体と引き換えに心を癒す |
| 286 | `e093_1_r` | 最後の商人→心と引き換えに体を癒す |
| 287 | `e093_2_r` | 最後の商人→運命と引き換えにお守りを買う |
| 288 | `e093_3_r` | 最後の商人→金貨で全てを少しずつ |
| 289 | `e094_0_ok` | 赤い月→月が孵る前に駆け抜ける（成功） |
| 290 | `e094_0_ng` | 赤い月→月が孵る前に駆け抜ける（失敗） |
| 291 | `e094_1_ok` | 赤い月→月を見上げて祈る（成功） |
| 292 | `e094_1_ng` | 赤い月→月を見上げて祈る（失敗） |
| 293 | `e094_2_ok` | 赤い月→月の光を浴びて力を得る（成功） |
| 294 | `e094_2_ng` | 赤い月→月の光を浴びて力を得る（失敗） |
| 295 | `e095_1_ok` | 胎動する闇→子守唄に身を委ねる（成功） |
| 296 | `e095_1_ng` | 胎動する闇→子守唄に身を委ねる（失敗） |
| 297 | `e095_2_ok` | 胎動する闇→闇を切り裂いて進む（成功） |
| 298 | `e095_2_ng` | 胎動する闇→闇を切り裂いて進む（失敗） |
| 299 | `e096_1_ok` | あの夜の部屋→寝台で休む（成功） |
| 300 | `e096_1_ng` | あの夜の部屋→寝台で休む（失敗） |
| 301 | `e096_2_r` | あの夜の部屋→部屋を出る |
| 302 | `n04_1_r` | 王の手紙→手紙を拾い集める |
| 303 | `n04_2_r` | 王の手紙→そっと元に戻す |
| 304 | `n05_0_r` | 何度目の挑戦者→「初めて会うはずだ」と言う |
| 305 | `n05_1_ok` | 何度目の挑戦者→なぜ戻されるのか訊く（成功） |
| 306 | `n05_1_ng` | 何度目の挑戦者→なぜ戻されるのか訊く（失敗） |
| 307 | `n05_2_r` | 何度目の挑戦者→亡霊の装備をもらう |
| 308 | `x01_0_ok` | 底の向こう→迷わず降りる（成功） |
| 309 | `x01_0_ng` | 底の向こう→迷わず降りる（失敗） |
| 310 | `x01_1_ok` | 底の向こう→声に耳を澄ます（成功） |
| 311 | `x01_1_ng` | 底の向こう→声に耳を澄ます（失敗） |
| 312 | `x01_2_ok` | 底の向こう→石を投げ込んで深さを測る（成功） |
| 313 | `x01_2_ng` | 底の向こう→石を投げ込んで深さを測る（失敗） |
| 314 | `x02_0_ok` | 誰かの足跡→足跡を辿る（成功） |
| 315 | `x02_0_ng` | 誰かの足跡→足跡を辿る（失敗） |
| 316 | `x02_1_ok` | 誰かの足跡→逆向きに辿る（成功） |
| 317 | `x02_1_ng` | 誰かの足跡→逆向きに辿る（失敗） |
| 318 | `x02_2_r` | 誰かの足跡→足跡を踏み消す |
| 319 | `x03_0_ok` | 願いの墓場→一枚拾って読む（成功） |
| 320 | `x03_0_ng` | 願いの墓場→一枚拾って読む（失敗） |
| 321 | `x03_1_r` | 願いの墓場→たいまつで弔い火を灯す |
| 322 | `x03_2_r` | 願いの墓場→自分の願いを書き加える |
| 323 | `x03_3_r` | 願いの墓場→そっと通り過ぎる |
| 324 | `x04_0_r` | 子守唄の残響→聴き入る |
| 325 | `x04_1_ok` | 子守唄の残響→旋律に言葉をのせる（成功） |
| 326 | `x04_1_ng` | 子守唄の残響→旋律に言葉をのせる（失敗） |
| 327 | `x04_2_ok` | 子守唄の残響→旋律の源を探す（成功） |
| 328 | `x04_2_ng` | 子守唄の残響→旋律の源を探す（失敗） |
| 329 | `x05_0_ok` | 眼の欠片→踏み砕く（成功） |
| 330 | `x05_0_ng` | 眼の欠片→踏み砕く（失敗） |
| 331 | `x05_1_ok` | 眼の欠片→小さな願いを言う（成功） |
| 332 | `x05_1_ng` | 眼の欠片→小さな願いを言う（失敗） |
| 333 | `x05_2_r` | 眼の欠片→欠片を持ち去る |
| 334 | `x06_0_ok` | 鏡の中の踏破者→「願いのために」と答える（成功） |
| 335 | `x06_0_ng` | 鏡の中の踏破者→「願いのために」と答える（失敗） |
| 336 | `x06_1_ok` | 鏡の中の踏破者→鏡の自分と剣を交える（成功） |
| 337 | `x06_1_ng` | 鏡の中の踏破者→鏡の自分と剣を交える（失敗） |
| 338 | `x06_2_r` | 鏡の中の踏破者→目を伏せて通り抜ける |
| 339 | `x07_0_r` | 果ての商人→運命で赤いお守りを買う |
| 340 | `x07_1_r` | 果ての商人→金貨で手当てを受ける |
| 341 | `x07_2_r` | 果ての商人→血と引き換えに鍛えてもらう |
| 342 | `x07_3_r` | 果ての商人→何も買わない |
| 343 | `x08_0_r` | 王の使者→地上へ帰還する |
| 344 | `x08_1_r` | 王の使者→まだ降りると告げる |
| 345 | `x08_2_r` | 王の使者→使者の荷を分けてもらう |

---

## プロンプトの組み立て方（全画像共通）

この指示書は長くなりすぎないよう、共通部分を一度だけ書いています。各画像のプロンプトは、次の順に**そのままつなげて**作ってください（書き換えない）。

1. 下の「共通の画風指定」の文章全体
2. 空行1つ
3. `Scene: ` に続けて、その画像の「Scene」の文章
4. その画像に「Characters」の指定がある場合だけ：空行1つ、`Characters (keep them consistent across images):` の1行、続けて指定された人物の行を、下の「登場人物」からそのまま1行ずつ

### 共通の画風指定

```
Dark fantasy horror illustration for a retro game, wide landscape composition. Strictly monochrome: pure black, charcoal grey, light grey and off-white only, plus blood red used ONLY on the elements listed as red. No other colours, no blue, brown, sepia or warm tint anywhere. Strong chiaroscuro: mostly deep black darkness, one dim light source, very high contrast. Large, simple, clearly readable shapes and silhouettes with minimal fine texture and no tiny details, because the image will be shrunk to 336x200 pixels. Flat graphic shading in three or four tones, like a woodcut or ink wash, crisp edges. Every element listed as red must be bold and clearly visible, because tiny red details disappear when shrunk, but red should cover only a small part of the image unless the scene says otherwise. Main characters should be large in the frame unless the scene says they are small. Everything happens underground inside the labyrinth: no sky, no moon, no sun, no trees, no outdoor scenery, unless the scene says it is outside. Any royal crest or emblem is always a simple crown shape. Keep every important subject inside the central horizontal band; the top and bottom 6% will be cropped. No text, no letters, no runes, no logo, no frame, no border, no UI, no signature, no watermark. Not anime or manga style: no big eyes, no cute or stylised faces; realistic human proportions and restrained, naturalistic faces, like a classic dark fantasy book illustration or etching. Not pixel art and no pixel grid (it will be pixelized afterwards).
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

### 1. e040_2_r：囁く人形→人形を後ろ向きにして去る

保存名：`generated/e040_2_r.png`

- Scene: the hooded adventurer walks out of a dark room, leaving a porcelain doll on its chair turned to face the wall; its head has twisted back to watch them. Red only: the doll's lips.
- Characters: the hooded adventurer

### 2. e041_0_ok：肖像画の回廊→絵の自分に触れる（成功）

保存名：`generated/e041_0_ok.png`

- Scene: In a gallery of portraits, the hooded adventurer touches the last portrait of their old self, which smiles and reaches out; a soft glow flows into the adventurer's hand. Red only: the portrait's eyes.
- Characters: the hooded adventurer

### 3. e041_0_ng：肖像画の回廊→絵の自分に触れる（失敗）

保存名：`generated/e041_0_ng.png`

- Scene: the hooded adventurer touches the last portrait in a gallery and their hand withers and ages while the painted old self grows younger. Red only: the portrait's eyes.
- Characters: the hooded adventurer

### 4. e041_1_r：肖像画の回廊→絵を切り裂く

保存名：`generated/e041_1_r.png`

- Scene: the hooded adventurer slashes a portrait with a short sword; the canvas splits and the painted face screams. Red only: the gash in the canvas.
- Characters: the hooded adventurer

### 5. e041_2_ok：肖像画の回廊→額縁を外して持ち去る（成功）

保存名：`generated/e041_2_ok.png`

- Scene: the hooded adventurer carries away a heavy ornate gilded frame from a gallery wall. Red only: a gem set in the frame.
- Characters: the hooded adventurer

### 6. e041_2_ng：肖像画の回廊→額縁を外して持ち去る（失敗）

保存名：`generated/e041_2_ng.png`

- Scene: the hooded adventurer staggers under an impossibly heavy ornate frame, clutching their lower back. Red only: a gem set in the frame.
- Characters: the hooded adventurer

### 7. e042_0_ok：朽ちた吊り橋→慎重に渡る（成功）

保存名：`generated/e042_0_ok.png`

- Scene: the hooded adventurer crosses a rotting rope bridge over a chasm step by careful step, gripping the ropes. Red only: the red cloth tied to the far post.
- Characters: the hooded adventurer

### 8. e042_0_ng：朽ちた吊り橋→慎重に渡る（失敗）

保存名：`generated/e042_0_ng.png`

- Scene: the hooded adventurer freezes in the middle of a rope bridge as countless pale hands reach up from the chasm below. Red only: the red cloth tied to the post.
- Characters: the hooded adventurer

### 9. e042_1_ok：朽ちた吊り橋→一気に駆け抜ける（成功）

保存名：`generated/e042_1_ok.png`

- Scene: Planks fall away behind the hooded adventurer, who leaps the last gap of a collapsing rope bridge onto the far edge. Red only: the red cloth on the post.
- Characters: the hooded adventurer

### 10. e042_1_ng：朽ちた吊り橋→一気に駆け抜ける（失敗）

保存名：`generated/e042_1_ng.png`

- Scene: the hooded adventurer hangs from a broken rope bridge, a plank snapped beneath them, clawing back up. Red only: the red cloth on the post.
- Characters: the hooded adventurer

### 11. e042_2_r：朽ちた吊り橋→ロープで体を繋いで渡る

保存名：`generated/e042_2_r.png`

- Scene: the hooded adventurer crosses a swaying rope bridge safely, a rope tied from their waist to the bridge's guide line. Red only: the red cloth on the post.
- Characters: the hooded adventurer

### 12. e042_3_ok：朽ちた吊り橋→裂け目へ飛び降りる（成功）

保存名：`generated/e042_3_ok.png`

- Scene: the hooded adventurer surfaces in an underground river at the bottom of a chasm, far below a tiny bridge high above. Red only: a faint red glow in the water.
- Characters: the hooded adventurer

### 13. e042_3_ng：朽ちた吊り橋→裂け目へ飛び降りる（失敗）

保存名：`generated/e042_3_ng.png`

- Scene: the hooded adventurer lies on a rock ledge deep in a chasm after a fall, a tiny bridge far above. Red only: a small bloody scrape.
- Characters: the hooded adventurer

### 14. e043_0_ok：錬金術師の工房→赤い薬を飲む（成功）

保存名：`generated/e043_0_ok.png`

- Scene: the hooded adventurer drinks a red potion in an alchemist's workshop, standing taller, faint heat shimmering from their body. Red only: the red potion.
- Characters: the hooded adventurer

### 15. e043_0_ng：錬金術師の工房→赤い薬を飲む（失敗）

保存名：`generated/e043_0_ng.png`

- Scene: the hooded adventurer clutches their burning throat beside an alchemist's desk, a dropped red bottle on the floor. Red only: the red potion.
- Characters: the hooded adventurer

### 16. e043_1_ok：錬金術師の工房→白い薬を飲む（成功）

保存名：`generated/e043_1_ok.png`

- Scene: the hooded adventurer drinks a white potion in an alchemist's workshop, eyes calm and clear, the darkness pushed back around them. Red only: the red potion left on the desk.
- Characters: the hooded adventurer

### 17. e043_1_ng：錬金術師の工房→白い薬を飲む（失敗）

保存名：`generated/e043_1_ng.png`

- Scene: the hooded adventurer staggers blind in an alchemist's workshop, the world washed out in white glare. Red only: the red potion left on the desk.
- Characters: the hooded adventurer

### 18. e043_2_ok：錬金術師の工房→黒い薬を飲む（成功）

保存名：`generated/e043_2_ok.png`

- Scene: the hooded adventurer drinks a black potion and sees faint glowing threads of fate stretching from their hands into the dark. Red only: one thread of fate.
- Characters: the hooded adventurer

### 19. e043_2_ng：錬金術師の工房→黒い薬を飲む（失敗）

保存名：`generated/e043_2_ng.png`

- Scene: the hooded adventurer doubles over after drinking a black potion, dark veins spreading on their hands. Red only: the red potion left on the desk.
- Characters: the hooded adventurer

### 20. e044_0_ok：死者の宴→席に着いて食べる（成功）

保存名：`generated/e044_0_ok.png`

- Scene: the hooded adventurer sits at a long banquet table among skeletons, eating; the skeletons clack their teeth happily. Red only: the wine in the goblets.
- Characters: the hooded adventurer

### 21. e044_0_ng：死者の宴→席に着いて食べる（失敗）

保存名：`generated/e044_0_ng.png`

- Scene: the hooded adventurer recoils from a banquet plate, spitting, as they realise what the food is made of; skeletons stare. Red only: the wine in the goblets.
- Characters: the hooded adventurer

### 22. e044_1_ok：死者の宴→乾杯の音頭を取る（成功）

保存名：`generated/e044_1_ok.png`

- Scene: the hooded adventurer raises a goblet in a toast at a banquet table; skeletons cheer and one offers a pouch of coins. Red only: the wine in the goblets.
- Characters: the hooded adventurer

### 23. e044_1_ng：死者の宴→乾杯の音頭を取る（失敗）

保存名：`generated/e044_1_ng.png`

- Scene: the hooded adventurer holds a goblet of blood as all the skeletons at the banquet rise from their seats at once. Red only: the blood in the goblet.
- Characters: the hooded adventurer

### 24. e044_2_r：死者の宴→丁重に辞退する

保存名：`generated/e044_2_r.png`

- Scene: the hooded adventurer bows and leaves a banquet hall while skeletons at the table watch, disappointed. Red only: the wine in the goblets.
- Characters: the hooded adventurer

### 25. e045_1_r：薄れゆく亡霊→最後の戦いの話を聞く

保存名：`generated/e045_1_r.png`

- Scene: the ghost knight, very faint, sits against a dungeon wall and tells a story; above him a ghostly vision shows a woman melting into a wall and a giant eye. the hooded adventurer listens. Red only: the giant eye in the vision.
- Characters: the hooded adventurer, the ghost knight

### 26. e045_2_r：薄れゆく亡霊→安らかに眠らせる

保存名：`generated/e045_2_r.png`

- Scene: the ghost knight, very faint, removes his helmet and bows his head before the hooded adventurer as he fades away; a small red amulet lies where he stood. Red only: the amulet.
- Characters: the hooded adventurer, the ghost knight

### 27. e046_1_ng：少女の墓→墓を掘り起こす（失敗）

保存名：`generated/e046_1_ng.png`

- Scene: the ghost girl, furious and screaming, flies off into the darkness of a crypt as the hooded adventurer kneels by a half-dug grave with a crown crest. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 28. e047_0_ok：鎖の囚人→男の願いを聞く（成功）

保存名：`generated/e047_0_ok.png`

- Scene: A chained eyeless prisoner touches the forehead of the hooded adventurer; a third eye opens on the adventurer's brow, glowing. Red only: the third eye.
- Characters: the hooded adventurer

### 29. e047_0_ng：鎖の囚人→男の願いを聞く（失敗）

保存名：`generated/e047_0_ng.png`

- Scene: A chained eyeless prisoner digs his fingers into the forehead of the hooded adventurer, who screams in pain. Red only: the wound on the forehead.
- Characters: the hooded adventurer

### 30. e047_1_r：鎖の囚人→鍵で鎖を外す

保存名：`generated/e047_1_r.png`

- Scene: A freed eyeless prisoner walks confidently away into the darkness, whispering over his shoulder to the hooded adventurer, who holds a key. Red only: the opened shackles.
- Characters: the hooded adventurer

### 31. e047_2_r：鎖の囚人→放っておく

保存名：`generated/e047_2_r.png`

- Scene: the hooded adventurer walks away from a dungeon cell while a chained eyeless prisoner cries out after them. Red only: the rusted shackles.
- Characters: the hooded adventurer

### 32. e048_0_ok：牢番→背後から鍵束を盗む（成功）

保存名：`generated/e048_0_ok.png`

- Scene: the hooded adventurer sneaks behind a headless jailer and slips one rusty key off his giant key ring. Red only: the small flame in the jailer's lantern.
- Characters: the hooded adventurer

### 33. e048_0_ng：牢番→背後から鍵束を盗む（失敗）

保存名：`generated/e048_0_ng.png`

- Scene: A headless jailer has turned toward the hooded adventurer, who freezes with a hand on his key ring. Red only: the small flame in the jailer's lantern.
- Characters: the hooded adventurer

### 34. e048_1_ok：牢番→正面から倒す（成功）

保存名：`generated/e048_1_ok.png`

- Scene: A headless jailer lies fallen before the hooded adventurer, his key ring and some coins scattered on the floor. Red only: the small flame in his dropped lantern.
- Characters: the hooded adventurer

### 35. e048_1_ng：牢番→正面から倒す（失敗）

保存名：`generated/e048_1_ng.png`

- Scene: A headless jailer's iron fist slams into the hooded adventurer, sending them flying. Red only: the small flame in the jailer's lantern.
- Characters: the hooded adventurer

### 36. e048_2_ok：牢番→囚人のふりをしてやり過ごす（成功）

保存名：`generated/e048_2_ok.png`

- Scene: the hooded adventurer sits slumped inside a cell like a prisoner while a headless jailer walks past, unaware. Red only: the small flame in the jailer's lantern.
- Characters: the hooded adventurer

### 37. e048_2_ng：牢番→囚人のふりをしてやり過ごす（失敗）

保存名：`generated/e048_2_ng.png`

- Scene: A headless jailer throws the hooded adventurer into a cell and slams the iron door. Red only: the small flame in the jailer's lantern.
- Characters: the hooded adventurer

### 38. e049_0_ok：蝋燭の道→蝋燭を消さないよう慎重に進む（成功）

保存名：`generated/e049_0_ok.png`

- Scene: the hooded adventurer edges carefully down a corridor lined with countless lit candles, holding the cloak close, every flame still burning. Red only: the nearest candle flames.
- Characters: the hooded adventurer

### 39. e049_0_ng：蝋燭の道→蝋燭を消さないよう慎重に進む（失敗）

保存名：`generated/e049_0_ng.png`

- Scene: the hooded adventurer's cloak brushes a candle out in a corridor of candles; they clutch their own throat, mouth open in a scream. Red only: the nearest candle flames.
- Characters: the hooded adventurer

### 40. e049_1_r：蝋燭の道→一本持っていく

保存名：`generated/e049_1_r.png`

- Scene: the hooded adventurer carries one lit candle like a torch down a corridor of candles. Red only: the candle's flame.
- Characters: the hooded adventurer

### 41. e049_2_ok：蝋燭の道→全部吹き消す（成功）

保存名：`generated/e049_2_ok.png`

- Scene: the hooded adventurer stands in a corridor of extinguished smoking candles as a hidden door swings open in the wall. Red only: the light from the hidden door.
- Characters: the hooded adventurer

### 42. e049_2_ng：蝋燭の道→全部吹き消す（失敗）

保存名：`generated/e049_2_ng.png`

- Scene: In a dark corridor of extinguished candles, pale wailing figures gather around the hooded adventurer. Red only: the figures' eyes.
- Characters: the hooded adventurer

### 43. e049_3_r：蝋燭の道→足早に通り抜ける

保存名：`generated/e049_3_r.png`

- Scene: the hooded adventurer hurries down a corridor of candles, eyes fixed straight ahead. Red only: the nearest candle flames.
- Characters: the hooded adventurer

### 44. e050_0_ok：闇の中の目→目を見つめ返す（成功）

保存名：`generated/e050_0_ok.png`

- Scene: A house-sized eye in the darkness of a cave slowly closes, as if approving; the hooded adventurer stands before it in a soft glow. Red only: the veins around the eye.
- Characters: the hooded adventurer

### 45. e050_0_ng：闇の中の目→目を見つめ返す（失敗）

保存名：`generated/e050_0_ng.png`

- Scene: the hooded adventurer stares into a gigantic eye whose pupil opens into a bottomless abyss that pulls at them. Red only: the veins around the eye.
- Characters: the hooded adventurer

### 46. e050_1_r：闇の中の目→第三の眼で見返す

保存名：`generated/e050_1_r.png`

- Scene: the hooded adventurer, with a glowing third eye on their brow, meets the gaze of a gigantic eye in a cave, which narrows contentedly. Red only: the third eye.
- Characters: the hooded adventurer

### 47. e050_2_ok：闇の中の目→視線から逃げる（成功）

保存名：`generated/e050_2_ok.png`

- Scene: the hooded adventurer slips between boulders, hiding from the gaze of a gigantic eye in the darkness. Red only: the veins around the eye.
- Characters: the hooded adventurer

### 48. e050_2_ng：闇の中の目→視線から逃げる（失敗）

保存名：`generated/e050_2_ng.png`

- Scene: the hooded adventurer is caught in the gaze of a gigantic eye, sinking to their knees as if turned heavy as stone. Red only: the veins around the eye.
- Characters: the hooded adventurer

### 49. e051_0_ok：地図職人の亡骸→地図を持っていく（成功）

保存名：`generated/e051_0_ok.png`

- Scene: the hooded adventurer studies an accurate map of the labyrinth drawn as maze lines, taken from a dead mapmaker's desk. Red only: the blood line on the map.
- Characters: the hooded adventurer

### 50. e051_0_ng：地図職人の亡骸→地図を持っていく（失敗）

保存名：`generated/e051_0_ng.png`

- Scene: The mummified mapmaker's hand grips the wrist of the hooded adventurer, and the map tears in two. Red only: the blood line on the map.
- Characters: the hooded adventurer

### 51. e051_1_ok：地図職人の亡骸→地図を描き足してやる（成功）

保存名：`generated/e051_1_ok.png`

- Scene: the hooded adventurer finishes drawing a maze map on a desk; the mapmaker's body crumbles peacefully into dust and a hidden passage glows on the map. Red only: the hidden passage on the map.
- Characters: the hooded adventurer

### 52. e051_1_ng：地図職人の亡骸→地図を描き足してやる（失敗）

保存名：`generated/e051_1_ng.png`

- Scene: the hooded adventurer draws on a maze map while the bookshelves around them twist and rearrange themselves. Red only: the blood line on the map.
- Characters: the hooded adventurer

### 53. e051_2_r：地図職人の亡骸→男のポケットを探る

保存名：`generated/e051_2_r.png`

- Scene: the hooded adventurer searches the coat of a mummified mapmaker and finds an inkwell and a few coins. Red only: the blood line on the map on the desk.
- Characters: the hooded adventurer

### 54. e052_0_ok：禁書庫→暴れる本を読む（成功）

保存名：`generated/e052_0_ok.png`

- Scene: the hooded adventurer reads a thrashing chained book with a face on its cover; glowing symbols stream into their eyes. Red only: the open mouth on the cover.
- Characters: the hooded adventurer

### 55. e052_0_ng：禁書庫→暴れる本を読む（失敗）

保存名：`generated/e052_0_ng.png`

- Scene: the hooded adventurer clutches their head as dark wriggling marks crawl from an open chained book into their eyes. Red only: the open mouth on the cover.
- Characters: the hooded adventurer

### 56. e052_1_r：禁書庫→本を焼き払う

保存名：`generated/e052_1_r.png`

- Scene: A chained book with a human face burns, screaming, while the hooded adventurer holds a torch to it. Red only: the flames.
- Characters: the hooded adventurer

### 57. e052_2_ok：禁書庫→静かな本を一冊選ぶ（成功）

保存名：`generated/e052_2_ok.png`

- Scene: the hooded adventurer sits reading a calm old medical book with simple anatomical diagrams in a forbidden library. Red only: a red ribbon bookmark.
- Characters: the hooded adventurer

### 58. e052_2_ng：禁書庫→静かな本を一冊選ぶ（失敗）

保存名：`generated/e052_2_ng.png`

- Scene: the hooded adventurer drops a calm-looking book in horror in a forbidden library. Red only: a red ribbon bookmark.
- Characters: the hooded adventurer

### 59. e053_0_ok：湖の歌声→耳を塞いで立ち去る（成功）

保存名：`generated/e053_0_ok.png`

- Scene: the hooded adventurer walks away from an underground lake, hands over their ears, while the pale woman sings on her rock. Red only: her lips.
- Characters: the hooded adventurer

### 60. e053_0_ng：湖の歌声→耳を塞いで立ち去る（失敗）

保存名：`generated/e053_0_ng.png`

- Scene: the hooded adventurer wakes waist-deep in a black underground lake, the singing woman on her rock ahead, and turns back in alarm. Red only: her lips.
- Characters: the hooded adventurer

### 61. e053_1_ok：湖の歌声→歌に合わせて歌い返す（成功）

保存名：`generated/e053_1_ok.png`

- Scene: The pale woman on a lake rock laughs and tosses a pearl to the hooded adventurer, who stands singing on the shore. Red only: her lips.
- Characters: the hooded adventurer

### 62. e053_1_ng：湖の歌声→歌に合わせて歌い返す（失敗）

保存名：`generated/e053_1_ng.png`

- Scene: the hooded adventurer sings on the shore of an underground lake, clutching their throat as their voice fades away. Red only: the woman's lips.
- Characters: the hooded adventurer

### 63. e053_2_ok：湖の歌声→湖に飛び込む（成功）

保存名：`generated/e053_2_ok.png`

- Scene: Underwater in an underground lake, the hooded adventurer swims past a hideous monster toward an underwater tunnel. Red only: the monster's eyes.
- Characters: the hooded adventurer

### 64. e053_2_ng：湖の歌声→湖に飛び込む（失敗）

保存名：`generated/e053_2_ng.png`

- Scene: the hooded adventurer struggles in an underground lake as countless arms drag at them from below. Red only: the arms' fingernails.
- Characters: the hooded adventurer

### 65. e054_0_ok：死神の賭け→命を賭けて挑む（成功）

保存名：`generated/e054_0_ok.png`

- Scene: A skeletal reaper at a chessboard laughs dryly and tips over its own king; the hooded adventurer sits across, glowing with life. Red only: the fallen king piece.
- Characters: the hooded adventurer

### 66. e054_0_ng：死神の賭け→命を賭けて挑む（失敗）

保存名：`generated/e054_0_ng.png`

- Scene: A skeletal reaper's scythe blade rests against the neck of the hooded adventurer across a chessboard. Red only: the king piece on the board.
- Characters: the hooded adventurer

### 67. e054_1_ok：死神の賭け→知略で挑む（成功）

保存名：`generated/e054_1_ok.png`

- Scene: A skeletal reaper hands a single chess piece to the hooded adventurer across a board locked in a draw. Red only: the chess piece.
- Characters: the hooded adventurer

### 68. e054_1_ng：死神の賭け→知略で挑む（失敗）

保存名：`generated/e054_1_ng.png`

- Scene: the hooded adventurer stares at a chessboard whose pieces have turned into tiny human faces. Red only: the king piece.
- Characters: the hooded adventurer

### 69. e054_2_ok：死神の賭け→盤をひっくり返して逃げる（成功）

保存名：`generated/e054_2_ok.png`

- Scene: the hooded adventurer flees from an overturned chessboard as a skeletal reaper sits calmly watching. Red only: the scattered king piece.
- Characters: the hooded adventurer

### 70. e054_2_ng：死神の賭け→盤をひっくり返して逃げる（失敗）

保存名：`generated/e054_2_ng.png`

- Scene: A reaper's scythe slices across the back of the hooded adventurer as they flee from an overturned chessboard. Red only: the slash on the cloak.
- Characters: the hooded adventurer

### 71. e055_0_ok：蛆の床→死骸を踏み越えて進む（成功）

保存名：`generated/e055_0_ok.png`

- Scene: the hooded adventurer leaps across a vast carcass above a floor of writhing maggots. Red only: the gash in the carcass.
- Characters: the hooded adventurer

### 72. e055_0_ng：蛆の床→死骸を踏み越えて進む（失敗）

保存名：`generated/e055_0_ng.png`

- Scene: the hooded adventurer falls into the split belly of a vast carcass above a floor of maggots. Red only: the gash.
- Characters: the hooded adventurer

### 73. e055_1_r：蛆の床→火を放つ

保存名：`generated/e055_1_r.png`

- Scene: A floor of maggots and a vast carcass burn; the hooded adventurer holds up a huge fang from the ashes. Red only: the flames.
- Characters: the hooded adventurer

### 74. e055_2_ok：蛆の床→目を閉じて走り抜ける（成功）

保存名：`generated/e055_2_ok.png`

- Scene: the hooded adventurer runs across a floor of maggots with eyes squeezed shut. Red only: the gash in the carcass.
- Characters: the hooded adventurer

### 75. e055_2_ng：蛆の床→目を閉じて走り抜ける（失敗）

保存名：`generated/e055_2_ng.png`

- Scene: the hooded adventurer claws at their clothes, maggots crawling out of their sleeves. Red only: the gash in the carcass behind.
- Characters: the hooded adventurer

### 76. e056_0_r：メモの続き→続きを読む

保存名：`generated/e056_0_r.png`

- Scene: the hooded adventurer turns over a handwritten note to find more illegible writing on the back, in a dark corridor. Red only: the pressed flower in the note.
- Characters: the hooded adventurer

### 77. e056_1_r：メモの続き→挟まれた押し花を手に取る

保存名：`generated/e056_1_r.png`

- Scene: the hooded adventurer holds a small pressed white flower from a note, gently, in a dark corridor. Red only: a tiny red thread tying the flower.
- Characters: the hooded adventurer

### 78. e056_2_r：メモの続き→メモを置いて先を急ぐ

保存名：`generated/e056_2_r.png`

- Scene: the hooded adventurer leaves a note on the corridor floor and walks on; a faint pale shape of a weeping woman hovers over the note. Red only: the pressed flower.
- Characters: the hooded adventurer

### 79. e057_0_r：喰らう扉→薬瓶を食わせる

保存名：`generated/e057_0_r.png`

- Scene: A door with a fleshy mouth crunches a potion bottle, glass and all, then swings open for the hooded adventurer. Red only: the tongue.
- Characters: the hooded adventurer

### 80. e057_1_ok：喰らう扉→腕を差し出す（成功）

保存名：`generated/e057_1_ok.png`

- Scene: A door's fleshy mouth licks the hooded adventurer's outstretched arm, grimaces, and opens. Red only: the tongue.
- Characters: the hooded adventurer

### 81. e057_1_ng：喰らう扉→腕を差し出す（失敗）

保存名：`generated/e057_1_ng.png`

- Scene: A door's fleshy mouth bites down on the hooded adventurer's outstretched arm. Red only: the bite wound.
- Characters: the hooded adventurer

### 82. e057_2_ok：喰らう扉→扉をこじ開ける（成功）

保存名：`generated/e057_2_ok.png`

- Scene: the hooded adventurer forces apart the jaws of a door's mouth with both hands and squeezes through. Red only: the tongue.
- Characters: the hooded adventurer

### 83. e057_2_ng：喰らう扉→扉をこじ開ける（失敗）

保存名：`generated/e057_2_ng.png`

- Scene: A door's mouth has snapped shut on half of the hooded adventurer's body. Red only: the tongue.
- Characters: the hooded adventurer

### 84. e057_3_r：喰らう扉→別の道を探す

保存名：`generated/e057_3_r.png`

- Scene: the hooded adventurer wanders lost through a maze of identical dark corridors, small and exhausted. Red only: a faint red glow far ahead.
- Characters: the hooded adventurer

### 85. g050_0_r：都市の番人→銀の剣で炉心を貫く

保存名：`generated/g050_0_r.png`

- Scene: the hooded adventurer leaps and drives a silver sword into the glowing furnace core in the chest of a colossal stone-and-iron guardian. Red only: the furnace core.
- Characters: the hooded adventurer

### 86. g050_2_ok：都市の番人→足元をすり抜ける（成功）

保存名：`generated/g050_2_ok.png`

- Scene: the hooded adventurer dashes between the huge slow legs of a colossal stone guardian toward a ruined gate. Red only: the furnace core in its chest.
- Characters: the hooded adventurer

### 87. g050_2_ng：都市の番人→足元をすり抜ける（失敗）

保存名：`generated/g050_2_ng.png`

- Scene: A colossal stone guardian's foot kicks the hooded adventurer flying through the air past a ruined gate. Red only: the furnace core.
- Characters: the hooded adventurer

### 88. g050_3_ok：都市の番人→正面から打ち倒す（成功）

保存名：`generated/g050_3_ok.png`

- Scene: the hooded adventurer shatters the knee of a colossal stone guardian, which topples. Red only: the furnace core.
- Characters: the hooded adventurer

### 89. g050_3_ng：都市の番人→正面から打ち倒す（失敗）

保存名：`generated/g050_3_ng.png`

- Scene: the hooded adventurer, battered, crawls under a ruined gate while a colossal guardian's iron fist slams down behind. Red only: the furnace core.
- Characters: the hooded adventurer

### 90. g050_4_ok：都市の番人→市民になりすます（成功）

保存名：`generated/g050_4_ok.png`

- Scene: the hooded adventurer bows in an old-fashioned courtly gesture before a colossal stone guardian, which steps aside. Red only: the furnace core.
- Characters: the hooded adventurer

### 91. g050_4_ng：都市の番人→市民になりすます（失敗）

保存名：`generated/g050_4_ng.png`

- Scene: A beam of light from a colossal guardian's chest scorches the hooded adventurer. Red only: the furnace core and the beam.
- Characters: the hooded adventurer

### 92. e058_0_ok：胞子の森→布で口を覆って進む（成功）

保存名：`generated/e058_0_ok.png`

- Scene: the hooded adventurer walks through a forest of giant mushrooms with a cloth over their mouth, spores falling like snow. Red only: a small glowing light deep in the forest.
- Characters: the hooded adventurer

### 93. e058_0_ng：胞子の森→布で口を覆って進む（失敗）

保存名：`generated/e058_0_ng.png`

- Scene: the hooded adventurer coughs in a forest of giant mushrooms, tiny sprouts growing from their sleeve. Red only: the sprouts' tips.
- Characters: the hooded adventurer

### 94. e058_1_ok：胞子の森→笑い声の方へ行く（成功）

保存名：`generated/e058_1_ok.png`

- Scene: Tiny mushroom sprites point the way for the hooded adventurer in a forest of giant mushrooms. Red only: the sprites' caps.
- Characters: the hooded adventurer

### 95. e058_1_ng：胞子の森→笑い声の方へ行く（失敗）

保存名：`generated/e058_1_ng.png`

- Scene: In a mushroom forest, the hooded adventurer finds laughing people half-overgrown with fungus, rooted in the ground. Red only: their eyes.
- Characters: the hooded adventurer

### 96. e058_2_r：胞子の森→森を焼き払う

保存名：`generated/e058_2_r.png`

- Scene: A forest of giant mushrooms burns fiercely; the hooded adventurer pushes through smoke and ash. Red only: the flames.
- Characters: the hooded adventurer

### 97. e059_0_ok：地下都市の大通り→家の中を探索する（成功）

保存名：`generated/e059_0_ok.png`

- Scene: In an empty house of a colourless underground city, the hooded adventurer pulls a pot of coins from the back of a fireplace. Red only: a single coin glinting red in the firelight.
- Characters: the hooded adventurer

### 98. e059_0_ng：地下都市の大通り→家の中を探索する（失敗）

保存名：`generated/e059_0_ng.png`

- Scene: the hooded adventurer sits at a dinner table in an empty house, surrounded by faint invisible figures shaped only by empty chairs pulled out and floating cutlery. Red only: the wine in a glass.
- Characters: the hooded adventurer

### 99. e059_1_ok：地下都市の大通り→大通りを堂々と歩く（成功）

保存名：`generated/e059_1_ok.png`

- Scene: the hooded adventurer walks openly down a colourless underground city avenue; faint translucent residents wave from doorways. Red only: one lit window.
- Characters: the hooded adventurer

### 100. e059_1_ng：地下都市の大通り→大通りを堂々と歩く（失敗）

保存名：`generated/e059_1_ng.png`

- Scene: the hooded adventurer stands in a colourless city avenue as every silhouette in every lit window has turned to face them. Red only: one lit window.
- Characters: the hooded adventurer

### 101. e059_2_ok：地下都市の大通り→裏路地を抜ける（成功）

保存名：`generated/e059_2_ok.png`

- Scene: the hooded adventurer finds a stairway going down at the end of a narrow back alley in an underground city. Red only: a faint glow from the stairway.
- Characters: the hooded adventurer

### 102. e059_2_ng：地下都市の大通り→裏路地を抜ける（失敗）

保存名：`generated/e059_2_ng.png`

- Scene: the hooded adventurer runs down a narrow alley, pursued by a shadowy shape. Red only: the shape's eyes.
- Characters: the hooded adventurer

### 103. e060_0_ok：王の亡骸→王冠を奪う（成功）

保存名：`generated/e060_0_ok.png`

- Scene: the hooded adventurer holds up a crown as the mummified king on the throne crumbles into dust. Red only: the jewels of the crown.
- Characters: the hooded adventurer

### 104. e060_0_ng：王の亡骸→王冠を奪う（失敗）

保存名：`generated/e060_0_ng.png`

- Scene: The mummified king's hand grips the wrist of the hooded adventurer, who is reaching for his crown; frost spreads. Red only: the jewels of the crown.
- Characters: the hooded adventurer

### 105. e060_1_ok：王の亡骸→跪いて臣従を誓う（成功）

保存名：`generated/e060_1_ok.png`

- Scene: the hooded adventurer kneels before a throne; the mummified king places his crown on the adventurer's hood. Red only: the jewels of the crown.
- Characters: the hooded adventurer

### 106. e060_1_ng：王の亡骸→跪いて臣従を誓う（失敗）

保存名：`generated/e060_1_ng.png`

- Scene: the hooded adventurer kneels before a throne while the mummified king shakes his head. Red only: the jewels of the crown.
- Characters: the hooded adventurer

### 107. e060_2_r：王の亡骸→玉座の裏の宝物庫を探す

保存名：`generated/e060_2_r.png`

- Scene: the hooded adventurer searches a looted treasure room behind a throne, finding a few coins among broken chests. Red only: a small red gem among the coins.
- Characters: the hooded adventurer

### 108. e061_0_r：蛾の女王→たいまつを差し出す

保存名：`generated/e061_0_r.png`

- Scene: A giant moth with face-patterned wings gazes entranced at a torch held up by the hooded adventurer, scattering glowing dust over them. Red only: the moth's eyes.
- Characters: the hooded adventurer

### 109. e061_1_r：蛾の女王→命の光を分け与える

保存名：`generated/e061_1_r.png`

- Scene: A giant moth with face-patterned wings hovers over the hooded adventurer, drawing a faint glow from their chest. Red only: the moth's eyes.
- Characters: the hooded adventurer

### 110. e061_2_ok：蛾の女王→羽を斬り落とす（成功）

保存名：`generated/e061_2_ok.png`

- Scene: A giant moth falls with one wing cut away, the faces on its wings screaming in release; the hooded adventurer stands with sword raised. Red only: the moth's eyes.
- Characters: the hooded adventurer

### 111. e061_2_ng：蛾の女王→羽を斬り落とす（失敗）

保存名：`generated/e061_2_ng.png`

- Scene: the hooded adventurer staggers in a cloud of glittering moth dust, surrounded by hallucinated faces. Red only: the moth's eyes.
- Characters: the hooded adventurer

### 112. e062_0_ok：菌糸の人→誘いを受け入れる(ふりをする)（成功）

保存名：`generated/e062_0_ok.png`

- Scene: the hooded adventurer runs away from a fungus-covered man with outstretched arms. Red only: the mushroom caps on his shoulders.
- Characters: the hooded adventurer

### 113. e062_0_ng：菌糸の人→誘いを受け入れる(ふりをする)（失敗）

保存名：`generated/e062_0_ng.png`

- Scene: Fungal threads take root in the hooded adventurer's arm as a fungus-covered man embraces them. Red only: the mushroom caps on his shoulders.
- Characters: the hooded adventurer

### 114. e062_1_r：菌糸の人→焼き払う

保存名：`generated/e062_1_r.png`

- Scene: A fungus-covered man burns with a calm face while the hooded adventurer holds a torch. Red only: the flames.
- Characters: the hooded adventurer

### 115. e062_2_ok：菌糸の人→殴り倒す（成功）

保存名：`generated/e062_2_ok.png`

- Scene: A fungus-covered man collapses wetly under the hooded adventurer's blow. Red only: the mushroom caps on his shoulders.
- Characters: the hooded adventurer

### 116. e062_2_ng：菌糸の人→殴り倒す（失敗）

保存名：`generated/e062_2_ng.png`

- Scene: Spores burst from a fungus-covered man into the hooded adventurer's fist as they punch him. Red only: the mushroom caps on his shoulders.
- Characters: the hooded adventurer

### 117. e063_0_ok：逆さ時計の塔→扉に入る（成功）

保存名：`generated/e063_0_ok.png`

- Scene: the hooded adventurer walks through a door under a backwards-running clock; their wounds fade away in reverse. Red only: the clock hands.
- Characters: the hooded adventurer

### 118. e063_0_ng：逆さ時計の塔→扉に入る（失敗）

保存名：`generated/e063_0_ng.png`

- Scene: the hooded adventurer stumbles out of a door under a giant clock, looking younger, swept backwards by a swirl of time. Red only: the clock hands.
- Characters: the hooded adventurer

### 119. e063_1_ok：逆さ時計の塔→時計の針を止める（成功）

保存名：`generated/e063_1_ok.png`

- Scene: Countless gears pour out of a stopped clock tower; the hooded adventurer picks a golden gear from the pile. Red only: the clock hands.
- Characters: the hooded adventurer

### 120. e063_1_ng：逆さ時計の塔→時計の針を止める（失敗）

保存名：`generated/e063_1_ng.png`

- Scene: the hooded adventurer's finger is caught in the stopped hand of a giant clock. Red only: the clock hands.
- Characters: the hooded adventurer

### 121. e063_2_ok：逆さ時計の塔→針を正しい向きに直す（成功）

保存名：`generated/e063_2_ok.png`

- Scene: The hands of a giant clock now turn the right way; below it a lift cage descends into the depths, its door open for the hooded adventurer. Red only: the clock hands.
- Characters: the hooded adventurer

### 122. e063_2_ng：逆さ時計の塔→針を正しい向きに直す（失敗）

保存名：`generated/e063_2_ng.png`

- Scene: the hooded adventurer stands frozen mid-step under a giant clock, ghostly after-images of themselves trailing behind. Red only: the clock hands.
- Characters: the hooded adventurer

### 123. e064_0_ok：黒い聖堂→影と共に祈る（成功）

保存名：`generated/e064_0_ok.png`

- Scene: the hooded adventurer kneels among shadows praying in the pews of an obsidian cathedral; dark wisps flow into them and turn into a faint glow. Red only: the outline of the black flame on the altar.
- Characters: the hooded adventurer

### 124. e064_0_ng：黒い聖堂→影と共に祈る（失敗）

保存名：`generated/e064_0_ng.png`

- Scene: the hooded adventurer kneels in an obsidian cathedral as the praying shadows lean toward them, whispering. Red only: the outline of the black flame.
- Characters: the hooded adventurer

### 125. e064_1_ok：黒い聖堂→黒い炎に手をかざす（成功）

保存名：`generated/e064_1_ok.png`

- Scene: the hooded adventurer holds a hand over a black flame on an obsidian altar; dark curse marks burn away from their arm. Red only: the outline of the black flame.
- Characters: the hooded adventurer

### 126. e064_1_ng：黒い聖堂→黒い炎に手をかざす（失敗）

保存名：`generated/e064_1_ng.png`

- Scene: A black flame climbs up the hooded adventurer's arm from an obsidian altar, leaving a dark scar. Red only: the outline of the black flame.
- Characters: the hooded adventurer

### 127. e064_2_r：黒い聖堂→聖水で炎を消す

保存名：`generated/e064_2_r.png`

- Scene: the hooded adventurer pours holy water on a black flame; freed shadows rise from the pews and vanish upward. Red only: the last ember of the flame.
- Characters: the hooded adventurer

### 128. e065_0_ok：双子の扉→「真実」の扉を開ける（成功）

保存名：`generated/e065_0_ok.png`

- Scene: the hooded adventurer opens the door carved with an open eye and finds a stairway leading down; the pale twins watch. Red only: the ribbons in the twins' hair.
- Characters: the hooded adventurer

### 129. e065_0_ng：双子の扉→「真実」の扉を開ける（失敗）

保存名：`generated/e065_0_ng.png`

- Scene: the hooded adventurer opens a door carved with an open eye onto a solid stone wall; the pale twins laugh behind. Red only: the twins' ribbons.
- Characters: the hooded adventurer

### 130. e065_1_ok：双子の扉→「嘘」の扉を開ける（成功）

保存名：`generated/e065_1_ok.png`

- Scene: the hooded adventurer steps through the door carved with a closed eye onto a true path; the twins pout. Red only: the twins' ribbons.
- Characters: the hooded adventurer

### 131. e065_1_ng：双子の扉→「嘘」の扉を開ける（失敗）

保存名：`generated/e065_1_ng.png`

- Scene: Countless arms reach out from a door carved with a closed eye and drag the hooded adventurer back. Red only: the twins' ribbons.
- Characters: the hooded adventurer

### 132. e065_2_ok：双子の扉→双子に問いかける（成功）

保存名：`generated/e065_2_ok.png`

- Scene: The sulking pale twins point to a hidden third door in the wall for the hooded adventurer. Red only: the twins' ribbons.
- Characters: the hooded adventurer

### 133. e065_2_ng：双子の扉→双子に問いかける（失敗）

保存名：`generated/e065_2_ng.png`

- Scene: the hooded adventurer clutches their head while the pale twins chatter at them from both sides. Red only: the twins' ribbons.
- Characters: the hooded adventurer

### 134. e066_0_ok：竜の骨→宝の山に潜り込む（成功）

保存名：`generated/e066_0_ok.png`

- Scene: the hooded adventurer scrambles out of a dragon's ribcage with arms full of treasure. Red only: a large gem in their arms.
- Characters: the hooded adventurer

### 135. e066_0_ng：竜の骨→宝の山に潜り込む（失敗）

保存名：`generated/e066_0_ng.png`

- Scene: A blast of hot wind and a ghostly dragon's head rise from the bones, scorching the hooded adventurer. Red only: the ghost dragon's eyes.
- Characters: the hooded adventurer

### 136. e066_1_ok：竜の骨→竜の牙を削り取る（成功）

保存名：`generated/e066_1_ok.png`

- Scene: the hooded adventurer carves a piece from a huge dragon fang and holds up a small red amulet made from it. Red only: the amulet.
- Characters: the hooded adventurer

### 137. e066_1_ng：竜の骨→竜の牙を削り取る（失敗）

保存名：`generated/e066_1_ng.png`

- Scene: the hooded adventurer strains against a dragon fang harder than steel, wrist aching. Red only: a large gem on the treasure pile.
- Characters: the hooded adventurer

### 138. e066_2_r：竜の骨→骨の前で黙祷する

保存名：`generated/e066_2_r.png`

- Scene: the hooded adventurer stands in silent prayer before the skull of a huge dragon skeleton; a faint glow rises from the bones. Red only: a large gem on the treasure pile.
- Characters: the hooded adventurer

### 139. e067_0_ok：影の自分→影と戦う（成功）

保存名：`generated/e067_0_ok.png`

- Scene: the hooded adventurer pins their own risen shadow back to the floor with a short sword; the shadow sinks back sulkily. Red only: the shadow's eyes.
- Characters: the hooded adventurer

### 140. e067_0_ng：影の自分→影と戦う（失敗）

保存名：`generated/e067_0_ng.png`

- Scene: A risen shadow of the hooded adventurer matches every sword stroke perfectly, overpowering them. Red only: the shadow's eyes.
- Characters: the hooded adventurer

### 141. e067_1_ok：影の自分→影を受け入れる（成功）

保存名：`generated/e067_1_ok.png`

- Scene: the hooded adventurer and their risen shadow embrace and merge into one in a ruin. Red only: the shadow's eyes.
- Characters: the hooded adventurer

### 142. e067_1_ng：影の自分→影を受け入れる（失敗）

保存名：`generated/e067_1_ng.png`

- Scene: A risen shadow pushes into the hooded adventurer's body, half of the adventurer turning black; they struggle. Red only: the shadow's eyes.
- Characters: the hooded adventurer

### 143. e067_2_r：影の自分→影を光で消し去る

保存名：`generated/e067_2_r.png`

- Scene: the hooded adventurer holds up a torch and their risen shadow shrinks away into nothing. Red only: the torch flame.
- Characters: the hooded adventurer

### 144. e068_0_r：仮面の商人→金貨で薬を買う

保存名：`generated/e068_0_r.png`

- Scene: A merchant in layered masks hands a potion bottle to the hooded adventurer over a stall of hanging masks. Red only: the mouth of the outermost mask.
- Characters: the hooded adventurer

### 145. e068_1_r：仮面の商人→顔の一部と引き換えに力を買う

保存名：`generated/e068_1_r.png`

- Scene: the hooded adventurer stands with a blank smooth patch where part of their face should be in shadow, strength in their stance, beside a mask merchant's stall. Red only: the mouth of the merchant's outer mask.
- Characters: the hooded adventurer

### 146. e068_2_ok：仮面の商人→商人の仮面を一枚剥がす（成功）

保存名：`generated/e068_2_ok.png`

- Scene: the hooded adventurer holds a peeled-off mask; behind it is nothing, and the merchant collapses into empty robes beside the stall. Red only: the mask's mouth.
- Characters: the hooded adventurer

### 147. e068_2_ng：仮面の商人→商人の仮面を一枚剥がす（失敗）

保存名：`generated/e068_2_ng.png`

- Scene: A peeled-off mask clamps itself onto the hooded adventurer's hood, grinning. Red only: the mask's mouth.
- Characters: the hooded adventurer

### 148. e069_0_ok：脈打つ卵→孵る前に壊す（成功）

保存名：`generated/e069_0_ok.png`

- Scene: the hooded adventurer smashes a pulsing fungal egg; black liquid gushes out of the broken shell. Red only: the light fading in the cracks.
- Characters: the hooded adventurer

### 149. e069_0_ng：脈打つ卵→孵る前に壊す（失敗）

保存名：`generated/e069_0_ng.png`

- Scene: Something bursts from a cracked fungal egg and bites the hooded adventurer's arm. Red only: the creature's mouth.
- Characters: the hooded adventurer

### 150. e069_1_ok：脈打つ卵→孵るのを見届ける（成功）

保存名：`generated/e069_1_ok.png`

- Scene: A tiny white dragon hatchling nuzzles the hooded adventurer beside a broken fungal egg, offering a single scale. Red only: the hatchling's eyes.
- Characters: the hooded adventurer

### 151. e069_1_ng：脈打つ卵→孵るのを見届ける（失敗）

保存名：`generated/e069_1_ng.png`

- Scene: the hooded adventurer recoils from an indescribable dark shape unfolding from a fungal egg. Red only: its many eyes.
- Characters: the hooded adventurer

### 152. e069_2_r：脈打つ卵→そっと離れる

保存名：`generated/e069_2_r.png`

- Scene: the hooded adventurer walks away from a pulsing fungal egg; behind them, the shell cracks open. Red only: the light leaking from the cracks.
- Characters: the hooded adventurer

### 153. e070_0_ok：亡者の行進→隊列に紛れ込む（成功）

保存名：`generated/e070_0_ok.png`

- Scene: the hooded adventurer marches hidden among a column of dead soldiers in rusted armour, descending a long stair. Red only: the standard-bearer's banner.
- Characters: the hooded adventurer

### 154. e070_0_ng：亡者の行進→隊列に紛れ込む（失敗）

保存名：`generated/e070_0_ng.png`

- Scene: Dead soldiers in rusted armour turn and surround the hooded adventurer. Red only: the standard-bearer's banner.
- Characters: the hooded adventurer

### 155. e070_1_r：亡者の行進→騎士の誓いを示す

保存名：`generated/e070_1_r.png`

- Scene: A dead standard-bearer raises his sword in salute to the hooded adventurer; the dead soldiers part to open a path. Red only: the banner.
- Characters: the hooded adventurer

### 156. e070_2_ok：亡者の行進→物陰に隠れる（成功）

保存名：`generated/e070_2_ok.png`

- Scene: the hooded adventurer hides behind ruined masonry as a column of dead soldiers passes. Red only: the banner.
- Characters: the hooded adventurer

### 157. e070_2_ng：亡者の行進→物陰に隠れる（失敗）

保存名：`generated/e070_2_ng.png`

- Scene: The last dead soldier in a column turns its empty helmet toward the hooded adventurer hiding behind masonry. Red only: the banner.
- Characters: the hooded adventurer

### 158. e071_0_r：魔女の再訪→印を返す

保存名：`generated/e071_0_r.png`

- Scene: The swamp witch peels a glowing mark off the hooded adventurer's neck with long fingers, grinning. Red only: the mark.
- Characters: the hooded adventurer

### 159. e071_1_r：魔女の再訪→薬の調合を頼む

保存名：`generated/e071_1_r.png`

- Scene: The swamp witch hands the hooded adventurer two potion bottles beside her cauldron. Red only: the potions.
- Characters: the hooded adventurer

### 160. e071_2_ok：魔女の再訪→迷宮の底について訊く（成功）

保存名：`generated/e071_2_ok.png`

- Scene: The swamp witch tells a tale over her cauldron; in the steam, a ghostly vision of a weeping woman wearing a ring walks into darkness toward a giant eye. the hooded adventurer listens. Red only: the giant eye in the vision.
- Characters: the hooded adventurer

### 161. e071_2_ng：魔女の再訪→迷宮の底について訊く（失敗）

保存名：`generated/e071_2_ng.png`

- Scene: the hooded adventurer stares blankly as the swamp witch speaks, the words drifting away like smoke. Red only: the sand in an hourglass.
- Characters: the hooded adventurer

### 162. e072_1_r：最後のメモ→メモを胸に抱く

保存名：`generated/e072_1_r.png`

- Scene: the hooded adventurer holds a handwritten note to their chest beside a wall of living flesh, head bowed. Red only: the veins in the flesh wall.
- Characters: the hooded adventurer

### 163. e072_2_r：最後のメモ→破り捨てる

保存名：`generated/e072_2_r.png`

- Scene: Scraps of a torn note flutter in the air beside a wall of flesh, and a faint wailing woman's face appears in the flesh; the hooded adventurer steps back. Red only: the veins in the wall.
- Characters: the hooded adventurer

### 164. e073_0_ok：沈黙の司書→筆談で道を尋ねる（成功）

保存名：`generated/e073_0_ok.png`

- Scene: A librarian with a sewn mouth hands the hooded adventurer an open book showing a maze map. Red only: the thread on his mouth.
- Characters: the hooded adventurer

### 165. e073_0_ng：沈黙の司書→筆談で道を尋ねる（失敗）

保存名：`generated/e073_0_ng.png`

- Scene: the hooded adventurer covers their mouth as many librarians with sewn mouths emerge from the shelves. Red only: the threads on their mouths.
- Characters: the hooded adventurer

### 166. e073_1_ok：沈黙の司書→音を立てずに本を盗む（成功）

保存名：`generated/e073_1_ok.png`

- Scene: the hooded adventurer slips an old book under their cloak in silence between tall shelves. Red only: the book's ribbon.
- Characters: the hooded adventurer

### 167. e073_1_ng：沈黙の司書→音を立てずに本を盗む（失敗）

保存名：`generated/e073_1_ng.png`

- Scene: A tall bookshelf topples with a crash next to the hooded adventurer, books flying. Red only: a librarian's sewn mouth in the background.
- Characters: the hooded adventurer

### 168. e073_2_ok：沈黙の司書→静かに通り抜ける（成功）

保存名：`generated/e073_2_ok.png`

- Scene: the hooded adventurer tiptoes silently through a maze of tall bookshelves. Red only: a librarian's sewn mouth in the distance.
- Characters: the hooded adventurer

### 169. e073_2_ng：沈黙の司書→静かに通り抜ける（失敗）

保存名：`generated/e073_2_ng.png`

- Scene: the hooded adventurer stumbles noisily against a bookshelf, books falling; a librarian turns. Red only: the librarian's sewn mouth.
- Characters: the hooded adventurer

### 170. e074_0_ok：血の泉→泉の血を飲む（成功）

保存名：`generated/e074_0_ok.png`

- Scene: the hooded adventurer drinks blood from a fountain with cupped hands; wounds on their arms close. Red only: the blood.
- Characters: the hooded adventurer

### 171. e074_0_ng：血の泉→泉の血を飲む（失敗）

保存名：`generated/e074_0_ng.png`

- Scene: the hooded adventurer drinks from a blood fountain, eyes hungry. Red only: the blood.
- Characters: the hooded adventurer

### 172. e074_1_r：血の泉→傷口を泉に浸す

保存名：`generated/e074_1_r.png`

- Scene: the hooded adventurer dips a wounded arm in a blood fountain; thin streams of their own blood are drawn into it. Red only: the blood.
- Characters: the hooded adventurer

### 173. e074_2_r：血の泉→泉に聖水を注ぐ

保存名：`generated/e074_2_r.png`

- Scene: A fountain once full of blood now runs with clear water after holy water is poured in; the hooded adventurer drinks. Red only: a last drop of blood on the rim.
- Characters: the hooded adventurer

### 174. e075_0_ok：吊るされた人々→助け下ろす（成功）

保存名：`generated/e075_0_ok.png`

- Scene: the hooded adventurer cuts down people hanging from fungal threads under a giant mushroom; the rescued kneel in thanks. Red only: a red cloth one of them offers.
- Characters: the hooded adventurer

### 175. e075_0_ng：吊るされた人々→助け下ろす（失敗）

保存名：`generated/e075_0_ng.png`

- Scene: Fungal threads wrap around the hooded adventurer's arm and lift them toward a giant mushroom's cap. Red only: the eyes of a hanging person.
- Characters: the hooded adventurer

### 176. e075_1_ok：吊るされた人々→せめて楽にしてやる（成功）

保存名：`generated/e075_1_ok.png`

- Scene: the hooded adventurer kneels in prayer beneath people hanging from fungal threads, now at peace. Red only: a single candle flame.
- Characters: the hooded adventurer

### 177. e075_1_ng：吊るされた人々→せめて楽にしてやる（失敗）

保存名：`generated/e075_1_ng.png`

- Scene: A hanging person reaches toward the hooded adventurer with their last breath. Red only: the person's eyes.
- Characters: the hooded adventurer

### 178. e075_2_r：吊るされた人々→見なかったことにする

保存名：`generated/e075_2_r.png`

- Scene: the hooded adventurer walks away from a giant mushroom with hanging people; fungal threads reach after them. Red only: the eyes of the one still alive.
- Characters: the hooded adventurer

### 179. e076_0_ok：忘却の川→一口だけ飲む（成功）

保存名：`generated/e076_0_ok.png`

- Scene: the hooded adventurer sips from a grey river; a dark memory image drifts away down the current. Red only: a small flower floating on the water.
- Characters: the hooded adventurer

### 180. e076_0_ng：忘却の川→一口だけ飲む（失敗）

保存名：`generated/e076_0_ng.png`

- Scene: the hooded adventurer kneels by a grey river, dazed, many memory images floating away. Red only: a small flower floating away.
- Characters: the hooded adventurer

### 181. e076_1_r：忘却の川→記憶を一つ川に流す

保存名：`generated/e076_1_r.png`

- Scene: the hooded adventurer lets a glowing memory slip from their hands into a grey river. Red only: the memory image, a small flower.
- Characters: the hooded adventurer

### 182. e076_2_ok：忘却の川→川を渡る（成功）

保存名：`generated/e076_2_ok.png`

- Scene: the hooded adventurer hops across stepping stones over a grey river of memories. Red only: a small flower floating on the water.
- Characters: the hooded adventurer

### 183. e076_2_ng：忘却の川→川を渡る（失敗）

保存名：`generated/e076_2_ng.png`

- Scene: the hooded adventurer has fallen into a grey river, memories streaming out of them like mist. Red only: a small flower floating away.
- Characters: the hooded adventurer

### 184. e077_0_ok：鉄の処女→扉を開ける（成功）

保存名：`generated/e077_0_ok.png`

- Scene: An opened iron maiden is empty inside; a gem rests on its inner spikes, offered to the hooded adventurer. Red only: the gem.
- Characters: the hooded adventurer

### 185. e077_0_ng：鉄の処女→扉を開ける（失敗）

保存名：`generated/e077_0_ng.png`

- Scene: The doors of an iron maiden swing shut toward the hooded adventurer as if to embrace them. Red only: the blood at the gap.
- Characters: the hooded adventurer

### 186. e077_1_ok：鉄の処女→歌声に耳を傾ける（成功）

保存名：`generated/e077_1_ok.png`

- Scene: An iron maiden rusts and crumbles to flakes while the hooded adventurer listens quietly. Red only: a last trickle of blood.
- Characters: the hooded adventurer

### 187. e077_1_ng：鉄の処女→歌声に耳を傾ける（失敗）

保存名：`generated/e077_1_ng.png`

- Scene: the hooded adventurer clutches their head, thorny dark lines around it, beside an iron maiden. Red only: the blood at the gap.
- Characters: the hooded adventurer

### 188. e077_2_ok：鉄の処女→部屋の拷問具を壊して回る（成功）

保存名：`generated/e077_2_ok.png`

- Scene: the hooded adventurer stands among smashed torture devices; the room's gloom lifts. Red only: a broken chain link.
- Characters: the hooded adventurer

### 189. e077_2_ng：鉄の処女→部屋の拷問具を壊して回る（失敗）

保存名：`generated/e077_2_ng.png`

- Scene: Torture devices start moving by themselves toward the hooded adventurer: chains rattle and a rack turns. Red only: the blood on the devices.
- Characters: the hooded adventurer

### 190. e078_0_ok：眠る巨人→荷物を回収する（成功）

保存名：`generated/e078_0_ok.png`

- Scene: the hooded adventurer hurries out of a sleeping giant's mouth with a pack of salvaged gear. Red only: the torn banner among the gear.
- Characters: the hooded adventurer

### 191. e078_0_ng：眠る巨人→荷物を回収する（失敗）

保存名：`generated/e078_0_ng.png`

- Scene: A giant's sneeze blasts the hooded adventurer out of its mouth through the air. Red only: the torn banner flying.
- Characters: the hooded adventurer

### 192. e078_1_ok：眠る巨人→喉の奥へ進む（成功）

保存名：`generated/e078_1_ok.png`

- Scene: the hooded adventurer slides down a giant's throat and emerges into a lower cavern. Red only: a faint red glow of the throat.
- Characters: the hooded adventurer

### 193. e078_1_ng：眠る巨人→喉の奥へ進む（失敗）

保存名：`generated/e078_1_ng.png`

- Scene: the hooded adventurer flees up a giant's throat, steam of stomach acid rising behind. Red only: the acid's glow.
- Characters: the hooded adventurer

### 194. e078_2_ok：眠る巨人→息を潜めて口から出る（成功）

保存名：`generated/e078_2_ok.png`

- Scene: the hooded adventurer tiptoes out between a sleeping giant's teeth in rhythm with its breathing. Red only: the torn banner on the tongue.
- Characters: the hooded adventurer

### 195. e078_2_ng：眠る巨人→息を潜めて口から出る（失敗）

保存名：`generated/e078_2_ng.png`

- Scene: the hooded adventurer is stuck between a giant's teeth as the giant rolls over. Red only: the torn banner on the tongue.
- Characters: the hooded adventurer

### 196. e079_1_r：少女の記憶→手を握ってやる

保存名：`generated/e079_1_r.png`

- Scene: the hooded adventurer holds the cold small hand of the ghost girl, who smiles slightly. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 197. e079_2_r：少女の記憶→先を急ぐ

保存名：`generated/e079_2_r.png`

- Scene: the ghost girl tugs the sleeve of the hooded adventurer, leading the way down a ruined street. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 198. n01_0_ok：王の命令書→布告を最後まで読む（成功）

保存名：`generated/n01_0_ok.png`

- Scene: the hooded adventurer reads a faded proclamation on a cracked wall, its writing illegible; in the margin one small shaky line of illegible handwriting stands out. Red only: the royal wax seal.
- Characters: the hooded adventurer

### 199. n01_0_ng：王の命令書→布告を最後まで読む（失敗）

保存名：`generated/n01_0_ng.png`

- Scene: the hooded adventurer stares at a proclamation whose blurred writing runs like ink; one line glows sharply but is illegible. Red only: the royal wax seal.
- Characters: the hooded adventurer

### 200. n01_1_r：王の命令書→封蝋を剥がして持ち帰る

保存名：`generated/n01_1_r.png`

- Scene: the hooded adventurer holds a royal wax seal in their palm in front of a proclamation on a wall. Red only: the wax seal.
- Characters: the hooded adventurer

### 201. n01_2_r：王の命令書→布告を破り捨てる

保存名：`generated/n01_2_r.png`

- Scene: the hooded adventurer tears down a proclamation, revealing many identical proclamations pasted beneath it. Red only: the wax seals.
- Characters: the hooded adventurer

### 202. n02_0_r：隔離塔→少女の手を握る

保存名：`generated/n02_0_r.png`

- Scene: Inside a cold tower cell, the ghost girl grips the hand of the hooded adventurer tightly beside a small bed, looking down. Red only: the crest pendant on her chest.
- Characters: the hooded adventurer, the ghost girl

### 203. n02_2_r：隔離塔→寝台を整える

保存名：`generated/n02_2_r.png`

- Scene: the hooded adventurer smooths the sheets of a small cold bed in a tower cell, child's chalk drawings on the wall. Red only: the drawing of a mother and child.
- Characters: the hooded adventurer

### 204. n02_3_r：隔離塔→塔に入らず立ち去る

保存名：`generated/n02_3_r.png`

- Scene: the hooded adventurer walks away from a leaning sunken tower; from its dark window, a tiny pale face looks out. Red only: the painted cross on the door.
- Characters: the hooded adventurer

### 205. n03_0_r：騎士の告白→話を聞く

保存名：`generated/n03_0_r.png`

- Scene: the ghost knight, holding his helmet, tells his story in a ruin; above him a ghostly vision shows an armoured man pulling a feverish child from a weeping woman's arms. the hooded adventurer listens. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 206. n03_1_ng：騎士の告白→「あなたのせいではない」と言う（失敗）

保存名：`generated/n03_1_ng.png`

- Scene: the ghost knight turns his back on the hooded adventurer, shoulders hunched, in a ruin. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 207. n03_2_r：騎士の告白→黙って隣に立つ

保存名：`generated/n03_2_r.png`

- Scene: the hooded adventurer stands silently beside the ghost knight in a ruin, both looking into the darkness. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 208. g075_2_ok：深淵の竜→竜の背に飛び乗る（成功）

保存名：`generated/g075_2_ok.png`

- Scene: the hooded adventurer clings to the spine of a huge skeletal dragon diving down into a chasm. Red only: the fire in the dragon's eye sockets.
- Characters: the hooded adventurer

### 209. g075_2_ng：深淵の竜→竜の背に飛び乗る（失敗）

保存名：`generated/g075_2_ng.png`

- Scene: the hooded adventurer tumbles down rocky ledges of a chasm, thrown off a skeletal dragon above. Red only: the dragon's burning eyes.
- Characters: the hooded adventurer

### 210. g075_3_ok：深淵の竜→竜の怒りを鎮める（成功）

保存名：`generated/g075_3_ok.png`

- Scene: the hooded adventurer stands before a huge skeletal dragon as the fire in its eye sockets quietly goes out; it lowers its head. Red only: the last embers in the eye sockets.
- Characters: the hooded adventurer

### 211. g075_3_ng：深淵の竜→竜の怒りを鎮める（失敗）

保存名：`generated/g075_3_ng.png`

- Scene: A huge skeletal dragon roars at the hooded adventurer, the shockwave tearing at their cloak. Red only: the dragon's burning eyes.
- Characters: the hooded adventurer

### 212. g075_4_ok：深淵の竜→影に紛れて裂溝を降りる（成功）

保存名：`generated/g075_4_ok.png`

- Scene: the hooded adventurer climbs down a chasm wall in shadow while a skeletal dragon searches above. Red only: the dragon's burning eyes.
- Characters: the hooded adventurer

### 213. g075_4_ng：深淵の竜→影に紛れて裂溝を降りる（失敗）

保存名：`generated/g075_4_ng.png`

- Scene: Dragon fire scorches the hooded adventurer's back on a chasm wall. Red only: the dragon fire.
- Characters: the hooded adventurer

### 214. e080_0_ok：肉の回廊→肉を切り裂いて近道を作る（成功）

保存名：`generated/e080_0_ok.png`

- Scene: the hooded adventurer cuts open a flesh wall and climbs through to a lower passage. Red only: the cut in the flesh.
- Characters: the hooded adventurer

### 215. e080_0_ng：肉の回廊→肉を切り裂いて近道を作る（失敗）

保存名：`generated/e080_0_ng.png`

- Scene: A wounded flesh corridor contracts around the hooded adventurer, squeezing. Red only: the largest veins.
- Characters: the hooded adventurer

### 216. e080_1_ok：肉の回廊→心音に合わせて歩く（成功）

保存名：`generated/e080_1_ok.png`

- Scene: the hooded adventurer walks in rhythm through a flesh corridor, the walls calm around them. Red only: the largest veins, glowing faintly.
- Characters: the hooded adventurer

### 217. e080_1_ng：肉の回廊→心音に合わせて歩く（失敗）

保存名：`generated/e080_1_ng.png`

- Scene: the hooded adventurer clutches their chest in a flesh corridor as the walls pulse in time with their heart. Red only: the veins pulsing.
- Characters: the hooded adventurer

### 218. e080_2_r：肉の回廊→何も考えずに進む

保存名：`generated/e080_2_r.png`

- Scene: the hooded adventurer trudges through a flesh corridor, eyes fixed ahead. Red only: the largest veins.
- Characters: the hooded adventurer

### 219. e081_0_r：眼の群れ→第三の眼で睨み返す

保存名：`generated/e081_0_r.png`

- Scene: the hooded adventurer, with a glowing third eye on their brow, stares down a wall of eyes; all the eyes close at once. Red only: the third eye.
- Characters: the hooded adventurer

### 220. e081_1_ok：眼の群れ→目を閉じて手探りで進む（成功）

保存名：`generated/e081_1_ok.png`

- Scene: the hooded adventurer feels their way along a wall of eyes with eyes shut. Red only: the irises of the largest eyes.
- Characters: the hooded adventurer

### 221. e081_1_ng：眼の群れ→目を閉じて手探りで進む（失敗）

保存名：`generated/e081_1_ng.png`

- Scene: the hooded adventurer walks with eyes shut, but faint eyes float in the darkness around their head. Red only: the floating eyes' irises.
- Characters: the hooded adventurer

### 222. e081_2_ok：眼の群れ→眼を潰して回る（成功）

保存名：`generated/e081_2_ok.png`

- Scene: the hooded adventurer stands in a silent passage where every eye in the walls is closed. Red only: one last closing eye.
- Characters: the hooded adventurer

### 223. e081_2_ng：眼の群れ→眼を潰して回る（失敗）

保存名：`generated/e081_2_ng.png`

- Scene: the hooded adventurer recoils as fluid from a burst eye burns their hand. Red only: the burn.
- Characters: the hooded adventurer

### 224. e081_3_ok：眼の群れ→見つめられることを受け入れる（成功）

保存名：`generated/e081_3_ok.png`

- Scene: the hooded adventurer gazes back at a wall of eyes, which now look sorrowful, glistening with tears. Red only: the irises of the largest eyes.
- Characters: the hooded adventurer

### 225. e081_3_ng：眼の群れ→見つめられることを受け入れる（失敗）

保存名：`generated/e081_3_ng.png`

- Scene: the hooded adventurer grows faint and translucent under the stare of countless eyes. Red only: the irises of the largest eyes.
- Characters: the hooded adventurer

### 226. e082_0_ok：心臓の間→結晶をえぐり取る（成功）

保存名：`generated/e082_0_ok.png`

- Scene: the hooded adventurer tears a glowing crystal out of a gigantic heart; the flesh chamber convulses. Red only: the crystal.
- Characters: the hooded adventurer

### 227. e082_0_ng：心臓の間→結晶をえぐり取る（失敗）

保存名：`generated/e082_0_ng.png`

- Scene: A gigantic heart convulses and a flood of dark fluid sweeps the hooded adventurer away. Red only: the glowing crystal.
- Characters: the hooded adventurer

### 228. e082_1_ng：心臓の間→心臓に手を当てる（失敗）

保存名：`generated/e082_1_ng.png`

- Scene: the hooded adventurer presses a palm to a gigantic heart and doubles over in pain. Red only: the glowing crystal.
- Characters: the hooded adventurer

### 229. e082_2_r：心臓の間→静かに部屋を出る

保存名：`generated/e082_2_r.png`

- Scene: the hooded adventurer leaves a flesh chamber quietly while a gigantic heart beats behind them. Red only: the glowing crystal.
- Characters: the hooded adventurer

### 230. e083_0_ok：手の海→手の上を渡る（成功）

保存名：`generated/e083_0_ok.png`

- Scene: the hooded adventurer leaps from hand to hand across a sea of pale reaching hands. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 231. e083_0_ng：手の海→手の上を渡る（失敗）

保存名：`generated/e083_0_ng.png`

- Scene: Pale hands grab the hooded adventurer and drag them into a sea of hands. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 232. e083_1_ok：手の海→手に身を委ねる（成功）

保存名：`generated/e083_1_ok.png`

- Scene: A sea of pale hands gently carries the hooded adventurer on their palms toward the far shore. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 233. e083_1_ng：手の海→手に身を委ねる（失敗）

保存名：`generated/e083_1_ng.png`

- Scene: Pale hands pull the hooded adventurer in different directions, fighting over them. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 234. e083_2_ok：手の海→手を一つずつ握り返す（成功）

保存名：`generated/e083_2_ok.png`

- Scene: the hooded adventurer grips pale hands one by one; they sink away contentedly, opening a path. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 235. e083_2_ng：手の海→手を一つずつ握り返す（失敗）

保存名：`generated/e083_2_ng.png`

- Scene: Countless pale hands cling to the hooded adventurer's hand and will not let go. Red only: the faint glow on the far shore.
- Characters: the hooded adventurer

### 236. e084_0_ok：堕ちた天使→鎖を断つ（成功）

保存名：`generated/e084_0_ok.png`

- Scene: A freed fallen angel, chains broken, wraps its one remaining wing around the hooded adventurer. Red only: the eye on the rotted half of its face.
- Characters: the hooded adventurer

### 237. e084_0_ng：堕ちた天使→鎖を断つ（失敗）

保存名：`generated/e084_0_ng.png`

- Scene: A chained fallen angel breathes out a dark cursed mist over the hooded adventurer, whose sword has failed to cut the chain. Red only: the eye on the rotted half of its face.
- Characters: the hooded adventurer

### 238. e084_1_ok：堕ちた天使→天使の正体を見極める（成功）

保存名：`generated/e084_1_ok.png`

- Scene: A fallen angel, its rotted half now dominant, vanishes in disgust, leaving only empty chains before the hooded adventurer. Red only: a last glint in the hanging chains.
- Characters: the hooded adventurer

### 239. e084_1_ng：堕ちた天使→天使の正体を見極める（失敗）

保存名：`generated/e084_1_ng.png`

- Scene: the hooded adventurer gazes enchanted at the beautiful half of a fallen angel's face while a glowing wisp is drawn from their chest. Red only: the eye on the rotted half of its face.
- Characters: the hooded adventurer

### 240. e084_2_r：堕ちた天使→聖水を捧げる

保存名：`generated/e084_2_r.png`

- Scene: A fallen angel, rotted half and all, dissolves into light as the hooded adventurer offers holy water. Red only: the eye on the rotted half, fading.
- Characters: the hooded adventurer

### 241. e085_0_ok：名前を呼ぶ声→振り向く（成功）

保存名：`generated/e085_0_ok.png`

- Scene: the hooded adventurer has turned around in total darkness and sees, for one moment, a faint warm figure of someone dear smiling. Red only: the figure's lips.
- Characters: the hooded adventurer

### 242. e085_0_ng：名前を呼ぶ声→振り向く（失敗）

保存名：`generated/e085_0_ng.png`

- Scene: the hooded adventurer has turned around in total darkness to face a pale face with only a mouth and no other features. Red only: the mouth.
- Characters: the hooded adventurer

### 243. e085_1_ok：名前を呼ぶ声→振り向かずに進む（成功）

保存名：`generated/e085_1_ok.png`

- Scene: the hooded adventurer walks forward in total darkness without turning; behind them the pale figures fade away. Red only: the nearest figure's lips.
- Characters: the hooded adventurer

### 244. e085_1_ng：名前を呼ぶ声→振り向かずに進む（失敗）

保存名：`generated/e085_1_ng.png`

- Scene: the hooded adventurer walks in total darkness with a pale mouth whispering right at their ear. Red only: the lips.
- Characters: the hooded adventurer

### 245. e085_2_ok：名前を呼ぶ声→耳を塞いで走る（成功）

保存名：`generated/e085_2_ok.png`

- Scene: the hooded adventurer runs through total darkness with hands over their ears, leaving the pale figures behind. Red only: the figures' lips.
- Characters: the hooded adventurer

### 246. e085_2_ng：名前を呼ぶ声→耳を塞いで走る（失敗）

保存名：`generated/e085_2_ng.png`

- Scene: the hooded adventurer has fallen in total darkness as pale figures close in around them. Red only: the figures' lips.
- Characters: the hooded adventurer

### 247. e086_0_ok：逆さまの階段→逆立ちで登る（成功）

保存名：`generated/e086_0_ok.png`

- Scene: the hooded adventurer climbs an impossible twisting staircase upside down, walking on the underside of the steps. Red only: the lantern hanging upside down.
- Characters: the hooded adventurer

### 248. e086_0_ng：逆さまの階段→逆立ちで登る（失敗）

保存名：`generated/e086_0_ng.png`

- Scene: the hooded adventurer clutches their head, dizzy, on an impossible staircase that spirals in every direction. Red only: the upside-down lantern.
- Characters: the hooded adventurer

### 249. e086_1_ok：逆さまの階段→目を閉じて足の感覚に従う（成功）

保存名：`generated/e086_1_ok.png`

- Scene: the hooded adventurer descends an impossible staircase step by step with eyes closed. Red only: the upside-down lantern.
- Characters: the hooded adventurer

### 250. e086_1_ng：逆さまの階段→目を閉じて足の感覚に従う（失敗）

保存名：`generated/e086_1_ng.png`

- Scene: the hooded adventurer walks an impossible staircase that loops back on itself, faint copies of them on every flight. Red only: the upside-down lantern.
- Characters: the hooded adventurer

### 251. e086_2_ok：逆さまの階段→手すりを乗り越えて飛び降りる（成功）

保存名：`generated/e086_2_ok.png`

- Scene: the hooded adventurer falls through twisted space past impossible staircases toward a floor far below. Red only: the upside-down lantern.
- Characters: the hooded adventurer

### 252. e086_2_ng：逆さまの階段→手すりを乗り越えて飛び降りる（失敗）

保存名：`generated/e086_2_ng.png`

- Scene: the hooded adventurer lands on a staircase landing that is above where they jumped from, staring up in confusion. Red only: the upside-down lantern.
- Characters: the hooded adventurer

### 253. e087_0_ok：自分の死体→死体の手から取る（成功）

保存名：`generated/e087_0_ok.png`

- Scene: the hooded adventurer kneels by their own corpse and takes a red amulet from its hand. Red only: the amulet.
- Characters: the hooded adventurer

### 254. e087_0_ng：自分の死体→死体の手から取る（失敗）

保存名：`generated/e087_0_ng.png`

- Scene: The eyes of the corpse that looks like the hooded adventurer have opened, glowing, staring up at them. Red only: the corpse's eyes.
- Characters: the hooded adventurer

### 255. e087_1_ok：自分の死体→死因を調べる（成功）

保存名：`generated/e087_1_ok.png`

- Scene: the hooded adventurer kneels examining their own corpse, finding a wound at its side; they nod grimly. Red only: the wound.
- Characters: the hooded adventurer

### 256. e087_1_ng：自分の死体→死因を調べる（失敗）

保存名：`generated/e087_1_ng.png`

- Scene: the hooded adventurer kneels by their own corpse, their own hands turning pale and translucent. Red only: the corpse's wound.
- Characters: the hooded adventurer

### 257. e087_2_r：自分の死体→埋葬する

保存名：`generated/e087_2_r.png`

- Scene: the hooded adventurer pats down a fresh grave mound in a passage, a lantern set on top. Red only: a small red flower on the grave.
- Characters: the hooded adventurer

### 258. e088_0_ok：深淵の司祭→司祭を斬る（成功）

保存名：`generated/e088_0_ok.png`

- Scene: the hooded adventurer slashes a tentacle-crowned priest, who laughs as he falls. Red only: the priest's eyes.
- Characters: the hooded adventurer

### 259. e088_0_ng：深淵の司祭→司祭を斬る（失敗）

保存名：`generated/e088_0_ng.png`

- Scene: Tentacles from a priest's crown wrap around and squeeze the hooded adventurer. Red only: the priest's eyes.
- Characters: the hooded adventurer

### 260. e088_1_ok：深淵の司祭→信者のふりをする（成功）

保存名：`generated/e088_1_ok.png`

- Scene: A tentacle-crowned priest opens a dark doorway behind the altar for the hooded adventurer, who bows like a believer. Red only: the priest's eyes.
- Characters: the hooded adventurer

### 261. e088_1_ng：深淵の司祭→信者のふりをする（失敗）

保存名：`generated/e088_1_ng.png`

- Scene: A tentacle-crowned priest's eyes turn cold as the hooded adventurer kneels in false prayer. Red only: the priest's eyes.
- Characters: the hooded adventurer

### 262. e088_2_ok：深淵の司祭→祭壇を叩き壊す（成功）

保存名：`generated/e088_2_ok.png`

- Scene: A black altar shatters under the hooded adventurer's blow; the tentacle-crowned priest screams and crumbles to dust. Red only: the priest's eyes.
- Characters: the hooded adventurer

### 263. e088_2_ng：深淵の司祭→祭壇を叩き壊す（失敗）

保存名：`generated/e088_2_ng.png`

- Scene: Shards of a shattered black altar rain down on the hooded adventurer as dark curses. Red only: the glowing shards.
- Characters: the hooded adventurer

### 264. e089_0_ok：星の落ちる井戸→星に願う（成功）

保存名：`generated/e089_0_ok.png`

- Scene: A small star falls from the void into the cupped hands of the hooded adventurer beside a stone well. Red only: the star.
- Characters: the hooded adventurer

### 265. e089_0_ng：星の落ちる井戸→星に願う（失敗）

保存名：`generated/e089_0_ng.png`

- Scene: the hooded adventurer stands at a stone well full of stars; a small light dims in their own chest. Red only: the fading light in the chest.
- Characters: the hooded adventurer

### 266. e089_1_ok：星の落ちる井戸→井戸に飛び込む（成功）

保存名：`generated/e089_1_ok.png`

- Scene: the hooded adventurer falls into a well of stars, rising through a starry sky inside it. Red only: one star.
- Characters: the hooded adventurer

### 267. e089_1_ng：星の落ちる井戸→井戸に飛び込む（失敗）

保存名：`generated/e089_1_ng.png`

- Scene: the hooded adventurer drags themselves back over the rim of a well of stars, frost on their cloak. Red only: one rising star.
- Characters: the hooded adventurer

### 268. e089_2_ok：星の落ちる井戸→井戸の水を汲む（成功）

保存名：`generated/e089_2_ok.png`

- Scene: the hooded adventurer drinks water glittering with stardust from a bucket at a well in the void. Red only: one star in the water.
- Characters: the hooded adventurer

### 269. e089_2_ng：星の落ちる井戸→井戸の水を汲む（失敗）

保存名：`generated/e089_2_ng.png`

- Scene: the hooded adventurer holds a rope-burned hand beside a heavy bucket at a well in the void. Red only: the rope burn.
- Characters: the hooded adventurer

### 270. e090_0_ok：喰らうもの→歯の間を駆け抜ける（成功）

保存名：`generated/e090_0_ok.png`

- Scene: the hooded adventurer dives between the closing teeth of a passage-sized mouth and out the other side. Red only: the glow deep in the throat.
- Characters: the hooded adventurer

### 271. e090_0_ng：喰らうもの→歯の間を駆け抜ける（失敗）

保存名：`generated/e090_0_ng.png`

- Scene: The teeth of a passage-sized mouth bite into the hooded adventurer's leg. Red only: the wound.
- Characters: the hooded adventurer

### 272. e090_1_ok：喰らうもの→口の主に話しかける（成功）

保存名：`generated/e090_1_ok.png`

- Scene: A passage-sized mouth yawns wide open, letting the hooded adventurer walk through. Red only: the glow deep in the throat.
- Characters: the hooded adventurer

### 273. e090_1_ng：喰らうもの→口の主に話しかける（失敗）

保存名：`generated/e090_1_ng.png`

- Scene: A passage-sized mouth slowly closes around the hooded adventurer as they talk. Red only: the glow deep in the throat.
- Characters: the hooded adventurer

### 274. e090_2_ok：喰らうもの→口に何かを食わせる（成功）

保存名：`generated/e090_2_ok.png`

- Scene: A passage-sized mouth chews dried meat and falls asleep as the hooded adventurer slips past. Red only: the glow deep in the throat.
- Characters: the hooded adventurer

### 275. e090_2_ng：喰らうもの→口に何かを食わせる（失敗）

保存名：`generated/e090_2_ng.png`

- Scene: A passage-sized mouth bites the hooded adventurer's arm along with their pack. Red only: the glow deep in the throat.
- Characters: the hooded adventurer

### 276. e091_0_ok：鏡の迷宮→自分たちの声に従う（成功）

保存名：`generated/e091_0_ok.png`

- Scene: In a maze of mirrors, the dead reflections of the hooded adventurer all point the same way, and the adventurer follows. Red only: the reflections' eyes.
- Characters: the hooded adventurer

### 277. e091_0_ng：鏡の迷宮→自分たちの声に従う（失敗）

保存名：`generated/e091_0_ng.png`

- Scene: the hooded adventurer clutches their head in a maze of mirrors while dead reflections shout in every direction. Red only: the reflections' eyes.
- Characters: the hooded adventurer

### 278. e091_1_ok：鏡の迷宮→鏡を全て割る（成功）

保存名：`generated/e091_1_ok.png`

- Scene: Mirrors shatter around the hooded adventurer, revealing a true exit glowing beyond. Red only: the reflections' eyes in the falling shards.
- Characters: the hooded adventurer

### 279. e091_1_ng：鏡の迷宮→鏡を全て割る（失敗）

保存名：`generated/e091_1_ng.png`

- Scene: Dead reflections reach out of shattered mirrors toward the hooded adventurer. Red only: the reflections' eyes.
- Characters: the hooded adventurer

### 280. e091_2_ok：鏡の迷宮→自分の直感だけを信じる（成功）

保存名：`generated/e091_2_ok.png`

- Scene: the hooded adventurer walks on through a maze of mirrors, ignoring the shouting reflections. Red only: the reflections' eyes.
- Characters: the hooded adventurer

### 281. e091_2_ng：鏡の迷宮→自分の直感だけを信じる（失敗）

保存名：`generated/e091_2_ng.png`

- Scene: the hooded adventurer walks confidently into a mirror maze dead end where a reflection grins. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 282. e092_1_ok：騎士の亡霊→安らかに眠らせる（成功）

保存名：`generated/e092_1_ok.png`

- Scene: the ghost knight fades peacefully into light in a black void, bowing to the hooded adventurer. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 283. e092_1_ng：騎士の亡霊→安らかに眠らせる（失敗）

保存名：`generated/e092_1_ng.png`

- Scene: the ghost knight shakes his empty helmet at the hooded adventurer in a black void, refusing to rest. Red only: the crown crest on the tabard.
- Characters: the hooded adventurer, the ghost knight

### 284. e092_2_r：騎士の亡霊→最後の戦いの話を聞く

保存名：`generated/e092_2_r.png`

- Scene: the ghost knight tells his story in a black void; above him a ghostly vision of a mother holding her child, swallowed by a giant eye. the hooded adventurer listens. Red only: the giant eye.
- Characters: the hooded adventurer, the ghost knight

### 285. e093_0_r：最後の商人→体と引き換えに心を癒す

保存名：`generated/e093_0_r.png`

- Scene: the faceless peddler nods contentedly to the hooded adventurer in a black void as a glowing wisp flows from the adventurer's body. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 286. e093_1_r：最後の商人→心と引き換えに体を癒す

保存名：`generated/e093_1_r.png`

- Scene: the faceless peddler hands the hooded adventurer a potion in a black void, bowing. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 287. e093_2_r：最後の商人→運命と引き換えにお守りを買う

保存名：`generated/e093_2_r.png`

- Scene: the faceless peddler hands the hooded adventurer a red amulet in a black void. Red only: the amulet.
- Characters: the hooded adventurer, the faceless peddler

### 288. e093_3_r：最後の商人→金貨で全てを少しずつ

保存名：`generated/e093_3_r.png`

- Scene: the faceless peddler accepts coins from the hooded adventurer with a shrug in a black void. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 289. e094_0_ok：赤い月→月が孵る前に駆け抜ける（成功）

保存名：`generated/e094_0_ok.png`

- Scene: the hooded adventurer runs across a rocky ridge as a giant moon overhead cracks open behind them. Red only: the moon.
- Characters: the hooded adventurer

### 290. e094_0_ng：赤い月→月が孵る前に駆け抜ける（失敗）

保存名：`generated/e094_0_ng.png`

- Scene: Red light spills from a cracking giant moon and burns the hooded adventurer on a rocky ridge. Red only: the moon and its spilling light.
- Characters: the hooded adventurer

### 291. e094_1_ok：赤い月→月を見上げて祈る（成功）

保存名：`generated/e094_1_ok.png`

- Scene: the hooded adventurer kneels in prayer on a ridge as the cracks in a giant moon stop spreading; soft light falls. Red only: the moon.
- Characters: the hooded adventurer

### 292. e094_1_ng：赤い月→月を見上げて祈る（失敗）

保存名：`generated/e094_1_ng.png`

- Scene: the hooded adventurer looks up at a giant moon where a huge eye has opened in a crack, staring back. Red only: the moon.
- Characters: the hooded adventurer

### 293. e094_2_ok：赤い月→月の光を浴びて力を得る（成功）

保存名：`generated/e094_2_ok.png`

- Scene: the hooded adventurer stands bathed in moonlight on a ridge, arms spread, glowing with power. Red only: the moon.
- Characters: the hooded adventurer

### 294. e094_2_ng：赤い月→月の光を浴びて力を得る（失敗）

保存名：`generated/e094_2_ng.png`

- Scene: the hooded adventurer writhes on a ridge, engulfed by the light of a giant cracked moon. Red only: the moon.
- Characters: the hooded adventurer

### 295. e095_1_ok：胎動する闇→子守唄に身を委ねる（成功）

保存名：`generated/e095_1_ok.png`

- Scene: the hooded adventurer lies curled peacefully in a pulsing darkness like a womb, faint ribbons of melody around. Red only: a faint heartbeat glow.
- Characters: the hooded adventurer

### 296. e095_1_ng：胎動する闇→子守唄に身を委ねる（失敗）

保存名：`generated/e095_1_ng.png`

- Scene: the hooded adventurer drifts into sleep in a pulsing darkness, dark membranes closing over them. Red only: the heartbeat glow.
- Characters: the hooded adventurer

### 297. e095_2_ok：胎動する闇→闇を切り裂いて進む（成功）

保存名：`generated/e095_2_ok.png`

- Scene: the hooded adventurer slashes a pulsing darkness, which splits open with a scream, light beyond. Red only: the heartbeat glow.
- Characters: the hooded adventurer

### 298. e095_2_ng：胎動する闇→闇を切り裂いて進む（失敗）

保存名：`generated/e095_2_ng.png`

- Scene: Dark tendrils flow into a wound on the hooded adventurer's arm as they cut through a pulsing darkness. Red only: the heartbeat glow.
- Characters: the hooded adventurer

### 299. e096_1_ok：あの夜の部屋→寝台で休む（成功）

保存名：`generated/e096_1_ok.png`

- Scene: the hooded adventurer lies curled on a small white bed in a quiet sickroom, sleeping peacefully. Red only: the flower on the windowsill.
- Characters: the hooded adventurer

### 300. e096_1_ng：あの夜の部屋→寝台で休む（失敗）

保存名：`generated/e096_1_ng.png`

- Scene: the hooded adventurer tosses in a small bed in a sickroom; a faint ghostly feverish child appears beside them. Red only: the flower on the windowsill.
- Characters: the hooded adventurer

### 301. e096_2_r：あの夜の部屋→部屋を出る

保存名：`generated/e096_2_r.png`

- Scene: the hooded adventurer closes the door of a small sickroom behind them without looking back, black void outside. Red only: the flower visible through the closing door.
- Characters: the hooded adventurer

### 302. n04_1_r：王の手紙→手紙を拾い集める

保存名：`generated/n04_1_r.png`

- Scene: the hooded adventurer gathers an armful of sealed envelopes at the bottom of a crevice, more piling at their feet. Red only: the wax seals.
- Characters: the hooded adventurer

### 303. n04_2_r：王の手紙→そっと元に戻す

保存名：`generated/n04_2_r.png`

- Scene: the hooded adventurer gently sets an envelope back on a pile as another letter flutters down from above. Red only: the wax seals.
- Characters: the hooded adventurer

### 304. n05_0_r：何度目の挑戦者→「初めて会うはずだ」と言う

保存名：`generated/n05_0_r.png`

- Scene: The ghost of an old adventurer, red scarf around his neck, speaks to the hooded adventurer; behind them a faint vision of a melody carrying a fallen hooded figure back up a stairway. Red only: the ghost's scarf.
- Characters: the hooded adventurer

### 305. n05_1_ok：何度目の挑戦者→なぜ戻されるのか訊く（成功）

保存名：`generated/n05_1_ok.png`

- Scene: The ghost of an old adventurer with a red scarf points down into the depths, explaining something to the hooded adventurer. Red only: the scarf.
- Characters: the hooded adventurer

### 306. n05_1_ng：何度目の挑戦者→なぜ戻されるのか訊く（失敗）

保存名：`generated/n05_1_ng.png`

- Scene: The ghost of an old adventurer with a red scarf shakes his head at the hooded adventurer. Red only: the scarf.
- Characters: the hooded adventurer

### 307. n05_2_r：何度目の挑戦者→亡霊の装備をもらう

保存名：`generated/n05_2_r.png`

- Scene: The ghost of an old adventurer hands his old gear to the hooded adventurer and begins to fade. Red only: the scarf.
- Characters: the hooded adventurer

### 308. x01_0_ok：底の向こう→迷わず降りる（成功）

保存名：`generated/x01_0_ok.png`

- Scene: the hooded adventurer descends an endless staircase into darkness, pale wisps of wishes swirling behind like a wind at their back. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 309. x01_0_ng：底の向こう→迷わず降りる（失敗）

保存名：`generated/x01_0_ng.png`

- Scene: Pale wisps cling to the hooded adventurer's legs on an endless staircase, weighing them down. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 310. x01_1_ok：底の向こう→声に耳を澄ます（成功）

保存名：`generated/x01_1_ok.png`

- Scene: the hooded adventurer listens on an endless staircase; among the pale wisps, one gentle ribbon of melody. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 311. x01_1_ng：底の向こう→声に耳を澄ます（失敗）

保存名：`generated/x01_1_ng.png`

- Scene: A thousand pale wisps whisper around the hooded adventurer on an endless staircase. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 312. x01_2_ok：底の向こう→石を投げ込んで深さを測る（成功）

保存名：`generated/x01_2_ok.png`

- Scene: the hooded adventurer drops a stone down an endless staircase and leaps down many flights after it. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 313. x01_2_ng：底の向こう→石を投げ込んで深さを測る（失敗）

保存名：`generated/x01_2_ng.png`

- Scene: the hooded adventurer waits at the top of an endless staircase, listening for a stone that never lands. Red only: the glow at the bottom.
- Characters: the hooded adventurer

### 314. x02_0_ok：誰かの足跡→足跡を辿る（成功）

保存名：`generated/x02_0_ok.png`

- Scene: the hooded adventurer follows a trail of footprints through a dusty corridor down a shortcut. Red only: the last footprint ahead.
- Characters: the hooded adventurer

### 315. x02_0_ng：誰かの足跡→足跡を辿る（失敗）

保存名：`generated/x02_0_ng.png`

- Scene: A trail of footprints ends at a blank wall; the hooded adventurer presses an ear to it. Red only: the last footprint.
- Characters: the hooded adventurer

### 316. x02_1_ok：誰かの足跡→逆向きに辿る（成功）

保存名：`generated/x02_1_ok.png`

- Scene: the hooded adventurer finds a dropped pouch of coins where a trail of footprints begins. Red only: the pouch's drawstring.
- Characters: the hooded adventurer

### 317. x02_1_ng：誰かの足跡→逆向きに辿る（失敗）

保存名：`generated/x02_1_ng.png`

- Scene: the hooded adventurer kneels at fresh footprints in dust, faint steam rising from the last one. Red only: the last footprint.
- Characters: the hooded adventurer

### 318. x02_2_r：誰かの足跡→足跡を踏み消す

保存名：`generated/x02_2_r.png`

- Scene: the hooded adventurer scuffs out a trail of footprints with their boots as they walk. Red only: the last remaining footprint.
- Characters: the hooded adventurer

### 319. x03_0_ok：願いの墓場→一枚拾って読む（成功）

保存名：`generated/x03_0_ok.png`

- Scene: the hooded adventurer reads a scrap of paper among piles of wishes, glowing with new strength; the writing is illegible. Red only: the scrap in their hand.
- Characters: the hooded adventurer

### 320. x03_0_ng：願いの墓場→一枚拾って読む（失敗）

保存名：`generated/x03_0_ng.png`

- Scene: the hooded adventurer drops a scrap of paper, dazed, among piles of wishes; the writing is illegible. Red only: the dropped scrap.
- Characters: the hooded adventurer

### 321. x03_1_r：願いの墓場→たいまつで弔い火を灯す

保存名：`generated/x03_1_r.png`

- Scene: Discarded wishes burn gently in a cave, embers rising like souls, while the hooded adventurer holds a torch. Red only: the rising embers.
- Characters: the hooded adventurer

### 322. x03_2_r：願いの墓場→自分の願いを書き加える

保存名：`generated/x03_2_r.png`

- Scene: the hooded adventurer writes on a scrap of paper and adds it to a pile of wishes; the writing is not shown. Red only: the scrap they add.
- Characters: the hooded adventurer

### 323. x03_3_r：願いの墓場→そっと通り過ぎる

保存名：`generated/x03_3_r.png`

- Scene: the hooded adventurer walks past piles of wish scraps, papers rustling at their feet. Red only: one scrap.
- Characters: the hooded adventurer

### 324. x04_0_r：子守唄の残響→聴き入る

保存名：`generated/x04_0_r.png`

- Scene: the hooded adventurer sits with eyes closed in a black void as pale ribbons of melody curl around them. Red only: one ribbon of melody.
- Characters: the hooded adventurer

### 325. x04_1_ok：子守唄の残響→旋律に言葉をのせる（成功）

保存名：`generated/x04_1_ok.png`

- Scene: the hooded adventurer sings in a black void and the pale ribbons of melody sway brighter around them. Red only: one ribbon.
- Characters: the hooded adventurer

### 326. x04_1_ng：子守唄の残響→旋律に言葉をのせる（失敗）

保存名：`generated/x04_1_ng.png`

- Scene: Pale ribbons of melody drift away from the hooded adventurer into the black void. Red only: one ribbon.
- Characters: the hooded adventurer

### 327. x04_2_ok：子守唄の残響→旋律の源を探す（成功）

保存名：`generated/x04_2_ok.png`

- Scene: the hooded adventurer finds a small cradle at the source of a melody in a black void, a single coin left inside as an offering. Red only: the crown crest on the cradle.
- Characters: the hooded adventurer

### 328. x04_2_ng：子守唄の残響→旋律の源を探す（失敗）

保存名：`generated/x04_2_ng.png`

- Scene: the hooded adventurer searches a black void as ribbons of melody come from every direction. Red only: one ribbon.
- Characters: the hooded adventurer

### 329. x05_0_ok：眼の欠片→踏み砕く（成功）

保存名：`generated/x05_0_ok.png`

- Scene: the hooded adventurer crushes a living eye shard under their boot on a floor of flesh. Red only: the iris on the shard.
- Characters: the hooded adventurer

### 330. x05_0_ng：眼の欠片→踏み砕く（失敗）

保存名：`generated/x05_0_ng.png`

- Scene: Black blood sprays from an eye shard onto the hooded adventurer's boot, smoking. Red only: the iris on the shard.
- Characters: the hooded adventurer

### 331. x05_1_ok：眼の欠片→小さな願いを言う（成功）

保存名：`generated/x05_1_ok.png`

- Scene: the hooded adventurer sits resting beside an eye shard in a floor of flesh, which glows softly. Red only: the iris on the shard.
- Characters: the hooded adventurer

### 332. x05_1_ng：眼の欠片→小さな願いを言う（失敗）

保存名：`generated/x05_1_ng.png`

- Scene: the hooded adventurer recoils as an eye shard grins and twists something into a strange shape in the air. Red only: the iris on the shard.
- Characters: the hooded adventurer

### 333. x05_2_r：眼の欠片→欠片を持ち去る

保存名：`generated/x05_2_r.png`

- Scene: the hooded adventurer tucks a living eye shard into their cloak; it blinks from the folds. Red only: the iris on the shard.
- Characters: the hooded adventurer

### 334. x06_0_ok：鏡の中の踏破者→「願いのために」と答える（成功）

保存名：`generated/x06_0_ok.png`

- Scene: The veteran reflection in a mirror smiles and steps aside, opening a path for the hooded adventurer. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 335. x06_0_ng：鏡の中の踏破者→「願いのために」と答える（失敗）

保存名：`generated/x06_0_ng.png`

- Scene: the hooded adventurer stands silent before a mirror, unable to answer the veteran reflection. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 336. x06_1_ok：鏡の中の踏破者→鏡の自分と剣を交える（成功）

保存名：`generated/x06_1_ok.png`

- Scene: A mirror shatters as the hooded adventurer's sword meets their reflection's; each shard shows a past scene. Red only: the reflection's eyes in a shard.
- Characters: the hooded adventurer

### 337. x06_1_ng：鏡の中の踏破者→鏡の自分と剣を交える（失敗）

保存名：`generated/x06_1_ng.png`

- Scene: The veteran reflection overpowers the hooded adventurer in a sword duel through the mirror. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 338. x06_2_r：鏡の中の踏破者→目を伏せて通り抜ける

保存名：`generated/x06_2_r.png`

- Scene: the hooded adventurer walks past a mirror with eyes lowered as the reflection watches. Red only: the reflection's eyes.
- Characters: the hooded adventurer

### 339. x07_0_r：果ての商人→運命で赤いお守りを買う

保存名：`generated/x07_0_r.png`

- Scene: the faceless peddler hands the hooded adventurer a red amulet in an endless black void. Red only: the amulet.
- Characters: the hooded adventurer, the faceless peddler

### 340. x07_1_r：果ての商人→金貨で手当てを受ける

保存名：`generated/x07_1_r.png`

- Scene: the faceless peddler wraps a bandage around the hooded adventurer's arm in an endless black void. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 341. x07_2_r：果ての商人→血と引き換えに鍛えてもらう

保存名：`generated/x07_2_r.png`

- Scene: the faceless peddler draws a glowing wisp from the hooded adventurer, who stands stronger, in an endless black void. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 342. x07_3_r：果ての商人→何も買わない

保存名：`generated/x07_3_r.png`

- Scene: the faceless peddler waves farewell as the hooded adventurer walks away into the black void. Red only: the small flame inside the lantern glass.
- Characters: the hooded adventurer, the faceless peddler

### 343. x08_0_r：王の使者→地上へ帰還する

保存名：`generated/x08_0_r.png`

- Scene: the hooded adventurer climbs a long stairway beside a royal messenger toward the blinding light of the surface; this one scene may show daylight at the top. Red only: the crown crest on the messenger's banner.
- Characters: the hooded adventurer

### 344. x08_1_r：王の使者→まだ降りると告げる

保存名：`generated/x08_1_r.png`

- Scene: A royal messenger bows deeply to the hooded adventurer in the darkness; a warm light glows in the adventurer's chest. Red only: the crown crest on the banner.
- Characters: the hooded adventurer

### 345. x08_2_r：王の使者→使者の荷を分けてもらう

保存名：`generated/x08_2_r.png`

- Scene: A royal messenger hands the hooded adventurer a potion bottle and a vial of holy water. Red only: the crown crest on the banner.
- Characters: the hooded adventurer
