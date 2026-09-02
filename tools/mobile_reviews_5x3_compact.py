from pathlib import Path
import json
import re

REVIEWS = [
    ['Александра Н.','Все отлично!! Благодарю) сама хожу в ваш салон на окрашивание, маникюр. И мужа регулярно на стрижку записываю. Все мастера настоящие профессионалы!'],
    ['natalia tatarinceva','Все отлично, мастер хороший,  внимательный.\nВсе на высшем уровне.\nРекомендую.\nСейчас сложно найти салон, где сочетаются цена и качество.  Спасибо'],
    ['Арина Боданова','обожаю'],
    ['gugen','Хорошо стригут. Если сказать, что живёшь в этом доме (прописку не проверяют) - скидка 20%🔥'],
    ['Екатерина Рэй','Была на окрашивании в один тон  у Нарине, оказалось, что она  замечательный специалист, помогла мне грамотно определиться с цветом, всё сделала аккуратно и быстро, очень рада что нашла этот салон! Большая благодарность мастеру! Обязательно обращусь сюда же в следующий раз 🌹'],
    ['aaarinkooo','Сегодня ходила в этот салон на наращивание ногтей, я в восторге, очень аккуратно, красиво и быстро сделал мастер, буду ходить ещё!💅🏻🫶🏻'],
    ['Алина Жукова','Подстригался сын остались очень довольны 👍 спасибо придём обязательно еще 🌸'],
    ['Светлана Старчикова','Мне очень нравится этот салон! Все девушки очень приятные, записываться можно к любой - все сделают на высшем уровне!'],
    ['Екатерина','Маникюр сделали быстро, качественно,'],
    ['Aliya Uderbaeva','Хочу выразить огромную благодарность Наре!!!Мастер-золото!!!Попала благодаря отзывам,было немного волнения, но результат превзошел ожидания!!!!После первого посещения, осталась довольна и теперь только к ней!!!В салоне атмосфера -супер!!!В последний раз приходила с дочкой,мечтала о розовых локонах!!!Результат-ребенок счастлив!!!Всем рекомендую данный салон!!!Девочки-огонь!!!!!'],
    ['Оксана Вайнбергер','Была первый раз в салоне Эва, у мастера маникюра Татев. Очень хороший мастер, все аккуратно, красиво и быстро!!! Спасибо, мастеру!♥️'],
    ['Ю.В. Куликова','Мастер Елена просто чудо! Легкая рука, эпиляцию сделали мега быстро и безболезненно. С Еленой максимально комфортно взаимодействовать, интересный собеседник. Однозначно рекомендую за такой процедурой обращаться именно к Елене!'],
    ['Алина С.','Что касается салона в целом: удобное расположение, приятные цены, приветливый коллектив, всегда дружелюбная атмосфера.\n\nОтдельно хочу отметить мастера по маникюру Розу. Она замечательный профессионал своего дела и просто чуткий человек. Маникюр держится превосходно и ручки после нее выглядят потрясающе. Спасибо 🌹\n\nХочу дополнить отзыв: была записана на окрашивание к Нарине, как вдруг во всем доме выключили свет, но мастер не растерялась и справилась блестяще со своей работой в таких экстремальных условиях. Тут работают настоящие профессионалы!'],
    ['Зарета К.','Мастер Евгения, лучшая в своём деле.Очень красиво подстригла, объяснила как делать укладку дома.'],
    ['Марина Ким','Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'],
]

if len(REVIEWS) != 15 or len({tuple(x) for x in REVIEWS}) != 15:
    raise SystemExit('review data must contain exactly 15 unique reviews')

mobile = Path('mobile-eva-current.js')
s = mobile.read_text(encoding='utf-8')
data = json.dumps(REVIEWS, ensure_ascii=False)
block = f'''// REVIEWS
const reviews=$('#tn13Reviews');
const REAL_REVIEW_DATA={data};
const reviewHref=r=>`${{YANDEX_REVIEWS}}#:~:text=${{encodeURIComponent(r[1])}}`;
const reviewStarSvg='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.7l2.45 4.96 5.47.8-3.96 3.85.94 5.45L10 14.2l-4.9 2.57.94-5.45L1.08 7.46l5.47-.8L10 1.7Z"/></svg>';
const reviewStars=`<span class="tn30-card-stars" aria-label="5 из 5">${{reviewStarSvg.repeat(5)}}</span>`;
const reviewCard=r=>`<a class="tn30-review-card tn30-review-card-compact" href="${{reviewHref(r)}}" target="_blank" rel="noopener"><div class="tn30-review-head"><span><strong class="tn30-review-name">${{r[0]}}</strong><span class="tn30-review-meta">Яндекс Карты</span>${{reviewStars}}</span></div><p>${{r[1]}}</p><span class="tn30-review-open">Подробнее →</span></a>`;
const reviewLanes=[REAL_REVIEW_DATA.slice(0,3),REAL_REVIEW_DATA.slice(3,6),REAL_REVIEW_DATA.slice(6,9),REAL_REVIEW_DATA.slice(9,12),REAL_REVIEW_DATA.slice(12,15)];
reviews.innerHTML=`<div class="tn30-reviews"><p class="tn22-kicker">Отзывы</p><h2>Что говорят о нас</h2><div class="tn30-score"><strong>4,8</strong><div class="tn30-stars">★★★★★</div><div class="tn30-count">92 отзыва на Яндекс Картах</div></div><div class="tn30-review-stage tn30-review-stage-5x3">${{reviewLanes.map((lane,i)=>`<div class="tn30-lane" data-lane="${{i}}"><div class="tn30-track">${{lane.map(reviewCard).join('')}}</div></div>`).join('')}}</div><a class="tn30-review-all" href="${{YANDEX_REVIEWS}}" target="_blank" rel="noopener">Смотреть все отзывы →</a></div>`;

// VISIT'''
s, n = re.subn(r'// REVIEWS\n.*?// VISIT', block, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('review block replacement failed')
review_block = re.search(r'// REVIEWS\n.*?// VISIT', s, re.S).group(0)
if review_block.count('REAL_REVIEW_DATA.slice(') != 5:
    raise SystemExit('must have five review rows')
if 'reviewGroupCount' in review_block:
    raise SystemExit('old carousel logic remains')
mobile.write_text(s, encoding='utf-8')

theme_file = Path('mobile-eva-theme-current.js')
theme = theme_file.read_text(encoding='utf-8')
marker = '.tn30-review-all{background:#f1f0f3!important;border-color:rgba(67,58,71,.14)!important}'
compact_css = '''
.tn30-review-stage-5x3{display:grid!important;gap:9px!important;margin:32px 14px 0!important;overflow:visible!important;touch-action:auto!important;cursor:default!important;user-select:auto!important}
.tn30-review-stage-5x3 .tn30-lane{width:100%!important;overflow:visible!important}
.tn30-review-stage-5x3 .tn30-track{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:7px!important;width:100%!important;transform:none!important;transition:none!important}
.tn30-review-stage-5x3 .tn30-review-card{flex:none!important;width:auto!important;min-width:0!important;height:136px!important;min-height:136px!important;padding:10px 9px 9px!important;border-radius:11px!important;display:flex!important;flex-direction:column!important;overflow:hidden!important}
.tn30-review-stage-5x3 .tn30-review-head{display:block!important;margin:0!important}
.tn30-review-stage-5x3 .tn30-review-avatar{display:none!important}
.tn30-review-stage-5x3 .tn30-review-name{display:block!important;font-size:11.5px!important;line-height:1.05!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
.tn30-review-stage-5x3 .tn30-review-meta{display:block!important;margin-top:4px!important;font-size:6.8px!important;letter-spacing:.06em!important}
.tn30-card-stars{display:flex!important;gap:1px!important;margin-top:5px!important;color:var(--stl-yellow)!important}
.tn30-card-stars svg{width:7px!important;height:7px!important;display:block!important;fill:currentColor!important;flex:0 0 auto!important}
.tn30-review-stage-5x3 .tn30-review-card p{margin:7px 0 0!important;font-size:9px!important;line-height:1.28!important;display:-webkit-box!important;-webkit-box-orient:vertical!important;-webkit-line-clamp:4!important;overflow:hidden!important;text-overflow:ellipsis!important}
.tn30-review-stage-5x3 .tn30-review-open{display:block!important;margin-top:auto!important;padding-top:5px!important;font-size:7.4px!important;line-height:1!important;white-space:nowrap!important}
'''
# Remove any previous compact override if this script is rerun.
theme = re.sub(r'\n\.tn30-review-stage-5x3\{.*?(?=\n/\* Contacts \*/)', '\n', theme, count=1, flags=re.S)
if marker not in theme:
    raise SystemExit('review theme marker missing')
theme = theme.replace(marker, marker + compact_css, 1)
theme_file.write_text(theme, encoding='utf-8')

index = Path('index.html')
x = index.read_text(encoding='utf-8')
x, n1 = re.subn(r'(mobile-eva-current\.js)(?:\?v=[^"\']*)?', r'\1?v=20260902-5x3-compact', x, count=1)
x, n2 = re.subn(r'(mobile-eva-theme-current\.js)(?:\?v=[^"\']*)?', r'\1?v=20260902-5x3-compact', x, count=1)
if n1 != 1 or n2 != 1:
    raise SystemExit('cache-buster replacement failed')
index.write_text(x, encoding='utf-8')

print('EVA mobile reviews patched: 5 rows x 3 compact cards')
