
const body=document.body;
const header=document.querySelector("[data-header]");
const menuButton=document.querySelector(".menu-toggle");
const menu=document.querySelector(".menu");

window.addEventListener("load",()=>setTimeout(()=>body.classList.add("loaded"),180));
window.addEventListener("scroll",()=>header?.classList.toggle("scrolled",window.scrollY>40),{passive:true});

menuButton?.addEventListener("click",()=>{
  const open=body.classList.toggle("menu-open");
  menuButton.setAttribute("aria-expanded",String(open));
  header?.classList.toggle("menu-open",open);
});
menu?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{
  body.classList.remove("menu-open");
  header?.classList.remove("menu-open");
  menuButton?.setAttribute("aria-expanded","false");
}));

const observer=new IntersectionObserver(entries=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add("visible");observer.unobserve(entry.target)}
  });
},{threshold:.12,rootMargin:"0px 0px -50px"});
document.querySelectorAll(".reveal").forEach(el=>observer.observe(el));

const parallaxItems=document.querySelectorAll("[data-parallax]");
window.addEventListener("scroll",()=>{
  if(window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
  parallaxItems.forEach(el=>{
    const rect=el.parentElement.getBoundingClientRect();
    const shift=(window.innerHeight/2-(rect.top+rect.height/2))*.055;
    el.style.transform=`translate3d(0,${shift}px,0) scale(1.08)`;
  });
},{passive:true});

document.querySelectorAll("[data-year]").forEach(el=>el.textContent=new Date().getFullYear());

const triggers=[...document.querySelectorAll(".lightbox-trigger")];
const lightbox=document.querySelector(".lightbox");
const lightboxImg=lightbox?.querySelector("img");
const lightboxCaption=lightbox?.querySelector("figcaption");
let current=0;

function showImage(index){
  if(!triggers.length||!lightbox)return;
  current=(index+triggers.length)%triggers.length;
  const trigger=triggers[current];
  lightboxImg.src=trigger.dataset.image;
  lightboxImg.alt=trigger.dataset.caption||"Imagen del proyecto";
  lightboxCaption.textContent=trigger.dataset.caption||"";
}
function openLightbox(index){
  showImage(index);
  lightbox.classList.add("open");
  lightbox.setAttribute("aria-hidden","false");
  body.classList.add("lightbox-open"); document.documentElement.style.overflow="hidden";
}
function closeLightbox(){
  lightbox?.classList.remove("open");
  lightbox?.setAttribute("aria-hidden","true");
  body.classList.remove("lightbox-open"); document.documentElement.style.overflow="";
}
triggers.forEach((trigger,index)=>trigger.addEventListener("click",()=>openLightbox(index)));
lightbox?.querySelector(".lightbox-close")?.addEventListener("click",closeLightbox);
lightbox?.querySelector(".lightbox-prev")?.addEventListener("click",()=>showImage(current-1));
lightbox?.querySelector(".lightbox-next")?.addEventListener("click",()=>showImage(current+1));
lightbox?.addEventListener("click",e=>{if(e.target===lightbox)closeLightbox()});
document.addEventListener("keydown",e=>{
  if(!lightbox?.classList.contains("open"))return;
  if(e.key==="Escape")closeLightbox();
  if(e.key==="ArrowLeft")showImage(current-1);
  if(e.key==="ArrowRight")showImage(current+1);
});


const contactForm=document.querySelector("#contact-form");
const formStatus=document.querySelector("#form-status");
contactForm?.addEventListener("submit",event=>{
  event.preventDefault();
  if(!contactForm.reportValidity())return;

  const data=new FormData(contactForm);
  const value=name=>(data.get(name)||"").toString().trim();
  const lines=[
    "Hola JBM ARQUITECTOS, quiero solicitar información para un proyecto.",
    "",
    `Nombre: ${value("nombre")}`,
    `Teléfono: ${value("telefono")}`,
    `Correo: ${value("correo")}`,
    `Ciudad: ${value("ciudad")||"No indicada"}`,
    `Tipo de proyecto: ${value("tipo")||"No indicado"}`,
    `Etapa actual: ${value("etapa")||"No indicada"}`,
    "",
    "Mensaje:",
    value("mensaje")
  ];
  const url=`https://wa.me/524423218552?text=${encodeURIComponent(lines.join("\n"))}`;
  formStatus.textContent="Abriendo WhatsApp con tu solicitud…";
  window.open(url,"_blank","noopener");
});


// Final accessibility and interaction refinements
const menuToggleClose=()=>{body.classList.remove('menu-open');header?.classList.remove('menu-open');menuButton?.setAttribute('aria-expanded','false')};
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&body.classList.contains('menu-open'))menuToggleClose()});
let touchStartX=0;
lightbox?.addEventListener('touchstart',event=>{touchStartX=event.changedTouches[0].clientX},{passive:true});
lightbox?.addEventListener('touchend',event=>{const delta=event.changedTouches[0].clientX-touchStartX;if(Math.abs(delta)>55)showImage(current+(delta<0?1:-1))},{passive:true});
document.querySelectorAll('.faq details').forEach(item=>item.addEventListener('toggle',()=>{if(item.open)document.querySelectorAll('.faq details[open]').forEach(other=>{if(other!==item)other.open=false})}));
