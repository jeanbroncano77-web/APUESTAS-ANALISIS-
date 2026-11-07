with open('scratch/sample_switcher.html', 'r', encoding='utf-8') as f:
    lines = [f.readline() for _ in range(70)]

print("".join(lines))
