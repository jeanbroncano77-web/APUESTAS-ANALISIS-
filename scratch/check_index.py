import re
from collections import Counter

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find rows in tbody id="audit-table-tbody"
tb_start = text.find('id="audit-table-tbody"')
tb_end = text.find('</tbody>', tb_start)
tbody_html = text[tb_start:tb_end]

cats = re.findall(r'data-category="([^"]+)"', tbody_html)
print('data-category in audit tbody:', Counter(cats))

statuses = re.findall(r'data-status="([^"]+)"', tbody_html)
print('data-status in audit tbody:', Counter(statuses))

# Total rows
rows = tbody_html.count('<tr class="audit-row')
print('Total rows in tbody:', rows)
