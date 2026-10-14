import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fb_start = text.find('<div class="audit-filter-bar">')
fb_end = text.find('</div>', fb_start) + 6
print(text[fb_start:fb_end])
