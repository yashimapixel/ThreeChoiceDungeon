"""Write a Codex brief (.md) that generates raw images only, one prompt per image.

python3 tools/ai_stills/make_brief.py OUT.md ZIPNAME TITLE (--batch N | --names a b c) [--why name=reason ...]
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_images import build_prompt  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('zipname')
    ap.add_argument('title')
    ap.add_argument('--batch', type=int)
    ap.add_argument('--names', nargs='*')
    ap.add_argument('--why', nargs='*', default=[])
    a = ap.parse_args()
    spec = json.load(open(os.path.join(HERE, 'jobs.json'), encoding='utf-8'))
    by = {j['name']: j for j in spec['jobs']}
    jobs = [by[n] for n in a.names] if a.names else [j for j in spec['jobs'] if j['batch'] == a.batch]
    why = dict(w.split('=', 1) for w in a.why)
    n, ex = len(jobs), jobs[0]['name']
    L = ['# Codex 向け作業指示：%s（元画像のみ）' % a.title, '',
         'ゲーム「三択ダンジョン」のイベント画像の元絵を、下の%d枚分、まとめて生成してください。' % n,
         '減色・縮小などの加工は、こちらで別に行います。**あなたの作業は、画像を生成して PNG で保存することだけです。**', '',
         '## ルール', '',
         '1. 下の「画像リスト」の順番どおりに、1枚ずつ生成する。',
         '2. 各画像のプロンプト（``` の中）を**一字一句そのまま**使う。書き換え・要約・翻訳はしない。',
         '3. サイズは横長の **1536×1024**（3:2）。',
         '4. 生成したら**すぐに** `generated/<name>.png` として保存してから、次の画像に進む（例：`generated/%s.png`）。' % ex,
         '5. **必ず PNG で保存する。JPEG は厳禁。** 縮小・トリミング・色の変更・圧縮など、画像の加工は一切しない。',
         '6. 途中で中断して再開したときは、`generated/` に既にある画像は作り直さず、残りから続ける。',
         '7. 品質の確認と作り直しの判断はこちらで行う。生成した画像を開いて確認したり、説明したりしなくてよい（作り直しも不要）。',
         '8. スクリプトの作成、リポジトリの取得、コミットは不要。返信は「OK %s」のように1枚1行の短い報告だけにする。' % ex,
         '9. %d枚すべて保存したら終了する。最後に、保存できたファイル名の一覧と、生成できなかったものがあればその名前を書く。'
         'クラウド環境で作業している場合は、`generated/` の PNG を **`%s`** にまとめてダウンロードできる形で出力する'
         '（自分のPCで作業している場合は zip は不要）。' % (n, a.zipname), '',
         '## 画像リスト（%d枚）' % n, '']
    if why:
        L += ['| # | name | 内容 | 作り直す理由 |', '| --- | --- | --- | --- |']
        L += ['| %d | `%s` | %s | %s |' % (i + 1, j['name'], j['ja'], why.get(j['name'], '')) for i, j in enumerate(jobs)]
    else:
        L += ['| # | name | 内容 |', '| --- | --- | --- |']
        L += ['| %d | `%s` | %s |' % (i + 1, j['name'], j['ja']) for i, j in enumerate(jobs)]
    L += ['', '---', '']
    for i, j in enumerate(jobs):
        L += ['### %d. %s：%s' % (i + 1, j['name'], j['ja']), '', '保存名：`generated/%s.png`' % j['name'], '',
              '```', build_prompt(spec, j), '```', '']
    text = '\n'.join(L)
    assert '{' not in text.split('## 画像リスト')[1].replace('{runs}', ''), 'unreplaced placeholder'
    open(a.out, 'w', encoding='utf-8').write(text)
    print('wrote', a.out, n, 'images')


if __name__ == '__main__':
    main()
