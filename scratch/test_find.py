with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

t_start = html.find('<table class="audit-table"')
tb_literal = html.find('<tbody>', t_start)
tb_id = html.find('<tbody id="audit-table-tbody"', t_start)

print("t_start:", t_start)
print("tb_literal:", tb_literal)
print("tb_id:", tb_id)
if tb_literal != -1:
    print("tb_literal is after tb_id by:", tb_literal - tb_id)
    # let's see what is at tb_literal
    print("Content around tb_literal:", html[tb_literal-50:tb_literal+50])
