with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('equityChartInstance = new Chart')
if idx == -1:
    idx = html.find('chart-equity-curve')
    idx = html.find('new Chart', idx)

print("Snippet:")
print(html[idx:idx+3500])
