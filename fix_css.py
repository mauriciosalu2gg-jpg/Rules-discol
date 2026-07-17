import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

correct_reveal_css = """
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
    .stagger.in > *:nth-child(1) { transition-delay: 0.00s; }
    .stagger.in > *:nth-child(2) { transition-delay: 0.08s; }
    .stagger.in > *:nth-child(3) { transition-delay: 0.16s; }
    .stagger.in > *:nth-child(4) { transition-delay: 0.24s; }
    .stagger.in > *:nth-child(5) { transition-delay: 0.32s; }
    .stagger.in > *:nth-child(6) { transition-delay: 0.40s; }
    .stagger.in > *:nth-child(7) { transition-delay: 0.48s; }
    .stagger.in > *:nth-child(8) { transition-delay: 0.56s; }
    .stagger.in > * { opacity: 1; transform: translateY(0); }
"""

html = re.sub(r'/\*\s*───\s*Reveal animations\s*───\s*\*/.*?\.stagger\s*>\s*\*\s*\{[^}]*\}', correct_reveal_css.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed CSS animations")
