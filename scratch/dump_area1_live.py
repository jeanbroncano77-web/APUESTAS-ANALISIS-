import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

url = "https://apuestas-analisis.onrender.com/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8")

# Let's see what is inside id="view-container-matches"
m = re.search(r'<div id="view-container-matches"[^>]*>([\s\S]*?)</div>\s*<!-- \/view-container-matches -->', html)
if not m:
    m = re.search(r'<div id="view-container-matches"[^>]*>([\s\S]*?)</div>\s*<div class="audit-section"', html)
if not m:
    # find where view-container-matches starts
    idx = html.find('id="view-container-matches"')
    print("Found index:", idx)
    print("Next 2000 chars:")
    print(html[idx:idx+2000])
else:
    print("Matched section! Length:", len(m.group(1)))
    print(m.group(1)[:1500])
