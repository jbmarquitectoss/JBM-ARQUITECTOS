from pathlib import Path
import re

path = Path('_site/index.html')
html = path.read_text(encoding='utf-8')

css_tag = '<link href="assets/css/refinement.css" rel="stylesheet"/>'
if css_tag not in html:
    html = html.replace('</head>', css_tag + '\n</head>', 1)

# Menú: solo lo esencial.
menu = '''<nav class="menu" id="main-menu"><a href="#proyectos">Portafolio</a><a href="#servicios">Servicios</a><a href="#estimador">Estimador</a><a class="menu-booking" href="https://calendar.app.google/h7XwWw9xizAmMNz38" rel="noopener" target="_blank">Agendar cita ↗</a></nav>'''
html = re.sub(r'<nav class="menu" id="main-menu">.*?</nav>', menu, html, count=1, flags=re.S)

# Hero y portafolio.
html = html.replace('Explorar proyectos', 'Explorar portafolio')
html = html.replace('02 / Proyectos seleccionados', '02 / Portafolio')

# El estudio: reforzar que JBM diseña y construye sin cargar de texto.
html = html.replace(
    'Acompañamos cada proyecto desde la primera conversación hasta su materialización, coordinando arquitectura, interiores, visualización y obra.',
    'Diseñamos y construimos proyectos residenciales bajo una sola visión, desde la primera conversación hasta su materialización.'
)
html = html.replace(
    'Nuestro trabajo busca equilibrio entre claridad funcional, identidad y permanencia.',
    'Arquitectura, proyecto ejecutivo, interiorismo y construcción coordinados desde un mismo estudio.'
)

# Eliminar bloques que repiten argumentos comerciales.
html = re.sub(r'<section class="trust-section section">.*?</section>', '', html, count=1, flags=re.S)

# Sección visual de arquitectura + construcción.
construction = '''
<section class="construction-feature" id="construccion">
  <div class="construction-feature-media"><img src="assets/images/casa-baeza-01-fachada-dia.webp" alt="Arquitectura residencial de JBM ARQUITECTOS" loading="lazy"/></div>
  <div class="construction-feature-shade"></div>
  <div class="construction-feature-copy">
    <p class="index-label reveal">04 / Arquitectura + Construcción</p>
    <h2 class="reveal">Diseñamos y construimos casa habitación residencial.</h2>
    <p class="reveal">Un mismo equipo coordina proyecto, documentación y ejecución para mantener continuidad entre la idea arquitectónica y la obra construida.</p>
    <div class="construction-feature-actions reveal"><a class="btn btn-light" href="#estimador">Estimar inversión ↗</a><a class="underlink" href="https://calendar.app.google/h7XwWw9xizAmMNz38" rel="noopener" target="_blank">Hablar de mi proyecto ↗</a></div>
  </div>
</section>
'''
if 'id="construccion"' not in html:
    html = html.replace('<section class="work-process section" id="proceso">', construction + '\n<section class="work-process section" id="proceso">', 1)

# Reordenar numeración de proceso y servicios.
html = html.replace('04 / Proceso', '05 / Proceso')
html = html.replace('05 / Servicios', '06 / Servicios')

# Servicios: menos dispersión y más peso comercial.
services = '''<section class="services section" id="servicios"><div class="section-top reveal"><p class="index-label">06 / Servicios</p><p class="section-note">Diseño y construcción bajo una sola visión.</p></div><div class="service-rows"><article class="service reveal"><span>01</span><h3>Diseño arquitectónico</h3><p>Concepto, anteproyecto, distribución, materialidad y visualización 3D para definir el proyecto con claridad.</p></article><article class="service reveal"><span>02</span><h3>Proyecto ejecutivo</h3><p>Planos arquitectónicos y documentación técnica para llevar el diseño a una etapa lista para construcción.</p></article><article class="service reveal"><span>03</span><h3>Construcción residencial</h3><p>Ejecución integral de casa habitación residencial, coordinando obra, calidad, tiempos y decisiones de proyecto.</p></article><article class="service reveal"><span>04</span><h3>Interiorismo</h3><p>Materiales, iluminación, mobiliario y atmósferas integradas al lenguaje arquitectónico.</p></article><article class="service reveal"><span>05</span><h3>Supervisión de obra</h3><p>Seguimiento técnico para proteger la intención del proyecto durante su ejecución.</p></article></div></section>'''
html = re.sub(r'<section class="services section" id="servicios">.*?</section>', services, html, count=1, flags=re.S)

# El estimador conserva el número 07 después de la nueva sección de construcción.
for old in ('06 / Estimador de inversión', '08 / Estimador de inversión'):
    html = html.replace(old, '07 / Estimador de inversión')

# CTA final: más corto y directo.
cta = '''<section class="cta-v4 section"><div><p class="index-label reveal">08 / Tu proyecto</p><h2 class="display reveal">Hablemos de tu próximo proyecto.</h2><div class="hero-actions reveal"><a class="btn btn-light" href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank" rel="noopener">Agendar una reunión ↗</a><a class="underlink" href="https://wa.me/524423218552?text=Hola%20JBM%20ARQUITECTOS,%20quiero%20platicar%20sobre%20mi%20proyecto." target="_blank" rel="noopener">Escribir por WhatsApp ↗</a></div></div></section>'''
html = re.sub(r'<section class="cta-v4 section">.*?</section>', cta, html, count=1, flags=re.S)

# Contacto y footer.
html = html.replace('10 / Contacto', '09 / Contacto')
html = html.replace('Arquitectura · Interiorismo · Proyecto integral', 'Arquitectura · Construcción · Interiorismo')

path.write_text(html, encoding='utf-8')
print('Refinamiento editorial JBM aplicado a', path)
