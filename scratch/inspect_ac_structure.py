import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

ac_start = text.find('id="view-container-autocorrect"')
ac_end = text.find('<!-- Fin de view-container-autocorrect -->')

ac_html = text[ac_start:ac_end]

# Find major section banners or headers in ac_html
banners = re.findall(r'<div[^>]*class="[^"]*(?:hero|title|heading|card-title)[^"]*"[^>]*>([^<]+)</div>', ac_html)
print("Sections in ac_html:", banners[:15])

# Find tables in ac_html
tables = re.findall(r'<table[^>]*>(.*?)</table>', ac_html, re.DOTALL)
print(f"Number of tables in ac_html: {len(tables)}")
for i, t in enumerate(tables):
    headers = re.findall(r'<th[^>]*>([^<]+)</th>', t)
    print(f"Table {i+1} headers: {headers}")
