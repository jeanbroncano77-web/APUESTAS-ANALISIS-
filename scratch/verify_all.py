# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

casos = re.findall(r'CASO DE [^\n<]+', text)
print("Casos found:", set(casos[:10]))

reglas = re.findall(r'REGLA [^\n<]+', text)
print("Reglas found:", set(reglas[:10]))

ciclos = re.findall(r'CICLO [^\n<]+', text)
print("Ciclos found:", set(ciclos[:10]))
