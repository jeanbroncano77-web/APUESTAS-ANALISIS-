import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ac_start = text.find('id="view-container-autocorrect"')
ac_end = text.find('</div> <!-- Fin de view-container-autocorrect -->')
ac_content = text[ac_start:ac_end]

matches_autopsy = re.findall(r'<div class="autopsy-match">(.*?)</div>', ac_content)
for m in matches_autopsy:
    print("Autopsy match:", re.sub(r'<[^>]+>', '', m).strip())
