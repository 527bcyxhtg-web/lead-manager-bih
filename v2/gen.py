#!/usr/bin/env python3
"""Generate style.css and app.js for LeadFlow Platform v2 upgrade."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ═══════════════════════════════════════════════════════════════
# STYLE.CSS
# ═══════════════════════════════════════════════════════════════
CSS = r'''
/* ═══════════════════════════════════════════════════════════════
   LeadFlow Platform v2 — Premium UI
   ═══════════════════════════════════════════════════════════════ */

*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}

/* ── Theme Palettes ── */
:root,[data-theme="dark"]{
  --bg:#050508;--bg2:#0a0a12;--surface:rgba(255,255,255,.03);
  --glass:rgba(255,255,255,.04);--glass-border:rgba(255,255,255,.08);
  --accent:#b9ff66;--accent2:#39ff14;--accent3:#00ff88;
  --grad:linear-gradient(135deg,#b9ff66,#39ff14);
  --text:#e8e8f0;--text2:#8888a0;--text3:#555570;
  --danger:#ff3e6c;--warn:#fbbf24;--info:#38bdf8;--success:#34d399;
  --radius:16px;--radius-sm:10px;--radius-xs:6px;
  --font-h:'Space Grotesk',system-ui,sans-serif;
  --font-b:'Inter',system-ui,sans-serif;
  --sidebar-w:320px;
}
[data-theme="light"]{
  --bg:#f5f5f7;--bg2:#ececec;--surface:rgba(0,0,0,.03);
  --glass:rgba(255,255,255,.7);--glass-border:rgba(0,0,0,.08);
  --accent:#16a34a;--accent2:#15803d;--accent3:#166534;
  --grad:linear-gradient(135deg,#16a34a,#15803d);
  --text:#1a1a2e;--text2:#555;--text3:#999;
  --danger:#dc2626;--warn:#d97706;--info:#2563eb;--success:#16a34a;
}
[data-theme="ocean"]{
  --bg:#031b26;--bg2:#062a3e;--surface:rgba(255,255,255,.03);
  --glass:rgba(255,255,255,.04);--glass-border:rgba(56,189,248,.12);
  --accent:#38bdf8;--accent2:#0ea5e9;--accent3:#06b6d4;
  --grad:linear-gradient(135deg,#38bdf8,#06b6d4);
  --text:#e0f2fe;--text2:#7dd3fc;--text3:#38bdf8;
  --danger:#f43f5e;--warn:#fbbf24;--info:#38bdf8;--success:#34d399;
}
[data-theme="sunset"]{
  --bg:#1a0a05;--bg2:#2d1510;--surface:rgba(255,255,255,.03);
  --glass:rgba(255,255,255,.04);--glass-border:rgba(251,146,60,.12);
  --accent:#f97316;--accent2:#ea580c;--accent3:#fb923c;
  --grad:linear-gradient(135deg,#f97316,#f59e0b);
  --text:#fef3c7;--text2:'#fdba74';--text3:'#f97316';
  --danger:#ef4444;--warn:#eab308;--info:#38bdf8;--success:#34d399;
}
[data-theme="neon"]{
  --bg:#020c0b;--bg2:#041a18;--surface:rgba(57,255,20,.02);
  --glass:rgba(57,255,20,.03);--glass-border:rgba(57,255,20,.1);
  --accent:#39ff14;--accent2:#22c55e;--accent3:#4ade80;
  --grad:linear-gradient(135deg,#39ff14,#22c55e);
  --text:#dcfce7;--text2:#86efac;--text3:#22c55e;
  --danger:#ef4444;--warn:#fbbf24;--info:#38bdf8;--success:#39ff14;
}
[data-theme="purple"]{
  --bg:#0a0514;--bg2:#130a24;--surface:rgba(139,92,246,.03);
  --glass:rgba(139,92,246,.04);--glass-border:rgba(139,92,246,.12);
  --accent:#a78bfa;--accent2:#8b5cf6;--accent3:#c4b5fd;
  --grad:linear-gradient(135deg,#8b5cf6,#a78bfa);
  --text:#ede9fe;--text2:#c4b5fd;--text3:#8b5cf6;
  --danger:#f43f5e;--warn:#fbbf24;--info:#38bdf8;--success:#34d399;
}

html{scroll-behavior:smooth;scrollbar-width:thin;scrollbar-color:rgba(185,255,102,.3) transparent}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(185,255,102,.2);border-radius:3px}

body{
  background:var(--bg);color:var(--text);font-family:var(--font-b);
  line-height:1.6;overflow:hidden;height:100vh;
  transition:background .3s,color .3s;
}
body *{transition:background .3s,border-color .3s,color .3s,box-shadow .3s}
a{color:var(--accent);text-decoration:none}
button{cursor:pointer;font-family:var(--font-b)}

/* ── Reduced Motion ── */
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  #particleCanvas{display:none!important}
}

/* ── Particle Canvas ── */
#particleCanvas{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.4}

/* ── Noise Overlay ── */
.noise-overlay{
  position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.03;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
  background-repeat:repeat;background-size:200px;
}

/* ═══ LOGIN ═══ */
.login-overlay{
  position:fixed;inset:0;z-index:10000;background:var(--bg);
  display:flex;align-items:center;justify-content:center;
}
.login-overlay.hidden{display:none}
.login-box{
  background:var(--glass);border:1px solid var(--glass-border);border-radius:24px;
  padding:48px 40px;backdrop-filter:blur(30px);width:100%;max-width:420px;
  text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.4);position:relative;z-index:2;
}
.login-logo{font-family:var(--font-h);font-size:2.2rem;font-weight:700;margin-bottom:4px}
.login-logo .g{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.login-sub{font-size:.85rem;color:var(--text2);margin-bottom:28px}
.login-avatars{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:24px}
.login-av{
  width:56px;height:56px;border-radius:14px;display:flex;align-items:center;justify-content:center;
  font-family:var(--font-h);font-weight:700;font-size:.85rem;cursor:pointer;
  border:2px solid transparent;transition:all .25s;position:relative;
}
.login-av:hover{transform:scale(1.08);box-shadow:0 0 20px rgba(185,255,102,.15)}
.login-av.sel{border-color:var(--accent);box-shadow:0 0 16px rgba(185,255,102,.3)}
.login-av-name{position:absolute;bottom:-18px;font-size:.6rem;color:var(--text3);white-space:nowrap}
.login-field{margin-bottom:14px;text-align:left}
.login-field label{display:block;font-size:.72rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);margin-bottom:5px}
.login-field input{
  width:100%;padding:12px 16px;border-radius:var(--radius-sm);border:1px solid var(--glass-border);
  background:rgba(255,255,255,.03);color:var(--text);font-size:.9rem;outline:none;transition:border .3s;
}
.login-field input:focus{border-color:rgba(185,255,102,.4)}
.login-field input::placeholder{color:var(--text3)}
.login-btn{
  width:100%;padding:14px;border:none;border-radius:var(--radius-sm);
  background:var(--grad);color:#000;font-weight:700;font-size:.95rem;
  transition:transform .2s,box-shadow .3s;margin-top:4px;position:relative;overflow:hidden;
}
.login-btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(185,255,102,.25)}
.login-err{color:var(--danger);font-size:.82rem;margin-top:10px;display:none}

/* ═══ APP LAYOUT ═══ */
.app-layout{display:none;height:100vh;grid-template-columns:56px 1fr var(--sidebar-w);position:relative;z-index:2}
.app-layout.active{display:grid}

/* ── Sidebar ── */
.sidebar{
  background:var(--bg2);border-right:1px solid var(--glass-border);
  display:flex;flex-direction:column;align-items:center;padding:10px 0;gap:2px;
  overflow-y:auto;z-index:10;backdrop-filter:blur(20px);
}
.sidebar-icon{
  width:40px;height:40px;border-radius:10px;border:none;background:transparent;
  color:var(--text3);font-size:1.15rem;display:flex;align-items:center;justify-content:center;
  transition:all .2s;position:relative;
}
.sidebar-icon:hover{background:rgba(255,255,255,.05);color:var(--text);transform:scale(1.1)}
.sidebar-icon.active{background:rgba(185,255,102,.12);color:var(--accent)}
.sidebar-icon.active::after{
  content:'';position:absolute;right:-6px;width:3px;height:16px;
  background:var(--accent);border-radius:2px;
}
.sidebar-sep{width:24px;height:1px;background:var(--glass-border);margin:6px 0}
.sidebar-bottom{margin-top:auto;display:flex;flex-direction:column;align-items:center;gap:2px}

.hamburger{display:none;background:none;border:none;color:var(--text);font-size:1.2rem;padding:4px 8px}

/* ── Main Area ── */
.main-area{display:flex;flex-direction:column;overflow:hidden}
.topbar{
  display:flex;align-items:center;justify-content:space-between;padding:10px 20px;
  border-bottom:1px solid var(--glass-border);background:rgba(255,255,255,.01);
  backdrop-filter:blur(20px);flex-shrink:0;z-index:5;
}
.topbar-left{display:flex;align-items:center;gap:14px}
.topbar-title{font-family:var(--font-h);font-size:1.05rem;font-weight:700}
.topbar-bc{font-size:.75rem;color:var(--text3)}
.topbar-right{display:flex;align-items:center;gap:8px}
.topbar-avatar{
  width:32px;height:32px;border-radius:8px;display:flex;align-items:center;
  justify-content:center;font-family:var(--font-h);font-weight:700;font-size:.7rem;cursor:pointer;
}
.tb-btn{
  padding:5px 12px;border-radius:7px;border:1px solid var(--glass-border);
  background:var(--glass);color:var(--text2);font-size:.75rem;transition:all .2s;
}
.tb-btn:hover{border-color:rgba(255,255,255,.12);color:var(--text);transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.2)}
.content-scroll{flex:1;overflow-y:auto;padding:20px;scroll-behavior:smooth}

/* ═══ COUNTRY TABS ═══ */
.country-tabs{display:flex;gap:6px;margin-bottom:16px;flex-wrap:wrap}
.country-tab{
  padding:7px 16px;border-radius:100px;border:1px solid var(--glass-border);
  background:var(--glass);color:var(--text2);font-size:.8rem;font-weight:600;
  cursor:pointer;transition:all .25s;display:flex;align-items:center;gap:5px;
}
.country-tab:hover{border-color:rgba(185,255,102,.2);color:var(--text);transform:translateY(-1px)}
.country-tab.active{background:rgba(185,255,102,.12);border-color:rgba(185,255,102,.3);color:var(--accent)}
.country-tab .ct{font-size:.65rem;opacity:.6;margin-left:2px}

/* ═══ TEAM GRID ═══ */
.team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-bottom:20px}
.team-card{
  background:var(--glass);border:1px solid var(--glass-border);border-radius:var(--radius-sm);
  padding:16px;cursor:pointer;transition:all .3s;position:relative;overflow:hidden;
  contain:layout style;
}
.team-card:hover{
  transform:translateY(-4px);border-color:rgba(185,255,102,.2);
  box-shadow:0 8px 32px rgba(0,0,0,.3),0 0 0 1px rgba(185,255,102,.1);
}
.team-card::before{
  content:'';position:absolute;inset:0;opacity:0;transition:opacity .3s;
  background:radial-gradient(circle at 50% 0%,rgba(185,255,102,.06),transparent 70%);
}
.team-card:hover::before{opacity:1}
.team-av{
  width:42px;height:42px;border-radius:10px;display:flex;align-items:center;
  justify-content:center;font-family:var(--font-h);font-weight:700;font-size:.85rem;margin-bottom:10px;
}
.team-name{font-family:var(--font-h);font-weight:600;font-size:.9rem;margin-bottom:2px}
.team-role{font-size:.72rem;color:var(--text2);margin-bottom:10px}
.team-stats{display:flex;gap:10px}
.team-stat{text-align:center}
.team-stat-val{font-family:var(--font-h);font-weight:700;font-size:1rem}
.team-stat-lbl{font-size:.6rem;color:var(--text3);text-transform:uppercase;letter-spacing:.04em}

/* ═══ BENTO STATS ═══ */
.bento{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px}
.bento-card{
  background:var(--glass);border:1px solid var(--glass-border);border-radius:var(--radius-xs);
  padding:14px;contain:layout style;position:relative;overflow:hidden;
}
.bento-card::after{
  content:'';position:absolute;top:-20px;right:-20px;width:60px;height:60px;
  border-radius:50%;opacity:.05;
}
.bento-card .b-icon{
  width:28px;height:28px;border-radius:7px;display:flex;align-items:center;
  justify-content:center;font-size:.8rem;margin-bottom:6px;
}
.bento-card .b-val{font-family:var(--font-h);font-size:1.3rem;font-weight:700}
.bento-card .b-lbl{font-size:.68rem;color:var(--text2)}

/* ═══ CONTACT LIST ═══ */
.contact-list{display:flex;flex-direction:column;gap:6px}
.contact-item{
  display:flex;align-items:center;gap:12px;padding:12px 14px;
  background:var(--glass);border:1px solid var(--glass-border);border-radius:var(--radius-xs);
  transition:all .25s;cursor:pointer;position:relative;overflow:hidden;
  contain:layout style;
}
.contact-item::before{
  content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  transition:background .3s;
}
.contact-item[data-status="pending"]::before{background:var(--text3)}
.contact-item[data-status="in_progress"]::before{background:var(--info)}
.contact-item[data-status="done"]::before{background:var(--success)}
.contact-item[data-status="lost"]::before{background:var(--danger)}
.contact-item:hover{
  border-color:rgba(185,255,102,.15);background:rgba(255,255,255,.06);
  transform:translateX(3px);
}
.contact-item.selected{border-color:var(--accent);background:rgba(185,255,102,.04)}
.ci-avatar{
  width:34px;height:34px;border-radius:8px;display:flex;align-items:center;
  justify-content:center;font-family:var(--font-h);font-weight:700;font-size:.7rem;flex-shrink:0;
}
.ci-info{flex:1;min-width:0}
.ci-name{font-weight:600;font-size:.84rem}
.ci-meta{font-size:.68rem;color:var(--text2);display:flex;gap:6px;align-items:center}
.ci-meta .city{color:var(--accent);opacity:.8}
.ci-actions{display:flex;gap:4px;flex-shrink:0;align-items:center}
.ci-status{
  padding:3px 8px;border-radius:100px;font-size:.62rem;font-weight:600;
  border:1px solid;flex-shrink:0;
}
.ci-status.s-pending{border-color:rgba(251,191,36,.2);color:var(--warn);background:rgba(251,191,36,.05)}
.ci-status.s-progress{border-color:rgba(56,189,248,.2);color:var(--info);background:rgba(56,189,248,.05)}
.ci-status.s-done{border-color:rgba(52,211,153,.2);color:var(--success);background:rgba(52,211,153,.05)}
.ci-status.s-lost{border-color:rgba(255,62,108,.2);color:var(--danger);background:rgba(255,62,108,.05)}

/* Quick action buttons on contact items */
.ci-quick{
  width:28px;height:28px;border-radius:6px;border:1px solid var(--glass-border);
  background:transparent;color:var(--text3);font-size:.75rem;display:flex;
  align-items:center;justify-content:center;transition:all .2s;
}
.ci-quick:hover{background:rgba(255,255,255,.08);color:var(--text);border-color:rgba(255,255,255,.15)}
.ci-quick.done-btn:hover{background:rgba(52,211,153,.1);color:var(--success);border-color:rgba(52,211,153,.3)}
.ci-quick.reset-btn:hover{background:rgba(251,191,36,.1);color:var(--warn);border-color:rgba(251,191,36,.3)}
.ci-quick.sale-yes{background:rgba(52,211,153,.1);color:var(--success);border-color:rgba(52,211,153,.2)}
.ci-quick.sale-no{background:rgba(255,62,108,.1);color:var(--danger);border-color:rgba(255,62,108,.2)}
.ci-quick.demo-on{background:rgba(56,189,248,.1);color:var(--info);border-color:rgba(56,189,248,.2)}

/* Checkmark animation */
.ci-quick .check-anim{
  display:inline-block;transform-origin:center;
}
.ci-quick .check-anim.pop{animation:checkPop .4s ease}
@keyframes checkPop{
  0%{transform:scale(0) rotate(-45deg)}
  50%{transform:scale(1.3) rotate(10deg)}
  100%{transform:scale(1) rotate(0)}
}

/* ═══ ADD FORM ═══ */
.add-form{
  background:var(--glass);border:1px solid var(--glass-border);
  border-radius:var(--radius);padding:20px;margin-bottom:16px;display:none;
}
.add-form.open{display:block;animation:fadeDown .3s ease}
@keyframes fadeDown{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.form-grid .full{grid-column:span 2}
.form-field label{display:block;font-size:.65rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);margin-bottom:3px}
.form-field input,.form-field select,.form-field textarea{
  width:100%;padding:8px 12px;border-radius:6px;border:1px solid var(--glass-border);
  background:rgba(255,255,255,.03);color:var(--text);font-size:.82rem;outline:none;
  transition:border .3s;font-family:var(--font-b);
}
.form-field input:focus,.form-field select:focus,.form-field textarea:focus{border-color:rgba(185,255,102,.4)}
.form-field textarea{height:50px;resize:none}
.form-actions{display:flex;gap:6px;margin-top:10px;justify-content:flex-end}

/* ═══ BUTTONS ═══ */
.btn-primary{
  padding:8px 18px;border:none;border-radius:7px;background:var(--grad);color:#000;
  font-weight:700;font-size:.82rem;transition:all .2s;position:relative;overflow:hidden;
}
.btn-primary:hover{box-shadow:0 4px 16px rgba(185,255,102,.2);transform:translateY(-1px)}
.btn-primary:active{transform:translateY(0);box-shadow:0 2px 8px rgba(185,255,102,.15)}
.btn-ghost{
  padding:8px 18px;border:1px solid var(--glass-border);border-radius:7px;
  background:transparent;color:var(--text2);font-size:.82rem;transition:all .2s;
}
.btn-ghost:hover{border-color:rgba(255,255,255,.15);color:var(--text);transform:translateY(-1px)}

/* Ripple Effect */
.ripple{
  position:absolute;border-radius:50%;background:rgba(255,255,255,.3);
  transform:scale(0);animation:rippleAnim .6s ease-out;pointer-events:none;
}
@keyframes rippleAnim{to{transform:scale(4);opacity:0}}

/* ═══ OVERVIEW GRID ═══ */
.overview-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px}
.overview-card{
  background:var(--glass);border:1px solid var(--glass-border);border-radius:var(--radius-sm);
  padding:18px;position:relative;overflow:hidden;contain:layout style;
}
.overview-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.overview-card.ba::before{background:linear-gradient(90deg,#fbbf24,#f59e0b)}
.overview-card.hr::before{background:linear-gradient(90deg,#38bdf8,#0ea5e9)}
.overview-card.rs::before{background:linear-gradient(90deg,#f472b6,#ec4899)}
.oc-flag{font-size:1.8rem;margin-bottom:6px}
.oc-name{font-family:var(--font-h);font-weight:700;font-size:.95rem;margin-bottom:3px}
.oc-count{font-size:.78rem;color:var(--text2);margin-bottom:10px}
.oc-teams{display:flex;flex-direction:column;gap:5px}
.oc-team{display:flex;align-items:center;justify-content:space-between;padding:5px 8px;background:rgba(255,255,255,.03);border-radius:5px;font-size:.74rem}

/* ═══ RIGHT SIDEBAR (AI Mentor) ═══ */
.sidebar-right{
  background:var(--bg2);border-left:1px solid var(--glass-border);
  display:flex;flex-direction:column;overflow:hidden;backdrop-filter:blur(20px);
}
.ai-header{
  padding:14px;border-bottom:1px solid var(--glass-border);
  display:flex;align-items:center;gap:10px;flex-shrink:0;
}
.ai-avatar{
  width:34px;height:34px;border-radius:9px;
  background:linear-gradient(135deg,#6366f1,#8b5cf6);
  display:flex;align-items:center;justify-content:center;font-size:.9rem;
}
.ai-title{flex:1}
.ai-title-text{font-family:var(--font-h);font-weight:600;font-size:.85rem}
.ai-title-sub{font-size:.62rem;color:var(--text3)}
.ai-close{
  width:28px;height:28px;border-radius:6px;border:none;background:transparent;
  color:var(--text3);font-size:.9rem;display:none;align-items:center;justify-content:center;
}
.ai-dot{width:7px;height:7px;border-radius:50%;background:var(--success);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:.5}50%{opacity:1}}

.ai-tabs{display:flex;border-bottom:1px solid var(--glass-border);flex-shrink:0}
.ai-tab{
  flex:1;padding:8px;text-align:center;font-size:.68rem;font-weight:600;
  color:var(--text3);cursor:pointer;border-bottom:2px solid transparent;transition:all .2s;
}
.ai-tab:hover{color:var(--text2)}
.ai-tab.active{color:var(--accent);border-bottom-color:var(--accent)}

.ai-content{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
.ai-msg{padding:10px 14px;border-radius:10px;font-size:.78rem;line-height:1.5}
.ai-msg.mentor{background:rgba(99,102,241,.06);border:1px solid rgba(99,102,241,.12);border-bottom-left-radius:3px}
.ai-msg.user{background:rgba(185,255,102,.04);border:1px solid rgba(185,255,102,.1);border-bottom-right-radius:3px;margin-left:16px}
.ai-msg .ml{font-size:.6rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:3px;color:var(--text3)}
.ai-msg .mt{color:var(--text)}
.ai-msg .mt strong{color:var(--accent)}
.ai-msg .mt code{background:rgba(255,255,255,.05);padding:1px 4px;border-radius:3px;font-size:.75rem}

.ai-suggest{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}
.ai-suggest button{
  padding:5px 10px;border-radius:100px;border:1px solid var(--glass-border);
  background:var(--glass);color:var(--text2);font-size:.68rem;cursor:pointer;transition:all .2s;
}
.ai-suggest button:hover{border-color:rgba(99,102,241,.3);color:#a5b4fc;background:rgba(99,102,241,.06)}

.ai-input-wrap{padding:10px 14px;border-top:1px solid var(--glass-border);flex-shrink:0;display:flex;gap:6px;align-items:flex-end}
.ai-input{
  flex:1;padding:9px 12px;border-radius:8px;border:1px solid var(--glass-border);
  background:rgba(255,255,255,.03);color:var(--text);font-size:.82rem;outline:none;
  resize:none;max-height:80px;font-family:var(--font-b);
}
.ai-input:focus{border-color:rgba(99,102,241,.35)}
.ai-send{
  width:36px;height:36px;border-radius:8px;border:none;
  background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-size:.95rem;
  display:flex;align-items:center;justify-content:center;transition:transform .2s;flex-shrink:0;
}
.ai-send:hover{transform:scale(1.05)}

.script-card{
  background:rgba(99,102,241,.03);border:1px solid rgba(99,102,241,.08);
  border-radius:8px;padding:12px;cursor:pointer;transition:all .2s;
}
.script-card:hover{border-color:rgba(99,102,241,.2);transform:translateY(-2px)}
.script-card .sc-t{font-weight:600;font-size:.82rem;margin-bottom:3px}
.script-card .sc-d{font-size:.72rem;color:var(--text2);line-height:1.4}
.script-card .sc-tag{display:inline-block;padding:2px 7px;border-radius:100px;font-size:.58rem;font-weight:600;margin-top:5px;background:rgba(99,102,241,.08);color:#a5b4fc}

/* ═══ CONTACT DETAIL MODAL ═══ */
.modal-overlay{
  position:fixed;inset:0;z-index:9000;background:rgba(0,0,0,.6);
  backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;
  padding:20px;
}
.modal-overlay.open{display:flex;animation:fadeIn .2s ease}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}

.modal-box{
  background:var(--bg2);border:1px solid var(--glass-border);border-radius:var(--radius);
  width:100%;max-width:560px;max-height:85vh;overflow-y:auto;
  box-shadow:0 20px 60px rgba(0,0,0,.5);position:relative;
  animation:modalSlide .3s ease;
}
@keyframes modalSlide{from{opacity:0;transform:translateY(20px) scale(.98)}to{opacity