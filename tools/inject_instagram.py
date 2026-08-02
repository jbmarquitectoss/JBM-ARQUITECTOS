from pathlib import Path

INDEX = Path("_site/index.html")

section = r'''
<section class="instagram-section section" id="instagram">
  <div class="section-top reveal">
    <div>
      <p class="index-label">07 / Instagram</p>
      <h2 class="display instagram-title">La obra continúa en imágenes.</h2>
    </div>
    <a class="underlink dark" href="https://www.instagram.com/jbm_arquitectos/" target="_blank" rel="noopener">Seguir a JBM ARQUITECTOS ↗</a>
  </div>

  <p class="instagram-intro reveal">Proyectos, procesos y detalles recientes del estudio. Selecciona una imagen para verla directamente en Instagram.</p>

  <div class="instagram-grid">
    <a class="instagram-card reveal" href="https://www.instagram.com/p/C7APinYL8A1/" target="_blank" rel="noopener" aria-label="Ver publicación de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/hero.webp" alt="Proyecto reciente de JBM ARQUITECTOS" loading="lazy">
      <span class="instagram-overlay"><strong>Proyecto residencial</strong><small>Ver en Instagram ↗</small></span>
    </a>

    <a class="instagram-card reveal" href="https://www.instagram.com/p/DMZIw5LMke5/?img_index=1" target="_blank" rel="noopener" aria-label="Ver publicación de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/casa-baeza-18-fachada-noche.webp" alt="Fachada contemporánea de JBM ARQUITECTOS" loading="lazy">
      <span class="instagram-overlay"><strong>Arquitectura contemporánea</strong><small>Ver en Instagram ↗</small></span>
    </a>

    <a class="instagram-card reveal" href="https://www.instagram.com/p/DSu9AKmERWY/?img_index=1" target="_blank" rel="noopener" aria-label="Ver publicación de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/facade.webp" alt="Proyecto arquitectónico de JBM ARQUITECTOS" loading="lazy">
      <span class="instagram-overlay"><strong>Diseño y ejecución</strong><small>Ver en Instagram ↗</small></span>
    </a>
  </div>

  <div class="instagram-action reveal">
    <a class="btn btn-dark" href="https://www.instagram.com/jbm_arquitectos/" target="_blank" rel="noopener">Ver más en Instagram ↗</a>
  </div>
</section>
'''

styles = r'''
<style id="instagram-section-styles">
.instagram-section{background:#f3f0e9}
.instagram-section .section-top{align-items:flex-end}
.instagram-title{max-width:850px;margin-top:1.25rem}
.instagram-intro{max-width:680px;margin:0 0 clamp(2rem,5vw,4.5rem);color:var(--muted);line-height:1.75}
.instagram-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(.8rem,1.6vw,1.5rem)}
.instagram-card{position:relative;display:block;overflow:hidden;background:#171714;aspect-ratio:4/5}
.instagram-card img{width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.7,.2,1),filter .5s ease}
.instagram-overlay{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;gap:.45rem;padding:clamp(1.2rem,2.2vw,2rem);color:#fff;background:linear-gradient(180deg,transparent 35%,rgba(0,0,0,.78));opacity:0;transition:opacity .4s ease}
.instagram-overlay strong{font-family:"DM Sans",sans-serif;font-size:.82rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.instagram-overlay small{font-size:.7rem;letter-spacing:.13em;text-transform:uppercase}
.instagram-card:hover img,.instagram-card:focus-visible img{transform:scale(1.045);filter:brightness(.78)}
.instagram-card:hover .instagram-overlay,.instagram-card:focus-visible .instagram-overlay{opacity:1}
.instagram-action{display:flex;justify-content:center;margin-top:clamp(2rem,4vw,3.5rem)}
@media (max-width:850px){
  .instagram-section .section-top{align-items:flex-start}
  .instagram-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .instagram-card:first-child{grid-column:1/-1;aspect-ratio:16/10}
  .instagram-overlay{opacity:1;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,.72))}
}
@media (max-width:560px){
  .instagram-grid{grid-template-columns:1fr}
  .instagram-card,.instagram-card:first-child{grid-column:auto;aspect-ratio:4/5}
}
</style>
'''

html = INDEX.read_text(encoding="utf-8")

if 'id="instagram"' not in html:
    marker = '<section class="contact section" id="contacto">'
    if marker not in html:
        raise SystemExit("No se encontró la sección de contacto para insertar Instagram")
    html = html.replace(marker, section + "\n" + marker, 1)

if 'id="instagram-section-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Sección de Instagram integrada correctamente")
