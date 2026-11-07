with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('equityChartInstance = new Chart')
print(html[idx-1500:idx])

