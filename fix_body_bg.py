with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('body {\n      font-family: \'Nunito\', sans-serif;\n      background: transparent;', 'body {\n      font-family: \'Nunito\', sans-serif;\n      background: var(--bg);')
html = html.replace('background: transparent;', 'background: var(--bg);') # fallback
html = html.replace('background: #0a0612;', 'background: transparent;') # make sure hero-wrapper itself doesn't hide video, wait hero-wrapper should have transparent background.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed body background")
