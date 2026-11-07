# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Has #199:', '#199' in text)
print('Has Caso 16:', 'CASO DE ÉXITO & CALIBRACIÓN #16' in text)
print('Has Autopsia 15:', 'AUTOPSIA DE FALLO #15' in text)
print('Has Regla 122:', 'Regla de Oro #122' in text or 'REGLA DE ORO #122' in text)
print('Win rate badge:', '87.4% WIN' in text)
print('Total file size:', len(text))
