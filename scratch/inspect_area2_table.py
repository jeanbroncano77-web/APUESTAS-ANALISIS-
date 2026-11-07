# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('col-id">#186')
if pos != -1:
    print(text[pos-100:pos+1500])
else:
    pos2 = text.find('#186')
    print("Pos2:", pos2)
    print(text[pos2-100:pos2+500])

