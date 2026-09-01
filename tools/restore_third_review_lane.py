from pathlib import Path
import re

p = Path('mobile-eva-current.js')
s = p.read_text(encoding='utf-8')

reviews = """const REAL_REVIEW_DATA=[
['Марина Ким','Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'],
['Екатерина Рэй','Была на окрашивании в один тон у Нарине. Помогла грамотно определиться с цветом, всё сделала аккуратно и быстро.'],
['Екатерина Рэй','Большая благодарность мастеру! Обязательно обращусь сюда же']
];"""

s, n = re.subn(r"const REAL_REVIEW_DATA=\[\n.*?\n\];", reviews, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('REAL_REVIEW_DATA not replaced')

lanes = "const reviewLanes=[[REAL_REVIEW_DATA[0],REAL_REVIEW_DATA[1],REAL_REVIEW_DATA[2]],[REAL_REVIEW_DATA[1],REAL_REVIEW_DATA[2],REAL_REVIEW_DATA[0]],[REAL_REVIEW_DATA[2],REAL_REVIEW_DATA[0],REAL_REVIEW_DATA[1]]];"
s, n = re.subn(r"const reviewLanes=.*?;\nreviews\.innerHTML=", lanes + "\nreviews.innerHTML=", s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('reviewLanes not replaced')

s, n = re.subn(r"const reviewGap=12,reviewDuration=780,reviewGroupCount=\d+;", "const reviewGap=12,reviewDuration=780,reviewGroupCount=3;", s, count=1)
if n != 1:
    raise SystemExit('reviewGroupCount not replaced')

if s.count('class="tn30-lane"') != 1:
    # Template contains the lane markup once inside map(); this is expected.
    pass
if 'REAL_REVIEW_DATA[2]' not in s:
    raise SystemExit('third review missing')
if 'reviewGroupCount=3' not in s:
    raise SystemExit('three-group loop missing')

p.write_text(s, encoding='utf-8')
print('Third EVA review lane restored')
