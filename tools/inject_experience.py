from pathlib import Path

INDEX = Path("_site/index.html")
CALENDAR = "https://calendar.app.google/h7XwWw9xizAmMNz38"
WHATSAPP = "https://wa.me/524191039430?text=Hola%20JBM%20ARQUITECTOS,%20vi%20su%20p%C3%A1gina%20y%20me%20gustar%C3%ADa%20hablar%20sobre%20mi%20proyecto."

hero = f'''
<section class="jbm-cinematic" id="inicio" aria-label="Presentación de JBM ARQUITECTOS">
  <video class="jbm-cinematic-video" autoplay muted loop playsinline preload="metadata" poster="assets/images/hero.webp" aria-hidden="true">
    <source src="assets/video/jbm-hero.mp4" type="video/mp4">
    <source src="assets/video/jbm-hero-small.mp4" type="video/mp4">
    <source src="jbm-hero.mp4" type="video/mp4">
  </video>
  <div class="jbm-cinematic-shade"></div>
  <div class="jbm-cinematic-copy">
    <p>Arquitectura · Interiorismo · Ejecución</p>
    <h1>Diseñamos la forma<br>en la que vas a vivir.</h1>
    <div class="jbm-hero-actions">
      <a href="#proyectos" class="jbm-link-light">Explorar proyectos ↘</a>
      <a href="{CALENDAR}" target="_blank" rel="noopener" class="jbm-link-light">Agendar una cita ↗</a>
    </div>
  </div>
  <div class="jbm-rotating-line" aria-live="polite">
    <span>Arquitectura contemporánea.</span>
    <span>Cada detalle tiene un propósito.</span>
    <span>El siguiente proyecto puede ser el tuyo.</span>
    <span>Bienvenido a JBM ARQUITECTOS.</span>
  </div>
</section>
'''

experience = f'''
<section class="jbm-manifesto section" id="manifiesto">
  <p class="index-label reveal">02 / Manifiesto</p>
  <h2 class="reveal">El siguiente proyecto<br>que aparecerá aquí…<br><em>podría ser el tuyo.</em></h2>
  <div class="jbm-manifesto-foot reveal">
    <p>Diseñamos espacios que responden a una forma de vivir, a un lugar y a una historia.</p>
    <a href="{CALENDAR}" target="_blank" rel="noopener">Hablemos de tu proyecto ↗</a>
  </div>
</section>

<section class="jbm-process section" id="proceso">
  <div class="jbm-section-head reveal">
    <div><p class="index-label">03 / Proceso</p><h2>De la primera conversación<br>a la entrega del espacio.</h2></div>
    <p>Un proceso claro permite tomar mejores decisiones, cuidar el presupuesto y mantener la esencia del proyecto.</p>
  </div>
  <ol class="jbm-process-grid">
    <li class="reveal"><span>01</span><strong>Escuchar</strong><p>Conocemos tus necesidades, terreno, presupuesto y expectativas.</p></li>
    <li class="reveal"><span>02</span><strong>Conceptualizar</strong><p>Construimos el programa arquitectónico y la idea rectora.</p></li>
    <li class="reveal"><span>03</span><strong>Diseñar</strong><p>Desarrollamos anteproyecto, materialidad y experiencia espacial.</p></li>
    <li class="reveal"><span>04</span><strong>Documentar</strong><p>Integramos el proyecto ejecutivo para llevarlo correctamente a obra.</p></li>
    <li class="reveal"><span>05</span><strong>Construir</strong><p>Coordinamos la ejecución, los detalles y la calidad del resultado.</p></li>
    <li class="reveal"><span>06</span><strong>Entregar</strong><p>Un espacio preparado para comenzar una nueva etapa.</p></li>
  </ol>
</section>

<section class="jbm-services section" id="servicios-jbm">
  <div class="jbm-section-head reveal">
    <div><p class="index-label">04 / Diseñamos para</p><h2>Una arquitectura integral.</h2></div>
    <p>Desde la idea inicial hasta la ejecución, cada servicio forma parte de una misma visión.</p>
  </div>
  <div class="jbm-services-list">
    <article class="reveal"><span>01</span><h3>Arquitectura residencial</h3><p>Casas pensadas desde el contexto, la luz y la vida cotidiana.</p></article>
    <article class="reveal"><span>02</span><h3>Remodelación</h3><p>Nuevas posibilidades para espacios existentes.</p></article>
    <article class="reveal"><span>03</span><h3>Interiorismo</h3><p>Materiales, iluminación y mobiliario con una identidad coherente.</p></article>
    <article class="reveal"><span>04</span><h3>Proyecto ejecutivo</h3><p>Información precisa para construir con mayor control.</p></article>
    <article class="reveal"><span>05</span><h3>Ejecución de obra</h3><p>Coordinación y seguimiento para materializar el diseño.</p></article>
  </div>
</section>

<section class="jbm-trust section" aria-label="Indicadores de confianza">
  <div class="jbm-trust-item reveal"><strong>5.0</strong><span>Calificación en Google</span></div>
  <div class="jbm-trust-item reveal"><strong>5</strong><span>Opiniones verificadas</span></div>
  <div class="jbm-trust-item reveal"><strong>360°</strong><span>Diseño y ejecución integral</span></div>
  <div class="jbm-trust-item reveal"><strong>1:1</strong><span>Atención personalizada</span></div>
</section>

<section class="jbm-final-cta" id="iniciar-proyecto">
  <div class="jbm-final-inner reveal">
    <p>El siguiente proyecto puede ser el tuyo.</p>
    <h2>¿Cómo imaginas<br>tu proyecto?</h2>
    <div class="jbm-final-actions">
      <a href="{CALENDAR}" target="_blank" rel="noopener" class="jbm-pill-light">Agenda una reunión ↗</a>
      <a href="{WHATSAPP}" target="_blank" rel="noopener" class="jbm-pill-outline">Cuéntanos tu idea ↗</a>
    </div>
  </div>
</section>
'''

styles = r'''
<style id="jbm-experience-styles">
.jbm-cinematic{position:relative;min-height:100svh;background:#111;color:#fff;overflow:hidden;display:flex;align-items:flex-end}
.jbm-cinematic-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.jbm-cinematic-shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.18),rgba(0,0,0,.25) 45%,rgba(0,0,0,.78))}
.jbm-cinematic-copy{position:relative;z-index:2;width:100%;padding:clamp(7rem,12vw,11rem) clamp(1.4rem,5vw,5rem) clamp(6rem,9vw,8rem)}
.jbm-cinematic-copy>p{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;margin:0 0 1.3rem}
.jbm-cinematic-copy h1{font-family:var(--display,serif);font-size:clamp(3.5rem,9.5vw,10rem);font-weight:400;line-height:.86;letter-spacing:-.045em;margin:0;max-width:1200px}
.jbm-hero-actions{display:flex;flex-wrap:wrap;gap:2rem;margin-top:clamp(2rem,4vw,4rem)}
.jbm-link-light{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,.65);padding-bottom:.35rem}
.jbm-rotating-line{position:absolute;z-index:2;right:clamp(1.4rem,5vw,5rem);bottom:2rem;min-width:min(430px,48vw);height:1.2rem;text-align:right;overflow:hidden;font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.72)}
.jbm-rotating-line span{position:absolute;inset:0;opacity:0;animation:jbmPhrase 16s infinite}
.jbm-rotating-line span:nth-child(2){animation-delay:4s}.jbm-rotating-line span:nth-child(3){animation-delay:8s}.jbm-rotating-line span:nth-child(4){animation-delay:12s}
@keyframes jbmPhrase{0%,20%{opacity:1;transform:translateY(0)}25%,100%{opacity:0;transform:translateY(-100%)}}
.jbm-manifesto{background:#11110f;color:#f5f1e9;min-height:88vh;display:flex;flex-direction:column;justify-content:center}
.jbm-manifesto .index-label{color:rgba(255,255,255,.5)}
.jbm-manifesto h2{font-family:var(--display,serif);font-size:clamp(3.2rem,9vw,9rem);font-weight:400;line-height:.9;letter-spacing:-.045em;margin:clamp(2rem,5vw,5rem) 0}
.jbm-manifesto h2 em{font-weight:400;color:#cbbda5}
.jbm-manifesto-foot{display:grid;grid-template-columns:1fr auto;gap:2rem;align-items:end;border-top:1px solid rgba(255,255,255,.18);padding-top:1.4rem}
.jbm-manifesto-foot p{max-width:600px;color:rgba(255,255,255,.64)}
.jbm-manifesto-foot a{font-size:.72rem;letter-spacing:.13em;text-transform:uppercase}
.jbm-section-head{display:grid;grid-template-columns:1.3fr .7fr;gap:clamp(2rem,8vw,9rem);align-items:end;margin-bottom:clamp(3rem,7vw,7rem)}
.jbm-section-head h2{font-family:var(--display,serif);font-size:clamp(2.8rem,6vw,6.5rem);font-weight:400;line-height:.95;margin:1rem 0 0}
.jbm-section-head>p{max-width:520px;color:var(--muted,#777);line-height:1.7}
.jbm-process{background:#f4f0e7}
.jbm-process-grid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line,#bbb);border-left:1px solid var(--line,#bbb)}
.jbm-process-grid li{padding:clamp(1.5rem,3vw,3rem);min-height:280px;border-right:1px solid var(--line,#bbb);border-bottom:1px solid var(--line,#bbb);display:flex;flex-direction:column}
.jbm-process-grid span,.jbm-services-list span{font-size:.64rem;letter-spacing:.15em;color:var(--muted,#777)}
.jbm-process-grid strong{font-family:var(--display,serif);font-size:clamp(2rem,3vw,3.4rem);font-weight:400;margin:auto 0 1rem}
.jbm-process-grid p{margin:0;line-height:1.65;color:var(--muted,#777)}
.jbm-services{background:#e9e3d7}
.jbm-services-list{border-top:1px solid var(--line,#aaa)}
.jbm-services-list article{display:grid;grid-template-columns:70px minmax(260px,.8fr) 1fr;gap:2rem;align-items:center;padding:clamp(1.5rem,3vw,2.5rem) 0;border-bottom:1px solid var(--line,#aaa)}
.jbm-services-list h3{font-family:var(--display,serif);font-size:clamp(2rem,4vw,4.4rem);font-weight:400;margin:0}
.jbm-services-list p{margin:0;color:var(--muted,#777);max-width:520px}
.jbm-trust{background:#11110f;color:#fff;display:grid;grid-template-columns:repeat(4,1fr);padding-top:0!important;padding-bottom:0!important}
.jbm-trust-item{padding:clamp(2rem,5vw,5rem);border-right:1px solid rgba(255,255,255,.16)}
.jbm-trust-item:last-child{border-right:0}
.jbm-trust-item strong{display:block;font-family:var(--display,serif);font-size:clamp(3rem,6vw,6.5rem);font-weight:400;line-height:1}
.jbm-trust-item span{display:block;margin-top:1rem;font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.jbm-final-cta{min-height:92vh;background:#0d0d0c;color:#f6f1e7;display:grid;place-items:center;padding:clamp(3rem,7vw,7rem);text-align:center}
.jbm-final-inner>p{font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.58)}
.jbm-final-inner h2{font-family:var(--display,serif);font-size:clamp(4rem,11vw,11rem);font-weight:400;line-height:.82;letter-spacing:-.055em;margin:clamp(2rem,4vw,4rem) 0}
.jbm-final-actions{display:flex;justify-content:center;flex-wrap:wrap;gap:1rem}
.jbm-pill-light,.jbm-pill-outline{display:inline-flex;align-items:center;justify-content:center;min-width:220px;padding:1.1rem 1.5rem;border-radius:999px;font-size:.69rem;letter-spacing:.13em;text-transform:uppercase}
.jbm-pill-light{background:#f4efe5;color:#111}.jbm-pill-outline{border:1px solid rgba(255,255,255,.35)}
@media(max-width:900px){.jbm-section-head,.jbm-manifesto-foot{grid-template-columns:1fr}.jbm-process-grid{grid-template-columns:repeat(2,1fr)}.jbm-trust{grid-template-columns:repeat(2,1fr)}.jbm-services-list article{grid-template-columns:50px 1fr}.jbm-services-list p{grid-column:2}}
@media(max-width:600px){.jbm-cinematic-copy h1{font-size:clamp(3rem,16vw,5.2rem)}.jbm-rotating-line{left:1.4rem;right:1.4rem;min-width:0;text-align:left}.jbm-process-grid{grid-template-columns:1fr}.jbm-trust{grid-template-columns:1fr}.jbm-trust-item{border-right:0;border-bottom:1px solid rgba(255,255,255,.16)}.jbm-services-list article{grid-template-columns:1fr;gap:.8rem}.jbm-services-list p{grid-column:auto}.jbm-manifesto h2{font-size:clamp(3.2rem,17vw,5.8rem)}}
@media(prefers-reduced-motion:reduce){.jbm-cinematic-video{display:none}.jbm-rotating-line span{animation:none;opacity:0}.jbm-rotating-line span:first-child{opacity:1}}
</style>
'''

html = INDEX.read_text(encoding="utf-8")
if 'id="jbm-experience-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

if 'class="jbm-cinematic"' not in html:
    html = html.replace('<body', '<body', 1)
    body_end = html.find('>') + 1 if html.lstrip().startswith('<body') else -1
    # insertar justo después de la etiqueta body usando una búsqueda robusta
    pos = html.lower().find('<body')
    if pos >= 0:
        close = html.find('>', pos)
        html = html[:close+1] + '\n' + hero + html[close+1:]

if 'id="manifiesto"' not in html:
    marker = '<section class="instagram-section'
    pos = html.find(marker)
    if pos < 0:
        marker = '<section class="reviews-section'
        pos = html.find(marker)
    if pos < 0:
        marker = '<section class="contact section" id="contacto">'
        pos = html.find(marker)
    if pos >= 0:
        html = html[:pos] + experience + '\n' + html[pos:]
    else:
        html = html.replace('</body>', experience + '\n</body>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Experiencia JBM integrada: video, manifiesto, proceso, servicios, confianza y cierre")
