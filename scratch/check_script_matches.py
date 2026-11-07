with open('scratch/update_cartelera_saturday_nov7.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'vs\.\s+[A-Za-z0-9 ]+', text)
print("Matches mentioned in script:", set(matches[:20]))

# find how cards are generated
idx = text.find('Libertad FC')
if idx != -1:
    print("\nSnippet around Libertad FC in update script:")
    print(text[idx-200:idx+400])

