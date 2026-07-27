#!/usr/bin/env python3
"""Write premium.css and index.html for LeadFlow CRM v2"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ════════════════════════════════════════════════════════════════════
# PREMIUM CSS
# ════════════════════════════════════════════════════════════════════
CSS = r'''/* LeadFlow CRM — Premium Visual Design
   Awwwards-level dark UI with glassmorphism, motion, and depth */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* ═══════════════════════════════════════════
   CUSTOM PROPERTIES
   ═══════════════════════════════════════════ */
:root {
  --accent: #00ffaa;
  --accent-dim: #00ffaa66;
  --accent-glow: #00ffaa33;
  --accent-rgb: 0, 255, 170;
  --bg: #0a0a0f;
  --bg2: #12121a;
  --bg3: #1a1a2e;
  --surface: #12121a;
  --card: rgba(255,255,255,0.04);
  --card-hover: rgba(255,255,255,0.08);
  --card-border: rgba(255,255,255,0.06);
  --glass: rgba(255,255,255,0.06);
  --glass-heavy: rgba(255,255,255,0.10);
  --glass-border: rgba(255,255,255,0.08);
  --glass-border-hover: rgba(255,255,255,0.15);
  --text: #e8e8f0;
  --text2: #8888aa;
  --text3: #555570;
  --text-bright: #ffffff;
  --success: #00ffaa;
  --fail: #ff4466;
  --warning: #ffaa00;
  --info: #00ccff;
  --radius: 16px;
  --radius-sm: 10px;
  --radius-xs: 6px;
  --radius-pill: 100px;
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.2);
  --shadow: 0 8px 32px rgba(0,0,0,0.4);
  --shadow-lg: 0 16px 64px rgba(0,0,0,0.5);
  --shadow-glow: 0 0 40px var(--accent-glow);
  --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-bounce: 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-heading: 'Space Grotesk', var(--font-body);
}

[data-theme="light"] {
  --bg: #f0f2f5;
  --bg2: #ffffff;
  --bg3: #e8eaee;
  --surface: #ffffff;
  --card: rgba(0,0,0,0.03);
  --card-hover: rgba(0,0,0,0.06);
  --card-border: rgba(0,0,0,0.06);
  --glass: rgba(255,255,255,0.7);
  --glass-heavy: rgba(255,255,255,0.85);
  --glass-border: rgba(0,0,0,0.08);
  --glass-border-hover: rgba(0,0,0,0.15);
  --text: #1a1a2e;
  --text2: #666680;
  --text3: #9999aa;
  --text-bright: #000000;
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
  --shadow: 0 8px 32px rgba(0,0,0,0.08);
  --shadow-lg: 0 16px 64px rgba(0,0,0,0.12);
}

[data-theme="deep-space"] {
  --bg: #050510;
  --bg2: #0a0a1a;
  --bg3: #10102a;
  --surface: #0a0a1a;
  --card: rgba(100,100,255,0.04);
  --card-hover: rgba(100,100,255,0.08);
  --card-border: rgba(100,100,255,0.08);
  --glass: rgba(100,100,255,0.06);
  --glass-heavy: rgba(100,100,255,0.10);
  --glass-border: rgba(100,100,255,0.1);
  --glass-border-hover: rgba(100,100,255,0.2);
  --accent: #6644ff;
  --accent-dim: #6644ff66;
  --accent-glow: #6644ff33;
  --accent-rgb: 102, 68, 255;
}

/* ═══════════════════════════════════════════
   RESET & BASE
   ═══════════════════════════════════════════ */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
body {
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  overflow-x: hidden;
  line-height: 1.6;
  transition: background var(--transition), color var(--transition);
}
::selection { background: var(--accent); color: #000; }

/* ═══════════════════════════════════════════
   SCROLLBAR
   ═══════════════════════════════════════════ */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--accent-dim); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }
* { scrollbar-width: thin; scrollbar-color: var(--accent-dim) transparent; }

/* ═══════════════════════════════════════════
   PARTICLE CANVAS & NOISE OVERLAY
   ═══════════════════════════════════════════ */
#particleCanvas {
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none; z-index: 0;
}
.noise-overlay {
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 1; opacity: 0.6;
}

/* ═══════════════════════════════════════════
   LOGIN OVERLAY — Animated mesh gradient blobs
   ═══════════════════════════════════════════ */
.login-overlay {
  position: fixed; inset: 0; z-index: 1000;
  display: flex; align-items: center; justify-content: center;
  background: var(--bg); overflow: hidden;
}
.login-overlay::before,
.login-overlay::after {
  content: ''; position: absolute; border-radius: 50%;
  filter: blur(120px); opacity: 0.35;
  animation: meshFloat 10s ease-in-out infinite alternate;
}
.login-overlay::before {
  width: 700px; height: 700px;
  background: radial-gradient(circle, var(--accent) 0%, transparent 70%);
  top: -20%; left: -15%;
}
.login-overlay::after {
  width: 600px; height: 600px;
  background: radial-gradient(circle, #6644ff 0%, transparent 70%);
  bottom: -25%; right: -15%;
  animation-delay: -5s;
}
@keyframes meshFloat {
  0%   { transform: translate(0, 0) scale(1); }
  25%  { transform: translate(50px, -40px) scale(1.08); }
  50%  { transform: translate(-30px, 50px) scale(0.94); }
  75%  { transform: translate(40px, 30px) scale(1.04); }
  100% { transform: translate(-20px, -30px) scale(1); }
}

/* Glassmorphism login card */
.login-box {
  position: relative; z-index: 2;
  width: 440px; max-width: 95vw;
  background: var(--glass-heavy);
  border: 1px solid var(--glass-border);
  border-radius: 28px;
  padding: 52px 44px 44px;
  backdrop-filter: blur(40px) saturate(1.5);
  -webkit-backdrop-filter: blur(40px) saturate(1.5);
  box-shadow: var(--shadow-lg), 0 0 80px var(--accent-glow), inset 0 1px 0 rgba(255,255,255,0.08);
  text-align: center;
  animation: loginSlideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes loginSlideUp {
  from { opacity: 0; transform: translateY(40px) scale(0.96); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

.login-logo {
  font-family: var(--font-heading);
  font-size: 46px; font-weight: 700; letter-spacing: -1.5px; margin-bottom: 4px;
  background: linear-gradient(135deg, var(--text-bright) 0%, var(--accent) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.login-logo .g {
  background: linear-gradient(135deg, var(--accent) 0%, #00ccff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.login-sub { font-size: 14px; color: var(--text2); margin-bottom: 36px; font-weight: 300; letter-spacing: 0.5px; }

/* Avatar Cards */
.login-avatars { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 28px; }
.avatar-card {
  background: var(--card); border: 2px solid transparent;
  border-radius: 16px; padding: 18px 8px 14px; cursor: pointer;
  transition: all var(--transition-bounce);
  position: relative; overflow: hidden;
}
.avatar-card::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, var(--accent) 0%, transparent 60%);
  opacity: 0; transition: opacity var(--transition); border-radius: 14px;
}
.avatar-card:hover {
  border-color: var(--accent); transform: translateY(-6px) scale(1.02);
  box-shadow: 0 12px 32px rgba(var(--accent-rgb), 0.25), 0 0 0 1px var(--accent-dim);
}
.avatar-card:hover::before { opacity: 0.1; }
.avatar-card.selected {
  border-color: var(--accent); background: rgba(var(--accent-rgb), 0.12);
  box-shadow: 0 0 40px rgba(var(--accent-rgb), 0.3), 0 0 0 1px var(--accent), inset 0 1px 0 rgba(255,255,255,0.1);
  transform: translateY(-4px);
}
.avatar-card.selected::before { opacity: 0.15; }
.avatar-emoji { font-size: 30px; margin-bottom: 8px; position: relative; z-index: 1; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3)); }
.avatar-name { font-size: 10px; font-weight: 600; line-height: 1.3; position: relative; z-index: 1; }
.avatar-role { font-size: 8px; color: var(--text3); margin-top: 3px; position: relative; z-index: 1; }

/* Login Field */
.login-field { text-align: left; margin-bottom: 24px; position: relative; }
.login-field label { display: block; font-size: 11px; font-weight: 600; color: var(--text2); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1.5px; }
.login-field input {
  width: 100%; padding: 16px 18px;
  background: var(--card); border: 1.5px solid var(--glass-border);
  border-radius: var(--radius-sm); color: var(--text);
  font-size: 15px; font-family: var(--font-body);
  outline: none; transition: all var(--transition);
}
.login-field input::placeholder { color: var(--text3); }
.login-field input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px rgba(var(--accent-rgb), 0.15), 0 0 20px rgba(var(--accent-rgb), 0.1);
  background: var(--glass-heavy);
}

/* Login Button */
.login-btn {
  width: 100%; padding: 16px;
  background: linear-gradient(135deg, var(--accent), #00ccff);
  border: none; border-radius: var(--radius-sm);
  color: #000; font-size: 15px; font-weight: 700;
  font-family: var(--font-body); cursor: pointer;
  transition: all var(--transition);
  text-transform: uppercase; letter-spacing: 1.5px;
  position: relative; overflow: hidden;
}
.login-btn::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%);
  transform: translateX(-100%); transition: transform 0.6s;
}
.login-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(var(--accent-rgb), 0.4), 0 0 80px rgba(var(--accent-rgb), 0.15);
}
.login-btn:hover::before { transform: translateX(100%); }
.login-btn:active { transform: translateY(-1px) scale(0.98); }
.login-err { color: var(--fail); font-size: 13px; margin-top: 14px; min-height: 20px; font-weight: 500; }

/* ═══════════════════════════════════════════
   APP LAYOUT
   ═══════════════════════════════════════════ */
.app-layout {
  display: none; width: 100vw; height: 100vh;
  position: relative; z-index: 2;
}

/* ═══════════════════════════════════════════
   SIDEBAR — Narrow icon sidebar, glassmorphism
   ═══════════════════════════════════════════ */
.sidebar {
  width: 72px; height: 100vh;
  background: var(--glass-heavy);
  border-right: 1px solid var(--glass-border);
  backdrop-filter: blur(30px) saturate(1.4);
  -webkit-backdrop-filter: blur(30px) saturate(1.4);
  display: flex; flex-direction: column;
  align-items: center; padding: 20px 0; gap: 6px;
  overflow-y: auto; flex-shrink: 0;
  position: relative;
}
.sidebar-item {
  width: 52px; height: 52px;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  border-radius: 14px; cursor: pointer;
  transition: all var(--transition);
  position: relative; font-size: 10px; color: var(--text3);
}
.sidebar-item:hover {
  background: var(--card-hover); color: var(--text);
  transform: scale(1.05);
}
.sidebar-item:hover .sidebar-icon { filter: drop-shadow(0 0 8px var(--accent-dim)); }
.sidebar-item.active {
  background: rgba(var(--accent-rgb), 0.12);
  color: var(--accent);
  box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.15);
}
.sidebar-item.active::before {
  content: ''; position: absolute; left: -10px;
  width: 3px; height: 24px;
  background: var(--accent);
  border-radius: 0 4px 4px 0;
  box-shadow: 0 0 10px var(--accent);
}
.sidebar-icon { font-size: 22px; margin-bottom: 2px; transition: all var(--transition); }
.sidebar-label { font-size: 8px; font-weight: 500; }

/* ═══════════════════════════════════════════
   MAIN AREA
   ═══════════════════════════════════════════ */
.main-area { flex: 1; display: flex; flex-direction: column; min-width: 0; }

/* ═══════════════════════════════════════════
   TOPBAR — Sticky glassmorphism blur
   ═══════════════════════════════════════════ */
.topbar {
  height: 68px; display: flex; align-items: center;
  padding: 0 28px;
  background: var(--glass-heavy);
  border-bottom: 1px solid var(--glass-border);
  backdrop-filter: blur(30px) saturate(1.4);
  -webkit-backdrop-filter: blur(30px) saturate(1.4);
  gap: 16px; flex-shrink: 0;
  position: sticky; top: 0; z-index: 100;
}
.hamburger { display: none; background: none; border: none; color: var(--text); font-size: 24px; cursor: pointer; padding: 4px; }
.topbar-left { flex: 1; }
.topbar-title {
  font-family: var(--font-heading); font-size: 22px; font-weight: 700;
  background: linear-gradient(135deg, var(--text) 0%, var(--accent) 120%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.topbar-bc { font-size: 12px; color: var(--text3); margin-top: 2px; }
.topbar-right { display: flex; align-items: center; gap: 14px; }
.topbar-avatar {
  width: 40px; height: 40px;
  background: rgba(var(--accent-rgb), 0.15);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px;
  border: 2px solid var(--accent);
  box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.2);
  transition: all var(--transition);
}
.topbar-avatar:hover { box-shadow: 0 0 30px rgba(var(--accent-rgb), 0.35); transform: scale(1.05); }
.tb-btn {
  background: var(--card); border: 1px solid var(--glass-border);
  border-radius: var(--radius-sm); color: var(--text);
  padding: 8px 18px; font-size: 13px; cursor: pointer;
  transition: all var(--transition); font-family: var(--font-body);
}
.tb-btn:hover { background: rgba(var(--accent-rgb), 0.12); border-color: var(--accent); color: var(--accent); }

/* ═══════════════════════════════════════════
   CONTENT SCROLL
   ═══════════════════════════════════════════ */
.content-scroll {
  flex: 1; overflow-y: auto; padding: 28px; scroll-behavior: smooth;
}

/* ═══════════════════════════════════════════
   STAT CARDS — Overview Dashboard
   ═══════════════════════════════════════════ */
.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 18px; margin-bottom: 36px;
}
.stat-card {
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius);
  padding: 28px 24px; text-align: center;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  backdrop-filter: blur(10px);
}
.stat-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent), transparent);
  opacity: 0; transition: opacity var(--transition);
}
.stat-card::after {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(var(--accent-rgb), 0.06) 0%, transparent 60%);
  opacity: 0; transition: opacity var(--transition);
}
.stat-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.3), 0 0 30px rgba(var(--accent-rgb), 0.1);
  border-color: var(--accent);
}
.stat-card:hover::before { opacity: 1; }
.stat-card:hover::after { opacity: 1; }
.stat-icon { font-size: 36px; margin-bottom: 10px; position: relative; z-index: 1; }
.stat-value {
  font-family: var(--font-heading); font-size: 40px; font-weight: 700;
  color: var(--accent); position: relative; z-index: 1;
  text-shadow: 0 0 20px rgba(var(--accent-rgb), 0.3);
}
.stat-label { font-size: 13px; color: var(--text2); margin-top: 6px; position: relative; z-index: 1; }
.clickable { cursor: pointer; }

/* ═══════════════════════════════════════════
   SECTION TITLES
   ═══════════════════════════════════════════ */
.section-title {
  font-family: var(--font-heading); font-size: 17px; font-weight: 600;
  color: var(--text2); margin-bottom: 18px; padding-bottom: 10px;
  border-bottom: 1px solid var(--glass-border);
  letter-spacing: 0.3px;
}

/* ═══════════════════════════════════════════
   CATEGORY PILLS
   ═══════════════════════════════════════════ */
.cat-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 36px; }
.cat-pill {
  background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: var(--radius-pill); padding: 10px 18px;
  font-size: 13px; display: flex; align-items: center; gap: 8px;
  transition: all var(--transition); backdrop-filter: blur(8px);
}
.cat-pill:hover {
  background: rgba(var(--accent-rgb), 0.12);
  border-color: var(--accent);
  box-shadow: 0 4px 16px rgba(var(--accent-rgb), 0.15);
  transform: translateY(-2px);
}
.cat-count {
  background: var(--accent); color: #000;
  border-radius: 20px; padding: 2px 10px;
  font-size: 11px; font-weight: 700;
}

/* ═══════════════════════════════════════════
   COUNTRY HEADER
   ═══════════════════════════════════════════ */
.country-header {
  display: flex; align-items: center; gap: 24px;
  margin-bottom: 28px; padding: 28px;
  background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: var(--radius);
  backdrop-filter: blur(10px);
  transition: all var(--transition);
}
.country-header:hover { box-shadow: 0 8px 32px rgba(var(--accent-rgb), 0.08); }
.country-flag-big {