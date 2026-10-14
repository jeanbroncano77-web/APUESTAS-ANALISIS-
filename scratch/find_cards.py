import re

html = open("index.html", encoding="utf-8").read()

# Find hero or date badges
badges = re.findall(r'<span[^>]*class="[^"]*badge[^"]*"[^>]*>(.*?)</span>', html, re.DOTALL)
print("Badges:", [b.strip() for b in badges[:10]])

dates = re.findall(r'(?:Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo)\s+\d{1,2}/\d{1,2}/\d{4}', html)
print("Dates in HTML:", set(dates))

# Find the match cards or match titles
match_titles = re.findall(r'<div class="match-name">([^<]+)</div>', html)
print("Match names in HTML:", match_titles)

# Find winrate badges / stats
kpis = re.findall(r'<div class="kpi-[^"]*">([^<]+)</div>', html)
print("KPIs:", kpis[:10])

# Find stat cards
stat_boxes = re.findall(r'<(?:div|span)[^>]*class="[^"]*(?:metric|stat|kpi|winrate|counter)[^"]*"[^>]*>([^<]+)</(?:div|span)>', html)
print("Stat boxes sample:", stat_boxes[:15])
