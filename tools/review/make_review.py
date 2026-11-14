"""Build a single-file HTML review sheet: every event, choice and result with its still,
plus checkboxes / notes per item and a Markdown export of the requested fixes.

python3 -I tools/review/make_review.py [OUT.html] [--placeholders]
  default images: art_ai/test/px1 (the AI stills); --placeholders uses art/ instead
"""
import base64, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TIERS = [('tier1', '第一章　降下（B1〜25）'), ('tier2', '第二章　弔い（B26〜50）'),
         ('tier3', '第三章　引き離された夜（B51〜75）'), ('tier4', '第四章　子守唄（B76〜100）'),
         ('endless', '無限迷宮（B101〜）')]


def item_names():
    src = open(os.path.join(ROOT, 'scripts', 'game.gd'), encoding='utf-8').read()
    return dict(re.findall(r'"(\w+)": \{"name": "([^"]+)"', src))


def main():
    out = next((a for a in sys.argv[1:] if not a.startswith('--')), os.path.join(ROOT, 'review', 'stills_review.html'))
    img_root = os.path.join(ROOT, 'art') if '--placeholders' in sys.argv else os.path.join(ROOT, 'art_ai', 'test', 'px1')
    prompts = {}
    jp = os.path.join(ROOT, 'tools', 'ai_stills', 'jobs.json')
    if os.path.exists(jp):
        prompts = {j['name']: j['prompt'] for j in json.load(open(jp, encoding='utf-8'))['jobs']}
    images = {}

    def img(rel):
        p = os.path.join(img_root, rel)
        if not os.path.exists(p):
            return None
        key = rel[:-4]
        if key not in images:
            images[key] = 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
        return key

    chapters = []
    for tier, label in TIERS:
        evs = json.load(open(os.path.join(ROOT, 'data', 'events', tier + '.json'), encoding='utf-8'))
        rows = []
        for e in evs:
            ev = {k: e[k] for k in ('id', 't', 'd', 'min', 'max', 'u', 'req', 'no', 'beat', 'fixed', 'once', 'dx', 'endless') if k in e}
            ev['img'] = img('events/%s.png' % e['id'])
            ev['prompt'] = prompts.get(e['id'], '')
            ev['c'] = []
            for k, c in enumerate(e['c']):
                ch = {kk: c[kk] for kk in ('t', 'req', 'no', 'chk', 'p', 'mreq_any') if kk in c}
                ch['out'] = []
                for b in ('r', 'ok', 'ng'):
                    if b in c:
                        name = '%s_%d_%s' % (e['id'], k, b)
                        res = dict(c[b])
                        ch['out'].append({'b': b, 'name': name, 'res': res, 'img': img('results/%s.png' % name),
                                          'prompt': prompts.get(name, '')})
                ev['c'].append(ch)
            rows.append(ev)
        chapters.append({'label': label, 'events': rows})
    specials = [{'id': n, 't': t, 'img': img('events/%s.png' % n), 'prompt': prompts.get(n, '')}
                for n, t in (('title', 'タイトル画面'), ('gameover', 'ゲームオーバー画面'), ('clear', 'クリア画面'))]
    data = {'chapters': chapters, 'specials': specials, 'items': item_names(),
            'source': 'AI版（art_ai/test/px1）' if img_root.endswith('px1') else '仮画像（art/）'}
    html = TEMPLATE.replace('/*DATA*/', json.dumps(data, ensure_ascii=False)).replace('/*IMAGES*/', json.dumps(images))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    n_res = sum(len(c['out']) for ch in chapters for e in ch['events'] for c in e['c'])
    print('wrote', out, '%.1f MB' % (len(html) / 1e6), 'events', sum(len(ch['events']) for ch in chapters),
          'results', n_res, 'images', len(images))


TEMPLATE = r'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>三択ダンジョン 修正チェック</title>
<style>
:root{--bg:#0e0c0e;--panel:#1b181b;--line:#4a4646;--dim:#989288;--text:#e8e2d4;--red:#ce242e;--dred:#6e141c;--chip:#2a2629}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 "Hiragino Sans","Noto Sans JP","Yu Gothic",sans-serif}
header{position:sticky;top:0;z-index:5;background:#141114f2;border-bottom:1px solid var(--line);padding:10px 16px;backdrop-filter:blur(4px)}
header h1{font-size:17px;margin:0 0 6px}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.bar input[type=search],.bar select{background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:6px 8px;font:inherit;min-width:0}
.bar input[type=search]{flex:1 1 180px}
button{background:var(--chip);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:6px 12px;font:inherit;cursor:pointer}
button.primary{background:var(--dred);border-color:var(--red)}
button:hover{border-color:var(--dim)}
.count{color:var(--dim);font-size:13px}
.count b{color:var(--red)}
main{max-width:1100px;margin:0 auto;padding:12px 16px 80px}
h2.chapter{font-size:18px;border-left:4px solid var(--red);padding-left:10px;margin:28px 0 12px}
.event{background:var(--panel);border:1px solid var(--line);border-radius:10px;margin:0 0 18px;overflow:hidden}
.event.flag{border-color:var(--red)}
.ehead{display:grid;grid-template-columns:minmax(0,336px) 1fr;gap:14px;padding:14px}
.still{width:100%;max-width:672px;aspect-ratio:336/200;image-rendering:pixelated;background:#000;border:1px solid var(--line);display:block}
.noimg{display:flex;align-items:center;justify-content:center;color:var(--dim);font-size:13px}
.id{color:var(--dim);font-size:12px;font-family:ui-monospace,monospace}
.etitle{font-size:18px;font-weight:bold;margin:0}
.meta{color:var(--dim);font-size:13px;margin:2px 0 8px}
.desc{white-space:pre-wrap}
.dx{color:var(--dim);font-size:13px;margin-top:6px;white-space:pre-wrap}
.choices{border-top:1px solid var(--line)}
.choice{padding:12px 14px;border-top:1px dashed #333}
.choice:first-child{border-top:none}
.ctext{font-weight:bold}
.cond{color:var(--red);font-size:13px;margin-left:6px}
.outs{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:10px}
.out{background:#141114;border:1px solid #333;border-radius:8px;padding:8px}
.out.flag{border-color:var(--red)}
.blabel{font-size:12px;font-weight:bold;letter-spacing:.05em}
.blabel.ok{color:var(--text)}.blabel.ng{color:var(--red)}.blabel.r{color:var(--dim)}
.rtext{font-size:14px;margin:6px 0 2px;white-space:pre-wrap}
.eff{font-size:12px;color:var(--dim)}
.fix{margin-top:8px;padding:8px;border-radius:6px;background:#0e0c0e;border:1px solid #2c2829}
.fix.on{border-color:var(--red)}
.fix label{cursor:pointer;user-select:none}
.fix .row{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:center;font-size:13px}
.fix .main{font-weight:bold}
.fix .tags{display:none;gap:6px;flex-wrap:wrap}
.fix.on .tags{display:flex}
.tag{border:1px solid var(--line);border-radius:999px;padding:1px 9px;font-size:12px}
.tag input{display:none}
.tag:has(input:checked){background:var(--dred);border-color:var(--red)}
.fix textarea{display:none;width:100%;margin-top:6px;min-height:52px;background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:6px 8px;font:inherit;font-size:14px;resize:vertical}
.fix.on textarea{display:block}
details.prompt{margin-top:6px;font-size:12px;color:var(--dim)}
details.prompt summary{cursor:pointer}
details.prompt div{white-space:pre-wrap;font-family:ui-monospace,monospace;font-size:11px;margin-top:4px}
.hidden{display:none!important}
dialog{background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:10px;max-width:min(900px,94vw);width:100%}
dialog textarea{width:100%;height:55vh;background:#0e0c0e;color:var(--text);border:1px solid var(--line);font:12px/1.5 ui-monospace,monospace}
@media (max-width:640px){.ehead{grid-template-columns:1fr}.outs{grid-template-columns:1fr}header{position:static}}
</style>
</head>
<body>
<header>
  <h1>三択ダンジョン 修正チェック <span class="count" id="src"></span></h1>
  <div class="bar">
    <input type="search" id="q" placeholder="検索（ID・題名・文章）">
    <select id="chap"><option value="">すべての章</option></select>
    <select id="mode"><option value="all">すべて表示</option><option value="flag">チェックしたものだけ</option></select>
    <span class="count" id="cnt"></span>
    <button class="primary" id="exp">修正リストを書き出す（.md）</button>
    <button id="show">表示してコピー</button>
    <button id="more">…</button>
  </div>
  <div class="bar hidden" id="morebar" style="margin-top:6px">
    <button id="save">チェック内容を保存（.json）</button>
    <label><button id="loadbtn" type="button">保存した内容を読み込む</button><input type="file" id="load" accept=".json" class="hidden"></label>
    <button id="clear">チェックをすべて消す</button>
  </div>
</header>
<main id="main"></main>
<dialog id="dlg"><p>下の文章をコピーして、AI に渡してください。</p><textarea id="dlgtext" readonly></textarea>
<p><button id="copy">コピー</button> <button id="close">閉じる</button> <span class="count" id="copied"></span></p></dialog>
<script>
const DATA=/*DATA*/;
const IMG=/*IMAGES*/;
const KEY='tcd_review_v1';
let state={};
try{state=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){state={}}
function persist(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
const STAT={b:'肉体',m:'精神',f:'運命'};
const TAGS={event:['画像','本文','出現条件'],choice:['選択肢の文','条件・判定'],result:['画像','結果の文','効果・数値'],special:['画像']};
const BL={r:'結果',ok:'成功',ng:'失敗'};
const item=n=>DATA.items[n]||n;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function effects(r){
  const a=[];
  for(const k of ['b','m','f']) if(r[k]) a.push(STAT[k]+(r[k]>0?'+':'')+r[k]);
  for(const k of ['mb','mm','mf']) if(r[k]) a.push('最大'+STAT[k[1]]+(r[k]>0?'+':'')+r[k]);
  if(r.g) a.push('金貨'+(r.g>0?'+':'')+r.g);
  if(r.set) a.push('入手: '+r.set.map(item).join('・'));
  if(r.clr) a.push('喪失: '+r.clr.map(item).join('・'));
  if(r.meta) a.push('記録: '+[].concat(r.meta).join('・'));
  if(r.skip) a.push(r.skip+'階進む');
  if(r.end) a.push('結末: '+r.end);
  if(r.retire) a.push('地上へ帰還');
  if(r.fixed) a.push('固定: '+r.fixed);
  return a.join('　');
}
function cond(c){
  const a=[];
  if(c.chk) a.push('［'+STAT[c.chk]+'判定 基本'+Math.round(c.p*100)+'%］');
  if(c.req) a.push('〈'+c.req.map(item).join('・')+'〉');
  if(c.no) a.push('〈'+c.no.map(item).join('・')+'なし〉');
  if(c.mreq_any) a.push('〈記録: '+c.mreq_any.join(' or ')+'〉');
  return a.join(' ');
}
function evmeta(e){
  const a=[];
  if(e.fixed) a.push('B'+e.fixed+' 固定（門番・最深部）'); else if(e.min!=null) a.push('B'+e.min+'〜'+e.max);
  if(e.beat) a.push('第'+e.beat+'章の物語');
  if(e.u) a.push(typeof e.u==='number'?'累計'+e.u+'階で解放':'解放条件: '+e.u);
  if(e.req) a.push('必要: '+e.req.map(item).join('・'));
  if(e.no) a.push('なし: '+e.no.map(item).join('・'));
  if(e.once) a.push('1回のみ');
  return a.join(' / ');
}
function stillHTML(key){return key&&IMG[key]?'<img class="still" loading="lazy" alt="" src="'+IMG[key]+'">':'<div class="still noimg">画像なし</div>'}
function fixHTML(id,kind,label){
  const s=state[id]||{};
  const tags=TAGS[kind].map(t=>'<label class="tag"><input type="checkbox" data-tag="'+esc(t)+'"'+((s.tags||[]).includes(t)?' checked':'')+'>'+t+'</label>').join('');
  return '<div class="fix'+(s.on?' on':'')+'" data-id="'+id+'" data-kind="'+kind+'"><div class="row"><label class="main"><input type="checkbox" class="on"'+(s.on?' checked':'')+'> '+label+'</label><span class="tags">'+tags+'</span></div>'+
    '<textarea placeholder="どこをどう直したいか（例：主人公の顔が見えている／赤をもっと小さく／この選択肢の成功率を上げたい）">'+esc(s.note||'')+'</textarea></div>';
}
function promptHTML(p){return p?'<details class="prompt"><summary>画像のプロンプト</summary><div>'+esc(p)+'</div></details>':''}
const INDEX={};
function build(){
  const main=document.getElementById('main'),chap=document.getElementById('chap');
  let h='';
  DATA.chapters.forEach((ch,ci)=>{
    chap.insertAdjacentHTML('beforeend','<option value="'+ci+'">'+esc(ch.label)+'</option>');
    h+='<h2 class="chapter" data-ch="'+ci+'">'+esc(ch.label)+'</h2>';
    ch.events.forEach(e=>{
      INDEX[e.id]={kind:'event',e};
      let dx=(e.dx||[]).map(x=>'＋'+(x.req?'〈'+x.req.map(item).join('・')+'〉':'')+(x.no?'〈'+x.no.map(item).join('・')+'なし〉':'')+(x.mreq_any?'〈記録〉':'')+' '+x.d).join('\n');
      let body='';
      e.c.forEach((c,k)=>{
        const cid=e.id+'_c'+k; INDEX[cid]={kind:'choice',e,c,k};
        let outs='';
        c.out.forEach(o=>{
          INDEX[o.name]={kind:'result',e,c,k,o};
          const dx2=(o.res.dx||[]).map(x=>'＋ '+x.d).join('\n');
          outs+='<div class="out" data-id="'+o.name+'">'+stillHTML(o.img)+'<div class="blabel '+o.b+'">'+BL[o.b]+' <span class="id">'+o.name+'</span></div><div class="rtext">'+esc(o.res.d||'')+(dx2?'\n'+esc(dx2):'')+'</div><div class="eff">'+esc(effects(o.res))+'</div>'+fixHTML(o.name,'result','この結果を直したい')+promptHTML(o.prompt)+'</div>';
        });
        body+='<div class="choice"><div><span class="ctext">'+(k+1)+'. '+esc(c.t)+'</span><span class="cond">'+esc(cond(c))+'</span></div>'+fixHTML(cid,'choice','この選択肢を直したい')+'<div class="outs">'+outs+'</div></div>';
      });
      const search=(e.id+' '+e.t+' '+e.d+' '+e.c.map(c=>c.t+' '+c.out.map(o=>o.name+' '+(o.res.d||'')).join(' ')).join(' ')).toLowerCase();
      h+='<section class="event" data-ch="'+ci+'" data-id="'+e.id+'" data-s="'+esc(search)+'"><div class="ehead"><div>'+stillHTML(e.img)+promptHTML(e.prompt)+'</div><div><div class="id">'+e.id+(e.endless?'（エンドレス）':'')+'</div><p class="etitle">'+esc(e.t)+'</p><div class="meta">'+esc(evmeta(e))+'</div><div class="desc">'+esc(e.d)+'</div>'+(dx?'<div class="dx">'+esc(dx)+'</div>':'')+fixHTML(e.id,'event','このイベント（画像・本文）を直したい')+'</div></div><div class="choices">'+body+'</div></section>';
    });
  });
  h+='<h2 class="chapter" data-ch="sp">特殊画面</h2>';
  DATA.specials.forEach(s=>{INDEX[s.id]={kind:'special',s};
    h+='<section class="event" data-ch="sp" data-id="'+s.id+'" data-s="'+esc((s.id+' '+s.t).toLowerCase())+'"><div class="ehead"><div>'+stillHTML(s.img)+promptHTML(s.prompt)+'</div><div><div class="id">'+s.id+'</div><p class="etitle">'+esc(s.t)+'</p>'+fixHTML(s.id,'special','この画像を直したい')+'</div></div></section>';});
  main.innerHTML=h;
  refreshFlags(); filter();
}
function refreshFlags(){
  document.querySelectorAll('.fix').forEach(f=>{const on=!!(state[f.dataset.id]||{}).on;f.classList.toggle('on',on);
    if(f.closest('.out')) f.closest('.out').classList.toggle('flag',on);});
  document.querySelectorAll('section.event').forEach(s=>s.classList.toggle('flag',!!s.querySelector('.fix.on')));
  const n=Object.values(state).filter(v=>v.on).length;
  document.getElementById('cnt').innerHTML='修正チェック <b>'+n+'</b> 件';
}
function filter(){
  const q=document.getElementById('q').value.trim().toLowerCase(),c=document.getElementById('chap').value,m=document.getElementById('mode').value;
  document.querySelectorAll('section.event').forEach(s=>{
    let show=(!q||s.dataset.s.includes(q))&&(c===''||s.dataset.ch===c);
    if(m==='flag') show=show&&s.classList.contains('flag');
    s.classList.toggle('hidden',!show);
    if(m==='flag'&&show){s.querySelectorAll('.choice').forEach(ch=>ch.classList.toggle('hidden',!ch.querySelector('.fix.on')));s.querySelectorAll('.out').forEach(o=>o.classList.toggle('hidden',!o.classList.contains('flag')&&!o.closest('.choice').querySelector(':scope > .fix.on')));}
    else{s.querySelectorAll('.choice,.out').forEach(x=>x.classList.remove('hidden'));}
  });
  document.querySelectorAll('h2.chapter').forEach(h=>{const any=[...document.querySelectorAll('section.event[data-ch="'+h.dataset.ch+'"]')].some(s=>!s.classList.contains('hidden'));h.classList.toggle('hidden',!any)});
}
document.addEventListener('change',ev=>{
  const f=ev.target.closest('.fix'); if(!f) return;
  const id=f.dataset.id, s=state[id]||(state[id]={});
  if(ev.target.classList.contains('on')) s.on=ev.target.checked;
  if(ev.target.dataset.tag!==undefined) s.tags=[...f.querySelectorAll('[data-tag]:checked')].map(x=>x.dataset.tag);
  if(!s.on&&!s.note&&!(s.tags||[]).length) delete state[id];
  persist(); refreshFlags();
});
document.addEventListener('input',ev=>{
  if(ev.target.tagName!=='TEXTAREA') return;
  const f=ev.target.closest('.fix'), id=f.dataset.id, s=state[id]||(state[id]={});
  s.note=ev.target.value; if(s.note&&!s.on){s.on=true;f.querySelector('.on').checked=true;refreshFlags();}
  persist();
});
['q','chap','mode'].forEach(id=>document.getElementById(id).addEventListener('input',filter));
function md(){
  const items=Object.entries(state).filter(([k,v])=>v.on&&INDEX[k]);
  const order=Object.keys(INDEX); items.sort((a,b)=>order.indexOf(a[0])-order.indexOf(b[0]));
  const d=new Date(), ds=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
  let o='# 三択ダンジョン 修正リスト（'+ds+'）\n\n';
  o+='ゲーム「三択ダンジョン」で修正したい箇所の一覧です。各項目の「修正内容」が依頼です。\n';
  o+='- 画像は 336×200・6色のピクセルアート（元絵は画像生成AIで作り、減色・縮小して使用）。画像を直す場合はプロンプトの修正と作り直しが必要です。\n';
  o+='- 文章・選択肢・数値はリポジトリの data/events/*.json にあります（ID で検索できます）。\n';
  o+='- 確認に使った画像：'+DATA.source+'\n\n件数：'+items.length+'件\n';
  let lastEv='';
  for(const [id,v] of items){
    const x=INDEX[id], tags=(v.tags||[]).join('・')||'（指定なし）', note=(v.note||'').trim()||'（文章なし。チェックのみ）';
    const ev=x.e?x.e.id:'special';
    if(ev!==lastEv){o+='\n## '+(x.e?x.e.id+' '+x.e.t:'特殊画面')+'\n';lastEv=ev;}
    if(x.kind==='event'){
      o+='\n### イベント '+id+'「'+x.e.t+'」\n- 直したいところ：'+tags+'\n- 修正内容：'+note+'\n- 現在の本文：'+x.e.d+'\n';
      if(x.e.dx) o+='- 条件付きの追記：'+x.e.dx.map(d=>d.d).join(' ／ ')+'\n';
      o+='- 出現：'+evmeta(x.e)+'\n- 画像：events/'+id+'.png\n'+(x.e.prompt?'- 現在のプロンプト：'+x.e.prompt+'\n':'');
      o+='- 選択肢：'+x.e.c.map((c,i)=>(i+1)+'.「'+c.t+'」'+cond(c)).join(' ')+'\n';
    }else if(x.kind==='choice'){
      o+='\n### 選択肢 '+x.e.id+' の '+(x.k+1)+'番目「'+x.c.t+'」\n- 直したいところ：'+tags+'\n- 修正内容：'+note+'\n- 条件・判定：'+(cond(x.c)||'なし')+'\n';
      x.c.out.forEach(r=>{o+='- '+BL[r.b]+'（'+r.name+'）：'+(r.res.d||'')+(effects(r.res)?'　['+effects(r.res)+']':'')+'\n'});
    }else if(x.kind==='result'){
      o+='\n### 結果 '+id+'（選択肢「'+x.c.t+'」→ '+BL[x.o.b]+'）\n- 直したいところ：'+tags+'\n- 修正内容：'+note+'\n- 現在の文章：'+(x.o.res.d||'')+'\n- 効果：'+(effects(x.o.res)||'なし')+'\n- 画像：results/'+id+'.png\n'+(x.o.prompt?'- 現在のプロンプト：'+x.o.prompt+'\n':'');
    }else{
      o+='\n### '+x.s.t+'（'+id+'）\n- 直したいところ：'+tags+'\n- 修正内容：'+note+'\n- 画像：events/'+id+'.png\n'+(x.s.prompt?'- 現在のプロンプト：'+x.s.prompt+'\n':'');
    }
  }
  return {text:o,name:'fix_list_'+ds+'.md'};
}
function download(name,text,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type}));a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)}
document.getElementById('exp').onclick=()=>{const m=md();download(m.name,m.text,'text/markdown;charset=utf-8')};
document.getElementById('show').onclick=()=>{document.getElementById('dlgtext').value=md().text;document.getElementById('copied').textContent='';document.getElementById('dlg').showModal()};
document.getElementById('copy').onclick=async()=>{const t=document.getElementById('dlgtext');try{await navigator.clipboard.writeText(t.value)}catch(e){t.select();document.execCommand('copy')}document.getElementById('copied').textContent='コピーしました'};
document.getElementById('close').onclick=()=>document.getElementById('dlg').close();
document.getElementById('more').onclick=()=>document.getElementById('morebar').classList.toggle('hidden');
document.getElementById('save').onclick=()=>download('review_save.json',JSON.stringify(state,null,1),'application/json');
document.getElementById('loadbtn').onclick=()=>document.getElementById('load').click();
document.getElementById('load').onchange=async ev=>{const f=ev.target.files[0];if(!f)return;try{state=JSON.parse(await f.text());persist();build();}catch(e){alert('読み込めませんでした')}};
document.getElementById('clear').onclick=()=>{if(confirm('チェックと修正内容をすべて消しますか？')){state={};persist();build();}};
document.getElementById('src').textContent='（画像：'+DATA.source+'）';
build();
</script>
</body>
</html>
'''

if __name__ == '__main__':
    main()
