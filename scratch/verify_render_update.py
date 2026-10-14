import urllib.request
import time

for attempt in range(12):
    try:
        req = urllib.request.Request('https://apuestas-analisis.onrender.com/', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as res:
            html = res.read().decode('utf-8')
            has_atalanta = 'Atalanta vs Venezia' in html
            has_drawer = 'id="slip-drawer"' in html
            if has_atalanta and not has_drawer:
                print(f"Attempt {attempt+1}: Render is LIVE with Real Monday Matches and NO Ticket Cuantitativo!")
                break
            else:
                print(f"Attempt {attempt+1}: Render building... has_atalanta={has_atalanta}, has_drawer={has_drawer}")
                time.sleep(6)
    except Exception as e:
        print(f"Attempt {attempt+1}: Error: {e}")
        time.sleep(6)
