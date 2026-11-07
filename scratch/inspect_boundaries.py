# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = text.find('<div id="view-container-matches"')
m2 = text.find('<div id="view-container-winrate"')
area1 = text[m1:m2]

import re
headers = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', area1, re.DOTALL)
print("Headers in Area 1:")
for h in headers:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    print(" -", clean)

print("\nNumber of match cards / sections:")
print("Cards count:", len(re.findall(r'PARTIDO \d+:', area1)))
