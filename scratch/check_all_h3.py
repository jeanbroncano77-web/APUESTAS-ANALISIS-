import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL)
print("Total h3 elements:", len(h3s))
for idx, h in enumerate(h3s):
    clean = re.sub(r'<[^>]+>', ' ', h).strip()
    print(f"  {idx+1}: {clean}")

