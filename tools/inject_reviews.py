from pathlib import Path

INDEX = Path("_site/index.html")

GOOGLE_REVIEWS_URL = "https://share.google/fnFeZkxGPF0vKbSpl"
GOOGLE_MAPS_URL = "https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/data=!3m1!4b1!4m6!3m5!1s0x85d4bb4228ed4485:0xc2fbabcd8b8c256e!8m2!3d20.9935165!4d-100.3944233!16s%2Fg%2F11k4sqlyzs?entry=ttu"

section = f'''
<section class="reviews-section section" id="opiniones" aria-labelledby="reviews-title">
  <div class="reviews-head reveal">
    <div>
      <p class="index-label">08 / Opiniones</p>
      <h2 class="display" id="reviews-title">La confianza también se construye.</h2>
    </div>
    <div class="reviews-score" aria-label="Calificación de cinco estrellas en Google">
      <div class="reviews-stars" aria-hidden="true">★★★★★</div>
      <strong>5.0</strong>
      <span>Calificación en Google</span>
    </div>
  </div>

  <div class="reviews-grid">
    <article class="reviews-feature reveal">
      <span class="reviews-kicker">Experiencias verificadas</span>
      <p>Conoce las opiniones reales de quienes han trabajado con <strong>JBM ARQUITECTOS</strong>. Cada reseña se consulta directamente en Google para mantener la información transparente y actualizada.</p>
      <a class="btn btn-light" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Leer opiniones en Google ↗</a>
    </article>

    <aside class="reviews-aside reveal">
      <div class="reviews-mark">“</div>
      <p>Una buena arquitectura comienza con escucha, claridad y confianza durante todo el proceso.</p>
      <div class="reviews-aside-footer">
        <span>JBM ARQUITECTOS</span>
        <a href="{GOOGLE_MAPS_URL}" target="_blank" rel="noopener">Ver ficha en Google Maps ↗</a>
      </div>
    </aside>
  </div>

  <div class="reviews-strip reveal">
    <span>★★★★★</span>
    <p>Opiniones reales · Consulta directa en Google</p>
    <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Ver todas ↗</a>
  </div>
</section>
'''

styles = r'''
<style id="reviews-section-styles">
.reviews-section{background:#11110f;color:#f4f0e7;position:relative;overflow:hidden}
.reviews-section:before{content:"5.0";position:absolute;right:-.02em;bottom:-.18em;font-family:var(--display);font-size:clamp(12rem,30vw,34rem);line-height:1;color:rgba(255,255,255,.025);pointer-events:none}
.reviews-head{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:clamp(2rem,7vw,8rem);align-items:end;margin-bottom:clamp(3rem,7vw,6rem)}
.reviews-section .index-label{color:rgba(255,255,255,.58)}
.reviews-section .display{max-width:900px;margin-top:1.1rem;color:#f4f0e7}
.reviews-score{display:grid;grid-template-columns:auto auto;column-gap:1rem;align-items:end;min-width:220px;padding-top:1rem;border-top:1px solid rgba(255,255,255,.22)}
.reviews-score strong{font-family:var(--display);font-size:clamp(3.8rem,7vw,7rem);line-height:.85;font-weight:400}
.reviews-score span{grid-column:1/-1;margin-top:.7rem;font-size:.66rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.58)}
.reviews-stars{font-size:.78rem;letter-spacing:.15em;color:#f4f0e7;margin-bottom:.65rem}
.reviews-grid{position:relative;z-index:1;display:grid;grid-template-columns:1.2fr .8fr;border-top:1px solid rgba(255,255,255,.18);border-bottom:1px solid rgba(255,255,255,.18)}
.reviews-feature,.reviews-aside{padding:clamp(2rem,5vw,5rem)}
.reviews-feature{border-right:1px solid rgba(255,255,255,.18)}
.reviews-kicker{display:block;margin-bottom:clamp(2rem,5vw,4rem);font-size:.65rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.reviews-feature p{max-width:760px;font-family:var(--display);font-size:clamp(2rem,4.4vw,4.8rem);line-height:1.08;margin:0 0 clamp(2rem,4vw,3rem)}
.reviews-feature p strong{font-weight:400;font-style:italic}
.reviews-aside{display:flex;flex-direction:column;justify-content:space-between;gap:3rem;background:#1a1a17}
.reviews-mark{font-family:var(--display);font-size:clamp(5rem,10vw,10rem);line-height:.5;color:rgba(255,255,255,.18)}
.reviews-aside>p{font-family:var(--display);font-size:clamp(1.8rem,3vw,3rem);line-height:1.18;margin:0}
.reviews-aside-footer{display:flex;flex-direction:column;gap:.65rem;padding-top:1.3rem;border-top:1px solid rgba(255,255,255,.16)}
.reviews-aside-footer span{font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.58)}
.reviews-aside-footer a{font-size:.82rem;border-bottom:1px solid rgba(255,255,255,.45);width:max-content;padding-bottom:.25rem}
.reviews-strip{position:relative;z-index:1;display:grid;grid-template-columns:auto 1fr auto;gap:1.4rem;align-items:center;padding:1.2rem 0 0;margin-top:1.2rem}
.reviews-strip span{letter-spacing:.12em}
.reviews-strip p{margin:0;color:rgba(255,255,255,.62)}
.reviews-strip a{font-size:.72rem;letter-spacing:.13em;text-transform:uppercase}
@media(max-width:900px){
  .reviews-head{grid-template-columns:1fr}
  .reviews-score{max-width:280px}
  .reviews-grid{grid-template-columns:1fr}
  .reviews-feature{border-right:0;border-bottom:1px solid rgba(255,255,255,.18)}
}
@media(max-width:620px){
  .reviews-strip{grid-template-columns:1fr;gap:.65rem}
  .reviews-feature,.reviews-aside{padding:2rem 0}
  .reviews-grid{border-top:1px solid rgba(255,255,255,.18);border-bottom:1px solid rgba(255,255,255,.18)}
}
</style>
'''

html = INDEX.read_text(encoding="utf-8")
marker = '<section class="contact section" id="contacto">'

if 'id="opiniones"' not in html:
    if marker not in html:
        raise SystemExit("No se encontró la sección de contacto para insertar opiniones")
    html = html.replace(marker, section + "\n" + marker, 1)

if 'id="reviews-section-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Sección de opiniones de Google integrada correctamente")
