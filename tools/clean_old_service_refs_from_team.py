from pathlib import Path
import re

# Remove stale service references from the old/wrong EVA while preserving the team block design.

p=Path('index.html')
s=p.read_text(encoding='utf-8')
team='''    <section id="team">
      <div class="section-head"><div><h2>Специалисты</h2><p>Направления команды EVA</p></div></div>
      <div class="specialists">
        <button class="specialist" onclick="openRole('Мастер по волосам','Стрижка женская|Стрижка модельная мужская|Окрашивание волос в один тон|Укладка')"><span class="avatar-placeholder">E</span><strong>Мастер по волосам</strong><span>Волосы</span></button>
        <button class="specialist" onclick="openRole('Мастер бровей и ресниц','Архитектура бровей|Ламинирование бровей/ Ламинирование ресниц')"><span class="avatar-placeholder">E</span><strong>Мастер бровей и ресниц</strong><span>Брови · ресницы</span></button>
        <button class="specialist" onclick="openRole('Мастер маникюра','Маникюр аппаратный/комбинированный/классический|Маникюр с покрытием гель-лак/гель/укрепление')"><span class="avatar-placeholder">E</span><strong>Мастер маникюра</strong><span>Маникюр</span></button>
      </div>
    </section>'''
s,n=re.subn(r'    <section id="team">.*?    </section>',team,s,count=1,flags=re.S)
assert n==1
p.write_text(s,encoding='utf-8')

p=Path('mobile-eva-current.js')
s=p.read_text(encoding='utf-8')
masters1="""const masters=[
    {id:'hair',name:'Мастер',category:'Волосы',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['hair']},
    {id:'look',name:'Мастер',category:'Брови · ресницы',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['browslashes']},
    {id:'nails',name:'Мастер',category:'Маникюр',initial:'E',about:'Персональные данные специалиста уточняются у салона.',cats:['nails']}
  ];"""
s,n=re.subn(r'const masters=\[.*?\n  \];',lambda _:masters1,s,count=1,flags=re.S)
assert n==1
masters2="""const MASTERS=[
{id:'hair',name:'Мастер',role:'Волосы',about:'Персональные данные специалиста уточняются у салона.',cats:['Волосы'],work:['hair00001.webp','hair00002.webp','hair00003.webp'],reviewNames:[]},
{id:'look',name:'Мастер',role:'Брови · ресницы',about:'Персональные данные специалиста уточняются у салона.',cats:['Брови и ресницы'],work:['brows00001.webp','lashes00001.webp'],reviewNames:[]},
{id:'nails',name:'Мастер',role:'Маникюр',about:'Персональные данные специалиста уточняются у салона.',cats:['Маникюр'],work:['nails00001.webp','nails00002.webp','nails00003.webp'],reviewNames:[]}
];"""
s,n=re.subn(r'const MASTERS=\[.*?\n\];',lambda _:masters2,s,count=1,flags=re.S)
assert n==1
p.write_text(s,encoding='utf-8')

# Audit only team/master configuration, not authentic review text.
idx=Path('index.html').read_text(encoding='utf-8')
team_block=re.search(r'<section id="team">.*?</section>',idx,re.S).group(0)
for stale in ['Педикюр','Чистка лица','Пилинг','Инъекционные процедуры','Коррекция фигуры','Коррекция бровей','Услуги для ресниц']:
    assert stale not in team_block, stale
assert team_block.count('class="specialist"')==3
mob=Path('mobile-eva-current.js').read_text(encoding='utf-8')
assert "cats:['Брови и ресницы']" in mob
assert "cats:['Маникюр']" in mob
assert "cats:['Волосы']" in mob
print('OK: stale wrong-service references removed from team UI')
