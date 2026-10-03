import re

html = open("index.html", encoding="utf-8").read()
badge = re.findall(r'<div class="badge-fija-oro">.*?</div>', html)
fija_title = re.findall(r'<div class="fija-oro-title">.*?</div>', html)
switcher = re.findall(r'<div class="switcher-teams">.*?</div>', html, re.DOTALL)
matches_hero = re.findall(r'<div class="team-name">(.*?)</div>', html)

out = []
out.append("Badge: " + str(badge))
out.append("Fija title: " + str(fija_title))
for s in switcher:
    cleaned = re.sub(r'\s+', ' ', s).strip()
    out.append("Match: " + cleaned)
out.append("Hero teams: " + str(matches_hero))

with open("scratch/index_inspection_result.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(out))

print("Inspection written to scratch/index_inspection_result.txt")
