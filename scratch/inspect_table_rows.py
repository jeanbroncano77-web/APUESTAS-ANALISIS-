import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_tbody = text.find('id="audit-table-tbody"')
pos_tbody_end = text.find('</tbody>', pos_tbody)
tbody = text[pos_tbody:pos_tbody_end]

rows = re.findall(r'<tr class="audit-row[^"]*"[^>]*>(.*?)</tr>', tbody, re.DOTALL)
print(f"Total rows in audit table: {len(rows)}")

matches_in_table = set()
for r in rows:
    m_name = re.search(r'<div class="match-name">(.*?)</div>', r)
    if m_name:
        matches_in_table.add(m_name.group(1))

print("Matches in table:", matches_in_table)
