(function(){
'use strict';
if(!window.matchMedia||!window.matchMedia('(max-width:767px)').matches)return;
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;

const root=document.getElementById('eva-tanem-v13');
if(!root)return;

const style=document.createElement('style');
style.id='eva-motion-v1';
style.textContent=`
@media(max-width:767px) and (prefers-reduced-motion:no-preference){
  #eva-tanem-v13.eva-motion-ready .eva-hero-motion{
    opacity:0;
    transform:translate3d(0,10px,0);
    transition:opacity .42s ease,transform .52s cubic-bezier(.22,.72,.28,1);
    will-change:opacity,transform;
  }
  #eva-tanem-v13.eva-motion-ready.eva-motion-start .eva-hero-motion{
    opacity:1;
    transform:translate3d(0,0,0);
  }
  #eva-tanem-v13 .eva-reveal-motion{
    opacity:0;
    transform:translate3d(0,14px,0);
    transition:opacity .46s ease,transform .56s cubic-bezier(.22,.72,.28,1);
    will-change:opacity,transform;
  }
  #eva-tanem-v13 .eva-reveal-motion.eva-inview{
    opacity:1;
    transform:translate3d(0,0,0);
  }
  #eva-tanem-v13 .eva-item-motion{
    opacity:0;
    transform:translate3d(0,10px,0) scale(.985);
    transition:opacity .36s ease,transform .46s cubic-bezier(.22,.72,.28,1);
    transition-delay:var(--eva-delay,0ms);
    will-change:opacity,transform;
  }
  #eva-tanem-v13 .eva-item-motion.eva-inview{
    opacity:1;
    transform:translate3d(0,0,0) scale(1);
  }
  #eva-tanem-v13 .tn31-service-row.eva-service-enter{
    animation:evaServiceEnter .34s cubic-bezier(.22,.72,.28,1) both;
    animation-delay:var(--eva-delay,0ms);
  }
  @keyframes evaServiceEnter{
    from{opacity:0;transform:translate3d(0,8px,0)}
    to{opacity:1;transform:translate3d(0,0,0)}
  }
  #eva-tanem-v13 .tn22-cta,
  #eva-tanem-v13 .tn22-worklink,
  #eva-tanem-v13 .tn31-service-more,
  #eva-tanem-v13 .tn22-port-all{
    transition:transform .16s ease,opacity .16s ease,background-color .2s ease,border-color .2s ease!important;
  }
  #eva-tanem-v13 .tn22-cta:active,
  #eva-tanem-v13 .tn22-worklink:active,
  #eva-tanem-v13 .tn31-service-more:active,
  #eva-tanem-v13 .tn22-port-all:active{
    transform:scale(.985);
  }
}
`;
document.head.appendChild(style);

const heroSelectors=['.tn22-title','.tn22-sub','.tn22-copy','.tn37-hero-info','.tn22-cta','.tn22-worklink'];
heroSelectors.forEach((sel,i)=>{
  const el=root.querySelector(sel);
  if(!el)return;
  el.classList.add('eva-hero-motion');
  el.style.transitionDelay=(60+i*55)+'ms';
});
root.classList.add('eva-motion-ready');
requestAnimationFrame(()=>requestAnimationFrame(()=>root.classList.add('eva-motion-start')));

const revealObserver=new IntersectionObserver(entries=>{
  entries.forEach(entry=>{
    if(!entry.isIntersecting)return;
    entry.target.classList.add('eva-inview');
    revealObserver.unobserve(entry.target);
  });
},{threshold:.1,rootMargin:'0px 0px -8% 0px'});

function observe(el){
  if(!el||el.classList.contains('eva-reveal-motion'))return;
  el.classList.add('eva-reveal-motion');
  revealObserver.observe(el);
}

[
  '#tn13Portfolio .tn22-kicker','#tn13Portfolio h2','#tn13Portfolio .tn22-port-all',
  '#tn13Services .tn22-kicker','#tn13Services h2','#tn13Services .tn31-cats-wrap',
  '#tn38About .tn42-kicker','#tn38About .tn42-card',
  '#tn13Team .tn22-kicker','#tn13Team h2','#tn13Team .tn22-team-grid'
].forEach(sel=>observe(root.querySelector(sel)));

const portfolioItems=Array.from(root.querySelectorAll('#tn13Portfolio .tn22-photo'));
portfolioItems.forEach((el,i)=>{
  el.classList.add('eva-item-motion');
  el.style.setProperty('--eva-delay',(i*55)+'ms');
  revealObserver.observe(el);
});

function animateServiceRows(){
  const rows=Array.from(root.querySelectorAll('#tn13Services .tn31-service-row'));
  rows.forEach((row,i)=>{
    row.classList.remove('eva-service-enter');
    row.style.setProperty('--eva-delay',(Math.min(i,7)*34)+'ms');
  });
  requestAnimationFrame(()=>rows.forEach(row=>row.classList.add('eva-service-enter')));
}

const serviceList=root.querySelector('#tn13Services .tn31-service-list');
if(serviceList){
  animateServiceRows();
  const mo=new MutationObserver(()=>animateServiceRows());
  mo.observe(serviceList,{childList:true});
}

function animateServiceHeight(trigger){
  if(!serviceList)return;
  const from=serviceList.getBoundingClientRect().height;
  requestAnimationFrame(()=>{
    const to=serviceList.getBoundingClientRect().height;
    if(Math.abs(to-from)<2)return;
    serviceList.animate(
      [{height:from+'px',overflow:'hidden'},{height:to+'px',overflow:'hidden'}],
      {duration:320,easing:'cubic-bezier(.22,.72,.28,1)'}
    );
  });
}

const services=root.querySelector('#tn13Services');
if(services){
  services.addEventListener('click',e=>{
    const trigger=e.target.closest('.tn31-service-more,[data-scat]');
    if(trigger)animateServiceHeight(trigger);
  },true);
}
})();
