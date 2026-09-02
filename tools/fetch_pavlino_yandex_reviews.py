import html as htmlmod
import re
from pathlib import Path
import requests

URL='https://yandex.com/maps/org/yeva/1179517154/?page=1'
HEADERS={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36','Accept-Language':'ru-RU,ru;q=0.9,en;q=0.8'}
r=requests.get(URL,headers=HEADERS,timeout=30)
print('status',r.status_code,'len',len(r.text),'url',r.url)
r.raise_for_status()
s=htmlmod.unescape(r.text)
positions=[m.start() for m in re.finditer(r'"reviewId"',s)]
print('reviewId occurrences',len(positions))
out=[]
for i,pos in enumerate(positions[:30],1):
    frag=s[max(0,pos-1200):pos+3600]
    frag=re.sub(r'\s+',' ',frag)
    out.append(f'--- REVIEW_CONTEXT_{i} ---\n{frag[:4600]}\n')
Path('tmp').mkdir(exist_ok=True)
Path('tmp/pavlino-review-contexts.txt').write_text('\n'.join(out),encoding='utf-8')
print('saved contexts',len(out))
