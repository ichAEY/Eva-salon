from pathlib import Path
import re

p=Path('mobile-eva-current.js')
s=p.read_text(encoding='utf-8')

# Normalize every known Mytishchi address form before the guarded main correction.
s=s.replace('<strong>Мытищи,</strong>ул. Академика Каргина, 25','<strong>Балашиха,</strong>д. Павлино, 69')
s=s.replace('Мытищи, ул. Академика Каргина, 25','Балашиха, д. Павлино, 69')
s=s.replace('Мытищи, улица Академика Каргина, 25','Балашиха, д. Павлино, 69')
s=s.replace('ул. Академика Каргина, 25','д. Павлино, 69')
s=s.replace('улица Академика Каргина, 25','д. Павлино, 69')
s=re.sub(r'(?:ул\.?|улица)\s*Академика Каргина\s*,?\s*25','д. Павлино, 69',s)
s=s.replace('Академика Каргина, 25','Павлино, 69')

if 'Академика Каргина' in s or 'Каргина' in s:
    raise SystemExit('unhandled Akademika Kargina fragment remains before main correction')

p.write_text(s,encoding='utf-8')
print('all hidden Mytishchi address fragments normalized')
