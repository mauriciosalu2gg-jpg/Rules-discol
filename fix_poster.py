import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update hero-wrapper CSS
wrapper_css_old = r'\.hero-wrapper\s*\{\s*position:\s*fixed;\s*top:\s*0;\s*left:\s*0;\s*width:\s*100%;\s*height:\s*100svh;\s*z-index:\s*0;\s*pointer-events:\s*none;\s*\}'
wrapper_css_new = """
    .hero-wrapper {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100svh;
      z-index: 0;
      pointer-events: none;
      background-image: url('poster.jpg');
      background-size: cover;
      background-position: center;
    }
"""
html = re.sub(wrapper_css_old, wrapper_css_new.strip(), html)

# 2. Update video tag
html = html.replace('<video id="hero-video" autoplay loop muted playsinline>', '<video id="hero-video" autoplay loop muted playsinline poster="poster.jpg">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added poster and background fallback")
