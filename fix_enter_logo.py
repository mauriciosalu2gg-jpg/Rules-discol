import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the enter-logo gradient
old_logo_css = """    .enter-logo {
      font-family: 'Playfair Display', serif;
      font-size: 4.5rem;
      font-weight: 900;
      color: #fff;
      text-shadow: 0 0 20px rgba(255,255,255,0.4), 0 0 40px rgba(255,204,77,0.2);"""
new_logo_css = """    .enter-logo {
      font-family: 'Playfair Display', serif;
      font-size: 4.5rem;
      font-weight: 900;
      background: linear-gradient(135deg, #ffd369 0%, #ff85a2 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 20px rgba(255,133,162,0.3));"""
html = html.replace(old_logo_css, new_logo_css)

# Update the content from "✦ Umas community ✦" to add the tiny stars like the screenshot
# The screenshot has:
# • SERVIDOR OFICIAL •
# Umas community
# — Bajo la luna y los cerezos —
old_enter = """<div class="enter-logo">✦ Umas community ✦</div>
    <p>Bajo la luna y los cerezos</p>"""
new_enter = """<div style="font-size:0.75rem; letter-spacing:0.3em; color:rgba(255,255,255,0.6); margin-bottom:15px;">✦ SERVIDOR OFICIAL ✦</div>
    <div class="enter-logo">Umas community</div>
    <p style="font-style:italic; font-family:'Playfair Display', serif; letter-spacing:0.05em; color:rgba(255,255,255,0.8); text-transform:none;">— Bajo la luna y los cerezos —</p>"""
html = html.replace(old_enter, new_enter)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated enter logo styling")
