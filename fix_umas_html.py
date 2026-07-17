import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Video sources to HQ
html = html.replace('bg-optimized.webm', 'bg-hq.webm')
html = html.replace('bg-optimized.mp4', 'bg-hq.mp4')

# 2. Text and Disclaimer in Enter Screen
old_enter_content = """<div class="enter-logo">✦ Alero ✦</div>
    <p>Sumérgete en la montaña</p>
    <button id="enter-btn">Entrar al Reglamento</button>"""
new_enter_content = """<div class="enter-logo">✦ Umas community ✦</div>
    <p>Bajo la luna y los cerezos</p>
    <button id="enter-btn">Entrar al Reglamento</button>
    <div style="margin-top: 25px; font-size: 0.75rem; color: rgba(255,255,255,0.4); max-width: 400px; text-align: center; line-height: 1.4;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume, solo un servidor de comunidad externo.
    </div>"""
html = html.replace(old_enter_content, new_enter_content)

# Update navbar logo too if they want
html = html.replace('<div class="nav-logo"><span></span> Alero</div>', '<div class="nav-logo"><span></span> Umas community</div>')

# 3. Colors to more purple
html = re.sub(r'--bg:\s*#[0-9a-fA-F]+;', '--bg: #150926;', html)
html = re.sub(r'--surface:\s*rgba\([^)]+\);', '--surface: rgba(28, 14, 46, 0.65);', html)
html = html.replace('rgba(8,5,14,0.35)', 'rgba(21, 9, 38, 0.4)')
html = html.replace('rgba(8,5,14,0.65)', 'rgba(21, 9, 38, 0.85)') # enter screen background

# 4. Smoother transition
html = html.replace('transition: opacity 0.8s ease;', 'transition: opacity 2.5s ease-in-out;')

# 5. Fix Javascript delays for the new 2.5s transition
html = html.replace('setTimeout(() => {\n      if (heroOverlay) heroOverlay.classList.add(\'start-anim\');\n    }, 300);', 
                    'setTimeout(() => {\n      if (heroOverlay) heroOverlay.classList.add(\'start-anim\');\n    }, 1500);')
html = html.replace('}, 850);', '}, 2800);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML for Umas community, colors, and smooth transition")
