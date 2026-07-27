#!/usr/bin/env python3
"""Generate the Lead Manager HTML file."""
import os

OUT = "/Users/maki/.qwenpaw/workspaces/cloud-orchestrator/lead-manager-repo/index.html"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ── The full L data array as a JS string ──
L_JS = '''const L=[
["Almir","Alibegović","Frizerski salon A.A. Alibegović","Sarajevo","frizerski salon","+387 33 537 539","","Nema web — listing na bascarsija.ba"],
["Amela","Husić","Frizerski salon Amela s.z.r.","Sarajevo","frizerski salon","+387 62 583 854","","Baščaršija — nema web stranicu"],
["","","Beauty Salon Na-Na","Sarajevo","kozmetički salon","+387 61 666 002","info@na-na.ba","Stupska 19-B2"],
["","","Beauty First Salon & Spa d.o.o.","Sarajevo","kozmetički salon","+387 33 977 913","","Ilidža — nema web stranicu"],
["","","Ženski frizerski salon KIM","Sarajevo","frizerski salon","+387 33 667 513","","Avde Hume 21"],
["Sead","Rizvić","Restoran Sarajevo Vl Rizvić","Sarajevo","restoran","+387 61 053 678","","Restoran bez web sajta"],
["Semih","Aslan","Restoran Sofra d.o.o.","Sarajevo","restoran","+387 33 447 815","","Baščaršija 31"],
["","","Auto Servis Team","Sarajevo","auto servis","+387 61 552 168","","Samo Facebook stranica"],
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
["","","Motorex P.J. Bihać 1","Bihać","auto dijelovi","+387 37 351 833","","37 retail objekata u BiH"],
["","","Cvjećara Vernisaž","Bihać","cvjećara","+387 62 595 946","cvjecara.vernisaz@gmail.com",""],
["","","Cvjećara S-Garden","Bihać","cvjećara","+387 63 597 585","cvjecarasgarden@gmail.com","TC Bingo Bihać"],
["Snježana","Rajković","Cvjećara Iris Bihać","Bihać","cvjećara","+387 66 955 874","",""],
["","","DELFIN Autopraona Vl. Helđić","Bihać","autopraonica","+387 61 591 903","",""],
["","","Auto Lider d.o.o.","Brčko","auto","+387 61 600 008","","Mostarska bb"],
["Adis","Selimović","Autolimar ADO","Brčko","autolimar","+387 62 180 655","","Alije Selimovića"],
["","","Autolimar i Lakirer Šiša","Brčko","autolimar","+387 61 425 314","","Samo Facebook"],
["","","Vulkanizer Brzi Servis Marić","Grude","vulkanizer","+387 63 326 099","","Pokraj puta Imotski-Grude"],
["","","COKUL COMMERCE d.o.o.","Grude","vulkanizer","+387 39 661 601","",""],
["","","Foto Studio Franjić","Novi Travnik","photo studio","+387 30 791 536","foto.franjic@gmail.com",""],
["","","Studio Level","Novi Travnik","photo studio","+387 63 595 500","info@studio-level.com","72290 Novi Travnik"],
["","","Foto-Video Studio Home","Novi Travnik","photo studio","+387 62 33","",""],
["","","Caffe Studio","Novi Travnik","caffe bar","+387 30 790 600","margetonij@gmail.com","Samo Facebook"],
["","","Pulmont d.o.o.","Zenica","građevinska firma","+387 32 402 045","","Direktor: Sabahudin Đuherić"],
["","","EN-BE Građevinski obrt","Zenica","građevinska firma","+387 61 451 939","crjasko@gmail.com","Gorica 46"],
["","","Techno Shop Zenica","Zenica","trgovina","+387 32 249 111","zenica@technoshop.ba","Kamberovića čikma bb"],
["","","Tehnomag Zenica","Zenica","trgovina","+387 32 445 740","zenica@tehnomag.com","Lanac trgovina"],
["","","ES OPTIC Visoko","Visoko","optika","+387 62 148 462","esopticvisoko@gmail.com","Musala 1"],
["","","Optika Tihić","Visoko","optika","+387 61 925 925","","Kralja Tvrtka bb"],
["","","Optika Beganović","Visoko","optika","+387 62 750 800","","Čaršijska Visoko"],
["","","BB NEW LOOK d.o.o.","Mostar","trgovina odjećom","+387 36 317 299","","Vlasnik: Boro Bandić"],
["","","ANGEL'S FASHION d.o.o.","Mostar","trgovina odjećom","+387 36 322 360","","Vlasnik: Ivana Džidić"],
["","","Moda Best d.o.o.","Mostar","trgovina odjećom","+387 36 836 257","","Vlasnik: Ivan Grgić"],
["","","FREE SHOP d.o.o.","Mostar","trgovina odjećom","+387 36 550 385","","Vlasnik: Damir Beljo"],
["","","Elko Marić d.o.o.","Mostar","električar","+387 36 558 080","elkomaric@bih.net.ba","Maršala Tita 294"],
["","","Elektro Mont Mostar","Mostar","električar","+387 36 334 334","elektro-mont@tel.net.ba","Put za Aluminij"],
["","","Intertekstil","Široki Brijeg","trgovina odjećom","+387 39 705 451","","Gojka Šuška 2A"],
["","","Boutique Markos","Široki Brijeg","trgovina odjećom","+387 39 705 743","dpenava85@gmail.com",""],
["","","SARTEKS d.o.o.","Široki Brijeg","trgovina","+387 39 701 838","sarteks1@tel.net.ba","Uzarići bb"],
["","","EUROM d.o.o.","Široki Brijeg","trgovina","+387 39 705 411","euromsb1@gmail.com","Igračke i kućanske potrepštine"],
["","","Dječiji vrtić Ljubuški","Ljubuški","dječiji vrtić","+387 39 833 261","d.vrtic.ljubuski@gmail.com","Grad Ljubuški"],
["","","Restoran Labirint","Mostar","restoran","","",""],
["","","La-Tour Agencija","Čapljina","putnička agencija","+387 63 320 325","info@la-touragency.com","Višići Čapljina"],
["","","Čapljinka Turistička org.","Čapljina","putnička agencija","+387 36 806 147","tur.org.capljina@tel.net.ba","Mate Bobana bb"],
["","","Hotel Turist '98","Jajce","hotel","+387 30 658 151","utd.turist98@tel.net.ba","Kulina bana 1"],
["","","Hotel Plivsko Jezero","Jajce","hotel","+387 30 654 090","reception@plivskojezero.com","Jajce"],
["Boban","Savić","Advokatska kancelarija Savić","Doboj","advokat","+387 66 490 494","bobansavic84@gmail.com","Svetog Save 24"],
["Irena","Puzić-Obradović","Adv. kancelarija Puzić-Obradović","Doboj","advokat","+387 53 222 030","irenapuzic@yahoo.com",""],
["","","Finel Računovodstvo i Revizija","Tuzla","računovodstvo","+387 35 262 370","info@finel.ba","Stupine B9"],
["","","Revis Računovodstvo","Tuzla","računovodstvo","+387 35 270 094","revis@revis.ba","Kazan mahala 36"],
["","","ESGfin Tuzla","Tuzla","računovodstvo","+387 61 480 834","info@esgfin.ba",""],
["","","Atria d.o.o.","Tuzla","računovodstvo","+387 61 732 398","info@atria.ba","Titanik zgrada"],
["","","Fitness Studio Fuke","Tuzla","fitness studio","+387 61 179 000","","Mije Keroševića 20"],
["","","Fitness Studio Dobar Osjećaj","Tuzla","fitness studio","+387 61 271 655","","Armije BiH 15"],
["","","Fitness & Aerobic Studio LIFE","Tuzla","fitness studio","+387 61 855 843","",""],
["","","Feel Good Fitness Studio","Tuzla","fitness studio","","feelgoodfitness875@gmail.com","Samo Facebook"]
];'''

# ── CSS ──
CSS = r'''
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

:root{
  --bg:#050508;--surface:rgba(255,255,255,0.03);--glass:rgba(255,255,255,0.05);
  --border:rgba(255,255,255,0.08);--border-hover:rgba(255,255,255,0.16);
  --text:#f0f0f5;--text2:rgba(255,255,255,0.5);--text3:rgba(255,255,255,0.3);
  --accent:#667eea;--accent2:#764ba2;--glow:rgba(102,126,234,0.4);
  --grad:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
  --radius:20px;--radius-sm:12px;
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;
  -webkit-font-smoothing:antialiased}

/* ── Scrollbar ── */
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--accent2);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--accent)}

/* ── Loader ── */
#loader{position:fixed;inset:0;z-index:9999;background:var(--bg);display:flex;
  flex-direction:column;align-items:center;justify-content:center;
  transition:opacity .6s,visibility .6s}
#loader.hidden{opacity:0;visibility:hidden;pointer-events:none}
#loader svg{width:80px;height:80px;animation:loaderSpin 2s linear infinite}
@keyframes loaderSpin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
#loader p{margin-top:24px;font-family:'Space Grotesk',sans-serif;font-size:14px;
  color:var(--text2);letter-spacing:4px;text-transform:uppercase}
.loader-ring{fill:none;stroke:url(#lg);stroke-width:2;stroke-linecap:round;
  stroke-dasharray:120;stroke-dashoffset:40}

/* ── Hero ── */
.hero{position:relative;min-height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;overflow:hidden;z-index:1}
.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.35;
  animation:orbFloat 20s ease-in-out infinite}
.orb-1{width:600px;height:600px;background:var(--accent);top:-200px;left:-100px;
  animation-delay:0s}
.orb-2{width:500px;height:500px;background:var(--accent2);bottom:-150px;right:-50px;
  animation-delay:-7s}
.orb-3{width:400px;height:400px;background:#e040fb;top:50%;left:50%;
  transform:translate(-50%,-50%);animation-delay:-14s}
@keyframes orbFloat{
  0%,100%{transform:translate(0,0) scale(1)}
  25%{transform:translate(60px,-40px) scale(1.05)}
  50%{transform:translate(-30px,60px) scale(.95)}
  75%{transform:translate(-60px,-20px) scale(1.02)}
}
.hero h1{font-family:'Space Grotesk',sans-serif;font-size:clamp(2.5rem,7vw,5.5rem);
  font-weight:700;line-height:1.1;letter-spacing:-2px;position:relative;z-index:2;
  opacity:0;transform:translateY(40px);animation:revealUp 1s .3s forwards}
.hero .accent{background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.hero-sub{font-size:clamp(1rem,2vw,1.25rem);color:var(--text2);margin-top:20px;
  max-width:600px;line-height:1.6;position:relative;z-index:2;
  opacity:0;transform:translateY(30px);animation:revealUp 1s .6s forwards}
.hero-badge{display:inline-flex;align-items:center;gap:8px;margin-top:28px;
  padding:10px 24px;border-radius:100px;background:var(--glass);
  border:1px solid var(--border);backdrop-filter:blur(20px);font-size:14px;
  color:var(--text2);opacity:0;transform:translateY(20px);
  animation:revealUp 1s .9s forwards}
.hero-badge .dot{width:8px;height:8px;border-radius:50%;background:#4ade80;
  animation:pulse 2s infinite}
.hero-scroll{position:absolute;bottom:40px;left:50%;transform:translateX(-50%);
  width:28px;height:44px;border:2px solid var(--border);border-radius:14px;
  z-index:2;opacity:0;animation:revealUp 1s 1.2s forwards}
.hero-scroll::after{content:'';position:absolute;top:6px;left:50%;
  transform:translateX(-50%);width:4px;height:10px;border-radius:2px;
  background:var(--accent);animation:scrollDot 2s infinite}
@keyframes scrollDot{0%{opacity:1;transform:translateX(-50%) translateY(0)}
  100%{opacity:0;transform:translateX(-50%) translateY(16px)}}
@keyframes revealUp{to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(74,222,128,.6)}
  50%{box-shadow:0 0 0 8px rgba(74,222,128,0)}}

/* ── Sections ── */
section{position:relative;z-index:1}
.section-title{font-family:'Space Grotesk',sans-serif;font-size:clamp(1.5rem,3vw,2rem);
  text-align:center;margin-bottom:40px;letter-spacing:-1px}
.section-title span{background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}

/* ── Stats Bento ── */
.stats-bento{padding:80px 24px;max-width:1200px;margin:0 auto;
  display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.bento-card{background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius);padding:28px;
  transition:all .4s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.bento-card::before{content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(102,126,234,0.06),transparent);
  opacity:0;transition:opacity .4s}
.bento-card:hover{border-color:var(--border-hover);transform:translateY(-2px)}
.bento-card:hover::before{opacity:1}
.bento-card.span-2{grid-column:span 2}
.bento-card.span-row{grid-row:span 2}
.bento-label{font-size:13px;color:var(--text2);margin-bottom:8px;
  text-transform:uppercase;letter-spacing:1.5px;font-weight:500}
.bento-value{font-family:'Space Grotesk',sans-serif;font-size:2.2rem;font-weight:700;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text}
.bento-value.white{-webkit-text-fill-color:var(--text)}

/* ── Progress Ring ── */
.ring-wrap{display:flex;align-items:center;gap:20px}
.ring-container{position:relative;width:100px;height:100px;flex-shrink:0}
.ring-container svg{width:100%;height:100%;transform:rotate(-90deg)}
.ring-bg{fill:none;stroke:rgba(255,255,255,0.06);stroke-width:6}
.ring-fg{fill:none;stroke:url(#ringGrad);stroke-width:6;stroke-linecap:round;
  transition:stroke-dashoffset 1.5s cubic-bezier(.4,0,.2,1)}
.ring-text{position:absolute;inset:0;display:flex;align-items:center;
  justify-content:center;font-family:'Space Grotesk',sans-serif;font-size:1.4rem;
  font-weight:700}
.ring-info{display:flex;flex-direction:column;gap:4px}
.ring-info .pct{font-family:'Space Grotesk',sans-serif;font-size:1.4rem;
  font-weight:700;color:var(--text)}
.ring-info .sub{font-size:13px;color:var(--text2)}

/* ── Controls ── */
.controls{padding:0 24px 60px;max-width:1200px;margin:0 auto;
  display:flex;flex-direction:column;gap:20px}
.search-wrap{position:relative;max-width:500px;margin:0 auto;width:100%}
.search-wrap input{width:100%;padding:16px 20px 16px 52px;border-radius:16px;
  border:1px solid var(--border);background:var(--glass);color:var(--text);
  font-size:16px;font-family:'Inter',sans-serif;outline:none;
  backdrop-filter:blur(20px);transition:all .3s}
.search-wrap input:focus{border-color:var(--accent);
  box-shadow:0 0 0 3px rgba(102,126,234,0.15),0 0 30px rgba(102,126,234,0.1)}
.search-wrap input::placeholder{color:var(--text3)}
.search-wrap svg{position:absolute;left:18px;top:50%;transform:translateY(-50%);
  width:20px;height:20px;stroke:var(--text3);fill:none;stroke-width:2;
  stroke-linecap:round;stroke-linejoin:round}

.filter-row{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.filter-pills{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.pill{padding:10px 22px;border-radius:100px;border:1px solid var(--border);
  background:transparent;color:var(--text2);font-size:14px;font-family:'Inter',sans-serif;
  cursor:pointer;transition:all .3s;white-space:nowrap}
.pill:hover{border-color:var(--accent);color:var(--text)}
.pill.active{background:var(--grad);border-color:transparent;color:#fff;
  box-shadow:0 4px 20px rgba(102,126,234,0.3)}
.action-buttons{display:flex;gap:10px;justify-content:center}
.action-btn{padding:10px 20px;border-radius:12px;border:1px solid var(--border);
  background:var(--glass);color:var(--text2);font-size:14px;cursor:pointer;
  transition:all .3s;font-family:'Inter',sans-serif;backdrop-filter:blur(10px)}
.action-btn:hover{border-color:var(--accent);color:var(--text);
  transform:scale(1.03);box-shadow:0 4px 20px rgba(102,126,234,0.15)}

/* ── Contacts Grid ── */
.contacts-grid{padding:0 24px 100px;max-width:1200px;margin:0 auto;
  display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.contact-card{background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius);padding:24px;
  transition:all .4s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;
  display:flex;flex-direction:column;gap:14px;opacity:0;transform:translateY(30px)}
.contact-card.visible{opacity:1;transform:translateY(0)}
.contact-card:hover{border-color:rgba(102,126,234,0.3);transform:translateY(-4px);
  box-shadow:0 20px 60px rgba(0,0,0,0.3),0 0 40px rgba(102,126,234,0.08)}

.card-header{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.card-company{font-family:'Space Grotesk',sans-serif;font-size:1.1rem;
  font-weight:600;line-height:1.3}
.card-person{font-size:14px;color:var(--text2)}
.card-badges{display:flex;gap:6px;flex-wrap:wrap}
.badge{display:inline-flex;align-items:center;gap:4px;padding:4px 12px;
  border-radius:100px;font-size:11px;font-weight:500;border:1px solid var(--border);
  background:rgba(255,255,255,0.04);white-space:nowrap}
.badge.city{color:#60a5fa;border-color:rgba(96,165,250,0.2)}
.badge.cat{color:#c084fc;border-color:rgba(192,132,252,0.2)}

.card-contact{display:flex;flex-direction:column;gap:6px}
.card-phone a{color:var(--text);text-decoration:none;font-weight:500;
  display:inline-flex;align-items:center;gap:6px;transition:color .2s}
.card-phone a:hover{color:var(--accent)}
.card-email{font-size:13px;color:var(--accent);text-decoration:none;word-break:break-all}
.card-email:hover{text-decoration:underline}
.card-note{font-size:13px;color:var(--text3);line-height:1.5;
  padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:var(--radius-sm);
  border:1px solid rgba(255,255,255,0.04)}

/* Status dot */
.status-row{display:flex;align-items:center;gap:10px}
.status-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;
  transition:background .3s,box-shadow .3s}
.status-dot.ceka{background:#facc15;box-shadow:0 0 12px rgba(250,204,21,0.4)}
.status-dot.utoku{background:#3b82f6;box-shadow:0 0 12px rgba(59,130,246,0.4)}
.status-dot.zavrseno{background:#22c55e;box-shadow:0 0 12px rgba(34,197,94,0.4)}
.status-text{font-size:13px;color:var(--text2);font-weight:500}

.card-actions{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto}
.card-btn{padding:6px 12px;border-radius:10px;border:1px solid var(--border);
  background:transparent;color:var(--text2);font-size:12px;cursor:pointer;
  transition:all .25s;font-family:'Inter',sans-serif}
.card-btn:hover{border-color:var(--accent);color:var(--text)}
.card-btn.active-call{background:rgba(74,222,128,0.1);border-color:rgba(74,222,128,0.3);
  color:#4ade80}
.card-btn.status-active{background:var(--grad);border-color:transparent;color:#fff}

.notes-toggle{background:none;border:none;color:var(--text3);font-size:12px;
  cursor:pointer;padding:0;transition:color .2s;font-family:'Inter',sans-serif}
.notes-toggle:hover{color:var(--text2)}
.notes-area{width:100%;min-height:0;max-height:0;overflow:hidden;border:none;
  background:rgba(255,255,255,0.02);color:var(--text);font-size:13px;
  font-family:'Inter',sans-serif;padding:0 14px;border-radius:var(--radius-sm);
  border:1px solid transparent;transition:all .3s;resize:none;line-height:1.5}
.notes-area.open{max-height:150px;padding:10px 14px;
  border-color:rgba(255,255,255,0.06);margin-top:4px}

/* ── Empty State ── */
.empty-state{grid-column:1/-1;text-align:center;padding:80px 20px;
  color:var(--text3);font-size:1.1rem}

/* ── Toast ── */
.toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%) translateY(100px);
  padding:14px 28px;border-radius:14px;background:rgba(30,30,40,0.95);
  backdrop-filter:blur(20px);border:1px solid var(--border);color:var(--text);
  font-size:14px;z-index:10000;transition:transform .4s cubic-bezier(.4,0,.2,1);
  box-shadow:0 20px 60px rgba(0,0,0,0.4)}
.toast.show{transform:translateX(-50%) translateY(0)}

/* ── Reveal animation ── */
.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s,transform .8s;
  transition-timing-function:cubic-bezier(.4,0,.2,1)}
.reveal.visible{opacity:1;transform:translateY(0)}

/* ── Responsive ── */
@media(max-width:900px){
  .stats-bento{grid-template-columns:repeat(2,1fr)}
  .bento-card.span-2{grid-column:span 2}
}
@media(max-width:600px){
  .stats-bento{grid-template-columns:1fr;gap:12px}
  .bento-card.span-2{grid-column:span 1}
  .contacts-grid{grid-template-columns:1fr}
  .hero h1{letter-spacing:-1px}
  .controls{padding:0 16px 40px}
}
'''

# ── JavaScript