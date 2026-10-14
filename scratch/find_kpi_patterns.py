import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

patterns = [
    r'92\.7%',
    r'95\.3%',
    r'89\s*Aciertos',
    r'7\s*Fallos',
    r'89/96',
    r'61/64',
    r'14\s*Verdes',
    r'Racha activa[^<]*',
    r'2,303\.75',
    r'1,303\.75',
    r'130\.3%'
]

for p in patterns:
    matches = list(re.finditer(p, text))
    print(f"Pattern '{p}': found {len(matches)} times")
    for m in matches[:3]:
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        print("  Snippet:", text[start:end].replace('\n', ' '))
