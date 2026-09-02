import html as htmlmod
import json
import re
from pathlib import Path
import requests

BUSINESS_ID='1179517154'
BASE='https://yandex.com/maps/org/yeva/1179517154/reviews/'
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36','Accept-Language':'ru-RU,ru;q=0.9','Accept':'text/html,application/xhtml+xml'}
PAT=re.compile(r'"reviewId":"(?P<id>(?:\\.|[^"])*)".*?"businessId":"1179517154".*?"author":\{"name":"(?P<name>(?:\\.|[^"])*)".*?\},"text":"(?P<text>(?:\\.|[^"])*)".*?"rating":(?P<rating>\d+)',re.S)

def dec(s):
    return json.loads('"'+s+'"')

session=requests.Session(); seen=set(); reviews=[]
for page in range(1,8):
    url=BASE if page==1 else BASE+f'?page={page}'
    r=session.get(url,headers=HEADERS,timeout=30)
    print('page',page,'status',r.status_code,'len',len(r.text),'url',r.url)
    r.raise_for_status()
    s=htmlmod.unescape(r.text)
    matches=list(PAT.finditer(s))
    print('matches',len(matches))
    new=0
    for m in matches:
        rid=dec(m.group('id'))
        if rid in seen: continue
        seen.add(rid); new+=1
        name=dec(m.group('name')); text=dec(m.group('text')); rating=int(m.group('rating'))
        if rating==5 and text.strip():
            reviews.append({'reviewId':rid,'businessId':BUSINESS_ID,'name':name,'text':text,'rating':rating})
    print('new ids',new,'five-star total',len(reviews))
    if len(reviews)>=15: break

if len(reviews)<15:
    raise SystemExit(f'only {len(reviews)} unique 5-star reviews from exact reviews pages')
reviews=reviews[:15]
if len({r['reviewId'] for r in reviews}) != 15 or any(r['businessId']!=BUSINESS_ID or r['rating']!=5 for r in reviews):
    raise SystemExit('validation failed')
Path('tmp').mkdir(exist_ok=True)
Path('tmp/pavlino-5star-reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
print('SUCCESS 15 exact five-star reviews from business',BUSINESS_ID)
for i,r in enumerate(reviews,1): print(i,r['name'],repr(r['text'][:110]))
