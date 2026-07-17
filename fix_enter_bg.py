import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_enter_css = """    #enter-screen {
      position: fixed;
      inset: 0;
      background: rgba(21, 9, 38, 0.85);
      backdrop-filter: blur(0px);"""
new_enter_css = """    #enter-screen {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at center, #1c0e30 0%, #10061e 100%);
      background-image: radial-gradient(circle at center, #1c0e30 0%, #10061e 100%), url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='30' cy='30' r='0.8' fill='rgba(255,255,255,0.15)'/%3E%3Ccircle cx='10' cy='10' r='0.5' fill='rgba(255,210,120,0.1)'/%3E%3Ccircle cx='50' cy='15' r='1' fill='rgba(255,255,255,0.1)'/%3E%3Ccircle cx='15' cy='50' r='0.6' fill='rgba(255,255,255,0.1)'/%3E%3C/svg%3E");
      backdrop-filter: blur(0px);"""
html = html.replace(old_enter_css, new_enter_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated enter background")
