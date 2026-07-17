import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the stars div (the old div had style="position:absolute; inset:0; background: url('data:image/svg+xml;... )
# I will just find the div that contains "data:image/svg+xml" inside enter-screen and replace it.
svg_div_pattern = re.compile(r'<div style="position:absolute; inset:0; background: url\(\'data:image/svg\+xml;utf8,[^>]+\) repeat; opacity: 0.5; pointer-events: none;"></div>')
html = svg_div_pattern.sub('<div class="space-stars"></div>', html)

# 2. Fix hero-title animation (remove translateY, set final opacity to 0.55)
old_title_in = """    @keyframes title-in {
      from { opacity: 0; transform: translateY(30px); }
      to   { opacity: 1; transform: translateY(0); }
    }"""
new_title_in = """    @keyframes title-in {
      from { opacity: 0; transform: translateY(0); }
      to   { opacity: 0.55; transform: translateY(0); }
    }"""
html = html.replace(old_title_in, new_title_in)

# Also fix the base .hero-title so it doesn't have translateY(30px)
html = html.replace('transform: translateY(30px);', 'transform: translateY(0);')

# 3. Ensure the disclaimer text is perfectly centered with auto margin
old_disclaimer = """<div style="margin-top: 30px; font-size: 0.65rem; color: rgba(255,255,255,0.4); letter-spacing: 0.05em; max-width: 450px; line-height: 1.6; text-align: center;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume.<br>Solo un servidor de comunidad externo sin fines de lucro bajo Uso Legítimo (Fair Use).<br>No afiliado a Discord Inc.
    </div>"""
new_disclaimer = """<div style="margin: 30px auto 0 auto; font-size: 0.65rem; color: rgba(255,255,255,0.45); letter-spacing: 0.05em; max-width: 500px; line-height: 1.7; text-align: center; display: block;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume.<br>Solo un servidor de comunidad externo sin fines de lucro bajo Uso Legítimo (Fair Use).<br>No afiliado a Discord Inc.
    </div>"""
html = html.replace(old_disclaimer, new_disclaimer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied final fixes")
