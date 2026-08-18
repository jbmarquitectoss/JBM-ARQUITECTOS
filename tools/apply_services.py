from pathlib import Path

path = Path('_site/index.html')
html = path.read_text(encoding='utf-8')

construction = '<article class="service reveal"><span>04</span><h3>Construcción</h3><p>Construcción integral de casa habitación residencial, desde la planeación y coordinación de obra hasta la ejecución y entrega.</p></article>'
supervision_old = '<article class="service reveal"><span>04</span><h3>Supervisión de obra</h3><p>Seguimiento técnico para proteger la intención del proyecto.</p></article>'
supervision_new = '<article class="service reveal"><span>05</span><h3>Supervisión de obra</h3><p>Seguimiento técnico para proteger la intención del proyecto.</p></article>'

if '<h3>Construcción</h3>' not in html and supervision_old in html:
    html = html.replace(supervision_old, construction + supervision_new, 1)
elif '<h3>Construcción</h3>' in html:
    html = html.replace(supervision_old, supervision_new, 1)

path.write_text(html, encoding='utf-8')
print('Servicios JBM actualizados en', path)
