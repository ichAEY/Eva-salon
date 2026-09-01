from pathlib import Path
import re

MOBILE = Path('mobile-eva-current.js')
INDEX = Path('index.html')

mobile = MOBILE.read_text(encoding='utf-8')
index = INDEX.read_text(encoding='utf-8')

ABOUT_LEAD = 'EVA — салон красоты в Мытищах, где основные бьюти‑процедуры собраны в одном месте.'
ABOUT_COPY = 'Здесь работают с волосами, ногтями, бровями и ресницами, предлагают косметологические процедуры, эпиляцию и макияж. Формат салона позволяет удобно сочетать разные услуги и подобрать уход под свой образ.'

# Rating requested from the current client card view; review count remains the current 92 reviews.
mobile = mobile.replace("const RATING='5,0';", "const RATING='4,8';")
mobile = mobile.replace('>5,0</strong>', '>4,8</strong>')
mobile = mobile.replace('★ 5,0 <span>рейтинг салона</span>', '★ 4,8 <span>рейтинг салона</span>')
mobile = mobile.replace('<strong>5,0</strong><div class="tn30-stars">', '<strong>4,8</strong><div class="tn30-stars">')
mobile = mobile.replace('92 отзыва на Яндекс Картах', '92 отзыва на Яндекс Картах')

# About copy: no references to Yandex as marketing copy and no online-booking claim.
mobile = mobile.replace(
    'EVA — салон красоты в Мытищах с несколькими направлениями в одном пространстве.',
    ABOUT_LEAD
)
mobile = mobile.replace(
    'В Яндекс Картах для EVA указаны парикмахерские услуги, маникюр и педикюр, косметология, брови и ресницы, эпиляция, Wi‑Fi, оплата картой и онлайн-запись.',
    ABOUT_COPY
)
mobile = mobile.replace(
    '<div class="tn42-facts"><div class="tn42-fact">Маникюр и педикюр</div><div class="tn42-fact">Волосы и косметология</div><div class="tn42-fact">Онлайн-запись</div></div>',
    '<div class="tn42-facts"><div class="tn42-fact">7 направлений красоты</div><div class="tn42-fact">Ежедневно 10:00–21:00</div><div class="tn42-fact">Запись по телефону</div></div>'
)

# Floating nav: About immediately after Services, while keeping the STLuxe navigation mechanics.
mobile = mobile.replace(
    "const sectionIds=['tn13Portfolio','tn13Services','tn13Team','tn13Reviews','tn13Visit'];",
    "const sectionIds=['tn13Portfolio','tn13Services','tn38About','tn13Team','tn13Reviews','tn13Visit'];"
)
mobile = mobile.replace(
    "sectionNav.innerHTML=[['tn13Portfolio','Портфолио'],['tn13Services','Услуги'],['tn13Team','Команда'],['tn13Reviews','Отзывы'],['tn13Visit','Визит']]",
    "sectionNav.innerHTML=[['tn13Portfolio','Портфолио'],['tn13Services','Услуги'],['tn38About','О нас'],['tn13Team','Команда'],['tn13Reviews','Отзывы'],['tn13Visit','Визит']]"
)
mobile = mobile.replace('>О салоне</a>', '>О нас</a>')

# No direct phone invocation from the hero. First open the booking sheet, then the visitor taps the phone link explicitly.
hero_anchor = '<a class="tn22-cta" href="tel:${PHONE}"><svg'
hero_button = '<button class="tn22-cta" type="button"><svg'
if hero_anchor in mobile:
    mobile = mobile.replace(hero_anchor, hero_button, 1)
    mobile = mobile.replace('</svg><span>Записаться</span></a><a class="tn22-worklink"', '</svg><span>Записаться</span></button><a class="tn22-worklink"', 1)
if "hero.querySelector('.tn22-cta').addEventListener('click',book);" not in mobile:
    marker = "const menuButton=hero.querySelector('.tn22-menu');"
    mobile = mobile.replace(marker, "hero.querySelector('.tn22-cta').addEventListener('click',book);\n" + marker, 1)

# Remove any remaining programmatic telephone navigation if an older template fragment survived.
mobile = re.sub(r"\s*window\.location\.href\s*=\s*['\"]tel:[^;]+;?", '', mobile)
mobile = re.sub(r"\s*location\.href\s*=\s*['\"]tel:[^;]+;?", '', mobile)

# Reviews: delete all synthetic/paraphrased copy. Only verbatim snippets from the visible Yandex reviews remain,
# and each lane has different content. Cards link to Yandex for the full original review.
reviews_block = """const REAL_REVIEW_DATA=[
['Марина Ким','Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'],
['Екатерина Рэй','Большая благодарность мастеру! Обязательно обращусь сюда же']
];"""
mobile, n = re.subn(r"const REAL_REVIEW_DATA=\[\n.*?\n\];", reviews_block, mobile, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace mobile review data')
mobile, n = re.subn(
    r"const reviewLanes=.*?;\nreviews\.innerHTML=",
    "const reviewLanes=[[REAL_REVIEW_DATA[0],REAL_REVIEW_DATA[1]],[REAL_REVIEW_DATA[1],REAL_REVIEW_DATA[0]]];\nreviews.innerHTML=",
    mobile,
    count=1,
    flags=re.S
)
if n != 1:
    raise SystemExit('Could not replace review lanes')
mobile = re.sub(r"const reviewGap=12,reviewDuration=780,reviewGroupCount=\d+;", "const reviewGap=12,reviewDuration=780,reviewGroupCount=2;", mobile, count=1)

# Remove any old synthetic review strings that may exist in another data layer.
for bad in [
    'Клиент EVA · Зуля', 'Клиент EVA · Ани',
    'Отдельно благодарит Нару за результат окрашивания и тёплую атмосферу салона.',
    'В отзыве отмечает профессионализм мастера и армянский кофе.',
    'Нарине помогла грамотно определиться с цветом.',
    'Окрашивание выполнено аккуратно и быстро.',
    'Профессиональный мастер Нара; отдельно благодарит за результат окрашивания и тёплую атмосферу салона.',
    'Нарине помогла грамотно определиться с цветом и выполнила окрашивание аккуратно и быстро.'
]:
    mobile = mobile.replace(bad, '')

# Booking language: phone only, no online-booking promise.
mobile = mobile.replace('Записаться онлайн', 'Записаться по телефону')
mobile = mobile.replace('Онлайн-запись', 'Запись по телефону')
mobile = mobile.replace('онлайн-запись', 'запись по телефону')
mobile = mobile.replace('онлайн запись', 'запись по телефону')

# Desktop/fallback stays consistent with the same EVA facts.
index = index.replace('5,0', '4,8')
index = index.replace('Онлайн-запись', 'Запись по телефону')
index = index.replace('онлайн-запись', 'запись по телефону')
index = index.replace('онлайн запись', 'запись по телефону')
index = index.replace('Записаться онлайн', 'Записаться по телефону')
index = index.replace(
    '<button class="nav-chip" data-target="services">Услуги</button>\n        <button class="nav-chip" data-target="team">Специалисты</button>',
    '<button class="nav-chip" data-target="services">Услуги</button>\n        <button class="nav-chip" data-target="about">О нас</button>\n        <button class="nav-chip" data-target="team">Специалисты</button>'
)
index = index.replace("const watched=['top','portfolio','services','team','reviews','visit'];", "const watched=['top','portfolio','services','about','team','reviews','visit'];")
index = index.replace(
    '<div class="section-head"><div><h2>О EVA</h2><p>Салон красоты в Мытищах с несколькими направлениями в одном пространстве</p></div></div>\n      <div class="about-card"><h3>Услуги красоты в одном месте</h3><p>EVA предлагает парикмахерские услуги, маникюр и педикюр, косметологию, оформление бровей и ресниц, эпиляцию и макияж. В карточке Яндекс также указаны Wi‑Fi, оплата картой и онлайн-запись.</p></div>',
    f'<div class="section-head"><div><h2>О EVA</h2><p>{ABOUT_LEAD}</p></div></div>\n      <div class="about-card"><h3>Красота в одном пространстве</h3><p>{ABOUT_COPY}</p></div>'
)

# Fallback review cards: verbatim snippets only.
index = re.sub(
    r'<article class="review-card"><div class="review-top"><span class="review-name">Марина Ким</span>.*?</article>\s*<article class="review-card"><div class="review-top"><span class="review-name">Екатерина Рэй</span>.*?</article>',
    '<article class="review-card"><div class="review-top"><span class="review-name">Марина Ким</span><span class="review-stars">★★★★★</span></div><p class="review-text">Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))</p></article>\n      <article class="review-card"><div class="review-top"><span class="review-name">Екатерина Рэй</span><span class="review-stars">★★★★★</span></div><p class="review-text">Большая благодарность мастеру! Обязательно обращусь сюда же</p></article>',
    index,
    count=1,
    flags=re.S
)

# Explicit call must remain user-triggered inside the booking sheet / contact links only.
if 'window.location.href' in mobile and 'tel:' in mobile:
    raise SystemExit('Programmatic tel navigation still exists in mobile')
if 'Клиент EVA ·' in mobile:
    raise SystemExit('Synthetic review author remains')
if 'онлайн-запись' in mobile.lower() or 'онлайн-запись' in index.lower():
    raise SystemExit('Online booking wording remains')
if "['tn38About','О нас']" not in mobile:
    raise SystemExit('About nav item missing')
if ABOUT_LEAD not in mobile or ABOUT_COPY not in mobile:
    raise SystemExit('New About copy missing')
if '<strong>4,8</strong><div class="tn30-stars">' not in mobile:
    raise SystemExit('Review score not updated')
if '92 отзыва на Яндекс Картах' not in mobile:
    raise SystemExit('Review count missing')

MOBILE.write_text(mobile, encoding='utf-8')
INDEX.write_text(index, encoding='utf-8')
print('EVA about/reviews/call patch OK')
