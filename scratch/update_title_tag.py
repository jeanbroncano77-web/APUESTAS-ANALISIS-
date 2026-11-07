import re

new_title = "<title>SportsAI Analytics &middot; 11 Partidos Estelares &bull; S\u00e1bado 07/11 &bull; Win Rate & Autoaprendizaje</title>"

for path in ['index.html', 'dashboard_pronosticos.html', '../index.html']:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<title>.*?</title>', new_title, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated title in {path}")
    except Exception as e:
        print(f"Error {path}: {e}")

