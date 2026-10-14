with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="slip-drawer"')
print("Found pos:", pos)
if pos != -1:
    start = text.rfind('<div', 0, pos)
    print("Start:", start, text[start:pos+30])
    # Let's find end
    # How many nested divs inside?
    end = text.find('<!-- Embedded Raw JSON', pos)
    print("End before script:", end)
    print("Content:\n", text[start:end])
