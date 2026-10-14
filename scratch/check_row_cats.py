import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

tb_start = text.find('id="audit-table-tbody"')
tb_end = text.find('</tbody>', tb_start)
tbody_html = text[tb_start:tb_end]

for m in re.finditer(r'<tr class="audit-row[^"]*"[^>]*data-category="([^"]+)"[^>]*data-status="([^"]+)"[\s\S]*?class="col-id">#(\d+)</td>[\s\S]*?<div class="match-name">([^<]+)</div>[\s\S]*?<div class="sel-text">([^<]+)</div>', tbody_html):
    cat, status, mid, match, sel = m.groups()
    if int(mid) <= 15 or int(mid) >= 60:
        print(f"Row #{mid}: cat={cat}, status={status}, match={match}, sel={sel[:35]}")
