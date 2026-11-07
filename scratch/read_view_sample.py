with open('scratch/sample_match_view.html', 'r', encoding='utf-8') as f:
    lines = [f.readline() for _ in range(120)]

print("".join(lines))
