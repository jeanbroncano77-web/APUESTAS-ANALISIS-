with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function filterAuditTable')
print("Function pos:", pos)
if pos != -1:
    print(text[pos:pos+1500].encode('ascii', 'ignore').decode())
