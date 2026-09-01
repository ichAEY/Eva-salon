from pathlib import Path
import re

MOBILE = Path('mobile-eva-current.js')
INDEX = Path('index.html')

s = MOBILE.read_text(encoding='utf-8')

# Base data in the unchanged STLuxe template.
s = s.replace("const RATINGS_COUNT=125;", "const RATINGS_COUNT=185;")
s = s.replace(
    "const serviceTabs=[['all','Все'],['nails','Ногти'],['hair','Волосы'],['face','Косметология'],['brows','Брови'],['depilation','Депиляция']];",
    "const serviceTabs=[['all','Все'],['nails','Ногти'],['hair','Волосы'],['face','Косметология'],['brows','Брови'],['lashes','Ресницы'],['depilation','Эпиляция'],['other','Макияж']];"
)
s = s.replace(
    "const galleryTabs=[['all','Все'],['salon','Салон'],['nails','Ногти'],['hair','Волосы']];",
    "const galleryTabs=[['all','Все'],['salon','Салон'],['nails','Ногти'],['hair','Волосы'],['brows','Брови'],['lashes','Ресницы'],['other','Перманент'],['team','Команда']];"
)
s = s.replace(
    'Ногти, волосы, косметология и другие направления — в одном пространстве на улице Победы.',
    'Ногти, волосы, косметология и другие направления — в одном пространстве на улице Академика Каргина.'
)
s = s.replace('Мытищи · Победы, 16', 'Мытищи · Академика Каргина, 25')
s = s.replace(
    'EVA находится в Ивантеевке на улице Победы, 16. Актуальное расписание указано в карточке EVA, со вторника по воскресенье салон работает с 10:00 до 20:00.',
    'EVA находится в Мытищах на улице Академика Каргина, 25. Актуальный статус и расписание работы доступны в Яндекс Картах.'
)
s = s.replace(
    'https://yandex.ru/map-widget/v1/?text=%D0%98%D0%B2%D0%B0%D0%BD%D1%82%D0%B5%D0%B5%D0%B2%D0%BA%D0%B0%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%9F%D0%BE%D0%B1%D0%B5%D0%B4%D1%8B%2C%2016&z=16',
    'https://yandex.ru/map-widget/v1/?text=%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D0%BA%D0%B0%20%D0%9A%D0%B0%D1%80%D0%B3%D0%B8%D0%BD%D0%B0%2C%2025&z=16'
)
s = s.replace('<span><strong>10–20</strong><small>Вт–Вс</small></span>', '<span><strong>Яндекс</strong><small>часы работы</small></span>')
s = s.replace('<span><strong>17</strong><small>услуг</small></span>', '<span><strong>${services.length}</strong><small>услуг</small></span>')
s = s.replace(
    'Онлайн-ссылка салона в карточке не указана. Для записи можно позвонить или открыть карточку EVA в Яндекс Картах.',
    'Для записи можно позвонить или открыть карточку EVA в Яндекс Картах.'
)

# The refined full gallery must contain exactly the manually uploaded EVA media.
gallery = """const GALLERY={
'Салон':[
 {src:'salon02.webp',alt:'Интерьер EVA'},
 {src:'salon03.webp',alt:'Интерьер EVA'},
 {src:'salon01.webp',alt:'Интерьер EVA'}
],
'Ногти':[
 {src:'nails00001.webp',alt:'Маникюр EVA'},
 {src:'nails00002.webp',alt:'Маникюр EVA'},
 {src:'nails00003.webp',alt:'Маникюр EVA'},
 {src:'nails00004.webp',alt:'Маникюр EVA'}
],
'Волосы':[
 {src:'hair00001.webp',alt:'Работа с волосами EVA'},
 {src:'hair00002.webp',alt:'Работа с волосами EVA'},
 {src:'hair00003.webp',alt:'Работа с волосами EVA'},
 {src:'hair00004.webp',alt:'Работа с волосами EVA'},
 {src:'hair00005.webp',alt:'Работа с волосами EVA'},
 {src:'hair00006.webp',alt:'Работа с волосами EVA'},
 {src:'hair00007.webp',alt:'Работа с волосами EVA'}
],
'Брови':[
 {src:'brows00001.webp',alt:'Брови EVA'},
 {src:'brows00002.webp',alt:'Брови EVA'},
 {src:'brows00003.webp',alt:'Брови EVA'},
 {src:'brows00004.webp',alt:'Брови EVA'}
],
'Ресницы':[
 {src:'lashes00001.webp',alt:'Ресницы EVA'},
 {src:'lashes00002.webp',alt:'Ресницы EVA'},
 {src:'lashes00003.webp',alt:'Ресницы EVA'},
 {src:'lashes00004.webp',alt:'Ресницы EVA'}
],
'Перманент':[
 {src:'lips01.webp',alt:'Перманентный макияж EVA'}
],
'Команда':[
 {src:'team01.webp',alt:'Команда EVA'}
]};"""
s, n = re.subn(r"const GALLERY=\{.*?\};\nconst PORTFOLIO=", gallery + "\nconst PORTFOLIO=", s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace refined GALLERY')

# Only reviews confirmed for EVA. Reuse them in carousel lanes rather than inventing testimonials.
real_reviews = """const REAL_REVIEW_DATA=[
['Марина Ким','Профессиональный мастер Нара; благодарит за результат окрашивания и армянский кофе.'],
['Екатерина Рэй','Нарине помогла грамотно определиться с цветом и выполнила окрашивание аккуратно и быстро.']
];"""
s, n = re.subn(r"const REAL_REVIEW_DATA=\[.*?\];\nconst reviewInitial=", real_reviews + "\nconst reviewInitial=", s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace refined REAL_REVIEW_DATA')
s = s.replace(
    "const reviewLanes=[0,1,2].map(row=>REAL_REVIEW_DATA.filter((_,i)=>i%3===row));",
    "const reviewBase=REAL_REVIEW_DATA;const reviewLanes=[0,1,2].map(row=>Array.from({length:5},(_,i)=>reviewBase[(row*5+i)%reviewBase.length]));"
)
s = s.replace('86 отзывов на Яндекс Картах', '92 отзыва на Яндекс Картах')
s = s.replace("const reviewInitial=n=>([...String(n).trim()][0]||'S').toUpperCase();", "const reviewInitial=n=>([...String(n).trim()][0]||'E').toUpperCase();")

# Keep the STLuxe contact block UI, but do not invent EVA opening hours.
s = s.replace(
    '<div class="tn22-contact">${clock}<span><strong>Вт–Вс 10:00–20:00</strong><span>Актуальное расписание указано в карточке EVA</span></span></div>',
    '<a class="tn22-contact" href="${YANDEX_RU}" target="_blank" rel="noopener">${clock}<span><strong>Часы работы</strong><span>Актуальное расписание — в Яндекс Картах</span></span></a>'
)
s = s.replace(
    'https://yandex.ru/map-widget/v1/?mode=search&text=%D0%98%D0%B2%D0%B0%D0%BD%D1%82%D0%B5%D0%B5%D0%B2%D0%BA%D0%B0%2C%20%D1%83%D0%BB.%20%D0%9F%D0%BE%D0%B1%D0%B5%D0%B4%D1%8B%2C%2016&z=16',
    'https://yandex.ru/map-widget/v1/?mode=search&text=%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB.%20%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D0%BA%D0%B0%20%D0%9A%D0%B0%D1%80%D0%B3%D0%B8%D0%BD%D0%B0%2C%2025&z=16'
)
status_re = re.compile(r"function status\(\)\{.*?\}status\(\);setInterval\(status,60000\);", re.S)
status_new = "function status(){const el=visit.querySelector('#tn22Status'),txt=el.querySelector('.tn22-status-text');txt.textContent='Часы — в Яндекс Картах';el.className='tn22-status';const hs=hero.querySelector('.tn50-hero-status');if(hs){const main=hs.querySelector('.tn50-hero-status-main'),sub=hs.querySelector('.tn50-hero-status-sub');main.textContent='Режим работы';sub.textContent='смотреть в Яндекс Картах';hs.classList.remove('open','closed')}}status();"
s, n = status_re.subn(status_new, s, count=1)
if n != 1:
    raise SystemExit('Could not replace STLuxe schedule function')

s = s.replace("port.querySelector('.tn22-port-all').onclick=()=>openGallery('Ногти');", "port.querySelector('.tn22-port-all').onclick=()=>openGallery('Салон');")
s = s.replace('Фото ресниц пока не добавлены', 'Фотографии в этой категории пока не добавлены')

# Same About component; factual EVA content only.
s = s.replace(
    'Мы сделали EVA местом, где можно спокойно доверить свою красоту мастеру.',
    'EVA — салон красоты в Мытищах с несколькими направлениями в одном пространстве.'
)
s = s.replace(
    'Нам важно, чтобы вам было комфортно на каждом этапе: мы внимательно относимся к пожеланиям, ценим аккуратную работу и собираем в одном пространстве мастеров разных направлений.',
    'В Яндекс Картах для EVA указаны парикмахерские услуги, маникюр и педикюр, косметология, брови и ресницы, эпиляция, Wi‑Fi, оплата картой и онлайн-запись.'
)
s = s.replace(
    '<div class="tn42-fact">Мастера разных направлений</div><div class="tn42-fact">Комфортная атмосфера</div><div class="tn42-fact">Индивидуальный подход</div>',
    '<div class="tn42-fact">Маникюр и педикюр</div><div class="tn42-fact">Волосы и косметология</div><div class="tn42-fact">Онлайн-запись</div>'
)

MOBILE.write_text(s, encoding='utf-8')

# Desktop is still STLuxe's exact structure; only fix inherited client data.
h = INDEX.read_text(encoding='utf-8')
h = h.replace('<span class="brand-dot">ST</span> EVA', '<span class="brand-dot">E</span> EVA')
h = h.replace('<span>Вт–Вс 10:00–20:00</span>', '<span>Часы работы — в Яндекс Картах</span>')
h = h.replace('Онлайн-ссылка салона в карточке не указана, поэтому сейчас запись ведём через прямой контакт.', 'Для записи можно позвонить или открыть карточку EVA в Яндекс Картах.')
INDEX.write_text(h, encoding='utf-8')

photos = [
    'brows00001.webp','brows00002.webp','brows00003.webp','brows00004.webp',
    'hair00001.webp','hair00002.webp','hair00003.webp','hair00004.webp','hair00005.webp','hair00006.webp','hair00007.webp',
    'lashes00001.webp','lashes00002.webp','lashes00003.webp','lashes00004.webp',
    'lips01.webp',
    'nails00001.webp','nails00002.webp','nails00003.webp','nails00004.webp',
    'salon01.webp','salon02.webp','salon03.webp','team01.webp'
]

published = INDEX.read_text(encoding='utf-8') + MOBILE.read_text(encoding='utf-8')
missing = [x for x in photos if x not in published]
if missing:
    raise SystemExit('Missing EVA photos: ' + repr(missing))

gallery_block = re.search(r"const GALLERY=\{.*?\};\nconst PORTFOLIO=", MOBILE.read_text(encoding='utf-8'), re.S)
if not gallery_block:
    raise SystemExit('No refined gallery block after patch')
for photo in photos:
    if gallery_block.group(0).count(photo) != 1:
        raise SystemExit(f'Gallery must contain {photo} exactly once')

forbidden = [
    'Ивантеевка','улице Победы','Победы, 16','51087098664','+79163552222',
    'Татьяна','Алёна','Ольга К.','Оксана Семина','Дарья К.','Надежда Донеско','Галина Б.',
    'Londa','Barex','Luxio','OPI','Selective',
    'salon10.webp','nails10.webp','hair8.webp','res.webp','assets/images/'
]
for file in [INDEX, MOBILE, Path('mobile-eva-theme-current.js')]:
    text = file.read_text(encoding='utf-8')
    hits = [x for x in forbidden if x in text]
    if hits:
        raise SystemExit(f'{file}: inherited STLuxe data remains: {hits}')

if "const RATINGS_COUNT=185;" not in MOBILE.read_text(encoding='utf-8'):
    raise SystemExit('Rating count is not EVA value')

print(f'Audit OK: {len(photos)} EVA photos, zero inherited salon data in published sources')
