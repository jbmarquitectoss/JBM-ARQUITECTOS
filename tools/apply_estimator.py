from pathlib import Path

path = Path('_site/index.html')
html = path.read_text(encoding='utf-8')

css_tag = '<link href="assets/css/estimador.css" rel="stylesheet"/>'
js_tag = '<script src="assets/js/estimador.js"></script>'

if css_tag not in html:
    html = html.replace('</head>', css_tag + '\n</head>', 1)

# Eliminar Preguntas frecuentes para mantener una página más minimalista.
faq_start = html.find('<section class="faq section" id="preguntas">')
if faq_start != -1:
    faq_end = html.find('</section>', faq_start)
    if faq_end != -1:
        html = html[:faq_start] + html[faq_end + len('</section>'):]

# Eliminar por completo la sección de opiniones y su acceso en el menú.
reviews_start = html.find('<section class="reviews-v4 section" id="opiniones">')
if reviews_start != -1:
    reviews_end = html.find('</section>', reviews_start)
    if reviews_end != -1:
        html = html[:reviews_start] + html[reviews_end + len('</section>'):]

html = html.replace('<a href="#opiniones">Opiniones</a>', '')
# Mantener la sección Estudio dentro de la página, pero quitar su acceso de la barra principal.
html = html.replace('<a href="#estudio">Estudio</a>', '')

section = r'''
<section class="estimator-section section" id="estimador">
  <div class="section-top reveal">
    <p class="index-label">07 / Estimador de inversión</p>
    <p class="section-note">Una referencia inicial antes de preparar una cotización personalizada.</p>
  </div>
  <div class="estimator-intro">
    <h2 class="display reveal">Conoce una referencia aproximada para tu proyecto.</h2>
    <p class="reveal">Selecciona el servicio, introduce los datos básicos y obtén una referencia preliminar. El resultado no constituye una cotización definitiva.</p>
  </div>
  <div class="estimator-shell reveal">
    <div class="estimator-tabs" role="tablist" aria-label="Tipo de estimación">
      <button class="estimator-tab" type="button" role="tab" aria-selected="true" data-estimator-tab="executive"><span>01</span><strong>Proyecto ejecutivo</strong></button>
      <button class="estimator-tab" type="button" role="tab" aria-selected="false" tabindex="-1" data-estimator-tab="construction"><span>02</span><strong>Construcción de casa</strong></button>
    </div>

    <div class="estimator-panel active" data-estimator-panel="executive">
      <div class="estimator-form">
        <h3>Proyecto ejecutivo para planos</h3>
        <p>Obtén una referencia para desarrollar la documentación necesaria de una casa habitación.</p>
        <div class="estimator-fields">
          <div class="estimator-field">
            <label for="exec-area">Superficie aproximada de construcción</label>
            <input id="exec-area" name="exec-area" type="number" inputmode="numeric" min="40" step="1" placeholder="Ej. 180"/>
            <span class="estimator-help">Metros cuadrados aproximados.</span>
          </div>
          <div class="estimator-field">
            <label for="exec-levels">Número de niveles</label>
            <select id="exec-levels" name="exec-levels">
              <option value="one">1 nivel</option>
              <option value="two" selected>2 niveles</option>
              <option value="three">3 niveles o más</option>
            </select>
          </div>
        </div>
        <div class="estimator-actions"><button class="estimator-calc" type="button" data-calc="executive">Calcular referencia</button></div>
        <p class="estimator-disclaimer">Base JBM: $180 MXN/m² de diseño. Estimación preliminar sujeta a alcance, complejidad y condiciones del proyecto.</p>
      </div>
      <aside class="estimator-result" aria-live="polite">
        <p class="estimator-result-empty">Completa los datos para conocer una referencia estimada de inversión.</p>
        <div class="estimator-result-content" hidden>
          <span class="estimator-result-eyebrow">Inversión estimada</span>
          <p class="estimator-result-amount" data-result-amount></p>
          <p class="estimator-result-copy" data-result-copy></p>
          <div class="estimator-result-details" data-result-details></div>
          <div class="estimator-scope"><strong>Alcance considerado</strong><p data-result-scope></p></div>
          <a class="estimator-whatsapp" data-result-whatsapp href="#" target="_blank" rel="noopener">Solicitar cotización personalizada ↗</a>
        </div>
      </aside>
    </div>

    <div class="estimator-panel" data-estimator-panel="construction">
      <div class="estimator-form">
        <h3>Construcción de casa habitación</h3>
        <p>Calcula una referencia inicial según la superficie aproximada de construcción.</p>
        <div class="estimator-fields">
          <div class="estimator-field">
            <label for="build-area">Superficie aproximada de construcción</label>
            <input id="build-area" name="build-area" type="number" inputmode="numeric" min="40" step="1" placeholder="Ej. 200"/>
            <span class="estimator-help">Metros cuadrados aproximados.</span>
          </div>
          <div class="estimator-field">
            <label for="build-levels">Número de niveles</label>
            <select id="build-levels" name="build-levels">
              <option value="one">1 nivel</option>
              <option value="two" selected>2 niveles</option>
              <option value="three">3 niveles o más</option>
            </select>
          </div>
          <div class="estimator-field">
            <label for="build-finish">Nivel de acabados</label>
            <select id="build-finish" name="build-finish">
              <option value="standard">Estándar contemporáneo</option>
              <option value="residential" selected>Residencial</option>
              <option value="premium">Premium</option>
            </select>
          </div>
          <div class="estimator-field">
            <label for="build-terrain">Condición general del terreno</label>
            <select id="build-terrain" name="build-terrain">
              <option value="flat" selected>Plano / regular</option>
              <option value="medium">Desnivel moderado</option>
              <option value="slope">Pendiente o condición especial</option>
            </select>
          </div>
        </div>
        <div class="estimator-actions"><button class="estimator-calc" type="button" data-calc="construction">Calcular referencia</button></div>
        <p class="estimator-disclaimer">Base JBM: desde $12,000 MXN/m². El presupuesto definitivo requiere proyecto ejecutivo, revisión del sitio y especificación de materiales.</p>
      </div>
      <aside class="estimator-result" aria-live="polite">
        <p class="estimator-result-empty">Completa los datos para conocer una referencia estimada de inversión.</p>
        <div class="estimator-result-content" hidden>
          <span class="estimator-result-eyebrow">Inversión estimada</span>
          <p class="estimator-result-amount" data-result-amount></p>
          <p class="estimator-result-copy" data-result-copy></p>
          <div class="estimator-result-details" data-result-details></div>
          <div class="estimator-scope"><strong>Alcance considerado</strong><p data-result-scope></p></div>
          <a class="estimator-whatsapp" data-result-whatsapp href="#" target="_blank" rel="noopener">Solicitar cotización personalizada ↗</a>
        </div>
      </aside>
    </div>
  </div>
</section>
'''

if 'id="estimador"' not in html:
    marker = '<section class="cta-v4 section">'
    html = html.replace(marker, section + '\n' + marker, 1)

if '<a href="#estimador">Estimador</a>' not in html:
    html = html.replace('<a href="#contacto">Contacto</a>', '<a href="#estimador">Estimador</a><a href="#contacto">Contacto</a>', 1)

# Corregir numeración después de eliminar Opiniones y Preguntas frecuentes.
for old in ('09 / Estimador de inversión', '08 / Estimador de inversión'):
    html = html.replace(old, '07 / Estimador de inversión')
for old in ('10 / Tu proyecto', '09 / Tu proyecto'):
    html = html.replace(old, '08 / Tu proyecto')
for old in ('11 / Contacto', '10 / Contacto'):
    html = html.replace(old, '09 / Contacto')

if js_tag not in html:
    html = html.replace('</body>', js_tag + '\n</body>', 1)

path.write_text(html, encoding='utf-8')
print('Estimador JBM aplicado a', path)
