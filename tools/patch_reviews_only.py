from pathlib import Path
import json

path = Path('mobile-eva-current.js')
s = path.read_text(encoding='utf-8')
start_marker = '// REVIEWS\n'
end_marker = '// VISIT\n'
start = s.index(start_marker)
end = s.index(end_marker, start)
prefix = s[:start]
suffix = s[end:]

reviews = [
    ['Александра Н.', 'Все отлично!! Благодарю) сама хожу в ваш салон на окрашивание, маникюр. И мужа регулярно на стрижку записываю. Все мастера настоящие профессионалы!'],
    ['natalia tatarinceva', 'Все отлично, мастер хороший,  внимательный. \nВсе на высшем уровне. \nРекомендую.  \nСейчас сложно найти салон, где сочетаются цена и качество.  Спасибо'],
    ['Арина Боданова', 'обожаю'],
    ['gugen', 'Хорошо стригут. Если сказать, что живёшь в этом доме (прописку не проверяют) - скидка 20%🔥'],
    ['Екатерина Рэй', 'Была на окрашивании в один тон  у Нарине, оказалось, что она  замечательный специалист, помогла мне грамотно определиться с цветом, всё сделала аккуратно и быстро, очень рада что нашла этот салон! Большая благодарность мастеру! Обязательно обращусь сюда же в следующий раз 🌹'],
    ['aaarinkooo', 'Сегодня ходила в этот салон на наращивание ногтей, я в восторге, очень аккуратно, красиво и быстро сделал мастер, буду ходить ещё!💅🏻🫶🏻'],
    ['Алина Жукова', 'Подстригался сын остались очень довольны 👍 спасибо придём обязательно еще 🌸'],
    ['Светлана Старчикова', 'Мне очень нравится этот салон! Все девушки очень приятные, записываться можно к любой - все сделают на высшем уровне!'],
    ['Екатерина', 'Маникюр сделали быстро, качественно,'],
    ['Aliya Uderbaeva', 'Хочу выразить огромную благодарность Наре!!!Мастер-золото!!!Попала благодаря отзывам,было немного волнения, но результат превзошел ожидания!!!!После первого посещения, осталась довольна и теперь только к ней!!!В салоне атмосфера -супер!!!В последний раз приходила с дочкой,мечтала о розовых локонах!!!Результат-ребенок счастлив!!!Всем рекомендую данный салон!!!Девочки-огонь!!!!!'],
    ['Оксана Вайнбергер', 'Была первый раз в салоне Эва, у мастера маникюра Татев. Очень хороший мастер, все аккуратно, красиво и быстро!!! Спасибо, мастеру!♥️'],
    ['Ю.В. Куликова', 'Мастер Елена просто чудо! Легкая рука, эпиляцию сделали мега быстро и безболезненно. С Еленой максимально комфортно взаимодействовать, интересный собеседник. Однозначно рекомендую за такой процедурой обращаться именно к Елене!'],
    ['Алина С.', 'Что касается салона в целом: удобное расположение, приятные цены, приветливый коллектив, всегда дружелюбная атмосфера. \n\nОтдельно хочу отметить мастера по маникюру Розу. Она замечательный профессионал своего дела и просто чуткий человек. Маникюр держится превосходно и ручки после нее выглядят потрясающе. Спасибо 🌹 \n\nХочу дополнить отзыв: была записана на окрашивание к Нарине, как вдруг во всем доме выключили свет, но мастер не растерялась и справилась блестяще со своей работой в таких экстремальных условиях. Тут работают настоящие профессионалы!'],
    ['Зарета К.', 'Мастер Евгения, лучшая в своём деле.Очень красиво подстригла, объяснила как делать укладку дома.'],
    ['Марина Ким', 'Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'],
]
assert len(reviews) == 15
assert len({text for _, text in reviews}) == 15

js_data = json.dumps(reviews, ensure_ascii=False, indent=0)
lanes = ','.join(
    '[' + ','.join(f'REAL_REVIEW_DATA[{j}]' for j in range(i, i + 3)) + ']'
    for i in range(0, 15, 3)
)

block = f'''// REVIEWS
const reviews=$('#tn13Reviews');
const REAL_REVIEW_DATA={js_data};
const reviewInitial=n=>([...String(n).trim()][0]||'E').toUpperCase();
const reviewHref=r=>`${{YANDEX_REVIEWS}}#:~:text=${{encodeURIComponent(r[1])}}`;
const reviewStarSvg='<svg viewBox="0 0 20 20" aria-hidden="true" style="width:12px;height:12px;display:block;fill:currentColor"><path d="M10 1.7l2.45 4.96 5.47.8-3.96 3.85.94 5.45L10 14.2l-4.9 2.57.94-5.45L1.08 7.46l5.47-.8L10 1.7Z"/></svg>';
const reviewStars=`<span aria-label="5 из 5" style="display:flex;gap:2px;margin-top:7px;color:#b78d4f">${{reviewStarSvg.repeat(5)}}</span>`;
const reviewCard=r=>`<a class="tn30-review-card" href="${{reviewHref(r)}}" target="_blank" rel="noopener"><div class="tn30-review-head"><span class="tn30-review-avatar">${{reviewInitial(r[0])}}</span><span><strong class="tn30-review-name">${{r[0]}}</strong><span class="tn30-review-meta">Яндекс Карты</span>${{reviewStars}}</span></div><p>${{r[1]}}</p><span class="tn30-review-open">Подробнее →</span></a>`;
const reviewLanes=[{lanes}];
reviews.innerHTML=`<div class="tn30-reviews"><p class="tn22-kicker">Отзывы</p><h2>Что говорят о нас</h2><div class="tn30-score"><strong>4,8</strong><div class="tn30-stars">★★★★★</div><div class="tn30-count">92 отзыва на Яндекс Картах</div></div><div class="tn30-review-stage">${{reviewLanes.map((lane,i)=>{{const loop=[lane[lane.length-1],...lane,lane[0]];return `<div class="tn30-lane" data-lane="${{i}}"><div class="tn30-track">${{loop.map(reviewCard).join('')}}</div></div>`}}).join('')}}</div><a class="tn30-review-all" href="${{YANDEX_REVIEWS}}" target="_blank" rel="noopener">Смотреть все отзывы →</a></div>`;
const reviewStage=reviews.querySelector('.tn30-review-stage'),reviewTracks=[...reviews.querySelectorAll('.tn30-track')];
let reviewIndex=1,reviewPauseTimer=0,reviewMotionTimer=0,reviewDragging=false,reviewMoved=false,reviewSuppressClick=false,reviewStartX=0,reviewStartY=0,reviewDx=0;
const reviewGap=12,reviewDuration=780,reviewGroupCount=3;
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

'''

new = prefix + block + suffix
assert new.startswith(prefix)
assert new.endswith(suffix)
assert new.count('const REAL_REVIEW_DATA=') == 1
assert new.count('const reviewLanes=') == 1
assert 'reviewGroupCount=3' in block
assert lanes.count('REAL_REVIEW_DATA[') == 15
assert block.count('const reviewStarSvg=') == 1

path.write_text(new, encoding='utf-8')
print('PATCH_OK')
print('outside_review_block_unchanged=true')
print('reviews=15 rows=5 per_row=3 reviewGroupCount=3')
