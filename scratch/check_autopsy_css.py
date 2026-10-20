with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('.autopsy-card')
if pos != -1:
    print(text[pos:pos+1500])
