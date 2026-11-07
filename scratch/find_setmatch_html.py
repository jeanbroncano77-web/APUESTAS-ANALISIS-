import subprocess

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')

idx = out.find('setMatch(0)')
print("Found setMatch(0) at:", idx)
if idx != -1:
    print(out[max(0, idx-300):idx+1500])
