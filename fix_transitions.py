import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the specific broken transitions
html = html.replace('transition: color 0.05s, border-color 0.05s', 'transition: color 0.3s ease, border-color 0.3s ease;')
html = html.replace('transition: opacity 2.5s ease-in-out;, filter 0.05s ease', 'transition: opacity 0.8s ease-in-out, filter 0.8s ease;')
html = html.replace('transition: opacity 0.05s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.05s cubic-bezier(0.25, 0.46, 0.45, 0.94)', 'transition: opacity 1.2s cubic-bezier(0.25, 0.8, 0.25, 1), transform 1.2s cubic-bezier(0.25, 0.8, 0.25, 1);')
html = html.replace('transition: border-color 0.05s', 'transition: border-color 0.4s ease;')
html = html.replace('transition: opacity 0.05s', 'transition: opacity 0.4s ease;')
html = html.replace('transition: background 0.05s, border-color 0.05s, transform 0.05s', 'transition: background 0.3s ease, border-color 0.3s ease, transform 0.3s ease;')
html = html.replace('transition: transform 0.05s ease-out, box-shadow 0.05s ease-out, border-color 0.05s ease-out', 'transition: transform 0.4s ease-out, box-shadow 0.4s ease-out, border-color 0.4s ease-out;')
html = html.replace('transition: width 0.05s cubic-bezier(0.22,1,0.36,1) position: relative;', 'transition: width 1.5s cubic-bezier(0.22,1,0.36,1); position: relative;')
html = html.replace('transition: transform 0.05s ease-out, box-shadow 0.05s ease-out', 'transition: transform 0.4s ease-out, box-shadow 0.4s ease-out;')
html = html.replace('transition: border-color 0.05s ease-out, transform 0.05s ease-out', 'transition: border-color 0.4s ease-out, transform 0.4s ease-out;')
html = html.replace('transition: transform 0.05s ease-out }', 'transition: transform 0.4s ease-out; }')
html = html.replace('transition: background 0.05s }', 'transition: background 0.3s ease; }')
html = html.replace('transition: opacity 0.05s, transform 0.05s, box-shadow 0.05s box-shadow: 0 8px 28px rgba(144,96,208,0.4);', 'transition: all 0.4s ease; box-shadow: 0 8px 28px rgba(144,96,208,0.4);')
html = html.replace('transition: color 0.05s }', 'transition: color 0.3s ease; }')
html = html.replace('transition: all 0.05s cubic-bezier(0.25, 0.46, 0.45, 0.94)', 'transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Transitions fixed")
