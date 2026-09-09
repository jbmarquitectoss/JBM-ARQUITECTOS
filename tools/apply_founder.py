from pathlib import Path
import re

path = Path('_site/index.html')
html = path.read_text(encoding='utf-8')

css_tag = '<link href="assets/css/founder.css" rel="stylesheet"/>'
if css_tag not in html:
    html = html.replace('</head>', css_tag + '\n</head>', 1)

founder = '''<section class="studio founder-studio" id="estudio"><div class="studio-image reveal"><img alt="Jesús Bryan Vargas Martínez, arquitecto fundador de JBM ARQUITECTOS" loading="lazy" src="assets/images/bryan-fundador.svg"/></div><div class="studio-copy section"><p class="index-label reveal">03 / El estudio</p><h2 class="display reveal">Una visión clara detrás de cada proyecto.</h2><p class="founder-name reveal">Jesús Bryan Vargas Martínez</p><p class="founder-role reveal">Arquitecto fundador de JBM ARQUITECTOS</p><p class="founder-bio reveal">Dirige el desarrollo de proyectos residenciales desde la idea inicial hasta su construcción, buscando que cada decisión responda al sitio, a la forma de habitar y a una arquitectura clara y duradera.</p><p class="founder-bio reveal">Desde San José Iturbide, JBM integra diseño arquitectónico, proyecto, interiorismo y construcción de casa habitación bajo una misma visión.</p><div class="founder-disciplines reveal"><span>Arquitectura</span><span>Construcción</span><span>Dirección de proyecto</span></div></div></section>'''

html = re.sub(r'<section class="studio(?: founder-studio)?" id="estudio">.*?</section>', founder, html, count=1, flags=re.S)

path.write_text(html, encoding='utf-8')
print('Fundador JBM integrado en', path)
