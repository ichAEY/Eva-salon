from pathlib import Path
import re

p=Path('mobile-stluxe-current.js')
s=p.read_text(encoding='utf-8')
files=[x.name for x in Path('.').glob('*.webp') if x.is_file()]

def key(v):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)',v)]
def group(prefix):
    return sorted([x for x in files if x.lower().startswith(prefix)],key=key)
def lead(exact, arr):
    return exact if exact in arr else (arr[0] if arr else None)

salon=group('salon'); nails=group('nails'); hair=group('hair'); brows=group('brows'); lashes=group('lashes'); lips=group('lips'); team=group('team')
if not salon: raise SystemExit('No salon media')
main_salon=lead('salon.webp',salon)
main_nails=lead('nails.webp',nails) or lead('hair.webp',hair) or main_salon
main_hair=lead('hair.webp',hair)

s=re.sub(r'(<button class="tn13-visual-main"[^>]*><img src=")[^"]+',r'\1'+main_salon,s,count=1)
s=re.sub(r'(<button class="tn13-visual-small"[^>]*><img src=")[^"]+',r'\1'+main_nails,s,count=1)
s=s.replace('Мытищи · Победы, 16','Мытищи · Академика Каргина, 25')
s=s.replace('на улице Победы.','на улице Академика Каргина.')
s=s.replace('рейтинг 4,9','рейтинг 5,0')

preview=[]
def add_preview(f,cat,alt):
    if f and f not in [x[0] for x in preview]: preview.append((f,cat,alt))
add_preview(main_salon,'salon','Интерьер EVA')
add_preview(main_nails,'nails','Маникюр EVA')
add_preview(main_hair,'hair','Работа с волосами EVA')
add_preview(brows[0] if brows else None,'brows','Брови EVA')
add_preview(lashes[0] if lashes else None,'lashes','Ресницы EVA')
add_preview(lips[0] if lips else None,'other','Перманентный макияж EVA')
add_preview(next((x for x in salon if x!=main_salon),None),'salon','Пространство EVA')

ordered=list(preview); seen={x[0] for x in preview}
for arr,cat,alt in [(salon,'salon','Интерьер EVA'),(nails,'nails','Маникюр EVA'),(hair,'hair','Работа с волосами EVA'),(brows,'brows','Брови EVA'),(lashes,'lashes','Ресницы EVA'),(lips,'other','Перманентный макияж EVA')]:
    for f in arr:
        if f not in seen: ordered.append((f,cat,alt)); seen.add(f)
works='const works=[\n'+',\n'.join("    {src:%r,cat:%r,alt:%r}"%x for x in ordered)+'\n  ];'
s=re.sub(r'const works=\[.*?\n  \];',works,s,count=1,flags=re.S)

s=re.sub(r"const galleryTabs=\[[^;]+;","const galleryTabs=[['all','Все'],['salon','Салон'],['nails','Ногти'],['hair','Волосы'],['brows','Брови'],['lashes','Ресницы'],['other','Перманент']];",s,count=1)
s=re.sub(r'<div class="tn13-gallery-sub">.*?</div>','<div class="tn13-gallery-sub">Салон · ногти · волосы · брови · ресницы · перманент</div>',s,count=1)
s=re.sub(r'(<div class="tn13-feature">\$\{)works\.slice\([^)]*\)',r'\1works.slice(0,3)',s,count=1)
s=re.sub(r'(<div class="tn13-work-grid">\$\{)works\.slice\([^)]*\)',r'\1works.slice(3,7)',s,count=1)
s=s.replace('Открыть всю галерею','Смотреть все работы')

if team:
    if 'class="tn13-team-photo"' not in s:
        marker='<div class="tn13-team-grid">${masters.map(m=>`<button class="tn13-master"'
        s=s.replace(marker,f'<div class="tn13-team-photo"><img src="{team[0]}" alt="Команда EVA"></div>\n        '+marker,1)
    else:
        s=re.sub(r'(<div class="tn13-team-photo"[^>]*><img src=")[^"]+',r'\1'+team[0],s,count=1)
    if '.tn13-team-photo{' not in s:
        s=s.replace('.tn13-team-grid{','.tn13-team-photo{margin:0 0 18px;border-radius:24px;overflow:hidden;aspect-ratio:1.45/1;background:#ddd}.tn13-team-photo img{width:100%;height:100%;object-fit:cover;display:block}\n    .tn13-team-grid{',1)

s=s.replace('EVA находится в Ивантеевке на улице Победы, 16. Понедельник — выходной, со вторника по воскресенье салон работает с 10:00 до 20:00.','EVA находится в Мытищах на улице Академика Каргина, 25.')
s=s.replace('https://yandex.ru/map-widget/v1/?text=%D0%98%D0%B2%D0%B0%D0%BD%D1%82%D0%B5%D0%B5%D0%B2%D0%BA%D0%B0%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%9F%D0%BE%D0%B1%D0%B5%D0%B4%D1%8B%2C%2016&z=16','https://yandex.ru/map-widget/v1/?text=%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D0%BA%D0%B0%20%D0%9A%D0%B0%D1%80%D0%B3%D0%B8%D0%BD%D0%B0%2C%2025&z=16')
s=s.replace('<strong>4,9</strong><small>рейтинг</small>','<strong>${RATING}</strong><small>рейтинг</small>')
s=s.replace('<strong>17</strong><small>услуг</small>','<strong>${services.length}</strong><small>услуг</small>')
s=s.replace('Позвонить +7 916 355-22-22','Позвонить +7 (968) 427-01-01')
p.write_text(s,encoding='utf-8')

idx=Path('index.html'); h=idx.read_text(encoding='utf-8'); h=h.replace('assets/eva-gallery/eva-01.jpg',main_salon); idx.write_text(h,encoding='utf-8')
print('Applied',len(ordered),'uploaded EVA photos; hero',main_salon,main_nails,'team',team[0] if team else '-')
