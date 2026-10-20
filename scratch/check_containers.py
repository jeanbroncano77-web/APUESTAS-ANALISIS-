with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.search(r'<div id=["\']view-container-winrate["\']', text)
m2 = re.search(r'<div id=["\']view-container-autocorrect["\']', text)
m3 = re.search(r'<script', text[m2.start():]) if m2 else None

print('m1 (winrate start):', m1.start() if m1 else None)
print('m2 (autocorrect start):', m2.start() if m2 else None)
print('m3 (script start after autocorrect):', m2.start() + m3.start() if m3 else None)

# Check what is between m1 and m2
print('Text before m2 (last 100 chars):', repr(text[m2.start()-100:m2.start()]))
# Check what is before m3 (last 100 chars):
script_pos = m2.start() + m3.start()
print('Text before script (last 100 chars):', repr(text[script_pos-100:script_pos]))
