import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_js = text.find('chart-equity-curve')
if pos_js != -1:
    print(text[pos_js-200:pos_js+1200])
