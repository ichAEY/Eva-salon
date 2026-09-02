import html as htmlmod
import json
import re
import requests

URL='https://yandex.com/maps/org/yeva/1179517154/?page=1'
HEADERS={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36','Accept-Language':'ru-RU,ru;q=0.9,en;q=0.8'}
r=requests.get(URL,headers=HEADERS,timeout=30)
print('status',r.status_code,'len',len(r.text),'url',r.url)
r.raise_for_status()
s=htmlmod.unescape(r.text)
# print compact context around review identifiers so we can inspect Yandex's current server-rendered schema.
positions=[m.start() for m in re.finditer(r'"reviewId"',s)]
print('reviewId occurrences',len(positions))
for i,pos in enumerate(positions[:20],1):
    frag=s[max(0,pos-900):pos+2500]
    frag=re.sub(r'\s+',' ',frag)
    print(f'--- REVIEW_CONTEXT_{i} ---')
    print(frag[:3300])
