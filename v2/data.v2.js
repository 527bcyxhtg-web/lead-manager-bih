/* LeadFlow Platform v2 — Data Layer + Tarot Cards */

var DB='lf_v2';
var USERS=[
  {id:'natasad',name:'Nataša Damnjanović',country:'ba',role:'Agent — Bosna',pass:'natasA123',color:'#fbbf24',initials:'ND'},
  {id:'mariob',name:'Mario Beara',country:'hr',role:'Agent — Hrvatska',pass:'mariO123',color:'#38bdf8',initials:'MB'},
  {id:'aleksav',name:'Aleksa Vukićević',country:'rs',role:'Agent — Srbija',pass:'aleksa123',color:'#f472b6',initials:'AV'},
  {id:'admin',name:'Admin',country:'all',role:'Administrator',pass:'admin123',color:'#b9ff66',initials:'AD'}
];

/* ── Seed Data ── */
var SEED_BA=[
  ["Almir","Alibegović","Frizerski salon A.A. Alibegović","Sarajevo","Frizerski salon","+387 33 537 539","",""],
  ["Amela","Husić","Frizerski salon Amela s.z.r.","Sarajevo","Frizerski salon","+387 62 583 854","","Baščaršija"],
  ["","Beauty Salon Na-Na","Sarajevo","Kozmetički salon","+387 61 666 002","info@na-na.ba",""],
  ["","Beauty First Salon & Spa","Sarajevo","Kozmetički salon","+387 33 977 913","","Ilidža"],
  ["","Ženski frizerski salon KIM","Sarajevo","Frizerski salon","+387 33 667 513","",""],
  ["Sead","Rizvić","Restoran Sarajevo Vl Rizvić","Sarajevo","Restoran","+387 61 053 678","",""],
  ["Semih","Aslan","Restoran Sofra d.o.o.","Sarajevo","Restoran","+387 33 447 815","","Baščaršija 31"],
  ["","Auto Servis Team","Sarajevo","Auto servis","+387 61 552 168","","Samo Facebook"],
  ["","Autoelektra","Sarajevo","Auto servis","+387 33 444 749","aesa@bih.net.ba",""],
  ["","Automotive Center","Sarajevo","Auto servis","+387 33 715 465","",""],
  ["","Dodir Kozmetički salon","Sarajevo","Kozmetički salon","+387 33 204 756","info@dodir.ba",""],
  ["","Nova Beauty d.o.o.","Sarajevo","Kozmetički salon","+387 62 725 741","",""],
  ["","Pekara AS d.o.o.","Sarajevo","Pekara","+387 33 610 286","",""],
  ["","SAPLAST d.o.o.","Sarajevo","Stolarija","+387 33 779 500","info@saplast.ba",""],
  ["","ELOX d.o.o.","Sarajevo","Stolarija","+387 61 984 333","info@elox.ba",""],
  ["","BH Werk d.o.o.","Sarajevo","Stolarija","+387 62 853 773","info@bhwerk.com",""],
  ["","DOM-A d.o.o.","Sarajevo","Stolarija","+387 61 264 233","info@dom-a.ba",""],
  ["Miroslav","Tomić","Caffe Miroslav Tomić","Banja Luka","Caffe bar","+387 65 385 026","",""],
  ["","Caffe Bar ARIA","Banja Luka","Caffe bar","","",""],
  ["","Tehnomag","Banja Luka","Trgovina","+387 51 200 000","banjaluka@tehnomag.com",""],
  ["","Motorex P.J. Bihać","Bihać","Auto dijelovi","+387 37 351 833","",""],
  ["","Cvjećara Vernisaž","Bihać","Cvjećara","+387 62 595 946","",""],
  ["","Cvjećara S-Garden","Bihać","Cvjećara","+387 63 597 585","",""],
  ["Snježana","Rajković","Cvjećara Iris Bihać","Bihać","Cvjećara","+387 66 955 874","",""],
  ["","DELFIN Autopraona","Bihać","Autopraonica","+387 61 591 903","",""],
  ["","Auto Lider d.o.o.","Brčko","Auto","+387 61 600 008","",""],
  ["Adis","Selimović","Autolimar ADO","Brčko","Autolimar","+387 62 180 655","",""],
  ["","Pulmont d.o.o.","Zenica","Građevinska","+387 32 402 045","",""],
  ["","Techno Shop Zenica","Zenica","Trgovina","+387 32 249 111","zenica@technoshop.ba",""],
  ["","ES OPTIC Visoko","Visoko","Optika","+387 62 148 462","",""],
  ["","Optika Tihić","Visoko","Optika","+387 61 925 925","",""],
  ["","Optika Beganović","Visoko","Optika","+387 62 750 800","",""],
  ["","BB NEW LOOK d.o.o.","Mostar","Trgovina odjećom","+387 36 317 299","",""],
  ["","ANGEL'S FASHION","Mostar","Trgovina odjećom","+387 36 322 360","",""],
  ["","Moda Best d.o.o.","Mostar","Trgovina odjećom","+387 36 836 257","",""],
  ["","FREE SHOP d.o.o.","Mostar","Trgovina odjećom","+387 36 550 385","",""],
  ["","Elko Marić d.o.o.","Mostar","Električar","+387 36 558 080","",""],
  ["","Intertekstil","Široki Brijeg","Trgovina odjećom","+387 39 705 451","",""],
  ["","Boutique Markos","Široki Brijeg","Trgovina odjećom","+387 39 705 743","",""],
  ["","La-Tour Agencija","Čapljina","Putnička agencija","+387 63 320 325","",""],
  ["","Hotel Turist '98","Jajce","Hotel","+387 30 658 151","",""],
  ["","Hotel Plivsko Jezero","Jajce","Hotel","+387 30 654 090","",""],
  ["Boban","Savić","Adv. kancelarija Savić","Doboj","Advokat","+387 66 490 494","",""],
  ["Irena","Puzić-Obradović","Adv. kancelarija Puzić-Obradović","Doboj","Advokat","+387 53 222 030","",""],
  ["","Finel Računovodstvo","Tuzla","Računovodstvo","+387 35 262 370","",""],
  ["","Revis Računovodstvo","Tuzla","Računovodstvo","+387 35 270 094","",""],
  ["","Atria d.o.o.","Tuzla","Računovodstvo","+387 61 732 398","",""],
  ["","Fitness Studio Fuke","Tuzla","Fitness","+387 61 179 000","",""],
  ["","Fitness Studio Dobar Osjećaj","Tuzla","Fitness","+387 61 271 655","",""],
  ["","Feel Good Fitness","Tuzla","Fitness","","feelgoodfitness875@gmail.com",""]
];
var SEED_HR=[
  ["","Dental Centar Split","Split","Stomatologija","+385 21 456 789","info@dc-split.hr",""],
  ["","Frizerski salon Zagreb","Zagreb","Frizerski salon","+385 1 234 5678","",""],
  ["","Kafić Riva","Dubrovnik","Caffe bar","+385 20 321 123","",""],
  ["","Auto Servis Rijeka","Rijeka","Auto servis","+385 51 555 123","",""],
  ["","Tehno Plus","Osijek","Trgovina","+385 31 456 789","",""]
];
var SEED_RS=[
  ["","Studio Lepote","Beograd","Kozmetički salon","+381 11 234 5678","",""],
  ["","Restoran Kod Braće","Beograd","Restoran","+381 11 987 6543","",""],
  ["","Auto Servis Niš","Niš","Auto servis","+381 18 345 678","",""],
  ["","Knjižara Vulkan","Novi Sad","Knjižara","+381 21 555 123","",""],
  ["","Fit Center Kragujevac","Kragujevac","Fitness","+381 34 222 333","",""]
];

function seedContacts(){
  if(localStorage.getItem(DB+'_c'))return;
  var a={};
  SEED_BA.forEach(function(r,i){a['ba_natasad_'+i]={owner:'natasad',country:'ba',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:'',saleOutcome:'',demoSent:false,comments:'',timeline:[]}});
  SEED_HR.forEach(function(r,i){a['hr_mariob_'+i]={owner:'mariob',country:'hr',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:'',saleOutcome:'',demoSent:false,comments:'',timeline:[]}});
  SEED_RS.forEach(function(r,i){a['rs_aleksav_'+i]={owner:'aleksav',country:'rs',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:'',saleOutcome:'',demoSent:false,comments:'',timeline:[]}});
  localStorage.setItem(DB+'_c',JSON.stringify(a));
}

function getContacts(){try{return JSON.parse(localStorage.getItem(DB+'_c'))||{}}catch(e){return{}}}
function saveContacts(c){localStorage.setItem(DB+'_c',JSON.stringify(c))}
function addContact(c){var all=getContacts(),id=c.country+'_'+c.owner+'_'+Date.now();all[id]=c;saveContacts(all);return id}
function updateContact(id,f,v){var a=getContacts();if(a[id]){a[id][f]=v;saveContacts(a)}}
function deleteContact(id){var a=getContacts();delete a[id];saveContacts(a)}
function getUserContacts(uid){var a=getContacts(),r=[];Object.keys(a).forEach(function(k){if(a[k].owner===uid){a[k]._id=k;r.push(a[k])}});return r}
function getCountryContacts(co){var a=getContacts(),r=[];Object.keys(a).forEach(function(k){if(a[k].country===co){a[k]._id=k;r.push(a[k])}});return r}
function getAllContacts(){var a=getContacts(),r=[];Object.keys(a).forEach(function(k){a[k]._id=k;r.push(a[k])});return r}

/* ── Backward Compatibility: migrate old contacts ── */
function migrateContacts(){
  var a=getContacts(),changed=false;
  Object.keys(a).forEach(function(k){
    var c=a[k];
    if(c.saleOutcome===undefined){c.saleOutcome='';changed=true}
    if(c.demoSent===undefined){c.demoSent=false;changed=true}
    if(c.comments===undefined){c.comments='';changed=true}
    if(c.timeline===undefined){c.timeline=[];changed=true}
  });
  if(changed)saveContacts(a);
}
function addTimelineEntry(id,event){
  var a=getContacts();if(!a[id])return;
  if(!a[id].timeline)a[id].timeline=[];
  a[id].timeline.push({event:event,time:new Date().toISOString()});
  saveContacts(a);
}

/* ── Theme Management ── */
var THEMES=['dark','light','ocean','sunset','neon','purple'];
var THEME_NAMES={dark:'Tamna',light:'Svijetla',ocean:'Ocean Plava',sunset:'Zalazak',neon:'Neon Zelena',purple:'Ljubičasta'};
function setTheme(t){document.documentElement.setAttribute('data-theme',t);localStorage.setItem(DB+'_theme',t)}
function getTheme(){return localStorage.getItem(DB+'_theme')||'dark'}

/* ── Tarot Cards (78 Major + Minor Arcana feel, 30+ curated) ── */
var TAROT_CARDS=[
  {id:1,name:'The Closer',emoji:'🏁',meaning:'Danas je dan za zaključivanje dogovora. Ne odgađaj.',color:'#b9ff66'},
  {id:2,name:'The Cold Call',emoji:'📞',meaning:'Hrabro nazovi. Iza straha čeka uspjeh.',color:'#fbbf24'},
  {id:3,name:'The Follow-Up',emoji:'📧',meaning:'Pošalji follow-up email. Podsjeti se na obećanje.',color:'#38bdf8'},
  {id:4,name:'The Listener',emoji:'👂',meaning:'Danas slušaj više nego što pričaš. Klijenti ti govore što trebaju.',color:'#f472b6'},
  {id:5,name:'The Networker',emoji:'🤝',meaning:'Proširi mrežu kontakata. Sastanak za kafu mijenja sve.',color:'#a78bfa'},
  {id:6,name:'The Strategist',emoji:'♟️',meaning:'Pauziraj i razmisli. Strategija pobjeđuje brzinu.',color:'#6366f1'},
  {id:7,name:'The Negotiator',emoji:'⚖️',meaning:'Danas je dan za pregovore. Fokusiraj se na vrijednost, ne cijenu.',color:'#f59e0b'},
  {id:8,name:'The Creative',emoji:'🎨',meaning:'Budi inventivan u pristupu. Originalnost privlači klijente.',color:'#ec4899'},
  {id:9,name:'The Closer II',emoji:'✍️',meaning:'Klijent je spreman. Samo mu reci: "Potpisujemo danas?"',color:'#10b981'},
  {id:10,name:'The Rest',emoji:'🌙',meaning:'Danas je za odmor. Sutra punom snagom.',color:'#8b5cf6'},
  {id:11,name:'The Mentor',emoji:'🎓',meaning:'Podijeli znanje s kolegama. Mentorstvo gradi tim.',color:'#06b6d4'},
  {id:12,name:'The Pioneer',emoji:'🚀',meaning:'Izađi iz zone komfora. Novi kanali = novi klijenti.',color:'#ef4444'},
  {id:13,name:'The Analyst',emoji:'📊',meaning:'Prouči brojke. Podaci ti govore šta radiš dobro.',color:'#3b82f6'},
  {id:14,name:'The Communicator',emoji:'💌',meaning:'Pošalji personaliziranu poruku. Masovni mailovi ne prolaze.',color:'#f97316'},
  {id:15,name:'The Closer III',emoji:'🏆',meaning:'Posljednji korak je najlakši. Zatraži potpis.',color:'#b9ff66'},
  {id:16,name:'The Helper',emoji:'🤲',meaning:'Pomozi klijentu besplatno. Dobar glas se širi.',color:'#14b8a6'},
  {id:17,name:'The Dreamer',emoji:'🌟',meaning:'Sanjaj veliko, ali kreni s malim koracima.',color:'#a855f7'},
  {id:18,name:'The Resilient',emoji:'💪',meaning:'Odbijanje nije kraj. To je put do "da".',color:'#f43f5e'},
  {id:19,name:'The Timer',emoji:'⏳',meaning:'Timing je sve. Ne žuri, ali ne čekaj predugo.',color:'#eab308'},
  {id:20,name:'The Observer',emoji:'🔍',meaning:'Promatraj konkurenciju. Nauči iz njihovih grešaka.',color:'#64748b'},
  {id:21,name:'The Builder',emoji:'🏗️',meaning:'Gradi dugoročne odnose, ne jednokratne transakcije.',color:'#78716c'},
  {id:22,name:'The Teacher',emoji:'📚',meaning:'Edukuj klijente. Ko zna — taj kupuje.',color:'#2563eb'},
  {id:23,name:'The Mirror',emoji:'🪞',meaning:'Reflektiraj na prošlu sedmicu. Šta bi drugačije?',color:'#8b5cf6'},
  {id:24,name:'The Bridge',emoji:'🌉',meaning:'Poveži ljude. Tvoja mreža je tvoja snaga.',color:'#0891b2'},
  {id:25,name:'The Sprint',emoji:'⚡',meaning:'Fokusiraj se na jedan zadatak. Multitasking ubija produktivnost.',color:'#facc15'},
  {id:26,name:'The Marathon',emoji:'🏃',meaning:'Ovo je maraton, ne sprint. Strpljivost donosi nagradu.',color:'#22c55e'},
  {id:27,name:'The Gift',emoji:'🎁',meaning:'Pošalji zahvalnicu starom klijentu. Iznenadi ih.',color:'#e11d48'},
  {id:28,name:'The Mirror II',emoji:'☀️',meaning:'Tvoj stav definira tvoj dan. Budi pozitivan.',color:'#f97316'},
  {id:29,name:'The Key',emoji:'🔑',meaning:'Pronađi ključni problem klijenta. To je tvoj adut.',color:'#d97706'},
  {id:30,name:'The Sunrise',emoji:'🌅',meaning:'Novi dan, nove mogućnosti. Ostavi jučer iza sebe.',color:'#fb923c'},
  {id:31,name:'The Closer IV',emoji:'🎯',meaning:'Precizno ciljaj. Znaš što klijent treba — ponudi rješenje.',color:'#059669'},
  {id:32,name:'The Patience',emoji:'🧘',meaning:'Ne pritiskaj. Ponekad čekanje je najbolja strategija.',color:'#7c3aed'},
  {id:33,name:'The Warrior',emoji:'⚔️',meaning:'Bori se za svaki dogovor. Predanošću pobeđuješ.',color:'#dc2626'},
  {id:34,name:'The Alchemist',emoji:'⚗️',meaning:'Pretvori neuspjeh u lekciju. Svaki "ne" te jača.',color:'#0d9488'},
  {id:35,name:'The Oracle',emoji:'🔮',meaning:'Vjeruj svojoj intuiciji. Osjećaj te vodi na pravi put.',color:'#7c3aed'},
  {id:36,name:'The Champion',emoji:'🥇',meaning:'Proslavi male pobjede. One grade veliki uspjeh.',color:'#eab308'},
  {id:37,name:'The Gardener',emoji:'🌱',meaning:'Sij sjeme danas, žanjev sutra. Strpljivost u prodaji.',color:'#22c55e'},
  {id:38,name:'The Navigator',emoji:'🧭',meaning:'Postavi jasan cilj i drži se kursa. Nema skretanja.',color:'#3b82f6'},
  {id:39,name:'The Storyteller',emoji:'📖',meaning:'Ispričaj priču. Ljudi kupuju emocije, ne proizvode.',color:'#e879f9'},
  {id:40,name:'The Phoenix',emoji:'🔥',meaning:'Podigni se iz pepela. Svaki neuspjeh je novi početak.',color:'#ef4444'}
];

/* ── Theme Palettes ── */
var THEME_PALETTES={
  dark:{
    bg:'#050508',bg2:'#0a0a12',surface:'rgba(255,255,255,.03)',
    glass:'rgba(255,255,255,.04)',glassBorder:'rgba(255,255,255,.08)',
    accent:'#b9ff66',accent2:'#39ff14',accent3:'#00ff88',
    grad:'linear-gradient(135deg,#b9ff66,#39ff14)',
    text:'#e8e8f0',text2:'#8888a0',text3:'#555570',
    danger:'#ff3e6c',warn:'#fbbf24',info:'#38bdf8',success:'#34d399'
  },
  light:{
    bg:'#f5f5f7',bg2:'#ececec',surface:'rgba(0,0,0,.03)',
    glass:'rgba(255,255,255,.7)',glassBorder:'rgba(0,0,0,.08)',
    accent:'#16a34a',accent2:'#15803d',accent3:'#166534',
    grad:'linear-gradient(135deg,#16a34a,#15803d)',
    text:'#1a1a2e',text2:'#555',text3:'#999',
    danger:'#dc2626',warn:'#d97706',info:'#2563eb',success:'#16a34a'
  },
  ocean:{
    bg:'#031b26',bg2:'#062a3e',surface:'rgba(255,255,255,.03)',
    glass:'rgba(255,255,255,.04)',glassBorder:'rgba(56,189,248,.12)',
    accent:'#38bdf8',accent2:'#0ea5e9',accent3:'#06b6d4',
    grad:'linear-gradient(135deg,#38bdf8,#06b6d4)',
    text:'#e0f2fe',text2:'#7dd3fc',text3:'#38bdf8',
    danger:'#f43f5e',warn:'#fbbf24',info:'#38bdf8',success:'#34d399'
  },
  sunset:{
    bg:'#1a0a05',bg2:'#2d1510',surface:'rgba(255,255,255,.03)',
    glass:'rgba(255,255,255,.04)',glassBorder:'rgba(251,146,60,.12)',
    accent:'#f97316',accent2:'#ea580c',accent3:'#fb923c',
    grad:'linear-gradient(135deg,#f97316,#f59e0b)',
    text:'#fef3c7',text2:'#fdba74',text3:'#f97316',
    danger:'#ef4444',warn:'#eab308',info:'#38bdf8',success:'#34d399'
  },
  neon:{
    bg:'#020c0b',bg2:'#041a18',surface:'rgba(57,255,20,.02)',
    glass:'rgba(57,255,20,.03)',glassBorder:'rgba(57,255,20,.1)',
    accent:'#39ff14',accent2:'#22c55e',accent3:'#4ade80',
    grad:'linear-gradient(135deg,#39ff14,#22c55e)',
    text:'#dcfce7',text2:'#86efac',text3:'#22c55e',
    danger:'#ef4444',warn:'#fbbf24',info:'#38bdf8',success:'#39ff14'
  },
  purple:{
    bg:'#0a0514',bg2:'#130a24',surface:'rgba(139,92,246,.03)',
    glass:'rgba(139,92,246,.04)',glassBorder:'rgba(139,92,246,.12)',
    accent:'#a78bfa',accent2:'#8b5cf6',accent3:'#c4b5fd',
    grad:'linear-gradient(135deg,#8b5cf6,#a78bfa)',
    text:'#ede9fe',text2:'#c4b5fd',text3:'#8b5cf6',
    danger:'#f43f5e',warn:'#fbbf24',info:'#38bdf8',success:'#34d399'
  }
};
