from pathlib import Path

INDEX = Path("_site/index.html")
CALENDAR = "https://calendar.app.google/h7XwWw9xizAmMNz38"

markup = f'''
<div class="jbm-loader" aria-hidden="true"><div class="jbm-loader-mark"><span>JBM</span><small>ARQUITECTOS</small><i></i></div></div>
<div class="jbm-cursor" aria-hidden="true"><span>Explorar</span></div>
<aside class="jbm-idle-invite" role="dialog" aria-label="Invitación para agendar una reunión">
  <button type="button" aria-label="Cerrar">×</button>
  <span>¿Ya imaginaste cómo se verá tu proyecto?</span>
  <a href="{CALENDAR}" target="_blank" rel="noopener">Agenda una reunión ↗</a>
</aside>
'''

styles = r'''
<style id="jbm-interaction-styles">
.jbm-loader{position:fixed;z-index:99999;inset:0;display:grid;place-items:center;background:#11110f;color:#fff;transition:opacity .7s ease,visibility .7s ease}
.jbm-loader.is-hidden{opacity:0;visibility:hidden}
.jbm-loader-mark{position:relative;text-align:center;padding:2rem 3rem}
.jbm-loader-mark span{display:block;font-family:var(--display,serif);font-size:clamp(4rem,10vw,9rem);line-height:.85;letter-spacing:-.04em}
.jbm-loader-mark small{display:block;margin-top:1rem;font-size:.62rem;letter-spacing:.45em}
.jbm-loader-mark i{position:absolute;left:0;right:0;bottom:0;height:1px;background:rgba(255,255,255,.18);overflow:hidden}
.jbm-loader-mark i:after{content:"";display:block;width:38%;height:100%;background:#fff;animation:jbmLoad 1.4s ease-in-out infinite}
@keyframes jbmLoad{from{transform:translateX(-110%)}to{transform:translateX(370%)}}
.jbm-cursor{position:fixed;z-index:9999;left:0;top:0;width:74px;height:74px;margin:-37px 0 0 -37px;border-radius:50%;display:grid;place-items:center;background:rgba(17,17,15,.86);color:#fff;pointer-events:none;opacity:0;transform:scale(.7);transition:opacity .2s,transform .2s;backdrop-filter:blur(8px)}
.jbm-cursor span{font-size:.58rem;letter-spacing:.12em;text-transform:uppercase}
.jbm-cursor.is-visible{opacity:1;transform:scale(1)}
.jbm-idle-invite{position:fixed;z-index:7000;right:1.2rem;bottom:1.2rem;width:min(390px,calc(100vw - 2.4rem));padding:1.4rem 1.5rem;background:#11110f;color:#fff;border:1px solid rgba(255,255,255,.18);box-shadow:0 20px 60px rgba(0,0,0,.28);transform:translateY(130%);opacity:0;transition:transform .5s ease,opacity .5s ease}
.jbm-idle-invite.is-visible{transform:translateY(0);opacity:1}
.jbm-idle-invite button{position:absolute;right:.8rem;top:.65rem;background:none;border:0;color:#fff;font-size:1.3rem;cursor:pointer}
.jbm-idle-invite span{display:block;font-family:var(--display,serif);font-size:1.6rem;line-height:1.08;padding-right:2rem;margin-bottom:1.2rem}
.jbm-idle-invite a{font-size:.65rem;letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,.5);padding-bottom:.3rem}
body.jbm-evening .jbm-cinematic-shade{background:linear-gradient(180deg,rgba(0,0,0,.28),rgba(0,0,0,.45) 45%,rgba(0,0,0,.86))}
@media(pointer:coarse),(max-width:900px){.jbm-cursor{display:none}}
@media(prefers-reduced-motion:reduce){.jbm-loader-mark i:after{animation:none}.jbm-loader{display:none}.jbm-idle-invite{transition:none}}
</style>
'''

script = r'''
<script id="jbm-interactions-script">
(() => {
  const loader = document.querySelector('.jbm-loader');
  const hideLoader = () => loader && loader.classList.add('is-hidden');
  window.addEventListener('load', () => setTimeout(hideLoader, 450), {once:true});
  setTimeout(hideLoader, 3500);

  const hour = new Date().getHours();
  if (hour >= 19 || hour < 7) document.body.classList.add('jbm-evening');

  const cursor = document.querySelector('.jbm-cursor');
  const targets = 'a, button, .project-card, .instagram-card, .gallery-item, img';
  if (cursor && matchMedia('(pointer:fine)').matches) {
    document.addEventListener('mousemove', e => {
      cursor.style.transform = `translate(${e.clientX}px,${e.clientY}px) scale(${cursor.classList.contains('is-visible') ? 1 : .7})`;
    });
    document.querySelectorAll(targets).forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('is-visible'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('is-visible'));
    });
  }

  const invite = document.querySelector('.jbm-idle-invite');
  let idleTimer;
  const armInvite = () => {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => {
      if (invite && !sessionStorage.getItem('jbmInviteClosed')) invite.classList.add('is-visible');
    }, 22000);
  };
  ['mousemove','keydown','scroll','touchstart'].forEach(evt => addEventListener(evt, armInvite, {passive:true}));
  armInvite();
  invite?.querySelector('button')?.addEventListener('click', () => {
    invite.classList.remove('is-visible');
    sessionStorage.setItem('jbmInviteClosed','1');
  });

  document.querySelectorAll('video').forEach(video => {
    video.muted = true;
    const attempt = video.play();
    if (attempt?.catch) attempt.catch(() => video.setAttribute('controls',''));
  });
})();
</script>
'''

html = INDEX.read_text(encoding="utf-8")
if 'class="jbm-loader"' not in html:
    pos = html.lower().find('<body')
    if pos >= 0:
        close = html.find('>', pos)
        html = html[:close+1] + '\n' + markup + html[close+1:]
if 'id="jbm-interaction-styles"' not in html:
    html = html.replace('</head>', styles + '\n</head>', 1)
if 'id="jbm-interactions-script"' not in html:
    html = html.replace('</body>', script + '\n</body>', 1)
INDEX.write_text(html, encoding="utf-8")
print("Microinteracciones JBM integradas")
