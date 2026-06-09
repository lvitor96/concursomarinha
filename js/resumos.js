/**
 * resumos.js — Módulo Banco de Resumos.
 * Vistas: lista (com busca/filtro) → detalhe (Markdown + anotações).
 */

import { db } from './firebase.js';
import { doc, getDoc, setDoc, serverTimestamp } from 'firebase/firestore';

// ── Estado do módulo ─────────────────────────────────────────
const M = {
  resumos:      [],      // todos os resumos carregados
  progresso:    {},      // { [id]: true } — marcados como estudados
  anotacoes:    {},      // { [id]: string } — carregadas sob demanda
  filtroBloco:  'todos',
  busca:        '',
  resumoAtivo:  null,    // objeto resumo em exibição
  versao:       'curta', // 'curta' | 'completa'
  _debounceId:  null,
};

// ── Entrada ──────────────────────────────────────────────────
export async function iniciarResumes() {
  const painel = document.getElementById('painel-estudar');
  if (!painel) return;

  // Carrega JSON
  try {
    const resp = await fetch('./data/resumos.json');
    const data = await resp.json();
    M.resumos = data.resumos || [];
  } catch {
    _renderizarErro(painel);
    return;
  }

  // Carrega progresso do Firestore (best-effort)
  await _carregarProgresso();

  // Modo inicial: Mesa → completo; Metrô/Carro → curto
  const modo = document.body.dataset.modo;
  M.versao = modo === 'mesa' ? 'completa' : 'curta';

  _renderizarLista(painel);
}

// ── Progresso (Firestore) ────────────────────────────────────
async function _carregarProgresso() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    const snap = await getDoc(doc(db, 'users', uid, 'resumos', 'progresso'));
    if (snap.exists()) M.progresso = snap.data() || {};
  } catch { /* offline ok */ }
}

async function _salvarProgresso() {
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    await setDoc(doc(db, 'users', uid, 'resumos', 'progresso'),
      { ...M.progresso, atualizadoEm: serverTimestamp() },
      { merge: true }
    );
  } catch { /* offline — Firestore fará sync depois */ }
}

async function _carregarAnotacao(id) {
  if (M.anotacoes[id] !== undefined) return M.anotacoes[id];
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return '';
  try {
    const snap = await getDoc(doc(db, 'users', uid, 'anotacoes', id));
    M.anotacoes[id] = snap.exists() ? (snap.data().texto || '') : '';
  } catch {
    M.anotacoes[id] = '';
  }
  return M.anotacoes[id];
}

async function _salvarAnotacao(id, texto) {
  M.anotacoes[id] = texto;
  const uid = window.app?.estado?.usuario?.uid;
  if (!uid) return;
  try {
    await setDoc(doc(db, 'users', uid, 'anotacoes', id), {
      texto,
      atualizadoEm: serverTimestamp(),
    });
  } catch { /* offline ok */ }
}

// ── Vista: LISTA ─────────────────────────────────────────────
function _renderizarLista(painelEl) {
  const painel = painelEl || document.getElementById('painel-estudar');
  if (!painel) return;

  const clone = painel.cloneNode(false);
  painel.parentNode.replaceChild(clone, painel);

  clone.innerHTML = `
    <div class="painel-header" data-emoji="📚">
      <div class="painel-header-label">Banco de Resumos</div>
      <div class="painel-header-titulo">Estudar</div>
      <div class="painel-header-sub">${M.resumos.length} resumos · busca e filtro por bloco</div>
    </div>

    <div class="r-busca-wrap">
      <input id="r-busca" class="r-busca-input" type="search"
        placeholder="Buscar resumo..." autocomplete="off"
        value="${_escapeHtml(M.busca)}">
    </div>

    <div class="r-chips" id="r-chips">
      ${_htmlChips()}
    </div>

    <div class="r-contador" id="r-contador"></div>
    <div class="r-lista" id="r-lista"></div>
  `;

  // Preenche lista
  _filtrarERenderizar();

  // Eventos
  clone.querySelector('#r-busca').addEventListener('input', e => {
    M.busca = e.target.value;
    _filtrarERenderizar();
  });

  clone.querySelectorAll('.r-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      M.filtroBloco = chip.dataset.filtro;
      clone.querySelectorAll('.r-chip').forEach(c => c.classList.remove('ativo'));
      chip.classList.add('ativo');
      _filtrarERenderizar();
    });
  });
}

function _htmlChips() {
  const opcoes = [
    { filtro: 'todos',          label: 'Todos' },
    { filtro: 'especificos',    label: '🎵 Específicos' },
    { filtro: 'complementares', label: '📖 Complementares' },
    { filtro: 'basicos',        label: '📝 Básicos' },
  ];
  return opcoes.map(o => `
    <button class="r-chip ${M.filtroBloco === o.filtro ? 'ativo' : ''}"
      data-filtro="${o.filtro}">${o.label}</button>
  `).join('');
}

function _filtrarERenderizar() {
  const lista   = document.getElementById('r-lista');
  const contador = document.getElementById('r-contador');
  if (!lista) return;

  const busca = M.busca.trim().toLowerCase();

  const filtrados = M.resumos.filter(r => {
    const blocoOk = M.filtroBloco === 'todos' || r.bloco === M.filtroBloco;
    const buscaOk = !busca ||
      r.nome.toLowerCase().includes(busca) ||
      r.disciplina.toLowerCase().includes(busca);
    return blocoOk && buscaOk;
  });

  if (contador) {
    contador.textContent = `${filtrados.length} ${filtrados.length === 1 ? 'resumo' : 'resumos'}`;
  }

  if (filtrados.length === 0) {
    lista.innerHTML = `
      <div class="r-vazio">
        <div class="r-vazio-emoji">🔍</div>
        <div class="r-vazio-texto">Nenhum resumo encontrado para essa busca.</div>
      </div>`;
    return;
  }

  lista.innerHTML = filtrados.map(r => _htmlCard(r)).join('');

  lista.addEventListener('click', e => {
    const card = e.target.closest('.r-card');
    if (!card) return;
    const id = card.dataset.id;
    const resumo = M.resumos.find(r => r.id === id);
    if (resumo) _abrirDetalhe(resumo);
  });
}

function _htmlCard(r) {
  const estudado  = M.progresso[r.id];
  const incLabel  = { alta: '🔴 Alta', media: '🟡 Média', baixa: '🟢 Baixa' }[r.incidencia] || '';
  return `
    <button class="r-card" data-id="${r.id}">
      <div class="r-card-topo">
        <span class="r-card-nome">${_escapeHtml(r.nome)}</span>
        ${estudado ? '<span class="r-estudado-badge">✅ Estudado</span>' : ''}
      </div>
      <div class="r-card-meta">
        <span class="tag tag-bloco-${r.bloco}">${_siglaBloco(r.bloco)}</span>
        <span class="r-incidencia ${r.incidencia}">${incLabel}</span>
        <span style="font-size:11px;color:var(--cor-texto-leve);">${_nomeDisc(r.disciplina)}</span>
      </div>
    </button>
  `;
}

// ── Vista: DETALHE ───────────────────────────────────────────
async function _abrirDetalhe(resumo) {
  M.resumoAtivo = resumo;
  const painel = document.getElementById('painel-estudar');
  if (!painel) return;

  // Carrega anotação antes de renderizar
  const anotacaoTexto = await _carregarAnotacao(resumo.id);

  const clone = painel.cloneNode(false);
  painel.parentNode.replaceChild(clone, painel);

  const modo      = document.body.dataset.modo;
  const estudado  = !!M.progresso[resumo.id];
  const incLabel  = { alta: '🔴 Alta', media: '🟡 Média', baixa: '🟢 Baixa' }[resumo.incidencia] || '';

  clone.innerHTML = `
    <div class="r-detalhe">

      <div class="r-detalhe-topo">
        <button class="r-btn-voltar" id="r-voltar">← Resumos</button>
        <span class="r-detalhe-titulo">${_escapeHtml(resumo.nome)}</span>
      </div>

      <div class="r-detalhe-meta">
        <span class="tag tag-bloco-${resumo.bloco}">${_siglaBloco(resumo.bloco)}</span>
        <span class="r-incidencia ${resumo.incidencia}">${incLabel}</span>
        <span style="font-size:11px;color:var(--cor-texto-leve);">${_nomeDisc(resumo.disciplina)}</span>
      </div>

      <div class="r-toggle-wrap" id="r-toggle-wrap">
        <button class="r-toggle-btn ${M.versao === 'curta' ? 'ativo' : ''}" data-v="curta">⚡ Versão Curta</button>
        <button class="r-toggle-btn ${M.versao === 'completa' ? 'ativo' : ''}" data-v="completa">📖 Versão Completa</button>
      </div>

      <div class="r-conteudo-scroll">
        <div class="r-conteudo-md" id="r-md"></div>
      </div>

      <div class="r-anotacoes-wrap" id="r-anotacoes-wrap">
        <div class="r-anotacoes-label">Minhas anotações</div>
        <textarea id="r-anotacoes" class="r-anotacoes-textarea"
          placeholder="Escreva observações, dúvidas ou complementos sobre este tópico..."
          >${_escapeHtml(anotacaoTexto)}</textarea>
        <div class="r-anotacoes-footer">
          <span class="r-anotacoes-status" id="r-status"></span>
          <button class="r-btn-estudado ${estudado ? 'feito' : ''}" id="r-btn-estudado">
            ${estudado ? '✅ Estudado' : '○ Marcar como estudado'}
          </button>
        </div>
      </div>

    </div>
  `;

  // Renderiza Markdown inicial
  _renderizarMd(resumo);

  // Scroll ao topo
  clone.scrollTop = 0;

  // ── Eventos ──

  // Voltar
  clone.querySelector('#r-voltar').addEventListener('click', () => {
    _renderizarLista(document.getElementById('painel-estudar'));
  });

  // Toggle versão
  clone.querySelectorAll('.r-toggle-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      M.versao = btn.dataset.v;
      clone.querySelectorAll('.r-toggle-btn').forEach(b => b.classList.remove('ativo'));
      btn.classList.add('ativo');
      _renderizarMd(resumo);
    });
  });

  // Anotações — auto-save com debounce
  const textarea = clone.querySelector('#r-anotacoes');
  const statusEl = clone.querySelector('#r-status');

  textarea?.addEventListener('input', () => {
    if (statusEl) { statusEl.textContent = 'Digitando...'; statusEl.className = 'r-anotacoes-status'; }
    clearTimeout(M._debounceId);
    M._debounceId = setTimeout(async () => {
      await _salvarAnotacao(resumo.id, textarea.value);
      if (statusEl) { statusEl.textContent = '✓ Salvo'; statusEl.className = 'r-anotacoes-status salvo'; }
    }, 1500);
  });

  // Marcar como estudado
  const btnEstudado = clone.querySelector('#r-btn-estudado');
  btnEstudado?.addEventListener('click', async () => {
    const novoEstado = !M.progresso[resumo.id];
    M.progresso[resumo.id] = novoEstado || undefined;
    if (!novoEstado) delete M.progresso[resumo.id];

    btnEstudado.textContent = novoEstado ? '✅ Estudado' : '○ Marcar como estudado';
    btnEstudado.classList.toggle('feito', novoEstado);

    await _salvarProgresso();
    window.app?.mostrarToast(novoEstado ? '✅ Marcado como estudado!' : 'Desmarcado');
  });
}

function _renderizarMd(resumo) {
  const el = document.getElementById('r-md');
  if (!el) return;
  const texto = M.versao === 'completa' ? resumo.versaoCompleta : resumo.versaoCurta;
  el.innerHTML = _parseMd(texto || '');
}

// ── Parser Markdown custom ───────────────────────────────────
function _parseMd(texto) {
  // Processa linha a linha
  const linhas = texto.split('\n');
  const html = [];
  let emLista = false;

  for (let i = 0; i < linhas.length; i++) {
    let l = linhas[i];

    // Headings
    if (l.startsWith('### ')) {
      if (emLista) { html.push('</ul>'); emLista = false; }
      html.push(`<h3>${_inline(l.slice(4))}</h3>`);
      continue;
    }
    if (l.startsWith('## ')) {
      if (emLista) { html.push('</ul>'); emLista = false; }
      html.push(`<h2>${_inline(l.slice(3))}</h2>`);
      continue;
    }
    if (l.startsWith('# ')) {
      if (emLista) { html.push('</ul>'); emLista = false; }
      html.push(`<h1>${_inline(l.slice(2))}</h1>`);
      continue;
    }

    // HR
    if (l.trim() === '---') {
      if (emLista) { html.push('</ul>'); emLista = false; }
      html.push('<hr>');
      continue;
    }

    // List item
    if (l.startsWith('- ') || l.startsWith('  - ') || l.startsWith('    - ')) {
      if (!emLista) { html.push('<ul>'); emLista = true; }
      html.push(`<li>${_inline(l.replace(/^\s*-\s/, ''))}</li>`);
      continue;
    }

    // Linha vazia
    if (l.trim() === '') {
      if (emLista) { html.push('</ul>'); emLista = false; }
      continue;
    }

    // Parágrafo normal
    if (emLista) { html.push('</ul>'); emLista = false; }
    html.push(`<p>${_inline(l)}</p>`);
  }

  if (emLista) html.push('</ul>');
  return html.join('');
}

// Inline: bold, italic, code
function _inline(txt) {
  return txt
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code style="background:var(--cor-fundo);padding:1px 5px;border-radius:4px;font-size:.9em;">$1</code>');
}

// ── Helpers ──────────────────────────────────────────────────
function _siglaBloco(bloco) {
  return { especificos: 'CE', complementares: 'CC', basicos: 'CB' }[bloco] || bloco;
}

function _nomeDisc(disc) {
  const mapa = {
    'metodologias':           'Metodologias',
    'bncc-musica':            'BNCC — Música',
    'historia-musica':        'História da Música',
    'teoria-musical':         'Teoria Musical',
    'regencia':               'Regência',
    'legislacao-educacional': 'Legislação',
    'eca':                    'ECA',
    'politicas-publicas':     'Políticas Públicas',
    'gestao-pedagogica':      'Gestão Pedagógica',
    'lingua-portuguesa':      'Língua Portuguesa',
    'redacao-oficial':        'Redação Oficial',
    'realidade-df':           'Realidade do DF',
  };
  return mapa[disc] || disc;
}

function _escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function _renderizarErro(painel) {
  painel.innerHTML = `
    <div class="estado-vazio">
      <div class="estado-vazio-emoji">⚠️</div>
      <div class="estado-vazio-texto">Não foi possível carregar os resumos.<br>Verifique a conexão e tente novamente.</div>
    </div>`;
}
