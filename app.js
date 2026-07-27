var DB='lead_manager_biH',filter='all';

var L=[
["Almir","Alibegović","Frizerski salon A.A. Alibegović","Sarajevo","frizerski salon","+387 33 537 539","","Nema web"],
["Amela","Husić","Frizerski salon Amela s.z.r.","Sarajevo","frizerski salon","+387 62 583 854","","Baščaršija"],
["","","Beauty Salon Na-Na","Sarajevo","kozmetički salon","+387 61 666 002","info@na-na.ba","Stupska 19-B2"],
["","","Beauty First Salon & Spa d.o.o.","Sarajevo","kozmetički salon","+387 33 977 913","","Ilidža"],
["","","Ženski frizerski salon KIM","Sarajevo","frizerski salon","+387 33 667 513","","Avde Hume 21"],
["Sead","Rizvić","Restoran Sarajevo Vl Rizvić","Sarajevo","restoran","+387 61 053 678","","Restoran"],
["Semih","Aslan","Restoran Sofra d.o.o.","Sarajevo","restoran","+387 33 447 815","","Baščaršija 31"],
["","","Auto Servis Team","Sarajevo","auto servis","+387 61 552 168","","Samo Facebook"],
["","","Autoelektra","Sarajevo","auto servis","+387 33 444 749","aesa@bih.net.ba","Patriotske lige 10"],
["","","Automotive Center","Sarajevo","auto servis","+387 33 715 465","","Vilsonovo šetalište 10"],
["","","Auto Servis DEL","Sarajevo","auto servis","+387 62 1","","Urijan Dedina 48"],
["","","Dodir Kozmetički salon","Sarajevo","kozmetički salon","+387 33 204 756","info@dodir.ba","Grbavička 5"],
["","","Salon Estetika","Sarajevo","kozmetički salon","+387 61 030 504","","Kemala Kapetanovića 13"],
["","","Nova Beauty d.o.o.","Sarajevo","kozmetički salon","+387 62 725 741","","Direktor: Fazlić Alma"],
["","","Pekara AS d.o.o.","Sarajevo","pekara","+387 33 610 286","","Direktor: Gjuraj"],
["","","Pekara EDI d.o.o.","Sarajevo","pekara","+387 62 412 405","","Ilidža"],
["","","SAPLAST d.o.o.","Sarajevo","stolarija","+387 33 779 500","info@saplast.ba","Nikole Šopa 245"],
["","","ELOX d.o.o.","Sarajevo","stolarija","+387 61 984 333","info@elox.ba","Put Famosa 38"],
["","","BH Werk d.o.o.","Sarajevo","stolarija","+387 62 853 773","info@bhwerk.com","Vogošćanskih odreda 44D"],
["","","DOM-A d.o.o.","Sarajevo","stolarija","+387 61 264 233","info@dom-a.ba","PVC i ALU stolarija"],
["Miroslav","Tomić","Lokal Caffe Miroslav Tomić s.p.","Banja Luka","caffe bar","+387 65 385 026","tomicmiroslav00@gmail.com",""],
["","","Caffe Bar ARIA","Banja Luka","caffe bar","","","Bana Milosavljevića 1"],
["","","Restoran Kastel","Banja Luka","restoran","","",""],
["","","Pekara Mlinar","Banja Luka","pekara","","","Lanac pekara"],
["","","Fitness centar Fit Zone","Banja Luka","fitness studio","","",""],
["","","Tehnomag","Banja Luka","trgovina","+387 51 200 000","banjaluka@tehnomag.com","Lanac trgovina"],
["","","Motorex P.J. Bihać 1","Bihać","auto dijelovi","+387 37 351 833","","37 retail objekata"],
["","","Cvjećara Vernisaž","Bihać","cvjećara","+387 62 595 946","cvjecara.vernisaz@gmail.com",""],
["","","Cvjećara S-Garden","Bihać","cvjećara","+387 63 597 585","cvjecarasgarden@gmail.com","TC Bingo"],
["Snježana","Rajković","Cvjećara Iris Bihać","Bihać","cvjećara","+387 66 955 874","",""],
["","","DELFIN Autopraona","Bihać","autopraonica","+387 61 591 903","",""],
["","","Auto Lider d.o.o.","Brčko","auto","+387 61 600 008","","Mostarska bb"],
["Adis","Selimović","Autolimar ADO","Brčko","autolimar","+387 62 180 655","","Alije Selimovića"],
["","","Autolimar i Lakirer Šiša","Brčko","autolimar","+387 61 425 314","","Samo Facebook"],
["","","Vulkanizer Brzi Servis Marić","Grude","vulkanizer","+387 63 326 099","","Imotski-Grude"],
["","","COKUL COMMERCE d.o.o.","Grude","vulkanizer","+387 39 661 601","",""],
["","","Foto Studio Franjić","Novi Travnik","photo studio","+387 30 791 536","foto.franjic@gmail.com",""],
["","","Studio Level","Novi Travnik","photo studio","+387 63 595 500","info@studio-level.com","72290"],
["","","Foto-Video Studio Home","Novi Travnik","photo studio","+387 62 33","",""],
["","","Caffe Studio","Novi Travnik","caffe bar","+387 30 790 600","margetonij@gmail.com","Samo Facebook"],
["","","Pulmont d.o.o.","Zenica","građevinska","+387 32 402 045","","Sabahudin Đuherić"],
["","","EN-BE Građevinski obrt","Zenica","građevinska","+387 61 451 939","crjasko@gmail.com","Gorica 46"],
["","","Techno Shop Zenica","Zenica","trgovina","+387 32 249 111","zenica@technoshop.ba","Kamberovića čikma"],
["","","Tehnomag Zenica","Zenica","trgovina","+387 32 445 740","zenica@tehnomag.com","Lanac trgovina"],
["","","ES OPTIC Visoko","Visoko","optika","+387 62 148 462","esopticvisoko@gmail.com","Musala 1"],
["","","Optika Tihić","Visoko","optika","+387 61 925 925","","Kralja Tvrtka bb"],
["","","Optika Beganović","Visoko","optika","+387 62 750 800","","Čaršijska"],
["","","BB NEW LOOK d.o.o.","Mostar","trgovina odjećom","+387 36 317 299","","Boro Bandić"],
["","","ANGEL'S FASHION d.o.o.","Mostar","trgovina odjećom","+387 36 322 360","","Ivana Džidić"],
["","","Moda Best d.o.o.","Mostar","trgovina odjećom","+387 36 836 257","","Ivan Grgić"],
["","","FREE SHOP d.o.o.","Mostar","trgovina odjećom","+387 36 550 385","","Damir Beljo"],
["","","Elko Marić d.o.o.","Mostar","električar","+387 36 558 080","elkomaric@bih.net.ba","Maršala Tita 294"],
["","","Elektro Mont Mostar","Mostar","električar","+387 36 334 334","elektro-mont@tel.net.ba","Put za Aluminij"],
["","","Intertekstil","Široki Brijeg","trgovina odjećom","+387 39 705 451","","Gojka Šuška 2A"],
["","","Boutique Markos","Široki Brijeg","trgovina odjećom","+387 39 705 743","dpenava85@gmail.com",""],
["","","SARTEKS d.o.o.","Široki Brijeg","trgovina","+387 39 701 838","sarteks1@tel.net.ba","Uzarići bb"],
["","","EUROM d.o.o.","Široki Brijeg","trgovina","+387 39 705 411","euromsb1@gmail.com","Igračke i kućanske"],
["","","Dječiji vrtić Ljubuški","Ljubuški","vrtić","+387 39 833 261","d.vrtic.ljubuski@gmail.com",""],
["","","Restoran Labirint","Mostar","restoran","","",""],
["","","La-Tour Agencija","Čapljina","putnička agencija","+387 63 320 325","info@la-touragency.com","Višići"],
["","","Čapljinka Turistička org.","Čapljina","putnička agencija","+387 36 806 147","tur.org.capljina@tel.net.ba","Mate Bobana bb"],
["","","Hotel Turist '98","Jajce","hotel","+387 30 658 151","utd.turist98@tel.net.ba","Kulina bana 1"],
["","","Hotel Plivsko Jezero","Jajce","hotel","+387 30 654 090","reception@plivskojezero.com","Jajce"],
["Boban","Savić","Advokatska kancelarija Savić","Doboj","advokat","+387 66 490 494","bobansavic84@gmail.com","Svetog Save 24"],
["Irena","Puzić-Obradović","Adv. kancelarija Puzić-Obradović","Doboj","advokat","+387 53 222 030","irenapuzic@yahoo.com",""],
["","","Finel Računovodstvo i Revizija","Tuzla","računovodstvo","+387 35 262 370","info@finel.ba","Stupine B9"],
["","","Revis Računovodstvo","Tuzla","računovodstvo","+387 35 270 094","revis@revis.ba","Kazan mahala 36"],
["","","ESGfin Tuzla","Tuzla","računovodstvo","+387 61 480 834","info@esgfin.ba",""],
["","","Atria d.o.o.","Tuzla","računovodstvo","+387 61 732 398","info@atria.ba","Titanik zgrada"],
["","","Fitness Studio Fuke","Tuzla","fitness","+387 61 179 000","","Mije Keroševića 20"],
["","","Fitness Studio Dobar Osjećaj","Tuzla","fitness","+387 61 271 655","","Armije BiH 15"],
["","","Fitness & Aerobic Studio LIFE","Tuzla","fitness","+387 61 855 843","",""],
["","","Feel Good Fitness Studio","Tuzla","fitness","","feelgoodfitness875@gmail.com","Samo Facebook"]
];

function ls(){try{return JSON.parse(localStorage.getItem(DB))||{}}catch(e){return{}}}
function ss(s){localStorage.setItem(DB,JSON.stringify(s))}
function gc(){return L.map(function(l,i){var id='c'+i,st=ls()[id]||{};return{id:id,owner:[l[0],l[1]].filter(Boolean).join(' '),company:l[2],city:l[3],category:l[4],phone:l[5],email:l[6],notes:l[7]||'',status:st.status||'pending',called:st.called||false,custNotes:st.notes||''}})}
function uc(id,f,v){var st=ls();if(!st[id])st[id]={status:'pending',called:false,notes:''};st[id][f]=v;ss(st)}
function toast(msg){var c=document.getElementById('toastBox'),t=document.createElement('div');t.className='toast';t.innerHTML=msg;c.appendChild(t);setTimeout(function(){t.classList.add('out');setTimeout(function(){t.remove()},300)},2500)}

function initBento(){
  var all=gc(),done=0,prog=0,pend=0,called=0;
  all.forEach(function(c){if(c.status==='done')done++;else if(c.status==='in_progress')prog++;if(c.called)called++});
  pend=all.length-done-prog;
  var pct=all.length?Math.round(done/all.length*100):0;
  var off=314-(314*pct/100);
  document.getElementById('bentoGrid').innerHTML=
    '<div class="bento-card span-2"><div style="display:flex;align-items:center;gap:20px"><div class="progress-ring"><svg viewBox="0 0 120 120"><circle class="bg" cx="60" cy="60" r="50"/><circle class="fg" cx="60" cy="60" r="50" style="stroke-dashoffset:'+off+'"/></svg><div class="progress-center">'+pct+'%</div></div><div><div class="bento-value">'+done+'<span style="font-size:1rem;color:var(--text3)">/'+all.length+'</span></div><div class="bento-label">Kontakata završeno</div></div></div></div>'+
    '<div class="bento-card"><div class="bento-icon" style="background:rgba(251,191,36,.1);color:#fbbf24">⏳</div><div class="bento-value" style="color:#fbbf24">'+pend+'</div><div class="bento-label">Čeka na poziv</div></div>'+
    '<div class="bento-card"><div class="bento-icon" style="background:rgba(56,189,248,.1);color:#38bdf8">🔄</div><div class="bento-value" style="color:#38bdf8">'+prog+'</div><div class="bento-label">U toku</div></div>'+
    '<div class="bento-card"><div class="bento-icon" style="background:rgba(52,211,153,.1);color:#34d399">✅</div><div class="bento-value" style="color:#34d399">'+done+'</div><div class="bento-label">Završeno</div></div>'+
    '<div class="bento-card"><div class="bento-icon" style="background:rgba(244,114,182,.1);color:#f472b6">📞</div><div class="bento-value" style="color:#f472b6">'+called+'</div><div class="bento-label">Pozvano</div></div>';
  setTimeout(function(){document.querySelectorAll('.bento-card').forEach(function(c,i){setTimeout(function(){c.classList.add('visible')},i*80)})},100);
}

function updateCounts(){
  var all=gc(),cp=0,co=0,cd=0,cc=0;
  all.forEach(function(c){if(c.status==='pending')cp++;else if(c.status==='in_progress')co++;else if(c.status==='done')cd++;if(c.called)cc++});
  document.getElementById('cAll').textContent=all.length;
  document.getElementById('cPen').textContent=cp;
  document.getElementById('cPro').textContent=co;
  document.getElementById('cDon').textContent=cd;
  document.getElementById('cCal').textContent=cc;
}

function renderContacts(){
  var q=document.getElementById('searchInput').value.toLowerCase();
  var all=gc(),d=[];
  all.forEach(function(c){
    var show=true;
    if(filter==='called'){if(!c.called)show=false}
    else if(filter!=='all'){if(c.status!==filter)show=false}
    if(show&&(c.company+c.city+c.category+c.owner+c.custNotes+c.notes).toLowerCase().indexOf(q)===-1)show=false;
    if(show)d.push(c);
  });
  document.getElementById('contactCount').textContent='— '+d.length+' rezultata';
  var grid=document.getElementById('contactGrid');
  if(!d.length){grid.innerHTML='';document.getElementById('emptyState').style.display='block';return}
  document.getElementById('emptyState').style.display='none';
  grid.innerHTML=d.map(function(c,i){
    var ini=c.company.split(' ').slice(0,2).map(function(w){return w[0]||''}).join('').toUpperCase();
    var sc=c.status==='done'?'s-done':c.status==='in_progress'?'s-progress':'s-pending';
    var sl=c.status==='done'?'✅ Završeno':c.status==='in_progress'?'⏳ U toku':'↩️ Čeka';
    return '<div class="contact-card" style="transition-delay:'+Math.min(i*30,300)+'ms">'+
      '<div class="card-head"><div class="card-av">'+ini+'</div><div class="card-info"><div class="card-company">'+c.company+'</div><div class="card-meta"><span class="tag">📍 '+c.city+'</span><span class="tag">🏷 '+c.category+'</span></div></div></div>'+
      '<div class="card-body">'+
      (c.owner?'<div class="card-row"><span class="ic">👤</span>'+c.owner+'</div>':'')+
      (c.phone?'<div class="card-row"><span class="ic">📞</span><a href="tel:'+c.phone.replace(/\s/g,'')+'">'+c.phone+'</a></div>':'')+
      (c.email?'<div class="card-row"><span class="ic">✉️</span><a href="mailto:'+c.email+'">'+c.email+'</a></div>':'')+
      (c.notes?'<div class="card-row"><span class="ic">ℹ️</span><span style="color:var(--text3)">'+c.notes+'</span></div>':'')+
      '</div>'+
      (c.custNotes?'<div style="padding:8px 18px 0"><div style="padding:8px 12px;background:rgba(185,255,102,.06);border-radius:8px;font-size:.8rem;color:var(--accent)">📝 '+c.custNotes+'</div></div>':'')+
      '<div class="card-actions"><div class="card-right"><button class="status-btn '+sc+'" onclick="cycleStatus(\''+c.id+'\')"><span class="status-dot"></span>'+sl+'</button></div><div class="card-right"><button class="btn-ic '+(c.called?'called':'')+'" onclick="tC(\''+c.id+'\')">📞</button><button class="btn-ic" onclick="toggleNotes(this)">📝</button></div></div>'+
      '<div class="card-notes"><textarea placeholder="Dodaj bilješku..." onblur="sN(\''+c.id+'\',this.value)">'+(c.custNotes||'')+'</textarea></div>'+
      '</div>';
  }).join('');
  setTimeout(function(){document.querySelectorAll('.contact-card').forEach(function(c,i){setTimeout(function(){c.classList.add('visible')},i*30)})},50);
}

function cycleStatus(id){var all=gc(),c=null;all.forEach(function(x){if(x.id===id)c=x});if(!c)return;var n={pending:'in_progress',in_progress:'done',done:'pending'};var ns=n[c.status];uc(id,'status',ns);renderContacts();initBento();updateCounts();toast(ns==='done'?'✅ Završeno':ns==='in_progress'?'⏳ U toku':'↩️ Čeka')}
function tC(id){var v=!(ls()[id]&&ls()[id].called);uc(id,'called',v);renderContacts();initBento();updateCounts();toast(v?'📞 Označeno zvano':'↩️ Maknuto')}
function sN(id,n){uc(id,'notes',n)}
function toggleNotes(btn){var n=btn.closest('.contact-card').querySelector('.card-notes');n.classList.toggle('open');btn.classList.toggle('exp-active')}

document.getElementById('filterBar').addEventListener('click',function(e){var p=e.target.closest('.filter-pill');if(!p)return;document.querySelectorAll('.filter-pill').forEach(function(x){x.classList.remove('active')});p.classList.add('active');filter=p.dataset.filter;renderContacts()});
document.getElementById('searchInput').addEventListener('input',function(){renderContacts()});

var glow=document.getElementById('cursorGlow');
document.addEventListener('mousemove',function(e){glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'});

/* Settings */
function toggleSettings(){document.getElementById('settingsDrop').classList.toggle('show')}
function setMode(m,btn){if(m==='light')document.body.classList.add('light');else document.body.classList.remove('light');document.querySelectorAll('.mode-btn').forEach(function(b){b.classList.remove('active')});btn.classList.add('active')}
function setAccent(a1,a2,a3,el){var r=document.documentElement;r.style.setProperty('--accent',a1);r.style.setProperty('--accent2',a2);r.style.setProperty('--accent3',a3);r.style.setProperty('--grad','linear-gradient(135deg,'+a1+','+a2+')');
  document.querySelectorAll('.color-dot').forEach(function(d){d.classList.remove('active')});el.classList.add('active');
  /* Update Three.js particles */
  if(window.particleMat)window.particleMat.color.set(a1);
}

function expCSV(){var all=gc(),csv='Firma,Vlasnik,Grad,Kategorija,Telefon,Email,Bilješke,Status,Zvali\n';all.forEach(function(c){csv+='"'+c.company+'","'+c.owner+'","'+c.city+'","'+c.category+'","'+c.phone+'","'+c.email+'","'+(c.custNotes||c.notes)+'","'+c.status+'","'+(c.called?'Da':'Ne')+'"\n'});dl('leadovi-bih.csv',csv,'text/csv')}
function expJSON(){dl('leadovi-bih.json',JSON.stringify(gc(),null,2),'application/json')}
function dl(n,c,t){var b=new Blob([c],{type:t}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download=n;a.click();URL.revokeObjectURL(u);toast('📥 '+n)}
function resetAll(){if(confirm('Resetovati sve?')){localStorage.removeItem(DB);initBento();updateCounts();renderContacts();toast('🔄 Resetovano')}}

/* Three.js Particles */
function initThree(){
  if(typeof THREE==='undefined')return;
  var canvas=document.getElementById('three-canvas');
  var renderer=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:true});
  renderer.setSize(window.innerWidth,window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  var scene=new THREE.Scene();
  var camera=new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
  camera.position.z=30;
  var count=500;
  var geo=new THREE.BufferGeometry();
  var pos=new Float32Array(count*3);
  for(var i=0;i<count*3;i++){pos[i]=(Math.random()-0.5)*60}
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  var mat=new THREE.PointsMaterial({color:0xb9ff66,size:0.15,transparent:true,opacity:0.6});
  window.particleMat=mat;
  var pts=new THREE.Points(geo,mat);
  scene.add(pts);
  /* Add floating torus */
  var torusGeo=new THREE.TorusGeometry(8,0.3,16,100);
  var torusMat=new THREE.MeshBasicMaterial({color:0xb9ff66,transparent:true,opacity:0.08,wireframe:true});
  var torus=new THREE.Mesh(torusGeo,torusMat);
  scene.add(torus);
  var torus2=new THREE.Mesh(new THREE.TorusGeometry(12,0.2,16,100),new THREE.MeshBasicMaterial({color:0x39ff14,transparent:true,opacity:0.05,wireframe:true}));
  scene.add(torus2);
  function animate(){requestAnimationFrame(animate);pts.rotation.y+=0.001;pts.rotation.x+=0.0005;torus.rotation.x+=0.003;torus.rotation.y+=0.002;torus2.rotation.x-=0.002;torus2.rotation.z+=0.001;renderer.render(scene,camera)}
  animate();
  window.addEventListener('resize',function(){camera.aspect=window.innerWidth/window.innerHeight;camera.updateProjectionMatrix();renderer.setSize(window.innerWidth,window.innerHeight)});
}

window.addEventListener('load',function(){
  setTimeout(function(){document.getElementById('loader').classList.add('hide')},1200);
  setTimeout(function(){initBento();updateCounts();renderContacts();initThree()},1500);
});
