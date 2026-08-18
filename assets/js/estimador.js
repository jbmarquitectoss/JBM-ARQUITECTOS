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

  function showResult(panel,{low,high,summary,details,scope,whatsapp,type,displayMode='range'}){
    const empty=panel.querySelector('.estimator-result-empty');
    const content=panel.querySelector('.estimator-result-content');
    if(empty)empty.hidden=true;
    if(content)content.hidden=false;

    const amount=panel.querySelector('[data-result-amount]');
    if(displayMode==='from'){
      amount.textContent=`Desde ${money(low)}`;
    }else if(Math.round(low)===Math.round(high)){
      amount.textContent=money(low);
    }else{
      amount.textContent=`${money(low)} – ${money(high)}`;
    }

    panel.querySelector('[data-result-copy]').textContent=summary;
    const detailBox=panel.querySelector('[data-result-details]');
    detailBox.innerHTML=details.map(([label,value])=>`<div><span>${label}</span><span>${value}</span></div>`).join('');
    panel.querySelector('[data-result-scope]').textContent=scope;
    const link=panel.querySelector('[data-result-whatsapp]');
    link.href=`https://wa.me/524423218552?text=${encodeURIComponent(whatsapp)}`;

    if(typeof window.gtag==='function')window.gtag('event','estimator_result',{
      estimator_type:type,
      estimate_low:Math.round(low),
      estimate_high:Math.round(high),
      currency:'MXN'
    });
  }

  root.querySelector('[data-calc="executive"]')?.addEventListener('click',()=>{
    const panel=root.querySelector('[data-estimator-panel="executive"]');
    const area=Number(panel.querySelector('[name="exec-area"]').value);
    const levels=panel.querySelector('[name="exec-levels"]').value;
    if(!area||area<40){panel.querySelector('[name="exec-area"]').focus();return;}

    // Base comercial indicada por JBM ARQUITECTOS: $180 MXN/m².
    const unitRate=180;
    const base=area*unitRate;
    const levelLabel={one:'1 nivel',two:'2 niveles',three:'3 niveles o más'}[levels];

    const whatsapp=[
      'Hola JBM ARQUITECTOS, utilicé el estimador de su página.',
      '',
      'Servicio: Proyecto ejecutivo para casa habitación',
      `Superficie aproximada: ${area} m²`,
      `Niveles: ${levelLabel}`,
      `Base de cálculo: ${money(unitRate)} por m²`,
      `Estimación base: ${money(base)}`,
      '',
      'Me gustaría recibir una cotización personalizada.'
    ].join('\n');

    showResult(panel,{
      low:base,
      high:base,
      type:'executive',
      displayMode:'exact',
      summary:`Estimación base calculada a ${money(unitRate)} por m² de proyecto. El precio definitivo se confirma después de revisar el terreno, alcance y necesidades específicas.`,
      details:[
        ['Superficie',`${area} m²`],
        ['Niveles',levelLabel],
        ['Base JBM',`${money(unitRate)} / m²`],
        ['Tipo','Proyecto ejecutivo']
      ],
      scope:'Base considerada para proyecto ejecutivo de casa habitación. El alcance final y cualquier servicio adicional se definen en la cotización personalizada.',
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

    // Base comercial indicada por JBM ARQUITECTOS: $12,000 MXN/m² de construcción.
    const unitRate=12000;
    const base=area*unitRate;
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
      `Base de cálculo: ${money(unitRate)} por m²`,
      `Inversión base estimada: ${money(base)}`,
      '',
      'Me gustaría revisar mi proyecto y recibir una cotización personalizada.'
    ].join('\n');

    showResult(panel,{
      low:base,
      high:base,
      type:'construction',
      displayMode:'from',
      summary:`Inversión base calculada desde ${money(unitRate)} por m² de construcción. El presupuesto definitivo varía según proyecto ejecutivo, estructura, instalaciones, acabados, terreno y ubicación.`,
      details:[
        ['Superficie',`${area} m²`],
        ['Niveles',levelLabel],
        ['Acabados',finishLabel],
        ['Terreno',terrainLabel],
        ['Base JBM',`${money(unitRate)} / m²`]
      ],
      scope:'Referencia base de construcción de casa habitación. El precio final se ajusta según condiciones reales del proyecto. No incluye terreno, proyecto y honorarios profesionales, permisos y derechos, estudios de suelo, mobiliario, paisajismo, alberca, obras exteriores especiales ni condiciones extraordinarias de cimentación.',
      whatsapp
    });
  });
})();
