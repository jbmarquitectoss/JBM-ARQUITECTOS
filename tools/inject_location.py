from pathlib import Path

INDEX = Path("_site/index.html")

MAPS_URL = "https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/data=!3m1!4b1!4m6!3m5!1s0x85d4bb4228ed4485:0xc2fbabcd8b8c256e!8m2!3d20.9935165!4d-100.3944233!16s%2Fg%2F11k4sqlyzs?entry=ttu&g_ep=EgoyMDI2MDcyOS4wIKXMDSoASAFQAw%3D%3D"
EMBED_URL = "https://www.google.com/maps?q=20.9935165,-100.3944233&z=16&output=embed"

section = f'''
<section class="location-section" id="ubicacion" aria-labelledby="location-title">
  <div class="location-copy section reveal">
    <p class="index-label">08 / Ubicación</p>
    <p class="location-kicker">ESTUDIO · SAN JOSÉ ITURBIDE</p>
    <h2 class="display" id="location-title">Ven a platicarnos<br><em>tu próxima idea.</em></h2>
    <p class="location-text">Estamos en San José Iturbide, Guanajuato. Agenda una visita para conocer tu proyecto, revisar el terreno y definir los siguientes pasos.</p>

    <div class="location-details">
      <div><span>Estudio</span><strong>JBM ARQUITECTOS</strong></div>
      <div><span>Ciudad</span><strong>San José Iturbide, Gto.</strong></div>
      <div><span>Atención</span><strong>Con cita previa</strong></div>
    </div>

    <div class="location-actions">
      <a class="btn btn-light" href="{MAPS_URL}" target="_blank" rel="noopener">Cómo llegar ↗</a>
      <a class="location-link" href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank" rel="noopener">Agendar visita ↗</a>
    </div>
  </div>

  <div class="location-map reveal">
    <iframe
      title="Ubicación de JBM ARQUITECTOS en San José Iturbide"
      src="{EMBED_URL}"
      width="100%"
      height="100%"
      style="border:0"
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
      allowfullscreen>
    </iframe>
    <a class="map-corner" href="{MAPS_URL}" target="_blank" rel="noopener">
      <span>20.9935° N</span>
      <strong>Abrir en Google Maps ↗</strong>
    </a>
  </div>
</section>
'''

styles = r'''
<style id="location-section-styles">
.location-section{display:grid;grid-template-columns:minmax(320px,.82fr) minmax(0,1.18fr);min-height:min(820px,90vh);background:#11110f;color:#f4f0e7}
.location-copy{display:flex;flex-direction:column;justify-content:center;padding-top:clamp(5rem,9vw,9rem);padding-bottom:clamp(5rem,9vw,9rem)}
.location-copy .index-label{color:rgba(255,255,255,.5)}
.location-kicker{margin:clamp(2.5rem,6vw,5.5rem) 0 1rem;font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.58)}
.location-copy .display{color:#f4f0e7;margin:0;max-width:750px}
.location-copy .display em{font-weight:400;color:#c7a978}
.location-text{max-width:610px;margin:clamp(1.8rem,4vw,3.2rem) 0;color:rgba(255,255,255,.68);font-size:clamp(1rem,1.3vw,1.2rem);line-height:1.75}
.location-details{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;padding:1.4rem 0;border-top:1px solid rgba(255,255,255,.16);border-bottom:1px solid rgba(255,255,255,.16)}
.location-details div{display:flex;flex-direction:column;gap:.45rem}
.location-details span{font-size:.58rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.45)}
.location-details strong{font-size:.78rem;font-weight:400;letter-spacing:.02em;color:#fff}
.location-actions{display:flex;align-items:center;gap:clamp(1.2rem,3vw,2.5rem);margin-top:clamp(2rem,4vw,3.5rem);flex-wrap:wrap}
.location-link{color:#fff;border-bottom:1px solid rgba(255,255,255,.65);padding-bottom:.25rem;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase}
.location-map{position:relative;min-height:620px;overflow:hidden;background:#d9d4ca}
.location-map iframe{position:absolute;inset:0;filter:grayscale(1) contrast(.92) brightness(.9);transition:filter .55s ease,transform .8s ease}
.location-map:hover iframe{filter:grayscale(.2) contrast(.98) brightness(.98);transform:scale(1.01)}
.location-map:after{content:"";position:absolute;inset:0;pointer-events:none;box-shadow:inset 28px 0 45px rgba(17,17,15,.16)}
.map-corner{position:absolute;z-index:2;right:clamp(1rem,2.4vw,2rem);bottom:clamp(1rem,2.4vw,2rem);display:flex;flex-direction:column;gap:.35rem;min-width:230px;padding:1.1rem 1.25rem;background:rgba(17,17,15,.88);color:#fff;backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.18)}
.map-corner span{font-size:.58rem;letter-spacing:.16em;color:rgba(255,255,255,.55)}
.map-corner strong{font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase}
@media(max-width:960px){
  .location-section{grid-template-columns:1fr}
  .location-map{min-height:520px;order:-1}
  .location-map:after{box-shadow:inset 0 -28px 45px rgba(17,17,15,.12)}
}
@media(max-width:620px){
  .location-map{min-height:430px}
  .location-details{grid-template-columns:1fr;gap:1.2rem}
  .map-corner{left:1rem;right:1rem;min-width:0}
  .location-actions .btn{width:100%}
}
</style>
'''

html = INDEX.read_text(encoding="utf-8")
marker = '<section class="contact section" id="contacto">'

if 'id="ubicacion"' not in html:
    if marker not in html:
        raise SystemExit("No se encontró la sección de contacto para insertar la ubicación")
    html = html.replace(marker, section + "\n" + marker, 1)

if 'id="location-section-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Mapa editorial integrado correctamente")
