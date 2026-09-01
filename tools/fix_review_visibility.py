from pathlib import Path
import re

mobile_path = Path('mobile-eva-current.js')
index_path = Path('index.html')

mobile = mobile_path.read_text(encoding='utf-8')
index = index_path.read_text(encoding='utf-8')

# Make all five review lanes physically visible. Older STLuxe CSS constrained the stage height.
override = """
const reviewVisibilityStyle=document.createElement('style');reviewVisibilityStyle.textContent=`
#tn13Reviews .tn30-review-stage{display:flex!important;flex-direction:column!important;gap:12px!important;height:auto!important;max-height:none!important;min-height:0!important;overflow:visible!important}
#tn13Reviews .tn30-lane{display:block!important;position:relative!important;height:auto!important;min-height:0!important;overflow:hidden!important}
#tn13Reviews .tn30-track{display:flex!important;align-items:stretch!important}
#tn13Reviews .tn30-review-card{flex:0 0 min(82vw,330px)!important;min-height:170px!important}
#tn13Reviews .tn30-card-stars{display:flex!important;visibility:visible!important;opacity:1!important}
`;document.head.appendChild(reviewVisibilityStyle);
"""

if 'reviewVisibilityStyle' not in mobile:
    mobile = mobile.replace('// REVIEWS\n', '// REVIEWS\n' + override, 1)

# The review block must contain 5 independent lanes of 3 reviews each.
expected = 'const reviewLanes=[REAL_REVIEW_DATA.slice(0,3),REAL_REVIEW_DATA.slice(3,6),REAL_REVIEW_DATA.slice(6,9),REAL_REVIEW_DATA.slice(9,12),REAL_REVIEW_DATA.slice(12,15)];'
if expected not in mobile:
    raise SystemExit('Five review lanes are not present before visibility patch')
if mobile.count('tn30-card-stars') < 2:
    raise SystemExit('Five-star card markup is missing')

# Force mobile browsers to load the new JS instead of a cached copy.
version = '20260902-5x3-v2'
patterns = [
    r'mobile-eva-current\.js(?:\?[^\"\']*)?',
    r'mobile-stluxe-current\.js(?:\?[^\"\']*)?'
]
replaced = False
for pat in patterns:
    if re.search(pat, index):
        index = re.sub(pat, f'mobile-eva-current.js?v={version}', index)
        replaced = True

# If the page had an inline injection rather than a plain script tag, ensure a definitive mobile script exists.
if not replaced and 'mobile-eva-current.js' not in index:
    index = index.replace('</body>', f'<script src="mobile-eva-current.js?v={version}" defer></script>\n</body>')
    replaced = True

if f'mobile-eva-current.js?v={version}' not in index:
    raise SystemExit('Could not cache-bust mobile bundle reference')

mobile_path.write_text(mobile, encoding='utf-8')
index_path.write_text(index, encoding='utf-8')
print('Review visibility and cache-busting patch OK')
