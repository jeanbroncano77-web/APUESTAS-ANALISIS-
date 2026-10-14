import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

for url in [
    "https://jeanbroncano77-web.github.io/APUESTAS-ANALISIS-/",
    "https://apuestas-analisis.onrender.com/"
]:
    print(f"\n--- Checking {url} ---")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")
            print(f"Length: {len(html)}")
            
            # Find banner
            fija_oro = re.findall(r'<div class="fija-oro-title">([^<]+)</div>', html)
            print("Fija de oro title:", fija_oro[:2])
            
            # Find date badge
            badge_fija = re.findall(r'<div class="badge-fija-oro">([^<]+)</div>', html)
            print("Badge fija oro:", badge_fija[:2])
            
            # Find teams in switcher
            switcher_teams = re.findall(r'<div class="switcher-teams">\s*<span>([^<]+)</span>\s*<span class="vs-text">vs</span>\s*<span>([^<]+)</span>', html)
            print("Switcher teams count:", len(switcher_teams))
            for st in switcher_teams[:4]:
                print(f"   {st[0].strip()} vs {st[1].strip()}")
                
    except Exception as e:
        print("Error fetching:", e)
