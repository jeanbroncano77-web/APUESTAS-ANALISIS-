import subprocess

out = subprocess.check_output(['git', 'show', 'f195ebe:index.html'], encoding='utf-8')

# Search for '<div class="match-switcher"'
idx = out.find('<div class="match-switcher"')
print("Found <div class=\"match-switcher\" at:", idx)
if idx != -1:
    print(out[idx:idx+2500])
