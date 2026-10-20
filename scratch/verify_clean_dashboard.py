with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check Area 2
vr_start = text.find('<div id="view-container-winrate"')
vr_end = text.find('<!-- Fin de view-container-winrate -->')
vr_content = text[vr_start:vr_end]

print("Area 2 checks:")
print("  - Container found:", vr_start != -1 and vr_end != -1)
print("  - Search input present:", 'id="audit-search-input"' in vr_content)
print("  - Search badge present:", 'id="audit-count-badge"' in vr_content)
print("  - Chart equity canvas:", 'id="chart-equity-curve"' in vr_content)
print("  - Chart category canvas:", 'id="chart-category-winrate"' in vr_content)
print("  - Autopsias wrongly in Area 2:", 'AUTOPSIA #9' in vr_content)
print("  - Rows count:", vr_content.count('class="audit-row'))

# Check Area 3
ac_start = text.find('<div id="view-container-autocorrect"')
ac_end = text.find('<!-- Fin de view-container-autocorrect -->')
ac_content = text[ac_start:ac_end]

print("\nArea 3 checks:")
print("  - Container found:", ac_start != -1 and ac_end != -1)
print("  - Autopsia #9 present:", 'AUTOPSIA #9' in ac_content)
print("  - Caso Ecuabet present:", 'CASO DE ÉXITO & APRENDIZAJE #2' in ac_content)
print("  - Autopsia #7 present:", 'AUTOPSIA #7' in ac_content)
print("  - Autopsia #8 present:", 'AUTOPSIA #8' in ac_content)
print("  - Caso Barcelona present:", 'CASO DE ÉXITO & APRENDIZAJE: FC BARCELONA' in ac_content)
print("  - Calibration table present:", 'Ciclo #' in ac_content)

# Check JS
print("\nJS checks:")
print("  - searchAuditTable defined:", 'function searchAuditTable' in text)
print("  - filterAuditTable defined:", 'function filterAuditTable' in text)
print("  - initWinrateCharts defined:", 'function initWinrateCharts' in text)
