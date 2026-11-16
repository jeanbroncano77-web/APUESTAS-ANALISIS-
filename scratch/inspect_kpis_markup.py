# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('class="winrate-kpi-grid"')
end_p = html.find('class="audit-filter-bar"', pos)
print('pos:', pos, 'end_p:', end_p)
if pos != -1 and end_p != -1:
    print(html[pos-10:end_p])
