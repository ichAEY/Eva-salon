from pathlib import Path
import re, json, html

mobile_path=Path('mobile-eva-current.js')
index_path=Path('index.html')
mobile=mobile_path.read_text(encoding='utf-8')
index=index_path.read_text(encoding='utf-8')

block=re.search(r'const REAL_REVIEW_DATA=\[(.*?)\];', mobile, flags=re.S)
if not block:
    raise SystemExit('REAL_REVIEW_DATA not found')

# Parse every generated JSON string pair independently. This is robust even when review text contains newlines or emoji.
pairs=re.findall(r'\[("(?:\\.|[^"\\])*")\s*,\s*("(?:\\.|[^"\\])*")\]', block.group(1), flags=re.S)
reviews=[[json.loads(name),json.loads(text)] for name,text in pairs]
if len(reviews)!=15:
    raise SystemExit(f'Expected 15 reviews, parsed {len(reviews)}')
if len({r[1] for r in reviews})!=15:
    raise SystemExit('Review texts are not unique')

def card(r):
    name,text=r
    return (
      '<a class="review-card eva-review-card" href="https://yandex.ru/maps/org/eva/200326329284/reviews/" target="_blank" rel="noopener">'
      f'<div class="review-top"><span class="review-name">{html.escape(name)}</span><span class="review-stars" aria-label="5 из 5">★★★★★</span></div>'
      f'<p class="review-text">{html.escape(text)}</p></a>'
    )

rows=[]
for i in range(0,15,3):
    rows.append('<div class="eva-review-row">'+''.join(card(r) for r in reviews[i:i+3])+'</div>')

section='''<section id="reviews">
      <div class="section-head"><div><h2>Отзывы</h2><p>Оригинальные отзывы клиентов EVA из Яндекс Карт</p></div><a class="section-link" href="https://yandex.ru/maps/org/eva/200326329284/reviews/" target="_blank" rel="noopener">Все отзывы ↗</a></div>
      <div class="reviews-summary"><div><div class="score">4,8</div><div class="score-label">рейтинг EVA</div></div><div style="text-align:right"><div style="color:var(--violet);font-size:16px;letter-spacing:2px">★★★★★</div><div class="score-label">15 отзывов с оценкой 5★</div></div></div>
      '''+''.join(rows)+'''
    </section>'''

index,n=re.subn(r'<section id="reviews">.*?</section>', lambda _m: section, index, count=1, flags=re.S)
if n!=1:
    raise SystemExit('Desktop reviews section not replaced')

css='''
    .eva-review-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px;align-items:stretch}
    .eva-review-card{display:block;margin-top:0;min-width:0}
    .eva-review-card .review-text{display:-webkit-box;-webkit-line-clamp:7;-webkit-box-orient:vertical;overflow:hidden}
'''
if '.eva-review-row{' not in index:
    index=index.replace('</style>',css+'  </style>',1)

if index.count('class="review-card eva-review-card"') != 15:
    raise SystemExit('Desktop does not contain exactly 15 review cards')

index_path.write_text(index,encoding='utf-8')
print('Desktop fallback synced to 15 original Yandex reviews, 5 rows x 3')
