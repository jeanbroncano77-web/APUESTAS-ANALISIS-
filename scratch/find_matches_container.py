with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('id="view-container-matches"')
print("Found id=\"view-container-matches\" at:", idx)
if idx != -1:
    print(h[max(0, idx-200):idx+500])
