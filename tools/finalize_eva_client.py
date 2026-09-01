from pathlib import Path
import re

MOBILE = Path("mobile-eva-current.js")
THEME = Path("mobile-eva-theme-current.js")
INDEX = Path("index.html")

def must_sub(text, pattern, repl, label, flags=re.S, count=1):
    new, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n != count:
        raise SystemExit(f"{label}: expected {count} replacement(s), got {n}")
    return new

mobile = MOBILE.read_text(encoding="utf-8")

first_services = """  const services=[
    ['hair','Стрижка женская — короткие волосы','1 300 ₽'],
    ['hair','Стрижка женская — средние волосы','1 500 ₽'],
    ['hair','Стрижка женская — длинные волосы','1 700 ₽'],
    ['hair','Стрижка женская — очень длинные волосы','2 000 ₽'],
    ['hair','Стрижка детская','1 000 ₽'],
    ['hair','Стрижка модельная мужская','1 500 ₽'],
    ['hair','Укладка','1 000 ₽'],
    ['hair','Уход за волосами','1 000 ₽'],
    ['hair','Окрашивание волос в один тон','3 600 ₽'],
    ['hair','Окрашивание корней','3 500 ₽'],
    ['hair','Тонирование волос','3 600 ₽'],
    ['hair','Сложное окрашивание','7 000 ₽'],
    ['hair','Мелирование прикорневое','3 000 ₽'],
    ['nails','Маникюр аппаратный / комбинированный / классический','1 000 ₽'],
    ['nails','Маникюр с покрытием гель-лак / гель / укрепление','2 000 ₽'],
    ['face','Энзимный мягкий пилинг для всех типов кожи','2 000 ₽'],
    ['face','Аппаратная косметология','Цена по записи'],
    ['face','Чистка лица','Цена по записи'],
    ['face','Массаж лица','Цена по записи'],
    ['brows','Архитектура бровей','1 500 ₽'],
    ['brows','Ламинирование бровей','2 500 ₽'],
    ['lashes','Ламинирование ресниц','2 500 ₽'],
    ['depilation','Лазерная эпиляция — классическое бикини','1 700 ₽'],
    ['depilation','Лазерная эпиляция','Цена по записи'],
    ['depilation','Электроэпиляция','Цена по записи'],
    ['depilation','Шугаринг','Цена по записи'],
    ['depilation','Восковая эпиляция','Цена по записи'],
    ['other','Макияж дневной с ресницами','3 300 ₽']
  ];"""
mobile = must_sub(mobile, r"  const services=\[\n.*?\n  \];", first_services, "mobile first services")

mobile = must_sub(
    mobile,
    r"  const serviceTabs=.*?;\n  const galleryTabs=.*?;",
    "  const serviceTabs=[['hair','Волосы'],['nails','Маникюр'],['face','Косметология'],['brows','Брови'],['lashes','Ресницы'],['depilation','Эпиляция'],['other','Макияж']];\n"
    "  const galleryTabs=[['all','Все'],['salon','Салон'],['nails','Ногти'],['hair','Волосы'],['brows','Брови'],['lashes','Ресницы'],['other','Перманент'],['team','Команда']];",
    "mobile first tabs",
    flags=0
)
mobile = mobile.replace("let serviceCat='all',expanded=false;", "let serviceCat='hair',expanded=false;", 1)
mobile = mobile.replace("на улице Победы", "на улице Академика Каргина")
mobile = mobile.replace("Мытищи · Победы, 16", "Мытищи · Академика Каргина, 25")
mobile = mobile.replace("Ивантеевке на улице Победы, 16", "Мытищах на улице Академика Каргина, 25")
mobile = mobile.replace(">10–20</strong><small>Вт–Вс</small>", ">10–21</strong><small>ежедневно</small>")
mobile = mobile.replace("17</strong><small>услуг</small>", "28</strong><small>услуг</small>")

late_services = """const SERVICES=[];
const add=(cat,title,price,desc='')=>SERVICES.push({cat,title,price,desc});

[
['Волосы','Стрижка женская — короткие волосы','1 300 ₽'],
['Волосы','Стрижка женская — средние волосы','1 500 ₽'],
['Волосы','Стрижка женская — длинные волосы','1 700 ₽'],
['Волосы','Стрижка женская — очень длинные волосы','2 000 ₽'],
['Волосы','Стрижка детская','1 000 ₽'],
['Волосы','Стрижка модельная мужская','1 500 ₽'],
['Волосы','Укладка','1 000 ₽'],
['Волосы','Уход за волосами','1 000 ₽'],
['Волосы','Окрашивание волос в один тон','3 600 ₽'],
['Волосы','Окрашивание корней','3 500 ₽'],
['Волосы','Тонирование волос','3 600 ₽'],
['Волосы','Сложное окрашивание','7 000 ₽'],
['Волосы','Мелирование прикорневое','3 000 ₽'],
['Маникюр','Маникюр аппаратный / комбинированный / классический','1 000 ₽'],
['Маникюр','Маникюр с покрытием гель-лак / гель / укрепление','2 000 ₽'],
['Косметология','Энзимный мягкий пилинг для всех типов кожи','2 000 ₽'],
['Косметология','Аппаратная косметология','Цена по записи'],
['Косметология','Чистка лица','Цена по записи'],
['Косметология','Массаж лица','Цена по записи'],
['Брови','Архитектура бровей','1 500 ₽'],
['Брови','Ламинирование бровей','2 500 ₽'],
['Ресницы','Ламинирование ресниц','2 500 ₽'],
['Эпиляция','Лазерная эпиляция — классическое бикини','1 700 ₽'],
['Эпиляция','Лазерная эпиляция','Цена по записи'],
['Эпиляция','Электроэпиляция','Цена по записи'],
['Эпиляция','Шугаринг','Цена по записи'],
['Эпиляция','Восковая эпиляция','Цена по записи'],
['Макияж','Макияж дневной с ресницами','3 300 ₽']
].forEach(x=>add(x[0],x[1],x[2],x[3]||''));"""
mobile = must_sub(mobile, r"const SERVICES=\[\];.*?(?=const GALLERY=\{)", late_services + "\n\n", "mobile late services")

portfolio = """const PORTFOLIO=[
 {src:'hair00001.webp',alt:'Работа с волосами EVA'},
 {src:'nails00001.webp',alt:'Маникюр EVA'},
 {src:'brows00001.webp',alt:'Брови EVA'},
 {src:'lashes00001.webp',alt:'Ресницы EVA'},
 {src:'lips01.webp',alt:'Перманентный макияж EVA'},
 {src:'hair00002.webp',alt:'Работа с волосами EVA'},
 {src:'nails00002.webp',alt:'Маникюр EVA'}
];"""
mobile = must_sub(mobile, r"const PORTFOLIO=\[\n.*?\n\];", portfolio, "mobile portfolio")
mobile = mobile.replace("port.querySelector('.tn22-port-all').onclick=()=>openGallery('Салон');", "port.querySelector('.tn22-port-all').onclick=()=>openGallery('Волосы');")

mobile = mobile.replace("const serv=$('#tn13Services');let serviceCat='Маникюр',servicesExpanded=false;",
                        "const serv=$('#tn13Services');let serviceCat='Волосы',servicesExpanded=false;")
mobile = must_sub(
    mobile,
    r"const SERVICE_CATS=\[.*?\];",
    "const SERVICE_CATS=['Волосы','Маникюр','Косметология','Брови','Ресницы','Эпиляция','Макияж'];",
    "mobile service category order",
    flags=0
)

reviews = """const REAL_REVIEW_DATA=[
['Марина Ким','Отдельно благодарит Нару за результат окрашивания и тёплую атмосферу салона.'],
['Марина Ким','В отзыве отмечает профессионализм мастера и армянский кофе.'],
['Екатерина Рэй','Нарине помогла грамотно определиться с цветом.'],
['Екатерина Рэй','Окрашивание выполнено аккуратно и быстро.'],
['Клиент EVA · Зуля','Отдельно благодарит Зулю за работу с бровями и рекомендует мастера.'],
['Клиент EVA · Ани','Отдельно отмечает работу Ани и рекомендует косметолога.']
];"""
mobile = must_sub(mobile, r"const REAL_REVIEW_DATA=\[\n.*?\n\];", reviews, "mobile reviews")
mobile = must_sub(
    mobile,
    r"const reviewBase=REAL_REVIEW_DATA;const reviewLanes=.*?;",
    "const reviewLanes=[[REAL_REVIEW_DATA[0],REAL_REVIEW_DATA[1]],[REAL_REVIEW_DATA[2],REAL_REVIEW_DATA[3]],[REAL_REVIEW_DATA[4],REAL_REVIEW_DATA[5]]];",
    "mobile review lanes",
    flags=0
)
mobile = mobile.replace("const reviewGap=12,reviewDuration=780,reviewGroupCount=5;",
                        "const reviewGap=12,reviewDuration=780,reviewGroupCount=2;")

mobile = mobile.replace(
    '<button class="tn22-cta" type="button"><svg',
    '<a class="tn22-cta" href="tel:${PHONE}"><svg',
    1
)
mobile = mobile.replace(
    '</svg><span>Записаться</span></button><a class="tn22-worklink"',
    '</svg><span>Записаться</span></a><a class="tn22-worklink"',
    1
)
mobile = re.sub(r"\nhero\.querySelector\('\.tn22-cta'\)\.addEventListener\('click',\(\)=>\{window\.location\.href='tel:'\+PHONE\}\);", "", mobile, count=1)

mobile = must_sub(
    mobile,
    r"const ROUTE='[^']*';",
    "const ROUTE='https://yandex.ru/maps/?rtext=~55.918782%2C37.779988&rtt=auto';",
    "mobile route",
    flags=0
)
mobile = re.sub(
    r'src="https://yandex\.ru/map-widget/v1/\?mode=search&text=[^"]+&z=16"',
    'src="https://yandex.ru/map-widget/v1/?ll=37.779988%2C55.918782&z=17"',
    mobile,
    count=1
)
mobile = mobile.replace(
    '<a class="tn22-contact" href="${YANDEX_RU}" target="_blank" rel="noopener">${clock}<span><strong>Часы работы</strong><span>Актуальное расписание — в Яндекс Картах</span></span></a>',
    '<div class="tn22-contact">${clock}<span><strong>Ежедневно 10:00–21:00</strong><span>Без выходных</span></span></div>'
)
mobile = must_sub(
    mobile,
    r"function status\(\)\{.*?\}status\(\);",
    """function status(){
const parts=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Moscow',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date());
const get=t=>parts.find(x=>x.type===t)?.value||'0';
const mins=(+get('hour'))*60+(+get('minute'));
const open=mins>=600&&mins<1260;
const el=visit.querySelector('#tn22Status'),txt=el.querySelector('.tn22-status-text');
txt.textContent=open?'Открыто до 21:00':(mins<600?'Закрыто до 10:00':'Закрыто до завтра 10:00');
el.className='tn22-status '+(open?'open':'closed');
const hs=hero.querySelector('.tn50-hero-status');
if(hs){
 const main=hs.querySelector('.tn50-hero-status-main'),sub=hs.querySelector('.tn50-hero-status-sub');
 main.textContent=open?'Открыто':'Закрыто';
 sub.textContent=open?'до 21:00':(mins<600?'до 10:00':'до завтра 10:00');
 hs.classList.toggle('open',open);hs.classList.toggle('closed',!open);
}
}status();""",
    "mobile status"
)

for a,b in [
    ("Часы — в Яндекс Картах","Ежедневно 10:00–21:00"),
    ("Режим работы','смотреть в Яндекс Картах","Режим работы','ежедневно 10:00–21:00"),
    ("Вт–Вс 10:00–20:00","Ежедневно 10:00–21:00"),
    ("10:00–20:00","10:00–21:00"),
]:
    mobile = mobile.replace(a,b)

MOBILE.write_text(mobile, encoding="utf-8")

theme = THEME.read_text(encoding="utf-8")
repls = {
    "--stl-violet:#8f55b5;":"--stl-violet:#c98299;",
    "--stl-violet-deep:#4c285c;":"--stl-violet-deep:#8b4b61;",
    "--stl-dark-violet:#6f3d82;":"--stl-dark-violet:#8d4c63;",
    "--stl-dark-violet-bright:#8d55a5;":"--stl-dark-violet-bright:#b86582;",
    "rgba(145,78,184":"rgba(201,130,153",
    "rgba(161,101,197":"rgba(214,151,170",
    "rgba(147,80,185":"rgba(201,130,153",
    "rgba(151,84,190":"rgba(205,136,158",
    "rgba(150,82,190":"rgba(205,136,158",
    "rgba(143,85,181":"rgba(185,101,128",
    "rgba(111,61,130":"rgba(141,76,99",
    "rgba(157,91,194":"rgba(210,145,165",
    "rgba(189,121,222":"rgba(226,166,184",
    "rgba(62,35,72":"rgba(111,60,78",
    "rgba(73,37,88":"rgba(111,60,78",
    "#342338":"#3a2a30",
    "#c28fd1":"#dda1b2",
    "#c69bd2":"#dca5b5",
    "#cbbfd0":"#d5c2c9",
}
for a,b in repls.items():
    theme = theme.replace(a,b)

pin_css = """
#tn13Visit .tn22-mapwrap{position:relative!important}
#tn13Visit .tn22-mapwrap:before{content:'';position:absolute;z-index:4;left:50%;top:50%;width:28px;height:28px;border-radius:50%;background:rgba(201,130,153,.18);transform:translate(-50%,-50%);pointer-events:none}
#tn13Visit .tn22-mapwrap:after{content:'';position:absolute;z-index:5;left:50%;top:50%;width:12px;height:12px;border:3px solid #fff;border-radius:50%;background:var(--stl-violet);box-shadow:0 3px 12px rgba(38,23,29,.32);transform:translate(-50%,-50%);pointer-events:none}
"""
if "#tn13Visit .tn22-mapwrap:after" not in theme:
    theme = theme.replace("/* Live hero status */", pin_css + "\n/* Live hero status */")
THEME.write_text(theme, encoding="utf-8")

index = INDEX.read_text(encoding="utf-8")
index = index.replace("EVA — салон красоты в Ивантеевке", "EVA — салон красоты в Мытищах")
index = index.replace("--violet:#75665e;", "--violet:#c97f96;")
index = index.replace("--violet-2:#8e7b70;", "--violet-2:#b86682;")
index = index.replace("--violet-soft:#f2ede8;", "--violet-soft:#f8eaf0;")
index = index.replace("rgba(117,102,94,.075)", "rgba(201,127,150,.10)")
index = index.replace("rgba(117,102,94,.2)", "rgba(184,102,130,.22)")
index = index.replace("rgba(117,102,94,.07)", "rgba(201,127,150,.08)")
index = index.replace('<span class="brand-dot">ST</span> EVA', '<span class="brand-dot">E</span> EVA')
index = index.replace("Часы работы — в Яндекс Картах", "Ежедневно 10:00–21:00")
index = index.replace("<strong>Часы работы</strong><span>Актуальный статус и расписание — в Яндекс Картах</span>",
                      "<strong>Ежедневно 10:00–21:00</strong><span>Без выходных</span>")
index = index.replace("<div><h2>Портфолио</h2><p>Работы и пространство EVA</p></div>",
                      "<div><h2>Портфолио</h2><p>Реальные работы мастеров EVA</p></div>")
index = re.sub(r'\n\s*<button class="filter " data-filter="interior">.*?</button>', '', index)
index = re.sub(r'\n\s*<button class="filter " data-filter="team">.*?</button>', '', index)
index = re.sub(r'\n\s*<button class="work-card" data-category="interior".*?</button>', '', index)
index = re.sub(r'\n\s*<button class="work-card" data-category="team".*?</button>', '', index)

desktop_services = [
("hair","Стрижка женская — короткие волосы","1 300 ₽"),
("hair","Стрижка женская — средние волосы","1 500 ₽"),
("hair","Стрижка женская — длинные волосы","1 700 ₽"),
("hair","Стрижка женская — очень длинные волосы","2 000 ₽"),
("hair","Стрижка детская","1 000 ₽"),
("hair","Стрижка модельная мужская","1 500 ₽"),
("hair","Укладка","1 000 ₽"),
("hair","Уход за волосами","1 000 ₽"),
("hair","Окрашивание волос в один тон","3 600 ₽"),
("hair","Окрашивание корней","3 500 ₽"),
("hair","Тонирование волос","3 600 ₽"),
("hair","Сложное окрашивание","7 000 ₽"),
("hair","Мелирование прикорневое","3 000 ₽"),
("nails","Маникюр аппаратный / комбинированный / классический","1 000 ₽"),
("nails","Маникюр с покрытием гель-лак / гель / укрепление","2 000 ₽"),
("face","Энзимный мягкий пилинг для всех типов кожи","2 000 ₽"),
("face","Аппаратная косметология","Цена по записи"),
("face","Чистка лица","Цена по записи"),
("face","Массаж лица","Цена по записи"),
("brows","Архитектура бровей","1 500 ₽"),
("brows","Ламинирование бровей","2 500 ₽"),
("lashes","Ламинирование ресниц","2 500 ₽"),
("depilation","Лазерная эпиляция — классическое бикини","1 700 ₽"),
("depilation","Лазерная эпиляция","Цена по записи"),
("depilation","Электроэпиляция","Цена по записи"),
("depilation","Шугаринг","Цена по записи"),
("depilation","Восковая эпиляция","Цена по записи"),
("other","Макияж дневной с ресницами","3 300 ₽"),
]
groups = """      <div class="service-groups" id="serviceGroups">
        <button class="service-group active" data-service-filter="hair">Волосы</button>
        <button class="service-group" data-service-filter="nails">Маникюр</button>
        <button class="service-group" data-service-filter="face">Косметология</button>
        <button class="service-group" data-service-filter="brows">Брови</button>
        <button class="service-group" data-service-filter="lashes">Ресницы</button>
        <button class="service-group" data-service-filter="depilation">Эпиляция</button>
        <button class="service-group" data-service-filter="other">Макияж</button>
      </div>"""
rows=[]
for i,(cat,name,price) in enumerate(desktop_services):
    extra = "" if cat=="hair" and i < 6 else " extra"
    rows.append(
        f'        <div class="service{extra}" data-service-category="{cat}"><div><div class="service-name">{name}</div>'
        f'<div class="service-note">EVA</div></div><div class="service-side"><div class="price">{price}</div>'
        f'<button class="pick" onclick="openBooking({name!r})">Выбрать</button></div></div>'
    )
service_html = groups + '\n      <div class="services" id="servicesList">\n' + '\n'.join(rows) + '\n      </div>'
index = must_sub(
    index,
    r'      <div class="service-groups" id="serviceGroups">.*?      </div>\n      <button class="show-more" id="servicesMore"',
    service_html + '\n      <button class="show-more" id="servicesMore"',
    "desktop services"
)
index = index.replace("Доступно 31 услуг", f"Доступно {len(desktop_services)} услуг")

desktop_review_cards = """      <article class="review-card"><div class="review-top"><span class="review-name">Марина Ким</span><span class="review-stars">★★★★★</span></div><p class="review-text">Отдельно благодарит Нару за результат окрашивания и тёплую атмосферу салона.</p></article>
      <article class="review-card"><div class="review-top"><span class="review-name">Екатерина Рэй</span><span class="review-stars">★★★★★</span></div><p class="review-text">Нарине помогла грамотно определиться с цветом; окрашивание выполнено аккуратно и быстро.</p></article>
      <article class="review-card"><div class="review-top"><span class="review-name">Клиент EVA · Зуля</span><span class="review-stars">★★★★★</span></div><p class="review-text">Отдельно благодарит Зулю за работу с бровями и рекомендует мастера.</p></article>
      <article class="review-card"><div class="review-top"><span class="review-name">Клиент EVA · Ани</span><span class="review-stars">★★★★★</span></div><p class="review-text">Отдельно отмечает работу Ани и рекомендует косметолога.</p></article>"""
index = must_sub(
    index,
    r'      <article class="review-card">.*?</article>\n      <article class="review-card">.*?</article>',
    desktop_review_cards,
    "desktop reviews"
)
INDEX.write_text(index, encoding="utf-8")

mobile = MOBILE.read_text(encoding="utf-8")
theme = THEME.read_text(encoding="utf-8")
index = INDEX.read_text(encoding="utf-8")
checks = [
    ("hair first mobile", "let serviceCat='Волосы'" in mobile and "const SERVICE_CATS=['Волосы','Маникюр','Косметология'" in mobile),
    ("prices", all(x in mobile for x in ["1 300 ₽","1 500 ₽","1 700 ₽","2 000 ₽","3 600 ₽","7 000 ₽","3 000 ₽"])),
    ("daily schedule", "Ежедневно 10:00–21:00" in mobile and "Открыто до 21:00" in mobile),
    ("portfolio no salon", "const PORTFOLIO=[\n {src:'hair00001.webp'" in mobile and "salon02.webp',alt:'EVA — работа" not in mobile),
    ("phone direct", 'href="tel:${PHONE}"' in mobile and "window.location.href='tel:'" not in mobile),
    ("map coords", "37.779988%2C55.918782" in mobile),
    ("pink theme", "--stl-violet:#c98299;" in theme and "--stl-violet-deep:#8b4b61;" in theme),
    ("review lanes", "reviewGroupCount=2" in mobile and "Клиент EVA · Зуля" in mobile and "Клиент EVA · Ани" in mobile),
    ("desktop mytishchi", "салон красоты в Ивантеевке" not in index),
    ("desktop no ST logo", '<span class="brand-dot">ST</span>' not in index),
]
bad=[name for name,ok in checks if not ok]
if bad:
    raise SystemExit("Audit failed: "+", ".join(bad))
print("EVA FINALIZE OK")
