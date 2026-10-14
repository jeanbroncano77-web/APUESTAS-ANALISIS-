import re

html = open("index.html", encoding="utf-8").read()

# Look for section header
header_match = re.search(r'<div class="header-content">([\s\S]*?)</div>\s*</div>', html)
if header_match:
    print("Header content:")
    for line in header_match.group(1).splitlines():
        if line.strip():
            print(" ", line.strip()[:100])

# Look for view-container-matches
start_m = html.find('id="view-container-matches"')
if start_m != -1:
    print("\nFound view-container-matches at pos:", start_m)
    # Search for match names within next 10000 chars
    chunk = html[start_m:start_m+20000]
    matches_in_chunk = re.findall(r'<div class="match-[^"]*">([^<]+)</div>', chunk)
    print("Matches in chunk sample:", matches_in_chunk[:10])
    
    # Check what teams appear in chunk
    for team in ["Liverpool", "Manchester City", "Galatasaray", "Barcelona", "Arsenal", "Inter", "Atalanta", "Real Madrid", "Boca"]:
        if team in chunk:
            print(f"  Team {team} is in Area 1!")

# Also check date pill / badge
pills = re.findall(r'<span[^>]*class="[^"]*badge[^"]*"[^>]*>(.*?)</span>', html)
print("\nBadges sample:")
for p in pills[:8]:
    print(" ", p.strip()[:80])
