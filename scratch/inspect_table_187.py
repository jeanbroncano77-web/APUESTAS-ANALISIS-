# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('AUTOPSIA DE FALLO #14')
print(text[pos+2500:pos+5500])
