with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
style_match = re.search(r'<style>([\s\S]*?)</style>', text)
if style_match:
    css = style_match.group(1)
    print("CSS length:", len(css))
    
    # Check key classes
    classes_to_check = [
        'view-mode-nav', 'btn-view-mode', 'badge-winrate-pill',
        'spotlight-banner', 'spotlight-title', 'spotlight-prob-badge',
        'winrate-kpi-grid', 'kpi-card', 'kpi-card-emerald', 'kpi-card-gold',
        'audit-filter-bar', 'btn-filter-audit', 'audit-table-wrap',
        'audit-table', 'audit-row', 'badge-status', 'badge-win', 'badge-loss',
        'autolearn-hero', 'autopsy-card', 'autopsy-header', 'autopsy-split',
        'box-flaw', 'box-fix', 'agent-showcase-card'
    ]
    for c in classes_to_check:
        print(f".{c}: {('.' + c) in css}")
