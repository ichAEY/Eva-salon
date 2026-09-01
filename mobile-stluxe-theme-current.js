(function(){
'use strict';
if(!window.matchMedia||!window.matchMedia('(max-width:767px)').matches)return;

const style=document.createElement('style');
style.id='stluxe-theme-current';
style.textContent=`
@media(max-width:767px){
:root{
  --stl-white:#fafafa;
  --stl-white-soft:#f7f7f8;
  --stl-violet:#9b657d;
  --stl-violet-deep:#7b4b61;
  --stl-ink:#1b191d;
  --stl-yellow:#d9aa42;
  --stl-dark:#242127;
  --stl-dark-2:#2d2931;
  --stl-dark-3:#37313b;
  --stl-dark-text:#f7f3f8;
  --stl-dark-muted:#b9b2bd;
  --stl-dark-line:rgba(255,255,255,.11);
  --stl-dark-violet:#6f3d82;
  --stl-dark-violet-bright:#8d55a5;
}

html,body{background:var(--stl-white)!important}
#stluxe-tanem-v13{background:var(--stl-white)!important;color:var(--stl-ink)!important}

/* Hero + portfolio */
#stluxe-tanem-v13 .tn13-hero{
  background:
    radial-gradient(390px 250px at 112% 11%,rgba(145,78,184,.12),transparent 70%),
    radial-gradient(260px 190px at -12% 78%,rgba(161,101,197,.055),transparent 72%),
    linear-gradient(180deg,#fbfafb 0%,#fafafa 91%,#fafafa 100%)!important;
}
.tn22-top{
  background:
    radial-gradient(280px 160px at 108% -18%,rgba(147,80,185,.12),transparent 72%),
    #fbfafb!important;
}
.tn22-media:after{background:linear-gradient(180deg,rgba(250,250,250,0),#fafafa 96%)!important}
.tn22-card{
  background:
    radial-gradient(250px 170px at 112% 4%,rgba(151,84,190,.06),transparent 72%),
    linear-gradient(180deg,rgba(252,251,252,.985) 0%,rgba(252,251,252,.985) 81%,#fafafa 100%)!important;
}
.tn22-card:after{background:linear-gradient(180deg,rgba(250,250,250,0),rgba(250,250,250,.5) 48%,#fafafa 92%)!important}
#tn13Portfolio{
  background:
    radial-gradient(330px 230px at -14% 28%,rgba(150,82,190,.07),transparent 71%),
    #fafafa!important;
}

/* Shared interface accents */
.tn22-cta,#tn13Sticky button{background:var(--stl-violet-deep)!important;border-color:var(--stl-violet-deep)!important;color:#fff!important}
.tn23-section-nav{background:rgba(250,250,250,.96)!important;border-bottom-color:rgba(75,40,91,.09)!important}
.tn23-section-nav button.active:after{background:var(--stl-violet)!important}
.tn22-worklink{border-color:rgba(83,48,98,.18)!important;background:rgba(255,255,255,.4)!important}
#tn13Sticky{background:rgba(250,250,250,.96)!important;border-color:rgba(72,47,82,.10)!important}

/* Services */
#tn13Services{
  background:
    radial-gradient(420px 310px at 108% 8%,rgba(143,85,181,.19),transparent 67%),
    radial-gradient(300px 230px at -14% 88%,rgba(111,61,130,.10),transparent 72%),
    var(--stl-dark)!important;
  color:var(--stl-dark-text)!important;
  border-top-color:rgba(255,255,255,.055)!important;
  border-bottom-color:rgba(255,255,255,.055)!important;
}
#tn13Services .tn22-kicker{color:#aaa2ad!important}
#tn13Services .tn31-services h2,
#tn13Services .tn31-service-name,
#tn13Services .tn31-service-price{color:var(--stl-dark-text)!important}
#tn13Services .tn31-service-detail{color:var(--stl-dark-muted)!important}
#tn13Services .tn31-service-list,
#tn13Services .tn31-service-row{border-color:rgba(255,255,255,.10)!important}
#tn13Services .tn31-cat{background:rgba(255,255,255,.035)!important;border-color:rgba(255,255,255,.12)!important;color:#c9c1cc!important}
#tn13Services .tn31-cat.active{background:var(--stl-dark-violet)!important;border-color:var(--stl-dark-violet)!important;color:#fff!important}
#tn13Services .tn31-service-book{color:#c28fd1!important}
#tn13Services .tn31-service-more{background:rgba(255,255,255,.045)!important;border-color:rgba(255,255,255,.13)!important;color:#eee8f0!important}
#tn13Services .tn31-service-more span:last-child{color:#bfb6c2!important}

/* About */
#tn38About{
  background:
    radial-gradient(430px 310px at 108% 18%,rgba(150,79,190,.155),transparent 67%),
    radial-gradient(300px 220px at -16% 84%,rgba(157,91,194,.06),transparent 73%),
    var(--stl-white-soft)!important;
}
#tn38About .tn42-kicker{color:#6f6971!important}
#tn38About .tn42-card{background:#ebe9ed!important;border-color:rgba(67,56,71,.10)!important;box-shadow:0 14px 34px rgba(43,35,47,.08)!important}
#tn38About .tn42-photo{background:#342338!important}
#tn38About .tn42-photo:after{content:'';position:absolute;inset:0;pointer-events:none;background:radial-gradient(280px 190px at 88% 12%,rgba(189,121,222,.18),transparent 70%)}
#tn38About .tn42-photo img{filter:brightness(1.17) saturate(1.08) contrast(.98)!important}
#tn38About .tn42-body{
  background:
    radial-gradient(250px 180px at 108% 0%,rgba(143,85,181,.055),transparent 72%),
    #ebe9ed!important;
}
#tn38About .tn42-lead{color:#211e23!important}
#tn38About .tn42-copy{color:#5c565f!important}
#tn38About .tn42-facts{border-top-color:rgba(60,52,64,.08)!important}
#tn38About .tn42-fact{background:#dfdce2!important;border-color:rgba(75,58,81,.09)!important;color:#2c282e!important;box-shadow:none!important}
#tn38About .tn42-fact b{color:var(--stl-dark-violet)!important}
#tn38About .tn42-fact span{color:#2c282e!important}
#tn38About .tn42-rating{background:rgba(62,35,72,.74)!important;border-color:rgba(255,255,255,.25)!important}
#tn38About .tn42-rating-star{color:#f0c45d!important}

/* Team */
#tn13Team{
  background:
    radial-gradient(420px 310px at 108% 8%,rgba(143,85,181,.19),transparent 67%),
    radial-gradient(300px 230px at -14% 88%,rgba(111,61,130,.10),transparent 72%),
    var(--stl-dark)!important;
  color:var(--stl-dark-text)!important;
  border-top-color:rgba(255,255,255,.055)!important;
  border-bottom-color:rgba(255,255,255,.055)!important;
}
#tn13Team .tn22-kicker,#tn13Team .tn42-team-hint{color:#aaa2ad!important}
#tn13Team .tn22-team h2,#tn13Team .tn22-master-name{color:var(--stl-dark-text)!important}
#tn13Team .tn22-master-role{color:var(--stl-dark-muted)!important}
#tn13Team .tn22-master-circle{
  background:radial-gradient(circle at 42% 30%,rgba(255,255,255,.07),transparent 45%),linear-gradient(145deg,#3c3641,#302b34)!important;
  color:#cbbfd0!important;border:1px solid rgba(255,255,255,.085)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.035)!important;
}
#tn13Team .tn22-master-circle svg{opacity:.92!important}

/* Reviews */
#tn13Reviews{
  background:
    radial-gradient(390px 270px at 111% 8%,rgba(150,80,190,.12),transparent 69%),
    radial-gradient(270px 210px at -14% 84%,rgba(166,102,200,.05),transparent 73%),
    #fafafa!important;
  border-top:1px solid rgba(31,28,34,.055)!important;
  border-bottom:1px solid rgba(31,28,34,.055)!important;
}
.tn30-reviews .tn22-kicker{color:#6f6a71!important}
.tn30-stars{color:var(--stl-yellow)!important}
.tn30-review-card{background:rgba(245,244,247,.88)!important;border-color:rgba(69,61,73,.105)!important}
.tn30-review-avatar{background:#e4e2e7!important;color:#504a52!important}
.tn30-review-meta{color:#88828a!important}
.tn30-review-all{background:#f1f0f3!important;border-color:rgba(67,58,71,.14)!important}

/* Contacts */
#tn13Visit{
  background:
    radial-gradient(420px 310px at 108% 8%,rgba(143,85,181,.19),transparent 67%),
    radial-gradient(300px 230px at -14% 88%,rgba(111,61,130,.10),transparent 72%),
    var(--stl-dark)!important;
  color:var(--stl-dark-text)!important;
  border-radius:0!important;
  border-top-color:rgba(255,255,255,.055)!important;
  border-bottom-color:rgba(255,255,255,.055)!important;
}
#tn13Visit .tn22-kicker{color:#aaa2ad!important}
#tn13Visit h2,#tn13Visit .tn22-contact strong,#tn13Visit .tn22-visit-head{color:var(--stl-dark-text)!important}
#tn13Visit .tn22-contact{background:rgba(255,255,255,.045)!important;border-color:rgba(255,255,255,.11)!important;color:var(--stl-dark-text)!important}
#tn13Visit .tn22-contact span{color:var(--stl-dark-muted)!important}
#tn13Visit .tn22-contact svg{stroke:#c69bd2!important}
#tn13Visit .tn22-call{background:rgba(255,255,255,.035)!important;border-color:rgba(255,255,255,.13)!important;color:#f1ebf3!important}
#tn13Visit .tn22-route{background:var(--stl-dark-violet)!important;border-color:var(--stl-dark-violet)!important;color:#fff!important}
#tn13Visit .tn22-mapwrap{background:#302b34!important}
#tn13Visit .tn22-map-skeleton{background:linear-gradient(110deg,#302b34 10%,#3a343e 35%,#302b34 60%)!important;background-size:220% 100%!important;color:var(--stl-dark-muted)!important}
#tn13Visit .tn22-status{border-color:rgba(255,255,255,.14)!important}
#tn13Visit .tn22-status.open{background:#2e4133!important;border-color:#4d6752!important;color:#a9d5b0!important}
#tn13Visit .tn22-status.closed{background:#493336!important;border-color:#65474b!important;color:#d59a9f!important}
#tn13Visit .tn22-footer{background:#1d1a20!important}

/* Live hero status */
.tn50-hero-status-sub{display:block}
.tn50-hero-status.open .tn50-hero-status-main{color:#3f8750!important}
.tn50-hero-status.closed .tn50-hero-status-main{color:#a45e64!important}

/* Master profile */
.tn22-master-page{
  background:
    radial-gradient(430px 310px at 106% 0%,rgba(143,85,181,.18),transparent 68%),
    radial-gradient(300px 220px at -14% 80%,rgba(111,61,130,.08),transparent 72%),
    var(--stl-dark)!important;
  color:var(--stl-dark-text)!important;
}
.tn22-master-page .tn22-back,.tn22-master-page .tn22-master-brand{color:var(--stl-dark-text)!important}
.tn22-master-page .tn22-profile-circle{
  background:radial-gradient(circle at 42% 31%,rgba(255,255,255,.075),transparent 43%),linear-gradient(145deg,#3d3742,#2f2a33)!important;
  color:#cbbfd0!important;border:1px solid rgba(255,255,255,.085)!important;box-shadow:0 14px 34px rgba(0,0,0,.16)!important;
}
.tn22-master-page .tn22-profile h1{color:var(--stl-dark-text)!important}
.tn22-master-page .tn22-profile-role{color:var(--stl-dark-muted)!important}
.tn22-master-page .tn22-salon-rating{color:#d8d1da!important}
.tn22-master-page .tn22-salon-rating b{color:#e0ad43!important}
.tn22-master-page .tn22-master-tabs{gap:7px!important}
.tn22-master-page .tn22-master-tabs button{background:rgba(255,255,255,.035)!important;border-color:var(--stl-dark-line)!important;color:#c6bec9!important}
.tn22-master-page .tn22-master-tabs button.active{background:var(--stl-dark-violet)!important;border-color:var(--stl-dark-violet)!important;color:#fff!important}
.tn22-master-page .tn22-master-content h3{color:var(--stl-dark-text)!important}
.tn22-master-page .tn22-master-about{color:#d0c9d2!important}
.tn22-master-page .tn22-master-service{border-bottom-color:rgba(255,255,255,.09)!important}
.tn22-master-page .tn22-master-service b{color:#f0ebf2!important}
.tn22-master-page .tn22-master-service span{color:#d9d0dc!important}
.tn22-master-page .tn22-master-review{background:#302b34!important;border-color:rgba(255,255,255,.09)!important}
.tn22-master-page .tn22-master-review strong{color:var(--stl-dark-text)!important}
.tn22-master-page .tn22-master-review p{color:#c9c1cc!important}
.tn22-master-page .tn22-master-book{background:linear-gradient(180deg,var(--stl-dark-violet-bright),var(--stl-dark-violet))!important;color:#fff!important;box-shadow:0 14px 36px rgba(73,37,88,.34)!important}

/* Full gallery */
#tn13Gallery{
  background:
    radial-gradient(430px 300px at 108% 2%,rgba(143,85,181,.17),transparent 68%),
    radial-gradient(320px 230px at -12% 92%,rgba(111,61,130,.08),transparent 72%),
    var(--stl-dark)!important;
  color:var(--stl-dark-text)!important;
}
#tn13Gallery .tn22-gallery-back,#tn13Gallery .tn22-gallery-title strong{color:var(--stl-dark-text)!important}
#tn13Gallery .tn22-gallery-title span,#tn13Gallery .tn23-gallery-empty{color:var(--stl-dark-muted)!important}
#tn13Gallery .tn22-gallery-tabs{border-color:rgba(255,255,255,.11)!important;background:rgba(255,255,255,.025)!important}
#tn13Gallery .tn22-gallery-tab{color:#c6bec9!important;background:transparent!important}
#tn13Gallery .tn22-gallery-tab.active{background:var(--stl-dark-violet)!important;color:#fff!important}
#tn13Gallery .tn22-gallery-tile{background:#302b34!important;box-shadow:0 8px 22px rgba(0,0,0,.12)!important}
}
`;

document.head.appendChild(style);
const meta=document.querySelector('meta[name="theme-color"]');
if(meta)meta.setAttribute('content','#fafafa');
})();
