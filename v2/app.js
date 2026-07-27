/* LeadFlow v2 — App Logic */
var currentUser=null,currentView='overview',currentCountry='ba',currentAgent=null,selectedContact=null,aiTab='chat';
var COUNTRY_FLAGS={ba:'🇧🇦',hr:'🇭🇷',rs:'🇷🇸'};
var COUNTRY_NAMES={ba:'Bosna i Hercegovina',hr:'Hrvatska',rs:'Srbija'};
var CAT_ICONS={'Frizerski salon':'✂️','Kozmetički salon':'💆','Restoran':'🍽️','Auto servis':'🔧','Caffe bar':'☕','Trgovina':'🛒','Stolarija':'🪟','Cvjećara':'🌸','Autopraonica':'🚗','Auto dijelovi':'⚙️','Optika':'👓','Trgovina odjećom':'👗','Električar':'⚡','Putnička agencija':'✈️','Hotel':'🏨','Advokat':'⚖️','Računovodstvo':'📊','Fitness':'💪','Pekara':'🥐','Autolimar':'🔨','Građevinska':'🏗️','Stomatologija':'🦷','Knjižara':'📚','Fitness studio':'💪','Auto':'🚗'};

/* ===== AI Mentor ===== */
var AI_SCRIPTS=[
  {title:'Telefonski poziv — Hladni poziv',desc:'Struktura poziva: Predstavljanje → Problem → Rješenje → Termin',tag:'Sales',country:'all'},
  {title:'Follow-up email nakon poziva',desc:'Template emaila sa personaliziranom porukom i CTA',tag:'Email',country:'all'},
  {title:'Analiza konkurencije — tržište BiH',desc:'Kako analizirati konkurenciju i pronaći USP za klijenta',tag:'Analiza',country:'ba'},
  {title:'Lokalni SEO za male biznise',desc:'Koraci za optimizaciju Google My Business profila',tag:'Marketing',country:'all'},
  {title:'Social media strategija',desc:'Kreiranje sadržaja za Instagram/Facebook lokalnog biznisa',tag:'Marketing',country:'all'},
  {title:'Pregovaračke vještine — Cijena',desc:'Kako pregovarati o cijeni bez gubitka vrijednosti',tag:'Sales',country:'all'},
  {title:'Scenarij: Klijent kaže "Previše je"',desc:'Odgovori na najčešće prigovore tokom prodaje',tag:'Script',country:'all'},
  {title:'Analiza portfelja klijenata',desc:'Kategorizacija klijenata po prioritetu i potencijalu',tag:'Analiza',country:'all'}
];

function aiGetContext(){
  if(!selectedContact)return 'Općenito';
  return selectedContact.company+' ('+selectedContact.city+', '+selectedContact.cat+')';
}
function aiGenerateReply(msg){
  var ctx=aiGetContext();
  var lower=msg.toLowerCase();
  if(lower.indexOf('poziv')!==-1||lower.indexOf('telefon')!==-1||lower.indexOf('zvati')!==-1){
    return '📞 <strong>Strategija poziva za '+ctx+'</strong><br><br>1. <strong>Priprema:</strong> Pročitaj bilješke o klijentu prije poziva<br>2. <strong>Uvod:</strong> "Dobar dan, zovem iz LeadFlow agencije..."<br>3. <strong>Vrijednost:</strong> Fokusiraj se na problem koji rješavate<br>4. <strong>CTA:</strong> Predloži sastanak ili demo<br><br>Trajanje poziva: max 3-5 minuta. Budi kratak i fokusiran.';
  }
  if(lower.indexOf('email')!==-1||lower.indexOf('poruk')!==-1){
    return '✉️ <strong>Template emaila za '+ctx+'</strong><br><br><code>Zdravo [Ime],<br><br>Vidio sam vaš biznis u [Grad] i imam ideju koja bi vam mogla pomoći da privučete više klijenata.<br><br>Biste li imali 15 minuta za kratki razgovor?<br><br>Lijep pozdrav</code><br><br>Personaliziraj uvod — spomeni nešto specifično o njihovom poslu.';
  }
  if(lower.indexOf('cijen')!==-1||lower.indexOf('skupo')!==-1||lower.indexOf('budget')!==-1){
    return '💰 <strong>Pregovori o cijeni za '+ctx+'</strong><br><br>Klijenti često kažu "previše je" — to nije odbijanje, to je pregovor.<br><br>✅ <strong>Tipični prigovori:</strong><br>• "Nemam budžet" → "Razumijem. Koliki ROI očekujete za X mjeseci?"<br>• "Skupo je" → "U usporedbi s čim? Koliko vas košta da NEMATE web?"<br>• "Razmisli ću" → "Naravno. Šta vas najviše zanima da razjasnim?"';
  }
  if(lower.indexOf('analiz')!==-1||lower.indexOf('statist')!==-1){
    var contacts=getUserContacts(currentUser.id);
    var done=contacts.filter(function(c){return c.status==='done'}).length;
    var prog=contacts.filter(function(c){return c.status==='in_progress'}).length;
    var pend=contacts.filter(function(c){return c.status==='pending'}).length;
    var cal=contacts.filter(function(c){return c.called}).length;
    return '📊 <strong>Analiza portfelja — '+currentUser.name+'</strong><br><br>• Ukupno kontakata: <strong>'+contacts.length+'</strong><br>• Završeno: <strong>'+done+'</strong> ('+(contacts.length?Math.round(done/contacts.length*100):0)+'%)<br>• U toku: <strong>'+prog+'</strong><br>• Čeka: <strong>'+pend+'</strong><br>• Pozvano: <strong>'+cal+'</strong><br><br>📈 <strong>Preporuka:</strong> '+(pend>done?'Fokusiraj se na kontakte koji čekaju — imaš '+pend+' nepozvanih.':'Odličan rad! Nastavi s follow-up pozivima za završene.');
  }
  if(lower.indexOf('konkurenc')!==-1||lower.indexOf('konkurent')!==-1){
    return '🔍 <strong>Analiza konkurencije — '+ctx+'</strong><br><br>1. <strong>Google Maps:</strong> Provjeri recenzije konkurenata u istom gradu<br>2. <strong>Web prisutnost:</strong> Imaju li web, Instagram, Facebook?<br>3. <strong>Cijene:</strong> Jesu li skuplji ili jeftiniji?<br>4. <strong>USP:</strong> Šta TI možeš ponuditi što oni ne mogu?<br><br>Tvoj adut: Nudiš digitalnu transformaciju za firme koje nemaju web prisutnost.';
  }
  if(lower.indexOf('seo')!==-1||lower.indexOf('google')!==-1){
    return '🔎 <strong>Lokalni SEO za '+ctx+'</strong><br><br>1. <strong>Google My Business:</strong> Postavi profil sa slikama, radnim vremenom, opisom<br>2. <strong>Recenzije:</strong> Traži od klijenata da ostave recenziju<br>3. <strong>Ključne riječi:</strong> "[kategorija] u [grad]" npr. "frizerski salon Sarajevo"<br>4. <strong>Fotografije:</strong> Redovito objavljuj slike rada<br><br>⏱️ Rezultati SEO: 3-6 mjeseci za prve rezultate.';
  }
  /* Default */
  return '🤖 <strong>AI Mentor — '+ctx+'</strong><br><br>Tvoje pitanje: "'+msg+'"<br><br>Možeš me pitati o:<br>• <strong>"Poziv"</strong> — strategija telefonskog poziva<br>• <strong>"Email"</strong> — template emaila<br>• <strong>"Cijena"</strong> — pregovori o cijeni<br>• <strong>"Analiza"</strong> — pregled tvog portfelja<br>• <strong>"Konkurencija"</strong> — kako analizirati konkurente<br>• <strong>"SEO"</strong> — lokalni SEO savjeti';
}

/* ===== Auth ===== */
function doLogin(userId,pass){
  var u=USERS.find(function(x){return x.id===userId});
  if(!u)return false;
  if(u.pass!==pass)return false;
  currentUser=u;
  localStorage.setItem(DB+'_session',JSON.stringify({id:u.id}));
  return true;
}
function tryRestoreSession(){
  try{var s=JSON.parse(localStorage.getItem(DB+'_session'));if(s){currentUser=USERS.find(function(x){return x.id===s.id});return!!currentUser}}catch(e){return false}
}
function doLogout(){currentUser=null;localStorage.removeItem(DB+'_session');showLogin()}
function showLogin(){document.getElementById('loginOverlay').classList.remove('hidden');document.getElementById('appLayout').classList.remove('active')}
function showApp(){document.getElementById('loginOverlay').classList.add('hidden');document.getElementById('appLayout').classList.add('active');render()}

/* ===== Views ===== */
function switchView(v){currentView=v;currentAgent=null;selectedContact=null;render()}
function switchCountry(c){currentCountry=c;currentAgent=null;selectedContact=null;render()}
function selectAgent(uid){currentAgent=uid;currentView='agent-contacts';selectedContact=null;render()}
function selectContact(c){selectedContact=c;renderContactDetail();renderAIContent()}

/* ===== Render ===== */
function render(){
  updateTopbar();
  updateSidebar();
  var cs=document.getElementById('contentScroll');
  if(currentView==='overview')renderOverview(cs);
  else if(currentView==='country')renderCountry(cs);
  else if(currentView==='agent-contacts')renderAgentContacts(cs);
  renderAIContent();
}
function updateTopbar(){
  var u=currentUser;
  document.getElementById('topTitle').textContent=u.name;
  var bc='';
  if(currentView==='overview')bc='Pregled';
  else if(currentView==='country')bc=COUNTRY_FLAGS[currentCountry]+' '+COUNTRY_NAMES[currentCountry];
  else if(currentView==='agent-contacts'){var ag=USERS.find(function(x){return x.id===currentAgent});bc=(ag?ag.name:'')+' — Kontakti'}
  document.getElementById('topBC').textContent=bc;
  document.getElementById('topAvatar').style.background=u.color;
  document.getElementById('topAvatar').textContent=u.initials;
  document.getElementById('topAvatarTitle').textContent=u.name;
}
function updateSidebar(){
  var sb=document.getElementById('sidebarIcons');
  var icons=[
    {id:'overview',icon:'📊',tip:'Pregled'},
    {id:'ba',icon:'🇧🇦',tip:'BiH'},
    {id:'hr',icon:'🇭🇷',tip:'Hrvatska'},
    {id:'rs',icon:'🇷🇸',tip:'Srbija'}
  ];
  if(currentUser.country!=='all'){
    icons=icons.filter(function(i){return i.id==='overview'||i.id===currentUser.country});
  }
  sb.innerHTML=icons.map(function(i){
    var active=(currentView===i.id||(currentView==='country'&&currentCountry===i.id)||(currentView==='agent-contacts'&&currentCountry===i.id))?'active':'';
    return '<button class="sidebar-icon '+active+'" onclick="'+(i.id==='overview'?"switchView('overview')":"switchCountry('"+i.id+"')")+'" title="'+i.tip+'">'+i.icon+'</button>';
  }).join('')+'<div class="sidebar-sep"></div>'+
  '<button class="sidebar-icon" onclick="toggleAIRight()" title="AI Mentor">🤖</button>'+
  '<div class="sidebar-bottom"><div class="sidebar-sep"></div><button class="sidebar-icon" onclick="doLogout()" title="Odjavi se">🚪</button></div>';
}

/* ===== Overview ===== */
function renderOverview(el){
  var all=getAllContacts();
  var stats={ba:{total:0,done:0,agents:{}},hr:{total:0,done:0,agents:{}},rs:{total:0,done:0,agents:{}}};
  all.forEach(function(c){if(!stats[c.country])return;stats[c.country].total++;if(c.status==='done')stats[c.country].done++;if(!stats[c.country].agents[c.owner])stats[c.country].agents[c.owner]=0;stats[c.country].agents[c.owner]++});
  var canSee=(currentUser.country==='all')?['ba','hr','rs']:[currentUser.country];
  el.innerHTML='<div class="country-tabs"><button class="country-tab active" onclick="switchView(\'overview\')">📊 Sve zemlje</button></div>'+
  '<div class="overview-grid">'+canSee.map(function(co){
    var s=stats[co]||{total:0,done:0,agents:{}};
    var pct=s.total?Math.round(s.done/s.total*100):0;
    var teamsHtml=Object.keys(s.agents).map(function(uid){
      var u=USERS.find(function(x){return x.id===uid});
      return '<div class="oc-team"><span style="color:var(--text)">'+(u?u.name:uid)+'</span><span style="color:var(--accent);font-weight:600">'+s.agents[uid]+'</span></div>';
    }).join('');
    return '<div class="overview-card '+co+'"><div class="oc-flag">'+COUNTRY_FLAGS[co]+'</div><div class="oc-name">'+COUNTRY_NAMES[co]+'</div><div class="oc-count">'+s.total+' kontakata · '+pct+'% završeno</div><div class="oc-teams">'+teamsHtml+'</div></div>';
  }).join('')+'</div>';
}

/* ===== Country ===== */
function renderCountry(el){
  var contacts=getCountryContacts(currentCountry);
  var agents={};
  contacts.forEach(function(c){if(!agents[c.owner])agents[c.owner]=0;agents[c.owner]++});
  var canSee=(currentUser.country==='all')?Object.keys(agents):[currentUser.id];
  var agentUsers=canSee.filter(function(uid){return agents[uid]}).map(function(uid){return USERS.find(function(x){return x.id===uid)}});
  el.innerHTML='<div class="country-tabs">'+
  ['ba','hr','rs'].map(function(co){
    var cls=currentCountry===co?'active':'';
    var cnt=getCountryContacts(co).length;
    return '<button class="country-tab '+cls+'" onclick="switchCountry(\''+co+'\')">'+COUNTRY_FLAGS[co]+' '+COUNTRY_NAMES[co]+' <span class="ct">'+cnt+'</span></button>';
  }).join('')+'</div>'+
  '<div class="team-grid">'+agentUsers.map(function(u){
    var uc=contacts.filter(function(c){return c.owner===u.id});
    var done=uc.filter(function(c){return c.status==='done'}).length;
    var prog=uc.filter(function(c){return c.status==='in_progress'}).length;
    return '<div class="team-card" onclick="selectAgent(\''+u.id+'\')"><div class="team-av" style="background:'+u.color+';color:#000">'+u.initials+'</div><div class="team-name">'+u.name+'</div><div class="team-role">'+u.role+'</div><div class="team-stats"><div class="team-stat"><div class="team-stat-val">'+uc.length+'</div><div class="team-stat-lbl">Ukupno</div></div><div class="team-stat"><div class="team-stat-val" style="color:var(--success)">'+done+'</div><div class="team-stat-lbl">Završeno</div></div><div class="team-stat"><div class="team-stat-val" style="color:var(--info)">'+prog+'</div><div class="team-stat-lbl">U toku</div></div></div></div>';
  }).join('')+'</div>';
}

/* ===== Agent Contacts ===== */
function renderAgentContacts(el){
  var contacts=getUserContacts(currentAgent);
  var agent=USERS.find(function(x){return x.id===currentAgent});
  var pend=contacts.filter(function(c){return c.status==='pending'}).length;
  var prog=contacts.filter(function(c){return c.status==='in_progress'}).length;
  var done=contacts.filter(function(c){return c.status==='done'}).length;
  var pct=contacts.length?Math.round(done/contacts.length*100):0;
  el.innerHTML='<div class="country-tabs"><button class="country-tab active" onclick="switchCountry(\''+currentCountry+'\')">'+COUNTRY_FLAGS[currentCountry]+' '+COUNTRY_NAMES[currentCountry]+'</button></div>'+
  '<div class="bento"><div class="bento-card"><div class="b-icon" style="background:rgba(185,255,102,.1);color:var(--accent)">📋</div><div class="b-val">'+contacts.length+'</div><div class="b-lbl">Ukupno</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(251,191,36,.1);color:#fbbf24">⏳</div><div class="b-val" style="color:#fbbf24">'+pend+'</div><div class="b-lbl">Čeka</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(56,189,248,.1);color:#38bdf8">🔄</div><div class="b-val" style="color:#38bdf8">'+prog+'</div><div class="b-lbl">U toku</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(52,211,153,.1);color:#34d399">✅</div><div class="b-val" style="color:#34d399">'+pct+'%</div><div class="b-lbl">Završeno</div></div></div>'+
  '<div style="display:flex;gap:8px;margin-bottom:14px;align-items:center"><button class="btn-primary" onclick="toggleAddForm()">+ Dodaj kontakt</button><span style="font-size:.78rem;color:var(--text3)">'+agent.name+'</span></div>'+
  '<div class="add-form" id="addForm"><div class="form-grid">'+
  '<div class="form-field"><label>Ime</label><input id="afFirst" placeholder="Ime"></div>'+
  '<div class="form-field"><label>Prezime</label><input id="afLast" placeholder="Prezime"></div>'+
  '<div class="form-field full"><label>Firma</label><input id="afCompany" placeholder="Naziv firme"></div>'+
  '<div class="form-field"><label>Grad</label><input id="afCity" placeholder="Grad"></div>'+
  '<div class="form-field"><label>Kategorija</label><input id="afCat" placeholder="npr. Frizerski salon"></div>'+
  '<div class="form-field"><label>Telefon</label><input id="afPhone" placeholder="+387..."></div>'+
  '<div class="form-field"><label>Email</label><input id="afEmail" placeholder="email@example.com"></div>'+
  '<div class="form-field full"><label>Bilješke</label><textarea id="afNotes" placeholder="Dodatne informacije..."></textarea></div>'+
  '</div><div class="form-actions"><button class="btn-ghost" onclick="toggleAddForm()">Otkaži</button><button class="btn-primary" onclick="submitContact()">Spremi</button></div></div>'+
  '<div class="contact-list" id="contactList">'+contacts.map(function(c){
    var ini=(c.company||'?').split(' ').slice(0,2).map(function(w){return w[0]||''}).join('').toUpperCase();
    var sc=c.status==='done'?'s-done':c.status==='in_progress'?'s-progress':'s-pending';
    var sl=c.status==='done'?'✅ Završeno':c.status==='in_progress'?'⏳ U toku':'⏳ Čeka';
    var sel=selectedContact&&selectedContact._id===c._id?'selected':'';
    return '<div class="contact-item '+sel+'" onclick="selectContact('+JSON.stringify(c).replace(/"/g,'&quot;')+')">'+
    '<div class="ci-avatar" style="background:linear-gradient(135deg,'+(agent?agent.color:'#b9ff66')+'33,'+(agent?agent.color:'#39ff14')+'22)">'+ini+'</div>'+
    '<div class="ci-info"><div class="ci-name">'+c.company+'</div><div class="ci-meta"><span class="city">'+CAT_ICONS[c.cat]||'📋'+' '+c.cat+'</span> · '+c.city+'</div></div>'+
    '<div class="ci-status '+sc+'">'+sl+'</div></div>';
  }).join('')+'</div>';
}

/* ===== Contact Detail ===== */
function renderContactDetail(){
  if(!selectedContact)return;
  var el=document.getElementById('aiContent');
  /* We show detail in the AI panel's "notes" tab */
}

/* ===== Add Contact ===== */
function toggleAddForm(){var f=document.getElementById('addForm');if(f)f.classList.toggle('open')}
function submitContact(){
  var c={owner:currentAgent,country:currentCountry,first:document.getElementById('afFirst').value.trim(),last:document.getElementById('afLast').value.trim(),company:document.getElementById('afCompany').value.trim(),city:document.getElementById('afCity').value.trim(),cat:document.getElementById('afCat').value.trim(),phone:document.getElementById('afPhone').value.trim(),email:document.getElementById('afEmail').value.trim(),notes:document.getElementById('afNotes').value.trim(),status:'pending',called:false,customNotes:''};
  if(!c.company){toast('⚠️ Unesi naziv firme');return}
  addContact(c);
  toggleAddForm();
  toast('✅ Kontakt dodan');
  render();
}

/* ===== AI Right Panel ===== */
function toggleAIRight(){document.getElementById('sidebarRight').classList.toggle('show')}
function renderAIContent(){
  if(!currentUser)return;
  var el=document.getElementById('aiContent');
  var tabsEl=document.getElementById('aiTabs');
  tabsEl.innerHTML=['chat','notes','scripts'].map(function(t){
    var labels={chat:'💬 Chat',notes:'📝 Bilješke',scripts:'📜 Skripte'};
    var cls=aiTab===t?'active':'';
    return '<div class="ai-tab '+cls+'" onclick="switchAITab(\''+t+'\')">'+labels[t]+'</div>';
  }).join('');
  if(aiTab==='chat')renderAIChat(el);
  else if(aiTab==='notes')renderAINotes(el);
  else if(aiTab==='scripts')renderAIScripts(el);
}
function switchAITab(t){aiTab=t;renderAIContent()}

function renderAIChat(el){
  var ctx=aiGetContext();
  el.innerHTML='<div class="ai-msg mentor"><div class="ml">🤖 AI Mentor</div><div class="mt">Zdravo '+currentUser.name.split(' ')[0]+'! Trenutno gledaš: <strong>'+ctx+'</strong><br><br>Kako ti mogu pomoći? Pitaj me o pozivima, emailima, cijenama, analizi...</div></div>'+
  '<div class="ai-suggest"><button onclick="aiQuick(\'Kako da pozovem ovog klijenta?\')">📞 Poziv</button><button onclick="aiQuick(\'Napiši mi email template\')">✉️ Email</button><button onclick="aiQuick(\'Kako da pregovaram o cijeni?\')">💰 Cijena</button><button onclick="aiQuick(\'Daj mi analizu mog portfelja\')">📊 Analiza</button></div>'+
  '<div id="aiMessages"></div>';
  document.getElementById('aiInput').value='';
}
function aiQuick(msg){document.getElementById('aiInput').value=msg;aiSend()}
function aiSend(){
  var input=document.getElementById('aiInput');
  var msg=input.value.trim();
  if(!msg)return;
  var msgs=document.getElementById('aiMessages');
  msgs.innerHTML+='<div class="ai-msg user"><div class="ml">Ti</div><div class="mt">'+msg+'</div></div>';
  var reply=aiGenerateReply(msg);
  msgs.innerHTML+='<div class="ai-msg mentor"><div class="ml">🤖 AI Mentor</div><div class="mt">'+reply+'</div></div>';
  input.value='';
  msgs.parentElement.scrollTop=msgs.parentElement.scrollHeight;
}

function renderAINotes(el){
  if(!selectedContact){
    el.innerHTML='<div class="ai-msg mentor"><div class="ml">📝 Bilješke</div><div class="mt">Odaberi kontakt sa strane da vidiš i uređuješ bilješke.</div></div>';
    return;
  }
  var c=selectedContact;
  el.innerHTML='<div class="ai-msg mentor" style="background:rgba(185,255,102,.04);border-color:rgba(185,255,102,.1)"><div class="ml">'+c.company+'</div><div class="mt"><strong>'+c.city+'</strong> · '+c.cat+(c.phone?'<br>📞 '+c.phone:'')+(c.email?'<br>✉️ '+c.email:'')+'</div></div>'+
  '<div style="margin-top:4px"><label style="display:block;font-size:.65rem;font-weight:600;text-transform:uppercase;color:var(--text3);margin-bottom:4px">Bilješke za klijenta</label>'+
  '<textarea id="notesTA" style="width:100%;min-height:100px;padding:10px;border-radius:8px;border:1px solid var(--glass-border);background:rgba(255,255,255,.03);color:var(--text);font-family:var(--font-b);font-size:.82rem;resize:vertical;outline:none" onblur="saveNotes(\''+c._id+'\',this.value)">'+(c.customNotes||'')+'</textarea></div>'+
  '<div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap">'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px" onclick="cycleStatus(\''+c._id+'\')">'+(c.status==='done'?'↩️ Reset status':c.status==='in_progress'?'✅ Označi završeno':'⏳ Stavi u toku')+'</button>'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px" onclick="toggleCalled(\''+c._id+'\')">'+(c.called?'↩️ Nije zvano':'📞 Označi zvano')+'</button>'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px;color:var(--danger)" onclick="delContact(\''+c._id+'\')">🗑️ Obriši</button></div>';
}
function saveNotes(id,v){updateContact(id,'customNotes',v);toast('📝 Bilješke spremljene')}
function cycleStatus(id){var all=getContacts(),c=all[id];if(!c)return;var n={pending:'in_progress',in_progress:'done',done:'pending'};updateContact(id,'status',n[c.status]);selectedContact=getContacts()[id];render();toast('✅ Status ažuriran')}
function toggleCalled(id){var all=getContacts(),c=all[id];if(!c)return;updateContact(id,'called',!c.called);selectedContact=getContacts()[id];render();toast(c.called?'↩️ Nije zvano':'📞 Označeno zvano')}
function delContact(id){if(confirm('Obrisati kontakt?')){deleteContact(id);selectedContact=null;render();toast('🗑️ Kontakt obrisan')}}

function renderAIScripts(el){
  var filtered=AI_SCRIPTS.filter(function(s){return s.country==='all'||s.country===currentUser.country});
  el.innerHTML='<div style="margin-bottom:6px;font-size:.7rem;color:var(--text3)">Skripte i vodiči za '+COUNTRY_NAMES[currentUser.country]+'</div>'+
  filtered.map(function(s){
    return '<div class="script-card" onclick="aiQuick(\'Objasni mi skriptu: '+s.title+'\')"><div class="sc-t">'+s.title+'</div><div class="sc-d">'+s.desc+'</div><div class="sc-tag">'+s.tag+'</div></div>';
  }).join('');
}

/* ===== Init ===== */
function toast(msg){var c=document.getElementById('toastBox'),t=document.createElement('div');t.className='toast';t.textContent=msg;c.appendChild(t);setTimeout(function(){t.remove()},2500)}

function initLoginAvatars(){
  var el=document.getElementById('loginAvatars');
  var selectedUid=null;
  el.innerHTML=USERS.map(function(u){
    return '<div class="login-av" style="background:'+u.color+';color:#000" data-uid="'+u.id+'" onclick="selectLoginUser(\''+u.id+'\',this)">'+u.initials+'<div class="login-av-name">'+u.name.split(' ')[0]+'</div></div>';
  }).join('');
  document.getElementById('doLogin').addEventListener('click',function(){
    var uid=document.querySelector('.login-av.sel')?.dataset?.uid;
    var pass=document.getElementById('loginPass').value;
    if(!uid){showLoginErr('Odaberi korisnika');return}
    if(doLogin(uid,pass)){showApp();selectedContact=null}
    else{showLoginErr('Netočna lozinka')}
  });
}
function selectLoginUser(uid,el){
  document.querySelectorAll('.login-av').forEach(function(e){e.classList.remove('sel')});
  el.classList.add('sel');
  document.getElementById('loginPass').focus();
}
function showLoginErr(msg){var e=document.getElementById('loginErr');e.textContent=msg;e.style.display='block';setTimeout(function(){e.style.display='none'},3000)}

window.addEventListener('DOMContentLoaded',function(){
  seedContacts();
  if(tryRestoreSession())showApp();
  else showLogin();
  initLoginAvatars();
});
