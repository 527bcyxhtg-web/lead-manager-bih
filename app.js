/* LeadFlow v2 — App Logic */
var currentUser=null,currentView='overview',currentCountry='ba',currentAgent=null,selectedContact=null,aiTab='chat';
var COUNTRY_FLAGS={ba:'\uD83C\uDDE7\uD83C\uDDEE',hr:'\uD83C\uDDED\uD83C\uDDDD',rs:'\uD83C\uDDF7\uD83C\uDDF8'};
var COUNTRY_NAMES={ba:'Bosna i Hercegovina',hr:'Hrvatska',rs:'Srbija'};
var CAT_ICONS={'Frizerski salon':'\u2702\uFE0F','Kozmetički salon':'\uD83D\uDC86','Restoran':'\uD83C\uDF7D\uFE0F','Auto servis':'\uD83D\uDD27','Caffe bar':'\u2615','Trgovina':'\uD83D\uDED2','Stolarija':'\uD83E\uDE9F','Cvjećara':'\uD83C\uDF38','Autopraonica':'\uD83D\uDE97','Auto dijelovi':'\u2699\uFE0F','Optika':'\uD83D\uDC53','Trgovina odjećom':'\uD83D\uDC57','Električar':'\u26A1','Putnička agencija':'\u2708\uFE0F','Hotel':'\uD83C\uDFE8','Advokat':'\u2696\uFE0F','Računovodstvo':'\uD83D\uDCCA','Fitness':'\uD83D\uDCAA','Pekara':'\uD83E\uDD50','Autolimar':'\uD83D\uDD28','Građevinska':'\uD83C\uDFD7\uFE0F','Stomatologija':'\uD83E\uDDB7','Knjižara':'\uD83D\uDCDA','Fitness studio':'\uD83D\uDCAA','Auto':'\uD83D\uDE97'};

var AI_SCRIPTS=[
  {title:'Telefonski poziv \u2014 Hladni poziv',desc:'Struktura poziva: Predstavljanje \u2192 Problem \u2192 Rje\u0161enje \u2192 Termin',tag:'Sales',country:'all'},
  {title:'Follow-up email nakon poziva',desc:'Template emaila sa personaliziranom porukom i CTA',tag:'Email',country:'all'},
  {title:'Analiza konkurencije \u2014 tr\u017Ei\u0161te BiH',desc:'Kako analizirati konkurenciju i prona\u0107i USP za klijenta',tag:'Analiza',country:'ba'},
  {title:'Lokalni SEO za male biznise',desc:'Koraci za optimizaciju Google My Business profila',tag:'Marketing',country:'all'},
  {title:'Social media strategija',desc:'Kreiranje sadr\u017Eaja za Instagram/Facebook lokalnog biznisa',tag:'Marketing',country:'all'},
  {title:'Pregovara\u010Dke vje\u0161tine \u2014 Cijena',desc:'Kako pregovarati o cijeni bez gubitka vrijednosti',tag:'Sales',country:'all'},
  {title:'Scenarij: Klijent ka\u017Ee "Previ\u0161e je"',desc:'Odgovori na naj\u010De\u0167\u0107e prigovore tokom prodaje',tag:'Script',country:'all'},
  {title:'Analiza portfelja klijenata',desc:'Kategorizacija klijenata po prioritetu i potencijalu',tag:'Analiza',country:'all'}
];

function aiGetContext(){
  if(!selectedContact)return 'Op\u0107enito';
  return selectedContact.company+' ('+selectedContact.city+', '+selectedContact.cat+')';
}
function aiGenerateReply(msg){
  var ctx=aiGetContext();
  var lower=msg.toLowerCase();
  if(lower.indexOf('poziv')!==-1||lower.indexOf('telefon')!==-1||lower.indexOf('zvati')!==-1){
    return '\uD83D\uDCDE <strong>Strategija poziva za '+ctx+'</strong><br><br>1. <strong>Priprema:</strong> Pro\u010Ditaj bilje\u0161ke o klijentu prije poziva<br>2. <strong>Uvod:</strong> "Dobar dan, zovem iz LeadFlow agencije..."<br>3. <strong>Vrijednost:</strong> Fokusiraj se na problem koji rje\u0161avate<br>4. <strong>CTA:</strong> Predlo\u017Ei sastanak ili demo<br><br>Trajanje poziva: max 3-5 minuta.';
  }
  if(lower.indexOf('email')!==-1||lower.indexOf('poruk')!==-1){
    return '\u2709\uFE0F <strong>Template emaila za '+ctx+'</strong><br><br><code>Zdravo [Ime],<br><br>Vidio sam va\u0161 biznis u [Grad] i imam ideju koja bi vam mogla pomo\u0107i da privu\u010Dete vi\u0161e klijenata.<br><br>Biste li imali 15 minuta za kratki razgovor?<br><br>Lijep pozdrav</code><br><br>Personaliziraj uvod.';
  }
  if(lower.indexOf('cijen')!==-1||lower.indexOf('skupo')!==-1||lower.indexOf('budget')!==-1){
    return '\uD83D\uDCB0 <strong>Pregovori o cijeni za '+ctx+'</strong><br><br>Klijenti \u010Desto ka\u017Eu "previ\u0161e je" \u2014 to nije odbijanje.<br><br>\u2705 <strong>Tipi\u010Dni prigovori:</strong><br>\u2022 "Nemam bud\u017Eet" \u2192 "Koliki ROI o\u010Dekujete za X mjeseci?"<br>\u2022 "Skupo je" \u2192 "Koliko vas ko\u0161ta da NEMATE web?"<br>\u2022 "Razmisli \u0107u" \u2192 "\u0160ta vas najvi\u0161e zanima da razjasnim?"';
  }
  if(lower.indexOf('analiz')!==-1||lower.indexOf('statist')!==-1){
    var contacts=getUserContacts(currentUser.id);
    var done=contacts.filter(function(c){return c.status==='done'}).length;
    var prog=contacts.filter(function(c){return c.status==='in_progress'}).length;
    var pend=contacts.filter(function(c){return c.status==='pending'}).length;
    var cal=contacts.filter(function(c){return c.called}).length;
    return '\uD83D\uDCCA <strong>Analiza portfelja \u2014 '+currentUser.name+'</strong><br><br>\u2022 Ukupno kontakata: <strong>'+contacts.length+'</strong><br>\u2022 Zavr\u0161eno: <strong>'+done+'</strong><br>\u2022 U toku: <strong>'+prog+'</strong><br>\u2022 \u010Ceka: <strong>'+pend+'</strong><br>\u2022 Pozvano: <strong>'+cal+'</strong><br><br>\uD83D\uDCC8 <strong>Preporuka:</strong> '+(pend>done?'Fokusiraj se na '+pend+' nepozvanih.':'Odli\u010Dan rad! Nastavi s follow-up pozivima.');
  }
  if(lower.indexOf('konkurenc')!==-1||lower.indexOf('konkurent')!==-1){
    return '\uD83D\uDD0D <strong>Analiza konkurencije \u2014 '+ctx+'</strong><br><br>1. <strong>Google Maps:</strong> Provjeri recenzije konkurenata<br>2. <strong>Web prisutnost:</strong> Imaju li web, Instagram, Facebook?<br>3. <strong>Cijene:</strong> Jesu li skuplji ili jeftiniji?<br>4. <strong>USP:</strong> \u0160ta TI mo\u017Ee\u0161 ponuditi \u0161to oni ne mogu?';
  }
  if(lower.indexOf('seo')!==-1||lower.indexOf('google')!==-1){
    return '\uD83D\uDD0E <strong>Lokalni SEO za '+ctx+'</strong><br><br>1. <strong>Google My Business:</strong> Postavi profil sa slikama<br>2. <strong>Recenzije:</strong> Tra\u017Ei od klijenata da ostave recenziju<br>3. <strong>Klju\u010Dne rije\u010Di:</strong> "[kategorija] u [grad]"<br>4. <strong>Fotografije:</strong> Redovito objavljuj slike rada';
  }
  return '\uD83E\uDD16 <strong>AI Mentor \u2014 '+ctx+'</strong><br><br>Pitaj me o:<br>\u2022 <strong>"Poziv"</strong> \u2014 strategija poziva<br>\u2022 <strong>"Email"</strong> \u2014 template emaila<br>\u2022 <strong>"Cijena"</strong> \u2014 pregovori<br>\u2022 <strong>"Analiza"</strong> \u2014 pregled portfelja<br>\u2022 <strong>"Konkurencija"</strong> \u2014 analiza konkurenata<br>\u2022 <strong>"SEO"</strong> \u2014 lokalni SEO savjeti';
}

function doLogin(userId,pass){
  var u=USERS.find(function(x){return x.id===userId});
  if(!u||u.pass!==pass)return false;
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

function switchView(v){currentView=v;currentAgent=null;selectedContact=null;render()}
function switchCountry(c){currentCountry=c;currentAgent=null;selectedContact=null;render()}
function selectAgent(uid){currentAgent=uid;currentView='agent-contacts';selectedContact=null;render()}
function selectContact(c){selectedContact=c;renderAIContent()}

function render(){
  updateTopbar();updateSidebar();
  var cs=document.getElementById('contentScroll');
  if(currentView==='overview')renderOverview(cs);
  else if(currentView==='country')renderCountry(cs);
  else if(currentView==='agent-contacts')renderAgentContacts(cs);
  renderAIContent();
}
function updateTopbar(){
  document.getElementById('topTitle').textContent=currentUser.name;
  var bc='';
  if(currentView==='overview')bc='Pregled';
  else if(currentView==='country')bc=COUNTRY_FLAGS[currentCountry]+' '+COUNTRY_NAMES[currentCountry];
  else if(currentView==='agent-contacts'){var ag=USERS.find(function(x){return x.id===currentAgent});bc=ag?ag.name:''}
  document.getElementById('topBC').textContent=bc;
  document.getElementById('topAvatar').style.background=currentUser.color;
  document.getElementById('topAvatar').textContent=currentUser.initials;
}
function updateSidebar(){
  var sb=document.getElementById('sidebarIcons');
  var icons=[{id:'overview',icon:'\uD83D\uDCCA',tip:'Pregled'}];
  if(currentUser.country==='all'){
    icons.push({id:'ba',icon:'\uD83C\uDDE7\uD83C\uDDEE',tip:'BiH'});
    icons.push({id:'hr',icon:'\uD83C\uDDED\uD83C\uDDDD',tip:'Hrvatska'});
    icons.push({id:'rs',icon:'\uD83C\uDDF7\uD83C\uDDF8',tip:'Srbija'});
  }else{
    icons.push({id:currentUser.country,icon:COUNTRY_FLAGS[currentCountry],tip:COUNTRY_NAMES[currentCountry]});
  }
  sb.innerHTML=icons.map(function(i){
    var active=(currentView===i.id||(currentView==='country'&&currentCountry===i.id)||(currentView==='agent-contacts'&&currentCountry===i.id))?'active':'';
    var fn=i.id==='overview'?"switchView('overview')":"switchCountry('"+i.id+"')";
    return '<button class="sidebar-icon '+active+'" onclick="'+fn+'" title="'+i.tip+'">'+i.icon+'</button>';
  }).join('')+'<div class="sidebar-sep"></div><button class="sidebar-icon" onclick="toggleAIRight()" title="AI Mentor">\uD83E\uDD16</button><div class="sidebar-bottom"><div class="sidebar-sep"></div><button class="sidebar-icon" onclick="doLogout()" title="Odjavi se">\uD83D\uDEAA</button></div>';
}

function renderOverview(el){
  var all=getAllContacts();
  var stats={ba:{total:0,done:0,agents:{}},hr:{total:0,done:0,agents:{}},rs:{total:0,done:0,agents:{}}};
  all.forEach(function(c){if(!stats[c.country])return;stats[c.country].total++;if(c.status==='done')stats[c.country].done++;if(!stats[c.country].agents[c.owner])stats[c.country].agents[c.owner]=0;stats[c.country].agents[c.owner]++});
  var canSee=(currentUser.country==='all')?['ba','hr','rs']:[currentUser.country];
  el.innerHTML='<div class="country-tabs"><button class="country-tab active">\uD83D\uDCCA Sve zemlje</button></div><div class="overview-grid">'+canSee.map(function(co){
    var s=stats[co]||{total:0,done:0,agents:{}};
    var pct=s.total?Math.round(s.done/s.total*100):0;
    var teamsHtml=Object.keys(s.agents).map(function(uid){
      var u=USERS.find(function(x){return x.id===uid});
      return '<div class="oc-team"><span style="color:var(--text)">'+(u?u.name:uid)+'</span><span style="color:var(--accent);font-weight:600">'+s.agents[uid]+'</span></div>';
    }).join('');
    return '<div class="overview-card '+co+'"><div class="oc-flag">'+COUNTRY_FLAGS[co]+'</div><div class="oc-name">'+COUNTRY_NAMES[co]+'</div><div class="oc-count">'+s.total+' kontakata \u00B7 '+pct+'% zavr\u0161eno</div><div class="oc-teams">'+teamsHtml+'</div></div>';
  }).join('')+'</div>';
}

function renderCountry(el){
  var contacts=getCountryContacts(currentCountry);
  var agents={};
  contacts.forEach(function(c){if(!agents[c.owner])agents[c.owner]=0;agents[c.owner]++});
  var canSee=(currentUser.country==='all')?Object.keys(agents):[currentUser.id];
  var agentUsers=canSee.filter(function(uid){return agents[uid]}).map(function(uid){return USERS.find(function(x){return x.id===uid})}).filter(Boolean);
  el.innerHTML='<div class="country-tabs">'+
  ['ba','hr','rs'].map(function(co){
    var cls=currentCountry===co?'active':'';
    var cnt=getCountryContacts(co).length;
    return '<button class="country-tab '+cls+'" onclick="switchCountry(\''+co+'\')">'+COUNTRY_FLAGS[co]+' '+COUNTRY_NAMES[co]+' <span class="ct">'+cnt+'</span></button>';
  }).join('')+'</div><div class="team-grid">'+agentUsers.map(function(u){
    var uc=contacts.filter(function(c){return c.owner===u.id});
    var done=uc.filter(function(c){return c.status==='done'}).length;
    var prog=uc.filter(function(c){return c.status==='in_progress'}).length;
    return '<div class="team-card" onclick="selectAgent(\''+u.id+'\')"><div class="team-av" style="background:'+u.color+';color:#000">'+u.initials+'</div><div class="team-name">'+u.name+'</div><div class="team-role">'+u.role+'</div><div class="team-stats"><div class="team-stat"><div class="team-stat-val">'+uc.length+'</div><div class="team-stat-lbl">Ukupno</div></div><div class="team-stat"><div class="team-stat-val" style="color:var(--success)">'+done+'</div><div class="team-stat-lbl">Zavr\u0161eno</div></div><div class="team-stat"><div class="team-stat-val" style="color:var(--info)">'+prog+'</div><div class="team-stat-lbl">U toku</div></div></div></div>';
  }).join('')+'</div>';
}

function renderAgentContacts(el){
  var contacts=getUserContacts(currentAgent);
  var agent=USERS.find(function(x){return x.id===currentAgent});
  var pend=contacts.filter(function(c){return c.status==='pending'}).length;
  var prog=contacts.filter(function(c){return c.status==='in_progress'}).length;
  var done=contacts.filter(function(c){return c.status==='done'}).length;
  var pct=contacts.length?Math.round(done/contacts.length*100):0;
  el.innerHTML='<div class="country-tabs"><button class="country-tab active" onclick="switchCountry(\''+currentCountry+'\')">'+COUNTRY_FLAGS[currentCountry]+' '+COUNTRY_NAMES[currentCountry]+'</button></div>'+
  '<div class="bento"><div class="bento-card"><div class="b-icon" style="background:rgba(185,255,102,.1);color:var(--accent)"><pre></div><div class="b-val">'+contacts.length+'</div><div class="b-lbl">Ukupno</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(251,191,36,.1);color:#fbbf24">\u23F3</div><div class="b-val" style="color:#fbbf24">'+pend+'</div><div class="b-lbl">\u010Ceka</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(56,189,248,.1);color:#38bdf8">\uD83D\uDD04</div><div class="b-val" style="color:#38bdf8">'+prog+'</div><div class="b-lbl">U toku</div></div>'+
  '<div class="bento-card"><div class="b-icon" style="background:rgba(52,211,153,.1);color:#34d399">\u2705</div><div class="b-val" style="color:#34d399">'+pct+'%</div><div class="b-lbl">Zavr\u0161eno</div></div></div>'+
  '<div style="display:flex;gap:8px;margin-bottom:14px;align-items:center"><button class="btn-primary" onclick="toggleAddForm()">+ Dodaj kontakt</button><span style="font-size:.78rem;color:var(--text3)">'+agent.name+'</span></div>'+
  '<div class="add-form" id="addForm"><div class="form-grid">'+
  '<div class="form-field"><label>Ime</label><input id="afFirst" placeholder="Ime"></div>'+
  '<div class="form-field"><label>Prezime</label><input id="afLast" placeholder="Prezime"></div>'+
  '<div class="form-field full"><label>Firma</label><input id="afCompany" placeholder="Naziv firme"></div>'+
  '<div class="form-field"><label>Grad</label><input id="afCity" placeholder="Grad"></div>'+
  '<div class="form-field"><label>Kategorija</label><input id="afCat" placeholder="npr. Frizerski salon"></div>'+
  '<div class="form-field"><label>Telefon</label><input id="afPhone" placeholder="+387..."></div>'+
  '<div class="form-field"><label>Email</label><input id="afEmail" placeholder="email@example.com"></div>'+
  '<div class="form-field full"><label>Bilje\u0161ke</label><textarea id="afNotes" placeholder="Dodatne informacije..."></textarea></div>'+
  '</div><div class="form-actions"><button class="btn-ghost" onclick="toggleAddForm()">Otka\u017Ei</button><button class="btn-primary" onclick="submitContact()">Spremi</button></div></div>'+
  '<div class="contact-list" id="contactList">'+contacts.map(function(c){
    var ini=(c.company||'?').split(' ').slice(0,2).map(function(w){return w[0]||''}).join('').toUpperCase();
    var sc=c.status==='done'?'s-done':c.status==='in_progress'?'s-progress':'s-pending';
    var sl=c.status==='done'?'\u2705 Zavr\u0161eno':c.status==='in_progress'?'\u23F3 U toku':'\u23F3 \u010Ceka';
    var sel=selectedContact&&selectedContact._id===c._id?'selected':'';
    return '<div class="contact-item '+sel+'" onclick=\'selectContact('+JSON.stringify(c).replace(/'/g,"\\'")+')\'>'+
    '<div class="ci-avatar" style="background:linear-gradient(135deg,'+(agent?agent.color:'#b9ff66')+'33,'+(agent?agent.color:'#39ff14')+'22)">'+ini+'</div>'+
    '<div class="ci-info"><div class="ci-name">'+c.company+'</div><div class="ci-meta"><span class="city">'+(CAT_ICONS[c.cat]||'\uD83D\uDCCB')+' '+c.cat+'</span> \u00B7 '+c.city+'</div></div>'+
    '<div class="ci-status '+sc+'">'+sl+'</div></div>';
  }).join('')+'</div>';
}

function toggleAddForm(){var f=document.getElementById('addForm');if(f)f.classList.toggle('open')}
function submitContact(){
  var c={owner:currentAgent,country:currentCountry,first:document.getElementById('afFirst').value.trim(),last:document.getElementById('afLast').value.trim(),company:document.getElementById('afCompany').value.trim(),city:document.getElementById('afCity').value.trim(),cat:document.getElementById('afCat').value.trim(),phone:document.getElementById('afPhone').value.trim(),email:document.getElementById('afEmail').value.trim(),notes:document.getElementById('afNotes').value.trim(),status:'pending',called:false,customNotes:''};
  if(!c.company){toast('\u26A0\uFE0F Unesi naziv firme');return}
  addContact(c);toggleAddForm();toast('\u2705 Kontakt dodan');render();
}

function toggleAIRight(){document.getElementById('sidebarRight').classList.toggle('show')}
function renderAIContent(){
  if(!currentUser)return;
  var tabsEl=document.getElementById('aiTabs');
  tabsEl.innerHTML=['chat','notes','scripts'].map(function(t){
    var labels={chat:'\uD83D\uDCAC Chat',notes:'\uD83D\uDCDD Bilje\u0161ke',scripts:'\uD83D\uDCDC Skripte'};
    return '<div class="ai-tab '+(aiTab===t?'active':'')+'" onclick="switchAITab(\''+t+'\')">'+labels[t]+'</div>';
  }).join('');
  var el=document.getElementById('aiContent');
  if(aiTab==='chat')renderAIChat(el);
  else if(aiTab==='notes')renderAINotes(el);
  else if(aiTab==='scripts')renderAIScripts(el);
}
function switchAITab(t){aiTab=t;renderAIContent()}
function renderAIChat(el){
  var ctx=aiGetContext();
  el.innerHTML='<div class="ai-msg mentor"><div class="ml">\uD83E\uDD16 AI Mentor</div><div class="mt">Zdravo '+currentUser.name.split(' ')[0]+'! Gleda\u0161: <strong>'+ctx+'</strong><br><br>Kako ti mogu pomo\u0107i?</div></div>'+
  '<div class="ai-suggest"><button onclick="aiQuick(\'Kako da pozovem ovog klijenta?\')">\uD83D\uDCDE Poziv</button><button onclick="aiQuick(\'Napi\u0161i mi email template\')">\u2709\uFE0F Email</button><button onclick="aiQuick(\'Kako da pregovaram o cijeni?\')">\uD83D\uDCB0 Cijena</button><button onclick="aiQuick(\'Daj mi analizu mog portfelja\')">\uD83D\uDCCA Analiza</button></div>'+
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
  msgs.innerHTML+='<div class="ai-msg mentor"><div class="ml">\uD83E\uDD16 AI Mentor</div><div class="mt">'+aiGenerateReply(msg)+'</div></div>';
  input.value='';msgs.parentElement.scrollTop=msgs.parentElement.scrollHeight;
}
function renderAINotes(el){
  if(!selectedContact){el.innerHTML='<div class="ai-msg mentor"><div class="ml">\uD83D\uDCDD Bilje\u0161ke</div><div class="mt">Odaberi kontakt sa strane da vidi\u0161 bilje\u0161ke.</div></div>';return}
  var c=selectedContact;
  el.innerHTML='<div class="ai-msg mentor" style="background:rgba(185,255,102,.04);border-color:rgba(185,255,102,.1)"><div class="ml">'+c.company+'</div><div class="mt"><strong>'+c.city+'</strong> \u00B7 '+c.cat+(c.phone?'<br>\uD83D\uDCDE '+c.phone:'')+(c.email?'<br>\u2709\uFE0F '+c.email:'')+'</div></div>'+
  '<div style="margin-top:4px"><label style="display:block;font-size:.65rem;font-weight:600;text-transform:uppercase;color:var(--text3);margin-bottom:4px">Bilje\u0161ke za klijenta</label>'+
  '<textarea id="notesTA" style="width:100%;min-height:100px;padding:10px;border-radius:8px;border:1px solid var(--glass-border);background:rgba(255,255,255,.03);color:var(--text);font-family:var(--font-b);font-size:.82rem;resize:vertical;outline:none" onblur="saveNotes(\''+c._id+'\',this.value)">'+(c.customNotes||'')+'</textarea></div>'+
  '<div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap">'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px" onclick="cycleStatus(\''+c._id+'\')">'+(c.status==='done'?'\u21A9\uFE0F Reset status':c.status==='in_progress'?'\u2705 Zavr\u0161eno':'\u23F3 U toku')+'</button>'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px" onclick="toggleCalled(\''+c._id+'\')">'+(c.called?'\u21A9\uFE0F Nije zvano':'\uD83D\uDCDE Zvali')+'</button>'+
  '<button class="btn-ghost" style="font-size:.72rem;padding:5px 10px;color:var(--danger)" onclick="delContact(\''+c._id+'\')">\uD83D\uDDD1\uFE0F Obri\u0161i</button></div>';
}
function saveNotes(id,v){updateContact(id,'customNotes',v);toast('\uD83D\uDCDD Bilje\u0161ke spremljene')}
function cycleStatus(id){var all=getContacts(),c=all[id];if(!c)return;var n={pending:'in_progress',in_progress:'done',done:'pending'};updateContact(id,'status',n[c.status]);selectedContact=getContacts()[id];render();toast('\u2705 Status a\u017Euriran')}
function toggleCalled(id){var all=getContacts(),c=all[id];if(!c)return;updateContact(id,'called',!c.called);selectedContact=getContacts()[id];render();toast(c.called?'\u21A9\uFE0F Nije zvano':'\uD83D\uDCDE Zvali')}
function delContact(id){if(confirm('Obrisati kontakt?')){deleteContact(id);selectedContact=null;render();toast('\uD83D\uDDD1\uFE0F Kontakt obrisan')}}
function renderAIScripts(el){
  var filtered=AI_SCRIPTS.filter(function(s){return s.country==='all'||s.country===currentUser.country});
  el.innerHTML=filtered.map(function(s){
    return '<div class="script-card" onclick="aiQuick(\'Objasni mi: '+s.title+'\')"><div class="sc-t">'+s.title+'</div><div class="sc-d">'+s.desc+'</div><div class="sc-tag">'+s.tag+'</div></div>';
  }).join('');
}
function toast(msg){var c=document.getElementById('toastBox'),t=document.createElement('div');t.className='toast';t.textContent=msg;c.appendChild(t);setTimeout(function(){t.remove()},2500)}
function initLoginAvatars(){
  var el=document.getElementById('loginAvatars');
  if(!el)return;
  el.innerHTML=USERS.map(function(u){
    return '<div class="login-av" style="background:'+u.color+';color:#000" data-uid="'+u.id+'" onclick="selectLoginUser(\''+u.id+'\',this)">'+u.initials+'<div class="login-av-name">'+u.name.split(' ')[0]+'</div></div>';
  }).join('');
  document.getElementById('doLogin').addEventListener('click',function(){
    var uid=document.querySelector('.login-av.sel')?document.querySelector('.login-av.sel').getAttribute('data-uid'):null;
    var pass=document.getElementById('loginPass').value;
    if(!uid){showLoginErr('Odaberi korisnika');return}
    if(doLogin(uid,pass))showApp();
    else showLoginErr('Neto\u010Dna lozinka');
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
