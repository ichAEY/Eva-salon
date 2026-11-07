const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {loadSiteData} = require('./validate-site-data.cjs');
const data = loadSiteData('site-data.js');
const unusedLocales = new Set(['ru','en','hy','uz','tg'].filter(locale=>!data.locales.includes(locale)));
function checkLocaleData(value, path='site') {
  if(!value||typeof value!=='object')return;
  for(const [key,item] of Object.entries(value)) {
    assert.ok(!unusedLocales.has(key), `${path}.${key}: inactive locale in client data`);
    checkLocaleData(item, `${path}.${key}`);
  }
}
checkLocaleData(data);
const window = {TANEM_SITE_DATA:data};
vm.runInNewContext(fs.readFileSync('site-services.js','utf8'),{window});
const view = window.TANEM_SERVICES;
assert.equal(view.normalizePrice('от 500 до 1 000 ₽'), '500–1 000 ₽');
assert.equal(view.normalizePrice('от 500 ₽'), 'от 500 ₽');
assert.equal(view.duration('90 мин','ru'),'1,5 ч');
const service = {id:'test',title:{ru:'Маникюр /обрезной/'},price:{ru:'600 ₽'},description:{ru:'Мастер: 600 ₽; ТОП мастер: 600 ₽; Индивидуальный уход.'},variants:[{label:{ru:'Мастер'},price:{ru:'600 ₽'}},{label:{ru:'ТОП мастер'},price:{ru:'600 ₽'}}]};
assert.equal(view.description(service,'ru'),'Индивидуальный уход.');
for (const layout of ['desktop','mobile']) {
  const html=view.render(service,layout,'ru');
  assert.equal((html.match(/<dt>/g)||[]).length,2);
  assert.equal((html.match(/<dd>/g)||[]).length,2);
  assert.match(html,/<details class="tanem-service-options"><summary><span class="tanem-options-label">Варианты и цены \+<\/span><\/summary><div class="tanem-options-panel">/);
  assert.doesNotMatch(html,/<details[^>]*\bopen\b/);
  assert.doesNotMatch(html,/is-tariff-description/);
  assert.match(html,/>Индивидуальный уход\./);
  assert.match(html,/tanem-service-price">/);
  assert.doesNotMatch(html,/Мастер: 600 ₽/);
  const lengthService={
    id:'color-length',profileId:'elvira',variantType:'length',title:{ru:'Окрашивание'},price:'4 500–7 600 ₽',
    variants:[
      {label:{ru:'Короткие'},price:'4 500 ₽'},
      {label:{ru:'Средние'},price:'5 500 ₽'},
      {label:{ru:'Длинные'},price:'6 600 ₽'},
      {label:{ru:'Очень длинные'},price:'7 600 ₽'},
      {label:{ru:'Без цены'},price:'—'}
    ],
    description:{ru:'Окрашивание по длине.'}
  };
  const options=view.render(lengthService,layout,'ru');
  assert.match(options,/<details class="tanem-service-options"><summary><span class="tanem-options-label">Стоимость по длине \+<\/span><\/summary><div class="tanem-options-panel">/);
  assert.doesNotMatch(options,/<details[^>]*\bopen\b/);
  assert.equal((options.match(/<dd>/g)||[]).length,4);
  assert.doesNotMatch(options,/Без цены/);
  assert.match(options,new RegExp('service-description-'+layout+'-elvira-color-length'));
  assert.match(options,/data-eva-profile="elvira"/);
  for (const item of data.services) {
    const rendered=view.render(item,layout,'ru');
    assert.ok(rendered.includes('tanem-service-book'));
    assert.ok(!rendered.includes('undefined'));
  }
}
console.log('PASS: client service ranges, tariff deduplication, prose preservation and both renderers');
