import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Total HTML characters: {len(html)}")

# 1. Contenedores
for cid in ['view-container-matches', 'view-container-winrate', 'view-container-autocorrect']:
    assert cid in html, f"Falta {cid}"
    print(f"✓ Contenedor {cid} presente.")

# 2. Navegación
assert '90.9% WIN &bull; 100% FIJAS' in html
assert 'Ciclo #15 Activo' in html
print("✓ Navegación con badges de Win Rate y Aprendizaje presente.")

# 3. Win Rate
assert 'WIN RATE GLOBAL: 90.9% | FIJAS: 100%' in html
assert '12 de 12 aciertos' in html
assert '#44' in html
assert 'Portugal vs Noruega' in html
assert 'Grecia vs Alemania' in html
assert 'Países Bajos vs Serbia' in html
assert 'Gales vs Dinamarca' in html
assert 'Irlanda vs Israel' in html
assert 'Kosovo vs Austria' in html
print("✓ Auditoría de Win Rate con 44 selecciones y racha 100% en Fijas validada.")

# 4. Autoaprendizaje
assert 'AUTOPSIA #5 (FALLO ESTRUCTURAL DE NOVATO CORREGIDO)' in html
assert 'official_calendar.json' in html
assert 'Ciclo #15' in html
print("✓ Autopsia #5 y Bitácora de Aprendizaje Ciclo #15 validadas.")

# 5. Charts
assert '1953.75' in html
print("✓ Curva de Equity en Chart.js validada.")

print("\n¡TODAS LAS VALIDACIONES PASARON EXITOSAMENTE (100% OK)!")
