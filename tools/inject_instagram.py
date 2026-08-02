from pathlib import Path

INDEX = Path("_site/index.html")

section = r'''
<section class="instagram-section section" id="instagram" aria-labelledby="instagram-title">
  <div class="instagram-head reveal">
    <div>
      <p class="index-label">07 / Instagram</p>
      <h2 class="display instagram-title" id="instagram-title">Arquitectura en proceso.<br>Ideas que toman forma.</h2>
    </div>
    <div class="instagram-profile">
      <span>Contenido reciente del estudio</span>
      <a href="https://www.instagram.com/jbmarquitectos.mx/" target="_blank" rel="noopener">@jbmarquitectos.mx ↗</a>
    </div>
  </div>

  <div class="instagram-editorial-grid">
    <a class="instagram-card instagram-card-main reveal" href="https://www.instagram.com/p/C7APinYL8A1/" target="_blank" rel="noopener" aria-label="Abrir la publicación C7APinYL8A1 de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/hero.webp" alt="Arquitectura residencial de JBM ARQUITECTOS" loading="lazy">
      <span class="instagram-number">01</span>
      <span class="instagram-overlay"><strong>Arquitectura residencial</strong><small>Abrir publicación ↗</small></span>
    </a>

    <a class="instagram-card reveal" href="https://www.instagram.com/p/DMZIw5LMke5/" target="_blank" rel="noopener" aria-label="Abrir la publicación DMZIw5LMke5 de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/casa-baeza-18-fachada-noche.webp" alt="Fachada nocturna de CASA BAEZA" loading="lazy">
      <span class="instagram-number">02</span>
      <span class="instagram-overlay"><strong>CASA BAEZA</strong><small>Abrir publicación ↗</small></span>
    </a>

    <a class="instagram-card reveal" href="https://www.instagram.com/p/DSu9AKmERWY/" target="_blank" rel="noopener" aria-label="Abrir la publicación DSu9AKmERWY de JBM ARQUITECTOS en Instagram">
      <img src="assets/images/facade.webp" alt="Proyecto contemporáneo de JBM ARQUITECTOS" loading="lazy">
      <span class="instagram-number">03</span>
      <span class="instagram-overlay"><strong>Diseño y ejecución</strong><small>Abrir publicación ↗</small></span>
    </a>
  </div>

  <div class="instagram-footer reveal">
    <p>Proyectos, obra, interiorismo y detalles detrás de cada espacio.</p>
    <a class="btn btn-dark" href="https://www.instagram.com/jbmarquitectos.mx/" target="_blank" rel="noopener">Ver Instagram ↗</a>
  </div>
</section>
'''

styles = r'''
<style id="instagram-section-styles">
.instagram-section{position:relative;overflow:hidden;background:#ece6da}
.instagram-section:before{content:"JBM";position:absolute;right:-.04em;top:-.22em;font-family:var(--display);font-size:clamp(10rem,27vw,31rem);line-height:1;color:rgba(17,17,15,.035);pointer-events:none}
.instagram-head{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(240px,.65fr);gap:clamp(2rem,7vw,8rem);align-items:end;margin-bottom:clamp(3rem,7vw,7rem)}
.instagram-title{max-width:980px;margin-top:1.1rem}
.instagram-profile{border-top:1px solid var(--line);padding-top:1.1rem;display:flex;flex-direction:column;gap:.45rem;align-items:flex-start}
.instagram-profile span{font-size:.66rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted)}
.instagram-profile a{font-family:var(--display);font-size:clamp(1.5rem,2.5vw,2.4rem);line-height:1.1;border-bottom:1px solid currentColor;padding-bottom:.3rem}
.instagram-editorial-grid{position:relative;z-index:1;display:grid;grid-template-columns:1.35fr .65fr;grid-template-rows:repeat(2,minmax(260px,36vw));gap:clamp(.8rem,1.5vw,1.4rem)}
.instagram-card{position:relative;display:block;overflow:hidden;background:#151512;isolation:isolate}
.instagram-card-main{grid-row:1/3}
.instagram-card img{width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1),filter .5s ease}
.instagram-number{position:absolute;z-index:2;top:1.1rem;left:1.1rem;width:2.5rem;height:2.5rem;display:grid;place-items:center;border:1px solid rgba(255,255,255,.55);border-radius:50%;color:#fff;font-size:.62rem;letter-spacing:.08em;background:rgba(0,0,0,.18);backdrop-filter:blur(8px)}
.instagram-overlay{position:absolute;z-index:1;inset:0;display:flex;flex-direction:column;justify-content:flex-end;gap:.5rem;padding:clamp(1.25rem,2.4vw,2.3rem);color:#fff;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.82));opacity:.88;transition:opacity .4s ease}
.instagram-overlay strong{font-family:var(--display);font-size:clamp(1.7rem,3vw,3.5rem);font-weight:400;line-height:1}
.instagram-card:not(.instagram-card-main) .instagram-overlay strong{font-size:clamp(1.35rem,2.2vw,2.4rem)}
.instagram-overlay small{font-size:.64rem;letter-spacing:.15em;text-transform:uppercase}
.instagram-card:hover img,.instagram-card:focus-visible img{transform:scale(1.055);filter:brightness(.76)}
.instagram-card:hover .instagram-overlay,.instagram-card:focus-visible .instagram-overlay{opacity:1}
.instagram-footer{position:relative;z-index:1;display:flex;justify-content:space-between;align-items:center;gap:2rem;margin-top:clamp(2rem,4vw,3.5rem);padding-top:1.5rem;border-top:1px solid var(--line)}
.instagram-footer p{margin:0;color:var(--muted);max-width:520px}
@media(max-width:900px){
  .instagram-head{grid-template-columns:1fr;align-items:start}
  .instagram-editorial-grid{grid-template-columns:1fr 1fr;grid-template-rows:auto}
  .instagram-card-main{grid-column:1/-1;grid-row:auto;aspect-ratio:16/10}
  .instagram-card:not(.instagram-card-main){aspect-ratio:4/5}
}
@media(max-width:620px){
  .instagram-editorial-grid{grid-template-columns:1fr}
  .instagram-card,.instagram-card-main{grid-column:auto;aspect-ratio:4/5}
  .instagram-footer{align-items:flex-start;flex-direction:column}
  .instagram-footer .btn{width:100%}
}
</style>
'''

html = INDEX.read_text(encoding="utf-8")
marker = '<section class="contact section" id="contacto">'

if 'id="instagram"' not in html:
    if marker not in html:
        raise SystemExit("No se encontró la sección de contacto para insertar Instagram")
    html = html.replace(marker, section + "\n" + marker, 1)

if 'id="instagram-section-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Instagram actualizado: perfil y publicaciones correctas")
