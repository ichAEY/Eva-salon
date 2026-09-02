from pathlib import Path
import json, re, html

BUSINESS_ID='1179517154'
YANDEX='https://yandex.com/maps/org/yeva/1179517154/'
YANDEX_RU='https://yandex.ru/maps/org/yeva/1179517154/'
YANDEX_REVIEWS='https://yandex.com/maps/org/yeva/1179517154/reviews/'
PHONE='+79260063922'
PHONE_DISPLAY='+7 (926) 006-39-22'
ADDRESS='Балашиха, д. Павлино, 69'
ADDRESS_FULL='Московская область, г.о. Балашиха, д. Павлино, 69'
LAT='55.729412'; LON='37.961358'
ROUTE=f'https://yandex.ru/maps/?rtext=~{LAT}%2C{LON}&rtt=auto'
MAP=f'https://yandex.ru/map-widget/v1/?ll={LON}%2C{LAT}&z=17'
RATING='4,8'; RATINGS='310'; REVIEW_COUNT='155'

review_path=Path('tmp/pavlino-5star-reviews.json')
reviews=json.loads(review_path.read_text(encoding='utf-8'))
assert len(reviews)==15
assert len({r['reviewId'] for r in reviews})==15
assert all(str(r['businessId'])==BUSINESS_ID and int(r['rating'])==5 and r['name'] and r['text'].strip() for r in reviews)
review_pairs=[[r['name'],r['text']] for r in reviews]
review_js=json.dumps(review_pairs,ensure_ascii=False)

SERVICES=[
 ('hair','Волосы','Женская стрижка','800–1 700 ₽'),
 ('hair','Волосы','Мужская стрижка','1 000–1 500 ₽'),
 ('hair','Волосы','Окрашивание волос','Цена по записи'),
 ('hair','Волосы','Укладка волос','Цена по записи'),
 ('nails','Маникюр','Маникюр','Цена по записи'),
 ('nails','Маникюр','Педикюр','Цена по записи'),
 ('face','Косметология','Чистка лица','Цена по записи'),
 ('face','Косметология','Пилинг','Цена по записи'),
 ('face','Косметология','Инъекционные процедуры','Цена по записи'),
 ('face','Косметология','Коррекция фигуры','Цена по записи'),
 ('brows','Брови','Коррекция бровей','Цена по записи'),
 ('lashes','Ресницы','Услуги для ресниц','Цена по записи'),
 ('depilation','Эпиляция','Шугаринг','Цена по записи'),
 ('depilation','Эпиляция','Восковая эпиляция','Цена по записи'),
 ('other','Перманент','Перманентный макияж','Цена по записи'),
]

# ---------- index.html ----------
p=Path('index.html'); x=p.read_text(encoding='utf-8')
x=x.replace('EVA — салон красоты в Мытищах. Услуги, портфолио, специалисты и запись.','EVA — салон красоты в Павлино, Балашиха. Услуги, портфолио, направления и запись.')
x=x.replace('EVA — салон красоты в Мытищах','EVA — салон красоты в Павлино, Балашиха')
x=x.replace('Салон красоты · Мытищи','Салон красоты · Балашиха · Павлино')
x=x.replace('ул. Академика Каргина, 25',ADDRESS)
x=x.replace('Мытищи · ул. Академика Каргина, 25',ADDRESS)
x=x.replace('4,8 · 92 отзыва',f'{RATING} · {REVIEW_COUNT} отзывов')
x=x.replace('185 оценок',f'{RATINGS} оценок').replace('92 отзыва на Яндекс Картах',f'{REVIEW_COUNT} отзывов на Яндекс Картах')
x=x.replace('https://yandex.com/maps/org/eva/200326329284/reviews/',YANDEX_REVIEWS)
x=x.replace('https://yandex.com/maps/org/eva/200326329284/',YANDEX)
x=x.replace('https://yandex.ru/maps/org/eva/200326329284/',YANDEX_RU)
x=x.replace('+7 (968) 427-01-01',PHONE_DISPLAY).replace('+79684270101',PHONE)
x=x.replace('https://yandex.ru/maps/?rtext=~%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB.%20%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D0%BA%D0%B0%20%D0%9A%D0%B0%D1%80%D0%B3%D0%B8%D0%BD%D0%B0%2C%2025&rtt=auto',ROUTE)

# Services section: same styling, only verified exact-card directions/prices.
filters='''<div class="service-groups" id="serviceGroups">
        <button class="service-group active" data-service-filter="hair">Волосы</button>
        <button class="service-group" data-service-filter="nails">Маникюр</button>
        <button class="service-group" data-service-filter="face">Косметология</button>
        <button class="service-group" data-service-filter="brows">Брови</button>
        <button class="service-group" data-service-filter="lashes">Ресницы</button>
        <button class="service-group" data-service-filter="depilation">Эпиляция</button>
        <button class="service-group" data-service-filter="other">Перманент</button>
      </div>'''
rows=[]
for i,(cat,label,title,price) in enumerate(SERVICES):
    extra=' extra' if i>=6 else ''
    et=html.escape(title,quote=True); ep=html.escape(price)
    rows.append(f'        <div class="service{extra}" data-service-category="{cat}"><div><div class="service-name">{et}</div><div class="service-note">EVA · Павлино</div></div><div class="service-side"><div class="price">{ep}</div><button class="pick" onclick="openBooking(\'{et}\')">Выбрать</button></div></div>')
services_section='''    <section id="services">
      <div class="section-head"><div><h2>Услуги</h2><p>Направления из карточки EVA в Яндекс Картах</p></div></div>
      '''+filters+'''\n      <div class="services" id="servicesList">\n'''+"\n".join(rows)+'''\n      </div>
      <button class="show-more" id="servicesMore" type="button">Посмотреть ещё</button>
    </section>'''
x,n=re.subn(r'    <section id="services">.*?    </section>',services_section,x,count=1,flags=re.S)
assert n==1, 'desktop services section not replaced'

# Team: remove the wrong Mytishchi person; keep neutral roles until salon confirms names.
team_section='''    <section id="team">
      <div class="section-head"><div><h2>Специалисты</h2><p>Направления команды EVA</p></div></div>
      <div class="specialists">
        <button class="specialist" onclick="openRole('Мастер по волосам','Стрижки|Окрашивание|Укладка')"><span class="avatar-placeholder">E</span><strong>Мастер по волосам</strong><span>Стрижки · окрашивание</span></button>
        <button class="specialist" onclick="openRole('Мастер ногтевого сервиса','Маникюр|Педикюр')"><span class="avatar-placeholder">E</span><strong>Мастер ногтевого сервиса</strong><span>Маникюр · педикюр</span></button>
        <button class="specialist" onclick="openRole('Косметолог','Чистка лица|Пилинг|Инъекционные процедуры|Коррекция фигуры')"><span class="avatar-placeholder">E</span><strong>Косметолог</strong><span>Косметология</span></button>
        <button class="specialist" onclick="openRole('Мастер бровей и ресниц','Коррекция бровей|Услуги для ресниц')"><span class="avatar-placeholder">E</span><strong>Мастер бровей и ресниц</strong><span>Брови · ресницы</span></button>
      </div>
    </section>'''
x,n=re.subn(r'    <section id="team">.*?    </section>',team_section,x,count=1,flags=re.S); assert n==1

# Desktop reviews: all 15 exact 5-star Yandex reviews, five rows of three.
star='<span class="review-stars-svg" aria-label="5 из 5">'+('<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.7l2.45 4.96 5.47.8-3.96 3.85.94 5.45L10 14.2l-4.9 2.57.94-5.45L1.08 7.46l5.47-.8L10 1.7Z"/></svg>'*5)+'</span>'
review_rows=[]
for offset in range(0,15,3):
    cards=[]
    for r in reviews[offset:offset+3]:
        name=html.escape(r['name']); text=html.escape(r['text']).replace('\n','<br>')
        cards.append(f'<article class="review-card"><div class="review-top"><span class="review-name">{name}</span>{star}</div><p class="review-text">{text}</p></article>')
    review_rows.append('        <div class="reviews-row-3">'+''.join(cards)+'</div>')
reviews_section=f'''    <section id="reviews">
      <div class="section-head"><div><h2>Отзывы</h2><p>Оригинальные отзывы клиентов EVA из Яндекс Карт</p></div><a class="section-link" href="{YANDEX_REVIEWS}" target="_blank" rel="noopener">Все отзывы ↗</a></div>
      <div class="reviews-summary"><div><div class="score">{RATING}</div><div class="score-label">{RATINGS} оценок</div></div><div style="text-align:right"><div style="color:var(--violet);font-size:16px;letter-spacing:2px">★★★★★</div><div class="score-label">{REVIEW_COUNT} отзывов на Яндекс Картах</div></div></div>
      <div class="reviews-grid-5x3">
{chr(10).join(review_rows)}
      </div>
    </section>'''
x,n=re.subn(r'    <section id="reviews">.*?    </section>',reviews_section,x,count=1,flags=re.S); assert n==1

# Clamp desktop review text too; exact full text stays in DOM, cards do not explode.
if '.reviews-row-3 .review-text{' not in x:
    x=x.replace('.reviews-row-3 .review-card{margin-top:0;height:100%;min-width:0}', '.reviews-row-3 .review-card{margin-top:0;height:100%;min-width:0;overflow:hidden}\n    .reviews-row-3 .review-text{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:5;overflow:hidden;text-overflow:ellipsis}')

# About section, if present, replace with strictly factual copy.
about='''    <section id="about">
      <div class="section-head"><div><h2>О салоне</h2><p>EVA · Павлино</p></div></div>
      <div class="about-card"><h3>Салон красоты EVA</h3><p>EVA — салон красоты в Павлино. Здесь работают с волосами и ногтями, предлагают косметологические процедуры, оформление бровей и ресниц, эпиляцию и перманентный макияж. Салон работает ежедневно с 10:00 до 21:00.</p></div>
    </section>'''
x,n_about=re.subn(r'    <section id="about">.*?    </section>',about,x,count=1,flags=re.S)

# Visit: replace whole section, preserving card visual language.
visit=f'''    <section id="visit">
      <div class="section-head"><div><h2>Визит</h2><p>{ADDRESS_FULL}</p></div><a class="section-link" href="{YANDEX_RU}" target="_blank" rel="noopener">Яндекс Карты ↗</a></div>
      <div class="visit-card">
        <div class="visit-row"><span class="visit-icon">⌖</span><div><strong>{ADDRESS}</strong><span>Московская область · городской округ Балашиха</span></div></div>
        <div class="visit-row"><span class="visit-icon">◷</span><div><strong>Ежедневно 10:00–21:00</strong><span>Актуальные часы — в карточке Яндекс Карт</span></div></div>
        <div class="visit-row"><span class="visit-icon">☎</span><div><strong>{PHONE_DISPLAY}</strong><span>Запись и уточнение стоимости услуг</span></div></div>
        <div class="visit-actions"><a class="btn" href="tel:{PHONE}" style="display:grid;place-items:center">Позвонить</a><a class="btn primary" href="{ROUTE}" target="_blank" rel="noopener" style="display:grid;place-items:center">Маршрут</a></div>
      </div>
    </section>'''
x,n=re.subn(r'    <section id="visit">.*?    </section>',visit,x,count=1,flags=re.S); assert n==1

x=x.replace('Мытищи · ул. Академика Каргина, 25',ADDRESS).replace('Мытищи', 'Павлино')
x=re.sub(r'<div class="availability"><strong>Доступно \d+ услуг</strong>',f'<div class="availability"><strong>Доступно {len(SERVICES)} услуг</strong>',x)
x=re.sub(r'mobile-eva-current\.js\?v=[^"\']+', 'mobile-eva-current.js?v=20260902-pavlino-correct', x)
x=re.sub(r'mobile-eva-theme-current\.js\?v=[^"\']+', 'mobile-eva-theme-current.js?v=20260902-pavlino-correct', x)
p.write_text(x,encoding='utf-8')

# ---------- mobile-eva-current.js ----------
p=Path('mobile-eva-current.js'); s=p.read_text(encoding='utf-8')
# Exact global identity replacements in both bundled mobile layers.
repls={
 '+79684270101':PHONE,
 '+7 (968) 427-01-01':PHONE_DISPLAY,
 'https://yandex.com/maps/org/eva/200326329284/reviews/':YANDEX_REVIEWS,
 'https://yandex.com/maps/org/eva/200326329284/':YANDEX,
 'https://yandex.ru/maps/org/eva/200326329284/':YANDEX_RU,
 'https://yandex.ru/maps/?rtext=~55.918782%2C37.779988&rtt=auto':ROUTE,
 '55.918782':LAT,
 '37.779988':LON,
 'Мытищи, ул. Академика Каргина, 25':ADDRESS,
 'Мытищи, улица Академика Каргина, 25':ADDRESS,
 'ул. Академика Каргина, 25':ADDRESS,
 'Мытищи':'Павлино',
 '92 отзыва на Яндекс Картах':f'{REVIEW_COUNT} отзывов на Яндекс Картах',
 '92 отзыва':f'{REVIEW_COUNT} отзывов',
 '185 оценок':f'{RATINGS} оценок',
}
for a,b in repls.items(): s=s.replace(a,b)
# counters in first bundle
s=re.sub(r'const RATINGS_COUNT=\d+;',f'const RATINGS_COUNT={RATINGS};',s,count=1)

# First bundle services array.
services1='const services=[\n'+',\n'.join("    [%s]"%(','.join(repr(v) for v in (cat,title,price))) for cat,label,title,price in SERVICES)+'\n  ];'
s,n=re.subn(r'const services=\[.*?\n  \];',lambda m:services1,s,count=1,flags=re.S); assert n==1
# First bundle reviews: exact same 15.
reviews1='const reviews='+json.dumps([{'name':r['name'],'text':r['text']} for r in reviews],ensure_ascii=False)+';'
s,n=re.subn(r'const reviews=\[.*?\n  \];',lambda m:reviews1,s,count=1,flags=re.S); assert n==1
# First bundle masters: no stale person names.
masters1="""const masters=[
    {id:'hair',name:'Мастер',category:'Волосы',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['hair']},
    {id:'nails',name:'Мастер',category:'Маникюр · педикюр',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['nails']},
    {id:'cosmetology',name:'Мастер',category:'Косметология',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['face']},
    {id:'look',name:'Мастер',category:'Брови · ресницы',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['brows','lashes']}
  ];"""
s,n=re.subn(r'const masters=\[.*?\n  \];',lambda m:masters1,s,count=1,flags=re.S); assert n==1

# Refined current service list.
svc2='[\n'+',\n'.join("[%s]"%(','.join(repr(v) for v in (label,title,price))) for cat,label,title,price in SERVICES)+'\n].forEach(x=>add(x[0],x[1],x[2],x[3]||\'\'));'
s,n=re.subn(r'\[\n\[\'Волосы\'.*?\n\]\.forEach\(x=>add\(x\[0\],x\[1\],x\[2\],x\[3\]\|\|\'\'\)\);',lambda m:svc2,s,count=1,flags=re.S); assert n==1, 'refined service list not replaced'
# Master-review cache + masters in refined bundle.
s=re.sub(r"const REVIEW_DATA=\[.*?\n\];",'const REVIEW_DATA=[];',s,count=1,flags=re.S)
masters2="""const MASTERS=[
{id:'hair',name:'Мастер',role:'Волосы',about:'Персональные данные специалиста уточняются у салона.',cats:['Волосы'],work:['hair00001.webp','hair00002.webp','hair00003.webp'],reviewNames:[]},
{id:'nails',name:'Мастер',role:'Маникюр · педикюр',about:'Персональные данные специалиста уточняются у салона.',cats:['Маникюр'],work:['nails00001.webp','nails00002.webp','nails00003.webp'],reviewNames:[]},
{id:'cosmetology',name:'Мастер',role:'Косметология',about:'Персональные данные специалиста уточняются у салона.',cats:['Косметология'],work:[],reviewNames:[]},
{id:'look',name:'Мастер',role:'Брови · ресницы',about:'Персональные данные специалиста уточняются у салона.',cats:['Брови','Ресницы'],work:['brows00001.webp','lashes00001.webp'],reviewNames:[]}
];"""
s,n=re.subn(r'const MASTERS=\[.*?\n\];',lambda m:masters2,s,count=1,flags=re.S); assert n==1

# Current animated 3-row carousel keeps its mechanics; replace ONLY source data with exact 15 reviews.
s,n=re.subn(r'const REAL_REVIEW_DATA=.*?;\nconst reviewInitial',lambda m:'const REAL_REVIEW_DATA='+review_js+';\nconst reviewInitial',s,count=1,flags=re.S); assert n==1

# Factual copy and contacts in refined bundle.
s=s.replace('EVA — салон красоты в Павлино, где основные бьюти‑процедуры собраны в одном месте.','EVA — салон красоты в Павлино, Балашиха.')
s=s.replace('Здесь работают с волосами, ногтями, бровями и ресницами, предлагают косметологические процедуры, эпиляцию и макияж. Формат салона позволяет удобно сочетать разные услуги и подобрать уход под свой образ.','Здесь работают с волосами и ногтями, предлагают косметологические процедуры, оформление бровей и ресниц, эпиляцию и перманентный макияж.')
s=s.replace('7 направлений красоты','Салон красоты · Павлино')
s=s.replace('Московская область · открыть в Яндекс Картах','Московская область · городской округ Балашиха · Яндекс Карты')
s=s.replace('https://yandex.ru/map-widget/v1/?ll=37.961358%2C55.729412&z=17',MAP)
# If old iframe survived a textual variant, normalize it.
s=re.sub(r'https://yandex\.ru/map-widget/v1/\?ll=[^"`]+&z=17',MAP,s)
# hero location label variants
s=s.replace('Академика Каргина, 25', 'д. Павлино, 69')

p.write_text(s,encoding='utf-8')

# ---------- audit ----------
wrong=['Мытищи','Академика Каргина','200326329284','79684270101','+7 (968) 427-01-01','Нарине','Марина Ким','Екатерина Рэй','Александра Н.','natalia tatarinceva','Арина Боданова','Aliya Uderbaeva']
for fp in ['index.html','mobile-eva-current.js']:
    data=Path(fp).read_text(encoding='utf-8')
    leftovers=[w for w in wrong if w in data]
    if leftovers: raise SystemExit(f'{fp}: wrong EVA leftovers: {leftovers}')
    for must in [BUSINESS_ID,PHONE,'Павлино']:
        if must not in data: raise SystemExit(f'{fp}: missing {must}')
# Mobile exact carousel invariants.
m=Path('mobile-eva-current.js').read_text(encoding='utf-8')
block=re.search(r'// REVIEWS\n.*?// VISIT',m,re.S).group(0)
assert 'REAL_REVIEW_DATA.slice(0,5)' in block and 'REAL_REVIEW_DATA.slice(10,15)' in block
assert 'reviewGroupCount=5' in block and 'reviewStarSvg.repeat(5)' in block
assert block.count('slice(')>=3
# Review names must be present verbatim in live mobile source.
for r in reviews:
    assert r['name'] in block

print('CORRECT EVA READY: business 1179517154, Pavlino, 15 exact 5-star reviews, no Mytishchi leftovers')
