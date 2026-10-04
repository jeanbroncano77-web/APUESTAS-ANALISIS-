import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_init = text.find("getElementById('chart-equity-curve')")
if pos_init != -1:
    print(text[pos_init-100:pos_init+1200])
else:
    print("Not found by getElementById")
    # let's search for chart-equity-curve in scripts
    matches = [m.start() for m in re.finditer(r'chart-equity-curve', text)]
    print("Occurrences at:", matches)
    for p in matches[1:]:
        print("Snippet:", text[p-50:p+300])
