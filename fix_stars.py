import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the enter-screen transition
old_css_es = "transition: opacity 0.05s ease"
new_css_es = "transition: opacity 2.5s ease-in-out;"
html = html.replace(old_css_es, new_css_es)

# 2. Add animation to the stars div
# Currently the div is: <div style="position:absolute; inset:0; background: url('data:image/svg+xml;... repeat; opacity: 0.5; pointer-events: none;"></div>
# We can give it a class or just add an inline animation? No, better add a class and keyframes.
old_stars_div = r"<div style=\"position:absolute; inset:0; background: url\('data:image/svg\+xml;utf8,[^']+'\) repeat; opacity: 0.5; pointer-events: none;\"></div>"
new_stars_div = '<div class="space-stars"></div>'
html = re.sub(old_stars_div, new_stars_div, html)

# Add the CSS for .space-stars and better logo animation
old_enter_content_css = "    .enter-content {"
new_enter_css = """    .space-stars {
      position: absolute;
      inset: -50%;
      width: 200%;
      height: 200%;
      background: url('data:image/svg+xml;utf8,<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="0.5" fill="%23fff" opacity="0.4"/><circle cx="100" cy="80" r="1.5" fill="%23ff85a2" opacity="0.3"/><circle cx="160" cy="150" r="1" fill="%23ffd369" opacity="0.5"/><circle cx="50" cy="180" r="0.8" fill="%23fff" opacity="0.2"/><circle cx="180" cy="30" r="0.5" fill="%23a872e8" opacity="0.4"/><circle cx="10" cy="120" r="1.2" fill="%23ff85a2" opacity="0.2"/></svg>') repeat;
      opacity: 0.6;
      pointer-events: none;
      animation: rotate-stars 200s linear infinite;
    }
    @keyframes rotate-stars {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    .enter-content {"""
html = html.replace(old_enter_content_css, new_enter_css)

# Update the pulse-glow animation to be smoother and bigger
old_pulse = """    @keyframes pulse-glow {
      0% { filter: drop-shadow(0 0 10px rgba(255,133,162,0.3)); transform: scale(1); }
      100% { filter: drop-shadow(0 0 25px rgba(255,133,162,0.6)); transform: scale(1.02); }
    }"""
new_pulse = """    @keyframes pulse-glow {
      0% { filter: drop-shadow(0 0 15px rgba(255,133,162,0.3)); transform: scale(1); }
      50% { filter: drop-shadow(0 0 30px rgba(255,211,105,0.5)); transform: scale(1.03); }
      100% { filter: drop-shadow(0 0 15px rgba(255,133,162,0.3)); transform: scale(1); }
    }"""
html = html.replace(old_pulse, new_pulse)

# Fix the enter logo animation line
html = html.replace("animation: pulse-glow 3s infinite alternate;", "animation: pulse-glow 4s ease-in-out infinite;")

# Update disclaimer text
old_disclaimer = """<div style="margin-top: 30px; font-size: 0.65rem; color: rgba(255,255,255,0.3); letter-spacing: 0.05em; max-width: 350px; line-height: 1.6;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume.<br>Solo un servidor de comunidad externo.
    </div>"""
new_disclaimer = """<div style="margin-top: 30px; font-size: 0.65rem; color: rgba(255,255,255,0.4); letter-spacing: 0.05em; max-width: 450px; line-height: 1.6; text-align: center;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume.<br>Solo un servidor de comunidad externo sin fines de lucro bajo Uso Legítimo (Fair Use).<br>No afiliado a Discord Inc.
    </div>"""
html = html.replace(old_disclaimer, new_disclaimer)

# Check if javascript delay for fade needs adjustment since it's 2.5s transition now
html = html.replace("}, 1800);", "}, 2600);")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated enter screen stars and text")
