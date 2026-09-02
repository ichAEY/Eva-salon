from pathlib import Path
import re

p=Path('mobile-eva-current.js')
s=p.read_text(encoding='utf-8')

# Normalize every known Mytishchi address form in both legacy and refined mobile layers.
s=s.replace('<strong>Мытищи,</strong>ул. Академика Каргина, 25','<strong>Балашиха,</strong>д. Павлино, 69')
s=s.replace('Мытищи, ул. Академика Каргина, 25','Балашиха, д. Павлино, 69')
s=s.replace('Мытищи, улица Академика Каргина, 25','Балашиха, д. Павлино, 69')
s=s.replace('Мытищи · Академика Каргина, 25','Балашиха · д. Павлино, 69')
s=s.replace('Ногти, волосы, косметология и другие направления — в одном пространстве на улице Академика Каргина.','Ногти, волосы, косметология и другие направления — в одном пространстве в Павлино.')
s=s.replace('EVA находится в Мытищах на улице Академика Каргина, 25. Актуальный статус и расписание работы доступны в Яндекс Картах.','EVA находится в Павлино, Балашиха, по адресу д. Павлино, 69. Актуальный статус и расписание работы доступны в Яндекс Картах.')
s=s.replace('ул. Академика Каргина, 25','д. Павлино, 69')
s=s.replace('улица Академика Каргина, 25','д. Павлино, 69')
s=re.sub(r'(?:ул\.?|улица)\s*Академика Каргина\s*,?\s*25','д. Павлино, 69',s)
s=s.replace('Академика Каргина, 25','Павлино, 69')
s=s.replace('https://yandex.ru/map-widget/v1/?text=%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%90%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D0%BA%D0%B0%20%D0%9A%D0%B0%D1%80%D0%B3%D0%B8%D0%BD%D0%B0%2C%2025&z=16','https://yandex.ru/map-widget/v1/?ll=37.961358%2C55.729412&z=17')

if 'Академика Каргина' in s or 'Каргина' in s:
    i=s.find('Каргина')
    raise SystemExit('unhandled Kargina fragment remains: '+repr(s[max(0,i-120):i+160]))

p.write_text(s,encoding='utf-8')
print('all hidden Mytishchi address fragments normalized')
