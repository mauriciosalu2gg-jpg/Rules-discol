import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

points_html = """
        <div class="pts-bars" id="pts-bars">
          <!-- Escala Dinámica de Sanciones -->
          <div class="pts-row"><div class="pts-lbl">05 pts</div><div class="pts-track"><div class="pts-fill" data-w="5" style="background:#555"></div></div><div class="pts-action" style="color:#aaa">Aviso silencioso</div></div>
          <div class="pts-row"><div class="pts-lbl">10 pts</div><div class="pts-track"><div class="pts-fill" data-w="10" style="background:var(--teal)"></div></div><div class="pts-action" style="color:var(--teal)">Advertencia leve</div></div>
          <div class="pts-row"><div class="pts-lbl">15 pts</div><div class="pts-track"><div class="pts-fill" data-w="15" style="background:var(--yellow)"></div></div><div class="pts-action" style="color:var(--yellow)">Silencio 5m</div></div>
          <div class="pts-row"><div class="pts-lbl">20 pts</div><div class="pts-track"><div class="pts-fill" data-w="20" style="background:var(--yellow)"></div></div><div class="pts-action" style="color:var(--yellow)">Silencio 10m</div></div>
          <div class="pts-row"><div class="pts-lbl">25 pts</div><div class="pts-track"><div class="pts-fill" data-w="25" style="background:var(--gold)"></div></div><div class="pts-action" style="color:var(--gold)">Silencio 30m</div></div>
          <div class="pts-row"><div class="pts-lbl">30 pts</div><div class="pts-track"><div class="pts-fill" data-w="30" style="background:var(--gold)"></div></div><div class="pts-action" style="color:var(--gold)">Silencio 1h</div></div>
          <div class="pts-row"><div class="pts-lbl">35 pts</div><div class="pts-track"><div class="pts-fill" data-w="35" style="background:var(--orange)"></div></div><div class="pts-action" style="color:var(--orange)">Silencio 3h</div></div>
          <div class="pts-row"><div class="pts-lbl">40 pts</div><div class="pts-track"><div class="pts-fill" data-w="40" style="background:var(--orange)"></div></div><div class="pts-action" style="color:var(--orange)">Silencio 6h</div></div>
          <div class="pts-row"><div class="pts-lbl">45 pts</div><div class="pts-track"><div class="pts-fill" data-w="45" style="background:#ff8844"></div></div><div class="pts-action" style="color:#ff8844">Silencio 12h</div></div>
          <div class="pts-row"><div class="pts-lbl">50 pts</div><div class="pts-track"><div class="pts-fill" data-w="50" style="background:#ff6644"></div></div><div class="pts-action" style="color:#ff6644">Silencio 1d</div></div>
          <div class="pts-row"><div class="pts-lbl">55 pts</div><div class="pts-track"><div class="pts-fill" data-w="55" style="background:#ff4444"></div></div><div class="pts-action" style="color:#ff4444">Silencio 3d</div></div>
          <div class="pts-row"><div class="pts-lbl">60 pts</div><div class="pts-track"><div class="pts-fill" data-w="60" style="background:var(--red)"></div></div><div class="pts-action" style="color:var(--red)">Silencio 1s</div></div>
          <div class="pts-row"><div class="pts-lbl">65 pts</div><div class="pts-track"><div class="pts-fill" data-w="65" style="background:var(--red)"></div></div><div class="pts-action" style="color:var(--red)">Kick (Expulsión)</div></div>
          <div class="pts-row"><div class="pts-lbl">70 pts</div><div class="pts-track"><div class="pts-fill" data-w="70" style="background:#d41133"></div></div><div class="pts-action" style="color:#d41133">Silencio 2s</div></div>
          <div class="pts-row"><div class="pts-lbl">75 pts</div><div class="pts-track"><div class="pts-fill" data-w="75" style="background:#b30022"></div></div><div class="pts-action" style="color:#b30022">Silencio 3s</div></div>
          <div class="pts-row"><div class="pts-lbl">80 pts</div><div class="pts-track"><div class="pts-fill" data-w="80" style="background:#8b0011"></div></div><div class="pts-action" style="color:#8b0011">Silencio 4s</div></div>
          <div class="pts-row"><div class="pts-lbl">85 pts</div><div class="pts-track"><div class="pts-fill" data-w="85" style="background:#700000"></div></div><div class="pts-action" style="color:#700000">Ban 7d</div></div>
          <div class="pts-row"><div class="pts-lbl">90 pts</div><div class="pts-track"><div class="pts-fill" data-w="90" style="background:#500000"></div></div><div class="pts-action" style="color:#500000">Ban 30d</div></div>
          <div class="pts-row"><div class="pts-lbl">95 pts</div><div class="pts-track"><div class="pts-fill" data-w="95" style="background:#300000"></div></div><div class="pts-action" style="color:#300000">Ban 90d</div></div>
          <div class="pts-row"><div class="pts-lbl">100 pts</div><div class="pts-track"><div class="pts-fill" data-w="100" style="background:#111111; box-shadow: 0 0 10px #ff0000"></div></div><div class="pts-action" style="color:#ff0000; font-weight: bold; text-shadow: 0 0 5px #ff0000;">Ban Permanente</div></div>
        </div>
"""

html = re.sub(r'<div class="pts-bars" id="pts-bars">.*?</div>\s*</div>\s*<div class="callout', points_html.strip() + '\n\n        <div class="callout', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Points updated")
