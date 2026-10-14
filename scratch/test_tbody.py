with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

t_start = text.find('class="audit-table"')
tb_start = text.find('<tbody', t_start)
tb_end = text.find('</tbody>', tb_start)
print("t_start:", t_start)
print("tb_start:", tb_start, text[tb_start:tb_start+40])
print("tb_end:", tb_end)

rows = text[tb_start:tb_end].count('class="audit-row')
print("Total rows inside audit-table:", rows)
