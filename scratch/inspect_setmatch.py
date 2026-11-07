with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('function setMatch')
if idx != -1:
    print("setMatch implementation:")
    print(h[idx:idx+1500])
else:
    print("function setMatch not found directly")
