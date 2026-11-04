# 三択ダンジョン（ThreeChoiceDungeon）

三つの選択肢を選びながら地下百階を目指す、白・黒・赤のホラー風ファンタジーRPG。
Godot 4.7 / 論理解像度 360×640（縦画面）/ Android 対応。

## APK

`release/ThreeChoiceDungeon-v1.0.0.apk`（arm64-v8a / armeabi-v7a, 署名済み）

## ゲームの仕組み

- **3つのパラメータ**：肉体・精神・運命。どれか一つでも 0 になるとゲームオーバー。
- **1階ごとに1イベント**：ピクセルアートの情景と文章、3つの選択肢。
  - `［肉体判定 成功率 62%］` のような判定つき選択肢は、現在の能力値・所持品・深さで成功率が変わる。
  - `〈ロープ〉` のような所持品が必要な選択肢。持っていなければ、選べない状態で表示される（所持品の価値がわかる）。
  - 選択の結果、パラメータの増減、所持品（フラグ）の入手・喪失、近道（階層スキップ）が起こる。
- **フラグ**：所持品として表示されるもの（たいまつ・聖水・黒い犬・呪い…）と、周回をまたいで残るもの（騎士との出会い、日記の続きなど）がある。フラグで発生するイベントや、結果が変わるイベントがある。
- **所持品の効果**：判定ボーナス（犬・剣・王冠・第三の眼など）、呪い（運命判定-15%）、赤い護符（一度だけ死を免れる）、薬瓶（タップで肉体回復）。
- **深さ**：深く潜るほどダメージ・回復が大きくなり、判定も厳しくなる。地下25・50・75階には門番がいて、地下100階が最深部（結末は5種類）。
- **周回要素**
  - ゲームオーバー時、到達階層と拾った金貨に応じてコインを獲得。
  - コインで肉体・精神・運命の初期値を強化（Lvが上がるほど費用増）。
  - 累計で潜った階数に応じて新しいイベントが解放される（最初は29種類、全100種類）。
  - 地下100階に到達するとクリア、無限迷宮（エンドレスモード）が解放される。
- 探索中は毎階オートセーブ。アプリを閉じてもタイトルの「続きから」で再開できる。

## ファイル構成

| パス | 内容 |
| --- | --- |
| `data/events/tier1〜4.json` | 全100イベント（文章・選択肢・結果・解放条件） |
| `data/balance.json` | バランス調整値（ゲームとシミュレータで共有） |
| `scripts/game.gd` | ゲームルール・セーブ（autoload `Game`） |
| `scripts/main.gd` | 全画面のUI（コードで構築）、効果音（プロシージャル生成） |
| `art/events/*.png` | イベント画像（168×100、2倍表示）。`tools/gen_art.py` で生成 |
| `fonts/` | PixelMplus12（M+ FONT LICENSE） |
| `tools/gen_art.py` | 3色ピクセルアート生成（`python3 tools/gen_art.py --sheet out.png` で一覧画像） |
| `tools/gen_icon.py` | アプリアイコン生成 |
| `tools/sim.py` | バランスシミュレータ（ルールを Python で再現） |
| `tools/test_runs.gd` | ヘッドレスでランダムに数百回プレイするテスト |
| `tools/screenshots.gd` | 各画面のスクリーンショット生成（xvfb 上で実行） |

### イベントデータの書式（抜粋）

```jsonc
{"id":"e011","t":"落とし穴","a":"corridor:pit",   // a = 背景:小物（画像生成用）
 "min":1,"max":60,"w":9,                          // 出現階層・重み
 "u":0,                                           // 解放条件：累計階数 / "m:メタフラグ"
 "req":["girl"],"no":["dog"],                     // 発生に必要/禁止のフラグ
 "d":"本文", "dx":[{"req":["torch"],"d":"追記"}],
 "c":[{"t":"ロープを使って渡る","req":["rope"],"r":{"d":"結果","b":-1}},
      {"t":"跳ぶ","chk":"b","p":0.6,"ok":{...},"ng":{...}}]}
// 結果: b/m/f=増減, mb/mm/mf=最大値増減, g=金貨, set/clr=フラグ, meta=永続フラグ, skip=近道
```

## ビルド

1. Godot 4.7.2 と Android エクスポートテンプレートを用意。
2. エディタ設定で Android SDK（`platform-tools/adb` と `build-tools/*/apksigner`）と JDK 17+ を指定。
3. リリース署名の鍵を環境変数で渡してエクスポート：

```sh
export GODOT_ANDROID_KEYSTORE_RELEASE_PATH=/path/to/release.keystore
export GODOT_ANDROID_KEYSTORE_RELEASE_USER=<alias>
export GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD=<password>
godot --headless --export-release "Android" build/ThreeChoiceDungeon.apk
```

## クレジット

- フォント：[PixelMplus](https://github.com/itouhiro/PixelMplus)（M+ FONT LICENSE、`fonts/LICENSE_PixelMplus.txt`）
