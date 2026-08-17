// JBM ARQUITECTOS — Google Analytics 4: eventos de negocio
(function(){
  function track(eventName,params={}){
    if(typeof window.gtag!=="function")return;
    window.gtag("event",eventName,{
      ...params,
      page_path:window.location.pathname,
      page_title:document.title
    });
  }

  function trackLead(leadType,params={}){
    track("generate_lead",{
      lead_type:leadType,
      ...params
    });
  }

  const textOf=el=>(el?.textContent||"").trim().replace(/\s+/g," ").slice(0,120);

  document.addEventListener("click",event=>{
    const link=event.target.closest("a[href]");
    if(!link)return;

    const href=link.getAttribute("href")||"";
    const text=textOf(link);
    const params={link_text:text,link_url:link.href};

    if(href.includes("wa.me/")){
      track("whatsapp_click",params);
      trackLead("whatsapp",params);
    }else if(href.includes("calendar.app.google")){
      track("booking_click",params);
      trackLead("booking",params);
    }else if(href==="#proyectos"){
      track("portfolio_click",params);
    }else if(href.includes("casa-gh.html")){
      track("project_open",{...params,project_name:"Casa GH"});
    }else if(href.includes("casa-baeza.html")){
      track("project_open",{...params,project_name:"Casa Baeza"});
    }else if(href.includes("maps.app.goo.gl")||/cómo llegar/i.test(text)){
      track("directions_click",params);
    }
  });

  document.addEventListener("submit",event=>{
    if(event.target?.matches("#contact-form")){
      const form=new FormData(event.target);
      const params={
        project_type:(form.get("tipo")||"no_indicado").toString(),
        project_city:(form.get("ciudad")||"no_indicada").toString()
      };
      track("contact_form_submit",params);
      trackLead("contact_form",params);
    }
  });

  const path=window.location.pathname.toLowerCase();
  if(path.endsWith("casa-gh.html")){
    track("project_view",{project_name:"Casa GH"});
  }else if(path.endsWith("casa-baeza.html")){
    track("project_view",{project_name:"Casa Baeza"});
  }
})();
