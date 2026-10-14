with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for m in re.finditer(r'Ticket Cuantitativo', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    print("Match at pos", m.start(), ":", repr(text[start:end]))

for m in re.finditer(r'slip-drawer', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    print("Match at pos", m.start(), ":", repr(text[start:end]))
