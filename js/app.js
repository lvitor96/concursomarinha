/**
 * app.js — Controlador principal do SEDF Estudos PWA.
 * Responsável por: SW, auth, telas, navegação, modo de estudo.
 */

import { iniciarAuth, fazerLogin, fazerLogout } from './auth.js';
import { iniciarSync } from './sync.js';

// ── Estado global ───────────────────────────────────────────
const ESTADO = {
  modo: null,           // 'metro' | 'mesa' | 'carro' | null
  usuario: null,        // objeto Firebase User
  painelAtivo: 'dashboard',
  online: navigator.onLine,
};

// ── Utilitários ─────────────────────────────────────────────
let _toastTimer = null;

function mostrarToast(msg, ms = 2500) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('visivel');
  clearTimeout(_toastTimer);
  _toastTimer = setTimeout(() => t.classList.remove('visivel'), ms);
}

function mostrarTela(nome) {
  document.querySelectorAll('.tela').forEach(t => t.classList.add('oculto'));
  const el = document.getElementById(`tela-${nome}`);
  if (el) el.classList.remove('oculto');
}

// ── Service Worker ───────────────────────────────────────────
function registrarSW() {
  if (!('serviceWorker' in navigator)) return;
  navigator.serviceWorker.register('/sw.js', { scope: '/' })
    .then(reg => {
      reg.addEventListener('updatefound', () => {
        const novoSW = reg.installing;
        novoSW.addEventListener('statechange', () => {
          if (novoSW.state === 'installed' && navigator.serviceWorker.controller) {
            mostrarToast('🔄 Atualização disponível — recarregue para aplicar');
          }
        });
      });
    })
    .catch(err => console.warn('SW não registrado:', err));
}

// ── Autenticação ─────────────────────────────────────────────
function configurarLogin() {
  const btnGoogle = document.getElementById('btn-google-login');
  if (!btnGoogle) return;

  btnGoogle.addEventListener('click', async () => {
    btnGoogle.disabled = true;
    btnGoogle.innerHTML = '<span class="spinner-inline"></span> Aguarde...';
    try {
      await fazerLogin();
      // onAuthStateChanged em iniciarAuth() cuida do restante
    } catch (err) {
      console.error('Erro no login:', err);
      mostrarToast('❌ Erro ao fazer login. Tente novamente.');
      btnGoogle.disabled = false;
      btnGoogle.innerHTML = _htmlBtnGoogle();
    }
  });
}

function _htmlBtnGoogle() {
  return `
    <svg class="btn-google-logo" viewBox="0 0 24 24" aria-hidden="true">
      <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
      <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
      <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"/>
      <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
    </svg>
    Entrar com Google
  `;
}

// ── Seletor de Modo ──────────────────────────────────────────
function configurarModo() {
  document.querySelectorAll('.modo-card').forEach(card => {
    card.addEventListener('click', () => {
      const modo = card.dataset.modo;
      selecionarModo(modo);
    });
  });

  const btnPular = document.getElementById('btn-pular-modo');
  if (btnPular) {
    btnPular.addEventListener('click', () => selecionarModo(null));
  }
}

function selecionarModo(modo) {
  ESTADO.modo = modo;
  if (modo) {
    sessionStorage.setItem('sedf-modo', modo);
    document.body.dataset.modo = modo;
  } else {
    sessionStorage.removeItem('sedf-modo');
    delete document.body.dataset.modo;
  }
  iniciarApp();
}

function aplicarModo(modo) {
  ESTADO.modo = modo;
  if (modo) {
    document.body.dataset.modo = modo;
  } else {
    delete document.body.dataset.modo;
  }
  atualizarBarraModo();
}

const MODOS = {
  metro: { emoji: '🚇', nome: 'Modo Metrô — Rápido' },
  mesa:  { emoji: '🖥️', nome: 'Modo Mesa — Foco total' },
  carro: { emoji: '🚗', nome: 'Modo Carro — Só áudio' },
};

function atualizarBarraModo() {
  const icone = document.getElementById('barra-modo-icone');
  const nome  = document.getElementById('barra-modo-nome');
  if (!icone || !nome) return;

  const modo = ESTADO.modo;
  if (modo && MODOS[modo]) {
    icone.textContent = MODOS[modo].emoji;
    nome.textContent  = MODOS[modo].nome;
    document.getElementById('barra-modo')?.classList.remove('oculto');
  } else {
    document.getElementById('barra-modo')?.classList.add('oculto');
  }

  // Sidebar badge
  const badge = document.getElementById('sidebar-modo-badge');
  if (badge) badge.textContent = modo ? MODOS[modo].nome : 'Sem modo';
}

// ── Navegação entre painéis ──────────────────────────────────
function configurarNavegacao() {
  // Bottom nav + sidebar nav
  document.querySelectorAll('[data-painel]').forEach(btn => {
    btn.addEventListener('click', () => {
      navegarPara(btn.dataset.painel);
    });
  });

  // Botão "Mudar modo"
  const btnMudar = document.getElementById('btn-mudar-modo');
  if (btnMudar) {
    btnMudar.addEventListener('click', () => mostrarTela('modo'));
  }
}

function navegarPara(painel) {
  if (!painel) return;
  ESTADO.painelAtivo = painel;

  // Painéis
  document.querySelectorAll('.painel').forEach(p => {
    p.classList.toggle('ativo', p.id === `painel-${painel}`);
  });

  // Botões nav
  document.querySelectorAll('[data-painel]').forEach(btn => {
    btn.classList.toggle('ativo', btn.dataset.painel === painel);
  });

  // Scroll to top
  const painelEl = document.getElementById(`painel-${painel}`);
  if (painelEl) painelEl.scrollTop = 0;

  // Carregar módulo se necessário
  carregarModulo(painel);
}

// ── Carregamento dinâmico de módulos ─────────────────────────
const _modulosCarregados = new Set();

async function carregarModulo(painel) {
  if (_modulosCarregados.has(painel)) return;
  _modulosCarregados.add(painel);

  try {
    switch (painel) {
      case 'dashboard':
        // Dashboard é renderizado inline por agora
        renderizarDashboardPlaceholder();
        break;
      case 'estudar':
        renderizarPlaceholder('estudar', '📚', 'Banco de Resumos', 'Em desenvolvimento...');
        break;
      case 'questoes':
        renderizarPlaceholder('questoes', '❓', 'Banco de Questões', 'Em desenvolvimento...');
        break;
      case 'cronograma':
        renderizarPlaceholder('cronograma', '📅', 'Cronograma', 'Em desenvolvimento...');
        break;
      case 'config':
        renderizarPainelConfig();
        break;
    }
  } catch (err) {
    console.error(`Erro ao carregar módulo ${painel}:`, err);
  }
}

function renderizarPlaceholder(painel, emoji, titulo, sub) {
  const el = document.getElementById(`painel-${painel}`);
  if (!el) return;
  el.innerHTML = `
    <div class="painel-header" data-emoji="${emoji}">
      <div class="painel-header-titulo">${titulo}</div>
      <div class="painel-header-sub">${sub}</div>
    </div>
    <div class="estado-vazio">
      <div class="estado-vazio-emoji">${emoji}</div>
      <div class="estado-vazio-texto">Este módulo está sendo desenvolvido.<br>Em breve disponível!</div>
    </div>
  `;
}

// ── Dashboard (placeholder inicial) ─────────────────────────
function renderizarDashboardPlaceholder() {
  const el = document.getElementById('painel-dashboard');
  if (!el || el.dataset.renderizado) return;
  el.dataset.renderizado = '1';

  const usuario = ESTADO.usuario;
  const nome = usuario?.displayName?.split(' ')[0] || 'Lucas';
  const hora = new Date().getHours();
  const saudacao = hora < 5 ? 'Boa madrugada' : hora < 12 ? 'Bom dia' : hora < 18 ? 'Boa tarde' : 'Boa noite';

  el.innerHTML = `
    <div class="painel-header" data-emoji="🎵">
      <div class="painel-header-label">Dashboard</div>
      <div class="painel-header-titulo">${saudacao}, ${nome}!</div>
      <div class="painel-header-sub">SEDF — Professor de Música / CEP-EMB</div>
    </div>

    <!-- Banner sem edital -->
    <div style="margin:16px;padding:12px 16px;background:var(--cor-atencao-bg);border:1px solid var(--cor-atencao);border-radius:var(--raio-md);display:flex;align-items:center;gap:10px;font-size:13px;color:var(--cor-texto);">
      <span style="font-size:18px;">⏳</span>
      <span><strong>Concurso sem data prevista</strong> — Estudando em ciclo aberto</span>
    </div>

    <!-- Stats cards -->
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:0 16px 16px;">
      <div class="card" style="padding:14px;text-align:center;">
        <div style="font-family:var(--fonte-titulo);font-size:28px;font-weight:700;color:var(--cor-primaria);">0</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);font-weight:600;text-transform:uppercase;letter-spacing:.4px;margin-top:2px;">Questões hoje</div>
      </div>
      <div class="card" style="padding:14px;text-align:center;">
        <div style="font-family:var(--fonte-titulo);font-size:28px;font-weight:700;color:var(--cor-sucesso);">—</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);font-weight:600;text-transform:uppercase;letter-spacing:.4px;margin-top:2px;">Acerto hoje</div>
      </div>
      <div class="card" style="padding:14px;text-align:center;">
        <div style="font-family:var(--fonte-titulo);font-size:28px;font-weight:700;color:var(--cor-secundaria);">0h</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);font-weight:600;text-transform:uppercase;letter-spacing:.4px;margin-top:2px;">Tempo hoje</div>
      </div>
      <div class="card" style="padding:14px;text-align:center;">
        <div style="font-family:var(--fonte-titulo);font-size:28px;font-weight:700;color:var(--cor-acento);">0🔥</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);font-weight:600;text-transform:uppercase;letter-spacing:.4px;margin-top:2px;">Streak</div>
      </div>
    </div>

    <!-- Progresso por bloco -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header">
        <h3 class="secao-titulo">Progresso por Bloco</h3>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px;">
        ${_cardProgresso('Conhecimentos Básicos', 'CB', 'basicos', 0, 30)}
        ${_cardProgresso('Conhecimentos Complementares', 'CC', 'complementares', 0, 40)}
        ${_cardProgresso('Conhecimentos Específicos', 'CE', 'especificos', 0, 50)}
      </div>
    </div>

    <!-- Ações rápidas -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header">
        <h3 class="secao-titulo">Começar agora</h3>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <button class="card card-hover" onclick="app.navegarPara('questoes')" style="padding:16px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;">
          <span style="font-size:28px;">❓</span>
          <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">Questões</span>
          <span style="font-size:11px;color:var(--cor-texto-leve);">Treinar agora</span>
        </button>
        <button class="card card-hover" onclick="app.navegarPara('estudar')" style="padding:16px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;">
          <span style="font-size:28px;">📚</span>
          <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">Resumos</span>
          <span style="font-size:11px;color:var(--cor-texto-leve);">Estudar conteúdo</span>
        </button>
        <button class="card card-hover" onclick="app.navegarPara('cronograma')" style="padding:16px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;">
          <span style="font-size:28px;">📅</span>
          <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">Cronograma</span>
          <span style="font-size:11px;color:var(--cor-texto-leve);">Planejar estudos</span>
        </button>
        <button class="card card-hover" onclick="app.navegarPara('config')" style="padding:16px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;">
          <span style="font-size:28px;">⚙️</span>
          <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">Config.</span>
          <span style="font-size:11px;color:var(--cor-texto-leve);">Ajustes</span>
        </button>
      </div>
    </div>
  `;
}

function _cardProgresso(nome, sigla, bloco, feito, total) {
  const pct = total > 0 ? Math.round(feito / total * 100) : 0;
  const corBarra = pct >= 81 ? 'sucesso' : pct >= 70 ? 'atencao' : '';
  return `
    <div class="card" style="padding:14px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
        <div style="display:flex;align-items:center;gap:8px;">
          <span class="tag tag-bloco-${bloco}">${sigla}</span>
          <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">${nome}</span>
        </div>
        <span style="font-family:var(--fonte-titulo);font-size:15px;font-weight:700;color:var(--cor-primaria);">${pct}%</span>
      </div>
      <div class="barra-progresso-container">
        <div class="barra-progresso ${corBarra}" style="width:${pct}%"></div>
      </div>
      <div style="font-size:11px;color:var(--cor-texto-leve);margin-top:4px;">${feito} de ${total} questões respondidas</div>
    </div>
  `;
}

// ── Painel Config ────────────────────────────────────────────
function renderizarPainelConfig() {
  const el = document.getElementById('painel-config');
  if (!el || el.dataset.renderizado) return;
  el.dataset.renderizado = '1';

  const usuario = ESTADO.usuario;

  el.innerHTML = `
    <div class="painel-header" data-emoji="⚙️">
      <div class="painel-header-titulo">Configurações</div>
    </div>

    <!-- Perfil -->
    <div class="secao">
      <div class="secao-header"><h3 class="secao-titulo">Perfil</h3></div>
      <div class="card" style="padding:16px;display:flex;align-items:center;gap:14px;">
        <img class="avatar" src="${usuario?.photoURL || ''}" width="48" height="48" alt="${usuario?.displayName || 'Usuário'}">
        <div>
          <div style="font-weight:700;font-size:15px;">${usuario?.displayName || '—'}</div>
          <div style="font-size:12px;color:var(--cor-texto-leve);">${usuario?.email || '—'}</div>
        </div>
      </div>
    </div>

    <!-- Modo escuro -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Aparência</h3></div>
      <div class="card" style="padding:16px;display:flex;align-items:center;justify-content:space-between;">
        <div>
          <div style="font-weight:600;font-size:14px;">Modo Escuro</div>
          <div style="font-size:12px;color:var(--cor-texto-leve);">Reduz o brilho da tela</div>
        </div>
        <button id="toggle-dark" class="btn btn-sm" style="min-width:64px;">
          ${document.body.dataset.tema === 'escuro' ? '🌙 ON' : '☀️ OFF'}
        </button>
      </div>
    </div>

    <!-- Sobre -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Sobre</h3></div>
      <div class="card" style="padding:16px;">
        <div style="font-size:13px;color:var(--cor-texto-leve);line-height:1.7;">
          <div><strong>App:</strong> SEDF Estudos v0.1.0</div>
          <div><strong>Cargo:</strong> Professor de Educação Básica — Música</div>
          <div><strong>Escola:</strong> CEP-EMB · Concurso Público SEDF</div>
          <div style="margin-top:8px;font-size:11px;opacity:.6;">Banco de questões: provas reais (Quadrix, IADES)</div>
        </div>
      </div>
    </div>

    <!-- Logout -->
    <div class="secao" style="padding-top:0;">
      <button id="btn-logout" class="btn btn-outline btn-full" style="color:var(--cor-erro);border-color:var(--cor-erro);">
        Sair da conta
      </button>
    </div>
  `;

  // Toggle dark mode
  document.getElementById('toggle-dark')?.addEventListener('click', alternarTema);

  // Logout
  document.getElementById('btn-logout')?.addEventListener('click', async () => {
    await fazerLogout();
    location.reload();
  });
}

function alternarTema() {
  const escuro = document.body.dataset.tema === 'escuro';
  document.body.dataset.tema = escuro ? 'claro' : 'escuro';
  localStorage.setItem('sedf-tema', document.body.dataset.tema);
  const btn = document.getElementById('toggle-dark');
  if (btn) btn.textContent = document.body.dataset.tema === 'escuro' ? '🌙 ON' : '☀️ OFF';
}

// ── Perfil na sidebar ────────────────────────────────────────
function preencherPerfil(usuario) {
  const foto = document.getElementById('sidebar-foto');
  const nome = document.getElementById('sidebar-nome');
  if (foto) {
    foto.src = usuario.photoURL || '';
    foto.alt = usuario.displayName || 'Usuário';
  }
  if (nome) nome.textContent = usuario.displayName?.split(' ')[0] || 'Lucas';
}

// ── URL params ───────────────────────────────────────────────
function aplicarUrlParams() {
  const params = new URLSearchParams(location.search);
  const painel = params.get('painel');
  if (painel) navegarPara(painel);
}

// ── Tema salvo ───────────────────────────────────────────────
function carregarTema() {
  const tema = localStorage.getItem('sedf-tema') || 'claro';
  document.body.dataset.tema = tema;
}

// ── Inicialização principal ──────────────────────────────────
function iniciarApp() {
  mostrarTela('app');
  atualizarBarraModo();
  configurarNavegacao();
  iniciarSync(ESTADO);

  // Painel inicial
  const painelInicial = new URLSearchParams(location.search).get('painel') || 'dashboard';
  navegarPara(painelInicial);
}

async function iniciar() {
  carregarTema();
  registrarSW();

  // Aguarda Firebase Auth resolver
  mostrarTela('loading');
  configurarLogin();
  configurarModo();

  iniciarAuth((usuario) => {
    if (usuario) {
      ESTADO.usuario = usuario;
      preencherPerfil(usuario);

      // Recupera modo da sessão
      const modoSalvo = sessionStorage.getItem('sedf-modo');
      if (modoSalvo) {
        aplicarModo(modoSalvo);
        iniciarApp();
      } else {
        mostrarTela('modo');
      }
    } else {
      mostrarTela('login');
    }
  });
}

// ── Expõe API pública para uso inline nos painéis ────────────
window.app = {
  navegarPara,
  mostrarToast,
  alternarTema,
  get estado() { return ESTADO; },
};

// ── Inicia ───────────────────────────────────────────────────
iniciar();
