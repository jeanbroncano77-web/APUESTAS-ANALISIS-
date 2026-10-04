import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

wr_start = text.find('id="view-container-winrate"')
pos_table = text.find('<table class="audit-table">', wr_start)

print("=== WINRATE HEADER & KPIS ===")
print(text[wr_start:pos_table])
