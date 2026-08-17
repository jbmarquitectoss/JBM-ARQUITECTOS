from pathlib import Path

path = Path("_site/index.html")
html = path.read_text(encoding="utf-8")

css = r'''
  /* JBM 2.1 refinements */
  .hero::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:radial-gradient(circle at 70% 25%,rgba(185,155,103,.12),transparent 34%),linear-gradient(90deg,rgba(5,5,4,.78),rgba(5,5,4,.28) 58%,rgba(5,5,4,.18))}
  .hero-copy,.scroll-cue,.v4-sound{z-index:3}.v4-hero-video{filter:saturate(.9) contrast(1.03);transition:opacity 1.1s ease,transform 10s ease}.hero.has-video .v4-hero-video{opacity:1;transform:scale(1.025)}
  .btn,.underlink,.view-pill{transition:transform .28s ease,background .28s ease,color .28s ease,box-shadow .28s ease}.btn:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(0,0,0,.14)}
  .portfolio-card{position:relative}.project-media{border-radius:2px}.project-media::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(0,0,0,.28),transparent 45%);opacity:.35;transition:opacity .45s ease}.project-media:hover::after{opacity:.68}.project-media:hover .view-pill{transform:translateY(-4px)}
  .portfolio-heading{margin:.7rem 0 0;font-size:clamp(3.4rem,7vw,7.5rem);line-height:.88;letter-spacing:-.03em}
  .trust-card{position:relative;overflow:hidden}.trust-card::before{content:"";position:absolute;left:0;top:0;width:0;height:2px;background:var(--accent);transition:width .45s ease}.trust-card:hover::before{width:100%}
  .reviews-score{position:sticky;top:110px}.review-map{margin-top:2.2rem;background:rgba(255,255,255,.42);border:1px solid rgba(17,17,15,.12);overflow:hidden}.review-map iframe{display:block;width:100%;height:265px;border:0;filter:grayscale(1) contrast(.95);transition:filter .35s ease}.review-map:hover iframe{filter:grayscale(0) contrast(1)}
  .review-map-info{padding:1.25rem 1.35rem;display:grid;gap:.35rem}.review-map-info strong{font-family:var(--display);font-size:1.45rem;font-weight:400}.review-map-info p{margin:0;color:var(--muted)}.review-map-info a{margin-top:.65rem;width:max-content}
  .footer-links{display:flex;flex-wrap:wrap;gap:1.25rem;margin-top:1rem}.footer-links a{font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.72)}.footer-links a:hover{color:#fff}
  @media(max-width:900px){.reviews-score{position:static}.review-map iframe{height:230px}}
  @media(max-width:640px){.hero::after{background:linear-gradient(0deg,rgba(5,5,4,.76),rgba(5,5,4,.25) 65%)}.review-map{margin-top:1.5rem}.review-map iframe{height:210px}.footer-links{gap:.8rem 1.1rem}.portfolio-heading{font-size:clamp(2.8rem,16vw,4.8rem)}}
'''

if "/* JBM 2.1 refinements */" not in html:
    html = html.replace("</style>", css + "\n</style>", 1)

map_block = '''
<div class="review-map reveal">
  <iframe title="Ubicación de JBM ARQUITECTOS en San José Iturbide" src="https://www.google.com/maps?q=20.9935165,-100.3944233&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  <div class="review-map-info">
    <strong>JBM ARQUITECTOS</strong>
    <p>San José Iturbide, Guanajuato</p>
    <a class="underlink dark" href="https://maps.app.goo.gl/k8FFsKT5fi1p92pv8" target="_blank" rel="noopener">Cómo llegar ↗</a>
  </div>
</div>
'''

if "class=\"review-map reveal\"" not in html:
    marker = '<div class="reviews-score reveal">'
    start = html.find(marker)
    if start != -1:
        close = html.find('</div></div>', start)
        if close != -1:
            insert_at = close + len('</div>')
            html = html[:insert_at] + map_block + html[insert_at:]

if "class=\"footer-links\"" not in html:
    footer_marker = '<div><p>Arquitectura · Interiorismo · Proyecto integral</p><p>© <span data-year=""></span> JBM ARQUITECTOS</p></div>'
    footer_replacement = '''<div><p>Arquitectura · Interiorismo · Proyecto integral</p><p>© <span data-year=""></span> JBM ARQUITECTOS</p><div class="footer-links"><a href="https://www.instagram.com/jbmarquitectos.mx/" target="_blank" rel="noopener">Instagram</a><a href="https://maps.app.goo.gl/k8FFsKT5fi1p92pv8" target="_blank" rel="noopener">Google Maps</a><a href="https://wa.me/524423218552" target="_blank" rel="noopener">WhatsApp</a><a href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank" rel="noopener">Agendar cita</a></div></div>'''
    html = html.replace(footer_marker, footer_replacement, 1)

# Identidad de la sección de portafolio
html = html.replace('<a href="#proyectos">Proyectos</a>', '<a href="#proyectos">Portafolio</a>', 1)
html = html.replace('>Explorar proyectos</a>', '>Explorar portafolio</a>', 1)
html = html.replace(
    '<div class="section-top reveal"><p class="index-label">02 / Proyectos seleccionados</p><a class="underlink dark" href="#contacto">Iniciar un proyecto ↗</a></div>',
    '<div class="section-top reveal"><div><p class="index-label">02 / Portafolio</p><h2 class="display portfolio-heading">PORTAFOLIO</h2></div><a class="underlink dark" href="#contacto">Iniciar un proyecto ↗</a></div>',
    1
)

html = html.replace('>Sonido off</button>', '>Activar sonido</button>')
html = html.replace("soundButton.textContent=heroVideo.muted?'Sonido off':'Sonido on';", "soundButton.textContent=heroVideo.muted?'Activar sonido':'Desactivar sonido';")

path.write_text(html, encoding="utf-8")
print("JBM 2.1 aplicado a", path)
