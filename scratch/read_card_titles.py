with open('scratch/sample_match_view.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see all card headers in sample_match_view
import re
headers = re.findall(r'<div class="card-title">(.*?)</div>', text)
print("Card titles in match view:")
for h in headers:
    print(" -", h)
