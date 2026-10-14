with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
rows = re.findall(r'<tr class="audit-row.*?>.*?</tr>', text, re.DOTALL)
print("Total audit rows in index.html:", len(rows))
for r in rows:
    if '#79' in r or '#82' in r or '#40' in r or 'Liverpool' in r or 'Crystal Palace' in r:
        print("--- ROW ---")
        print(r.encode('ascii', 'ignore').decode())
