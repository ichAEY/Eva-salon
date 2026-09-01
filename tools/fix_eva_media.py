from pathlib import Path
import urllib.request, re

KNOWN='https://avatars.mds.yandex.net/get-altay/11908258/2a0000018e5bc631ae55a4afdfeeeb0de622/XXL_height'
HEADERS={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1'}
out=Path('assets/eva-gallery')
out.mkdir(parents=True,exist_ok=True)
for old in out.glob('*'):
    if old.is_file(): old.unlink()
data=urllib.request.urlopen(urllib.request.Request(KNOWN,headers=HEADERS),timeout=8).read()
if len(data)<15000:
    raise SystemExit('Verified Eva Yandex photo unavailable')
photo=out/'eva-01.jpg'
photo.write_bytes(data)

js=Path('mobile-stluxe-current.js')
s=js.read_text(encoding='utf-8')
cats=['salon','salon','hair','nails','face','hair','nails']
items=[]
for i in range(7):
    items.append("    {src:'assets/eva-gallery/eva-01.jpg',cat:%r,alt:%r}"%(cats[i],'EVA — салон красоты'))
works='const works=[\n'+',\n'.join(items)+'\n  ];'
s=re.sub(r"const works=\[.*?\n  \];",works,s,count=1,flags=re.S)
if "classList.remove('eva-boot')" not in s:
    s=s.replace("document.body.appendChild(root);","document.body.appendChild(root);\n  document.documentElement.classList.remove('eva-boot');",1)
js.write_text(s,encoding='utf-8')

idx=Path('index.html')
h=idx.read_text(encoding='utf-8')
if 'EVA_BOOT_V1' not in h:
    boot="""<!-- EVA_BOOT_V1 -->
<script>(function(){try{if(matchMedia('(max-width:767px)').matches)document.documentElement.classList.add('eva-boot')}catch(e){}})();</script>
<style>@media(max-width:767px){html.eva-boot body{margin:0!important;background:#f8f4ef!important;overflow:hidden!important;min-height:100dvh!important}html.eva-boot body>*{visibility:hidden!important}html.eva-boot body:before{content:'EVA';visibility:visible!important;position:fixed;z-index:2147483646;inset:0;display:grid;place-items:center;background:radial-gradient(circle at 50% 42%,rgba(180,126,151,.14),transparent 36%),#f8f4ef;color:#493c42;font:500 64px/1 Georgia,serif;letter-spacing:-.045em;animation:evaBoot 1.15s ease-in-out infinite alternate}html.eva-boot body:after{content:'САЛОН КРАСОТЫ';visibility:visible!important;position:fixed;z-index:2147483647;left:0;right:0;top:calc(50% + 48px);text-align:center;color:#8f727f;font:600 9px/1 Arial,sans-serif;letter-spacing:.24em}@keyframes evaBoot{from{opacity:.82;transform:scale(.985)}to{opacity:1;transform:scale(1)}}}</style>
"""
    h=h.replace('<head>','<head>\n'+boot,1)
h=re.sub(r"src=[\"']assets/[^\"']+\.(?:webp|jpg|jpeg|png)[\"']",'src="assets/eva-gallery/eva-01.jpg"',h,flags=re.I)
idx.write_text(h,encoding='utf-8')
