from pathlib import Path

INDEX = Path("_site/index.html")

GOOGLE_REVIEW_URL = "https://g.page/r/CW4ljIvNq_vCEAE/review"
GOOGLE_MAPS_URL = "https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/data=!3m1!4b1!4m6!3m5!1s0x85d4bb4228ed4485:0xc2fbabcd8b8c256e!8m2!3d20.9935165!4d-100.3944233!16s%2Fg%2F11k4sqlyzs?entry=ttu"

section = f'''
<section class="reviews-section section" id="opiniones" aria-labelledby="reviews-title">
  <div class="reviews-head reveal">
    <div>
      <p class="index-label">08 / Opiniones</p>
      <h2 class="display" id="reviews-title">La confianza también se construye.</h2>
    </div>
    <div class="reviews-score" aria-label="Calificación 5 de 5 basada en 5 opiniones de Google">
      <div class="reviews-stars" aria-hidden="true">★★★★★</div>
      <strong>5.0</strong>
      <span>5 opiniones en Google</span>
    </div>
  </div>

  <div class="reviews-carousel reveal" data-reviews-carousel>
    <article class="review-card is-active" data-review>
      <div class="review-card-top">
        <span class="review-source">Opinión en Google</span>
        <span class="review-stars" aria-label="5 estrellas">★★★★★</span>
      </div>
      <blockquote>“Deseo expresar mi más sincero agradecimiento por el excelente trabajo realizado en mi proyecto. Desde el primer día, ha sido evidente su profesionalismo y la apertura de criterio que los caracteriza como arquitectos.”</blockquote>
      <footer>
        <strong>Julio Cesar Chavez</strong>
        <span>Cliente de JBM ARQUITECTOS</span>
      </footer>
    </article>

    <article class="review-card" data-review>
      <div class="review-card-top">
        <span class="review-source">Opinión en Google</span>
        <span class="review-stars" aria-label="5 estrellas">★★★★★</span>
      </div>
      <blockquote>“Trabajar con JBM ha sido una experiencia excepcional. Desde el primer momento me sorprendió su profesionalismo y atención al cliente; su habilidad de interpretar mis ideas y convertirlas en un diseño innovador superó todas mis expectativas.”</blockquote>
      <footer>
        <strong>Rojas Antonio</strong>
        <span>Cliente de JBM ARQUITECTOS</span>
      </footer>
    </article>

    <div class="reviews-controls" aria-label="Controles de opiniones">
      <button type="button" class="reviews-arrow" data-review-prev aria-label="Opinión anterior">←</button>
      <div class="reviews-dots" role="tablist" aria-label="Seleccionar opinión">
        <button type="button" class="is-active" data-review-dot="0" aria-label="Ver opinión 1"></button>
        <button type="button" data-review-dot="1" aria-label="Ver opinión 2"></button>
      </div>
      <button type="button" class="reviews-arrow" data-review-next aria-label="Opinión siguiente">→</button>
    </div>
  </div>

  <div class="reviews-actions reveal">
    <div>
      <span>Calificación pública</span>
      <p>★★★★★ <strong>5.0</strong> · 5 opiniones</p>
    </div>
    <div class="reviews-buttons">
      <a class="btn btn-light" href="{GOOGLE_MAPS_URL}" target="_blank" rel="noopener">Leer en Google Maps ↗</a>
      <a class="underlink" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener">Escribir una opinión ↗</a>
    </div>
  </div>
</section>
'''

styles = r'''
<style id="reviews-section-styles">
.reviews-section{background:#11110f;color:#f4f0e7;position:relative;overflow:hidden}
.reviews-section:before{content:"5.0";position:absolute;right:-.03em;bottom:-.22em;font-family:var(--display);font-size:clamp(13rem,31vw,36rem);line-height:1;color:rgba(255,255,255,.025);pointer-events:none}
.reviews-head{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:clamp(2rem,7vw,8rem);align-items:end;margin-bottom:clamp(3rem,7vw,6rem)}
.reviews-section .index-label{color:rgba(255,255,255,.58)}
.reviews-section .display{max-width:900px;margin-top:1.1rem;color:#f4f0e7}
.reviews-score{display:grid;grid-template-columns:auto auto;column-gap:1rem;align-items:end;min-width:235px;padding-top:1rem;border-top:1px solid rgba(255,255,255,.22)}
.reviews-score strong{font-family:var(--display);font-size:clamp(3.8rem,7vw,7rem);line-height:.85;font-weight:400}
.reviews-score span{grid-column:1/-1;margin-top:.7rem;font-size:.66rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.58)}
.reviews-stars,.review-stars{font-size:.8rem;letter-spacing:.14em;color:#f5c84b}
.reviews-stars{margin-bottom:.65rem}
.reviews-carousel{position:relative;z-index:1;border-top:1px solid rgba(255,255,255,.18);border-bottom:1px solid rgba(255,255,255,.18);min-height:clamp(430px,48vw,650px);display:flex;align-items:stretch}
.review-card{position:absolute;inset:0;padding:clamp(2.2rem,6vw,6rem);display:flex;flex-direction:column;justify-content:space-between;gap:3rem;opacity:0;transform:translateX(35px);pointer-events:none;transition:opacity .55s ease,transform .55s ease}
.review-card.is-active{opacity:1;transform:none;pointer-events:auto}
.review-card-top{display:flex;justify-content:space-between;align-items:center;gap:1rem}
.review-source{font-size:.66rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.review-card blockquote{max-width:1150px;margin:0;font-family:var(--display);font-size:clamp(2.1rem,4.7vw,5.2rem);font-weight:400;line-height:1.08}
.review-card footer{display:flex;flex-direction:column;gap:.35rem;padding-top:1.4rem;border-top:1px solid rgba(255,255,255,.16);max-width:430px}
.review-card footer strong{font-size:.78rem;letter-spacing:.13em;text-transform:uppercase}
.review-card footer span{font-size:.78rem;color:rgba(255,255,255,.58)}
.reviews-controls{position:absolute;z-index:3;right:clamp(1rem,3vw,3rem);bottom:clamp(1rem,3vw,2rem);display:flex;align-items:center;gap:1rem}
.reviews-arrow{width:3rem;height:3rem;border:1px solid rgba(255,255,255,.25);border-radius:50%;background:transparent;color:#fff;cursor:pointer;font-size:1rem;transition:background .25s ease,color .25s ease}
.reviews-arrow:hover,.reviews-arrow:focus-visible{background:#f4f0e7;color:#11110f}
.reviews-dots{display:flex;gap:.45rem}
.reviews-dots button{width:1.8rem;height:2px;border:0;background:rgba(255,255,255,.25);padding:0;cursor:pointer;transition:background .25s ease,width .25s ease}
.reviews-dots button.is-active{width:3rem;background:#f4f0e7}
.reviews-actions{position:relative;z-index:1;display:flex;justify-content:space-between;align-items:center;gap:2rem;padding-top:1.5rem;margin-top:1.2rem}
.reviews-actions>div:first-child span{font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.5)}
.reviews-actions p{margin:.4rem 0 0;color:#f5c84b;letter-spacing:.08em}
.reviews-actions p strong{color:#f4f0e7}
.reviews-buttons{display:flex;align-items:center;gap:1.3rem;flex-wrap:wrap;justify-content:flex-end}
.reviews-section .underlink{color:#f4f0e7}
@media(max-width:900px){
  .reviews-head{grid-template-columns:1fr}
  .reviews-score{max-width:290px}
  .reviews-carousel{min-height:570px}
  .reviews-actions{align-items:flex-start;flex-direction:column}
  .reviews-buttons{justify-content:flex-start}
}
@media(max-width:620px){
  .reviews-carousel{min-height:650px}
  .review-card{padding:2rem 0 5.5rem}
  .review-card blockquote{font-size:clamp(1.85rem,8vw,2.7rem)}
  .reviews-controls{right:0;bottom:1.2rem}
  .reviews-buttons{width:100%;align-items:flex-start;flex-direction:column}
  .reviews-buttons .btn{width:100%}
}
</style>
'''

script = r'''
<script id="reviews-carousel-script">
(() => {
  const root = document.querySelector('[data-reviews-carousel]');
  if (!root) return;
  const slides = [...root.querySelectorAll('[data-review]')];
  const dots = [...root.querySelectorAll('[data-review-dot]')];
  const prev = root.querySelector('[data-review-prev]');
  const next = root.querySelector('[data-review-next]');
  let index = 0;
  let timer;

  const show = (nextIndex) => {
    index = (nextIndex + slides.length) % slides.length;
    slides.forEach((slide, i) => slide.classList.toggle('is-active', i === index));
    dots.forEach((dot, i) => dot.classList.toggle('is-active', i === index));
  };

  const restart = () => {
    clearInterval(timer);
    timer = setInterval(() => show(index + 1), 6500);
  };

  prev?.addEventListener('click', () => { show(index - 1); restart(); });
  next?.addEventListener('click', () => { show(index + 1); restart(); });
  dots.forEach((dot, i) => dot.addEventListener('click', () => { show(i); restart(); }));
  root.addEventListener('mouseenter', () => clearInterval(timer));
  root.addEventListener('mouseleave', restart);

  show(0);
  restart();
})();
</script>
'''

html = INDEX.read_text(encoding="utf-8")
marker = '<section class="contact section" id="contacto">'

if 'id="opiniones"' not in html:
    if marker not in html:
        raise SystemExit("No se encontró la sección de contacto para insertar opiniones")
    html = html.replace(marker, section + "\n" + marker, 1)

if 'id="reviews-section-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)

if 'id="reviews-carousel-script"' not in html:
    html = html.replace('</body>', script + '\n</body>', 1)

INDEX.write_text(html, encoding="utf-8")
print("Reseñas reales de Google integradas correctamente")
