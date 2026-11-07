with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

# Let's find where Area 1 starts and where Area 2 starts
idx_area1 = h.find('Cartelera')
print("Found Cartelera at:", idx_area1)
if idx_area1 != -1:
    print(h[max(0, idx_area1-200):idx_area1+300])

idx_area2 = h.find('VISTA 2: WIN RATE')
print("\nFound VISTA 2 at:", idx_area2)
if idx_area2 != -1:
    print(h[max(0, idx_area2-200):idx_area2+300])
