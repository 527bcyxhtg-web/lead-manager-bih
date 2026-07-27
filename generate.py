#!/usr/bin/env python3
"""Generate the Lead Manager BiH premium HTML file."""

import json, os

L=[
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
]

L_json = json.dumps(L, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lead Manager BiH — Premium CRM</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#050508;
  --surface:rgba(255,255,255,0.03);
  --glass:rgba(255,255,255,0.05);
  --border:rgba(255,255,255,0.08);
  --text:#f0f0f5;
  --text2:rgba(255,255,255,0.5);
  --accent1:#667eea;
  --accent2:#764ba2;
  --glow:rgba(102,126,234,0.4);
  --gradient:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
  --radius:20px;
  --radius-sm:12px;
  --transition:0.3s cubic-bezier(0.4,0,0.2,1);
}}
html{{scroll-behavior:smooth}}
body{{
  font-family:'Inter',sans-serif;
  background:var(--bg);
  color:var(--text);
  line-height:1.6;
  overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
}}
::-webkit-scrollbar{{width:6px}}
::-webkit-scrollbar-track{{background:var(--bg)}}
::-webkit-scrollbar-thumb{{background:linear-gradient(var(--accent1),var(--accent2));border-radius:3px}}

/* ========== LOADER ========== */
#loader{{
  position:fixed;inset:0;z-index:9999;
  background:var(--bg);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  transition:opacity 0.8s ease,visibility 0.8s ease;
}}
#loader.hide{{opacity:0;visibility:hidden;pointer-events:none}}
#loader .loader-svg{{width:80px;height:80px;animation:loaderSpin 2s linear infinite}}
#loader .loader-text{{
  margin-top:24px;font-family:'Space Grotesk',sans-serif;font-size:14px;
  letter-spacing:4px;text-transform:uppercase;color:var(--text2);
  animation:loaderPulse 1.5s ease-in-out infinite;
}}
@keyframes loaderSpin{{0%{{transform:rotate(0deg)}}100%{{transform:rotate(360deg)}}}}
@keyframes loaderPulse{{0%,100%{{opacity:.4}}50%{{opacity:1}}}}

/* ========== HERO ========== */
.hero{{
  position:relative;min-height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;overflow:hidden;
  text-align:center;padding:2rem;
}}
.orb{{
  position:absolute;border-radius:50%;
  filter:blur(120px);opacity:0.4;
  animation:orbFloat 20s ease-in-out infinite;
}}
.orb:nth-child(1){{width:500px;height:500px;background:#667eea;top:-10%;left:-5%;animation-delay:0s}}
.orb:nth-child(2){{width:400px;height:400px;background:#764ba2;bottom:-10%;right:-5%;animation-delay:-7s}}
.orb:nth-child(3){{width:350px;height:350px;background:#e040fb;top:40%;left:50%;animation-delay:-14s}}
@keyframes orbFloat{{
  0%,100%{{transform:translate(0,0) scale(1)}}
  25%{{transform:translate(60px,-40px) scale(1.1)}}
  50%{{transform:translate(-30px,50px) scale(0.95)}}
  75%{{transform:translate(40px,20px) scale(1.05)}}
}}
.hero-content{{position:relative;z-index:2}}
.hero h1{{
  font-family:'Space Grotesk',sans-serif;
  font-size:clamp(3rem,8vw,7rem);font-weight:700;
  line-height:1.05;letter-spacing:-0.03em;
  opacity:0;transform:translateY(40px);
  animation:heroReveal 1s 0.5s forwards;
}}
.hero .accent{{
  background:var(--gradient);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;
}}
.hero .subtitle{{
  font-size:clamp(1rem,2vw,1.3rem);color:var(--text2);
  margin-top:1.5rem;max-width:600px;
  opacity:0;transform:translateY(20px);
  animation:heroReveal 1s 0.8s forwards;
}}
@keyframes heroReveal{{to{{opacity:1;transform:translateY(0)}}}}
.hero .scroll-hint{{
  position:absolute;bottom:3rem;left:50%;transform:translateX(-50%);
  opacity:0;animation:heroReveal 1s 1.5s forwards,bobbing 2s ease-in-out infinite 2.5s;
}}
@keyframes bobbing{{0%,100%{{transform:translateX(-50%) translateY(0)}}50%{{transform:translateX(-50%) translateY(10px)}}}}

/* ========== STATS BENTO ========== */
.stats-bento{{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  grid-auto-rows:minmax(160px,auto);
  gap:16px;max-width:1200px;margin:0 auto;
  padding:0 2rem;
}}
.stat-card{{
  background:var(--glass);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius);
  padding:1.5rem;display:flex;flex-direction:column;justify-content:space-between;
  position:relative;overflow:hidden;
  opacity:0;transform:translateY(30px);transition:opacity 0.6s,transform 0.6s,border-color var(--transition),box-shadow var(--transition);
}}
.stat-card.visible{{opacity:1;transform:translateY(0)}}
.stat-card:hover{{border-color:rgba(102,126,234,0.3);box-shadow:0 0 40px rgba(102,126,234,0.1)}}
.stat-card.span-2{{grid-column:span 2}}
.stat-card.span-row-2{{grid-row:span 2}}
.stat-card .stat-label{{font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;color:var(--text2)}}
.stat-card .stat-value{{
  font-family:'Space Grotesk',sans-serif;font-size:2.8rem;font-weight:700;
  background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}}
.stat-card .stat-sub{{font-size:0.8rem;color:var(--text2);margin-top:4px}}

/* Progress ring */
.progress-ring-wrap{{display:flex;align-items:center;gap:1.5rem;height:100%}}
.progress-ring{{position:relative;width:100px;height:100px;flex-shrink:0}}
.progress-ring svg{{transform:rotate(-90deg)}}
.progress-ring circle{{fill:none;stroke-width:6;stroke-linecap:round}}
.progress-ring .ring-bg{{stroke:rgba(255,255,255,0.06)}}
.progress-ring .ring-fill{{
  stroke:url(#ringGrad);
  stroke-dasharray:283;stroke-dashoffset:283;
  transition:stroke-dashoffset 1.2s cubic-bezier(0.4,0,0.2,1);
}}
.progress-ring .ring-text{{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-family:'Space Grotesk',sans-serif;font-size:1.6rem;font-weight:700;
}}

/* ========== CONTROLS ========== */
.controls{{
  max-width:1200px;margin:3rem auto 2rem;padding:0 2rem;
  display:flex;flex-wrap:wrap;gap:1rem;align-items:center;
}}
#search{{
  flex:1;min-width:240px;padding:0.9rem 1.4rem;
  background:var(--glass);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius-sm);
  color:var(--text);font-size:0.95rem;font-family:'Inter',sans-serif;
  outline:none;transition:border-color var(--transition),box-shadow var(--transition);
}}
#search:focus{{border-color:var(--accent1);box-shadow:0 0 0 3px var(--glow)}}
#search::placeholder{{color:var(--text2)}}
.filter-pills{{display:flex;flex-wrap:wrap;gap:8px}}
.filter-pills button{{
  padding:0.55rem 1.1rem;border-radius:999px;border:1px solid var(--border);
  background:transparent;color:var(--text2);font-size:0.82rem;
  font-family:'Inter',sans-serif;cursor:pointer;
  transition:all var(--transition);
}}
.filter-pills button:hover{{background:var(--glass);color:var(--text)}}
.filter-pills button.active{{
  background:var(--gradient);color:#fff;border-color:transparent;
  box-shadow:0 4px 20px rgba(102,126,234,0.3);
}}
.action-buttons{{display:flex;gap:8px;margin-left:auto}}
.action-buttons button{{
  padding:0.55rem 1rem;border-radius:var(--radius-sm);
  border:1px solid var(--border);background:var(--glass);
  color:var(--text2);font-size:0.82rem;font-family:'Inter',sans-serif;
  cursor:pointer;transition:all var(--transition);backdrop-filter:blur(10px);
}}
.action-buttons button:hover{{background:rgba(102,126,234,0.15);color:var(--text);border-color:var(--accent1)}}

/* ========== CONTACTS GRID ========== */
.contacts-grid{{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));
  gap:16px;max-width:1200px;margin:0 auto;padding:0 2rem 4rem;
}}
.contact-card{{
  background:var(--glass);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius);
  padding:1.5rem;position:relative;overflow:hidden;
  transition:transform var(--transition),border-color var(--transition),box-shadow var(--transition);
  opacity:0;transform:translateY(30px);
}}
.contact-card.visible{{opacity:1;transform:translateY(0)}}
.contact-card:hover{{
  transform:translateY(-4px);
  border-color:rgba(102,126,234,0.3);
  box-shadow:0 8px 40px rgba(102,126,234,0.12);
}}
.contact-card .card-header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.8rem}}
.contact-card .company{{
  font-family:'Space Grotesk',sans-serif;font-size:1.15rem;font-weight:600;
  color:var(--text);line-height:1.3;flex:1;
}}
.contact-card .person{{font-size:0.85rem;color:var(--text2);margin-top:2px}}
.contact-card .status-dot{{
  width:10px;height:10px;border-radius:50%;flex-shrink:0;margin-top:6px;
}}
.contact-card .status-dot.ceka{{background:#f59e0b;box-shadow:0 0 8px rgba(245,158,11,0.5)}}
.contact-card .status-dot.utoku{{background:#3b82f6;box-shadow:0 0 8px rgba(59,130,246,0.5)}}
.contact-card .status-dot.zavrseno{{background:#10b981;box-shadow:0 0 8px rgba(16,185,129,0.5)}}
@keyframes dotPulse{{0%,100%{{opacity:1}}50%{{opacity:0.5}}}}
.status-dot{{animation:dotPulse 2s ease-in-out infinite}}

.card-badges{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:0.8rem}}
.badge{{
  padding:0.25rem 0.7rem;border-radius:999px;font-size:0.72rem;
  letter-spacing:0.5px;font-weight:500;
}}
.badge-city{{background:rgba(102,126,234,0.15);color:#667eea}}
.badge-cat{{background:rgba(118,75,162,0.15);color:#b07cdb}}
.badge-status{{background:rgba(255,255,255,0.06);color:var(--text2)}}

.card-contact{{display:flex;flex-direction:column;gap:6px;margin-bottom:0.8rem}}
.card-contact a,.card-contact span{{
  font-size:0.85rem;color:var(--text2);
  text-decoration:none;display:flex;align-items:center;gap:6px;
  transition:color var(--transition);
}}
.card-contact a:hover{{color:var(--accent1)}}
.card-contact .icon{{width:16px;text-align:center;flex-shrink:0}}

.card-notes{{
  max-height:0;overflow:hidden;transition:max-height 0.4s ease,margin 0.4s ease;
  margin-bottom:0;
}}
.card-notes.open{{max-height:200px;margin-bottom:0.8rem}}
.card-notes textarea{{
  width:100%;min-height:80px;padding:0.7rem;
  background:rgba(255,255,255,0.03);border:1px solid var(--border);
  border-radius:var(--radius-sm);color:var(--text);font-size:0.82rem;
  font-family:'Inter',sans-serif;resize:vertical;outline:none;
  transition:border-color var(--transition);
}}
.card-notes textarea:focus{{border-color:var(--accent1)}}

.card-actions{{display:flex;flex-wrap:wrap;gap:6px;margin-top:0.8rem}}
.card-actions button{{
  padding:0.4rem 0.75rem;border-radius:999px;border:1px solid var(--border);
  background:transparent;color:var(--text2);font-size:0.75rem;
  font-family:'Inter',sans-serif;cursor:pointer;
  transition:all var(--transition);
}}
.card-actions button:hover{{background:var(--glass);color:var(--text)}}
.card-actions button.active{{background:var(--gradient);color:#fff;border-color:transparent}}
.card-actions button.called-active{{background:rgba(245,158,11,0.2);color:#f59e0b;border-color:#f59e0b}}

.notes-toggle{{
  background:none;border:none;color:var(--text2);font-size:0.8rem;
  cursor:pointer;padding:0.3rem 0;transition:color var(--transition);
}}
.notes-toggle:hover{{color:var(--text)}}

/* ========== EMPTY STATE ========== */
.empty-state{{
  grid-column:1/-1;text-align:center;padding:4rem 2rem;
  color:var(--text2);
}}
.empty-state .empty-icon{{font-size:3rem;margin-bottom:1rem;opacity:0.4}}
.empty-state p{{font-size:1.1rem}}

/* ========== TOAST ========== */
#toast{{
  position:fixed;bottom:2rem;right:2rem;
  padding:0.9rem 1.6rem;border-radius:var(--radius-sm);
  background:rgba(16,185,129,0.15);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border:1px solid rgba(16,185,129,0.3);
  color:#10b981;font-size:0.9rem;font-weight:500;
  transform:translateY(100px);opacity:0;
  transition:all 0.4s cubic-bezier(0.4,0,0.2,1);
  z-index:1000;pointer-events:none;
}}
#toast.show{{transform:translateY(0);opacity:1}}

/* ========== REVEAL ========== */
.reveal{{opacity:0;transform:translateY(30px);transition:opacity 0.6s ease,transform 0.6s ease}}
.reveal.visible{{opacity:1;transform:translateY(0)}}

/* ========== RESPONSIVE ========== */
@media(max-width:900px){{
  .stats-bento{{grid-template-columns:repeat(2,1fr)}}
  .stat-card.span-2{{grid-column:span 2}}
}}
@media(max-width:600px){{
  .stats-bento{{grid-template-columns:1fr}}
  .stat-card.span-2{{grid-column:span 1}}
  .contacts-grid{{grid-template-columns:1fr}}
  .controls{{flex-direction:column}}
  .action-buttons{{margin-left:0;width:100%;justify-content:center}}
  .hero h1{{font-size:2.8rem}}
}}
</style>
</head>
<body>

<!-- ========== LOADER ========== -->
<div id="loader">
  <svg class="loader-svg" viewBox="0 0 80 80" fill="none">
    <defs>
      <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#667eea"/>
        <stop offset="100%" stop-color="#764ba2"/>
      </linearGradient>
    </defs>
    <polygon points="40,4 76,60 4,60" stroke="url(#lg)" stroke-width="2" fill="none"/>
    <polygon points="40,76 4,20 76,20" stroke="url(#lg)" stroke-width="2" fill="none" opacity="0.5"/>
    <circle cx="40" cy="40" r="8" fill="url(#lg)" opacity="0.8"/>
  </svg>
  <div class="loader-text">Lead Manager</div>
</div>

<!-- ========== HERO ========== -->
<section class="hero">
  <div class="orbs">
    <div class="orb"></div>
    <div class="orb"></div>
    <div class="orb"></div>
  </div>
  <div class="hero-content">
    <h1>Lead Manager<br><span class="accent">BiH</span></h1>
    <p class="subtitle">73 poslovnih kontakata iz Bosne i Hercegovine — frizerski saloni, restorani, auto servisi i mnogi drugi</p>
  </div>
  <div class="scroll-hint">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
  </div>
</section>

<!-- ========== SVG DEFS ========== -->
<svg width="0" height="0"><defs>
  