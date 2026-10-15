# -*- coding: utf-8 -*-
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of index.html:', len(text))

print('\n--- MATCHES IN SWITCHER ---')
for m in re.findall(r'<div class="switcher-teams">(.*?)</div>', text, re.DOTALL):
    clean = ' '.join(m.split())
    print(' ', clean)

print('\n--- AUDIT ROW CHECK ---')
matches_97_102 = re.findall(r'#10[0-2]|#9[7-9]', text)
print('Found references to #97-#102:', set(matches_97_102))

print('\n--- CICLO CHECK ---')
for m in re.findall(r'Ciclo #\d+[^<]*', text):
    print(' ', m)

print('\n--- WIN RATE / KPIS DETAILS ---')
for m in re.finditer(r'<div[^>]*class="[^"]*metric-card[^"]*"[^>]*>(.*?)</div>\s*</div>', text, re.DOTALL):
    snippet = ' '.join(m.group(0).split())
    print(' ', snippet[:140])

print('\n--- AUDIT ROWS #97 to #102 DETAILS ---')
for row_id in [97, 98, 99, 100, 101, 102]:
    pattern = rf'<tr[^>]*>.*?#{row_id}.*?</tr>'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        row_text = ' '.join(match.group(0).split())
        print(f'Row #{row_id}: {row_text[:160]}...')
    else:
        print(f'Row #{row_id}: NOT FOUND!')
