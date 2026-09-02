import html as htmlmod
import json
import re
from pathlib import Path
import requests

BUSINESS_ID='1179517154'
CARD='https://yandex.ru/maps/org/yeva/1179517154/'
ENDPOINT='https://yandex.ru/maps/api/business/fetchReviews'
HEADERS={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36','Accept-Language':'ru-RU,ru;q=0.9,en;q=0.8','Referer':CARD}

def djb2_xor(s):
    n=5381
    for ch in s:
        n=(33*n)^ord(ch)
    return n & 0xffffffff

session=requests.Session()
page=session.get(CARD,headers=HEADERS,timeout=30)
print('card',page.status_code,'len',len(page.text),'url',page.url)
page.raise_for_status()
s=htmlmod.unescape(page.text)
for key in ('reqId','sessionId','csrfToken'):
    vals=[]
    for pat in [rf'"{key}":"([^"]+)"',rf'{key}=([^&"\\]+)']:
        vals.extend(re.findall(pat,s))
    uniq=[]
    for v in vals:
        if v not in uniq: uniq.append(v)
    print(key,'candidates',uniq[:10])

reqs=re.findall(r'"reqId":"([^"]+)"',s)
sessions=re.findall(r'"sessionId":"([^"]+)"',s)
if not reqs or not sessions:
    raise SystemExit('reqId/sessionId not found in exact Yandex card')
req_id=reqs[0]; session_id=sessions[0]
post=session.post(ENDPOINT,headers=HEADERS,timeout=30)
print('csrf POST',post.status_code,post.text[:300])
post.raise_for_status()
csrf=post.json()['csrfToken']

reviews=[]; seen=set()
for pageno in range(1,8):
    ordered=[('ajax','1'),('businessId',BUSINESS_ID),('csrfToken',csrf),('locale','ru_RU'),('page',str(pageno)),('pageSize','50'),('ranking','by_time'),('reqId',req_id),('sessionId',session_id)]
    raw='&'.join(f'{k}={v}' for k,v in ordered)
    sig=str(djb2_xor(raw))
    params=dict(ordered); params['s']=sig
    r=session.get(ENDPOINT,params=params,headers=HEADERS,timeout=30)
    print('reviews page',pageno,'status',r.status_code,'url',r.url[:260])
    print('body head',r.text[:220])
    if r.status_code!=200: break
    data=r.json()
    candidates=data.get('reviews') or data.get('reviewResults',{}).get('reviews') or data.get('data',{}).get('reviews') or []
    print('items',len(candidates),'keys',list(data)[:15])
    for item in candidates:
        rid=str(item.get('reviewId',''))
        if not rid or rid in seen: continue
        seen.add(rid)
        author=item.get('author') or {}
        text=item.get('text') or ''
        rating=int(item.get('rating') or 0)
        if str(item.get('businessId',BUSINESS_ID))==BUSINESS_ID and rating==5 and text.strip():
            reviews.append({'reviewId':rid,'businessId':BUSINESS_ID,'name':author.get('name',''),'text':text,'rating':rating})
    if len(reviews)>=15: break

if len(reviews)<15:
    raise SystemExit(f'only {len(reviews)} exact 5-star reviews fetched through Yandex API')
reviews=reviews[:15]
Path('tmp').mkdir(exist_ok=True)
Path('tmp/pavlino-5star-reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
print('SUCCESS exact reviews',len(reviews))
for i,r in enumerate(reviews,1): print(i,r['name'],repr(r['text'][:100]))
