// JBM ARQUITECTOS — Estimador de inversión
(function(){
  const root=document.querySelector('#estimador');
  if(!root)return;

  const money=value=>new Intl.NumberFormat('es-MX',{style:'currency',currency:'MXN',maximumFractionDigits:0}).format(Math.round(value));
  const tabs=[...root.querySelectorAll('[data-estimator-tab]')];
  const panels=[...root.querySelectorAll('[data-estimator-panel]')];

  function activate(name){
    tabs.forEach(tab=>{
      const active=tab.dataset.estimatorTab===name;
      tab.setAttribute('aria-selected',String(active));
      tab.tabIndex=active?0:-1;
    });
    panels.forEach(panel=>panel.classList.toggle('active',panel.dataset.estimatorPanel===name));
    if(typeof window.gtag==='function')window.gtag('event','estimator_tab',{estimator_type:name});
  }

  tabs.forEach(tab=>tab.addEventListener('click',()=>activate(tab.dataset.estimatorTab)));

  function showResult(panel,{low,high,summary,details,scope,whatsapp,type}){
    const empty=panel.querySelector('.estimator-result-empty');
    const content=panel.querySelector('.estimator-result-content');
    if(empty)empty.hidden=true;
    if(content)content.hidden=false;
    panel.querySelector('[data-result-amount]').textContent=`${money(low)} – ${money(high)}`;
    panel.querySelector('[data-result-copy]').textContent=summary;
    const detailBox=panel.querySelector('[data-result-details]');
    detailBox.innerHTML=details.map(([label,value])=>`<div><span>${label}</span><span>${value}</span></div>`).join('');
    panel.querySelector('[data-result-scope]').textContent=scope;
    const link=panel.querySelector('[data-result-whatsapp]');
    link.href=`https://wa.me/524423218552?text=${encodeURIComponent(whatsapp)}`;
    if(typeof window.gtag==='function')window.gtag('event','estimator_result',{estimator_type:type,estimate_low:Math.round(low),estimate_high:Math.round(high),currency:'MXN'});
  }

  root.querySelector('[data-calc="executive"]')?.addEventListener('click',()=>{
    const panel=root.querySelector('[data-estimator-panel="executive"]');
    const area=Number(panel.querySelector('[name="exec-area"]').value);
    const levels=panel.querySelector('[name="exec-levels"]').value;
    if(!area||area<40){panel.querySelector('[name="exec-area"]').focus();return;}

    // Referencia comercial JBM para proyecto ejecutivo de vivienda.
    const unitRate=350;
    const levelFactor={one:1,two:1.08,three:1.15}[levels]||1;
    const base=Math.max(35000,area*unitRate*levelFactor);
    const low=base*.9;
    const high=base*1.1;
    const levelLabel={one:'1 nivel',two:'2 niveles',three:'3 niveles o más'}[levels];

    const whatsapp=[
      'Hola JBM ARQUITECTOS, utilicé el estimador de su página.',
      '',
      'Servicio: Proyecto ejecutivo para casa habitación',
      `Superficie aproximada: ${area} m²`,
      `Niveles: ${levelLabel}`,
      `Rango mostrado: ${money(low)} – ${money(high)}`,
      '',
      'Me gustaría recibir una cotización personalizada.'
    ].join('\n');

    showResult(panel,{
      low,high,type:'executive',
      summary:'Referencia preliminar para desarrollar los planos ejecutivos de una casa habitación. El alcance definitivo se confirma después de conocer el terreno y las necesidades del proyecto.',
      details:[['Superficie',`${area} m²`],['Niveles',levelLabel],['Tipo','Proyecto ejecutivo']],
      scope:'Base considerada: planos arquitectónicos, eléctricos, hidráulicos y sanitarios, criterio estructural y coordinación ejecutiva básica. No incluye cálculo estructural firmado, estudios, levantamiento, trámites, ingenierías especiales ni renders salvo cotización específica.',
      whatsapp
    });
  });

  root.querySelector('[data-calc="construction"]')?.addEventListener('click',()=>{
    const panel=root.querySelector('[data-estimator-panel="construction"]');
    const area=Number(panel.querySelector('[name="build-area"]').value);
    const levels=panel.querySelector('[name="build-levels"]').value;
    const finish=panel.querySelector('[name="build-finish"]').value;
    const terrain=panel.querySelector('[name="build-terrain"]').value;
    if(!area||area<40){panel.querySelector('[name="build-area"]').focus();return;}

    const rates={
      standard:[11000,13500],
      residential:[14500,18500],
      premium:[19500,26000]
    }[finish];
    const levelFactor={one:1,two:1.05,three:1.12}[levels]||1;
    const terrainFactor={flat:1,medium:1.05,slope:1.15}[terrain]||1;
    const low=area*rates[0]*levelFactor*terrainFactor;
    const high=area*rates[1]*levelFactor*terrainFactor;
    const levelLabel={one:'1 nivel',two:'2 niveles',three:'3 niveles o más'}[levels];
    const finishLabel={standard:'Estándar contemporáneo',residential:'Residencial',premium:'Premium'}[finish];
    const terrainLabel={flat:'Plano / regular',medium:'Con desnivel moderado',slope:'Pendiente o condición especial'}[terrain];

    const whatsapp=[
      'Hola JBM ARQUITECTOS, utilicé el estimador de su página.',
      '',
      'Servicio: Construcción de casa habitación',
      `Superficie aproximada: ${area} m²`,
      `Niveles: ${levelLabel}`,
      `Nivel de acabados: ${finishLabel}`,
      `Terreno: ${terrainLabel}`,
      `Rango mostrado: ${money(low)} – ${money(high)}`,
      '',
      'Me gustaría revisar mi proyecto y recibir una cotización personalizada.'
    ].join('\n');

    showResult(panel,{
      low,high,type:'construction',
      summary:'Rango preliminar de inversión para construcción de vivienda. El presupuesto real depende del proyecto ejecutivo, condiciones del suelo, sistema estructural, instalaciones, acabados y ubicación.',
      details:[['Superficie',`${area} m²`],['Niveles',levelLabel],['Acabados',finishLabel],['Terreno',terrainLabel]],
      scope:'Referencia de obra y acabados para casa habitación. No incluye terreno, proyecto y honorarios profesionales, permisos y derechos, estudios de suelo, mobiliario, paisajismo, alberca, obras exteriores especiales ni condiciones extraordinarias de cimentación.',
      whatsapp
    });
  });
})();
