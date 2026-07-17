import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS variable to :root
if ":root {" in html:
    html = html.replace(":root {", ":root {\n      --dynamic-dur: 1.8s;")
else:
    print("Warning: :root not found")

# 2. Replace static 1.2s in .reveal and .stagger with var(--dynamic-dur)
old_reveal = 'transition: opacity 1.2s cubic-bezier(0.25, 0.8, 0.25, 1), transform 1.2s cubic-bezier(0.25, 0.8, 0.25, 1);'
new_reveal = 'transition: opacity var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1), transform var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1);'
html = html.replace(old_reveal, new_reveal)

old_stitle_line = 'transition: transform 1.2s cubic-bezier(0.22, 1, 0.36, 1) 0.3s;'
new_stitle_line = 'transition: transform var(--dynamic-dur) cubic-bezier(0.22, 1, 0.36, 1) 0.3s;'
html = html.replace(old_stitle_line, new_stitle_line)

# 3. Add the JS snippet for Scroll Velocity right before </body> or inside the DOMContentLoaded script
js_script = """
  // ── Dynamic Scroll Speed Animation ──
  let lastScrollY = window.scrollY;
  let ticking = false;
  
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        const currentScrollY = window.scrollY;
        const speed = Math.abs(currentScrollY - lastScrollY);
        lastScrollY = currentScrollY;
        
        // Map scroll speed (0 to ~150) to duration (2.5s to 0.8s)
        // Slower scroll = longer duration (so animations play majestically)
        // Faster scroll = shorter duration (so you don't wait for animations when scrolling fast)
        let duration = 2.5 - (speed * 0.015);
        if (duration < 0.8) duration = 0.8;
        if (duration > 2.5) duration = 2.5;
        
        document.documentElement.style.setProperty('--dynamic-dur', duration + 's');
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
"""
html = html.replace('// ── Active nav highlight (Robust Scroll Listener) ──', js_script + '\n\n  // ── Active nav highlight (Robust Scroll Listener) ──')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Dynamic scroll duration implemented")
