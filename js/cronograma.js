/**
 * cronograma.js — Módulo Cronograma.
 * Três vistas: Kanban (status dos tópicos) · Log (registro de sessão) · Agenda (visão semanal).
 *
 * Firestore:
 *   users/{uid}/cronograma/kanban  → { [topicoId]: coluna }
 *   users/{uid}/cronograma/log     → { [YYYY-MM-DD]: { minutos, sessoes:[{topicoId,minutos,obs}] } }
 */

import { db } from './firebase.js';
import { doc, getDoc, setDoc, serverTimestamp } from 'firebase/firestore';

// ── Estado ───────────────────────────────────────────────────
const M = {
  topicos:      [],   // [{ id, nome, incidencia, bloco, blocoSigla, disciplina, disciplinaNome }]
  kanban:       {},   // { [topicoId]: 'para-estudar'|'em-estudo'|'revisao'|'dominado' }
  log:          {},   // { [YYYY-MM-DD]: { minutos, sessoes:[...] } }
  vista:        'kanban',
  buscaKanban:  '',
  semanaOffset: 0,    // 0 = semana atual
  diaAtivo:     null, // string 'YYYY-MM-DD'
};

const COLUNAS = [
  { id: 'para-estudar', label: 'Para Estudar', emoji: '📋' },
  { id: 'em-estudo',    label: 'Em Estudo',    emoji: '📖' },
  { id: 'revisao',      label: 'Revisão',      emoji: '🔄' },
  { id: 'dominado',     label: 'Dominado',     emoji: '✅' },
];

// ── Entrada ──────────────────────────────────────────────────
export async function iniciarCronograma() {
  const painel = document.getElementById('painel-cronograma');
  if (!painel) return;

  try {
    const resp = await fetch('./data/topicos.json');
    const data = await resp.json();
    M.topicos = _flatTopicos(data);
  } catch {
    painel.innerHTML = `<div class="estado-vazio"><div class="estado-vazio-emoji">⚠️</div><div class="estado-vazio-texto">Erro ao carregar dados.</div></div>`;
    return;
  }

  M.diaAtivo = _hoje();

  await Promise.all([_carregarKanban(), _carregarLog()]);

  _renderizar();
}

// ── Firestore ────────────────────────────────────────────────
async function _carregarKanban() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    const snap = await getDoc(doc(db, 'users', uid, 'cronograma', 'kanban'));
    if (snap.exists()) {
      const d = snap.data();
      delete d._ts;
      M.kanban = d;
    }
  } catch { /* offline ok */ }
}

async function _salvarKanban() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    await setDoc(doc(db, 'users', uid, 'cronograma', 'kanban'),
      { ...M.kanban, _ts: serverTimestamp() });
  } catch { /* offline — Firestore sincroniza depois */ }
}

async function _carregarLog() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    const snap = await getDoc(doc(db, 'users', uid, 'cronograma', 'log'));
    if (snap.exists()) {
      const d = snap.data();
      delete d._ts;
      M.log = d;
    }
  } catch { /* offline ok */ }
}

async function _salvarLog() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    await setDoc(doc(db, 'users', uid, 'cronograma', 'log'),
      { ...M.log, _ts: serverTimestamp() });
  } catch { /* offline ok */ }
}

// ── Renderização principal ───────────────────────────────────
function _renderizar() {
  const painel = document.getElementById('painel-cronograma');
  if (!painel) return;

  const clone = painel.cloneNode(false);
  painel.parentNode.replaceChild(clone, painel);

  clone.innerHTML = `
    <div class="painel-header" data-emoji="📅">
      <div class="painel-header-label">Cronograma</div>
      <div class="painel-header-titulo">Planejamento</div>
      <div class="painel-header-sub">Kanban de tópicos · Log de sessões · Agenda semanal</div>
    </div>

    <div class="cron-tabs" id="cron-tabs">
      <button class="cron-tab ${M.vista==='kanban' ? 'ativo':''}" data-vista="kanban">📋 Kanban</button>
      <button class="cron-tab ${M.vista==='log'    ? 'ativo':''}" data-vista="log">✏️ Log</button>
      <button class="cron-tab ${M.vista==='agenda' ? 'ativo':''}" data-vista="agenda">📅 Agenda</button>
    </div>

    <div id="cron-corpo" style="display:flex;flex-direction:column;flex:1;overflow:hidden;"></div>
  `;

  // Tabs
  clone.querySelectorAll('.cron-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      M.vista = tab.dataset.vista;
      clone.querySelectorAll('.cron-tab').forEach(t => t.classList.remove('ativo'));
      tab.classList.add('ativo');
      _renderizarVista();
    });
  });

  _renderizarVista();
}

function _renderizarVista() {
  const corpo = document.getElementById('cron-corpo');
  if (!corpo) return;

  switch (M.vista) {
    case 'kanban': _renderizarKanban(corpo); break;
    case 'log':    _renderizarLog(corpo);    break;
    case 'agenda': _renderizarAgenda(corpo); break;
  }
}

// ── Vista: KANBAN ────────────────────────────────────────────
function _renderizarKanban(corpo) {
  corpo.innerHTML = `
    <div class="cron-busca-wrap">
      <input id="cron-busca" class="cron-busca" type="search"
        placeholder="Filtrar tópicos..." value="${_esc(M.buscaKanban)}" autocomplete="off">
    </div>
    <div class="cron-kanban-scroll" id="cron-kanban">
      ${COLUNAS.map(col => _htmlColuna(col)).join('')}
    </div>
  `;

  corpo.querySelector('#cron-busca').addEventListener('input', e => {
    M.buscaKanban = e.target.value;
    _atualizarKanban();
  });

  _bindMoveBtns(corpo);
}

function _htmlColuna(col) {
  const topicos = _topicosDaColuna(col.id);
  return `
    <div class="cron-coluna cron-col-${col.id}">
      <div class="cron-col-header">
        <span>${col.emoji}</span>
        <span>${col.label}</span>
        <span class="cron-col-count">${topicos.length}</span>
      </div>
      <div class="cron-col-cards" id="cards-${col.id}">
        ${topicos.length
          ? topicos.map(t => _htmlCard(t, col.id)).join('')
          : `<div class="cron-col-vazia">Nenhum tópico aqui</div>`}
      </div>
    </div>
  `;
}

function _topicosDaColuna(colId) {
  const busca = M.buscaKanban.trim().toLowerCase();
  return M.topicos.filter(t => {
    const colAtual = M.kanban[t.id] || 'para-estudar';
    const nomeOk = !busca || t.nome.toLowerCase().includes(busca) || t.disciplinaNome.toLowerCase().includes(busca);
    return colAtual === colId && nomeOk;
  });
}

function _htmlCard(t, colAtual) {
  const idx = COLUNAS.findIndex(c => c.id === colAtual);
  const podeEsq = idx > 0;
  const podeDir = idx < COLUNAS.length - 1;
  const labelEsq = podeEsq ? `← ${COLUNAS[idx-1].label}` : '';
  const labelDir = podeDir ? `${COLUNAS[idx+1].label} →` : '';

  return `
    <div class="cron-card" data-id="${t.id}" data-col="${colAtual}">
      <div class="cron-card-nome">${_esc(t.nome)}</div>
      <div class="cron-card-meta">
        <span class="tag tag-bloco-${t.bloco}">${t.blocoSigla}</span>
        <span class="cron-inc ${t.incidencia}">${t.incidencia}</span>
      </div>
      <div class="cron-move-btns">
        <button class="cron-move-btn cron-btn-esq" data-id="${t.id}"
          ${podeEsq ? '' : 'disabled'}>${labelEsq || '←'}</button>
        <button class="cron-move-btn cron-btn-dir" data-id="${t.id}"
          ${podeDir ? '' : 'disabled'}>${labelDir || '→'}</button>
      </div>
    </div>
  `;
}

function _bindMoveBtns(corpo) {
  corpo.addEventListener('click', async e => {
    const btnEsq = e.target.closest('.cron-btn-esq');
    const btnDir = e.target.closest('.cron-btn-dir');
    const btn = btnEsq || btnDir;
    if (!btn || btn.disabled) return;

    const id = btn.dataset.id;
    const colAtual = M.kanban[id] || 'para-estudar';
    const idx = COLUNAS.findIndex(c => c.id === colAtual);

    let novoIdx;
    if (btnEsq && idx > 0)                    novoIdx = idx - 1;
    else if (btnDir && idx < COLUNAS.length-1) novoIdx = idx + 1;
    else return;

    M.kanban[id] = COLUNAS[novoIdx].id;
    _atualizarKanban();
    _salvarKanban();
    window.app?.mostrarToast(`Movido para ${COLUNAS[novoIdx].label}`);
  });
}

function _atualizarKanban() {
  COLUNAS.forEach(col => {
    const container = document.getElementById(`cards-${col.id}`);
    if (!container) return;
    const topicos = _topicosDaColuna(col.id);

    // Atualiza contador na header
    const header = container.closest('.cron-coluna')?.querySelector('.cron-col-count');
    if (header) header.textContent = topicos.length;

    container.innerHTML = topicos.length
      ? topicos.map(t => _htmlCard(t, col.id)).join('')
      : `<div class="cron-col-vazia">Nenhum tópico aqui</div>`;
  });
}

// ── Vista: LOG ───────────────────────────────────────────────
function _renderizarLog(corpo) {
  const hoje = _hoje();

  // Select de tópicos
  const optsTopicos = M.topicos.map(t =>
    `<option value="${t.id}">[${t.blocoSigla}] ${t.nome}</option>`
  ).join('');

  // Entradas recentes (últimos 30 dias com registro)
  const dias = Object.keys(M.log).sort().reverse().slice(0, 30);

  corpo.innerHTML = `
    <div style="overflow-y:auto;flex:1;">
      <!-- Formulário de registro -->
      <div class="cron-log-form">
        <div class="cron-form-row">
          <div class="cron-field">
            <label>Data</label>
            <input type="date" id="log-data" value="${hoje}" max="${hoje}">
          </div>
          <div class="cron-field">
            <label>Duração</label>
            <select id="log-min">
              <option value="15">15 min</option>
              <option value="30">30 min</option>
              <option value="45">45 min</option>
              <option value="60" selected>1 hora</option>
              <option value="90">1h 30</option>
              <option value="120">2 horas</option>
              <option value="180">3 horas</option>
            </select>
          </div>
        </div>
        <div class="cron-field">
          <label>Tópico estudado</label>
          <select id="log-topico">
            <option value="">— Selecione o tópico —</option>
            ${optsTopicos}
          </select>
        </div>
        <div class="cron-field">
          <label>Observação (opcional)</label>
          <textarea id="log-obs" placeholder="Ex.: Reli o capítulo 3, fiz 10 questões…"></textarea>
        </div>
        <button id="log-salvar" class="btn btn-primario btn-full">✅ Registrar sessão</button>
      </div>

      <!-- Entradas -->
      <div class="cron-log-entries" id="cron-log-lista">
        ${dias.length ? dias.map(d => _htmlLogDia(d)).join('') : `<p class="cron-log-vazio">Nenhuma sessão registrada ainda.<br>Use o formulário acima para começar!</p>`}
      </div>
    </div>
  `;

  corpo.querySelector('#log-salvar').addEventListener('click', async () => {
    const data   = corpo.querySelector('#log-data').value;
    const minStr = corpo.querySelector('#log-min').value;
    const topId  = corpo.querySelector('#log-topico').value;
    const obs    = corpo.querySelector('#log-obs').value.trim();

    if (!topId) { window.app?.mostrarToast('Selecione um tópico!'); return; }

    const minutos = parseInt(minStr, 10);
    if (!M.log[data]) M.log[data] = { minutos: 0, sessoes: [] };
    M.log[data].minutos += minutos;
    M.log[data].sessoes.push({ topicoId: topId, minutos, obs });

    await _salvarLog();
    window.app?.mostrarToast(`✅ ${minutos}min registrados!`);

    // Reseta form
    corpo.querySelector('#log-topico').value = '';
    corpo.querySelector('#log-obs').value    = '';

    // Atualiza lista
    const lista = document.getElementById('cron-log-lista');
    if (lista) {
      const dias = Object.keys(M.log).sort().reverse().slice(0, 30);
      lista.innerHTML = dias.map(d => _htmlLogDia(d)).join('');
    }
  });
}

function _htmlLogDia(data) {
  const entrada = M.log[data];
  if (!entrada) return '';
  const label = _formatarData(data);
  const total = entrada.minutos || 0;
  const sessoes = (entrada.sessoes || []).map(s => {
    const t = M.topicos.find(x => x.id === s.topicoId);
    const nome = t ? t.nome : s.topicoId;
    return `
      <div class="cron-sessao">
        <span class="cron-sessao-mins">${s.minutos}min</span>
        <div class="cron-sessao-info">
          <div class="cron-sessao-topico">${_esc(nome)}</div>
          ${s.obs ? `<div class="cron-sessao-obs">${_esc(s.obs)}</div>` : ''}
        </div>
      </div>`;
  }).join('');

  return `
    <div class="cron-log-dia">
      <div class="cron-log-dia-header">
        <span class="cron-log-dia-data">${label}</span>
        <span class="cron-log-dia-total">⏱ ${_formatarMinutos(total)}</span>
      </div>
      ${sessoes}
    </div>`;
}

// ── Vista: AGENDA ────────────────────────────────────────────
function _renderizarAgenda(corpo) {
  corpo.innerHTML = `
    <div class="cron-semana-nav">
      <button class="cron-nav-btn" id="sem-prev">‹ Anterior</button>
      <span class="cron-semana-label" id="sem-label"></span>
      <button class="cron-nav-btn" id="sem-next">Próxima ›</button>
    </div>
    <div class="cron-agenda-grid" id="cron-agenda-grid"></div>
    <div class="cron-agenda-detalhe" id="cron-agenda-detalhe"></div>
  `;

  corpo.querySelector('#sem-prev').addEventListener('click', () => {
    M.semanaOffset--;
    _renderizarGradeAgenda();
  });
  corpo.querySelector('#sem-next').addEventListener('click', () => {
    if (M.semanaOffset < 0) { M.semanaOffset++; _renderizarGradeAgenda(); }
  });

  _renderizarGradeAgenda();
}

function _renderizarGradeAgenda() {
  const grid    = document.getElementById('cron-agenda-grid');
  const label   = document.getElementById('sem-label');
  const detalhe = document.getElementById('cron-agenda-detalhe');
  if (!grid || !label) return;

  const diasSemana = _diasDaSemana(M.semanaOffset);
  const hoje = _hoje();

  label.textContent = _labelSemana(diasSemana);

  // Botão próxima semana habilitado só se offset < 0
  const btnNext = document.getElementById('sem-next');
  if (btnNext) btnNext.disabled = M.semanaOffset >= 0;

  grid.innerHTML = diasSemana.map(d => {
    const temLog   = !!M.log[d];
    const isHoje   = d === hoje;
    const isAtivo  = d === M.diaAtivo;
    const mins     = M.log[d]?.minutos || 0;
    const [,, dia] = d.split('-');
    const semana   = ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'][new Date(d + 'T12:00').getDay()];

    return `
      <button class="cron-dia-card ${isHoje?'hoje':''} ${isAtivo?'ativo':''} ${temLog?'tem-log':''}"
        data-dia="${d}">
        <span class="cron-dia-semana">${semana}</span>
        <span class="cron-dia-num">${parseInt(dia,10)}</span>
        ${temLog ? `<span class="cron-dia-pip"></span>` : '<span style="height:5px"></span>'}
      </button>`;
  }).join('');

  grid.querySelectorAll('.cron-dia-card').forEach(btn => {
    btn.addEventListener('click', () => {
      M.diaAtivo = btn.dataset.dia;
      grid.querySelectorAll('.cron-dia-card').forEach(b => b.classList.remove('ativo'));
      btn.classList.add('ativo');
      _renderizarDetalheAgenda();
    });
  });

  _renderizarDetalheAgenda();
}

function _renderizarDetalheAgenda() {
  const detalhe = document.getElementById('cron-agenda-detalhe');
  if (!detalhe) return;

  const d = M.diaAtivo;
  const entrada = M.log[d];
  const label = _formatarData(d);

  if (!entrada || !entrada.sessoes?.length) {
    detalhe.innerHTML = `
      <div class="cron-agenda-dia-titulo">${label}</div>
      <div class="cron-agenda-vazio">📭 Nenhuma sessão registrada neste dia.</div>`;
    return;
  }

  const sessoes = entrada.sessoes.map(s => {
    const t = M.topicos.find(x => x.id === s.topicoId);
    const nome = t ? t.nome : s.topicoId;
    return `
      <div class="cron-sessao">
        <span class="cron-sessao-mins">${s.minutos}min</span>
        <div class="cron-sessao-info">
          <div class="cron-sessao-topico">${_esc(nome)}</div>
          ${s.obs ? `<div class="cron-sessao-obs">${_esc(s.obs)}</div>` : ''}
        </div>
      </div>`;
  }).join('');

  detalhe.innerHTML = `
    <div class="cron-agenda-dia-titulo">${label} · ⏱ ${_formatarMinutos(entrada.minutos)}</div>
    <div class="cron-log-dia">${sessoes}</div>`;
}

// ── Utilitários ───────────────────────────────────────────────
function _flatTopicos(data) {
  const lista = [];
  const siglas = { basicos: 'CB', complementares: 'CC', especificos: 'CE' };
  for (const bloco of (data.blocos || [])) {
    for (const disc of (bloco.disciplinas || [])) {
      for (const t of (disc.topicos || [])) {
        lista.push({
          id:            t.id,
          nome:          t.nome,
          incidencia:    t.incidencia || 'media',
          bloco:         bloco.id,
          blocoSigla:    siglas[bloco.id] || bloco.sigla || bloco.id,
          disciplina:    disc.id,
          disciplinaNome: disc.nome,
        });
      }
    }
  }
  return lista;
}

function _hoje() {
  return new Date().toISOString().slice(0, 10);
}

function _diasDaSemana(offset = 0) {
  const hoje = new Date();
  // Começa no domingo; retorna Dom–Sex (6 dias — sábado é dia de descanso)
  const diaSem = hoje.getDay(); // 0=Dom
  const dom = new Date(hoje);
  dom.setDate(hoje.getDate() - diaSem + offset * 7);
  return Array.from({ length: 6 }, (_, i) => {
    const d = new Date(dom);
    d.setDate(dom.getDate() + i);
    return d.toISOString().slice(0, 10);
  });
}

function _labelSemana(dias) {
  const ini = _formatarDataCurta(dias[0]);
  const fim = _formatarDataCurta(dias[dias.length - 1]);
  return `${ini} – ${fim}`;
}

function _formatarData(iso) {
  if (!iso) return '';
  const [ano, mes, dia] = iso.split('-');
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  const hoje = _hoje();
  if (iso === hoje) return `Hoje, ${parseInt(dia,10)} de ${meses[+mes-1]}`;
  const ontem = new Date(); ontem.setDate(ontem.getDate()-1);
  if (iso === ontem.toISOString().slice(0,10)) return `Ontem, ${parseInt(dia,10)} de ${meses[+mes-1]}`;
  return `${parseInt(dia,10)} de ${meses[+mes-1]} de ${ano}`;
}

function _formatarDataCurta(iso) {
  if (!iso) return '';
  const [, mes, dia] = iso.split('-');
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  return `${parseInt(dia,10)} ${meses[+mes-1]}`;
}

function _formatarMinutos(min) {
  if (!min) return '0min';
  if (min < 60) return `${min}min`;
  const h = Math.floor(min / 60);
  const m = min % 60;
  return m ? `${h}h ${m}min` : `${h}h`;
}

function _esc(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
