from pathlib import Path
import re

path = Path('_site/index.html')
html = path.read_text(encoding='utf-8')

# Mantener la depuración editorial previa.
html = re.sub(r'<section class="faq section" id="preguntas">.*?</section>', '', html, count=1, flags=re.S)
html = re.sub(r'<section class="reviews-v4 section" id="opiniones">.*?</section>', '', html, count=1, flags=re.S)
html = html.replace('<a href="#opiniones">Opiniones</a>', '')
html = html.replace('<a href="#estudio">Estudio</a>', '')

# Eliminar por completo el estimador y cualquier acceso o recurso asociado.
html = re.sub(r'<section class="estimator-section section" id="estimador">.*?</section>', '', html, count=1, flags=re.S)
html = re.sub(r'<a href="#estimador">Estimador</a>', '', html)
html = re.sub(r'<link href="assets/css/estimador\.css(?:\?v=[^"]+)?" rel="stylesheet"/?>\s*', '', html)
html = re.sub(r'<script src="assets/js/estimador\.js(?:\?v=[^"]+)?"></script>\s*', '', html)

# Sin estimador, Contacto pasa a ser la sección 06.
for old in ('07 / Contacto', '08 / Contacto', '09 / Contacto', '10 / Contacto', '11 / Contacto'):
    html = html.replace(old, '06 / Contacto')

path.write_text(html, encoding='utf-8')
print('Estimador eliminado de', path)
