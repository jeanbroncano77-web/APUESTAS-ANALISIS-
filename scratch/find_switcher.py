import subprocess
import re

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')

idx = out.find('switcher-card')
print("Found switcher-card at:", idx)
if idx != -1:
    print(out[max(0, idx-200):idx+800])
