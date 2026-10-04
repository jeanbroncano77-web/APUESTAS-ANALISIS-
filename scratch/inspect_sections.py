import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Check view-container-winrate
pos_wr = text.find('id="view-container-winrate"')
pos_wr_end = text.find('</div> <!-- Fin de view-container-winrate -->')
if pos_wr != -1 and pos_wr_end != -1:
    print("=== VIEW CONTAINER WINRATE (Length: {}) ===".format(pos_wr_end - pos_wr))
    print(text[pos_wr:pos_wr+1500])
    print("...")
    print(text[pos_wr_end-500:pos_wr_end+50])

# Check view-container-autocorrect
pos_ac = text.find('id="view-container-autocorrect"')
pos_ac_end = text.find('</div> <!-- Fin de view-container-autocorrect -->')
if pos_ac != -1 and pos_ac_end != -1:
    print("\n=== VIEW CONTAINER AUTOCORRECT (Length: {}) ===".format(pos_ac_end - pos_ac))
    print(text[pos_ac:pos_ac+1500])
    print("...")
    print(text[pos_ac_end-500:pos_ac_end+50])
