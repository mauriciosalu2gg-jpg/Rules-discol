import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the enter-btn hover and styling, and enter-logo
old_css_start = "    .enter-content {"
old_css_end = "    .nav {"
css_pattern = re.compile(re.escape(old_css_start) + r".*?" + re.escape(old_css_end), re.DOTALL)

new_css = """    .enter-content {
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: fade-up 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) both;
    }

    .enter-logo {
      font-family: 'Playfair Display', serif;
      font-size: 5rem;
      font-weight: 900;
      font-style: italic;
      background: linear-gradient(135deg, #ffd369 0%, #ff85a2 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 15px rgba(255,133,162,0.4));
      margin-top: 10px;
      margin-bottom: 10px;
      animation: pulse-glow 3s infinite alternate;
    }
    
    @keyframes pulse-glow {
      0% { filter: drop-shadow(0 0 10px rgba(255,133,162,0.3)); transform: scale(1); }
      100% { filter: drop-shadow(0 0 25px rgba(255,133,162,0.6)); transform: scale(1.02); }
    }

    .divider {
      margin: 30px 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 15px;
    }
    .divider::before, .divider::after {
      content: '';
      width: 50px;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255,211,105,0.5), transparent);
    }
    .divider span {
      color: rgba(255,211,105,0.7);
      font-size: 0.6rem;
      letter-spacing: 2px;
    }

    #enter-btn {
      background: rgba(20, 10, 30, 0.6);
      border: 1px solid rgba(255,133,162,0.3);
      color: var(--white);
      padding: 16px 40px;
      font-size: 0.95rem;
      font-family: 'Nunito', sans-serif;
      font-weight: 700;
      border-radius: 100px;
      cursor: pointer;
      transition: all 0.3s ease;
      letter-spacing: 0.15em;
      backdrop-filter: blur(5px);
      box-shadow: 0 0 20px rgba(255,133,162,0.1);
      text-transform: uppercase;
    }

    #enter-btn:hover {
      background: rgba(255,133,162,0.15);
      border-color: rgba(255,133,162,0.8);
      box-shadow: 0 0 30px rgba(255,133,162,0.4);
      transform: scale(1.05);
    }

    /* ─── Nav ─── */
    .nav {"""

html = css_pattern.sub(new_css, html)

# 2. Fix the HTML structure of the enter screen to match the screenshot exactly
old_html_start = '<div id="enter-screen">'
old_html_end = '<!-- ── Ambient Audio ── -->'
html_pattern = re.compile(re.escape(old_html_start) + r".*?" + re.escape(old_html_end), re.DOTALL)

new_html = """<div id="enter-screen">
  <!-- CSS stars background to match exactly -->
  <div style="position:absolute; inset:0; background: url('data:image/svg+xml;utf8,<svg width=\\'200\\' height=\\'200\\' xmlns=\\'http://www.w3.org/2000/svg\\'><circle cx=\\'20\\' cy=\\'20\\' r=\\'0.5\\' fill=\\'%23fff\\' opacity=\\'0.3\\'/><circle cx=\\'100\\' cy=\\'80\\' r=\\'1\\' fill=\\'%23ff85a2\\' opacity=\\'0.2\\'/><circle cx=\\'160\\' cy=\\'150\\' r=\\'0.5\\' fill=\\'%23ffd369\\' opacity=\\'0.4\\'/><circle cx=\\'50\\' cy=\\'180\\' r=\\'0.8\\' fill=\\'%23fff\\' opacity=\\'0.1\\'/></svg>') repeat; opacity: 0.5; pointer-events: none;"></div>
  
  <div class="enter-content">
    <div style="font-size:0.65rem; letter-spacing:0.4em; color:rgba(255,255,255,0.5); text-transform:uppercase;">✦ Servidor Oficial ✦</div>
    
    <div class="enter-logo">Umas community</div>
    
    <div style="font-style:italic; font-family:'Playfair Display', serif; letter-spacing:0.05em; color:rgba(255,255,255,0.7); font-size:1.1rem;">— Bajo la luna y los cerezos —</div>
    
    <div class="divider">
      <span>✦ ✦ ✦</span>
    </div>
    
    <button id="enter-btn">Entrar al Reglamento</button>
    
    <div style="margin-top: 30px; font-size: 0.65rem; color: rgba(255,255,255,0.3); letter-spacing: 0.05em; max-width: 350px; line-height: 1.6;">
      No está afiliado con Cygames, ni como server extra o de soporte a Umamusume.<br>Solo un servidor de comunidad externo.
    </div>
  </div>
</div>

<!-- ── Ambient Audio ── -->"""

html = html_pattern.sub(new_html, html)

# 3. Increase the transition smoothness for the enter screen
html = html.replace('transition: opacity 0.8s ease;', 'transition: opacity 1.8s ease-in-out;')
html = html.replace('transition: opacity 2.5s ease-in-out;', 'transition: opacity 1.8s ease-in-out;')

# Adjust the javascript timeouts to match 1.8s fade out
old_js = """    // 3. Animación del título hero
    setTimeout(() => {
      if (heroOverlay) heroOverlay.classList.add('start-anim');
    }, 1500);

    // 4. Eliminar del DOM y arrancar reveal
    setTimeout(() => {
      if (enterScreen && enterScreen.parentNode) {
        enterScreen.parentNode.removeChild(enterScreen);
      }
      document.querySelectorAll('.reveal, .stagger').forEach(el => io.observe(el));
    }, 2800);"""
new_js = """    // 3. Animación del título hero
    setTimeout(() => {
      if (heroOverlay) heroOverlay.classList.add('start-anim');
    }, 800);

    // 4. Eliminar del DOM y arrancar reveal
    setTimeout(() => {
      if (enterScreen && enterScreen.parentNode) {
        enterScreen.parentNode.removeChild(enterScreen);
      }
      document.querySelectorAll('.reveal, .stagger').forEach(el => io.observe(el));
    }, 1800);"""
html = html.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Complete!")
