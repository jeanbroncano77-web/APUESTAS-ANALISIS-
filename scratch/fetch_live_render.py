import urllib.request
import re

url = "https://apuestas-analisis.onrender.com/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8")
        print(f"Live HTML fetched from Render! Length: {len(html)}")
        
        # Check title
        title = re.search(r'<title>(.*?)</title>', html)
        print("Title:", title.group(1) if title else "No title")
        
        # Check hero badges / dates
        badges = re.findall(r'<span[^>]*class="[^"]*badge[^"]*"[^>]*>(.*?)</span>', html)
        print("\nBadges:")
        for b in badges[:5]:
            print(" ", b.strip()[:80])
            
        # Check what matches are in Area 1
        matches_area1 = re.findall(r'<div class="match-name">([^<]+)</div>', html)
        print("\nMatch names in table or cards:")
        print("Count:", len(matches_area1))
        print("First 10:", matches_area1[:10])
        print("Last 10:", matches_area1[-10:] if len(matches_area1) > 10 else [])
        
        # Check team cards in Area 1
        teams_card = re.findall(r'<h3 class="team-name">([^<]+)</h3>', html)
        print("\nTeam names in match cards (Area 1):")
        print(teams_card)
        
        # Check TargetDate
        td = re.findall(r'(?:Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo)\s+\d{1,2}/\d{1,2}/\d{4}', html)
        print("\nDates in live HTML:", set(td))
except Exception as e:
    print("Error fetching from Render:", e)
