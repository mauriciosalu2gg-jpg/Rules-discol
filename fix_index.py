import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix .reveal animations (no scale, faster, smoother)
reveal_css = """
    /* ─── Reveal animations ─── */
    .reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .reveal.in { opacity: 1; transform: translateY(0); }

    .stagger > * {
      opacity: 0;
      transform: translateY(15px);
      transition: opacity 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
"""
html = re.sub(r'/\*\s*───\s*Reveal animations\s*───\s*\*/.*?\.stagger\.in\s*>\s*\*\s*\{\s*opacity:\s*1;\s*transform:\s*translateY\(0\)\s*scale\(1\);\s*\}', reveal_css.strip(), html, flags=re.DOTALL)


# 2. Fix hover lag / delay
html = re.sub(r'transition:\s*all\s*0\.[34]s\s*ease;\s*transition-delay:\s*0\.0[5-9]s;', 'transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);', html)
html = re.sub(r'transition:\s*all\s*0\.[34]s\s*ease(?:-out)?;', 'transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);', html)

# 3. Add audio to Enter logic
# We need to find the <audio> element or add it if not exists.
if '<audio id="ambient-audio"' not in html:
    html = html.replace('</body>', '  <audio id="ambient-audio" src="ambient.mp3" loop></audio>\n</body>')

enter_js_new = """
  // ── Enter logic ──
  const enterBtn = document.getElementById('enter-btn');
  const enterScreen = document.getElementById('enter-screen');
  const ambientAudio = document.getElementById('ambient-audio');

  enterBtn.addEventListener('click', () => {
    // Play audio smoothly
    if(ambientAudio) {
      ambientAudio.volume = 0;
      ambientAudio.play().then(() => {
        let vol = 0;
        let fade = setInterval(() => {
          vol += 0.05;
          if (vol >= 0.5) {
            clearInterval(fade);
          } else {
            ambientAudio.volume = vol;
          }
        }, 100);
      }).catch(e => console.log('Audio autoplay blocked', e));
    }

    enterScreen.style.opacity = '0';
    enterScreen.style.pointerEvents = 'none';
    setTimeout(() => {
      enterScreen.remove();
      // start animations
      document.querySelectorAll('.reveal, .stagger').forEach(el => io.observe(el));
    }, 800);
  });
"""
html = re.sub(r'// ── Enter logic ──.*?setTimeout\(\(\) => \{\s*enterScreen\.remove\(\);\s*// start animations\s*document\.querySelectorAll\(\'\.reveal, \.stagger\'\)\.forEach\(el => io\.observe\(el\)\);\s*\}, 800\);\s*}\);', enter_js_new.strip(), html, flags=re.DOTALL)

# 4. Remove io.observe on load because it should only happen on enter click
# Wait, let's just make sure the io.observe loop at the end is removed or commented out so it relies only on enter logic
html = re.sub(r"document\.querySelectorAll\('\.reveal, \.stagger'\)\.forEach\(el => io\.observe\(el\)\);\s*</script>", "</script>", html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated basic logic")
