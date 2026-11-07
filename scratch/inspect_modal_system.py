import re

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

funcs = re.findall(r'function\s+([A-Za-z0-9_]+)\s*\([^)]*\)', h)
print("JavaScript functions found:")
for fn in funcs:
    if any(k in fn.lower() for k in ['modal', 'open', 'show', 'detail', 'match', 'card', 'click', 'popup']):
        print(" ", fn)

# Check for modal HTML
modals = re.findall(r'<div[^>]*id=["\'][^"\']*modal[^"\']*["\'][^>]*>', h, re.I)
print("\nModal elements by ID:")
for m in modals:
    print(" ", m)

modals_cls = re.findall(r'<div[^>]*class=["\'][^"\']*modal[^"\']*["\'][^>]*>', h, re.I)
print("\nModal elements by class:")
for m in modals_cls[:10]:
    print(" ", m)
