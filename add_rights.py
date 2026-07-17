import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = """
      <!-- § 09 -->
      <div class="gap"></div>
      <div class="stitle reveal" id="derechos">
        <span class="stitle-badge">§ 09</span>
        <h2>Derechos del Usuario</h2>
      </div>

      <div class="card reveal">
        <div class="card-header">
          <div class="card-icon">👑</div>
          <div>
            <div class="card-title">Garantías y Libertades en Umas Community</div>
            <div class="card-sub">Todos los miembros gozan de los siguientes derechos fundamentales siempre que respeten las normativas.</div>
          </div>
        </div>
        <ul class="rule-list stagger">
          <li class="rule-item"><span class="rnum gold">1</span><div class="rtxt"><strong>Libertad de Expresión</strong><span>Tienes total libertad para opinar, sugerir, debatir y expresarte, siempre y cuando no se rompan las normas de respeto, no se fomente el odio, y se haga en el canal adecuado.</span></div></li>
          <li class="rule-item"><span class="rnum gold">2</span><div class="rtxt"><strong>Presunción de Inocencia</strong><span>Si Novarito o un sistema automático comete un error al sancionarte por contexto ambiguo, tienes el derecho de ser considerado inocente hasta que un administrador evalúe el caso manualmente.</span></div></li>
          <li class="rule-item"><span class="rnum gold">3</span><div class="rtxt"><strong>Privacidad Absoluta</strong><span>Garantizamos que el Staff jamás obligará a los usuarios a mostrar contenido privado. Tus mensajes directos son tuyos, y nadie puede exigirte revelar tu identidad real ni datos que no quieras compartir.</span></div></li>
          <li class="rule-item"><span class="rnum gold">4</span><div class="rtxt"><strong>Uso de Herramientas</strong><span>Tienes derecho a disfrutar de todas las características del servidor de forma justa: desde usar los bots de música, crear canales de voz personalizados temporales, y proponer emojis o actividades al Staff.</span></div></li>
          <li class="rule-item"><span class="rnum gold">5</span><div class="rtxt"><strong>Trato Igualitario</strong><span>No existen favores especiales. Las normas aplican para todos por igual, incluyendo al propio Staff, artistas y creadores de contenido. Si el Staff incumple, puedes reportarlo al Owner.</span></div></li>
        </ul>
      </div>

    </div><!-- /container -->"""

html = html.replace("    </div><!-- /container -->", new_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added section 09 successfully")
