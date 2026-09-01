from pathlib import Path
import json, random, re, time
from urllib.parse import urlencode
import requests

BUSINESS_ID='200326329284'
ENDPOINT='https://yandex.ru/maps/api/business/fetchReviews'
REFERER=f'https://yandex.ru/maps/org/eva/{BUSINESS_ID}/reviews/'
MOBILE=Path('mobile-eva-current.js')


def djb2_xor(s):
    n=5381
    for ch in s:
        n=((n*33) ^ ord(ch)) & 0xffffffff
    return n


def recursive_reviews(obj, out):
    if isinstance(obj, dict):
        text=obj.get('text')
        rating=obj.get('rating', obj.get('stars', obj.get('ratingValue', obj.get('reviewRating'))))
        author=obj.get('author')
        name=''
        if isinstance(author, dict):
            name=author.get('name') or author.get('displayName') or ''
        elif isinstance(author, str):
            name=author
        name=name or obj.get('authorName') or obj.get('userName') or ''
        if isinstance(text, str) and text.strip() and str(rating) in {'5','5.0'}:
            key=(name.strip(), text.strip())
            if key not in {(x['name'],x['text']) for x in out}:
                out.append({'name':name.strip() or 'Пользователь Яндекс Карт','text':text.strip()})
        for v in obj.values():
            recursive_reviews(v,out)
    elif isinstance(obj, list):
        for v in obj:
            recursive_reviews(v,out)


def get_csrf(session):
    r=session.post(ENDPOINT,headers={'User-Agent':'Mozilla/5.0','Referer':REFERER,'Accept':'application/json,text/plain,*/*'},timeout=30)
    r.raise_for_status()
    try:
        data=r.json()
    except Exception:
        raise RuntimeError(f'CSRF response is not JSON: {r.status_code} {r.text[:300]}')
    token=data.get('csrfToken')
    if not token:
        raise RuntimeError(f'No csrfToken in response: {str(data)[:500]}')
    return token


def request_page(session, csrf, page):
    now=int(time.time()*1000)
    req=f'{now}-{random.randint(100000000,999999999)}-sas1-0000'
    sess=f'{now}_{random.randint(100000,999999)}'
    base={
        'ajax':'1','businessId':BUSINESS_ID,'csrfToken':csrf,'locale':'ru_RU',
        'page':str(page),'pageSize':'50','ranking':'by_time','reqId':req,'sessionId':sess
    }
    attempts=[]
    # Current API: signature over all params except s. Try the documented sorted form first,
    # then legacy insertion order and URL-encoded variants for resilience.
    sorted_items=sorted(base.items())
    insertion_items=list(base.items())
    raw_sorted='&'.join(f'{k}={v}' for k,v in sorted_items)
    raw_insert='&'.join(f'{k}={v}' for k,v in insertion_items)
    enc_sorted=urlencode(sorted_items)
    enc_insert=urlencode(insertion_items)
    for raw in (raw_sorted,raw_insert,enc_sorted,enc_insert):
        p=dict(base); p['s']=str(djb2_xor(raw)); attempts.append(p)
    # Legacy fallbacks sometimes work with a valid CSRF/session cookie and no signature.
    attempts.append(dict(base))
    attempts.append({'ajax':'1','businessId':BUSINESS_ID,'csrfToken':csrf,'page':str(page),'pageSize':'50','ranking':'by_time'})
    last=''
    for p in attempts:
        r=session.get(ENDPOINT,params=p,headers={'User-Agent':'Mozilla/5.0','Referer':REFERER,'Accept':'application/json,text/plain,*/*','X-Requested-With':'XMLHttpRequest'},timeout=30)
        last=f'{r.status_code} {r.text[:500]}'
        if r.status_code!=200:
            continue
        try:
            data=r.json()
        except Exception:
            continue
        # A successful API payload contains review data; error payloads do not.
        probe=[]; recursive_reviews(data,probe)
        if probe:
            return data
    raise RuntimeError(f'Could not fetch Yandex reviews page {page}. Last response: {last}')


def fetch_reviews():
    s=requests.Session()
    s.headers.update({'Accept-Language':'ru-RU,ru;q=0.9,en;q=0.7'})
    csrf=get_csrf(s)
    found=[]
    for page in range(1,8):
        data=request_page(s,csrf,page)
        recursive_reviews(data,found)
        if len(found)>=15:
            break
    if len(found)<15:
        raise RuntimeError(f'Only {len(found)} distinct five-star reviews found; refusing to fabricate the rest')
    return found[:15]


def jsq(s):
    # JSON string literal is valid JavaScript and preserves the review text verbatim.
    return json.dumps(s,ensure_ascii=False)


def patch_mobile(reviews):
    s=MOBILE.read_text(encoding='utf-8')
    arr='const REAL_REVIEW_DATA=[\n'+',\n'.join(f'[{jsq(r["name"])},{jsq(r["text"])}]' for r in reviews)+'\n];'
    s,n=re.subn(r'const REAL_REVIEW_DATA=\[\n.*?\n\];',arr,s,count=1,flags=re.S)
    if n!=1: raise RuntimeError('REAL_REVIEW_DATA block not found')

    lanes='const reviewLanes=[REAL_REVIEW_DATA.slice(0,3),REAL_REVIEW_DATA.slice(3,6),REAL_REVIEW_DATA.slice(6,9),REAL_REVIEW_DATA.slice(9,12),REAL_REVIEW_DATA.slice(12,15)];'
    s,n=re.subn(r'const reviewLanes=.*?;\nreviews\.innerHTML=',lanes+'\nreviews.innerHTML=',s,count=1,flags=re.S)
    if n!=1: raise RuntimeError('reviewLanes block not found')
    s=re.sub(r'const reviewGap=12,reviewDuration=780,reviewGroupCount=\d+;', 'const reviewGap=12,reviewDuration=780,reviewGroupCount=3;', s, count=1)

    # Five small drawn stars inside every review card.
    star="<svg viewBox=\"0 0 20 20\" aria-hidden=\"true\"><path d=\"M10 1.8l2.35 4.77 5.27.77-3.81 3.71.9 5.24L10 13.82l-4.71 2.47.9-5.24L2.38 7.34l5.27-.77L10 1.8Z\"/></svg>"
    if 'const reviewFiveStars=' not in s:
        marker='const reviewInitial=n=>'
        s=s.replace(marker, f"const reviewFiveStars=`<span class=\"tn30-card-stars\">{star*5}</span>`;\n"+marker,1)
    card_pattern=r'const reviewCard=r=>`<a class="tn30-review-card".*?;</span></a>`;'
    card_repl='const reviewCard=r=>`<a class="tn30-review-card" href="${reviewHref(r)}" target="_blank" rel="noopener"><div class="tn30-review-head"><span class="tn30-review-avatar">${reviewInitial(r[0])}</span><span><strong class="tn30-review-name">${r[0]}</strong><span class="tn30-review-meta">Яндекс Карты</span></span></div>${reviewFiveStars}<p>${r[1]}</p><span class="tn30-review-open">Подробнее →</span></a>`;'
    s,n=re.subn(card_pattern,card_repl,s,count=1,flags=re.S)
    if n!=1: raise RuntimeError('reviewCard template not found')

    if '.tn30-card-stars{' not in s:
        css="""
const reviewStarStyle=document.createElement('style');reviewStarStyle.textContent=`
.tn30-card-stars{display:flex;align-items:center;gap:3px;margin:11px 0 9px;color:#c89555}
.tn30-card-stars svg{width:13px;height:13px;display:block;fill:currentColor;stroke:none}
`;document.head.appendChild(reviewStarStyle);
"""
        s=s.replace('// REVIEWS\n', '// REVIEWS\n'+css,1)

    # Guardrails: exactly 15 unique review texts and five rows.
    if len({r['text'] for r in reviews})!=15: raise RuntimeError('Review texts are not unique')
    if 'REAL_REVIEW_DATA.slice(12,15)' not in s: raise RuntimeError('Five review rows not configured')
    if 'reviewGroupCount=3' not in s: raise RuntimeError('Three cards per row not configured')
    if 'tn30-card-stars' not in s: raise RuntimeError('Stars not configured')
    MOBILE.write_text(s,encoding='utf-8')


reviews=fetch_reviews()
patch_mobile(reviews)
print('Fetched and installed 15 distinct 5-star Yandex reviews:')
for i,r in enumerate(reviews,1):
    print(f'{i:02d}. {r["name"]}: {r["text"][:90]}')
