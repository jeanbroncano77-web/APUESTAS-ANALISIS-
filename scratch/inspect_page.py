import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML Length:", len(html))

# Check KPI section
m_kpi = re.search(r'<div class="kpi-grid">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if m_kpi:
    clean = re.sub(r'<[^>]+>', ' ', m_kpi.group(0))
    print("KPI Grid Text:")
    print(' '.join(clean.split())[:1200])
else:
    # Look for other KPI / metric structures
    m2 = re.search(r'<section[^>]*class="[^"]*kpi[^"]*"[^>]*>.*?</section>', html, re.DOTALL)
    if m2:
        print("KPI Section Text:")
        print(' '.join(re.sub(r'<[^>]+>', ' ', m2.group(0)).split())[:1200])

# Check Area 1 Title & Dates
m_area1 = re.search(r'id="cartelera-section".*?</section>', html, re.DOTALL)
if not m_area1:
    m_area1 = re.search(r'<!-- ÁREA 1.*?-->.*?(?=<!-- ÁREA 2)', html, re.DOTALL)
if m_area1:
    print("\nArea 1 snippet:")
    lines = [line.strip() for line in m_area1.group(0).split('\n') if line.strip()][:30]
    print('\n'.join(lines[:20]))

# Check Area 2 summary
m_area2 = re.search(r'id="audit-section".*?</section>', html, re.DOTALL)
if not m_area2:
    m_area2 = re.search(r'<!-- ÁREA 2.*?-->.*?(?=<!-- ÁREA 3)', html, re.DOTALL)
if m_area2:
    print("\nArea 2 snippet:")
    lines = [line.strip() for line in m_area2.group(0).split('\n') if line.strip()][:20]
    print('\n'.join(lines[:15]))

# Check Area 3 summary
m_area3 = re.search(r'<!-- ÁREA 3.*?-->.*?(?=<!-- ÁREA 4|</main>|</body>)', html, re.DOTALL)
if m_area3:
    print("\nArea 3 snippet:")
    lines = [line.strip() for line in m_area3.group(0).split('\n') if line.strip()][:25]
    print('\n'.join(lines[:20]))
