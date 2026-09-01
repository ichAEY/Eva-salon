from pathlib import Path
import re

p=Path('mobile-eva-current.js')
s=p.read_text(encoding='utf-8')
start=s.index('// REVIEWS')
end=s.index('// VISIT', start)
prefix=s[:start]
suffix=s[end:]
block=s[start:end]

old_render="""reviews.innerHTML=`<div class=\"tn30-reviews\"><p class=\"tn22-kicker\">Отзывы</p><h2>Что говорят о нас</h2><div class=\"tn30-score\"><strong>4,8</strong><div class=\"tn30-stars\">★★★★★</div><div class=\"tn30-count\">92 отзыва на Яндекс Картах</div></div><div class=\"tn30-review-stage\">${reviewLanes.map((lane,i)=>{const loop=[lane[lane.length-1],...lane,lane[0]];return `<div class=\"tn30-lane\" data-lane=\"${i}\"><div class=\"tn30-track\">${loop.map(reviewCard).join('')}</div></div>`}).join('')}</div><a class=\"tn30-review-all\" href=\"${YANDEX_REVIEWS}\" target=\"_blank\" rel=\"noopener\">Смотреть все отзывы →</a></div>`;"""
new_render="""reviews.innerHTML=`<div class=\"tn30-reviews\"><p class=\"tn22-kicker\">Отзывы</p><h2>Что говорят о нас</h2><div class=\"tn30-score\"><strong>4,8</strong><div class=\"tn30-stars\">★★★★★</div><div class=\"tn30-count\">92 отзыва на Яндекс Картах</div></div><div class=\"tn30-review-stage\">${reviewLanes.map((lane,i)=>`<div class=\"tn30-lane\" data-lane=\"${i}\"><div class=\"tn30-track\">${lane.map(reviewCard).join('')}</div></div>`).join('')}</div><a class=\"tn30-review-all\" href=\"${YANDEX_REVIEWS}\" target=\"_blank\" rel=\"noopener\">Смотреть все отзывы →</a></div>`;"""
if old_render not in block:
    raise SystemExit('old review render not found')
block=block.replace(old_render,new_render,1)

motion_start=block.index("const reviewStage=reviews.querySelector('.tn30-review-stage')")
motion_end=block.index("reviewStage.addEventListener('click'", motion_start)
motion_end=block.index(";", motion_end)+1
new_motion=r'''const reviewStage=reviews.querySelector('.tn30-review-stage'),reviewTracks=[...reviews.querySelectorAll('.tn30-track')];
let reviewPauseTimer=0,reviewMotionTimer=0,reviewDragging=false,reviewMoved=false,reviewSuppressClick=false,reviewStartX=0,reviewStartY=0,reviewDx=0;
const reviewGap=12,reviewDuration=780;
function reviewMetrics(){const lane=reviews.querySelector('.tn30-lane'),card=reviews.querySelector('.tn30-review-card');const width=card?card.getBoundingClientRect().width:0;return {step:width+reviewGap,edge:lane?Math.max(0,(lane.clientWidth-width)/2):26}}
function setReviewTrack(track,x,animated){track.style.transition=animated?`transform ${reviewDuration}ms cubic-bezier(.22,.66,.24,1)`:'none';track.style.transform=`translate3d(${x}px,0,0)`}
function paintReviewTracks(animated,drag=0){const {edge}=reviewMetrics();reviewTracks.forEach(t=>setReviewTrack(t,edge+drag,animated))}
function scheduleReviews(){clearTimeout(reviewPauseTimer);reviewPauseTimer=setTimeout(()=>rotateReviewsForward(),4000)}
function rotateReviewsForward(){clearTimeout(reviewPauseTimer);clearTimeout(reviewMotionTimer);const {step,edge}=reviewMetrics();reviewTracks.forEach(t=>setReviewTrack(t,edge-step,true));reviewMotionTimer=setTimeout(()=>{reviewTracks.forEach(t=>{if(t.firstElementChild)t.appendChild(t.firstElementChild);setReviewTrack(t,edge,false)});scheduleReviews()},reviewDuration+40)}
function rotateReviewsBackward(){clearTimeout(reviewPauseTimer);clearTimeout(reviewMotionTimer);const {step,edge}=reviewMetrics();reviewTracks.forEach(t=>{if(t.lastElementChild)t.insertBefore(t.lastElementChild,t.firstElementChild);setReviewTrack(t,edge-step,false)});requestAnimationFrame(()=>requestAnimationFrame(()=>{reviewTracks.forEach(t=>setReviewTrack(t,edge,true));reviewMotionTimer=setTimeout(scheduleReviews,reviewDuration+40)}))}
requestAnimationFrame(()=>{paintReviewTracks(false);scheduleReviews()});
window.addEventListener('resize',()=>paintReviewTracks(false),{passive:true});
reviewStage.addEventListener('pointerdown',e=>{clearTimeout(reviewPauseTimer);clearTimeout(reviewMotionTimer);reviewDragging=true;reviewMoved=false;reviewDx=0;reviewStartX=e.clientX;reviewStartY=e.clientY;reviewStage.classList.add('dragging');paintReviewTracks(false);try{reviewStage.setPointerCapture(e.pointerId)}catch(_){}});
reviewStage.addEventListener('pointermove',e=>{if(!reviewDragging)return;const dx=e.clientX-reviewStartX,dy=e.clientY-reviewStartY;if(!reviewMoved&&Math.abs(dx)<6)return;if(!reviewMoved&&Math.abs(dy)>Math.abs(dx))return;reviewMoved=true;reviewDx=dx;paintReviewTracks(false,reviewDx)});
function finishReviewDrag(e){if(!reviewDragging)return;reviewDragging=false;reviewStage.classList.remove('dragging');try{reviewStage.releasePointerCapture(e.pointerId)}catch(_){}const {step}=reviewMetrics();const shouldMove=reviewMoved&&Math.abs(reviewDx)>Math.min(70,step*.16);reviewSuppressClick=reviewMoved;if(shouldMove){const dir=reviewDx<0?1:-1;reviewDx=0;if(dir>0)rotateReviewsForward();else rotateReviewsBackward()}else{reviewDx=0;paintReviewTracks(true);scheduleReviews()}}
reviewStage.addEventListener('pointerup',finishReviewDrag);reviewStage.addEventListener('pointercancel',finishReviewDrag);reviewStage.addEventListener('click',e=>{if(reviewSuppressClick){e.preventDefault();e.stopPropagation();reviewSuppressClick=false}},true);'''
block=block[:motion_start]+new_motion+block[motion_end:]

# Safety assertions: 5 lanes, exactly 3 unique reviews referenced in each lane, no clone-loop, rest of file untouched.
if block.count('REAL_REVIEW_DATA[') < 15:
    raise SystemExit('review data references unexpectedly low')
if "const reviewLanes=[[REAL_REVIEW_DATA[0],REAL_REVIEW_DATA[1],REAL_REVIEW_DATA[2]],[REAL_REVIEW_DATA[3],REAL_REVIEW_DATA[4],REAL_REVIEW_DATA[5]],[REAL_REVIEW_DATA[6],REAL_REVIEW_DATA[7],REAL_REVIEW_DATA[8]],[REAL_REVIEW_DATA[9],REAL_REVIEW_DATA[10],REAL_REVIEW_DATA[11]],[REAL_REVIEW_DATA[12],REAL_REVIEW_DATA[13],REAL_REVIEW_DATA[14]]];" not in block:
    raise SystemExit('5x3 lane map missing')
if 'const loop=[lane[lane.length-1],...lane,lane[0]]' in block:
    raise SystemExit('clone-loop still present')
if '${lane.map(reviewCard).join(\'\')}' not in block:
    raise SystemExit('three-card lane render missing')

out=prefix+block+suffix
if not out.startswith(prefix) or not out.endswith(suffix):
    raise SystemExit('outside-review content changed')
p.write_text(out,encoding='utf-8')
print('OK: 5 rows x exactly 3 cards, infinite rotation without edge clones')
