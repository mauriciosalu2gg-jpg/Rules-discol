import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_btn = """    #enter-btn {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255,255,255,0.3);
      color: var(--white);
      padding: 16px 56px;
      font-size: 1.1rem;
      font-family: 'Nunito', sans-serif;
      font-weight: 700;
      border-radius: 100px;
      cursor: pointer;
      transition: all 0.05s cubic-bezier(0.25, 0.46, 0.45, 0.94)
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
    }"""
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
      transition: all 0.5s ease-in-out;
      letter-spacing: 0.1em;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      text-transform: uppercase;
    }

    #enter-btn:hover {
      background: rgba(255,133,162,0.25);
      border-color: rgba(255,133,162,0.9);
      color: #fff;
      box-shadow: 0 0 35px rgba(255,133,162,0.5);
      transform: translateY(-2px) scale(1.05);
    }"""

html = html.replace(old_btn, new_btn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated enter btn")
