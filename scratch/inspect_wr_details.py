import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

wr_start = text.find('id="view-container-winrate"')
wr_end = text.find('</div> <!-- Fin de view-container-winrate -->')
if wr_start != -1 and wr_end != -1:
    content = text[wr_start:wr_end]
    print(f"Total length of winrate view: {len(content)}")
    print(content[:1500])
    print("\n--- MIDDLE / TABLE PART ---")
    pos_table = content.find('<table')
    if pos_table != -1:
        print(content[pos_table:pos_table+1500])
