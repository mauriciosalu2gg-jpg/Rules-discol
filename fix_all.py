import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. hero-wrapper: quitar aria-hidden y asegurarse que el video sea visible ───
html = html.replace('<div class="hero-wrapper" aria-hidden="true">', '<div class="hero-wrapper">')

# ─── 2. Reemplazar CSS del hero-wrapper - fondo negro como fallback ───
old_hero_css = r'\.hero-wrapper \{[\s\S]*?pointer-events: none; /\* Let clicks pass through \*/\s*\}'
new_hero_css = '''    .hero-wrapper {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      background: #0a0612;
    }'''
html = re.sub(old_hero_css, new_hero_css, html)

# ─── 3. Reemplazar CSS del #hero-video para que llene bien ───
old_video_css = r'/\* ─── Hero Video ─── \*/\s*#hero-video \{[\s\S]*?\}'
new_video_css = '''    /* ─── Hero Video ─── */
    #hero-video {
      position: absolute;
      top: 0; left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      filter: brightness(0.85) saturate(1.1);
      will-change: transform;
    }'''
html = re.sub(old_video_css, new_video_css, html)

# ─── 4. hero-overlay: sutil, no opaco ───
old_overlay = r'\.hero-overlay \{[\s\S]*?\}'
new_overlay = '''    .hero-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.05) 0%,
        rgba(0,0,0,0.15) 60%,
        rgba(0,0,0,0.5) 100%
      );
      pointer-events: none;
    }'''
html = re.sub(old_overlay, new_overlay, html, count=1)

# ─── 5. mountain-cave: fondo semi-transparente para que el video siga viéndose ───
old_cave = r'\.mountain-cave \{[\s\S]*?padding-top: 80px;\s*\}'
new_cave = '''    .mountain-cave {
      background: rgba(8,5,14,0.78);
      position: relative;
      padding-top: 80px;
    }'''
html = re.sub(old_cave, new_cave, html)

# ─── 6. body background transparente ───
html = re.sub(r'(body\s*\{[^}]*?)background:\s*[^;]+;', r'\1background: transparent;', html, count=1)

# ─── 7. Quitar moon-glow y mist (animaciones que hacen lag) ───
html = re.sub(r'\.moon-glow \{[\s\S]*?@keyframes mist-move \{[\s\S]*?\}', '', html, count=1)

# ─── 8. Scroll reveal - quitar rootMargin para que se dispare antes ───
html = html.replace("{ threshold: 0.05, rootMargin: '0px 0px -50px 0px' }", "{ threshold: 0.05 }")

# ─── 9. Quitar transition-delay en stagger para que sea más rápido ───
html = re.sub(r'    \.stagger\.in > \*:nth-child\(1\) \{ transition-delay: 0\.00s; \}\n.*?    \.stagger\.in > \*:nth-child\(8\) \{ transition-delay: 0\.56s; \}',
'    .stagger.in > *:nth-child(1) { transition-delay: 0.00s; }\n    .stagger.in > *:nth-child(2) { transition-delay: 0.04s; }\n    .stagger.in > *:nth-child(3) { transition-delay: 0.08s; }\n    .stagger.in > *:nth-child(4) { transition-delay: 0.12s; }\n    .stagger.in > *:nth-child(5) { transition-delay: 0.16s; }\n    .stagger.in > *:nth-child(6) { transition-delay: 0.20s; }\n    .stagger.in > *:nth-child(7) { transition-delay: 0.24s; }\n    .stagger.in > *:nth-child(8) { transition-delay: 0.28s; }',
html, flags=re.DOTALL)

# ─── 10. Video: forzar reproducción en JS ───
old_enter_js = "  enterBtn.addEventListener('click', () => {"
new_enter_js = """  // Forzar reproducción del video al cargar
  const heroVid = document.getElementById('hero-video');
  if (heroVid) {
    heroVid.muted = true;
    heroVid.play().catch(() => {});
  }

  enterBtn.addEventListener('click', () => {"""
html = html.replace(old_enter_js, new_enter_js, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("All fixes applied")
