#!/usr/bin/env python3
"""Generate the premium Lead Manager HTML file."""

import json, os

# ── Lead Data ──────────────────────────────────────────────────────────
L = [
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

# Convert to JSON for embedding
data_json = json.dumps(L, ensure_ascii=False, separators=(',',':'))

print(f"Total contacts: {len(L)}")
print(f"Data JSON length: {len(data_json)} chars")
print("Generating HTML...")

# ── Build the complete HTML ────────────────────────────────────────────

html = f'''<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lead Manager — BiH Premium Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#050508;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);
  --border-glow:rgba(120,90,255,.35);
  --accent:#7c5aff;
  --accent2:#b44aff;
  --accent3:#4a9eff;
  --text:#e8e8f0;
  --text-dim:rgba(255,255,255,.5);
  --glass:rgba(255,255,255,.05);
  --glass-border:rgba(255,255,255,.1);
  --radius:20px;
  --radius-sm:12px;
}}
html{{scroll-behavior:smooth}}
body{{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);
  color:var(--text);
  overflow-x:hidden;
  min-height:100vh;
}}
h1,h2,h3,h4,h5,h6{{font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-.02em}}

/* ─── Custom Scrollbar ─── */
::-webkit-scrollbar{{width:6px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:rgba(124,90,255,.3);border-radius:3px}}
::-webkit-scrollbar-thumb:hover{{background:rgba(124,90,255,.5)}}

/* ─── Loading Screen ─── */
#loader{{
  position:fixed;inset:0;z-index:10000;
  background:var(--bg);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  transition:opacity .8s ease,visibility .8s ease;
}}
#loader.hidden{{opacity:0;visibility:hidden;pointer-events:none}}
.loader-logo{{
  width:100px;height:100px;
  animation:logoPulse 2s ease-in-out infinite;
}}
.loader-logo svg{{width:100%;height:100%}}
@keyframes logoPulse{{
  0%,100%{{transform:scale(1);filter:drop-shadow(0 0 20px rgba(124,90,255,.5))}}
  50%{{transform:scale(1.08);filter:drop-shadow(0 0 40px rgba(124,90,255,.8))}}
}}
.loader-text{{
  margin-top:24px;font-family:'Space Grotesk',sans-serif;
  font-size:1.2rem;font-weight:600;
  background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  animation:loaderFade 1.5s ease-in-out infinite;
}}
@keyframes loaderFade{{0%,100%{{opacity:.5}}50%{{opacity:1}}}}
.loader-bar{{
  width:200px;height:2px;margin-top:20px;
  background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden;
}}
.loader-bar::after{{
  content:'';display:block;width:0;height:100%;
  background:linear-gradient(90deg,var(--accent),var(--accent2));
  border-radius:2px;
  animation:loadBar 2s ease-in-out forwards;
}}
@keyframes loadBar{{0%{{width:0}}100%{{width:100%}}}}

/* ─── Hero Section ─── */
.hero{{
  position:relative;min-height:70vh;
  display:flex;align-items:center;justify-content:center;
  overflow:hidden;padding:80px 24px 60px;
}}
.hero-bg{{
  position:absolute;inset:0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 30%,rgba(124,90,255,.15),transparent),
    radial-gradient(ellipse 60% 80% at 80% 70%,rgba(74,158,255,.12),transparent),
    radial-gradient(ellipse 50% 50% at 50% 50%,rgba(180,74,255,.08),transparent);
}}
.orb{{
  position:absolute;border-radius:50%;
  filter:blur(80px);opacity:.4;
  animation:orbFloat linear infinite;
}}
.orb-1{{
  width:500px;height:500px;
  background:radial-gradient(circle,rgba(124,90,255,.5),transparent 70%);
  top:-10%;left:-5%;animation-duration:25s;
}}
.orb-2{{
  width:400px;height:400px;
  background:radial-gradient(circle,rgba(74,158,255,.4),transparent 70%);
  bottom:-10%;right:-5%;animation-duration:30s;animation-delay:-10s;
}}
.orb-3{{
  width:350px;height:350px;
  background:radial-gradient(circle,rgba(180,74,255,.35),transparent 70%);
  top:40%;left:50%;animation-duration:20s;animation-delay:-5s;
}}
@keyframes orbFloat{{
  0%{{transform:translate(0,0) scale(1)}}
  25%{{transform:translate(40px,-30px) scale(1.05)}}
  50%{{transform:translate(-20px,40px) scale(.95)}}
  75%{{transform:translate(30px,20px) scale(1.02)}}
  100%{{transform:translate(0,0) scale(1)}}
}}
.hero-content{{position:relative;z-index:2;text-align:center;max-width:900px}}
.hero-badge{{
  display:inline-flex;align-items:center;gap:8px;
  padding:8px 20px;border-radius:100px;
  background:var(--glass);border:1px solid var(--glass-border);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  font-size:.85rem;color:var(--text-dim);margin-bottom:32px;
  animation:fadeInUp .8s ease .3s both;
}}
.hero-badge .dot{{width:8px;height:8px;border-radius:50%;background:#4ade80;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.5;transform:scale(1.3)}}}}
.hero-title{{
  font-size:clamp(2.8rem,6vw,5rem);
  line-height:1.05;margin-bottom:24px;
}}
.hero-title .word{{
  display:inline-block;
  opacity:0;transform:translateY(40px) rotateX(40deg);
  animation:wordReveal .6s ease forwards;
}}
@keyframes wordReveal{{
  to{{opacity:1;transform:translateY(0) rotateX(0)}}
}}
.hero-title .gradient-text{{
  background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.hero-sub{{
  font-size:clamp(1rem,2vw,1.25rem);
  color:var(--text-dim);max-width:600px;margin:0 auto;
  animation:fadeInUp .8s ease .6s both;line-height:1.6;
}}
@keyframes fadeInUp{{
  from{{opacity:0;transform:translateY(30px)}}
  to{{opacity:1;transform:translateY(0)}}
}}

/* ─── Bento Stats Grid ─── */
.stats-section{{padding:0 24px 60px;max-width:1200px;margin:0 auto}}
.bento-grid{{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  grid-template-rows:auto auto;
  gap:16px;
}}
.bento-card{{
  background:var(--glass);
  border:1px solid var(--glass-border);
  border-radius:var(--radius);
  padding:28px;
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  position:relative;overflow:hidden;
  transition:transform .4s ease,border-color .4s ease,box-shadow .4s ease;
  opacity:0;transform:translateY(40px);
}}
.bento-card.visible{{opacity:1;transform:translateY(0);transition:opacity .6s ease,transform .6s ease}}
.bento-card::before{{
  content:'';position:absolute;inset:-1px;
  border-radius:var(--radius);
  background:linear-gradient(135deg,rgba(124,90,255,.1),transparent,rgba(74,158,255,.1));
  opacity:0;transition:opacity .4s ease;z-index:0;pointer-events:none;
}}
.bento-card:hover::before{{opacity:1}}
.bento-card:hover{{
  transform:translateY(-4px);
  border-color:var(--border-glow);
  box-shadow:0 8px 40px rgba(124,90,255,.15);
}}
.bento-card>*{{position:relative;z-index:1}}
.bento-card.span-2{{grid-column:span 2}}
.bento-card.span-3{{grid-column:span 3}}
.bento-card.tall{{grid-row:span 2}}
.bento-icon{{
  width:48px;height:48px;border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.4rem;margin-bottom:16px;
  background:linear-gradient(135deg,rgba(124,90,255,.15),rgba(74,158,255,.1));
  border:1px solid rgba(124,90,255,.2);
}}
.bento-value{{
  font-family:'Space Grotesk',sans-serif;
  font-size:2.8rem;font-weight:700;line-height:1;
  background:linear-gradient(135deg,var(--text),rgba(255,255,255,.7));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.bento-label{{
  font-size:.85rem;color:var(--text-dim);margin-top:8px;
  text-transform:uppercase;letter-spacing:.08em;font-weight:500;
}}
.bento-progress-ring{{margin:16px auto 0;display:block}}

/* ─── Glass Panel ─── */
.glass-panel{{
  background:var(--glass);
  border:1px solid var(--glass-border);
  border-radius:var(--radius);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  padding:24px;
}}

/* ─── Search & Filters ─── */
.controls-section{{
  max-width:1200px;margin:0 auto 40px;padding:0 24px;
  opacity:0;transform:translateY(30px);
}}
.controls-section.visible{{opacity:1;transform:translateY(0);transition:opacity .6s ease,transform .6s ease}}
.search-wrap{{position:relative;margin-bottom:16px}}
.search-wrap svg{{
  position:absolute;left:20px;top:50%;transform:translateY(-50%);
  width:20px;height:20px;color:var(--text-dim);
  transition:color .3s ease;
}}
.search-input{{
  width:100%;padding:16px 20px 16px 52px;
  background:var(--glass);
  border:1px solid var(--glass-border);
  border-radius:16px;color:var(--text);
  font-family:'Inter',sans-serif;font-size:1rem;
  outline:none;transition:border-color .3s ease,box-shadow .3s ease;
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
}}
.search-input::placeholder{{color:var(--text-dim)}}
.search-input:focus{{
  border-color:var(--accent);
  box-shadow:0 0 0 3px rgba(124,90,255,.15),0 0 30px rgba(124,90,255,.1);
}}
.search-input:focus ~ svg{{color:var(--accent)}}
.filter-pills{{
  display:flex;flex-wrap:wrap;gap:8px;
}}
.pill{{
  padding:10px 20px;border-radius:100px;
  border:1px solid var(--glass-border);
  background:var(--glass);
  color:var(--text-dim);cursor:pointer;
  font-size:.88rem;font-weight:500;
  transition:all .3s ease;
  user-select:none;
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
}}
.pill:hover{{border-color:rgba(124,90,255,.3);color:var(--text);background:rgba(124,90,255,.08)}}
.pill.active{{
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff;border-color:transparent;
  box-shadow:0 4px 20px rgba(124,90,255,.3);
}}
.pill .count{{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:22px;height:22px;border-radius:11px;
  padding:0 6px;margin-left:6px;
  background:rgba(255,255,255,.15);font-size:.78rem;
}}
.pill.active .count{{background:rgba(255,255,255,.25)}}

/* ─── Action Bar ─── */
.action-bar{{
  display:flex;align-items:center;justify-content:space-between;
  flex-wrap:wrap;gap:12px;margin-top:16px;
}}
.result-count{{
  font-size:.9rem;color:var(--text-dim);
}}
.result-count strong{{color:var(--text);font-weight:600}}
.action-btns{{display:flex;gap:8px;flex-wrap:wrap}}
.btn{{
  display:inline-flex;align-items:center;gap:6px;
  padding:10px 18px;border-radius:12px;
  border:1px solid var(--glass-border);
  background:var(--glass);
  color:var(--text-dim);cursor:pointer;
  font-size:.85rem;font-weight:500;
  font-family:'Inter',sans-serif;
  transition:all .3s ease;
}}
.btn:hover{{
  border-color:rgba(124,90,255,.4);
  color:var(--text);
  background:rgba(124,90,255,.08);
  transform:translateY(-1px);
}}
.btn-danger:hover{{
  border-color:rgba(255,80,80,.4);
  background:rgba(255,80,80,.08);
  color:#ff6b6b;
}}
.btn-export{{
  background:linear-gradient(135deg,rgba(124,90,255,.12),rgba(74,158,255,.08));
  border-color:rgba(124,90,255,.25);
}}

/* ─── Contact Cards ─── */
.contacts-grid{{
  max-width:1200px;margin:0 auto;padding:0 24px 80px;
  display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));
  gap:16px;
}}
.contact-card{{
  background:var(--glass);
  border:1px solid var(--glass-border);
  border-radius:var(--radius);
  padding:0;
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  transition:transform .4s ease,border-color .4s ease,box-shadow .4s ease;
  overflow:hidden;
  opacity:0;transform:translateY(40px);
}}
.contact-card.visible{{
  opacity:1;transform:translateY(0);
  transition:opacity .5s ease,transform .5s ease,border-color .4s ease,box-shadow .4s ease;
}}
.contact-card:hover{{
  transform:translateY(-6px);
  border-color:var(--border-glow);
  box-shadow:0 12px 48px rgba(124,90,255,.12),0 0 0 1px rgba(124,90,255,.08);
}}
.card-top{{
  padding:24px 24px 0;
  display:flex;align-items:flex-start;justify-content:space-between;
}}
.card-avatar{{
  width:48px;height:48px;border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.1rem;
  color:#fff;flex-shrink:0;
}}
.card-status-badge{{
  display:flex;align-items:center;gap:6px;
  padding:6px 14px;border-radius:100px;
  font-size:.78rem;font-weight:600;
  border:1px solid;
}}
.card-status-badge.waiting{{background:rgba(251,191,36,.08);border-color:rgba(251,191,36,.25);color:#fbbf24}}
.card-status-badge.in-progress{{background:rgba(59,130,246,.08);border-color:rgba(59,130,246,.25);color:#3b82f6}}
.card-status-badge.done{{background:rgba(52,211,153,.08);border-color:rgba(52,211,153,.25);color:#34d399}}
.status-dot{{
  width:7px;height:7px;border-radius:50%;flex-shrink:0;
}}
.status-dot.waiting{{background:#fbbf24;animation:pulse 2s infinite}}
.status-dot.in-progress{{background:#3b82f6;animation:pulse 1.5s infinite}}
.status-dot.done{{background:#34d399}}
.card-body{{padding:16px 24px}}
.card-company{{
  font-family:'Space Grotesk',sans-serif;
  font-size:1.1rem;font-weight:600;line-height:1.3;
  margin-bottom:4px;
}}
.card-person{{font-size:.85rem;color:var(--text-dim);margin-bottom:12px}}
.card-meta{{
  display:flex;flex-direction:column;gap:6px;
  font-size:.83rem;color:var(--text