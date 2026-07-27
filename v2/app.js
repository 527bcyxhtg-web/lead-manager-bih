/* LeadFlow Platform v2 — App Logic (Complete) */

/* ═══════════════════════════════════════════════════════════════
   0. GLOBALS & CONSTANTS
   ═══════════════════════════════════════════════════════════════ */

var currentUser = null;
var currentView = 'overview';
var currentCountry = 'ba';
var currentAgent = null;
var selectedContact = null;
var aiTab = 'chat';
var mobileSidebarOpen = false;
var aiOpen = false;
var themePanelOpen = false;

var COUNTRY_FLAGS = { ba: '🇧🇦', hr: '🇭🇷', rs: '🇷🇸' };
var COUNTRY_NAMES = { ba: 'Bosna i Hercegovina', hr: 'Hrvatska', rs: 'Srbija' };

var CAT_ICONS = {
  'Frizerski salon': '✂️', 'Kozmetički salon': '💆', 'Restoran': '🍽️',
  'Auto servis': '🔧', 'Caffe bar': '☕', 'Trgovina': '🛒',
  'Stolarija': '🪵', 'Cvjećara': '🌸', 'Autopraonica': '🚗',
  'Auto dijelovi': '⚙️', 'Optika': '👓', 'Trgovina odjećom': '👖',
  'Električar': '⚡', 'Putnička agencija': '✈️', 'Hotel': '🏨',
  'Advokat': '⚖️', 'Računovodstvo': '📊', 'Fitness': '💪',
  'Pekara': '🥐', 'Autolimar': '🔨', 'Građevinska': '🏗️',
  'Stomatologija': '🦷', 'Knjižara': '📚', 'Fitness studio': '🏋️',
  'Auto': '🚗'
};

var AI_SCRIPTS = [
  { title: 'Hladan poziv — uvod', desc: 'Kratki uvod za novog klijenta', tag: '📞 Poziv', text: 'Dobar dan, zovem iz LeadFlow agencije. Vidjeli smo vaše poslovanje i mislimo da vam možemo pomoći s digitalnim marketingom. Imate li 2 minuta?' },
  { title: 'Follow-up email', desc: 'Nakon prvog kontakta', tag: '📧 Email', text: 'Poštovani, zahvaljujem se na razgovoru. Kao što smo dogovorili, šaljem vam ponudu za naše usluge. Molim vas da pogledate i javite se s pitanjima.' },
  { title: 'Obnova kontakta', desc: 'Za stare klijente', tag: '🔄 Restart', text: 'Zdravo, dugo se nismo čuli! Željeli smo vidjeti kako ide vaše poslovanje i ponuditi vam nove mogućnosti koje imamo.' },
  { title: 'Predstavljanje demoa', desc: 'Poziv za demo termin', tag: '💻 Demo', text: 'Imamo sjajan alat koji vam može pomoći da pratite sve vaše kontakte na jednom mjestu. Želite li besplatni demo?' },
  { title: 'Zatvaranje prodaje', desc: 'Završni korak', tag: '💰 Prodaja', text: 'Vidjeli ste sve prednosti. Danas je idealan dan da krenemo. Potpisujemo ugovor i krećemo odmah!' }
];

/* ═══════════════════════════════════════════════════════════════
   1. BOOT / INIT
   ═══════════════════════════════════════════════════════════════ */

function boot() {
  migrateContacts();
  seedContacts();
  setTheme(getTheme());
  tryRestoreSession();
  initParticles();
  initScrollObserver();
  initRippleEffects();
  bindLoginEvents();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', boot);
} else {
  boot();
}

function bindLoginEvents() {
  var btn = document.getElementById('doLogin');
  if (btn) btn.addEventListener('click', doLogin);
  var pass = document.getElementById('loginPass');
  if (pass) pass.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') doLogin();
  });
}

/* ═══════════════════════════════════════════════════════════════
   2. LOGIN SYSTEM
   ═══════════════════════════════════════════════════════════════ */

function showLogin() {
  var el = document.getElementById('loginAvatars');
  if (!el) return;
  var h = '';
  USERS.forEach(function (u) {
    h += '<div class="login-av" id="lav-' + u.id + '" onclick="selectLoginUser(\'' + u.id + '\',this)">';
    h += '<div style="width:56px;height:56px;border-radius:14px;background:' + u.color + ';display:flex;align-items:center;justify-content:center;font-family:var(--font-h);font-weight:700;font-size:.85rem;color:#000">' + u.initials + '</div>';
    h += '<div class="login-av-name">' + u.name.split(' ')[0] + '</div>';
    h += '</div>';
  });
  el.innerHTML = h;
}

function selectLoginUser(uid, el) {
  document.querySelectorAll('.login-av').forEach(function (c) { c.classList.remove('sel'); });
  if (el) el.classList.add('sel');
  currentUser = USERS.find(function (u) { return u.id === uid; });
  document.getElementById('loginPass').focus();
}

function showLoginErr(msg) {
  var e = document.getElementById('loginErr');
  if (e) { e.textContent = msg; e.style.display = 'block'; }
}

function initLoginAvatars() {
  showLogin();
}

function tryRestoreSession() {
  var saved = localStorage.getItem(DB + '_session');
  if (saved) {
    try {
      var uid = saved;
      currentUser = USERS.find(function (u) { return u.id === uid; });
      if (currentUser) {
        showApp();
        return;
      }
    } catch (e) { /* ignore */ }
  }
  showLogin();
}

function doLogin() {
  if (!currentUser) { showLoginErr('Odaberi profil!'); return; }
  var pass = document.getElementById('loginPass').value;
  if (pass !== currentUser.pass) {
    showLoginErr('Pogrešna lozinka!');
    return;
  }
  localStorage.setItem(DB + '_session', currentUser.id);
  showApp();
}

function doLogout() {
  currentUser = null;
  localStorage.removeItem(DB + '_session');
  currentView = 'overview';
  currentCountry = 'ba';
  currentAgent = null;
  showLogin();
  var overlay = document.getElementById('loginOverlay');
  if (overlay) { overlay.classList.remove('hidden'); overlay.style.display = ''; }
  var app = document.getElementById('appLayout');
  if (app) { app.classList.remove('active'); app.style.display = ''; }
}

function showLogin() {
  var overlay = document.getElementById('loginOverlay');
  if (overlay) { overlay.classList.remove('hidden'); overlay.style.display = ''; }
  var app = document.getElementById('appLayout');
  if (app) { app.classList.remove('active'); app.style.display = 'none'; }
  initLoginAvatars();
}

function showApp() {
  var overlay = document.getElementById('loginOverlay');
  if (overlay) { overlay.classList.add('hidden'); overlay.style.display = 'none'; }
  var app = document.getElementById('appLayout');
  if (app) { app.classList.add('active'); app.style.display = 'grid'; }
  render();
}

/* ═══════════════════════════════════════════════════════════════
   3. MASTER RENDER
   ═══════════════════════════════════════════════════════════════ */

function render() {
  updateTopbar();
  updateSidebar();
  renderContent();
}

function updateTopbar() {
  var titleEl = document.getElementById('topTitle');
  var bcEl = document.getElementById('topBC');
  var avEl = document.getElementById('topAvatar');
  var avTitle = document.getElementById('topAvatarTitle');

  if (currentView === 'overview') {
    if (titleEl) titleEl.textContent = '📊 Pregled';
    if (bcEl) bcEl.textContent = 'Sve države';
  } else if (currentView === 'country') {
    if (titleEl) titleEl.textContent = (COUNTRY_FLAGS[currentCountry] || '') + ' ' + (COUNTRY_NAMES[currentCountry] || currentCountry);
    if (bcEl) bcEl.textContent = 'Kontakti po državi';
  } else if (currentView === 'agent') {
    var ag = USERS.find(function (u) { return u.id === currentAgent; });
    if (titleEl) titleEl.textContent = (ag ? ag.name : 'Agent');
    if (bcEl) bcEl.textContent = (COUNTRY_FLAGS[currentCountry] || '') + ' ' + (COUNTRY_NAMES[currentCountry] || '');
  } else if (currentView === 'tarot') {
    if (titleEl) titleEl.textContent = '✨ Tarot';
    if (bcEl) bcEl.textContent = 'Dnevna kartica';
  } else {
    if (titleEl) titleEl.textContent = '📊 Pregled';
    if (bcEl) bcEl.textContent = '';
  }

  if (avEl && currentUser) {
    avEl.textContent = currentUser.initials;
    avEl.style.background = currentUser.color;
    avEl.style.color = '#000';
    avEl.style.borderRadius = '8px';
    avEl.style.display = 'flex';
    avEl.style.alignItems = 'center';
    avEl.style.justifyContent = 'center';
    avEl.style.fontFamily = 'var(--font-h)';
    avEl.style.fontWeight = '700';
    avEl.style.fontSize = '.7rem';
    avEl.style.cursor = 'pointer';
    avEl.onclick = function () { doLogout(); };
  }
  if (avTitle && currentUser) {
    avTitle.textContent = currentUser.name;
  }
}

function updateSidebar() {
  var el = document.getElementById('sidebarIcons');
  if (!el) return;

  var items = [
    { id: 'overview', icon: '📊', label: 'Pregled' },
    { id: 'ba', icon: '🇧🇦', label: 'BiH' },
    { id: 'hr', icon: '🇭🇷', label: 'Hrvatska' },
    { id: 'rs', icon: '🇷🇸', label: 'Srbija' },
    { id: 'tarot', icon: '✨', label: 'Tarot' }
  ];

  var h = '';
  items.forEach(function (it) {
    var isActive = false;
    if (it.id === 'overview' && currentView === 'overview') isActive = true;
    if (it.id === currentCountry && (currentView === 'country' || currentView === 'agent')) isActive = true;
    if (it.id === 'tarot' && currentView === 'tarot') isActive = true;

    h += '<div class="sidebar-icon' + (isActive ? ' active' : '') + '" onclick="switchView(\'' + it.id + '\')" title="' + it.label + '">';
    h += '<span>' + it.icon + '</span>';
    h += '</div>';
  });

  h += '<div class="sidebar-sep"></div>';
  h += '<div class="sidebar-bottom">';
  h += '<div class="sidebar-icon" onclick="doLogout()" title="Odjava"><span>🚪</span></div>';
  h += '</div>';

  el.innerHTML = h;
}

function renderContent() {
  var el = document.getElementById('contentScroll');
  if (!el) return;

  /* Page transition: fade out */
  el.classList.add('page-transition');
  el.style.opacity = '0';
  el.style.transform = 'translateY(8px)';

  setTimeout(function () {
    /* Show skeleton briefly */
    el.innerHTML = renderSkeleton();

    setTimeout(function () {
      if (currentView === 'overview') renderOverview(el);
      else if (currentView === 'country') renderCountry(el);
      else if (currentView === 'agent') renderAgentContacts(el);
      else if (currentView === 'tarot') renderTarotOverlay();
      else renderOverview(el);

      /* Fade in */
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
      el.classList.remove('page-transition');
      initScrollObserver();
      initRippleEffects();
      animateNumbers(el);
    }, 300);
  }, 200);
}

function switchView(id) {
  if (id === 'ba' || id === 'hr' || id === 'rs') {
    currentCountry = id;
    currentView = 'country';
    currentAgent = null;
  } else {
    currentView = id;
  }
  closeMobileSidebar();
  render();
}

/* ═══════════════════════════════════════════════════════════════
   4. SKELETON LOADING
   ═══════════════════════════════════════════════════════════════ */

function renderSkeleton() {
  var h = '';
  h += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px">';
  for (var i = 0; i < 4; i++) {
    h += '<div class="skeleton" style="height:90px;border-radius:var(--radius-xs)"></div>';
  }
  h += '</div>';
  for (var j = 0; j < 5; j++) {
    h += '<div class="skeleton" style="height:64px;margin-bottom:6px;border-radius:var(--radius-xs)"></div>';
  }
  return h;
}

/* ═══════════════════════════════════════════════════════════════
   5. OVERVIEW
   ═══════════════════════════════════════════════════════════════ */

function renderOverview(el) {
  var all = getAllContacts();
  var total = all.length;
  var done = all.filter(function (c) { return c.status === 'done'; }).length;
  var inProgress = all.filter(function (c) { return c.status === 'in_progress'; }).length;
  var pending = all.filter(function (c) { return c.status === 'pending'; }).length;
  var lost = all.filter(function (c) { return c.status === 'lost'; }).length;
  var saleSuccess = all.filter(function (c) { return c.saleOutcome === 'success'; }).length;
  var demosSent = all.filter(function (c) { return c.demoSent; }).length;

  var h = '';

  /* Bento stats */
  h += '<div class="bento">';
  h += bentoCard('📋', total, 'Ukupno leadova', 'var(--text)');
  h += bentoCard('✅', done, 'Završeno', 'var(--success)');
  h += bentoCard('🔄', inProgress, 'U toku', 'var(--info)');
  h += bentoCard('⏳', pending, 'Na čekanju', 'var(--warn)');
  h += '</div>';

  h += '<div class="bento">';
  h += bentoCard('❌', lost, 'Izgubljeno', 'var(--danger)');
  h += bentoCard('💰', saleSuccess, 'Uspješna prodaja', 'var(--success)');
  h += bentoCard('📧', demosSent, 'Demo poslano', 'var(--info)');
  h += bentoCard('🏆', total > 0 ? Math.round(done / total * 100) : 0, 'Konverzija %', 'var(--accent)');
  h += '</div>';

  /* Categories */
  var cats = {};
  all.forEach(function (c) { cats[c.cat] = (cats[c.cat] || 0) + 1; });
  var topCats = Object.keys(cats).sort(function (a, b) { return cats[b] - cats[a]; }).slice(0, 8);

  if (topCats.length > 0) {
    h += '<div class="anim-in"><div style="font-family:var(--font-h);font-weight:700;font-size:1rem;margin:16px 0 10px">📌 Kategorije</div>';
    h += '<div style="display:flex;flex-wrap:wrap;gap:6px">';
    topCats.forEach(function (cat) {
      h += '<div class="glass-card" style="padding:8px 14px;display:flex;align-items:center;gap:6px;cursor:default">';
      h += '<span>' + (CAT_ICONS[cat] || '📌') + '</span>';
      h += '<span style="font-size:.82rem;font-weight:600">' + cat + '</span>';
      h += '<span style="font-size:.7rem;color:var(--text2);background:rgba(255,255,255,.05);padding:2px 7px;border-radius:100px">' + cats[cat] + '</span>';
      h += '</div>';
    });
    h += '</div></div>';
  }

  /* Country cards */
  h += '<div class="anim-in"><div style="font-family:var(--font-h);font-weight:700;font-size:1rem;margin:16px 0 10px">🌍 Po državama</div>';
  h += '<div class="overview-grid">';
  ['ba', 'hr', 'rs'].forEach(function (cc) {
    var ccContacts = all.filter(function (c) { return c.country === cc; });
    var ccDone = ccContacts.filter(function (c) { return c.status === 'done'; }).length;
    var ccSale = ccContacts.filter(function (c) { return c.saleOutcome === 'success'; }).length;
    var ccAgents = USERS.filter(function (u) { return u.country === cc; });
    h += '<div class="overview-card ' + cc + '" onclick="switchView(\'' + cc + '\')">';
    h += '<div class="oc-flag">' + COUNTRY_FLAGS[cc] + '</div>';
    h += '<div class="oc-name">' + COUNTRY_NAMES[cc] + '</div>';
    h += '<div class="oc-count">' + ccContacts.length + ' kontakata · ' + ccDone + ' završeno · ' + ccSale + ' prodaja</div>';
    h += '<div class="oc-teams">';
    ccAgents.forEach(function (ag) {
      var agCount = all.filter(function (c) { return c.owner === ag.id; }).length;
      h += '<div class="oc-team"><span>' + ag.name.split(' ')[0] + '</span><span style="color:var(--accent);font-weight:600">' + agCount + '</span></div>';
    });
    h += '</div></div>';
  });
  h += '</div></div>';

  el.innerHTML = h;
}

function bentoCard(icon, value, label, color) {
  return '<div class="bento-card anim-in">' +
    '<div class="b-icon" style="background:rgba(255,255,255,.04);color:' + (color || 'var(--text)') + '">' + icon + '</div>' +
    '<div class="b-val" data-count-to="' + value + '">' + value + '</div>' +
    '<div class="b-lbl">' + label + '</div></div>';
}

/* ═══════════════════════════════════════════════════════════════
   6. COUNTRY VIEW
   ═══════════════════════════════════════════════════════════════ */

function renderCountry(el) {
  var contacts = getCountryContacts(currentCountry);
  var agents = USERS.filter(function (u) { return u.country === currentCountry || u.country === 'all'; });

  var h = '';

  /* Country header */
  h += '<div class="anim-in" style="display:flex;align-items:center;gap:14px;margin-bottom:16px">';
  h += '<div style="font-size:2.4rem">' + COUNTRY_FLAGS[currentCountry] + '</div>';
  h += '<div><div style="font-family:var(--font-h);font-weight:700;font-size:1.1rem">' + COUNTRY_NAMES[currentCountry] + '</div>';
  h += '<div style="font-size:.78rem;color:var(--text2)">' + contacts.length + ' kontakata ukupno</div></div>';
  h += '</div>';

  /* Team cards */
  h += '<div class="anim-in"><div style="font-family:var(--font-h);font-weight:700;font-size:.95rem;margin-bottom:10px">👥 Tim</div>';
  h += '<div class="team-grid">';
  agents.forEach(function (ag) {
    if (ag.country === 'all') return;
    var agContacts = contacts.filter(function (c) { return c.owner === ag.id; });
    var agDone = agContacts.filter(function (c) { return c.status === 'done'; }).length;
    var isActive = currentAgent === ag.id;
    h += '<div class="team-card' + (isActive ? ' active-card' : '') + '" onclick="selectAgent(\'' + ag.id + '\')">';
    h += '<div class="team-av" style="background:' + ag.color + ';color:#000">' + ag.initials + '</div>';
    h += '<div class="team-name">' + ag.name + '</div>';
    h += '<div class="team-role">' + ag.role + '</div>';
    h += '<div class="team-stats">';
    h += '<div class="team-stat"><div class="team-stat-val">' + agContacts.length + '</div><div class="team-stat-lbl">Leadovi</div></div>';
    h += '<div class="team-stat"><div class="team-stat-val">' + agDone + '</div><div class="team-stat-lbl">Završeno</div></div>';
    h += '<div class="team-stat"><div class="team-stat-val">' + agContacts.length > 0 ? Math.round(agDone / agContacts.length * 100) : 0 + '%</div><div class="team-stat-lbl">Stopa</div></div>';
    h += '</div></div>';
  });
  h += '</div></div>';

  /* Add form */
  h += renderAddForm();

  /* Contact list */
  h += '<div class="anim-in"><div style="font-family:var(--font-h);font-weight:700;font-size:.95rem;margin-bottom:10px">📋 Kontakti</div>';
  h += '<div class="contact-list" id="contactList">';
  contacts.forEach(function (c) {
    h += renderContactItem(c);
  });
  if (contacts.length === 0) {
    h += '<div style="text-align:center;padding:40px;color:var(--text3)">Nema kontakata u ovoj državi</div>';
  }
  h += '</div></div>';

  el.innerHTML = h;
}

/* ═══════════════════════════════════════════════════════════════
   7. AGENT CONTACTS VIEW
   ═══════════════════════════════════════════════════════════════ */

function renderAgentContacts(el) {
  if (!currentAgent) { renderCountry(el); return; }
  var agent = USERS.find(function (u) { return u.id === currentAgent; });
  var contacts = getUserContacts(currentAgent);

  var h = '';

  h += '<div class="anim-in" style="display:flex;align-items:center;gap:14px;margin-bottom:16px">';
  h += '<div style="width:48px;height:48px;border-radius:12px;background:' + (agent ? agent.color : 'var(--accent)') + ';display:flex;align-items:center;justify-content:center;font-family:var(--font-h);font-weight:700;color:#000;font-size:.9rem">' + (agent ? agent.initials : '??') + '</div>';
  h += '<div><div style="font-family:var(--font-h);font-weight:700;font-size:1.05rem">' + (agent ? agent.name : 'Nepoznat') + '</div>';
  h += '<div style="font-size:.78rem;color:var(--text2)">' + COUNTRY_FLAGS[currentCountry] + ' ' + contacts.length + ' kontakata</div></div>';
  h += '<button class="btn-ghost" onclick="currentAgent=null;switchView(\'' + currentCountry + '\')" style="margin-left:auto;font-size:.75rem">← Nazad</button>';
  h += '</div>';

  /* Stats */
  var done = contacts.filter(function (c) { return c.status === 'done'; }).length;
  var sale = contacts.filter(function (c) { return c.saleOutcome === 'success'; }).length;
  h += '<div class="bento">';
  h += bentoCard('📋', contacts.length, 'Ukupno', 'var(--text)');
  h += bentoCard('✅', done, 'Završeno', 'var(--success)');
  h += bentoCard('💰', sale, 'Prodaja', 'var(--success)');
  h += bentoCard('📧', contacts.filter(function (c) { return c.demoSent; }).length, 'Demo', 'var(--info)');
  h += '</div>';

  /* Add form */
  h += renderAddForm();

  /* Contact list */
  h += '<div class="anim-in"><div class="contact-list" id="contactList">';
  contacts.forEach(function (c) {
    h += renderContactItem(c);
  });
  if (contacts.length === 0) {
    h += '<div style="text-align:center;padding:40px;color:var(--text3)">Nema kontakata za ovog agenta</div>';
  }
  h += '</div></div>';

  el.innerHTML = h;
}

function selectAgent(agentId) {
  currentAgent = agentId;
  currentView = 'agent';
  render();
}

/* ═══════════════════════════════════════════════════════════════
   8. CONTACT CARD RENDERING
   ═══════════════════════════════════════════════════════════════ */

function renderContactItem(c) {
  var id = c._id || '';
  var statusClass = 's-pending';
  var statusLabel = '⏳ Pending';
  if (c.status === 'in_progress') { statusClass = 's-progress'; statusLabel = '🔄 In Progress'; }
  if (c.status === 'done') { statusClass = 's-done'; statusLabel = '✅ Done'; }
  if (c.status === 'lost') { statusClass = 's-lost'; statusLabel = '❌ Lost'; }

  var saleIcon = c.saleOutcome === 'success' ? '✅ Uspješna' : (c.saleOutcome === 'failed' ? '❌ Neuspješna' : '💰 —');
  var saleClass = c.saleOutcome === 'success' ? 'sale-btn-green' : (c.saleOutcome === 'failed' ? 'sale-btn-red' : '');
  var demoLabel = c.demoSent ? '📧 Da' : '📧 Ne';
  var demoClass = c.demoSent ? 'demo-btn' : '';

  var h = '';

  /* Main card */
  h += '<div class="contact-item ' + statusClass + '" data-id="' + id + '">';
  h += '<div class="ci-avatar" style="background:rgba(255,255,255,.06)">' + (CAT_ICONS[c.cat] || '📌') + '</div>';
  h += '<div class="ci-info" onclick="openContactModal(\'' + id + '\')">';
  h += '<div class="ci-name">' + (c.company || 'Nepoznat') + '</div>';
  h += '<div class="ci-meta">';
  if (c.city) h += '<span class="city">' + c.city + '</span>';
  h += '<span>' + (c.cat || '') + '</span>';
  if (c.phone) h += '<span>📞 ' + c.phone + '</span>';
  h += '</div></div>';

  /* Inline action buttons */
  h += '<div class="ci-actions">';
  /* Complete button */
  h += '<div class="ci-btn done-btn" onclick="event.stopPropagation();cycleStatusInline(\'' + id + '\')" title="Označi završeno">✅</div>';
  /* Reset button */
  h += '<div class="ci-btn" onclick="event.stopPropagation();resetStatusInline(\'' + id + '\')" title="Resetuj na pending">🔄</div>';
  /* Comment toggle */
  h += '<div class="ci-btn" onclick="event.stopPropagation();toggleComment(\'' + id + '\')" title="Komentar">💬</div>';
  /* Sale toggle */
  h += '<div class="ci-btn ' + saleClass + '" onclick="event.stopPropagation();toggleSaleInline(\'' + id + '\')" title="Prodaja">' + (c.saleOutcome === 'success' ? '✅' : '💰') + '</div>';
  /* Demo toggle */
  h += '<div class="ci-btn ' + demoClass + '" onclick="event.stopPropagation();toggleDemoInline(\'' + id + '\')" title="Demo">' + (c.demoSent ? '📧' : '📩') + '</div>';
  /* Status badge */
  h += '<span class="ci-status ' + statusClass + '">' + statusLabel + '</span>';
  h += '</div>';
  h += '</div>';

  /* Comment section (expandable) */
  h += '<div class="contact-comment" id="comment-' + id + '">';
  h += '<textarea placeholder="Dodaj komentar..." onblur="saveContactComment(\'' + id + '\',this.value)">' + (c.comments || '') + '</textarea>';
  h += '</div>';

  return h;
}

/* ═══════════════════════════════════════════════════════════════
   9. INLINE CONTACT ACTIONS
   ═══════════════════════════════════════════════════════════════ */

function cycleStatusInline(id) {
  var contacts = getContacts();
  if (!contacts[id]) return;
  var c = contacts[id];
  if (c.status === 'pending') c.status = 'in_progress';
  else if (c.status === 'in_progress') c.status = 'done';
  else c.status = 'done';
  addTimelineEntry(id, 'Status promijenjen na: ' + c.status);
  saveContacts(contacts);
  toast('✅ Status ažuriran: ' + c.status);
  render();
}

function resetStatusInline(id) {
  updateContact(id, 'status', 'pending');
  addTimelineEntry(id, 'Status resetovan na: pending');
  toast('🔄 Status resetovan');
  render();
}

function toggleComment(id) {
  var el = document.getElementById('comment-' + id);
  if (el) {
    el.classList.toggle('open');
    if (el.classList.contains('open')) {
      var ta = el.querySelector('textarea');
      if (ta) ta.focus();
    }
  }
}

function saveContactComment(id, value) {
  updateContact(id, 'comments', value);
  toast('💬 Komentar spremljen');
}

function toggleSaleInline(id) {
  var contacts = getContacts();
  if (!contacts[id]) return;
  var c = contacts[id];
  if (c.saleOutcome === 'success') c.saleOutcome = '';
  else c.saleOutcome = 'success';
  addTimelineEntry(id, 'Prodaja: ' + (c.saleOutcome === 'success' ? 'Uspješna' : 'Poništena'));
  saveContacts(contacts);
  toast(c.saleOutcome === 'success' ? '💰 Prodaja zabilježena!' : '💰 Prodaja poništena');
  render();
}

function toggleDemoInline(id) {
  var contacts = getContacts();
  if (!contacts[id]) return;
  var c = contacts[id];
  c.demoSent = !c.demoSent;
  addTimelineEntry(id, 'Demo: ' + (c.demoSent ? 'Poslan' : 'Nije poslan'));
  saveContacts(contacts);
  toast(c.demoSent ? '📧 Demo označen kao poslan' : '📧 Demo poništen');
  render();
}

/* ═══════════════════════════════════════════════════════════════
   10. ADD FORM
   ═══════════════════════════════════════════════════════════════ */

function renderAddForm() {
  var h = '';
  h += '<div class="add-form" id="addForm">';
  h += '<div style="font-family:var(--font-h);font-weight:600;font-size:.88rem;margin-bottom:12px">➕ Dodaj novi kontakt</div>';
  h += '<div class="form-grid">';
  h += formField('af-company', 'Naziv firme *', 'text', '', true