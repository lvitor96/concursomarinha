/**
 * dashboard.js — Dashboard principal com dados reais do Firestore.
 * Dados lidos: cronograma/log (streak + tempo), daily/{hoje} (questões do dia),
 * questoesStatus (progresso por bloco), questoes.json (totais por bloco).
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import { doc, getDoc, collection, getDocs } from 'firebase/firestore';

export async function iniciarDashboard() {
  const el = document.getElementById('painel-dashboard');
  if (!el) return;

  const usuario = obterUsuario();
  _renderizarEsqueleto(el, usuario);
  if (!usuario) return;

  const hoje = new Date().toISOString().slice(0, 10);

  const [logRes, dailyRes, statusRes, questoesRes] = await Promise.allSettled([
    getDoc(doc(db, 'users', usuario.uid, 'cronograma', 'log')),
    getDoc(doc(db, 'users', usuario.uid, 'daily', hoje)),
    getDocs(collection(db, 'users', usuario.uid, 'questoesStatus')),
    fetch('./data/questoes.json').then(r => r.json()),
  ]);

  const log      = logRes.status    === 'fulfilled' && logRes.value.exists()    ? logRes.value.data()    : {};
  const daily    = dailyRes.status  === 'fulfilled' && dailyRes.value.exists()  ? dailyRes.value.data()  : {};
  const statusDocs = statusRes.status === 'fulfilled' ? statusRes.value.docs : [];
  const questoes = questoesRes.status === 'fulfilled' ? (questoesRes.value.questoes ?? []) : [];

  // ── Stats ──────────────────────────────────────────────────
  const streak      = _calcularStreak(log, hoje);
  const minHoje     = log[hoje]?.minutos ?? 0;
  const respondHoje = daily.respondidas ?? 0;
  const acertosHoje = daily.acertos ?? 0;
  const acertoPct   = respondHoje > 0 ? Math.round(acertosHoje / respondHoje * 100) : null;

  // ── Progresso por bloco ────────────────────────────────────
  const blocos = ['basicos', 'complementares', 'especificos'];
  const total  = Object.fromEntries(blocos.map(b => [b, 0]));
  const feito  = Object.fromEntries(blocos.map(b => [b, 0]));

  for (const q of questoes) {
    if (total[q.bloco] !== undefined) total[q.bloco]++;
  }
  for (const d of statusDocs) {
    const data = d.data();
    if (data.respondida && feito[data.bloco] !== undefined) feito[data.bloco]++;
  }

  _atualizarStats(el, { streak, minHoje, respondHoje, acertoPct });
  _atualizarBlocos(el, { total, feito });
}

// ── Streak ─────────────────────────────────────────────────
function _calcularStreak(log, hoje) {
  const cur = new Date(hoje + 'T12:00:00');
  // Se hoje ainda não tem entrada, começa a contar a partir de ontem
  if (!log[hoje]?.minutos) cur.setDate(cur.getDate() - 1);

  let streak = 0;
  for (let i = 0; i < 366; i++) {
    const key = cur.toISOString().slice(0, 10);
    if (log[key]?.minutos > 0) {
      streak++;
      cur.setDate(cur.getDate() - 1);
    } else {
      break;
    }
  }
  return streak;
}

// ── Esqueleto imediato (sem dados) ─────────────────────────
function _renderizarEsqueleto(el, usuario) {
  const nome     = usuario?.displayName?.split(' ')[0] || 'Lucas';
  const hora     = new Date().getHours();
  const saudacao = hora < 5 ? 'Boa madrugada' : hora < 12 ? 'Bom dia' : hora < 18 ? 'Boa tarde' : 'Boa noite';

  el.innerHTML = `
    <div class="painel-header" data-emoji="🎵">
      <div class="painel-header-label">Dashboard</div>
      <div class="painel-header-titulo">${saudacao}, ${nome}!</div>
      <div class="painel-header-sub">SEDF — Professor de Música / CEP-EMB</div>
    </div>

    <div style="margin:16px 16px 0;padding:12px 16px;background:var(--cor-atencao-bg);border:1px solid var(--cor-atencao);border-radius:var(--raio-md);display:flex;align-items:center;gap:10px;font-size:13px;color:var(--cor-texto);">
      <span style="font-size:18px;">⏳</span>
      <span><strong>Concurso sem data prevista</strong> — Estudando em ciclo aberto</span>
    </div>

    <div id="dash-stats" style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:16px 16px 0;">
      ${_statCard('…', 'Questões hoje', 'var(--cor-primaria)')}
      ${_statCard('…', 'Acerto hoje', 'var(--cor-sucesso)')}
      ${_statCard('…', 'Tempo hoje', 'var(--cor-secundaria)')}
      ${_statCard('…', 'Sequência', 'var(--cor-acento)')}
    </div>

    <div id="dash-blocos" class="secao">
      <div class="secao-header"><h3 class="secao-titulo">Progresso por Bloco</h3></div>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <div class="card" style="height:70px;"></div>
        <div class="card" style="height:70px;"></div>
        <div class="card" style="height:70px;"></div>
      </div>
    </div>

    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Começar agora</h3></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding-bottom:80px;">
        ${_acaoCard('❓', 'Questões',    'Treinar agora',    'questoes')}
        ${_acaoCard('📚', 'Resumos',     'Estudar conteúdo', 'estudar')}
        ${_acaoCard('⏱️', 'Simulado',   'Prova cronometrada','simulado')}
        ${_acaoCard('📅', 'Cronograma', 'Planejar estudos', 'cronograma')}
        ${_acaoCard('📊', 'Estatísticas','Seu progresso',   'estatisticas')}
        ${_acaoCard('⚙️', 'Config.',    'Ajustes',          'config')}
      </div>
    </div>
  `;
}

// ── Atualiza apenas os cards de stats (mantém HTML do restante) ──
function _atualizarStats(el, { streak, minHoje, respondHoje, acertoPct }) {
  const statsEl = el.querySelector('#dash-stats');
  if (!statsEl) return;

  const tempoStr = minHoje >= 60
    ? `${Math.floor(minHoje / 60)}h${minHoje % 60 > 0 ? (minHoje % 60) + 'm' : ''}`
    : minHoje > 0 ? `${minHoje}m` : '0';

  statsEl.innerHTML = `
    ${_statCard(respondHoje || '0', 'Questões hoje', 'var(--cor-primaria)')}
    ${_statCard(acertoPct !== null ? acertoPct + '%' : '—', 'Acerto hoje', 'var(--cor-sucesso)')}
    ${_statCard(tempoStr, 'Tempo hoje', 'var(--cor-secundaria)')}
    ${_statCard(streak > 0 ? streak + ' 🔥' : '0', 'Sequência', 'var(--cor-acento)')}
  `;
}

// ── Atualiza as barras de progresso por bloco ─────────────
function _atualizarBlocos(el, { total, feito }) {
  const blocosEl = el.querySelector('#dash-blocos');
  if (!blocosEl) return;
  blocosEl.innerHTML = `
    <div class="secao-header"><h3 class="secao-titulo">Progresso por Bloco</h3></div>
    <div style="display:flex;flex-direction:column;gap:10px;">
      ${_barraBloco('Conhecimentos Básicos',        'CB', 'basicos',        feito.basicos,        total.basicos)}
      ${_barraBloco('Conhecimentos Complementares', 'CC', 'complementares', feito.complementares, total.complementares)}
      ${_barraBloco('Conhecimentos Específicos',    'CE', 'especificos',    feito.especificos,    total.especificos)}
    </div>
  `;
}

// ── Helpers de HTML ────────────────────────────────────────
function _statCard(valor, label, cor) {
  return `
    <div class="card" style="padding:14px;text-align:center;">
      <div style="font-family:var(--fonte-titulo);font-size:28px;font-weight:700;color:${cor};">${valor}</div>
      <div style="font-size:11px;color:var(--cor-texto-leve);font-weight:600;text-transform:uppercase;letter-spacing:.4px;margin-top:2px;">${label}</div>
    </div>`;
}

function _barraBloco(nome, sigla, bloco, qtdFeito, qtdTotal) {
  const pct = qtdTotal > 0 ? Math.round(qtdFeito / qtdTotal * 100) : 0;
  const corExtra = pct >= 81 ? 'sucesso' : pct >= 70 ? 'atencao' : '';
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
        <div class="barra-progresso ${corExtra}" style="width:${pct}%"></div>
      </div>
      <div style="font-size:11px;color:var(--cor-texto-leve);margin-top:4px;">${qtdFeito} de ${qtdTotal} questões respondidas</div>
    </div>`;
}

function _acaoCard(emoji, titulo, sub, painel) {
  return `
    <button class="card card-hover" onclick="app.navegarPara('${painel}')"
      style="padding:16px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;border:none;cursor:pointer;background:var(--cor-fundo-card);width:100%;">
      <span style="font-size:28px;">${emoji}</span>
      <span style="font-size:13px;font-weight:600;color:var(--cor-texto);">${titulo}</span>
      <span style="font-size:11px;color:var(--cor-texto-leve);">${sub}</span>
    </button>`;
}
