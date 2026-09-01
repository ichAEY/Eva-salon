from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
old='<script defer src="mobile-eva-current.js?v=20260831-current-clean"></script>'
new='<script defer src="mobile-eva-current.js?v=20260902-reviews-5x3"></script>'
assert s.count(old)==1, f'expected one old mobile script tag, got {s.count(old)}'
out=s.replace(old,new,1)
assert out.count(new)==1
# Exactly one line is allowed to change.
old_lines=s.splitlines()
new_lines=out.splitlines()
assert len(old_lines)==len(new_lines)
diffs=[i for i,(a,b) in enumerate(zip(old_lines,new_lines),1) if a!=b]
assert len(diffs)==1, diffs
p.write_text(out,encoding='utf-8')
print('CACHE_BUST_OK line',diffs[0])
