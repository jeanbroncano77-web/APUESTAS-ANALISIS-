with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cats = re.findall(r'data-category="([^"]+)"', text)
from collections import Counter
print("data-category counts in index.html:", Counter(cats))
