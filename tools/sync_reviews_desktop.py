from pathlib import Path
import re, html

index_path=Path('index.html')
index=index_path.read_text(encoding='utf-8')

# These 15 reviews were fetched successfully from EVA's Yandex review endpoint in the previous build.
# Keep text exactly as received; do not rewrite or shorten.
reviews=[
('Александра Н.','Все отлично!! Благодарю) сама хожу в ваш салон на окрашивание, маникюр. И мужа регулярно на стрижку записываю. Все мастера настоящие профессионалы!'),
('natalia tatarinceva','Все отлично, мастер хороший,  внимательный. \nВсе на высшем уровне. \nРекомендую.  \nСейчас сложно найти салон, где сочетаются цена и качество.  Спасибо'),
('Арина Боданова','обожаю'),
('gugen','Хорошо стригут. Если сказать, что живёшь в этом доме (прописку не проверяют) - скидка 20%🔥'),
('Екатерина Рэй','Была на окрашивании в один тон  у Нарине, оказалось, что она  замечательный специалист, помогла мне грамотно определиться с цветом, всё сделала аккуратно и быстро, очень рада что нашла этот салон! Большая благодарность мастеру! Обязательно обращусь сюда же в следующий раз 🌹'),
('aaarinkooo','Сегодня ходила в этот салон на наращивание ногтей, я в восторге, очень аккуратно, красиво и быстро сделал мастер, буду ходить ещё!💅🏻🫶🏻'),
('Алина Жукова','Подстригался сын остались очень довольны 👍 спасибо придём обязательно еще 🌸'),
('Светлана Старчикова','Мне очень нравится этот салон! Все девушки очень приятные, записываться можно к любой - все сделают на высшем уровне!'),
('Екатерина','Маникюр сделали быстро, качественно,'),
('Aliya Uderbaeva','Хочу выразить огромную благодарность Наре!!!Мастер-золото!!!Попала благодаря отзывам,было немного волнения, но результат превзошел ожидания!!!!После первого посещения, осталась довольна и теперь только к ней!!!В салоне атмосфера -супер!!!В последний раз приходила с дочкой,мечтала о розовых локонах!!!Результат-ребенок счастлив!!!Всем рекомендую данный салон!!!Девочки-огонь!!!!!'),
('Оксана Вайнбергер','Была первый раз в салоне Эва, у мастера маникюра Татев. Очень хороший мастер, все аккуратно, красиво и быстро!!! Спасибо, мастеру!♥️'),
('Ю.В. Куликова','Мастер Елена просто чудо! Легкая рука, эпиляцию сделали мега быстро и безболезненно. С Еленой максимально комфортно взаимодействовать, интересный собеседник. Однозначно рекомендую за такой процедурой обращаться именно к Елене!'),
('Алина С.','Что касается салона в целом: удобное расположение, приятные цены, приветливый коллектив, всегда дружелюбная атмосфера. \n\nОтдельно хочу отметить мастера по маникюру Розу. Она замечательный профессионал своего дела и просто чуткий человек. Маникюр держится превосходно и ручки после нее выглядят потрясающе. Спасибо 🌹 \n\nХочу дополнить отзыв: была записана на окрашивание к Нарине, как вдруг во всем доме выключили свет, но мастер не растерялась и справилась блестяще со своей работой в таких экстремальных условиях. Тут работают настоящие профессионалы!'),
('Зарета К.','Мастер Евгения, лучшая в своём деле.Очень красиво подстригла, объяснила как делать укладку дома.'),
('Марина Ким','Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))')
]

if len(reviews)!=15 or len({text for _,text in reviews})!=15:
    raise SystemExit('Confirmed review list is invalid')

def card(item):
    name,text=item
    return (
      '<a class="review-card eva-review-card" href="https://yandex.ru/maps/org/eva/200326329284/reviews/" target="_blank" rel="noopener">'
      f'<div class="review-top"><span class="review-name">{html.escape(name)}</span><span class="review-stars" aria-label="5 из 5">★★★★★</span></div>'
      f'<p class="review-text">{html.escape(text)}</p></a>'
    )

rows=[]
for i in range(0,15,3):
    rows.append('<div class="eva-review-row">'+''.join(card(x) for x in reviews[i:i+3])+'</div>')

section='''<section id="reviews">
      <div class="section-head"><div><h2>Отзывы</h2><p>Оригинальные отзывы клиентов EVA из Яндекс Карт</p></div><a class="section-link" href="https://yandex.ru/maps/org/eva/200326329284/reviews/" target="_blank" rel="noopener">Все отзывы ↗</a></div>
      <div class="reviews-summary"><div><div class="score">4,8</div><div class="score-label">рейтинг EVA</div></div><div style="text-align:right"><div style="color:var(--violet);font-size:16px;letter-spacing:2px">★★★★★</div><div class="score-label">15 отзывов с оценкой 5★</div></div></div>
      '''+''.join(rows)+'''
    </section>'''

index,n=re.subn(r'<section id="reviews">.*?</section>',lambda _m:section,index,count=1,flags=re.S)
if n!=1:
    raise SystemExit('Desktop review section not found')

css='''
    .eva-review-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px;align-items:stretch}
    .eva-review-card{display:block;margin-top:0;min-width:0}
    .eva-review-card .review-text{display:-webkit-box;-webkit-line-clamp:7;-webkit-box-orient:vertical;overflow:hidden}
'''
if '.eva-review-row{' not in index:
    index=index.replace('</style>',css+'  </style>',1)

if index.count('class="review-card eva-review-card"')!=15:
    raise SystemExit('Desktop review card count is not 15')

index_path.write_text(index,encoding='utf-8')
print('Desktop reviews hard-synced: 15 originals, 5 rows x 3')
