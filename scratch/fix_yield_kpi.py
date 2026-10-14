for fname in ['index.html', 'dashboard_pronosticos.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('+130.4%', '+107.6%')
    t = t.replace('+$1,303.75', '+$1,075.75')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(t)
print('Yield KPI fixed!')
