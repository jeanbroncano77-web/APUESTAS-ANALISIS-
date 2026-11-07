import subprocess

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')

idx_tab0 = out.find('id="tab-0"')
idx_match0 = out.find('id="match-0"')

print("Length between tab-0 and match-0:", idx_match0 - idx_tab0)
print(out[idx_tab0:idx_match0])
