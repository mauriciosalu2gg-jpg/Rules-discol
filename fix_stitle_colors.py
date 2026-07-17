import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .stitle h2
old_stitle_h2 = """    .stitle h2 {
      font-family: 'Playfair Display', serif;
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--white);
      letter-spacing: -0.01em;
    }"""
new_stitle_h2 = """    .stitle h2 {
      font-family: 'Playfair Display', serif;
      font-size: 1.55rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--theme-c1, #fff), var(--theme-c2, #a872e8));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.01em;
    }"""
html = html.replace(old_stitle_h2, new_stitle_h2)

# 2. Update .stitle::after
old_stitle_after = """    .stitle::after {
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, rgba(217,124,191,0.3), transparent);
    }"""
new_stitle_after = """    .stitle::after {
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, var(--theme-c1, rgba(217,124,191,0.5)), transparent);
      transform-origin: left;
      transform: scaleX(0);
      transition: transform 1.2s cubic-bezier(0.22, 1, 0.36, 1) 0.3s;
    }
    
    .stitle.reveal.in::after {
      transform: scaleX(1);
    }"""
html = html.replace(old_stitle_after, new_stitle_after)

# 3. Add variables to sections
# I will just add a <style> block before the end of </head> to assign variables to IDs
style_vars = """
    /* Section Color Variations */
    #conducta { --theme-c1: #ffb8c6; --theme-c2: #ff85a2; }
    #contenido { --theme-c1: #ff85a2; --theme-c2: #d97cbf; }
    #privacidad { --theme-c1: #d97cbf; --theme-c2: #a872e8; }
    #moderacion { --theme-c1: #a872e8; --theme-c2: #8c72e8; }
    #puntos { --theme-c1: #8c72e8; --theme-c2: #728ce8; }
    #sanciones { --theme-c1: #728ce8; --theme-c2: #72a8e8; }
    #legal { --theme-c1: #72a8e8; --theme-c2: #72cce8; }
    #apelacion { --theme-c1: #72cce8; --theme-c2: #72e8d9; }
"""
html = html.replace("  </style>", style_vars + "  </style>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated stitle styles and animations")
