import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find match cards
cards = re.findall(r'<div class="match-card-v6[^"]*"(.*?)</div>\s*</div>\s*</div>', html, re.DOTALL)
print("Cards found regex 1:", len(cards))

titles = re.findall(r'<div class="match-title-v6">(.*?)</div>', html)
print("Match titles found:", len(titles))
for i, t in enumerate(titles):
    print(f"{i+1}: {t.strip()}")

