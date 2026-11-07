import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find chart initialization script
idx_chart = html.find('chart-equity-curve')
if idx_chart != -1:
    print("Found chart-equity-curve at", idx_chart)
    print(html[idx_chart:idx_chart+2000])

# Look for script tag with Chart
idx_script = html.find('new Chart')
if idx_script != -1:
    print("\nFound new Chart at", idx_script)
    print(html[idx_script:idx_script+2000])

