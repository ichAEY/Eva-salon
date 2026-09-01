from pathlib import Path
import re

mobile_path = Path('mobile-eva-current.js')
index_path = Path('index.html')
mobile = mobile_path.read_text(encoding='utf-8')
index = index_path.read_text(encoding='utf-8')

# Client-confirmed live rating. Keep every visible template occurrence consistent.
mobile = mobile.replace('5,0', '4,8')
index = index.replace('5,0', '4,8')

# Restore the early data layer with the same verbatim Yandex snippets used by the active review block.
early_reviews = """  const reviews=[
    {name:'Марина Ким',text:'Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'},
    {name:'Екатерина Рэй',text:'Большая благодарность мастеру! Обязательно обращусь сюда же'}
  ];"""
mobile, n = re.subn(r"  const reviews=\[\n.*?\n  \];", early_reviews, mobile, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not restore early review data')

# Final safety checks.
for forbidden in ['Клиент EVA ·', 'window.location.href', 'Записаться онлайн', 'Онлайн-запись', 'онлайн-запись']:
    if forbidden in mobile:
        raise SystemExit(f'Forbidden mobile residue: {forbidden}')
if '5,0' in mobile or '5,0' in index:
    raise SystemExit('Old 5,0 rating remains')
if '92 отзыва на Яндекс Картах' not in mobile:
    raise SystemExit('92 review count missing')
if "const sectionIds=['tn13Portfolio','tn13Services','tn38About','tn13Team','tn13Reviews','tn13Visit'];" not in mobile:
    raise SystemExit('About navigation order incorrect')
if '<button class="tn22-cta" type="button">' not in mobile or "hero.querySelector('.tn22-cta').addEventListener('click',book);" not in mobile:
    raise SystemExit('Hero booking button is not safe')

mobile_path.write_text(mobile, encoding='utf-8')
index_path.write_text(index, encoding='utf-8')
print('Final EVA polish OK')
