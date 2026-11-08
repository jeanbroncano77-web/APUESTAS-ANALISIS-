import re

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

print("Switchers:", len(re.findall(r'class="switcher-card', h)))
print("Match views:", len(re.findall(r'class="match-view', h)))
print("Picks in table:", len(re.findall(r'<td class="col-id">#\d+</td>', h)))
print("Title:", re.search(r'<title>.*?</title>', h).group(0))
