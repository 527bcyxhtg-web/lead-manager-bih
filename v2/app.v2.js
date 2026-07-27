/* LeadFlow Platform v2 — App Logic */

var USERS=[
  {id:'natasa',name:'Nataša Damnjanović',role:'Agent – BiH',avatar:'👩‍💼',color:'#00ffaa',password:'lead2024'},
  {id:'ana',name:'Ana Marić',role:'Agent – Hrvatska',avatar:'👩‍💻',color:'#00ccff',password:'lead2024'},
  {id:'marko',name:'Marko Petrović',role:'Agent – Srbija',avatar:'👨‍💼',color:'#ff00aa',password:'lead2024'},
  {id:'admin',name:'Admin',role:'Administrator',avatar:'👑',color:'#ffaa00',password:'admin123'}
];

var COUNTRIES={ba:'Bosna i Hercegovina',hr:'Hrvatska',rs:'Srbija'};
var FLAGS={ba:'🇧🇦',hr:'🇭🇷',rs:'🇷🇸'};

var CAT_ICONS={
  'Frizerski salon':'✂️','Kozmetički salon':'💆','Restoran':'🍽️','Auto servis':'🔧',
  'Caffe bar':'☕','Trgovina':'🛒','Stolarija':'🪵','Cvjećara':'🌸',
  'Autopraonica':'🚗','Auto dijelovi':'⚙️','Optika':'👓','Trgovina odjećom':'👖',
  'Električar':'⚡','Putnička agencija':'✈️','Hotel':'🏨','Advokat':'⚖️',
  'Računovodstvo':'📊','Fitness':'💪','Pekara':'🥐','Autolimar':'🔨',
  'Građevinska':'🏗️','Stomatologija':'🦷','Knjižar':'📚','Fitness studio':'🏋️','Auto':'🚗'
};

var current_user=null, current_view='overview', current_country='ba', selected=null;
var sidebar_open=false, ai_open=false, theme_panel_open=false;

/* ═══════════════════════════════════════════
   INIT
   ═══════════════════════════════════════════ */
function boot(){
  console.log('LeadFlow booting...');
  initTheme();
  initParticles();
  showLogin();
  document.getElementById('doLogin').addEventListener('click',doLogin);
  document.getElementById('loginPass').addEventListener('keydown',function(e){if(e.key==='Enter')doLogin()});
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',boot);}else{boot();}

/* ═══════════════════════════════════════════
   THEME
   ═══════════════════════════════════════════ */
function initTheme(){
  var saved=localStorage.getItem('lf-theme')||'dark';
  var accent=localStorage.getItem('lf-accent')||'#00ffaa';
  document.documentElement.setAttribute('data-theme',saved);
  document.documentElement.style.setProperty('--accent',accent);
  document.documentElement.style.setProperty('--accent-glow',accent+'33');
}

function toggleThemePanel(){
  theme_panel_open=!theme_panel_open;
  var p=document.getElementById('themePanel');
  p.style.display=theme_panel_open?'block':'none';
  if(theme_panel_open) renderThemeOptions();
}

function renderThemeOptions(){
  var el=document.getElementById('themeOptions');
  var themes=[{name:'Dark',val:'dark'},{name:'Light',val:'light'},{name:'Deep Space',val:'deep-space'}];
  var accents=['#00ffaa','#00ccff','#ff00aa','#ffaa00','#aa66ff','#ff4444','#44ff44'];
  var h='';
  themes.forEach(function(t){
    var active=document.documentElement.getAttribute('data-theme')===t.val;
    h+='<button class="theme-opt'+(active?' active':'')+'" onclick="setTheme(\''+t.val+'\')">'+t.name+'</button>';
  });
  h+='<div style="margin-top:12px;font-size:11px;opacity:.5">Accent</div><div style="display:flex;gap:6px;margin-top:6px;flex-wrap:wrap">';
  accents.forEach(function(c){
    var cur=getComputedStyle(document.documentElement).getPropertyValue('--accent').trim();
    h+='<div onclick="setAccent(\''+c+'\')" style="width:28px;height:28px;border-radius:50%;background:'+c+';cursor:pointer;border:2px solid '+(cur===c?'#fff':'transparent')+';box-shadow:0 0 8px '+c+'44"></div>';
  });
  h+='</div>';
  el.innerHTML=h;
}

function setTheme(t){
  document.documentElement.setAttribute('data-theme',t);
  localStorage.setItem('lf-theme',t);
  renderThemeOptions();
}

function setAccent(c){
  document.documentElement.style.setProperty('--accent',c);
  document.documentElement.style.setProperty('--accent-glow',c+'33');
  localStorage.setItem('lf-accent',c);
  renderThemeOptions();
}

/* ═══════════════════════════════════════════
   PARTICLES
   ═══════════════════════════════════════════ */
function initParticles(){
  var canvas=document.getElementById('particleCanvas');
  if(!canvas) return;
  var ctx=canvas.getContext('2d');
  var particles=[];
  function resize(){canvas.width=window.innerWidth;canvas.height=window.innerHeight;}
  resize();
  window.addEventListener('resize',resize);
  for(var i=0;i<60;i++){
    particles.push({
      x:Math.random()*canvas.width, y:Math.random()*canvas.height,
      vx:(Math.random()-.5)*.3, vy:(Math.random()-.5)*.3,
      r:Math.random()*2+.5, a:Math.random()*.4+.1
    });
  }
  function draw(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    var accent=getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()||'#00ffaa';
    particles.forEach(function(p){
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<0)p.x=canvas.width; if(p.x>canvas.width)p.x=0;
      if(p.y<0)p.y=canvas.height; if(p.y>canvas.height)p.y=0;
      ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=accent; ctx.globalAlpha=p.a; ctx.fill();
    });
    ctx.globalAlpha=1;
    requestAnimationFrame(draw);
  }
  draw();
}

/* ═══════════════════════════════════════════
   LOGIN
   ═══════════════════════════════════════════ */
function showLogin(){
  console.log('showLogin called');
  var el=document.getElementById('loginAvatars');
  if(!el){console.error('loginAvatars not found');return;}
  var h='';
  USERS.forEach(function(u){
    h+='<div class="avatar-card" onclick="selectAvatar(\''+u.id+'\')" id="av-'+u.id+'">';
    h+='<div class="avatar-emoji">'+u.avatar+'</div>';
    h+='<div class="avatar-name">'+u.name+'</div>';
    h+='<div class="avatar-role">'+u.role+'</div></div>';
  });
  el.innerHTML=h;
}

function selectAvatar(id){
  document.querySelectorAll('.avatar-card').forEach(function(c){c.classList.remove('selected')});
  var card=document.getElementById('av-'+id);
  if(card) card.classList.add('selected');
  current_user=USERS.find(function(u){return u.id===id});
  document.getElementById('loginPass').focus();
}

function doLogin(){
  if(!current_user){showToast('Odaberi profil!','error');return;}
  var pass=document.getElementById('loginPass').value;
  if(pass!==current_user.password){
    document.getElementById('loginErr').textContent='Pogrešna lozinka!';
    return;
  }
  document.getElementById('loginOverlay').style.display='none';
  document.getElementById('appLayout').style.display='flex';
  initApp();
}

/* ═══════════════════════════════════════════
   APP INIT
   ═══════════════════════════════════════════ */
function initApp(){
  renderSidebar();
  renderTopbar();
  navigateTo('overview');
  renderThemeSwitcher();
}

function renderSidebar(){
  var items=[
    {id:'overview',icon:'📊',label:'Pregled'},
    {id:'ba',icon:'🇧🇦',label:'BiH'},
    {id:'hr',icon:'🇭🇷',label:'Hrvatska'},
    {id:'rs',icon:'🇷🇸',label:'Srbija'},
    {id:'tarot',icon:'🔮',label:'Tarot'},
    {id:'settings',icon:'⚙️',label:'Postavke'}
  ];
  var el=document.getElementById('sidebarIcons');
  var h='';
  items.forEach(function(it){
    var active=(it.id===current_view||(it.id===current_country&&current_view==='country'))?' active':'';
    h+='<div class="sidebar-item'+active+'" onclick="navigateTo(\''+it.id+'\')">';
    h+='<div class="sidebar-icon">'+it.icon+'</div>';
    h+='<div class="sidebar-label">'+it.label+'</div></div>';
  });
  el.innerHTML=h;
}

function renderTopbar(){
  var title='Pregled';
  if(current_view==='country') title=FLAGS[current_country]+' '+COUNTRIES[current_country];
  else if(current_view==='tarot') title='🔮 Tarot dnevnik';
  else if(current_view==='settings') title='⚙️ Postavke';
  document.getElementById('topTitle').textContent=title;
  document.getElementById('topAvatar').innerHTML=current_user.avatar;
  var t=document.getElementById('topAvatarTitle');
  if(t) t.textContent=current_user.name;
}

function renderThemeSwitcher(){
  document.getElementById('themeSwitcher').style.display='flex';
}

function navigateTo(id){
  if(['ba','hr','rs'].indexOf(id)>=0){
    current_country=id; current_view='country';
  } else {
    current_view=id;
  }
  renderSidebar();
  renderTopbar();
  renderContent();
}

function renderContent(){
  var el=document.getElementById('contentScroll');
  if(current_view==='overview') renderOverview(el);
  else if(current_view==='country') renderCountry(el);
  else if(current_view==='tarot') renderTarot(el);
  else if(current_view==='settings') renderSettings(el);
}

/* ═══════════════════════════════════════════
   OVERVIEW
   ═══════════════════════════════════════════ */
function renderOverview(el){
  var all=getContacts();
  var total=all.length;
  var done=all.filter(function(c){return c.status==='done'}).length;
  var pending=total-done;
  var sale_yes=all.filter(function(c){return c.sale==='yes'}).length;
  var categories={};
  all.forEach(function(c){categories[c.category]=(categories[c.category]||0)+1});
  var topCats=Object.keys(categories).sort(function(a,b){return categories[b]-categories[a]}).slice(0,5);

  var h='<div class="overview-grid">';
  h+=statCard('📋','Ukupno leadova',total);
  h+=statCard('✅','Završeno',done);
  h+=statCard('⏳','U toku',pending);
  h+=statCard('💰','Prodaja uspjela',sale_yes);
  h+='</div>';

  h+='<div class="section-title">Top kategorije</div><div class="cat-grid">';
  topCats.forEach(function(cat){
    h+='<div class="cat-pill">'+(CAT_ICONS[cat]||'📌')+' '+cat+' <span class="cat-count">'+categories[cat]+'</span></div>';
  });
  h+='</div>';

  h+='<div class="section-title">Po državama</div><div class="overview-grid">';
  Object.keys(COUNTRIES).forEach(function(cc){
    var cc_contacts=all.filter(function(c){return c.country===cc});
    h+='<div class="stat-card clickable" onclick="navigateTo(\''+cc+'\')">';
    h+='<div class="stat-icon">'+FLAGS[cc]+'</div>';
    h+='<div class="stat-label">'+COUNTRIES[cc]+'</div>';
    h+='<div class="stat-value">'+cc_contacts.length+'</div></div>';
  });
  h+='</div>';

  el.innerHTML=h;
}

function statCard(icon,label,value){
  return '<div class="stat-card"><div class="stat-icon">'+icon+'</div><div class="stat-value">'+value+'</div><div class="stat-label">'+label+'</div></div>';
}

/* ═══════════════════════════════════════════
   COUNTRY VIEW
   ═══════════════════════════════════════════ */
function renderCountry(el){
  var contacts=getContacts().filter(function(c){return c.country===current_country});
  var agents=getAgentsForCountry(current_country);

  var h='<div class="country-header">';
  h+='<div class="country-flag-big">'+FLAGS[current_country]+'</div>';
  h+='<div class="country-stats">';
  h+='<span>'+contacts.length+' kontakata</span>';
  h+='<span>'+contacts.filter(function(c){return c.status==='done'}).length+' završeno</span>';
  h+='</div></div>';

  if(agents.length>0){
    h+='<div class="agent-tabs">';
    h+='<div class="agent-tab active" onclick="filterAgent(null,this)">Svi</div>';
    agents.forEach(function(a){
      h+='<div class="agent-tab" onclick="filterAgent(\''+a.id+'\',this)">'+a.avatar+' '+a.name.split(' ')[0]+'</div>';
    });
    h+='</div>';
  }

  h+='<div class="search-bar"><input type="text" placeholder="🔍 Pretraži kontakate..." id="searchInput" oninput="filterContacts()"></div>';

  h+='<div class="contact-list" id="contactList">';
  contacts.forEach(function(c){ h+=contactCard(c); });
  h+='</div>';

  el.innerHTML=h;
}

function getAgentsForCountry(cc){
  if(cc==='ba') return USERS.filter(function(u){return u.id==='natasa'||u.id==='admin'});
  if(cc==='hr') return USERS.filter(function(u){return u.id==='ana'||u.id==='admin'});
  if(cc==='rs') return USERS.filter(function(u){return u.id==='marko'||u.id==='admin'});
  return [];
}

function contactCard(c){
  var statusClass=c.status==='done'?'done':'pending';
  var saleBadge='';
  if(c.status==='done'){
    saleBadge=c.sale==='yes'?'<span class="badge badge-success">✅ Prodaja</span>':'<span class="badge badge-fail">❌ Bez prodaje</span>';
  }
  return '<div class="contact-card '+statusClass+'" data-id="'+c.id+'" onclick="openContact(\''+c.id+'\')">'+
    '<div class="cc-top"><div class="cc-name">'+c.name+'</div>'+
    '<div class="cc-company">'+c.company+'</div></div>'+
    '<div class="cc-bottom"><span class="cc-cat">'+(CAT_ICONS[c.category]||'📌')+' '+c.category+'</span>'+
    '<span class="cc-phone">📞 '+c.phone+'</span>'+
    saleBadge+'</div>'+
    (c.comment?'<div class="cc-comment">💬 '+c.comment.substring(0,60)+(c.comment.length>60?'...':'')+'</div>':'')+
    '</div>';
}

function filterContacts(){
  var q=(document.getElementById('searchInput')||{}).value||'';
  q=q.toLowerCase();
  var cards=document.querySelectorAll('.contact-card');
  cards.forEach(function(card){
    var id=card.getAttribute('data-id');
    var c=getContacts().find(function(x){return x.id===id});
    if(!c) return;
    var match=c.name.toLowerCase().indexOf(q)>=0||c.company.toLowerCase().indexOf(q)>=0||c.category.toLowerCase().indexOf(q)>=0||c.phone.indexOf(q)>=0;
    card.style.display=match?'':'none';
  });
}

function filterAgent(agentId,tabEl){
  document.querySelectorAll('.agent-tab').forEach(function(t){t.classList.remove('active')});
  if(tabEl) tabEl.classList.add('active');
}

/* ═══════════════════════════════════════════
   CONTACT DETAIL MODAL
   ═══════════════════════════════════════════ */
function openContact(id){
  selected=getContacts().find(function(c){return c.id===id});
  if(!selected) return;
  var c=selected;
  var box=document.getElementById('contactModalBox');

  var h='<div class="modal-header">';
  h+='<div class="modal-avatar">'+(CAT_ICONS[c.category]||'📌')+'</div>';
  h+='<div><div class="modal-name">'+c.name+'</div>';
  h+='<div class="modal-company">'+c.company+'</div></div>';
  h+='<button class="modal-close" onclick="closeContactModal()">✕</button></div>';

  h+='<div class="modal-info-grid">';
  h+='<div class="modal-info"><span class="mi-label">📞 Telefon</span><span class="mi-val">'+c.phone+'</span></div>';
  if(c.email) h+='<div class="modal-info"><span class="mi-label">✉️ Email</span><span class="mi-val">'+c.email+'</span></div>';
  h+='<div class="modal-info"><span class="mi-label">📌 Kategorija</span><span class="mi-val">'+c.category+'</span></div>';
  h+='<div class="modal-info"><span class="mi-label">🌍 Država</span><span class="mi-val">'+FLAGS[c.country]+' '+COUNTRIES[c.country]+'</span></div>';
  if(c.owner) h+='<div class="modal-info"><span class="mi-label">👤 Vlasnik</span><span class="mi-val">'+c.owner+'</span></div>';
  h+='</div>';

  h+='<div class="modal-section-title">Status</div>';
  h+='<div class="status-controls">';
  h+='<button class="status-btn '+(c.status==='done'?'active-done':'')+'" onclick="setStatus(\''+c.id+'\',\'done\')">✅ Završeno</button>';
  h+='<button class="status-btn '+(c.status==='pending'?'active-pending':'')+'" onclick="setStatus(\''+c.id+'\',\'pending\')">⏳ U toku</button>';
  h+='</div>';

  if(c.status==='done'){
    h+='<div class="modal-section-title">Prodaja</div>';
    h+='<div class="status-controls">';
    h+='<button class="sale-btn '+(c.sale==='yes'?'active-yes':'')+'" onclick="setSale(\''+c.id+'\',\'yes\')">💰 Uspješna</button>';
    h+='<button class="sale-btn '+(c.sale==='no'?'active-no':'')+'" onclick="setSale(\''+c.id+'\',\'no\')">🚫 Neuspješna</button>';
    h+='</div>';
  }

  h+='<div class="modal-section-title">Komentar</div>';
  h+='<textarea class="comment-input" id="commentInput" placeholder="Dodaj komentar..." rows="3">'+(c.comment||'')+'</textarea>';
  h+='<button class="save-comment-btn" onclick="saveComment(\''+c.id+'\')">💾 Spremi komentar</button>';

  box.innerHTML=h;
  document.getElementById('contactModal').style.display='flex';
}

function closeContactModal(){
  document.getElementById('contactModal').style.display='none';
  selected=null;
}

function setStatus(id,status){
  var contacts=getContacts();
  var c=contacts.find(function(x){return x.id===id});
  if(c){c.status=status;c.sale=status==='pending'?null:c.sale;}
  saveContacts(contacts);
  openContact(id);
  renderContent();
  showToast(status==='done'?'✅ Kontakt označen kao završen':'⏳ Kontakt vraćen u toku');
}

function setSale(id,val){
  var contacts=getContacts();
  var c=contacts.find(function(x){return x.id===id});
  if(c) c.sale=val;
  saveContacts(contacts);
  openContact(id);
  showToast(val==='yes'?'💰 Prodaja zabilježena!':'🚫 Prodaja označena kao neuspješna');
}

function saveComment(id){
  var val=(document.getElementById('commentInput')||{}).value||'';
  var contacts=getContacts();
  var c=contacts.find(function(x){return x.id===id});
  if(c) c.comment=val;
  saveContacts(contacts);
  showToast('💬 Komentar spremljen');
}

/* ═══════════════════════════════════════════
   TAROT
   ═══════════════════════════════════════════ */
var TAROT_CARDS=[
  {name:'The Fool',emoji:'🃏',meaning:'Novi počeci, avantura, nevinost'},
  {name:'The Magician',emoji:'🎩',meaning:'Manifestacija, vještina, volja'},
  {name:'The High Priestess',emoji:'🌙',meaning:'Intuicija, tajne, podsvijest'},
  {name:'The Empress',emoji:'👑',meaning:'Plodnost, ljepota, priroda'},
  {name:'The Emperor',emoji:'🏛️',meaning:'Autoritet, struktura, stabilnost'},
  {name:'The Hierophant',emoji:'📿',meaning:'Tradicionalno znanje, vjera'},
  {name:'The Lovers',emoji:'💕',meaning:'Ljubav, izbor, harmonija'},
  {name:'The Chariot',emoji:'🏎️',meaning:'Pobjeda, odlučnost, snaga'},
  {name:'Strength',emoji:'🦁',meaning:'Unutarnja snaga, hrabrost'},
  {name:'The Hermit',emoji:'🏔️',meaning:'Mudrost, unutrašnje traženje'},
  {name:'Wheel of Fortune',emoji:'🎡',meaning:'Sudbina, ciklusi, promjene'},
  {name:'The Star',emoji:'⭐',meaning:'Nada, inspiracija, mir'},
  {name:'The Moon',emoji:'🌕',meaning:'Iluzije, strahovi, podsvijest'},
  {name:'The Sun',emoji:'☀️',meaning:'Sreća, uspjeh, energija'},
  {name:'Judgement',emoji:'📯',meaning:'Buđenje, poziv, procjena'},
  {name:'The World',emoji:'🌍',meaning:'Završetak, postignuće, putovanje'}
];

function renderTarot(el){
  var history=JSON.parse(localStorage.getItem('lf-tarot')||'[]');
  var h='<div class="tarot-container">';
  h+='<div class="tarot-title">🔮 Dnevnik tarot karata</div>';
  h+='<div class="tarot-subtitle">Povuci kartu za današnji dan</div>';
  h+='<button class="tarot-pull-btn" onclick="pullTarot()">✨ Vuci kartu</button>';
  h+='<div id="tarotResult"></div>';

  if(history.length>0){
    h+='<div class="tarot-history-title">Prethodna izvlačenja</div>';
    history.slice(-10).reverse().forEach(function(entry){
      h+='<div class="tarot-entry">';
      h+='<div class="tarot-entry-date">'+entry.date+'</div>';
      h+='<div class="tarot-entry-card">'+entry.card.emoji+' <strong>'+entry.card.name+'</strong></div>';
      h+='<div class="tarot-entry-meaning">'+entry.card.meaning+'</div>';
      if(entry.note) h+='<div class="tarot-entry-note">📝 '+entry.note+'</div>';
      h+='</div>';
    });
  }
  h+='</div>';
  el.innerHTML=h;
}

function pullTarot(){
  var card=TAROT_CARDS[Math.floor(Math.random()*TAROT_CARDS.length)];
  var today=new Date().toLocaleDateString('bs-BA');
  var history=JSON.parse(localStorage.getItem('lf-tarot')||'[]');

  var todayEntry=history.find(function(e){return e.date===today});
  if(todayEntry){
    document.getElementById('tarotResult').innerHTML=
      '<div class="tarot-pulled">'+todayEntry.card.emoji+'<div class="tp-name">'+todayEntry.card.name+'</div>'+
      '<div class="tp-meaning">'+todayEntry.card.meaning+'</div>'+
      '<div class="tp-date">Već izvučeno danas</div></div>';
    return;
  }

  var note=prompt('Dodaj bilješku za današnju kartu (opcionalno):')||'';
  history.push({date:today,card:card,note:note});
  localStorage.setItem('lf-tarot',JSON.stringify(history));

  document.getElementById('tarotResult').innerHTML=
    '<div class="tarot-pulled animate">'+card.emoji+'<div class="tp-name">'+card.name+'</div>'+
    '<div class="tp-meaning">'+card.meaning+'</div>'+
    (note?'<div class="tp-note">📝 '+note+'</div>':'')+
    '<div class="tp-date">'+today+'</div></div>';
}

/* ═══════════════════════════════════════════
   SETTINGS
   ═══════════════════════════════════════════ */
function renderSettings(el){
  var h='<div class="settings-container">';
  h+='<div class="settings-title">⚙️ Postavke</div>';
  h+='<div class="setting-group">';
  h+='<div class="setting-label">Trenutni korisnik</div>';
  h+='<div class="setting-val">'+current_user.avatar+' '+current_user.name+' ('+current_user.role+')</div></div>';
  h+='<div class="setting-group">';
  h+='<div class="setting-label">Ukupno kontakata</div>';
  h+='<div class="setting-val">'+getContacts().length+'</div></div>';
  h+='<div class="setting-group">';
  h+='<div class="setting-label">Izlaz</div>';
  h+='<button class="logout-btn" onclick="doLogout()">🚪 Odjavi se</button></div>';
  h+='</div>';
  el.innerHTML=h;
}

function doLogout(){
  current_user=null;
  document.getElementById('appLayout').style.display='none';
  document.getElementById('loginOverlay').style.display='flex';
  document.getElementById('loginPass').value='';
  document.querySelectorAll('.avatar-card').forEach(function(c){c.classList.remove('selected')});
}

/* ═══════════════════════════════════════════
   AI MENTOR
   ═══════════════════════════════════════════ */
function toggleAIRight(){
  ai_open=!ai_open;
  var sb=document.getElementById('sidebarRight');
  sb.style.display=ai_open?'flex':'none';
}

function aiSend(){
  var input=document.getElementById('aiInput');
  var msg=input.value.trim();
  if(!msg) return;
  input.value='';

  var content=document.getElementById('aiContent');
  content.innerHTML+='<div class="ai-msg user-msg">'+msg+'</div>';
  content.innerHTML+='<div class="ai-msg bot-msg" id="aiThinking">🤖 Razmišljam...</div>';
  content.scrollTop=content.scrollHeight;

  setTimeout(function(){
    var thinking=document.getElementById('aiThinking');
    if(thinking){
      thinking.innerHTML=getAIResponse(msg);
      thinking.removeAttribute('id');
      content.scrollTop=content.scrollHeight;
    }
  },800);
}

function getAIResponse(msg){
  var m=msg.toLowerCase();
  var contacts=getContacts();
  var done=contacts.filter(function(c){return c.status==='done'}).length;
  var total=contacts.length;

  if(m.indexOf('statistika')>=0||m.indexOf('koliko')>=0||m.indexOf('pregled')>=0){
    return '📊 <strong>Statistike:</strong><br>Ukupno: '+total+'<br>Završeno: '+done+'<br>U toku: '+(total-done)+
      '<br>Stopa završenih: '+Math.round(done/total*100)+'%';
  }
  if(m.indexOf('savjet')>=0||m.indexOf('preporuka')>=0||m.indexOf('kako')>=0){
    return '💡 <strong>Savjet:</strong> Fokusirajte se na kontakate koji su još u toku. Probajte personalizirani pristup.';
  }
  if(m.indexOf('kategorij')>=0){
    var cats={};
    contacts.forEach(function(c){cats[c.category]=(cats[c.category]||0)+1});
    var sorted=Object.keys(cats).sort(function(a,b){return cats[b]-cats[a]});
    return '📌 <strong>Kategorije:</strong><br>'+sorted.map(function(c){return c+': '+cats[c]}).join('<br>');
  }
  if(m.indexOf('držav')>=0||m.indexOf('bosn')>=0||m.indexOf('hrvats')>=0||m.indexOf('srbij')>=0){
    var byC={};
    contacts.forEach(function(c){byC[c.country]=(byC[c.country]||0)+1});
    return '🌍 <strong>Po državama:</strong><br>'+
      Object.keys(byC).map(function(c){return FLAGS[c]+' '+COUNTRIES[c]+': '+byC[c]}).join('<br>');
  }
  if(m.indexOf('prodaj')>=0){
    var sales=contacts.filter(function(c){return c.sale==='yes'}).length;
    return '💰 <strong>Prodaja:</strong> '+sales+' uspješnih od '+done+' završenih.<br>Stopa: '+Math.round(sales/done*100)+'%';
  }
  return '🤖 Mogu vam pomoći sa: Statistike, Savjeti, Kategorije, Države, Prodaja.';
}

/* ═══════════════════════════════════════════
   DATA
   ═══════════════════════════════════════════ */
function getContacts(){
  var stored=localStorage.getItem('lf-contacts');
  if(stored) return JSON.parse(stored);
  if(typeof LEAD_DATA!=='undefined') return LEAD_DATA;
  return [];
}

function saveContacts(data){
  localStorage.setItem('lf-contacts',JSON.stringify(data));
}

/* ═══════════════════════════════════════════
   TOAST & MOBILE
   ═══════════════════════════════════════════ */
function showToast(msg,type){
  var toast=document.createElement('div');
  toast.className='toast '+(type||'');
  toast.textContent=msg;
  document.getElementById('toastBox').appendChild(toast);
  setTimeout(function(){toast.classList.add('show')},10);
  setTimeout(function(){toast.classList.remove('show');setTimeout(function(){toast.remove()},300)},2500);
}

function toggleMobileSidebar(){
  var sb=document.getElementById('sidebarIcons');
  sidebar_open=!sidebar_open;
  sb.classList.toggle('mobile-open',sidebar_open);
}
