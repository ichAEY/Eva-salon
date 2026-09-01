from pathlib import Path
import re

js_path=Path('mobile-stluxe-current.js')
s=js_path.read_text(encoding='utf-8')

# Build gallery strictly from user-uploaded, pre-categorised files.
root=Path('.')
files=[p for p in root.glob('*.webp') if p.is_file()]

def natural_key(name):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)', name)]

def collect(prefix):
    return sorted([p.name for p in files if p.name.lower().startswith(prefix)], key=natural_key)

salon=collect('salon')
hair=collect('hair')
nails=collect('nails')
brows=collect('brows')
lashes=collect('lashes')
lips=collect('lips')
team=collect('team')

if not salon:
    raise SystemExit('No salon*.webp files found')

# Hero: interior + representative work.
hero_main=salon[0]
hero_small=(nails[0] if nails else (hair[0] if hair else salon[min(1,len(salon)-1)]))
s=s.replace('assets/images/salon-reception.webp', hero_main)
s=s.replace('assets/images/nails-pink.webp', hero_small)
s=s.replace('Мытищи · Победы, 16','Мытищи · Академика Каргина, 25')
s=s.replace('на улице Победы.','на улице Академика Каргина.')

# Portfolio order: visual variety first, then complete gallery by categories.
ordered=[]
def add_group(group, cat, alt):
    for f in group:
        ordered.append((f,cat,alt))

# First seven intentionally mixed for the portfolio preview.
preview=[]
for candidate in [
    (salon[0] if salon else None,'salon','Интерьер EVA'),
    (nails[0] if nails else None,'nails','Работа мастера ногтевого сервиса EVA'),
    (hair[0] if hair else None,'hair','Работа мастера по волосам EVA'),
    (brows[0] if brows else None,'brows','Работа brow-мастера EVA'),
    (lashes[0] if lashes else None,'lashes','Работа lash-мастера EVA'),
    (lips[0] if lips else None,'other','Перманентный макияж EVA'),
    (salon[1] if len(salon)>1 else (hair[1] if len(hair)>1 else None),'salon','Пространство EVA')
]:
    if candidate[0] and candidate[0] not in [x[0] for x in preview]: preview.append(candidate)

seen={x[0] for x in preview}
ordered.extend(preview)
for group,cat,alt in [
    (salon,'salon','Интерьер EVA'),
    (nails,'nails','Маникюр EVA'),
    (hair,'hair','Работа с волосами EVA'),
    (brows,'brows','Брови EVA'),
    (lashes,'lashes','Ресницы EVA'),
    (lips,'other','Перманентный макияж EVA')
]:
    for f in group:
        if f not in seen:
            ordered.append((f,cat,alt)); seen.add(f)

works='const works=[\n'+',\n'.join("    {src:%r,cat:%r,alt:%r}"%(f,c,a) for f,c,a in ordered)+'\n  ];'
s=re.sub(r"const works=\[.*?\n  \];",works,s,count=1,flags=re.S)

# Expand gallery category chips to match uploaded media.
gtabs="const galleryTabs=[['all','Все'],['salon','Салон'],['nails','Ногти'],['hair','Волосы'],['brows','Брови'],['lashes','Ресницы'],['other','Перманент']];"
s=re.sub(r"const galleryTabs=\[[^;]+;",gtabs,s,count=1)
s=s.replace('Салон · ногти · волосы','Салон · ногти · волосы · брови · ресницы')

# Portfolio must show exactly seven images before the all-works button.
s=s.replace("works.slice(0,2)","works.slice(0,3)")
s=s.replace("works.slice(2,5)","works.slice(3,7)")
s=s.replace('Открыть всю галерею','Смотреть все работы')

# Team photo: use the uploaded team image without inventing identities.
if team:
    team_block='''<div class="tn13-team-photo" data-gallery="salon"><img src="%s" alt="Команда EVA"></div>\n        ''' % team[0]
    marker='<div class="tn13-team-grid">${masters.map(m=>`<button class="tn13-master"'
    if 'tn13-team-photo' not in s and marker in s:
        s=s.replace(marker,team_block+marker,1)
    # CSS for the real team photo.
    css_marker='.tn13-team-grid{'
    if '.tn13-team-photo{' not in s and css_marker in s:
        s=s.replace(css_marker,'.tn13-team-photo{margin:0 0 18px;border-radius:24px;overflow:hidden;aspect-ratio:1.45/1;background:#ddd}.tn13-team-photo img{width:100%;height:100%;object-fit:cover;display:block}\n    '+css_marker,1)

# Use another salon image in the about/visual layer wherever copied STLuxe image may remain.
s=s.replace('assets/images/stluxe-about-dark.svg', salon[min(1,len(salon)-1)])

js_path.write_text(s,encoding='utf-8')

# Desktop fallback: replace old/copy imagery with user-uploaded EVA media.
idx=Path('index.html')
h=idx.read_text(encoding='utf-8')
# Prefer actual salon images for hero/gallery placeholders.
replacement_cycle=(salon + nails[:3] + hair[:3] + brows[:1] + lashes[:1] + lips[:1])
if replacement_cycle:
    i=0
    def repl(m):
        nonlocal_i = None
        return m.group(0)
    # Explicit known obsolete references first.
    h=h.replace('assets/eva-gallery/eva-01.jpg', salon[0])
idx.write_text(h,encoding='utf-8')

print('Applied uploaded media:',len(ordered),'gallery photos; hero=',hero_main,hero_small,'team=',team[0] if team else 'none')
