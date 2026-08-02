from pathlib import Path

SITE = Path('_site')
(SITE / 'assets/css').mkdir(parents=True, exist_ok=True)
(SITE / 'assets/js').mkdir(parents=True, exist_ok=True)

html = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JBM ARQUITECTOS | Arquitectura e interiorismo en Guanajuato</title>
<meta name="description" content="JBM ARQUITECTOS desarrolla arquitectura residencial, interiorismo y proyectos integrales en San José Iturbide, Guanajuato y el Bajío.">
<link rel="canonical" href="https://jbmarquitectos.mx/">
<meta property="og:title" content="JBM ARQUITECTOS | Arquitectura que permanece">
<meta property="og:description" content="Arquitectura residencial, interiorismo y ejecución integral.">
<meta property="og:image" content="https://jbmarquitectos.mx/assets/images/hero.webp">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Italiana&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/v3.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P9FECXB3LV"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-P9FECXB3LV');</script>
</head>
<body>
<div class="loader"><div><b>JBM</b><span>ARQUITECTOS</span></div></div>
<header class="topbar">
<a class="brand" href="#inicio"><img src="assets/images/logo-horizontal.png" alt="JBM ARQUITECTOS"></a>
<nav><a href="#proyectos">Proyectos</a><a href="#proceso">Proceso</a><a href="#opiniones">Opiniones</a><a href="#contacto">Contacto</a></nav>
<a class="book" href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank" rel="noopener">Agendar cita ↗</a>
</header>
<main>
<section class="hero" id="inicio">
<video id="heroVideo" autoplay muted loop playsinline poster="assets/images/hero.webp">
<source src="assets/video/jbm-hero.mp4" type="video/mp4">
<source src="jbm-hero.mp4" type="video/mp4">
<source src="assets/jbm-hero.mp4" type="video/mp4">
</video>
<div class="hero-fallback"></div><div class="shade"></div>
<div class="hero-copy"><p>ARQUITECTURA · INTERIORISMO · EJECUCIÓN</p><h1>Diseñamos la forma<br><em>en la que vivirás.</em></h1><div id="rotatingLine">Cada detalle tiene un propósito.</div><a href="#proyectos">Explorar proyectos ↓</a></div>
<button class="sound" id="soundToggle" type="button">Activar sonido</button>
</section>
<section class="statement reveal"><p>El siguiente proyecto que aparecerá aquí…</p><h2>podría ser el tuyo.</h2><a href="#contacto">Hablemos de tu proyecto ↗</a></section>
<section class="projects" id="proyectos">
<div class="section-head reveal"><span>01 / Proyectos seleccionados</span><h2>Arquitectura que se vive.</h2></div>
<a class="project reveal" href="casa-gh.html"><img src="assets/images/facade.webp" alt="CASA GH"><div><span>01</span><h3>CASA GH</h3><p>Residencial Villa Corzo · San José Iturbide · 320 m²</p></div></a>
<a class="project reverse reveal" href="casa-baeza.html"><img src="assets/images/casa-baeza-18-fachada-noche.webp" alt="CASA BAEZA"><div><span>02</span><h3>CASA BAEZA</h3><p>San José Campestre · Remodelación e interiorismo · 170 m²</p></div></a>
</section>
<section class="manifesto reveal"><p>La arquitectura no comienza con un plano.</p><h2>Comienza escuchando a quien va a vivirla.</h2></section>
<section class="process" id="proceso"><div class="section-head reveal"><span>02 / Nuestro proceso</span><h2>Una ruta clara, de la idea a la obra.</h2></div><div class="steps">
<article class="reveal"><b>01</b><h3>Conocerte</h3><p>Necesidades, terreno, presupuesto y visión.</p></article><article class="reveal"><b>02</b><h3>Escuchar</h3><p>Programa arquitectónico y prioridades reales.</p></article><article class="reveal"><b>03</b><h3>Diseñar</h3><p>Concepto, distribución, materialidad y visualización.</p></article><article class="reveal"><b>04</b><h3>Documentar</h3><p>Proyecto ejecutivo, criterios y detalles.</p></article><article class="reveal"><b>05</b><h3>Construir</h3><p>Coordinación y seguimiento de obra.</p></article><article class="reveal"><b>06</b><h3>Entregar</h3><p>Un espacio listo para vivirse.</p></article>
</div></section>
<section class="services"><div class="section-head reveal"><span>03 / Diseñamos para</span><h2>Espacios con identidad y permanencia.</h2></div><div class="service-list"><span>Casas residenciales</span><span>Remodelaciones</span><span>Interiorismo</span><span>Proyectos comerciales</span><span>Proyecto ejecutivo</span><span>Ejecución de obra</span></div></section>
<section class="instagram"><div class="section-head reveal"><span>04 / Instagram</span><h2>La obra continúa en imágenes.</h2></div><div class="ig-grid">
<a href="https://www.instagram.com/p/C7APinYL8A1/" target="_blank"><img src="assets/images/hero.webp" alt="Publicación de Instagram"><span>Ver publicación ↗</span></a>
<a href="https://www.instagram.com/p/DMZIw5LMke5/" target="_blank"><img src="assets/images/casa-baeza-18-fachada-noche.webp" alt="Publicación de Instagram"><span>Ver publicación ↗</span></a>
<a href="https://www.instagram.com/p/DSu9AKmERWY/" target="_blank"><img src="assets/images/facade.webp" alt="Publicación de Instagram"><span>Ver publicación ↗</span></a>
</div><a class="cta-link" href="https://www.instagram.com/jbmarquitectos.mx/" target="_blank">@jbmarquitectos.mx ↗</a></section>
<section class="reviews" id="opiniones"><div class="review-score reveal"><span>★★★★★</span><strong>5.0</strong><p>5 opiniones en Google</p></div><div class="review-copy reveal"><blockquote>“Desde el primer día fue evidente su profesionalismo y la apertura de criterio que los caracteriza…”</blockquote><cite>Julio Cesar Chavez · Google</cite><hr><blockquote>“Trabajar con JBM ha sido una experiencia excepcional. Interpretaron perfectamente mis ideas…”</blockquote><cite>Rojas Antonio · Google</cite><div class="review-actions"><a href="https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/" target="_blank">Leer opiniones ↗</a><a href="https://g.page/r/CW4ljIvNq_vCEAE/review" target="_blank">Dejar una reseña ↗</a></div></div></section>
<section class="location"><div class="location-card reveal"><span>05 / Visítanos</span><h2>JBM ARQUITECTOS</h2><p>San José Iturbide, Guanajuato</p><p>Atención con cita previa</p><div><a href="https://www.google.com/maps/place/JBM+ARQUITECTOS/@20.9935165,-100.3970036,17z/" target="_blank">Cómo llegar ↗</a><a href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank">Agendar visita ↗</a></div></div><iframe title="Mapa de JBM ARQUITECTOS" loading="lazy" src="https://www.google.com/maps?q=20.9935165,-100.3944233&z=16&output=embed"></iframe></section>
<section class="final" id="contacto"><p>El siguiente proyecto puede ser el tuyo.</p><h2>¿Cómo imaginas tu proyecto?</h2><div><a href="https://calendar.app.google/h7XwWw9xizAmMNz38" target="_blank">Agendar una reunión ↗</a><a href="https://wa.me/524423218552?text=Hola%20JBM%20ARQUITECTOS,%20quiero%20platicar%20sobre%20mi%20proyecto." target="_blank">Escribir por WhatsApp ↗</a></div></section>
</main>
<footer><img src="assets/images/logo-horizontal.png" alt="JBM ARQUITECTOS"><p>Arquitectura · Interiorismo · Proyecto integral</p><p>© 2026 JBM ARQUITECTOS</p></footer>
<div class="idle" id="idlePrompt"><button type="button">×</button><p>¿Ya imaginaste cómo se verá tu proyecto?</p><a href="#contacto">Cuéntanos tu idea ↗</a></div>
<script src="assets/js/v3.js"></script>
</body></html>'''

css = r'''
:root{--ink:#11110f;--paper:#f1ede4;--line:rgba(17,17,15,.18);--serif:"Italiana",serif;--sans:"DM Sans",sans-serif}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-weight:300}a{color:inherit;text-decoration:none}img{display:block;max-width:100%}.loader{position:fixed;inset:0;z-index:1000;background:var(--ink);color:#fff;display:grid;place-items:center;transition:.7s}.loader.hide{opacity:0;visibility:hidden}.loader div{text-align:center}.loader b{display:block;font:clamp(4rem,12vw,9rem)/.8 var(--serif)}.loader span{letter-spacing:.5em;font-size:.65rem}.topbar{position:fixed;z-index:50;top:0;left:0;right:0;height:86px;display:flex;align-items:center;gap:2rem;padding:0 4vw;color:#fff;background:linear-gradient(#0008,transparent)}.brand img{width:175px;filter:brightness(0) invert(1)}nav{display:flex;gap:1.5rem;margin-left:auto}nav a,.book{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase}.book{border-bottom:1px solid}.hero{height:100svh;min-height:680px;position:relative;overflow:hidden;color:#fff;background:#111}.hero video,.hero-fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.hero-fallback{background:url('../images/hero.webp') center/cover}.shade{position:absolute;inset:0;background:linear-gradient(90deg,#000b,#0002 65%),linear-gradient(0deg,#0007,transparent 40%)}.hero-copy{position:absolute;left:5vw;bottom:9vh;z-index:2;max-width:950px}.hero-copy p{font-size:.68rem;letter-spacing:.2em}.hero h1{font:clamp(4rem,9vw,9.5rem)/.88 var(--serif);margin:.6rem 0 1.4rem}.hero h1 em{font-weight:400}.hero-copy>div{font:clamp(1.2rem,2vw,2rem) var(--serif);margin-bottom:2rem}.hero-copy a{border-bottom:1px solid;padding-bottom:.4rem}.sound{position:absolute;z-index:3;right:3vw;bottom:3vw;border:1px solid #fff8;background:#0004;color:#fff;border-radius:999px;padding:.8rem 1.1rem}.statement,.manifesto,.final{min-height:80vh;display:flex;flex-direction:column;justify-content:center;padding:9vw 6vw}.statement p,.manifesto p,.final p{font-size:.75rem;letter-spacing:.18em;text-transform:uppercase}.statement h2,.manifesto h2,.final h2{font:clamp(4rem,9vw,10rem)/.9 var(--serif);max-width:1200px;margin:1rem 0}.statement a{width:max-content;border-bottom:1px solid}.projects,.process,.services,.instagram{padding:10vw 5vw}.section-head{display:grid;grid-template-columns:220px 1fr;gap:3rem;margin-bottom:6vw}.section-head span{font-size:.65rem;letter-spacing:.17em;text-transform:uppercase}.section-head h2{font:clamp(3rem,7vw,7rem)/.95 var(--serif);margin:0}.project{display:grid;grid-template-columns:1.4fr .6fr;gap:4vw;align-items:end;margin-bottom:10vw}.project.reverse{grid-template-columns:.6fr 1.4fr}.project.reverse img{order:2}.project img{width:100%;height:70vh;object-fit:cover}.project h3{font:clamp(3rem,6vw,6rem)/1 var(--serif);margin:1rem 0}.manifesto{background:#111;color:#fff}.steps{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line)}.steps article{padding:2.2rem;border-right:1px solid var(--line);border-bottom:1px solid var(--line);min-height:220px}.steps b{font-size:.7rem}.steps h3{font:2rem var(--serif)}.service-list{display:grid;grid-template-columns:repeat(2,1fr);border-top:1px solid}.service-list span{font:clamp(2rem,5vw,5rem) var(--serif);padding:2rem 0;border-bottom:1px solid}.ig-grid{display:grid;grid-template-columns:1.4fr .8fr .8fr;gap:1rem}.ig-grid a{position:relative;overflow:hidden;min-height:520px}.ig-grid img{width:100%;height:100%;object-fit:cover;transition:.6s}.ig-grid span{position:absolute;inset:auto 1rem 1rem;color:#fff}.ig-grid a:hover img{transform:scale(1.04);filter:brightness(.7)}.cta-link{display:inline-block;margin-top:2rem;border-bottom:1px solid}.reviews{background:#111;color:#fff;padding:10vw 6vw;display:grid;grid-template-columns:.45fr 1fr;gap:8vw}.review-score span{letter-spacing:.18em}.review-score strong{display:block;font:clamp(7rem,15vw,15rem)/.8 var(--serif)}.review-copy blockquote{font:clamp(2rem,4vw,4.5rem)/1.15 var(--serif);margin:0 0 1rem}.review-copy cite{font-style:normal;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase}.review-copy hr{border:0;border-top:1px solid #ffffff33;margin:4rem 0}.review-actions{display:flex;gap:2rem;margin-top:3rem}.review-actions a{border-bottom:1px solid}.location{display:grid;grid-template-columns:.6fr 1.4fr;min-height:75vh}.location-card{padding:6vw;background:#d9d2c5;display:flex;flex-direction:column;justify-content:center}.location-card h2{font:clamp(3rem,6vw,6rem) var(--serif);margin:1rem 0}.location-card a{display:inline-block;margin-right:1rem;border-bottom:1px solid}.location iframe{width:100%;height:100%;border:0;filter:grayscale(1) contrast(1.1)}.final{background:#111;color:#fff;text-align:center;align-items:center}.final div{display:flex;gap:2rem}.final a{border-bottom:1px solid}footer{padding:4rem 5vw;display:flex;align-items:center;gap:2rem;border-top:1px solid}footer img{width:180px}footer p:nth-child(2){margin-left:auto}.idle{position:fixed;right:2rem;bottom:2rem;z-index:60;background:#fff;padding:1.4rem 1.6rem;box-shadow:0 20px 60px #0003;transform:translateY(160%);transition:.5s;max-width:320px}.idle.show{transform:none}.idle button{float:right;border:0;background:none;font-size:1.2rem}.idle a{border-bottom:1px solid}.reveal{opacity:0;transform:translateY(40px);transition:1s}.reveal.on{opacity:1;transform:none}@media(max-width:850px){nav{display:none}.topbar{height:72px}.book{margin-left:auto}.project,.project.reverse,.reviews,.location,.section-head{grid-template-columns:1fr}.project.reverse img{order:0}.project img{height:55vh}.steps{grid-template-columns:1fr 1fr}.ig-grid{grid-template-columns:1fr}.ig-grid a{min-height:65vw}.service-list{grid-template-columns:1fr}.location iframe{height:55vh}.final div,.review-actions{flex-direction:column}.sound{bottom:1rem}.hero-copy{bottom:11vh}.hero h1{font-size:18vw}footer{flex-direction:column;align-items:flex-start}footer p:nth-child(2){margin-left:0}}@media(max-width:560px){.steps{grid-template-columns:1fr}.statement,.manifesto,.final{min-height:70vh}.section-head{gap:1.5rem}.project img{height:50vh}.reviews{padding:6rem 1.5rem}.ig-grid a{min-height:110vw}}
'''

js = r'''
const loader=document.querySelector('.loader');addEventListener('load',()=>setTimeout(()=>loader.classList.add('hide'),500));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('on')}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const lines=['Cada detalle tiene un propósito.','Arquitectura contemporánea.','Diseñamos espacios para vivir mejor.','El siguiente proyecto puede ser el tuyo.'];let i=0;setInterval(()=>{i=(i+1)%lines.length;document.getElementById('rotatingLine').textContent=lines[i]},3500);
const v=document.getElementById('heroVideo'),btn=document.getElementById('soundToggle');v.addEventListener('error',()=>v.style.display='none',true);btn.addEventListener('click',()=>{v.muted=!v.muted;btn.textContent=v.muted?'Activar sonido':'Silenciar'});
const idle=document.getElementById('idlePrompt');let timer=setTimeout(()=>idle.classList.add('show'),22000);['scroll','mousemove','keydown','touchstart'].forEach(ev=>addEventListener(ev,()=>{clearTimeout(timer);timer=setTimeout(()=>idle.classList.add('show'),22000)},{passive:true}));idle.querySelector('button').addEventListener('click',()=>idle.classList.remove('show'));
'''

(SITE / 'index.html').write_text(html, encoding='utf-8')
(SITE / 'assets/css/v3.css').write_text(css, encoding='utf-8')
(SITE / 'assets/js/v3.js').write_text(js, encoding='utf-8')
print('JBM ARQUITECTOS V3 construido')
