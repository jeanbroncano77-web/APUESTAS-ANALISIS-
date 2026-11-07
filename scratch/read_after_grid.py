with open('scratch/sample_match_view.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find after analytics-grid-3
idx = text.find('analytics-grid-3')
if idx != -1:
    end_grid = text.find('</div>\n            </div>\n\n            <!--', idx)
    print("Found after grid at:", end_grid)
    if end_grid != -1:
        print(text[end_grid:end_grid+2000])
