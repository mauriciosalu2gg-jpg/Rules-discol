import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_logo_css = """
    .enter-logo {
      font-family: 'Playfair Display', serif;
      font-size: 4.5rem;
      font-weight: 900;
      color: #fff;
      text-shadow: 0 0 20px rgba(255,255,255,0.4), 0 0 40px rgba(255,204,77,0.2);
      margin-bottom: 5px;
      animation: pulse-glow 3s infinite alternate;
    }
    @keyframes pulse-glow {
      0% { filter: drop-shadow(0 0 10px rgba(255,255,255,0.3)); transform: scale(1); }
      100% { filter: drop-shadow(0 0 25px rgba(255,255,255,0.6)); transform: scale(1.02); }
    }
"""
html = re.sub(r'\.enter-logo\s*\{[^}]*\}', new_logo_css.strip(), html)

new_btn_css = """
    #enter-btn {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255,255,255,0.3);
      color: var(--white);
      padding: 16px 56px;
      font-size: 1.1rem;
      font-family: 'Nunito', sans-serif;
      font-weight: 700;
      border-radius: 100px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      letter-spacing: 0.1em;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      text-transform: uppercase;
    }

    #enter-btn:hover {
      background: rgba(255,255,255,0.95);
      color: #0f0914;
      box-shadow: 0 0 40px rgba(255,255,255,0.8);
      transform: translateY(-2px);
    }
"""

html = re.sub(r'#enter-btn\s*\{[^}]*\}\s*#enter-btn:hover\s*\{[^}]*\}', new_btn_css.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated enter CSS")
