import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

charts = re.findall(r'new Chart\((.*?)\)', text, re.DOTALL)
print(f"Total Chart instances: {len(charts)}")

# Find canvas ids
canvas = re.findall(r'<canvas[^>]*id="([^"]+)"', text)
print("Canvas IDs found:", canvas)
