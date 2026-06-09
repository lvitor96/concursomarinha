/**
 * legislacao.js — Módulo Legislação
 * Visualizador de textos legais com progresso, favoritos e anotações.
 * Dados: data/legislacao.json → Firestore users/{uid}/legislacao/{docId}
 *        { [artKey]: { lido, favorito, anotacao } }
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import { doc, getDoc, setDoc, serverTimestamp } from 'firebase/firestore';

/* ── Estado ─────────────────────────────────────────────────── */
const M = {
  dados:            null,   // legislacao.json
  status:           {},     // { [docId]: { [artKey]: { lido, favorito, anotacao } } }
  docAtual:         null,   // documento aberto
  busca:            '',
  _statusCarregado: false,
};

let _autoSaveTimers = {};

/* ── Entry point ─────────────────────────────────────────────── */
export async function iniciarLegislacao() {
  const el = document.getElementById('painel-legislacao');
  if (!el) return;

  el.innerHTML = `<div style="padding:32px;text-align:center;"><div class="spinner" style="border-color:var(--cor-borda);border-top-color:var(--cor-secundaria);margin:auto;"></div></div>`;

  if (!M.dados) {
    const r = await fetch('./data/legislacao.json');
    M.dados = await r.json();
  }

  await _carregarStatus();
  M.docAtual = null;
  _renderHome(el);
}

/* ── Firestore ───────────────────────────────────────────────── */
async function _carregarStatus() {
  if (M._statusCarregado) return;
  const usuario = obterUsuario();
  if (!usuario || !M.dados) return;

  await Promise.allSettled(
    M.dados.documentos.map(async docDef => {
      const snap = await getDoc(doc(db, 'users', usuario.uid, 'legislacao', docDef.id));
      M.status[docDef.id] = snap.exists() ? snap.data() : {};
    })
  );
  M._statusCarregado = true;
}

async function _salvarStatus(docId) {
  const usuario = obterUsuario();
  if (!usuario) return;
  try {
    await setDoc(
      doc(db, 'users', usuario.uid, 'legislacao', docId),
      { ...M.status[docId], _ts: serverTimestamp() },
      { merge: true }
    );
  } catch {
    // offline
  }
}

function _salvarAnotacaoDebounced(docId, artKey, texto) {
  const k = `${docId}__${artKey}`;
  clearTimeout(_autoSaveTimers[k]);
  _autoSaveTimers[k] = setTimeout(async () => {
    if (!M.status[docId]) M.status[docId] = {};
    if (!M.status[docId][artKey]) M.status[docId][artKey] = {};
    M.status[docId][artKey].anotacao = texto;
    await _salvarStatus(docId);
  }, 1500);
}

/* ── HOME — lista de documentos ──────────────────────────────── */
function _renderHome(el) {
  const docs = M.dados?.documentos ?? [];
  el.innerHTML = `
    <div class="painel-header" data-emoji="⚖️">
      <div class="painel-header-label">Legislação</div>
      <div class="painel-header-titulo">Textos legais</div>
      <div class="painel-header-sub">LDB · ECA · CF/88 · PNE · BNCC</div>
    </div>
    <div class="leg-doc-grid">
      ${docs.map(d => _htmlDocCard(d)).join('')}
    </div>
  `;

  el.querySelectorAll('.leg-doc-card').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.docId;
      M.docAtual = M.dados.documentos.find(d => d.id === id) ?? null;
      if (M.docAtual) { M.busca = ''; _renderViewer(el); }
    });
  });
}

function _htmlDocCard(docDef) {
  const status = M.status[docDef.id] ?? {};
  const totalArt = docDef.capitulos.reduce((s, c) => s + c.artigos.length, 0);
  const lidos    = Object.values(status).filter(v => v?.lido).length;
  const pct      = totalArt > 0 ? Math.round(lidos / totalArt * 100) : 0;

  return `
    <button class="leg-doc-card" data-doc-id="${docDef.id}">
      <span class="leg-doc-icone">${docDef.icone}</span>
      <div class="leg-doc-info">
        <span class="leg-doc-sigla" style="background:${docDef.cor};">${docDef.sigla}</span>
        <div class="leg-doc-titulo">${docDef.titulo}</div>
        <div class="leg-doc-subtitulo">${docDef.subtitulo}</div>
        <div class="leg-doc-meta">
          <div class="leg-doc-progresso">
            <div class="leg-doc-progresso-fill" style="width:${pct}%;background:${docDef.cor};"></div>
          </div>
          <span class="leg-doc-pct">${pct}%</span>
        </div>
      </div>
    </button>`;
}

/* ── VIEWER — artigos de um documento ────────────────────────── */
function _renderViewer(el) {
  const docDef = M.docAtual;
  if (!docDef) return;

  el.innerHTML = `
    <!-- Header sticky -->
    <div class="leg-viewer-header">
      <button class="leg-viewer-back" id="leg-back">← Voltar</button>
      <div class="leg-viewer-doc-info">
        <div class="leg-viewer-sigla">${docDef.sigla}</div>
        <div class="leg-viewer-titulo">${docDef.titulo}</div>
      </div>
    </div>

    <!-- Busca sticky -->
    <div class="leg-busca-wrap">
      <input class="leg-busca" id="leg-busca" type="search" placeholder="Buscar artigo ou palavra-chave…" value="${_esc(M.busca)}">
    </div>

    <!-- Capítulos e artigos -->
    <div id="leg-conteudo"></div>
  `;

  el.querySelector('#leg-back').addEventListener('click', () => _renderHome(el));
  el.querySelector('#leg-busca').addEventListener('input', e => {
    M.busca = e.target.value;
    _renderConteudo(el.querySelector('#leg-conteudo'));
  });

  _renderConteudo(el.querySelector('#leg-conteudo'));
}

function _renderConteudo(conteudo) {
  const docDef = M.docAtual;
  const busca  = M.busca.toLowerCase().trim();

  let html = '';
  let totalVisiveis = 0;

  docDef.capitulos.forEach(cap => {
    const artigosFiltrados = busca
      ? cap.artigos.filter(a =>
          String(a.num).toLowerCase().includes(busca) ||
          (a.titulo ?? '').toLowerCase().includes(busca) ||
          a.texto.toLowerCase().includes(busca)
        )
      : cap.artigos;

    if (!artigosFiltrados.length) return;
    totalVisiveis += artigosFiltrados.length;

    html += `<div class="leg-capitulo">
      <div class="leg-capitulo-titulo">${_esc(cap.titulo)}</div>
      ${artigosFiltrados.map(a => _htmlArtigo(a, docDef.id)).join('')}
    </div>`;
  });

  if (!totalVisiveis) {
    html = `<p class="leg-sem-resultados">Nenhum artigo encontrado para "<strong>${_esc(M.busca)}</strong>"</p>`;
  }

  conteudo.innerHTML = html + '<div style="height:80px;"></div>';
  _bindArtigos(conteudo, docDef.id);
}

function _htmlArtigo(artigo, docId) {
  const key    = _artKey(artigo.num);
  const st     = M.status[docId]?.[key] ?? {};
  const lido   = st.lido ?? false;
  const fav    = st.favorito ?? false;
  const anot   = st.anotacao ?? '';

  const classes = ['leg-artigo', lido ? 'lido' : '', fav ? 'favorito' : ''].filter(Boolean).join(' ');

  return `
    <div class="${classes}" data-art-key="${key}" data-doc-id="${docId}">
      <div class="leg-artigo-header">
        <span class="leg-artigo-num">Art. ${artigo.num}</span>
        <span class="leg-artigo-titulo-nome">${_esc(artigo.titulo ?? artigo.texto.slice(0, 50) + '…')}</span>
        <div class="leg-artigo-badges">
          <button class="leg-badge ${lido ? 'ativo-lido' : ''}" data-acao="lido"   title="${lido ? 'Marcar como não lido' : 'Marcar como lido'}">✓</button>
          <button class="leg-badge ${fav  ? 'ativo-fav'  : ''}" data-acao="fav"    title="${fav  ? 'Remover favorito' : 'Favoritar'}">★</button>
          <button class="leg-badge ${anot ? 'ativo-anot' : ''}" data-acao="anot"   title="Anotação">✎</button>
        </div>
        <span class="leg-chevron">▼</span>
      </div>
      <div class="leg-artigo-corpo">
        <div class="leg-artigo-texto">${_esc(artigo.texto)}</div>
        <div class="leg-anotacao-label">Minha anotação</div>
        <textarea class="leg-anotacao-area" data-art-key="${key}" data-doc-id="${docId}" placeholder="Escreva aqui sua observação sobre este artigo…" rows="3">${_esc(anot)}</textarea>
      </div>
    </div>`;
}

function _bindArtigos(conteudo, docId) {
  // Expand / collapse ao clicar no header
  conteudo.querySelectorAll('.leg-artigo-header').forEach(header => {
    header.addEventListener('click', e => {
      if (e.target.closest('[data-acao]')) return; // badge → não expande
      const artEl = header.closest('.leg-artigo');
      artEl.classList.toggle('expandido');
    });
  });

  // Badges: lido, favorito, anotação
  conteudo.querySelectorAll('[data-acao]').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const artEl = btn.closest('.leg-artigo');
      const key   = artEl.dataset.artKey;
      const acao  = btn.dataset.acao;

      if (!M.status[docId]) M.status[docId] = {};
      if (!M.status[docId][key]) M.status[docId][key] = {};

      const st = M.status[docId][key];

      if (acao === 'lido') {
        st.lido = !st.lido;
        artEl.classList.toggle('lido', st.lido);
        btn.classList.toggle('ativo-lido', st.lido);
        btn.title = st.lido ? 'Marcar como não lido' : 'Marcar como lido';
        _salvarStatus(docId);
      } else if (acao === 'fav') {
        st.favorito = !st.favorito;
        artEl.classList.toggle('favorito', st.favorito);
        btn.classList.toggle('ativo-fav', st.favorito);
        btn.title = st.favorito ? 'Remover favorito' : 'Favoritar';
        _salvarStatus(docId);
      } else if (acao === 'anot') {
        artEl.classList.toggle('expandido', true);
        artEl.querySelector('.leg-anotacao-area')?.focus();
      }
    });
  });

  // Auto-save de anotações
  conteudo.querySelectorAll('.leg-anotacao-area').forEach(area => {
    area.addEventListener('input', () => {
      const key   = area.dataset.artKey;
      const docId = area.dataset.docId;
      const anotBtn = area.closest('.leg-artigo').querySelector('[data-acao="anot"]');
      if (anotBtn) anotBtn.classList.toggle('ativo-anot', area.value.length > 0);
      area.classList.add('salvando');
      _salvarAnotacaoDebounced(docId, key, area.value);
      setTimeout(() => area.classList.remove('salvando'), 1600);
    });
  });
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _artKey(num) {
  return String(num).replace(/\s+/g, '-').toLowerCase();
}

function _esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
