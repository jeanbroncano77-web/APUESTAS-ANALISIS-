import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Winrate section
wr_start = text.find('id="view-container-winrate"')
wr_end = text.find('</div> <!-- Fin de view-container-winrate -->')
if wr_start != -1:
    print("=== WINRATE SECTION PREVIEW ===")
    print(text[wr_start:wr_start+3000])

# Autocorrect section
ac_start = text.find('id="view-container-autocorrect"')
ac_end = text.find('</div> <!-- Fin de view-container-autocorrect -->')
if ac_start != -1:
    print("\n=== AUTOCORRECT SECTION PREVIEW ===")
    print(text[ac_start:ac_start+3000])
