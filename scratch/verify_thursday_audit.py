# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Has #211 in table:', '#211' in text)
print('Has Caso 17:', 'CASO DE ÉXITO & CALIBRACIÓN #17' in text)
print('Has Regla 123:', 'Regla de Oro #123' in text or 'REGLA DE ORO #123' in text)
print('Has Win rate badge 88.1%:', '88.1% WIN' in text)
print('Total file size:', len(text))
