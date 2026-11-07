import subprocess

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')

# Find match-0 start to match-1 start
idx0 = out.find('id="match-0"')
idx1 = out.find('id="match-1"')
print(f"Match-0 length: {idx1 - idx0}")

with open('scratch/sample_match_view.html', 'w', encoding='utf-8') as f:
    f.write(out[idx0:idx1])

print("Written scratch/sample_match_view.html")

# Also find switcher section
idx_sw_start = out.find('class="switcher-grid"')
idx_sw_end = out.find('id="match-0"')
print(f"Switcher section length: {idx_sw_end - idx_sw_start}")
with open('scratch/sample_switcher.html', 'w', encoding='utf-8') as f:
    f.write(out[idx_sw_start:idx_sw_end])
print("Written scratch/sample_switcher.html")
