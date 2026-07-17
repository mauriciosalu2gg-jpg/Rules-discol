import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .reveal and .stagger CSS to use animations instead of transitions
old_reveal_css = """    /* ─── Reveal animations ─── */
    .reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1), transform var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .reveal.in { opacity: 1; transform: translateY(0); }

    .stagger > * {
      opacity: 0;
      transform: translateY(15px);
      transition: opacity var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1), transform var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .stagger.in > *:nth-child(1) { transition-delay: 0.00s; }
    .stagger.in > *:nth-child(2) { transition-delay: 0.04s; }
    .stagger.in > *:nth-child(3) { transition-delay: 0.08s; }
    .stagger.in > *:nth-child(4) { transition-delay: 0.12s; }
    .stagger.in > *:nth-child(5) { transition-delay: 0.16s; }
    .stagger.in > *:nth-child(6) { transition-delay: 0.20s; }
    .stagger.in > *:nth-child(7) { transition-delay: 0.24s; }
    .stagger.in > *:nth-child(8) { transition-delay: 0.28s; }
    .stagger.in > * { opacity: 1; transform: translateY(0); }"""

new_reveal_css = """    /* ─── Reveal animations ─── */
    .reveal {
      opacity: 0;
    }
    .reveal.in {
      animation: reveal-in var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    }
    @keyframes reveal-in {
      from { opacity: 0; transform: translateY(30px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .stagger > * {
      opacity: 0;
    }
    .stagger.in > * {
      animation: stagger-in var(--dynamic-dur) cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    }
    @keyframes stagger-in {
      from { opacity: 0; transform: translateY(20px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .stagger.in > *:nth-child(1) { animation-delay: 0.00s; }
    .stagger.in > *:nth-child(2) { animation-delay: 0.08s; }
    .stagger.in > *:nth-child(3) { animation-delay: 0.16s; }
    .stagger.in > *:nth-child(4) { animation-delay: 0.24s; }
    .stagger.in > *:nth-child(5) { animation-delay: 0.32s; }
    .stagger.in > *:nth-child(6) { animation-delay: 0.40s; }
    .stagger.in > *:nth-child(7) { animation-delay: 0.48s; }
    .stagger.in > *:nth-child(8) { animation-delay: 0.56s; }
    .stagger.in > *:nth-child(9) { animation-delay: 0.64s; }
    .stagger.in > *:nth-child(10) { animation-delay: 0.72s; }
    .stagger.in > *:nth-child(11) { animation-delay: 0.80s; }
    .stagger.in > *:nth-child(12) { animation-delay: 0.88s; }
    .stagger.in > *:nth-child(13) { animation-delay: 0.96s; }
    .stagger.in > *:nth-child(14) { animation-delay: 1.04s; }
    .stagger.in > *:nth-child(15) { animation-delay: 1.12s; }
"""
if old_reveal_css in html:
    html = html.replace(old_reveal_css, new_reveal_css)
else:
    print("Warning: old reveal css not found")

# 2. Add .stagger to pts-bars and legal-table tbody, and .reveal to callouts
html = html.replace('<div class="pts-bars" id="pts-bars">', '<div class="pts-bars stagger" id="pts-bars">')
html = html.replace('<tbody class="legal-table">', '<tbody class="legal-table stagger">')
html = html.replace('<div class="callout">', '<div class="callout reveal">')
html = html.replace('<div class="callout warning">', '<div class="callout warning reveal">')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Animations fixed properly")
