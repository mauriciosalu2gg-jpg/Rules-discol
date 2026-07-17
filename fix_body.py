import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(body\s*\{[^}]*?background:)\s*var\(--bg\);', r'\1 transparent;', html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated body background")
