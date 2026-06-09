/**
 * simulado.js — Prova cronometrada com navegação livre entre questões.
 * Histórico salvo em users/{uid}/simulados (Firestore).
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import {
  collection, addDoc, getDocs, serverTimestamp,
  query, orderBy, limit,
} from 'firebase/firestore';

/* ── Estado ─────────────────────────────────────────────────── */
const M = {
  todos:    [],
  config: {
    blocos:  ['basicos', 'complementares', 'especificos'],
    qtd:     'todos',
    minutos: 210,
  },
  sessao:   null,   // { questoes, respostas, atual, tempoTotal, tempoRestante, timerInterval }
  vista:    'home',
  historico: [],
};

/* ── Entry point ─────────────────────────────────────────────── */
export async function iniciarSimulado() {
  const el = document.getElementById('painel-simulado');
  if (!el) return;

  if (!M.todos.length) {
    const r = await fetch('./data/questoes.json');
    const d = await r.json();
    M.todos = d.questoes ?? [];
  }

  await _carregarHistorico();
  _renderizarVista(el);
}

/* ── Histórico Firestore ─────────────────────────────────────── */
async function _carregarHistorico() {
  const usuario = obterUsuario();
  if (!usuario) return;
  try {
    const q = query(
      collection(db, 'users', usuario.uid, 'simulados'),
      orderBy('data', 'desc'),
      limit(5)
    );
    const snap = await getDocs(q);
    M.historico = snap.docs.map(d => ({ id: d.id, ...d.data() }));
  } catch {
    M.historico = [];
  }
}

async function _salvarResultado(stats) {
  const usuario = obterUsuario();
  if (!usuario) return;
  try {
    await addDoc(collection(db, 'users', usuario.uid, 'simulados'), {
      data:       serverTimestamp(),
      total:      stats.total,
      respondidas: stats.respondidas,
      acertos:    stats.acertos,
      pct:        stats.pct,
      tempoUsado: stats.tempoUsado,
      porBloco:   stats.porBloco,
      config:     { blocos: M.config.blocos, qtd: M.config.qtd, minutos: M.config.minutos },
    });
  } catch {
    // offline — não bloqueia o fluxo
  }
}

/* ── Router ──────────────────────────────────────────────────── */
function _renderizarVista(el) {
  switch (M.vista) {
    case 'home':      _renderHome(el);      break;
    case 'prova':     _renderProva(el);     break;
    case 'resultado': _renderResultado(el); break;
  }
  el.scrollTop = 0;
}

/* ════════════════════════════════════════════════════════════════
   VIEW: HOME
   ════════════════════════════════════════════════════════════════ */
function _renderHome(el) {
  const porBloco = { basicos: 0, complementares: 0, especificos: 0 };
  M.todos.forEach(q => { if (porBloco[q.bloco] !== undefined) porBloco[q.bloco]++; });
  const total = M.todos.length;

  el.innerHTML = `
    <div class="painel-header" data-emoji="⏱️">
      <div class="painel-header-label">Simulado</div>
      <div class="painel-header-titulo">Prova cronometrada</div>
      <div class="painel-header-sub">${total} questões disponíveis</div>
    </div>

    <div class="sim-config">
      <div class="sim-config-titulo">Configurar simulado</div>

      <div>
        <label style="display:block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.4px;color:var(--cor-texto-leve);margin-bottom:6px;">Blocos</label>
        <div class="sim-blocos">
          <button class="sim-bloco-toggle" data-bloco="basicos">Básicos (${porBloco.basicos})</button>
          <button class="sim-bloco-toggle" data-bloco="complementares">Complementares (${porBloco.complementares})</button>
          <button class="sim-bloco-toggle" data-bloco="especificos">Específicos (${porBloco.especificos})</button>
        </div>
      </div>

      <div class="sim-config-row">
        <div class="sim-campo">
          <label>Questões</label>
          <select id="sim-sel-qtd">
            <option value="todos">Todas (${total})</option>
            <option value="50">50 questões</option>
            <option value="30">30 questões</option>
            <option value="20">20 questões</option>
          </select>
        </div>
        <div class="sim-campo">
          <label>Tempo</label>
          <select id="sim-sel-tempo">
            <option value="210">3h30 (padrão)</option>
            <option value="120">2h00</option>
            <option value="60">1h00</option>
            <option value="45">45 min</option>
            <option value="30">30 min</option>
          </select>
        </div>
      </div>

      <button class="btn btn-primario btn-full" id="sim-btn-iniciar">▶ Iniciar simulado</button>
    </div>

    <div class="secao">
      <div class="secao-header"><h3 class="secao-titulo">Últimos simulados</h3></div>
      <div class="sim-historico">
        ${M.historico.length
          ? M.historico.map(h => _htmlHistItem(h)).join('')
          : '<p class="sim-hist-vazio">Nenhum simulado realizado ainda.<br>Configure acima e comece!</p>'}
      </div>
    </div>
  `;

  // Sync toggle states to M.config.blocos
  el.querySelectorAll('.sim-bloco-toggle').forEach(btn => {
    const b = btn.dataset.bloco;
    btn.classList.toggle('ativo', M.config.blocos.includes(b));
    btn.addEventListener('click', () => {
      if (M.config.blocos.includes(b)) {
        if (M.config.blocos.length === 1) return;
        M.config.blocos = M.config.blocos.filter(x => x !== b);
      } else {
        M.config.blocos = [...M.config.blocos, b];
      }
      btn.classList.toggle('ativo', M.config.blocos.includes(b));
    });
  });

  el.querySelector('#sim-btn-iniciar').addEventListener('click', () => {
    M.config.qtd     = el.querySelector('#sim-sel-qtd').value;
    M.config.minutos = parseInt(el.querySelector('#sim-sel-tempo').value, 10);
    _iniciarSessao(el);
  });
}

function _htmlHistItem(h) {
  const pct  = h.pct ?? 0;
  const cor  = pct >= 81 ? 'var(--cor-sucesso)' : pct >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)';
  const data = h.data?.toDate
    ? h.data.toDate().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric' })
    : '—';
  const blocos = h.porBloco
    ? Object.entries(h.porBloco)
        .filter(([, d]) => d.total > 0)
        .map(([b, d]) => `${_sigla(b)} ${Math.round(d.acertos / d.total * 100)}%`)
        .join(' · ')
    : '';
  return `
    <div class="sim-hist-item">
      <div class="sim-hist-pct" style="color:${cor};">${pct}%</div>
      <div class="sim-hist-info">
        <div class="sim-hist-data">${data} · ${h.total} questões · ${_formatarTempo(h.tempoUsado ?? 0)}</div>
        <div class="sim-hist-detalhe">${blocos}</div>
      </div>
    </div>`;
}

/* ════════════════════════════════════════════════════════════════
   INICIAR SESSÃO
   ════════════════════════════════════════════════════════════════ */
function _iniciarSessao(el) {
  let pool = M.todos.filter(q => M.config.blocos.includes(q.bloco));
  pool = _embaralhar(pool);
  if (M.config.qtd !== 'todos') pool = pool.slice(0, parseInt(M.config.qtd, 10));

  if (!pool.length) {
    window.app?.mostrarToast('Nenhuma questão disponível com essa configuração.');
    return;
  }

  _pararTimer();
  M.sessao = {
    questoes:      pool,
    respostas:     {},
    atual:         0,
    tempoTotal:    M.config.minutos * 60,
    tempoRestante: M.config.minutos * 60,
    timerInterval: null,
  };
  M.vista = 'prova';
  _renderizarVista(el);
  _iniciarTimer(el);
}

/* ════════════════════════════════════════════════════════════════
   VIEW: PROVA
   ════════════════════════════════════════════════════════════════ */
function _renderProva(el) {
  const s = M.sessao;
  const respondidas = Object.keys(s.respostas).length;

  el.innerHTML = `
    <!-- Header: timer + progresso + encerrar -->
    <div class="sim-prova-header">
      <div class="sim-timer" id="sim-timer">${_formatarTempo(s.tempoRestante)}</div>
      <div class="sim-progresso-wrap">
        <div class="sim-progresso-label">${respondidas} de ${s.questoes.length} respondidas</div>
        <div class="sim-progresso-barra">
          <div class="sim-progresso-fill" id="sim-fill" style="width:${Math.round(respondidas / s.questoes.length * 100)}%"></div>
        </div>
      </div>
      <button class="btn btn-outline btn-sm" id="sim-btn-encerrar" style="flex-shrink:0;font-size:11px;white-space:nowrap;">Encerrar</button>
    </div>

    <!-- Mapa de questões -->
    <div class="sim-mapa-scroll" id="sim-mapa">
      ${s.questoes.map((q, i) => `
        <button class="sim-mapa-btn ${s.respostas[q.id] ? 'respondida' : ''} ${i === s.atual ? 'atual' : ''}" data-idx="${i}">${i + 1}</button>
      `).join('')}
    </div>

    <!-- Área da questão -->
    <div class="sim-questao-area" id="sim-questao-area">
      ${_htmlQuestao(s.questoes[s.atual], s.atual)}
    </div>
  `;

  _bindProva(el);
  _scrollMapaParaAtual(el);
}

function _htmlQuestao(q, idx) {
  const s      = M.sessao;
  const marcada = s.respostas[q.id];
  const total  = s.questoes.length;
  return `
    <div class="sim-questao-meta">
      <span class="sim-questao-num">Questão ${idx + 1} de ${total}</span>
      <span class="tag tag-bloco-${q.bloco}">${_sigla(q.bloco)}</span>
      <span class="sim-questao-origem">${q.banca ?? ''}${q.ano ? ' · ' + q.ano : ''}</span>
    </div>

    <div class="sim-enunciado">${q.enunciado}</div>

    <div class="sim-alts">
      ${Object.entries(q.alternativas).map(([letra, texto]) => `
        <button class="sim-alt ${marcada === letra ? 'marcada' : ''}" data-alt="${letra}">
          <span class="sim-alt-letra">${letra}</span>
          <span class="sim-alt-texto">${texto}</span>
        </button>
      `).join('')}
    </div>

    <div class="sim-nav-btns">
      <button class="btn btn-outline" style="flex:1;" id="sim-prev" ${idx === 0 ? 'disabled' : ''}>← Anterior</button>
      <button class="btn btn-outline" style="flex:1;" id="sim-next" ${idx === total - 1 ? 'disabled' : ''}>Próxima →</button>
    </div>

    ${idx === total - 1
      ? `<button class="sim-btn-submit" id="sim-submit">✅ Entregar prova</button>`
      : ''}
  `;
}

function _bindProva(el) {
  const area = el.querySelector('#sim-questao-area');

  // Alternativas
  area.addEventListener('click', e => {
    const altBtn = e.target.closest('[data-alt]');
    if (altBtn) {
      const q = M.sessao.questoes[M.sessao.atual];
      M.sessao.respostas[q.id] = altBtn.dataset.alt;
      area.innerHTML = _htmlQuestao(q, M.sessao.atual);
      _atualizarMapa(el);
      _atualizarProgressoBar(el);
      return;
    }
    if (e.target.closest('#sim-prev'))   { _irPara(el, M.sessao.atual - 1); return; }
    if (e.target.closest('#sim-next'))   { _irPara(el, M.sessao.atual + 1); return; }
    if (e.target.closest('#sim-submit')) { _confirmarEntrega(el); }
  });

  // Mapa
  el.querySelector('#sim-mapa').addEventListener('click', e => {
    const btn = e.target.closest('[data-idx]');
    if (btn) _irPara(el, parseInt(btn.dataset.idx, 10));
  });

  // Encerrar
  el.querySelector('#sim-btn-encerrar').addEventListener('click', () => _confirmarEntrega(el));
}

function _irPara(el, idx) {
  const s = M.sessao;
  if (idx < 0 || idx >= s.questoes.length) return;
  s.atual = idx;
  const area = el.querySelector('#sim-questao-area');
  if (area) {
    area.innerHTML = _htmlQuestao(s.questoes[idx], idx);
    el.scrollTop = 0;
  }
  _atualizarMapa(el);
}

function _atualizarMapa(el) {
  const s = M.sessao;
  el.querySelectorAll('#sim-mapa [data-idx]').forEach(btn => {
    const i = parseInt(btn.dataset.idx, 10);
    const q = s.questoes[i];
    btn.className = [
      'sim-mapa-btn',
      s.respostas[q.id] ? 'respondida' : '',
      i === s.atual ? 'atual' : '',
    ].filter(Boolean).join(' ');
  });
  _scrollMapaParaAtual(el);
}

function _atualizarProgressoBar(el) {
  const s = M.sessao;
  const n = Object.keys(s.respostas).length;
  const label = el.querySelector('.sim-progresso-label');
  const fill  = el.querySelector('#sim-fill');
  if (label) label.textContent = `${n} de ${s.questoes.length} respondidas`;
  if (fill)  fill.style.width  = `${Math.round(n / s.questoes.length * 100)}%`;
}

function _scrollMapaParaAtual(el) {
  const btn = el.querySelector(`#sim-mapa [data-idx="${M.sessao.atual}"]`);
  btn?.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
}

/* ── Timer ───────────────────────────────────────────────────── */
function _iniciarTimer(el) {
  M.sessao.timerInterval = setInterval(() => {
    M.sessao.tempoRestante--;
    const timerEl = el.querySelector('#sim-timer');
    if (timerEl) {
      timerEl.textContent = _formatarTempo(M.sessao.tempoRestante);
      const t = M.sessao.tempoRestante;
      timerEl.className = 'sim-timer' + (t <= 600 ? ' urgente' : t <= 1800 ? ' aviso' : '');
    }
    if (M.sessao.tempoRestante <= 0) {
      _pararTimer();
      window.app?.mostrarToast('⏰ Tempo esgotado! Encerrando prova…');
      setTimeout(() => _encerrarProva(el), 1500);
    }
  }, 1000);
}

function _pararTimer() {
  if (M.sessao?.timerInterval) {
    clearInterval(M.sessao.timerInterval);
    M.sessao.timerInterval = null;
  }
}

/* ── Entrega ─────────────────────────────────────────────────── */
function _confirmarEntrega(el) {
  const naoresp = M.sessao.questoes.length - Object.keys(M.sessao.respostas).length;
  if (naoresp > 0) {
    if (!confirm(`Você ainda tem ${naoresp} questão(ões) sem resposta. Deseja entregar assim mesmo?`)) return;
  }
  _encerrarProva(el);
}

function _encerrarProva(el) {
  _pararTimer();
  const stats = _calcularStats();
  _salvarResultado(stats);
  M.vista = 'resultado';
  _renderizarVista(el);
}

/* ── Cálculo de estatísticas ─────────────────────────────────── */
function _calcularStats() {
  const s = M.sessao;
  let acertos = 0;
  const porBloco = {};

  s.questoes.forEach(q => {
    if (!porBloco[q.bloco]) porBloco[q.bloco] = { total: 0, acertos: 0 };
    porBloco[q.bloco].total++;
    const r = s.respostas[q.id];
    if (r && r === q.gabarito) { acertos++; porBloco[q.bloco].acertos++; }
  });

  const respondidas = Object.keys(s.respostas).length;
  const pct         = respondidas > 0 ? Math.round(acertos / respondidas * 100) : 0;
  const tempoUsado  = s.tempoTotal - s.tempoRestante;

  return { total: s.questoes.length, respondidas, acertos, pct, tempoUsado, porBloco };
}

/* ════════════════════════════════════════════════════════════════
   VIEW: RESULTADO
   ════════════════════════════════════════════════════════════════ */
function _renderResultado(el) {
  const s     = M.sessao;
  const stats = _calcularStats();
  const { total, respondidas, acertos, pct, tempoUsado, porBloco } = stats;
  const naoresp = total - respondidas;
  const emoji   = pct >= 81 ? '🟢' : pct >= 70 ? '🟡' : '🔴';
  const titulo  = pct >= 81 ? 'Ótimo resultado!' : pct >= 70 ? 'Quase lá!' : 'Continue estudando!';

  const htmlBlocos = Object.entries(porBloco).map(([bloco, d]) => {
    const p   = d.total > 0 ? Math.round(d.acertos / d.total * 100) : 0;
    const cor = p >= 81 ? 'var(--cor-sucesso)' : p >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)';
    return `
      <div class="q-relatorio-item">
        <span class="tag tag-bloco-${bloco}" style="flex-shrink:0;">${_sigla(bloco)}</span>
        <div class="q-relatorio-item-nome">${_nomeBloco(bloco)}</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);">${d.acertos}/${d.total}</div>
        <div class="q-relatorio-item-pct" style="color:${cor};">${p}%</div>
      </div>`;
  }).join('');

  const htmlGabarito = s.questoes.map((q, i) => {
    const r      = s.respostas[q.id];
    const correta = r === q.gabarito;
    const ico    = !r ? '⬜' : correta ? '✅' : '❌';
    return `
      <div class="q-relatorio-item">
        <span style="font-size:13px;flex-shrink:0;">${ico}</span>
        <div class="q-relatorio-item-nome" style="font-size:12px;">${i + 1}. ${q.enunciado.slice(0, 55)}…</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);flex-shrink:0;">${r ? `${r} → ${q.gabarito}` : `Gab: ${q.gabarito}`}</div>
      </div>`;
  }).join('');

  el.innerHTML = `
    <div class="sim-resultado-header">
      <div class="sim-resultado-emoji">${emoji}</div>
      <div class="sim-resultado-titulo">${titulo}</div>
      <div class="sim-resultado-pct">${pct}%</div>
      <div class="sim-resultado-sub">${acertos} de ${respondidas} corretas · ${_formatarTempo(tempoUsado)}</div>
    </div>

    <div class="sim-resultado-body">

      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Resumo</div>
        <div class="q-relatorio-item">
          <span style="font-size:16px;">✅</span>
          <div class="q-relatorio-item-nome">Acertos</div>
          <div class="q-relatorio-item-pct" style="color:var(--cor-sucesso);">${acertos}</div>
        </div>
        <div class="q-relatorio-item">
          <span style="font-size:16px;">❌</span>
          <div class="q-relatorio-item-nome">Erros</div>
          <div class="q-relatorio-item-pct" style="color:var(--cor-erro);">${respondidas - acertos}</div>
        </div>
        ${naoresp > 0 ? `
        <div class="q-relatorio-item">
          <span style="font-size:16px;">⬜</span>
          <div class="q-relatorio-item-nome">Não respondidas</div>
          <div class="q-relatorio-item-pct" style="color:var(--cor-texto-leve);">${naoresp}</div>
        </div>` : ''}
        <div class="q-relatorio-item">
          <span style="font-size:16px;">⏱️</span>
          <div class="q-relatorio-item-nome">Tempo usado</div>
          <div class="q-relatorio-item-pct">${_formatarTempo(tempoUsado)}</div>
        </div>
      </div>

      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Desempenho por bloco</div>
        ${htmlBlocos}
      </div>

      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Gabarito — questão por questão</div>
        ${htmlGabarito}
      </div>

      <div style="display:flex;gap:10px;">
        <button class="btn btn-outline" style="flex:1;" id="sim-btn-novo">Novo simulado</button>
        <button class="btn btn-primario" style="flex:1;" id="sim-btn-revisar">Revisar erros</button>
      </div>

    </div>
  `;

  el.querySelector('#sim-btn-novo').addEventListener('click', async () => {
    M.vista = 'home';
    await _carregarHistorico();
    _renderizarVista(el);
  });

  el.querySelector('#sim-btn-revisar').addEventListener('click', () => {
    const erros = s.questoes.filter(q => {
      const r = s.respostas[q.id];
      return !r || r !== q.gabarito;
    });
    if (!erros.length) {
      window.app?.mostrarToast('Parabéns! Nenhum erro para revisar! 🎉');
      return;
    }
    _pararTimer();
    const tempoRevisao = erros.length * 3 * 60;
    M.sessao = {
      questoes:      erros,
      respostas:     {},
      atual:         0,
      tempoTotal:    tempoRevisao,
      tempoRestante: tempoRevisao,
      timerInterval: null,
    };
    M.vista = 'prova';
    _renderizarVista(el);
    _iniciarTimer(el);
  });
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _embaralhar(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function _formatarTempo(seg) {
  const h = Math.floor(seg / 3600);
  const m = Math.floor((seg % 3600) / 60);
  const s = seg % 60;
  if (h > 0) return `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function _sigla(b) {
  return { basicos: 'CB', complementares: 'CC', especificos: 'CE' }[b] ?? b;
}

function _nomeBloco(b) {
  return {
    basicos:        'Conhecimentos Básicos',
    complementares: 'Conhecimentos Complementares',
    especificos:    'Conhecimentos Específicos',
  }[b] ?? b;
}
