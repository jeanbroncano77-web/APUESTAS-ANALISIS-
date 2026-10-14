import urllib.request
import json
import time

url_matches = "https://apuestas-analisis.onrender.com/api/matches"
url_audit = "https://apuestas-analisis.onrender.com/api/audit"

print("Comprobando despliegue en Render...")
for attempt in range(1, 10):
    try:
        req = urllib.request.Request(url_matches, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            matches = [m.get("match") for m in data.get("Matches", [])]
            target_date = data.get("TargetDate")
            print(f"Intento {attempt}: TargetDate={target_date}, Matches={matches[:3]}")
            if "Galatasaray vs Barcelona" in matches:
                print("¡Despliegue de Champions League confirmado en Render!")
                break
    except Exception as e:
        print(f"Intento {attempt}: Esperando despliegue ({e})...")
    time.sleep(6)
