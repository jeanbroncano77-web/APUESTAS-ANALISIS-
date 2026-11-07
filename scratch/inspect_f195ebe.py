import subprocess
import re

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')
print("f195ebe index.html length:", len(out))

# Find match views
views = re.findall(r'<div class="match-view[^"]*" id="match-\d+"[^>]*>', out)
print("Match views found:", len(views))
for v in views:
    print(" ", v)

# Find switcher cards
switchers = re.findall(r'<div class="switcher-card[^"]*"[^>]*onclick="setMatch\((\d+)\)"[^>]*>', out)
print("Switcher cards with onclick:", switchers)

# Check chartConfigs in script
idx_cfg = out.find('var chartConfigs =')
if idx_cfg != -1:
    print("\nchartConfigs:")
    print(out[idx_cfg:idx_cfg+800])

# Inspect first match-view
idx_view0 = out.find('id="match-0"')
if idx_view0 != -1:
    print("\nMatch-0 snippet (first 1200 chars):")
    print(out[idx_view0:idx_view0+1200])
