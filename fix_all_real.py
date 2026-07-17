import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the stars movement (which was added but maybe not correctly targeted or the animation doesn't look moving)
# We need to find `.space-stars { ... }` and change it to the new one that actually moves the background position.
old_stars = """    .space-stars {
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
    }"""
new_stars = """    .space-stars {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      background: url('data:image/svg+xml;utf8,<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="0.5" fill="%23fff" opacity="0.4"/><circle cx="100" cy="80" r="1.5" fill="%23ff85a2" opacity="0.3"/><circle cx="160" cy="150" r="1" fill="%23ffd369" opacity="0.5"/><circle cx="50" cy="180" r="0.8" fill="%23fff" opacity="0.2"/><circle cx="180" cy="30" r="0.5" fill="%23a872e8" opacity="0.4"/><circle cx="10" cy="120" r="1.2" fill="%23ff85a2" opacity="0.2"/></svg>') repeat;
      opacity: 0.6;
      background-size: 200px 200px;
      pointer-events: none;
      animation: move-stars 60s linear infinite;
    }
    @keyframes move-stars {
      0% { background-position: 0 0; }
      100% { background-position: -400px 400px; }
    }"""
if old_stars in html:
    html = html.replace(old_stars, new_stars)
else:
    print("WARNING: Could not find .space-stars in HTML!")

# 2. Fix the enter-btn (which currently has the broken syntax and old colors)
btn_start = "    #enter-btn {"
btn_end = "    </style>"
btn_pattern = re.compile(re.escape(btn_start) + r".*?" + re.escape(btn_end), re.DOTALL)
new_btn = """    #enter-btn {
      background: rgba(30, 15, 45, 0.7);
      border: 1px solid rgba(255,133,162,0.4);
      color: var(--white);
      padding: 16px 56px;
      font-size: 1.1rem;
      font-family: 'Nunito', sans-serif;
      font-weight: 700;
      border-radius: 100px;
      cursor: pointer;
      transition: all 0.4s ease-in-out;
      letter-spacing: 0.1em;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      text-transform: uppercase;
      margin-top: 10px;
    }

    #enter-btn:hover {
      background: rgba(255,133,162,0.25);
      border-color: rgba(255,133,162,0.9);
      color: #fff;
      box-shadow: 0 0 35px rgba(255,133,162,0.5);
      transform: translateY(-2px) scale(1.05);
    }
    </style>"""
if btn_pattern.search(html):
    html = btn_pattern.sub(new_btn, html)
else:
    print("WARNING: Could not find enter-btn block!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied successfully")
