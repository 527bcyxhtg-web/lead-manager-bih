var DB='lf_v2';
var USERS=[
  {id:'natasad',name:'Nataša Damnjanović',country:'ba',role:'Agent — Bosna',pass:'natasA123',color:'#fbbf24',initials:'ND'},
  {id:'mariob',name:'Mario Beara',country:'hr',role:'Agent — Hrvatska',pass:'mariO123',color:'#38bdf8',initials:'MB'},
  {id:'aleksav',name:'Aleksa Vukićević',country:'rs',role:'Agent — Srbija',pass:'aleksa123',color:'#f472b6',initials:'AV'},
  {id:'admin',name:'Admin',country:'all',role:'Administrator',pass:'admin123',color:'#b9ff66',initials:'AD'}
];
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
  SEED_BA.forEach(function(r,i){a['ba_natasad_'+i]={owner:'natasad',country:'ba',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:''}});
  SEED_HR.forEach(function(r,i){a['hr_mariob_'+i]={owner:'mariob',country:'hr',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:''}});
  SEED_RS.forEach(function(r,i){a['rs_aleksav_'+i]={owner:'aleksav',country:'rs',first:r[0]||'',last:r[1]||'',company:r[2],city:r[3],cat:r[4],phone:r[5],email:r[6],notes:r[7]||'',status:'pending',called:false,customNotes:''}});
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
