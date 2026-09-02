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
const reviewInitial=n=>([...String(n).trim()][0]||'E').toUpperCase();
const reviewHref=r=>`${{YANDEX_REVIEWS}}#:~:text=${{encodeURIComponent(r[1])}}`;
const reviewStarSvg='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.7l2.45 4.96 5.47.8-3.96 3.85.94 5.45L10 14.2l-4.9 2.57.94-5.45L1.08 7.46l5.47-.8L10 1.7Z"/></svg>';
const reviewStars=`<span class="tn30-card-stars" aria-label="5 из 5">${{reviewStarSvg.repeat(5)}}</span>`;
const reviewCard=r=>`<a class="tn30-review-card tn30-review-card-animated" href="${{reviewHref(r)}}" target="_blank" rel="noopener"><div class="tn30-review-head"><span class="tn30-review-avatar">${{reviewInitial(r[0])}}</span><span><strong class="tn30-review-name">${{r[0]}}</strong><span class="tn30-review-meta">Яндекс Карты</span>${{reviewStars}}</span></div><p>${{r[1]}}</p><span class="tn30-review-open">Подробнее →</span></a>`;
const reviewLanes=[REAL_REVIEW_DATA.slice(0,5),REAL_REVIEW_DATA.slice(5,10),REAL_REVIEW_DATA.slice(10,15)];
reviews.innerHTML=`<div class="tn30-reviews"><p class="tn22-kicker">Отзывы</p><h2>Что говорят о нас</h2><div class="tn30-score"><strong>4,8</strong><div class="tn30-stars">★★★★★</div><div class="tn30-count">92 отзыва на Яндекс Картах</div></div><div class="tn30-review-stage tn30-review-stage-3x5">${{reviewLanes.map((lane,i)=>{{const loop=[lane[lane.length-1],...lane,lane[0]];return `<div class="tn30-lane" data-lane="${{i}}"><div class="tn30-track">${{loop.map(reviewCard).join('')}}</div></div>`}}).join('')}}</div><a class="tn30-review-all" href="${{YANDEX_REVIEWS}}" target="_blank" rel="noopener">Смотреть все отзывы →</a></div>`;
const reviewStage=reviews.querySelector('.tn30-review-stage'),reviewTracks=[...reviews.querySelectorAll('.tn30-track')];
let reviewIndex=1,reviewPauseTimer=0,reviewMotionTimer=0,reviewDragging=false,reviewMoved=false,reviewSuppressClick=false,reviewStartX=0,reviewStartY=0,reviewDx=0;
const reviewGap=12,reviewDuration=780,reviewGroupCount=5;
function reviewMetrics(){{const lane=reviews.querySelector('.tn30-lane'),card=reviews.querySelector('.tn30-review-card');const width=card?card.getBoundingClientRect().width:0;return {{step:width+reviewGap,edge:lane?Math.max(0,(lane.clientWidth-width)/2):26}}}}
function paintReviewTracks(animated,drag=0){{const {{step,edge}}=reviewMetrics();reviewTracks.forEach(t=>{{t.style.transition=animated?`transform ${{reviewDuration}}ms cubic-bezier(.22,.66,.24,1)`:'none';t.style.transform=`translate3d(${{edge-reviewIndex*step+drag}}px,0,0)`}})}}
function scheduleReviews(){{clearTimeout(reviewPauseTimer);reviewPauseTimer=setTimeout(()=>moveReviews(reviewIndex+1),4000)}}
function normalizeReviewIndex(){{if(reviewIndex===0){{reviewIndex=reviewGroupCount;paintReviewTracks(false)}}else if(reviewIndex===reviewGroupCount+1){{reviewIndex=1;paintReviewTracks(false)}}}}
function moveReviews(next){{clearTimeout(reviewPauseTimer);clearTimeout(reviewMotionTimer);reviewIndex=Math.max(0,Math.min(reviewGroupCount+1,next));paintReviewTracks(true);reviewMotionTimer=setTimeout(()=>{{normalizeReviewIndex();scheduleReviews()}},reviewDuration+40)}}
requestAnimationFrame(()=>{{paintReviewTracks(false);scheduleReviews()}});
window.addEventListener('resize',()=>paintReviewTracks(false),{{passive:true}});
reviewStage.addEventListener('pointerdown',e=>{{clearTimeout(reviewPauseTimer);clearTimeout(reviewMotionTimer);reviewDragging=true;reviewMoved=false;reviewDx=0;reviewStartX=e.clientX;reviewStartY=e.clientY;reviewStage.classList.add('dragging');paintReviewTracks(false);try{{reviewStage.setPointerCapture(e.pointerId)}}catch(_){{}}}});
reviewStage.addEventListener('pointermove',e=>{{if(!reviewDragging)return;const dx=e.clientX-reviewStartX,dy=e.clientY-reviewStartY;if(!reviewMoved&&Math.abs(dx)<6)return;if(!reviewMoved&&Math.abs(dy)>Math.abs(dx))return;reviewMoved=true;reviewDx=dx;paintReviewTracks(false,reviewDx)}});
function finishReviewDrag(e){{if(!reviewDragging)return;reviewDragging=false;reviewStage.classList.remove('dragging');try{{reviewStage.releasePointerCapture(e.pointerId)}}catch(_){{}}const {{step}}=reviewMetrics();if(reviewMoved&&Math.abs(reviewDx)>Math.min(70,step*.16))reviewIndex+=reviewDx<0?1:-1;reviewIndex=Math.max(0,Math.min(reviewGroupCount+1,reviewIndex));reviewSuppressClick=reviewMoved;reviewDx=0;paintReviewTracks(true);clearTimeout(reviewMotionTimer);reviewMotionTimer=setTimeout(()=>{{normalizeReviewIndex();scheduleReviews()}},reviewDuration+40)}}
reviewStage.addEventListener('pointerup',finishReviewDrag);reviewStage.addEventListener('pointercancel',finishReviewDrag);reviewStage.addEventListener('click',e=>{{if(reviewSuppressClick){{e.preventDefault();e.stopPropagation();reviewSuppressClick=false}}}},true);

// VISIT'''
s, n = re.subn(r'// REVIEWS\n.*?// VISIT', lambda _: block, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('review block replacement failed')
review_block = re.search(r'// REVIEWS\n.*?// VISIT', s, re.S).group(0)
if review_block.count('REAL_REVIEW_DATA.slice(') != 3:
    raise SystemExit('must have exactly three animated review lanes')
if 'reviewGroupCount=5' not in review_block:
    raise SystemExit('five reviews per lane missing')
if 'const loop=[lane[lane.length-1],...lane,lane[0]]' not in review_block:
    raise SystemExit('infinite carousel loop missing')
mobile.write_text(s, encoding='utf-8')

theme_file = Path('mobile-eva-theme-current.js')
theme = theme_file.read_text(encoding='utf-8')
marker = '.tn30-review-all{background:#f1f0f3!important;border-color:rgba(67,58,71,.14)!important}'
# Remove the accidental static 5x3 grid override and any prior animated override.
theme = re.sub(r'\n\.tn30-review-stage-5x3\{.*?(?=\n/\* Contacts \*/)', '\n', theme, count=1, flags=re.S)
theme = re.sub(r'\n\.tn30-review-stage-3x5\{.*?(?=\n/\* Contacts \*/)', '\n', theme, count=1, flags=re.S)
animated_css = '''
.tn30-review-stage-3x5 .tn30-review-card{height:154px!important;min-height:154px!important;max-height:154px!important;overflow:hidden!important;display:flex!important;flex-direction:column!important}
.tn30-review-stage-3x5 .tn30-review-head{flex:0 0 auto!important}
.tn30-card-stars{display:flex!important;gap:1.5px!important;margin-top:4px!important;color:var(--stl-yellow)!important}
.tn30-card-stars svg{width:8px!important;height:8px!important;display:block!important;fill:currentColor!important;flex:0 0 auto!important}
.tn30-review-stage-3x5 .tn30-review-card p{margin-top:8px!important;display:-webkit-box!important;-webkit-box-orient:vertical!important;-webkit-line-clamp:4!important;overflow:hidden!important;text-overflow:ellipsis!important}
.tn30-review-stage-3x5 .tn30-review-open{margin-top:auto!important;padding-top:6px!important;flex:0 0 auto!important}
'''
if marker not in theme:
    raise SystemExit('review theme marker missing')
theme = theme.replace(marker, marker + animated_css, 1)
theme_file.write_text(theme, encoding='utf-8')

index = Path('index.html')
x = index.read_text(encoding='utf-8')
x, n1 = re.subn(r'(mobile-eva-current\.js)(?:\?v=[^"\']*)?', r'\1?v=20260902-animated-3x5', x, count=1)
x, n2 = re.subn(r'(mobile-eva-theme-current\.js)(?:\?v=[^"\']*)?', r'\1?v=20260902-animated-3x5', x, count=1)
if n1 != 1 or n2 != 1:
    raise SystemExit('cache-buster replacement failed')
index.write_text(x, encoding='utf-8')

print('EVA mobile reviews restored: 3 animated rows x 5 unique reviews')
