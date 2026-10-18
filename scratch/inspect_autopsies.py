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

# Find the cards in ac_html before table
table_pos = ac_html.find('<table')
cards_html = ac_html[:table_pos]

# Let's extract titles or bold text in cards
matches_in_autopsies = re.findall(r'<div[^>]*style="[^"]*font-size:\s*1\.[12]rem[^"]*"[^>]*>(.*?)</div>', cards_html)
print("Autopsy Card Titles:", matches_in_autopsies)

# Print snippet of cards
print("\nFirst 1500 chars of cards:")
print(cards_html[cards_html.find('autolearn-hero'):cards_html.find('autolearn-hero')+2500])
