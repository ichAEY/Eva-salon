import html as htmlmod
import json
import re
from pathlib import Path
import requests

BASE='https://yandex.com/maps/org/yeva/1179517154/'
BUSINESS_ID='1179517154'
HEADERS={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36','Accept-Language':'ru-RU,ru;q=0.9,en;q=0.8'}
PAT=re.compile(r'"reviewId":"(?P<id>(?:\\.|[^"])*)".*?"businessId":"1179517154".*?"author":\{"name":"(?P<name>(?:\\.|[^"])*)".*?\},"text":"(?P<text>(?:\\.|[^"])*)".*?"rating":(?P<rating>\d+)',re.S)

def dec(s):
    return json.loads('"'+s+'"')

session=requests.Session()
seen=set(); reviews=[]
for page in range(1,25):
    r=session.get(BASE,params={'page':page},headers=HEADERS,timeout=30)
    print('page',page,'status',r.status_code,'len',len(r.text))
    r.raise_for_status()
    s=htmlmod.unescape(r.text)
    matches=list(PAT.finditer(s))
    print('matches',len(matches))
    for m in matches:
        rid=dec(m.group('id'))
        if rid in seen: continue
        seen.add(rid)
        item={'reviewId':rid,'businessId':BUSINESS_ID,'name':dec(m.group('name')),'text':dec(m.group('text')),'rating':int(m.group('rating'))}
        if item['rating']==5 and item['text'].strip():
            reviews.append(item)
    if len(reviews)>=15:
        break

if len(reviews)<15:
    raise SystemExit(f'only {len(reviews)} unique 5-star reviews fetched')
reviews=reviews[:15]
if len({r['reviewId'] for r in reviews})!=15 or any(r['rating']!=5 or r['businessId']!=BUSINESS_ID for r in reviews):
    raise SystemExit('review validation failed')
Path('tmp').mkdir(exist_ok=True)
Path('tmp/pavlino-5star-reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
print('saved 15 exact five-star reviews from business',BUSINESS_ID)
for i,r in enumerate(reviews,1):
    print(i,r['name'],repr(r['text'][:90]))
