with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('class="kpi-card kpi-card-gold"')
if idx != -1:
    print(h[idx:idx+500])
