import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs = re.findall(r'id="tab-\d+"', html)
print("Tabs found in index.html:", tabs)

views = re.findall(r'id="match-\d+"', html)
print("Match views found in index.html:", views)

charts = re.findall(r'id="chart1X2-\d+"', html)
print("1X2 Chart canvases found:", charts)

print("Title in index.html:", re.search(r'<title>.*?</title>', html).group(0))

print("\nVerifying each match view has full content:")
for i in range(6):
    view_match = re.search(f'id="match-{i}"(.*?)<!-- ==================== PARTIDO|<!-- Fin de view-container-matches -->', html, re.DOTALL)
    if view_match:
        content = view_match.group(1)
        has_hero = 'hero-banner' in content
        has_fija = 'fija-gold-card' in content
        has_goals = 'Mercados de Goles' in content
        has_corners = 'Córners & Balón Parado' in content
        has_cards = 'Tarjetas & Rigor Arbitral' in content
        has_props = 'Remates & Disparos a Puerta' in content
        has_med = 'Auditoría Sanitaria' in content
        print(f"Match {i}: Hero={has_hero}, Fija={has_fija}, Goals={has_goals}, Corners={has_corners}, Cards={has_cards}, Props={has_props}, Med={has_med}")
    else:
        print(f"Match {i}: NOT FOUND")
