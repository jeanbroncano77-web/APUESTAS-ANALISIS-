import re, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

rows = re.findall(r'<tr class="audit-row[^"]*"[^>]*>.*?</tr>', text, re.DOTALL)
print("=== ROW 92 ===")
print(rows[91])
print("\n=== ROW 96 ===")
print(rows[95])
