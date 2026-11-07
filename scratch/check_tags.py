with open('scratch/update_cartelera_saturday_nov7.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
headers = re.findall(r'<div class="match-teams[^"]*">(.*?)</div>', text)
print("match-teams found:", len(headers))
for h in headers:
    print(" ", h.strip())

# Or look for any match name tag
names = re.findall(r'<div class="team-name">(.*?)</div>', text)
print("team-name found:", len(names))
for n in names[:10]:
    print(" ", n.strip())

