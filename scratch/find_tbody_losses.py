import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

tb_start = text.find('id="audit-table-tbody"')
tb_end = text.find('</tbody>', tb_start)
tbody_html = text[tb_start:tb_end]

rows = re.findall(r'<tr class="audit-row[^"]*"[^>]*data-category="([^"]+)"[^>]*data-status="([^"]+)"[\s\S]*?</tr>', tbody_html)
print(f"Total parsed rows: {len(rows)}")

row_blocks = re.findall(r'<tr class="audit-row[\s\S]*?</tr>', tbody_html)
for block in row_blocks:
    if 'data-status="loss"' in block:
        m_id = re.search(r'class="col-id">([^<]+)<', block)
        m_name = re.search(r'class="match-name">([^<]+)<', block)
        m_cat = re.search(r'data-category="([^"]+)"', block)
        id_str = m_id.group(1) if m_id else '?'
        name_str = m_name.group(1) if m_name else '?'
        cat_str = m_cat.group(1) if m_cat else '?'
        print(f"Loss: {id_str} | {name_str} | category: {cat_str}")
