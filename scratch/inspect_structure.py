import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all section tags
sections = re.findall(r'<section[^>]*>', html, re.I)
print("Sections found:", len(sections))
for s in sections[:15]:
    print(" ", s)

# Find major headers / comments
comments = re.findall(r'<!--(.*?)-->', html)
print("\nMajor comments found:", len(comments))
for c in comments:
    if any(k in c.lower() for k in ['área', 'area', 'cartelera', 'auditor', 'kpi', 'hero', 'fija', 'tabla']):
        print("  COMMENT:", c.strip()[:80])

# Find headings
headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html, re.I)
print("\nHeadings found:", len(headings))
for h in headings[:15]:
    clean_h = re.sub(r'<[^>]+>', ' ', h).strip()
    print("  H:", clean_h[:80])
