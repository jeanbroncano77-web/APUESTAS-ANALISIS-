with open('scratch/update_cartelera_saturday_nov7.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Valencia vs. Real Madrid')
print("Snippet around Valencia vs. Real Madrid:")
print(text[idx-200:idx+600])

