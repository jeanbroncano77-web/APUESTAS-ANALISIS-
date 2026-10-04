import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('class="view-mode-nav"')
if pos != -1:
    print("=== NAV FOUND ===")
    print(text[pos-100:pos+800])
else:
    print("view-mode-nav not found in index.html")
