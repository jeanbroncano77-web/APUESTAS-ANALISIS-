import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

patterns = [
    r'95\.8%',
    r'23/24',
    r'\(56\)',
    r'\(51\)',
    r'\(5\)',
    r'\(24\)',
    r'51 Aciertos',
    r'5 Fallos',
    r'56 selecciones',
    r'24 de 24',
    r'23 de 24'
]

for p in patterns:
    matches = list(re.finditer(p, text))
    print(f"Pattern '{p}': {len(matches)} occurrences")
    for m in matches[:3]:
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        snippet = text[start:end].replace('\n', ' ')
        print(f"   Line near pos {m.start()}: ...{snippet}...")
