#!/usr/bin/env python3
"""Generate the Lead Manager HTML file."""
import os, json

OUTPUT = os.path.join(os.path.dirname(__file__), "index.html")

# ── Lead data ──────────────────────────────────────────────────────────
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
["","","Feel Good Fitness Studio","Tuzla","fitness studio","","feelgoodfitness875@gmail.com","Samo Facebook"],
]

l_json = json.dumps(L, ensure_ascii=False)

html = r'''<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lead Manager — BiH</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
/* ═══════════════════════════════════════════════════════════════
   CSS — Awwwards-grade dark glassmorphism theme
   ═══════════════════════════════════════════════════════════════ */
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#050508;--surface:rgba(255,255,255,.04);--glass:rgba(255,255,255,.06);
  --glass-border:rgba(255,255,255,.08);--glass-hover:rgba(255,255,255,.1);
  --accent:#7c3aed;--accent2:#a855f7;--accent3:#6366f1;
  --cyan:#22d3ee;--emerald:#34d399;--rose:#fb7185;--amber:#fbbf24;
  --text:#f0f0f5;--text2:#9ca3af;--text3:#6b7280;
  --radius:20px;--radius-sm:12px;--radius-xs:8px;
}
html{scroll-behavior:smooth;scrollbar-width:thin;scrollbar-color:rgba(124,58,237,.4) transparent}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(124,58,237,.4);border-radius:3px}
h1,h2,h3,h4,h5{font-family:'Space Grotesk',system-ui,sans-serif;font-weight:700}

/* ─── Loading Screen ────────────────────────────────────────── */
#loader{position:fixed;inset:0;z-index:9999;background:var(--bg);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:2rem;transition:opacity .8s,visibility .8s}
#loader.hide{opacity:0;visibility:hidden;pointer-events:none}
.loader-logo{width:80px;height:80px;animation:logoSpin 2s ease-in-out infinite}
@keyframes logoSpin{0%,100%{transform:scale(1) rotate(0deg)}50%{transform:scale(1.1) rotate(180deg)}}
.loader-text{font-family:'Space Grotesk';font-size:1.2rem;color:var(--text2);letter-spacing:.3em;text-transform:uppercase;animation:pulse 1.5s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:.4}50%{opacity:1}}
.loader-bar{width:200px;height:2px;background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden}
.loader-bar-inner{height:100%;width:0;background:linear-gradient(90deg,var(--accent),var(--cyan));border-radius:2px;animation:loadBar 2s ease-in-out forwards}
@keyframes loadBar{0%{width:0}100%{width:100%}}

/* ─── Cursor Glow ───────────────────────────────────────────── */
#cursorGlow{position:fixed;width:400px;height:400px;border-radius:50%;pointer-events:none;z-index:1;background:radial-gradient(circle,rgba(124,58,237,.08) 0%,transparent 70%);transform:translate(-50%,-50%);transition:left .3s ease-out,top .3s ease-out;display:none}
@media(hover:hover){#cursorGlow{display:block}}

/* ─── Hero ──────────────────────────────────────────────────── */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden}
.hero-bg{position:absolute;inset:0;background:
  radial-gradient(ellipse 80% 60% at 20% 30%,rgba(124,58,237,.2),transparent),
  radial-gradient(ellipse 60% 80% at 80% 70%,rgba(99,102,241,.15),transparent),
  radial-gradient(ellipse 50% 50% at 50% 50%,rgba(34,211,238,.05),transparent),
  var(--bg)}
.hero-orbs{position:absolute;inset:0;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.5;animation:orbFloat 20s ease-in-out infinite}
.orb:nth-child(1){width:500px;height:500px;background:rgba(124,58,237,.3);top:-10%;left:-5%;animation-duration:25s}
.orb:nth-child(2){width:400px;height:400px;background:rgba(34,211,238,.2);bottom:-10%;right:-5%;animation-duration:20s;animation-delay:-5s}
.orb:nth-child(3){width:300px;height:300px;background:rgba(168,85,247,.2);top:40%;left:60%;animation-duration:22s;animation-delay:-10s}
.orb:nth-child(4){width:250px;height:250px;background:rgba(99,102,241,.25);top:20%;right:20%;animation-duration:18s;animation-delay:-8s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}25%{transform:translate(40px,-30px) scale(1.1)}50%{transform:translate(-20px,40px) scale(.95)}75%{transform:translate(30px,20px) scale(1.05)}}
.hero-content{position:relative;z-index:2;text-align:center;padding:2rem}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;padding:.5rem 1.2rem;background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:999px;font-size:.85rem;color:var(--text2);margin-bottom:2rem;animation:fadeUp .8s ease-out}
.hero-badge .dot{width:8px;height:8px;background:var(--emerald);border-radius:50%;animation:dotPulse 2s infinite}
@keyframes dotPulse{0%,100%{box-shadow:0 0 0 0 rgba(52,211,153,.4)}50%{box-shadow:0 0 0 8px rgba(52,211,153,0)}}
.hero-title{font-size:clamp(2.5rem,6vw,5rem);line-height:1.05;margin-bottom:1.5rem}
.hero-title .word{display:inline-block;overflow:hidden;vertical-align:bottom}
.hero-title .word span{display:inline-block;animation:wordReveal .8s cubic-bezier(.16,1,.3,1) forwards;transform:translateY(110%);opacity:0}
.hero-sub{font-size:clamp(1rem,2vw,1.35rem);color:var(--text2);max-width:600px;margin:0 auto 2.5rem;animation:fadeUp .8s .6s ease-out both}
.hero-cta{display:inline-flex;align-items:center;gap:.6rem;padding:.9rem 2rem;background:linear-gradient(135deg,var(--accent),var(--accent3));border:none;border-radius:999px;font-family:'Space Grotesk';font-size:1rem;font-weight:600;color:#fff;cursor:pointer;transition:transform .3s,box-shadow .3s;animation:fadeUp .8s .8s ease-out both}
.hero-cta:hover{transform:scale(1.05);box-shadow:0 0 40px rgba(124,58,237,.4)}
@keyframes wordReveal{to{transform:translateY(0);opacity:1}}
@keyframes fadeUp{from{transform:translateY(30px);opacity:0}to{transform:translateY(0);opacity:1}}
.scroll-indicator{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);animation:bounce 2s infinite;color:var(--text3);font-size:1.5rem}
@keyframes bounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(10px)}}

/* ─── Container ─────────────────────────────────────────────── */
.container{max-width:1200px;margin:0 auto;padding:0 1.5rem}
section{padding:6rem 0}

/* ─── Bento Stats ───────────────────────────────────────────── */
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:auto auto;gap:1rem}
.bento-card{position:relative;padding:1.8rem;background:var(--glass);backdrop-filter:blur(40px) saturate(1.5);border:1px solid var(--glass-border);border-radius:var(--radius);overflow:hidden;transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,border-color .4s;opacity:0;transform:translateY(40px)}
.bento-card.visible{opacity:1;transform:translateY(0);transition:opacity .6s cubic-bezier(.16,1,.3,1),transform .6s cubic-bezier(.16,1,.3,1)}
.bento-card:hover{transform:translateY(-4px);border-color:rgba(124,58,237,.3);box-shadow:0 20px 60px rgba(124,58,237,.1)}
.bento-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(124,58,237,.05),transparent 60%);pointer-events:none}
.bento-card.span-2{grid-column:span 2}
.bento-card.span-2 .stat-num{font-size:clamp(2rem,4vw,3.5rem)}
.bento-label{font-size:.8rem;text-transform:uppercase;letter-spacing:.15em;color:var(--text3);margin-bottom:.5rem}
.bento-num{font-family:'Space Grotesk';font-size:clamp(1.8rem,3vw,2.5rem);font-weight:700;line-height:1.1}
.bento-card .stat-icon{position:absolute;top:1.5rem;right:1.5rem;width:48px;height:48px;border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:1.4rem}
.stat-icon.purple{background:rgba(124,58,237,.15);color:var(--accent2)}
.stat-icon.cyan{background:rgba(34,211,238,.15);color:var(--cyan)}
.stat-icon.emerald{background:rgba(52,211,153,.15);color:var(--emerald)}
.stat-icon.rose{background:rgba(251,113,133,.15);color:var(--rose)}
.stat-icon.amber{background:rgba(251,191,36,.15);color:var(--amber)}

/* Progress ring card */
.bento-card.progress-card{display:flex;flex-direction:row;align-items:center;gap:2rem}
.progress-ring-wrap{position:relative;flex-shrink:0}
.progress-ring-wrap svg{transform:rotate(-90deg)}
.progress-ring-bg{fill:none;stroke:rgba(255,255,255,.06);stroke-width:6}
.progress-ring-fill{fill:none;stroke:url(#ringGrad);stroke-width:6;stroke-linecap:round;transition:stroke-dashoffset 1.5s cubic-bezier(.16,1,.3,1)}
.progress-ring-text{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-size:1.4rem;font-weight:700}
.progress-info{flex:1}

/* ─── Filters / Search ──────────────────────────────────────── */
.toolbar{display:flex;flex-wrap:wrap;align-items:center;gap:1rem;padding:2rem 0}
.search-wrap{position:relative;flex:1;min-width:260px}
.search-wrap input{width:100%;padding:.9rem 1.2rem .9rem 3rem;background:var(--glass);backdrop-filter:blur(30px);border:1px solid var(--glass-border);border-radius:999px;color:var(--text);font-family:'Inter';font-size:.95rem;outline:none;transition:border-color .3s,box-shadow .3s}
.search-wrap input::placeholder{color:var(--text3)}
.search-wrap input:focus{border-color:rgba(124,58,237,.5);box-shadow:0 0 30px rgba(124,58,237,.15)}
.search-wrap .search-icon{position:absolute;left:1rem;top:50%;transform:translateY(-50%);color:var(--text3);pointer-events:none;font-size:1.1rem}
.filters{display:flex;flex-wrap:wrap;gap:.5rem}
.filter-btn{padding:.5rem 1.2rem;background:var(--glass);border:1px solid var(--glass-border);border-radius:999px;color:var(--text2);font-family:'Inter';font-size:.85rem;cursor:pointer;transition:all .3s;white-space:nowrap}
.filter-btn:hover{background:var(--glass-hover);color:var(--text)}
.filter-btn.active{background:linear-gradient(135deg,var(--accent),var(--accent3));border-color:transparent;color:#fff;box-shadow:0 4px 20px rgba(124,58,237,.3)}
.actions-bar{display:flex;flex-wrap:wrap;gap:.6rem;margin-left:auto}
.act-btn{padding:.5rem 1rem;background:var(--glass);border:1px solid var(--glass-border);border-radius:var(--radius-xs);color:var(--text2);font-family:'Inter';font-size:.82rem;cursor:pointer;transition:all .3s;display:flex;align-items:center;gap:.4rem}
.act-btn:hover{background:var(--glass-hover);color:var(--text);transform:scale(1.03)}
.act-btn.danger:hover{border-color:rgba(251,113,133,.4);color:var(--rose)}

/* ─── Contact Grid ──────────────────────────────────────────── */
.contact-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1.2rem;padding:1rem 0 4rem}
.contact-card{position:relative;padding:1.5rem;background:var(--glass);backdrop-filter:blur(40px) saturate(1.5);border:1px solid var(--glass-border);border-radius:var(--radius);transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,border-color .4s;opacity:0;transform:translateY(30px)}
.contact-card.visible{opacity:1;transform:translateY(0)}
.contact-card:hover{transform:translateY(-6px);box-shadow:0 24px 64px rgba(0,0,0,.3),0 0 0 1px rgba(124,58,237,.2);border-color:rgba(124,58,237,.25)}
.contact-card::after{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(124,58,237,.3),transparent);opacity:0;transition:opacity .4s}
.contact-card:hover::after{opacity:1}
.card-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.8rem}
.card-name{font-family:'Space Grotesk';font-size:1.1rem;font-weight:600;line-height:1.3}
.card-name small{display:block;font-family:'Inter';font-size:.78rem;font-weight:400;color:var(--text3);margin-top:.15rem}
.card-status-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;margin-top:.3rem;transition:background .3s}
.card-status-dot.ceka{background:var(--amber)}
.card-status-dot.toku{background:var(--cyan);animation:dotPulse 2s infinite}
.card-status-dot.zavrseno{background:var(--emerald)}
.card-meta{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem}
.card-meta span{font-size:.82rem;color:var(--text2);display:flex;align-items:center;gap:.5rem}
.card-meta span .ci{width:16px;text-align:center;flex-shrink:0;opacity:.6}
.card-tags{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1rem}
.tag{padding:.2rem .6rem;background:rgba(124,58,237,.1);border:1px solid rgba(124,58,237,.15);border-radius:999px;font-size:.72rem;color:var(--accent2);white-space:nowrap}
.tag.city{background:rgba(34,211,238,.08);border-color:rgba(34,211,238,.15);color:var(--cyan)}
.card-actions{display:flex;gap:.4rem;flex-wrap:wrap}
.card-btn{padding:.4rem .7rem;background:var(--surface);border:1px solid var(--glass-border);border-radius:var(--radius-xs);color:var(--text2