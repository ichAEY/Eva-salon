from pathlib import Path
import html, re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

reviews = [
('Александра Н.','Все отлично!! Благодарю) сама хожу в ваш салон на окрашивание, маникюр. И мужа регулярно на стрижку записываю. Все мастера настоящие профессионалы!'),
('natalia tatarinceva','Все отлично, мастер хороший,  внимательный.\nВсе на высшем уровне.\nРекомендую.\nСейчас сложно найти салон, где сочетаются цена и качество.  Спасибо'),
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
('Алина С.','Что касается салона в целом: удобное расположение, приятные цены, приветливый коллектив, всегда дружелюбная атмосфера.\n\nОтдельно хочу отметить мастера по маникюру Розу. Она замечательный профессионал своего дела и просто чуткий человек. Маникюр держится превосходно и ручки после нее выглядят потрясающе. Спасибо 🌹\n\nХочу дополнить отзыв: была записана на окрашивание к Нарине, как вдруг во всем доме выключили свет, но мастер не растерялась и справилась блестяще со своей работой в таких экстремальных условиях. Тут работают настоящие профессионалы!'),
('Зарета К.','Мастер Евгения, лучшая в своём деле.Очень красиво подстригла, объяснила как делать укладку дома.'),
('Марина Ким','Professional Master Nara, thank you for my brown hair like 18 years old, and delicious armenian coffee))'),
]

star = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.7l2.45 4.96 5.47.8-3.96 3.85.94 5.45L10 14.2l-4.9 2.57.94-5.45L1.08 7.46l5.47-.8L10 1.7Z"/></svg>'
stars = '<span class="review-stars-svg" aria-label="5 из 5">' + star * 5 + '</span>'

def card(name, text):
    return '<article class="review-card"><div class="review-top"><span class="review-name">%s</span>%s</div><p class="review-text">%s</p></article>' % (
        html.escape(name), stars, html.escape(text).replace('\n','<br>')
    )

rows=[]
for i in range(0,15,3):
    rows.append('<div class="reviews-row-3">' + ''.join(card(*r) for r in reviews[i:i+3]) + '</div>')

grid='\n      <div class="reviews-grid-5x3">\n        ' + '\n        '.join(rows) + '\n      </div>'

section = '''<section id="reviews">
      <div class="section-head"><div><h2>Отзывы</h2><p>Отзывы клиентов EVA из Яндекс Карт</p></div><a class="section-link" href="https://yandex.com/maps/org/eva/200326329284/reviews/" target="_blank" rel="noopener">Все отзывы ↗</a></div>
      <div class="reviews-summary"><div><div class="score">4,8</div><div class="score-label">185 оценок</div></div><div style="text-align:right"><div style="color:var(--violet);font-size:16px;letter-spacing:2px">★★★★★</div><div class="score-label">92 отзыва на Яндекс Картах</div></div></div>%s
    </section>''' % grid

s, n = re.subn(r'<section id="reviews">.*?</section>', section, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('desktop reviews section not replaced')

old_css = '.review-card{border:1px solid var(--line);border-radius:17px;padding:14px;margin-top:8px;background:#fff}\n    .review-top{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:9px}\n    .review-name{font-size:12px;font-weight:760}.review-stars{font-size:11px;color:var(--violet)}\n    .review-text{font-size:13px;line-height:1.48;color:#444047;margin:0}'
new_css = '.review-card{border:1px solid var(--line);border-radius:17px;padding:14px;margin-top:8px;background:#fff}\n    .review-top{display:flex;justify-content:space-between;gap:12px;align-items:flex-start;margin-bottom:9px}\n    .review-name{font-size:12px;font-weight:760}.review-stars{font-size:11px;color:var(--violet)}\n    .review-text{font-size:12px;line-height:1.48;color:#444047;margin:0;overflow-wrap:anywhere}\n    .reviews-grid-5x3{display:grid;gap:10px;margin-top:10px}\n    .reviews-row-3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;align-items:stretch}\n    .reviews-row-3 .review-card{margin-top:0;height:100%;min-width:0}\n    .review-stars-svg{display:flex;flex:0 0 auto;gap:2px;color:var(--violet)}\n    .review-stars-svg svg{width:11px;height:11px;display:block;fill:currentColor}'
if old_css not in s:
    raise SystemExit('desktop review css marker not found')
s = s.replace(old_css, new_css, 1)

# Hard checks: exactly 5 rows, exactly 15 cards, no synthetic authors.
section_check = re.search(r'<section id="reviews">.*?</section>', s, flags=re.S).group(0)
if section_check.count('reviews-row-3') != 5:
    raise SystemExit('not five rows')
if section_check.count('<article class="review-card">') != 15:
    raise SystemExit('not fifteen cards')
if 'Клиент EVA ·' in section_check:
    raise SystemExit('synthetic review remains')
if section_check.count('review-stars-svg') != 15:
    raise SystemExit('stars missing')

p.write_text(s, encoding='utf-8')
print('Desktop EVA reviews: 5 rows x 3 cards OK')
