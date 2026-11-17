# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'view-matches', html)]
print('view-matches positions:', matches)
for p in matches:
    print('match at', p, repr(html[p-20:p+100]))

matches_banner = [m.start() for m in re.finditer(r'BANNER DE CONTEXTO TEMPORAL', html)]
print('BANNER DE CONTEXTO TEMPORAL:', matches_banner)
for p in matches_banner:
    print('banner at', p, repr(html[p-20:p+100]))
