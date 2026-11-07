with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx5 = h.find('id="match-5"')
idx_end = h.find('<!-- Fin de view-container-matches -->')
m5 = h[idx5:idx_end]
print("Match 5 len:", len(m5))
print("Hero in M5:", 'hero-banner' in m5)
print("Fija in M5:", 'fija-gold-card' in m5)
print("Goals in M5:", 'Mercados de Goles' in m5)
print("Corners in M5:", 'Córners & Balón Parado' in m5)
print("Cards in M5:", 'Tarjetas & Rigor Arbitral' in m5)
print("Props in M5:", 'Remates & Disparos a Puerta' in m5)
print("Med in M5:", 'Auditoría Sanitaria' in m5)
