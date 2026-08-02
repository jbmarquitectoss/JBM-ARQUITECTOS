from pathlib import Path
import re

INDEX = Path("_site/index.html")

html = INDEX.read_text(encoding="utf-8")

hero = '''
<section class="hero hero-v4" id="inicio">
  <video class="hero-v4-video" autoplay muted loop playsinline preload="metadata" poster="assets/images/hero.webp" aria-hidden="true">
    <source src="jbm-hero.mp4" type="video/mp4">
    <source src="assets/video/jbm-hero.mp4" type="video/mp4">
  </video>
  <div class="hero-v4-fallback" aria-hidden="true"></div>
  <div class="hero-v4-shade"></div>
  <div class="hero-copy hero-v4-copy">
    <p class="kicker reveal">SAN JOSÉ ITURBIDE · GUANAJUATO</p>
    <h1 class="reveal">Diseñamos espacios<br><em>donde ocurren historias.</em></h1>
    <p class="hero-lead reveal">Arquitectura, interiorismo y ejecución bajo una sola visión: crear lugares que respondan a tu forma de vivir.</p>
    <div class="hero-actions reveal">
      <a class="btn btn-light" href="#proyectos">Explorar proyectos</a>
      <a class="underlink" href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank" rel="noopener">Agendar una cita ↗</a>
    </div>
  </div>
  <button class="hero-sound" type="button" aria-pressed="false" aria-label="Activar sonido del video">SONIDO OFF</button>
  <a class="scroll-cue" href="#proyectos"><span>Descubrir</span><i></i></a>
</section>
'''

html = re.sub(r'<section class="hero" id="inicio">.*?</section>', hero, html, count=1, flags=re.S)

trust = '''
<section class="v4-statement section" aria-labelledby="v4-statement-title">
  <p class="index-label reveal">JBM / Filosofía</p>
  <div class="v4-statement-grid">
    <h2 class="display reveal" id="v4-statement-title">El siguiente proyecto que aparecerá aquí podría ser el tuyo.</h2>
    <div class="v4-statement-copy reveal">
      <p>No diseñamos espacios genéricos. Diseñamos alrededor de tus necesidades, tu terreno y la manera en la que quieres vivir.</p>
      <a class="underlink dark" href="#contacto">Comenzar mi proyecto ↗</a>
    </div>
  </div>
</section>

<section class="v4-value section" id="por-que-jbm">
  <div class="section-top reveal">
    <p class="index-label">Por qué JBM</p>
    <p class="section-note">Una sola visión desde la primera idea hasta la materialización.</p>
  </div>
  <div class="v4-value-grid">
    <article class="v4-value-card reveal"><span>01</span><h3>Diseño personalizado</h3><p>Cada propuesta responde a tu estilo de vida, necesidades y contexto.</p></article>
    <article class="v4-value-card reveal"><span>02</span><h3>Proyecto integral</h3><p>Arquitectura, instalaciones, criterio estructural, interiorismo y visualización coordinados.</p></article>
    <article class="v4-value-card reveal"><span>03</span><h3>Acompañamiento profesional</h3><p>Te guiamos con claridad en decisiones, alcances, tiempos y ejecución.</p></article>
    <article class="v4-value-card reveal"><span>04</span><h3>Visualización precisa</h3><p>Renders y documentación que permiten comprender el proyecto antes de construir.</p></article>
  </div>
</section>

<section class="v4-trust section" aria-labelledby="v4-trust-title">
  <div class="v4-trust-score reveal">
    <span class="v4-stars" aria-hidden="true">★★★★★</span>
    <strong>5.0</strong>
    <p>Calificación en Google · 5 opiniones</p>
  </div>
  <div class="v4-trust-copy reveal">
    <p class="index-label">Confianza comprobada</p>
    <h2 class="display" id="v4-trust-title">La experiencia del cliente también forma parte del proyecto.</h2>
    <div class="v4-trust-actions">
      <a class="btn btn-light" href="https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/data=!3m1!4b1!4m6!3m5!1s0x85d4bb4228ed4485:0xc2fbabcd8b8c256e!8m2!3d20.9935165!4d-100.3944233!16s%2Fg%2F11k4sqlyzs" target="_blank" rel="noopener">Ver opiniones ↗</a>
      <a class="underlink" href="https://g.page/r/CW4ljIvNq_vCEAE/review" target="_blank" rel="noopener">Escribir una opinión ↗</a>
    </div>
  </div>
</section>

<section class="v4-final-cta" aria-labelledby="v4-final-title">
  <div class="v4-final-shade"></div>
  <div class="v4-final-content reveal">
    <p class="kicker">TU PROYECTO · NUESTRA SIGUIENTE HISTORIA</p>
    <h2 id="v4-final-title">Cada gran historia comienza con un plano.</h2>
    <p>Cuéntanos cómo imaginas tu proyecto y construyamos juntos el siguiente capítulo de JBM ARQUITECTOS.</p>
    <div class="hero-actions">
      <a class="btn btn-light" href="#contacto">Solicitar proyecto</a>
      <a class="underlink" href="https://wa.me/524423218552?text=Hola%20JBM%20ARQUITECTOS,%20quiero%20platicar%20sobre%20mi%20proyecto." target="_blank" rel="noopener">WhatsApp ↗</a>
    </div>
  </div>
</section>
'''

contact_marker = '<section class="contact section" id="contacto">'
if 'id="por-que-jbm"' not in html and contact_marker in html:
    html = html.replace(contact_marker, trust + '\n' + contact_marker, 1)

styles = '''
<style id="jbm-v4-styles">
.hero-v4-video,.hero-v4-fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero-v4-fallback{background:url("assets/images/hero.webp") center 52%/cover no-repeat;z-index:-1}
.hero-v4-video{z-index:0}
.hero-v4-shade{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(5,5,4,.8),rgba(5,5,4,.18) 72%),linear-gradient(0deg,rgba(5,5,4,.58),transparent 58%)}
.hero-v4-copy{z-index:2}
.hero-sound{position:absolute;z-index:4;right:var(--pad);top:120px;border:1px solid rgba(255,255,255,.5);background:rgba(0,0,0,.22);color:#fff;padding:.65rem .85rem;font-size:.58rem;letter-spacing:.16em;backdrop-filter:blur(12px);cursor:pointer}
.v4-statement{background:#f8f6f1}
.v4-statement-grid{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(280px,.6fr);gap:clamp(3rem,9vw,9rem);align-items:end}
.v4-statement-copy{max-width:480px;color:var(--muted);font-size:1.05rem}
.v4-statement-copy .underlink{margin-top:1.7rem}
.v4-value{background:var(--paper)}
.v4-value-grid{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-left:1px solid var(--line)}
.v4-value-card{padding:clamp(1.5rem,3vw,3rem);min-height:330px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);display:flex;flex-direction:column}
.v4-value-card span{font-size:.64rem;letter-spacing:.16em;color:var(--muted)}
.v4-value-card h3{font-family:var(--display);font-size:clamp(1.8rem,2.6vw,3rem);font-weight:400;line-height:1.05;margin:auto 0 1.2rem}
.v4-value-card p{margin:0;color:var(--muted)}
.v4-trust{background:var(--ink);color:#fff;display:grid;grid-template-columns:.7fr 1.3fr;gap:clamp(3rem,9vw,10rem);align-items:center}
.v4-trust-score{border-top:1px solid rgba(255,255,255,.25);padding-top:1.5rem}
.v4-stars{display:block;letter-spacing:.14em;color:var(--accent)}
.v4-trust-score strong{display:block;font-family:var(--display);font-size:clamp(6rem,13vw,13rem);font-weight:400;line-height:.86;margin:.8rem 0}
.v4-trust-score p{color:rgba(255,255,255,.58);text-transform:uppercase;font-size:.65rem;letter-spacing:.13em}
.v4-trust-copy .display{font-size:clamp(3rem,5.5vw,6rem)}
.v4-trust-actions{display:flex;align-items:center;gap:2rem;margin-top:2.5rem}
.v4-final-cta{position:relative;min-height:90svh;display:flex;align-items:flex-end;padding:8rem var(--pad);color:#fff;background:url("assets/images/facade.webp") center/cover no-repeat}
.v4-final-shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(4,4,4,.82),rgba(4,4,4,.18)),linear-gradient(0deg,rgba(4,4,4,.68),transparent)}
.v4-final-content{position:relative;z-index:2;max-width:1050px}
.v4-final-content h2{font-family:var(--display);font-size:clamp(4rem,8vw,8.5rem);font-weight:400;line-height:.93;margin:0}
.v4-final-content>p:not(.kicker){max-width:620px;font-size:1.08rem;color:rgba(255,255,255,.76)}
@media(max-width:900px){.v4-statement-grid,.v4-trust{grid-template-columns:1fr}.v4-value-grid{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.hero-sound{top:auto;bottom:1.25rem;right:1.25rem}.v4-value-grid{grid-template-columns:1fr}.v4-value-card{min-height:260px}.v4-trust-actions{align-items:flex-start;flex-direction:column}.v4-final-cta{min-height:78svh;padding-bottom:5rem}}
</style>
'''

if 'id="jbm-v4-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

script = '''
<script id="jbm-v4-script">
(() => {
  const video = document.querySelector('.hero-v4-video');
  const button = document.querySelector('.hero-sound');
  if (!video || !button) return;
  const sync = () => {
    button.textContent = video.muted ? 'SONIDO OFF' : 'SONIDO ON';
    button.setAttribute('aria-pressed', String(!video.muted));
  };
  button.addEventListener('click', async () => {
    video.muted = !video.muted;
    try { await video.play(); } catch (_) {}
    sync();
  });
  video.addEventListener('error', () => video.style.display = 'none');
  sync();
})();
</script>
'''
if 'id="jbm-v4-script"' not in html:
    html = html.replace('</body>', script + '\n</body>', 1)

INDEX.write_text(html, encoding="utf-8")
print("JBM ARQUITECTOS V4 construida correctamente")
