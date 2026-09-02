from pathlib import Path
import re, html

# Exact service list from the user's screenshots of Yandex profile 1179517154.
SERVICES = [
    ('hair','Волосы','Стрижка женская (короткие)','1 300 ₽'),
    ('hair','Волосы','Стрижка женская (средние)','1 500 ₽'),
    ('hair','Волосы','Стрижка женская (длинные)','1 700 ₽'),
    ('hair','Волосы','Стрижка женская (оч. длинные)','2 000 ₽'),
    ('hair','Волосы','Стрижка детская','1 000 ₽'),
    ('hair','Волосы','Укладка','1 000 ₽'),
    ('hair','Волосы','Уход за волосами','1 000 ₽'),
    ('hair','Волосы','Окрашивание волос в один тон','3 600 ₽'),
    ('hair','Волосы','Окрашивание корней','3 500 ₽'),
    ('hair','Волосы','Тонирование волос','3 600 ₽'),
    ('hair','Волосы','Сложное окрашивание','7 000 ₽'),
    ('hair','Волосы','Мелирование прикорневое','3 000 ₽'),
    ('hair','Волосы','Стрижка модельная мужская','1 500 ₽'),
    ('browslashes','Брови и ресницы','Архитектура бровей','1 500 ₽'),
    ('browslashes','Брови и ресницы','Ламинирование бровей/ Ламинирование ресниц','2 500 ₽'),
    ('nails','Маникюр','Маникюр аппаратный/комбинированный/классический','1 000 ₽'),
    ('nails','Маникюр','Маникюр с покрытием гель-лак/гель/укрепление','2 000 ₽'),
]
assert len(SERVICES) == 17
assert len({x[2] for x in SERVICES}) == 17
CATS = [('hair','Волосы'),('browslashes','Брови и ресницы'),('nails','Маникюр')]

# ---------------- desktop index.html ----------------
p = Path('index.html')
s = p.read_text(encoding='utf-8')

filters = '<div class="service-groups" id="serviceGroups">\n' + '\n'.join(
    f'        <button class="service-group{" active" if i==0 else ""}" data-service-filter="{key}">{label}</button>'
    for i,(key,label) in enumerate(CATS)
) + '\n      </div>'

rows=[]
for i,(key,label,title,price) in enumerate(SERVICES):
    cls='service' + (' extra' if i >= 6 else '')
    t=html.escape(title, quote=True)
    rows.append(
        f'        <div class="{cls}" data-service-category="{key}"><div><div class="service-name">{t}</div><div class="service-note">EVA · Яндекс Карты</div></div><div class="service-side"><div class="price">{price}</div><button class="pick" onclick="openBooking(\'{t}\')">Выбрать</button></div></div>'
    )

section = '''    <section id="services">
      <div class="section-head"><div><h2>Услуги</h2><p>Услуги и цены из карточки EVA в Яндекс Картах</p></div></div>
      ''' + filters + '''
      <div class="services" id="servicesList">
''' + '\n'.join(rows) + '''
      </div>
      <button class="show-more" id="servicesMore" type="button">Посмотреть ещё</button>
    </section>'''

s,n = re.subn(r'    <section id="services">.*?    </section>', section, s, count=1, flags=re.S)
assert n == 1, 'desktop service section not replaced'
s = re.sub(r'<div class="availability"><strong>Доступно \d+ услуг</strong><span>.*?</span></div>',
           '<div class="availability"><strong>Доступно 17 услуг</strong><span>Волосы · брови и ресницы · маникюр</span></div>', s, count=1)
s = re.sub(r'mobile-eva-current\.js\?v=[^"\']+', 'mobile-eva-current.js?v=20260902-services-exact17', s)
p.write_text(s, encoding='utf-8')

# ---------------- mobile-eva-current.js ----------------
p = Path('mobile-eva-current.js')
s = p.read_text(encoding='utf-8')

first_array = 'const services=[\n' + ',\n'.join(
    f"    ['{key}','{title.replace(chr(39), chr(92)+chr(39))}','{price}']" for key,label,title,price in SERVICES
) + '\n  ];'
s,n = re.subn(r'const services=\[.*?\n  \];', first_array, s, count=1, flags=re.S)
assert n == 1, 'first mobile services array not replaced'

first_tabs = "const serviceTabs=[['hair','Волосы'],['browslashes','Брови и ресницы'],['nails','Маникюр']];"
s,n = re.subn(r'const serviceTabs=\[.*?\];', first_tabs, s, count=1)
assert n == 1, 'first mobile service tabs not replaced'

refined = '[\n' + ',\n'.join(
    f"['{label}','{title.replace(chr(39), chr(92)+chr(39))}','{price}']" for key,label,title,price in SERVICES
) + "\n].forEach(x=>add(x[0],x[1],x[2],x[3]||''));"
s,n = re.subn(r"\[\n\['Волосы'.*?\n\]\.forEach\(x=>add\(x\[0\],x\[1\],x\[2\],x\[3\]\|\|''\)\);", refined, s, count=1, flags=re.S)
assert n == 1, 'refined mobile services array not replaced'

s,n = re.subn(r"const SERVICE_CATS=\[.*?\];", "const SERVICE_CATS=['Волосы','Брови и ресницы','Маникюр'];", s, count=1)
assert n == 1, 'refined mobile service categories not replaced'

p.write_text(s, encoding='utf-8')

# ---------------- strict audit ----------------
idx = Path('index.html').read_text(encoding='utf-8')
mob = Path('mobile-eva-current.js').read_text(encoding='utf-8')

# Desktop: exactly 17 service rows and 3 category buttons.
service_section = re.search(r'<section id="services">.*?</section>', idx, re.S).group(0)
assert service_section.count('class="service') >= 17
assert service_section.count('data-service-category=') == 17
assert service_section.count('data-service-filter=') == 3

# Mobile refined list has all 17 exact names and only the 3 requested categories.
for _,_,title,price in SERVICES:
    assert title in idx, f'missing desktop {title}'
    assert title in mob, f'missing mobile {title}'
    assert price in idx and price in mob
for label in ('Волосы','Брови и ресницы','Маникюр'):
    assert label in idx and label in mob

# Wrong replacement-service titles must not survive inside the desktop services section.
wrong = [
    'Женская стрижка</div>','Мужская стрижка</div>','Окрашивание волос</div>',
    'Укладка волос</div>','Педикюр</div>','Чистка лица</div>','Пилинг</div>',
    'Инъекционные процедуры</div>','Коррекция фигуры</div>','Коррекция бровей</div>',
    'Услуги для ресниц</div>','Шугаринг</div>','Восковая эпиляция</div>',
    'Перманентный макияж</div>'
]
for w in wrong:
    assert w not in service_section, f'old wrong service remains: {w}'

# Refined mobile list invariant.
block = re.search(r"const SERVICES=\[\];.*?const GALLERY=", mob, re.S).group(0)
assert block.count("['Волосы'") == 13
assert block.count("['Брови и ресницы'") == 2
assert block.count("['Маникюр'") == 2
assert "const SERVICE_CATS=['Волосы','Брови и ресницы','Маникюр'];" in mob

print('OK: exact Yandex screenshot services installed: 17 total = 13 hair + 2 brows/lashes + 2 manicure')
