from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old='mobile-eva-current.js?v=20260902-reviews-5x3'
new='mobile-eva-current.js?v=20260902-reviews-3x5-v2'
if old not in s:
    raise SystemExit('old cache key not found')
out=s.replace(old,new,1)
if out.count(new)!=1:
    raise SystemExit('cache key count invalid')
p.write_text(out,encoding='utf-8')
print('OK: cache key only')
