import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS :root to include --dynamic-delay
html = html.replace('--dynamic-dur: 1.8s;', '--dynamic-dur: 1.8s;\n      --dynamic-delay: 0.08s;')

# 2. Update the JS script
old_js = """        // Map scroll speed (0 to ~150) to duration (2.5s to 0.8s)
        // Slower scroll = longer duration (so animations play majestically)
        // Faster scroll = shorter duration (so you don't wait for animations when scrolling fast)
        let duration = 2.5 - (speed * 0.015);
        if (duration < 0.8) duration = 0.8;
        if (duration > 2.5) duration = 2.5;
        
        document.documentElement.style.setProperty('--dynamic-dur', duration + 's');"""

new_js = """        // Map scroll speed to duration and stagger delay
        let duration = 2.5 - (speed * 0.02);
        let staggerDelay = 0.08 - (speed * 0.001);
        
        // If they scroll extremely fast (speed > 100), animations load almost instantly
        if (duration < 0.15) duration = 0.15;
        if (duration > 2.5) duration = 2.5;
        
        if (staggerDelay < 0.01) staggerDelay = 0.01;
        if (staggerDelay > 0.1) staggerDelay = 0.1;
        
        document.documentElement.style.setProperty('--dynamic-dur', duration + 's');
        document.documentElement.style.setProperty('--dynamic-delay', staggerDelay + 's');"""

html = html.replace(old_js, new_js)

# 3. Update the stagger CSS to use calc
old_stagger = """    .stagger.in > *:nth-child(1) { animation-delay: 0.00s; }
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
    .stagger.in > *:nth-child(15) { animation-delay: 1.12s; }"""

new_stagger = """    .stagger.in > *:nth-child(1) { animation-delay: calc(0 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(2) { animation-delay: calc(1 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(3) { animation-delay: calc(2 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(4) { animation-delay: calc(3 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(5) { animation-delay: calc(4 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(6) { animation-delay: calc(5 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(7) { animation-delay: calc(6 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(8) { animation-delay: calc(7 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(9) { animation-delay: calc(8 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(10) { animation-delay: calc(9 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(11) { animation-delay: calc(10 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(12) { animation-delay: calc(11 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(13) { animation-delay: calc(12 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(14) { animation-delay: calc(13 * var(--dynamic-delay)); }
    .stagger.in > *:nth-child(15) { animation-delay: calc(14 * var(--dynamic-delay)); }"""

html = html.replace(old_stagger, new_stagger)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated aggressive scroll physics")
