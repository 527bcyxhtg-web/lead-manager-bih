#!/usr/bin/env python3
"""Generate the Lead Manager awwwards-level HTML file."""

html = r'''<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lead Manager BiH — Premium Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#050508;--surface:rgba(255,255,255,.04);--glass:rgba(255,255,255,.06);
  --glass-border:rgba(255,255,255,.08);--glass-hover:rgba(255,255,255,.1);
  --accent:#7c3aed;--accent2:#06b6d4;--accent3:#f43f5e;
  --gradient:linear-gradient(135deg,#7c3aed,#06b6d4);
  --text:#f1f5f9;--text-dim:#94a3b8;--text-muted:#475569;
  --radius:16px;--radius-sm:10px;--radius-xs:6px;
  --shadow:0 8px 32px rgba(0,0,0,.4);
  --font-head:'Space Grotesk',sans-serif;--font-body:'Inter',sans-serif;
}
html{scroll-behavior:smooth;font-size:16px}
body{
  font-family:var(--font-body);background:var(--bg);color:var(--text);
  min-height:100vh;overflow-x:hidden;line-height:1.6;
}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(124,58,237,.4);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(124,58,237,.7)}

/* ===== LOADING SCREEN ===== */
#loader{
  position:fixed;inset:0;z-index:9999;
  background:var(--bg);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:2rem;
  transition:opacity .8s ease,visibility .8s ease;
}
#loader.hidden{opacity:0;visibility:hidden;pointer-events:none}
.loader-logo{width:80px;height:80px;animation:loaderSpin 2s linear infinite}
.loader-logo svg{width:100%;height:100%}
.loader-text{font-family:var(--font-head);font-size:1.2rem;font-weight:300;
  letter-spacing:.3em;text-transform:uppercase;color:var(--text-dim);
  animation:loaderPulse 1.5s ease-in-out infinite}
@keyframes loaderSpin{0%{transform:rotate(0deg) scale(1)}50%{transform:rotate(180deg) scale(1.1)}100%{transform:rotate(360deg) scale(1)}}
@keyframes loaderPulse{0%,100%{opacity:.4}50%{opacity:1}}

/* ===== HERO SECTION ===== */
.hero{
  position:relative;min-height:85vh;display:flex;align-items:center;
  justify-content:center;overflow:hidden;padding:2rem;
}
.hero-bg{position:absolute;inset:0;z-index:0}
.hero-mesh{
  position:absolute;inset:-50%;width:200%;height:200%;
  background:
    radial-gradient(ellipse at 20% 50%,rgba(124,58,237,.25) 0%,transparent 50%),
    radial-gradient(ellipse at 80% 20%,rgba(6,182,212,.2) 0%,transparent 50%),
    radial-gradient(ellipse at 50% 80%,rgba(244,63,94,.15) 0%,transparent 50%),
    radial-gradient(ellipse at 70% 60%,rgba(124,58,237,.1) 0%,transparent 40%);
  animation:meshFloat 20s ease-in-out infinite;
}
@keyframes meshFloat{0%,100%{transform:translate(0,0) rotate(0deg)}25%{transform:translate(-3%,2%) rotate(1deg)}50%{transform:translate(2%,-3%) rotate(-1deg)}75%{transform:translate(-1%,3%) rotate(.5deg)}}

.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.5;animation:orbFloat 15s ease-in-out infinite}
.orb-1{width:400px;height:400px;background:var(--accent);top:10%;left:15%;animation-delay:0s;animation-duration:18s}
.orb-2{width:300px;height:300px;background:var(--accent2);top:50%;right:10%;animation-delay:-5s;animation-duration:22s}
.orb-3{width:250px;height:250px;background:var(--accent3);bottom:10%;left:40%;animation-delay:-10s;animation-duration:16s}
.orb-4{width:200px;height:200px;background:#8b5cf6;top:30%;right:30%;animation-delay:-7s;animation-duration:20s}
@keyframes orbFloat{
  0%,100%{transform:translate(0,0) scale(1)}
  33%{transform:translate(40px,-30px) scale(1.05)}
  66%{transform:translate(-20px,40px) scale(.95)}
}

.hero-content{position:relative;z-index:1;text-align:center;max-width:900px}
.hero-badge{
  display:inline-flex;align-items:center;gap:.5rem;
  padding:.5rem 1.2rem;border-radius:100px;
  background:rgba(124,58,237,.15);border:1px solid rgba(124,58,237,.3);
  font-size:.8rem;font-weight:500;letter-spacing:.05em;
  margin-bottom:1.5rem;backdrop-filter:blur(10px);
  opacity:0;animation:fadeUp .8s ease forwards .3s;
}
.hero-badge .dot{width:6px;height:6px;border-radius:50%;background:#22c55e;animation:dotPulse 2s ease-in-out infinite}
@keyframes dotPulse{0%,100%{box-shadow:0 0 0 0 rgba(34,197,94,.4)}50%{box-shadow:0 0 0 6px rgba(34,197,94,0)}}

.hero h1{
  font-family:var(--font-head);font-size:clamp(2.5rem,6vw,5rem);
  font-weight:700;line-height:1.1;margin-bottom:1rem;
  background:linear-gradient(135deg,#f1f5f9 0%,#94a3b8 50%,#f1f5f9 100%);
  background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
  opacity:0;animation:fadeUp .8s ease forwards .5s;
}
.hero h1 .word{display:inline-block;opacity:0;transform:translateY(40px);animation:wordReveal .6s ease forwards}
.hero h1 .word:nth-child(1){animation-delay:.7s}
.hero h1 .word:nth-child(2){animation-delay:.85s}
.hero h1 .word:nth-child(3){animation-delay:1s}
.hero h1 .word:nth-child(4){animation-delay:1.15s}
@keyframes wordReveal{to{opacity:1;transform:translateY(0)}}

.hero p{
  font-size:clamp(1rem,2vw,1.3rem);color:var(--text-dim);
  max-width:600px;margin:0 auto 2rem;font-weight:300;
  opacity:0;animation:fadeUp .8s ease forwards .7s;
}
@keyframes fadeUp{to{opacity:1;transform:translateY(0)}}
.hero-content > * {transform:translateY(20px)}

/* ===== GLASS UTILITIES ===== */
.glass{
  background:var(--glass);backdrop-filter:blur(20px) saturate(1.5);
  -webkit-backdrop-filter:blur(20px) saturate(1.5);
  border:1px solid var(--glass-border);border-radius:var(--radius);
  box-shadow:var(--shadow),inset 0 1px 0 rgba(255,255,255,.05);
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.glass:hover{
  background:var(--glass-hover);border-color:rgba(255,255,255,.12);
  box-shadow:var(--shadow),0 0 30px rgba(124,58,237,.1),inset 0 1px 0 rgba(255,255,255,.08);
}

/* ===== CONTAINER ===== */
.container{max-width:1280px;margin:0 auto;padding:0 2rem}

/* ===== SECTION HEADERS ===== */
.section{padding:4rem 0}
.section-header{
  display:flex;align-items:flex-end;justify-content:space-between;
  margin-bottom:2.5rem;flex-wrap:wrap;gap:1rem;
}
.section-title{
  font-family:var(--font-head);font-size:clamp(1.5rem,3vw,2.2rem);
  font-weight:600;
}
.section-title span{
  background:var(--gradient);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;
}
.section-subtitle{color:var(--text-dim);font-size:.95rem;margin-top:.3rem}

/* ===== BENTO GRID ===== */
.bento-grid{
  display:grid;gap:1.2rem;
  grid-template-columns:repeat(4,1fr);
  grid-auto-rows:minmax(140px,auto);
}
.bento-card{padding:1.8rem;position:relative;overflow:hidden}
.bento-card::before{
  content:'';position:absolute;top:0;right:0;width:120px;height:120px;
  border-radius:50%;filter:blur(40px);opacity:.15;pointer-events:none;
  transition:opacity .4s ease;
}
.bento-card:hover::before{opacity:.25}
.bento-card:nth-child(1){grid-column:span 2;grid-row:span 2}
.bento-card:nth-child(1)::before{background:var(--accent)}
.bento-card:nth-child(2)::before{background:var(--accent2)}
.bento-card:nth-child(3)::before{background:var(--accent3)}
.bento-card:nth-child(4)::before{background:#22c55e}
.bento-card:nth-child(5)::before{background:#f59e0b}

.bento-card .stat-label{font-size:.85rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:.08em;font-weight:500}
.bento-card .stat-value{
  font-family:var(--font-head);font-size:clamp(2rem,4vw,3.2rem);
  font-weight:700;margin:.5rem 0;line-height:1;
}
.bento-card:nth-child(1) .stat-value{font-size:clamp(3rem,6vw,5rem)}
.bento-card .stat-sub{font-size:.85rem;color:var(--text-muted);margin-top:.3rem}

/* Progress Ring */
.progress-ring-wrap{position:relative;width:100px;height:100px;margin:1rem 0}
.progress-ring{transform:rotate(-90deg)}
.progress-ring circle{transition:stroke-dashoffset 1.5s cubic-bezier(.4,0,.2,1)}
.progress-ring .bg{fill:none;stroke:rgba(255,255,255,.06);stroke-width:8}
.progress-ring .fg{fill:none;stroke:url(#progressGrad);stroke-width:8;stroke-linecap:round}
.progress-ring-text{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-family:var(--font-head);font-size:1.5rem;font-weight:700;
}

/* ===== SEARCH & FILTERS ===== */
.toolbar{display:flex;flex-wrap:wrap;gap:1rem;align-items:center;margin-bottom:2rem}
.search-wrap{flex:1;min-width:280px;position:relative}
.search-wrap input{
  width:100%;padding:1rem 1.2rem 1rem 3rem;
  background:var(--glass);backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  border:1px solid var(--glass-border);border-radius:var(--radius);
  color:var(--text);font-size:1rem;font-family:var(--font-body);
  outline:none;transition:all .4s ease;
}
.search-wrap input::placeholder{color:var(--text-muted)}
.search-wrap input:focus{
  border-color:rgba(124,58,237,.5);
  box-shadow:0 0 0 4px rgba(124,58,237,.15),0 0 30px rgba(124,58,237,.1);
}
.search-wrap svg{position:absolute;left:1rem;top:50%;transform:translateY(-50%);color:var(--text-muted);width:18px;height:18px;pointer-events:none}

.filters{display:flex;flex-wrap:wrap;gap:.5rem}
.filter-pill{
  padding:.5rem 1.1rem;border-radius:100px;font-size:.85rem;font-weight:500;
  border:1px solid var(--glass-border);background:transparent;
  color:var(--text-dim);cursor:pointer;transition:all .3s ease;
  font-family:var(--font-body);user-select:none;
}
.filter-pill:hover{background:rgba(255,255,255,.06);color:var(--text)}
.filter-pill.active{
  background:linear-gradient(135deg,rgba(124,58,237,.25),rgba(6,182,212,.15));
  border-color:rgba(124,58,237,.4);color:var(--text);
  box-shadow:0 0 20px rgba(124,58,237,.15);
}
.filter-pill .count{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:20px;height:20px;border-radius:100px;
  background:rgba(255,255,255,.1);font-size:.75rem;
  padding:0 .4rem;margin-left:.4rem;
}

/* ===== ACTION BUTTONS ===== */
.actions{display:flex;gap:.6rem;flex-wrap:wrap}
.btn{
  padding:.6rem 1.2rem;border-radius:var(--radius-sm);font-size:.85rem;
  font-weight:500;cursor:pointer;border:none;font-family:var(--font-body);
  transition:all .3s cubic-bezier(.4,0,.2,1);display:inline-flex;
  align-items:center;gap:.4rem;position:relative;overflow:hidden;
}
.btn-primary{
  background:linear-gradient(135deg,var(--accent),#6d28d9);color:white;
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 4px 20px rgba(124,58,237,.4)}
.btn-ghost{
  background:transparent;border:1px solid var(--glass-border);color:var(--text-dim);
}
.btn-ghost:hover{background:rgba(255,255,255,.06);color:var(--text);border-color:rgba(255,255,255,.15)}
.btn-danger{background:rgba(244,63,94,.1);border:1px solid rgba(244,63,94,.2);color:var(--accent3)}
.btn-danger:hover{background:rgba(244,63,94,.2);transform:translateY(-2px)}

/* Ripple */
.btn::after{
  content:'';position:absolute;inset:0;
  background:radial-gradient(circle at var(--x,50%) var(--y,50%),rgba(255,255,255,.3),transparent 60%);
  opacity:0;transition:opacity .4s ease;
}
.btn:active::after{opacity:1;transition:opacity .1s ease}

/* ===== CONTACT CARDS ===== */
.cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1.2rem}
.card{
  padding:0;border-radius:var(--radius);overflow:hidden;
  background:var(--glass);backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  border:1px solid var(--glass-border);
  box-shadow:var(--shadow),inset 0 1px 0 rgba(255,255,255,.05);
  transition:all .4s cubic-bezier(.4,0,.2,1);
  transform:translateY(30px);opacity:0;
}
.card.visible{transform:translateY(0);opacity:1}
.card:hover{
  transform:translateY(-6px);border-color:rgba(124,58,237,.3);
  box-shadow:var(--shadow),0 0 40px rgba(124,58,237,.12),inset 0 1px 0 rgba(255,255,255,.08);
}
.card-header{padding:1.3rem 1.3rem 0;display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem}
.card-name{
  font-family:var(--font-head);font-size:1.05rem;font-weight:600;
  line-height:1.3;flex:1;
}
.card-name small{display:block;font-family:var(--font-body);font-weight:400;font-size:.8rem;color:var(--text-dim);margin-top:.15rem}

.card-status-badge{
  flex-shrink:0;padding:.25rem .7rem;border-radius:100px;
  font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;
  display:flex;align-items:center;gap:.35rem;white-space:nowrap;
}
.card-status-badge .pulse{
  width:6px;height:6px;border-radius:50%;position:relative;
}
.card-status-badge .pulse::after{
  content:'';position:absolute;inset:-3px;border-radius:50%;
  animation:statusPulse 2s ease-in-out infinite;
}
@keyframes statusPulse{0%,100%{box-shadow:0 0 0 0 currentColor;opacity:.6}50%{box-shadow:0 0 0 4px currentColor;opacity:0}}

.status-cceka{background:rgba(245,158,11,.12);color:#fbbf24}
.status-cceka .pulse{background:#fbbf24}.status-cceka .pulse::after{color:#fbbf24}
.status-utoku{background:rgba(6,182,212,.12);color:#22d3ee}
.status-utoku .pulse{background:#22d3ee}.status-utoku .pulse::after{color:#22d3ee}
.status-zavrseno{background:rgba(34,197,94,.12);color:#4ade80}
.status-zavrseno .pulse{background:#4ade80}.status-zavrseno .pulse::after{color:#4ade80}
.status-pozvani{background:rgba(124,58,237,.12);color:#a78bfa}
.status-pozvani .pulse{background:#a78bfa}.status-pozvani .pulse::after{color:#a78bfa}

.card-body{padding:1rem 1.3rem}
.card-meta{display:flex;flex-direction:column;gap:.4rem;margin-bottom:.8rem}
.card-meta-row{display:flex;align-items:center;gap:.5rem;font-size:.85rem;color:var(--text-dim)}
.card-meta-row svg{width:14px;height:14px;flex-shrink:0;opacity:.6}
.card-meta-row a{color:var(--accent2);text-decoration:none;transition:color .2s}
.card-meta-row a:hover{color:#22d3ee}

.card-tags{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.8rem}
.card-tag{
  padding:.2rem .55rem;border-radius:var(--radius-xs);font-size:.7rem;
  background:rgba(255,255,255,.05);color:var(--text-muted);
  border:1px solid rgba(255,255,255,.05);
}

.card-notes-toggle{
  display:flex;align-items:center;gap:.3rem;font-size:.8rem;
  color:var(--text-muted);cursor:pointer;padding:.3rem 0;
  transition:color .2s;background:none;border:none;font-family:var(--font-body);
}
.card-notes-toggle:hover{color:var(--text-dim)}
.card-notes-toggle svg{width:12px;height:12px;transition:transform .3s ease}
.card-notes-toggle.open svg{transform:rotate(180deg)}

.card-notes{
  max-height:0;overflow:hidden;transition:max-height .4s cubic-bezier(.4,0,.2,1);
}
.card-notes.open{max-height:200px}
.card-notes textarea{
  width:100%;padding:.6rem;border-radius:var(--radius-xs);
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);
  color:var(--text);font-size:.85rem;font-family:var(--font-body);
  resize:vertical;min-height:60px;outline:none;transition:border-color .2s;
  margin-top:.5rem;line-height:1.5;
}
.card-notes textarea:focus{border-color:rgba(124,58,237,.3)}
.card-notes textarea::placeholder{color:var(--text-muted)}

.card-footer{padding:0 1.3rem 1.3rem;display:flex;gap:.4rem;flex-wrap:wrap}
.card-footer .btn{padding:.4rem .8rem;font-size:.78rem}

/* ===== TOAST ===== */
.toast-container{
  position:fixed;bottom:2rem;right:2rem;z-index:10000;
  display:flex;flex-direction:column;gap:.6rem;
}
.toast{
  padding:.8rem 1.2rem;border-radius:var(--radius-sm);
  background:rgba(15,15,25,.95);backdrop-filter:blur(20px);
  border:1px solid rgba(255,255,255,.1);color:var(--text);
  font-size:.85rem;transform:translateX(120%);transition:transform .4s cubic-bezier(.4,0,.2,1);
  display:flex;align-items:center;gap:.5rem;
  box-shadow:0 8px 30px rgba(0,0,0,.5);
}
.toast.show{transform:translateX(0)}
.toast.success{border-color:rgba(34,197,94,.3)}
.toast.info{border-color:rgba(6,182,212,.3)}
.toast.warn{border-color:rgba(245,158,11,.3)}
.toast.error{border-color:rgba(244,63,94,.3)}

/* ===== EMPTY STATE ===== */
.empty-state{
  text-align:center;padding:4rem 2rem;color:var(--text-muted);
  grid-column:1/-1;
}
.empty-state svg{width:64px;height:64px;opacity:.3;margin-bottom:1rem}
.empty-state p{font-size:1.1rem}

/* ===== SCROLL ANIMATIONS ===== */
.reveal{opacity:0;transform:translateY(30px);transition:all .7s cubic-bezier(.4,0,.2,1)}
.reveal.visible{opacity:1;transform:translateY(0)}
.reveal-delay-1{transition-delay:.1s}.reveal-delay-2{transition-delay:.2s}
.reveal-delay-3{transition-delay:.3s}.reveal-delay-4{transition-delay:.4s}
.reveal-delay-5{transition-delay:.5s}

/* ===== RESPONSIVE ===== */
@media(max-width:1024px){
  .bento-grid{grid-template-columns:repeat(2,1fr)}
  .bento-card:nth-child(1){grid-column:span 2;grid-row:span 1}
}
@media(max-width:640px){
  .bento-grid{grid-template-columns:1fr}
  .bento-card:nth-child(1){grid-column:span 1}
  .cards-grid{grid-template-columns:1fr}
  .hero{min-height:70vh}
  .container{padding:0 1rem}
  .section{padding:2.5rem 0}
}

/* ===== FOOTER ===== */
.footer{
  text-align:center;padding:3rem 0;color:var(--text-muted);
  font-size:.8rem;border-top:1px solid rgba(255,255,255,.04);
  margin-top:2rem;
}
.footer span{color:var(--accent)}
</style>
</head>
<body>

<!-- ===== LOADER ===== -->
<div id="loader">
  <div class="loader-logo">
    <svg viewBox="0 0 80 80" fill="none">
      <defs>
        <linearGradient id="loaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#7c3aed"/>
          <stop offset="100%" stop-color="#06b6d4"/>
        </linearGradient>
      </defs>
      <rect x="8" y="8" width="64" height="64" rx="16" fill="none" stroke="url(#loaderGrad)" stroke-width="3" stroke-dasharray="12 6">
        <animateTransform attributeName="transform" type="rotate" values="0 40 40;360 40 40" dur="4s" repeatCount="indefinite"/>
      </rect>
      <circle cx="40" cy="40" r="12" fill="url(#loaderGrad)" opacity=".8">
        <animate attributeName="r" values="12;16;12" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values=".8;.4;.8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="40" cy="40" r="6" fill="white" opacity=".9"/>
    </svg>
  </div>
  <div class="loader-text">Lead Manager BiH</div>
</div>

<!-- ===== HERO ===== -->
<section class="hero" id="hero">
  <div class="hero-bg">
    <div class="hero-mesh"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="orb orb-4"></div>
  </div>
  <div class="hero-content">
    <div class="hero-badge"><span class="dot"></span> BiH Lead Dashboard</div>
    <h1><span class="word">Lead</span> <span class="word">Manager</span> <span class="word">Bosna</span> <span class="word">&amp; Hercegovina</span></h1>
    <p>Upravljajte svojim poslovnim kontaktima širom Bosne i Hercegovine. Elegantly. Efficiently.</p>
  </div>
</section>

<!-- ===== MAIN APP ===== -->
<div class="container">
  <!-- Bento Stats -->
  <section class="section" id="statsSection">
    <div class="section-header reveal">
      <div>
        <div class="section-title">Pregled <span>Podataka</span></div>
        <div class="section-subtitle">Statistike vaših kontakata u realnom vremenu</div>
      </div>
    </div>
    <div class="bento-grid" id="bentoGrid">
      <!-- Bento 1: Total (large) -->
      <div class="bento-card glass reveal reveal-delay-1">
        <div class="stat-label">Ukupno Kontakata</div>
        <div class="stat-value" id="statTotal">0</div>
        <div class="stat-sub">Poslovnih kontakata u BiH</div>
      </div>
      <!-- Bento 2: Progress Ring -->
      <div class="bento-card glass reveal reveal-delay-2" style="grid-row:span 2;display:flex;flex-direction:column;align-items:center;justify-content:center">
        <div class="stat-label">Obrada</div>
        <div class="progress-ring-wrap">
          <svg class="progress-ring" width="100" height="100">
            <defs>
              <linearGradient id="progressGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#7c3aed"/>
                <stop offset="100%" stop-color="#06b6d4"/>
              </linearGradient>
            </defs>
            <circle class="bg" cx="50" cy="50" r="42"/>
            <circle class="fg" id="progressCircle" cx="50" cy="50" r="42"
              stroke-dasharray="263.89" stroke-dashoffset="263.89"/>
          </svg>
          <div class="progress-ring-text" id="progressText">0%</div>
        </div>
        <div class="stat-sub">Završeno / Ukupno</div>
      </div>
      <!-- Bento 3: Čeka -->
      <div class="bento-card glass reveal reveal-delay-2">
        <div class="stat-label">Čeka</div>
        <div class="stat-value" id="statCeka" style="color:#fbbf24">0</div>
        <div class="stat-sub">Na obradu</div>
      </div>
      <!-- Bento 4: U toku -->
      <div class="bento-card glass reveal reveal-delay-3">
        <div class="stat-label">U Toku</div>
        <div class="stat-value" id="statToku" style="color:#22d3ee">0</div>
        <div class="stat-sub">Aktivni proces</div>
      </div>
      <!-- Bento 5: Završeno -->
      <div class="bento-card glass reveal reveal-delay-4" style="grid-column:span 2">
        <div class="stat-label">Završeno</div>
        <div class="stat-value" id="statZavrseno" style="color:#4ade80">0</div>
        <div class="stat-sub">Uspješno obrađeno</div>
      </div>
      <!-- Bento 6: Zvali -->
      <div class="bento-card glass reveal reveal-delay-5">
        <div class="stat-label">📞 Zvali</div>
        <div class="stat-value" id="statPozvani" style="color:#a78bfa">0</div>
        <div class="stat-sub">Kontaktirano telefonom</div>
      </div>
      <!-- Bento 7: Gradovi -->
      <div class="bento-card glass reveal reveal-delay-3">
        <div class="stat-label">Gradovi</div>
        <div class="stat-value" id="statGradovi">0</div>
        <div class="stat-sub">Jedinstvenih lokacija</div>
      </div>
      <!-- Bento 8: Kategorije -->
      <div class="bento-card glass reveal reveal-delay-4">
        <div class="stat-label">Kategorije</div>
        <div class="stat-value" id="statKategorije">0</div>
        <div class="stat-sub">Tipova biznisa</div>
      </div>
    </div>
  </section>

  <!-- Search & Filters -->
  <section class="section" id="leadsSection">
    <div class="section-header reveal">
      <div>
        <div class="section-title">Vaši <span>Kontakti</span></div>
        <div class="section-subtitle">Pretražite, filtrirajte i upravljajte svim leadovima</div>
      </div>
    </div>

    <div class="toolbar reveal reveal-delay-1">
      <div class="search-wrap">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchInput" placeholder="Pretraži po nazivu, gradu, kategoriji…">
      </div>
      <div class="filters" id="filters">
        <button class="filter-pill active" data-filter="all">Svi<span class="count" id="countAll">0</span></button>
        <button class="filter-pill" data-filter="ceka">↩️ Čeka<span class="count" id="countCeka">0