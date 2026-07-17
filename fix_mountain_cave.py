import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change mountain-cave background to be transparent
old_bg = r"rgba\(8,5,14,0\.75\) 0%, rgba\(8,5,14,0\.95\) 10%, rgba\(8,5,14,1\) 20%"
new_bg = r"rgba(8,5,14,0.4) 0%, rgba(8,5,14,0.7) 10%, rgba(8,5,14,0.85) 100%"

html = re.sub(old_bg, new_bg, html)

# Also let's check body background
# body { background: var(--bg); ... }
html = re.sub(r'body\s*\{\s*background:\s*var\(--bg\);', 'body {\n      background: transparent;', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated mountain-cave background")
