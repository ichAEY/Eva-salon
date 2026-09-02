from pathlib import Path
p=Path('mobile-eva-current.js')
s=p.read_text(encoding='utf-8')
old='<strong>Мытищи,</strong>ул. Академика Каргина, 25'
new='<strong>Балашиха,</strong>д. Павлино, 69'
if old not in s:
    raise SystemExit('expected old hero address fragment not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('hidden hero address fragment corrected')
