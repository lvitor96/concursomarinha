/**
 * videoaulas.js — Módulo Videoaulas
 * Biblioteca pessoal (YouTube URL → oEmbed) + sugestões de busca por bloco.
 * Firestore: users/{uid}/videos/{youtubeId} → { youtubeId, titulo, canal, bloco, assistido, addedAt }
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import {
  collection, doc, getDoc, getDocs, setDoc, deleteDoc,
  query, orderBy, serverTimestamp
} from 'firebase/firestore';

/* ── Sugestões por bloco ─────────────────────────────────────── */
const _SUGESTOES = [
  {
    bloco: 'Conhecimentos Básicos',
    itens: [
      { nome: 'LDB — Lei de Diretrizes e Bases da Educação',          url: 'https://www.youtube.com/results?search_query=LDB+lei+diretrizes+bases+educação+resumo' },
      { nome: 'ECA — Estatuto da Criança e do Adolescente',           url: 'https://www.youtube.com/results?search_query=ECA+estatuto+criança+adolescente+resumo+concurso' },
      { nome: 'BNCC — Base Nacional Comum Curricular',                url: 'https://www.youtube.com/results?search_query=BNCC+base+nacional+comum+curricular+explicação' },
      { nome: 'PNE — Plano Nacional de Educação',                     url: 'https://www.youtube.com/results?search_query=PNE+plano+nacional+educação+metas+concurso' },
      { nome: 'Didática e Planejamento de Ensino',                    url: 'https://www.youtube.com/results?search_query=didática+planejamento+ensino+concurso+professor' },
      { nome: 'Psicologia da Educação — Piaget, Vygotsky, Wallon',    url: 'https://www.youtube.com/results?search_query=piaget+vygotsky+wallon+psicologia+educação' },
      { nome: 'Avaliação Educacional',                                 url: 'https://www.youtube.com/results?search_query=avaliação+educacional+formativa+somativa+concurso' },
    ]
  },
  {
    bloco: 'Conhecimentos Complementares',
    itens: [
      { nome: 'Educação Musical — Fundamentos e Abordagens',          url: 'https://www.youtube.com/results?search_query=educação+musical+fundamentos+metodologia' },
      { nome: 'Música na BNCC — Arte e Linguagem Musical',            url: 'https://www.youtube.com/results?search_query=música+BNCC+linguagem+artística+educação+básica' },
      { nome: 'Pedagogia da Música — Orff, Kodály, Dalcroze',         url: 'https://www.youtube.com/results?search_query=orff+kodaly+dalcroze+pedagogia+musical' },
      { nome: 'Música Brasileira na Educação Básica',                  url: 'https://www.youtube.com/results?search_query=música+brasileira+educação+básica+sala+de+aula' },
      { nome: 'Inclusão e Educação Especial',                          url: 'https://www.youtube.com/results?search_query=educação+especial+inclusão+concurso+professor' },
    ]
  },
  {
    bloco: 'Conhecimentos Específicos',
    itens: [
      { nome: 'Teoria Musical — Notação e Leitura',                   url: 'https://www.youtube.com/results?search_query=teoria+musical+notação+leitura+de+música' },
      { nome: 'Solfejo e Percepção Musical',                           url: 'https://www.youtube.com/results?search_query=solfejo+percepção+musical+ditado+rítmico' },
      { nome: 'Harmonia Tonal',                                        url: 'https://www.youtube.com/results?search_query=harmonia+tonal+acordes+progressões+musicais' },
      { nome: 'Contraponto',                                           url: 'https://www.youtube.com/results?search_query=contraponto+musical+espécies+primeiro+segundo' },
      { nome: 'Formas Musicais — Fuga, Sonata, Rondó',                url: 'https://www.youtube.com/results?search_query=formas+musicais+fuga+sonata+rondó+análise' },
      { nome: 'História da Música Ocidental',                          url: 'https://www.youtube.com/results?search_query=história+música+ocidental+barroco+clássico+romântico' },
      { nome: 'Música Brasileira — MPB, Choro, Bossa Nova',           url: 'https://www.youtube.com/results?search_query=MPB+choro+bossa+nova+história+música+brasileira' },
      { nome: 'Regência Coral e Instrumental',                         url: 'https://www.youtube.com/results?search_query=regência+coral+instrumental+técnica+gestual' },
      { nome: 'Instrumento — Piano / Teclado',                         url: 'https://www.youtube.com/results?search_query=piano+teclado+técnica+educação+musical' },
      { nome: 'Instrumento — Violão / Guitarra',                       url: 'https://www.youtube.com/results?search_query=violão+guitarra+técnica+ensino+música' },
    ]
  },
];

/* ── Estado ─────────────────────────────────────────────────── */
const M = {
  videos: {},   // { [youtubeId]: { youtubeId, titulo, canal, bloco, assistido, addedAt } }
};

/* ── Entry point ─────────────────────────────────────────────── */
export async function iniciarVideoaulas() {
  const el = document.getElementById('painel-videoaulas');
  if (!el) return;

  el.innerHTML = `<div style="padding:32px;text-align:center;"><div class="spinner" style="border-color:var(--cor-borda);border-top-color:var(--cor-secundaria);margin:auto;"></div></div>`;

  await _carregarVideos();
  _renderHome(el);
}

/* ── Firestore ───────────────────────────────────────────────── */
async function _carregarVideos() {
  const usuario = obterUsuario();
  if (!usuario) return;

  try {
    const snap = await getDocs(
      query(collection(db, 'users', usuario.uid, 'videos'), orderBy('addedAt', 'desc'))
    );
    M.videos = {};
    snap.forEach(d => { M.videos[d.id] = d.data(); });
  } catch {
    // offline — M.videos permanece como estava
  }
}

async function _salvarVideo(vid) {
  const usuario = obterUsuario();
  if (!usuario) return;
  try {
    await setDoc(doc(db, 'users', usuario.uid, 'videos', vid.youtubeId), vid);
  } catch {
    // offline
  }
}

async function _removerVideo(youtubeId) {
  const usuario = obterUsuario();
  if (!usuario) return;
  try {
    await deleteDoc(doc(db, 'users', usuario.uid, 'videos', youtubeId));
  } catch {
    // offline
  }
}

/* ── Render principal ───────────────────────────────────────── */
function _renderHome(el) {
  const lista = Object.values(M.videos);

  el.innerHTML = `
    <div class="painel-header" data-emoji="🎬">
      <div class="painel-header-label">Videoaulas</div>
      <div class="painel-header-titulo">Minha biblioteca</div>
      <div class="painel-header-sub">Adicione aulas do YouTube e marque como assistidas</div>
    </div>

    <!-- Formulário de adição -->
    <div class="vid-add-wrap">
      <div class="vid-add-header" id="vid-add-toggle-btn">
        <span class="vid-add-header-titulo">+ Adicionar videoaula</span>
        <span class="vid-add-toggle" id="vid-add-toggle-lbl">Expandir</span>
      </div>
      <div class="vid-add-form" id="vid-add-form">
        <input
          class="vid-add-input"
          id="vid-url-input"
          type="url"
          placeholder="Cole a URL do YouTube (ex: https://youtu.be/…)"
          autocomplete="off"
        >
        <div class="vid-add-row">
          <select class="vid-add-bloco" id="vid-bloco-select">
            <option value="">Selecione o bloco…</option>
            <option value="basicos">Conhecimentos Básicos</option>
            <option value="complementares">Conhecimentos Complementares</option>
            <option value="especificos">Conhecimentos Específicos</option>
          </select>
          <button class="btn btn-primario" id="vid-add-btn" style="white-space:nowrap;">Adicionar</button>
        </div>
        <div class="vid-add-status" id="vid-add-status"></div>
      </div>
    </div>

    <!-- Biblioteca pessoal -->
    <div class="vid-lista" id="vid-lista">
      ${lista.length === 0 ? _htmlVazio() : lista.map(v => _htmlCard(v)).join('')}
    </div>

    <!-- Sugestões de busca -->
    <div style="padding:14px 16px 6px;">
      <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.4px;color:var(--cor-texto-leve);">
        Buscar no YouTube por assunto
      </div>
    </div>
    ${_SUGESTOES.map(bloco => _htmlBlocoSugestoes(bloco)).join('')}
    <div style="height:80px;"></div>
  `;

  _bindForm(el);
  _bindLista(el);
}

/* ── HTML helpers ────────────────────────────────────────────── */
function _htmlVazio() {
  return `
    <div class="vid-vazio">
      <div style="font-size:32px;margin-bottom:8px;">🎬</div>
      <div>Nenhuma videoaula adicionada ainda.</div>
      <div style="margin-top:4px;font-size:12px;">Cole uma URL do YouTube acima para começar.</div>
    </div>`;
}

function _htmlCard(v) {
  const thumb = `https://img.youtube.com/vi/${v.youtubeId}/mqdefault.jpg`;
  const assistido = v.assistido ?? false;
  return `
    <div class="vid-card${assistido ? ' assistido' : ''}" data-id="${_esc(v.youtubeId)}">
      <div class="vid-card-thumb-wrap" data-id="${_esc(v.youtubeId)}">
        <img class="vid-card-thumb" src="${thumb}" alt="${_esc(v.titulo)}" loading="lazy">
        <div class="vid-card-play">
          <div class="vid-card-play-btn">▶</div>
        </div>
      </div>
      <div class="vid-card-info">
        <div class="vid-card-titulo">${_esc(v.titulo)}</div>
        <div class="vid-card-meta">
          <span class="vid-card-canal">${_esc(v.canal || 'YouTube')}</span>
          ${v.bloco ? `<span class="tag tag-bloco-${_esc(v.bloco)}" style="font-size:10px;">${_nomeBloco(v.bloco)}</span>` : ''}
        </div>
        <div class="vid-card-acoes">
          <button class="vid-btn-assistido${assistido ? ' ativo' : ''}" data-acao="assistido" data-id="${_esc(v.youtubeId)}">
            ${assistido ? '✓ Assistida' : 'Marcar assistida'}
          </button>
          <button class="vid-btn-remover" data-acao="remover" data-id="${_esc(v.youtubeId)}" title="Remover">🗑</button>
        </div>
      </div>
    </div>`;
}

function _htmlBlocoSugestoes(bloco) {
  return `
    <div class="vid-sug-bloco">
      <div class="vid-sug-bloco-titulo">
        <span>${bloco.bloco}</span>
      </div>
      ${bloco.itens.map(item => `
        <div class="vid-sug-item">
          <span class="vid-sug-nome">${_esc(item.nome)}</span>
          <a class="vid-sug-btn" href="${item.url}" target="_blank" rel="noopener noreferrer">
            Buscar ↗
          </a>
        </div>`).join('')}
    </div>`;
}

/* ── Event bindings ──────────────────────────────────────────── */
function _bindForm(el) {
  const toggleBtn = el.querySelector('#vid-add-toggle-btn');
  const form      = el.querySelector('#vid-add-form');
  const toggleLbl = el.querySelector('#vid-add-toggle-lbl');

  toggleBtn?.addEventListener('click', () => {
    const aberto = form.classList.toggle('aberto');
    if (toggleLbl) toggleLbl.textContent = aberto ? 'Recolher' : 'Expandir';
  });

  el.querySelector('#vid-add-btn')?.addEventListener('click', () => _adicionarVideo(el));

  el.querySelector('#vid-url-input')?.addEventListener('keydown', e => {
    if (e.key === 'Enter') _adicionarVideo(el);
  });
}

function _bindLista(el) {
  el.querySelectorAll('[data-acao="assistido"]').forEach(btn => {
    btn.addEventListener('click', () => _toggleAssistido(el, btn.dataset.id));
  });

  el.querySelectorAll('[data-acao="remover"]').forEach(btn => {
    btn.addEventListener('click', () => _removerDaLista(el, btn.dataset.id));
  });

  el.querySelectorAll('.vid-card-thumb-wrap').forEach(wrap => {
    wrap.addEventListener('click', () => {
      const id = wrap.dataset.id;
      window.open(`https://www.youtube.com/watch?v=${encodeURIComponent(id)}`, '_blank', 'noopener,noreferrer');
    });
  });
}

/* ── Ações ───────────────────────────────────────────────────── */
async function _adicionarVideo(el) {
  const urlInput   = el.querySelector('#vid-url-input');
  const blocoSel   = el.querySelector('#vid-bloco-select');
  const statusEl   = el.querySelector('#vid-add-status');
  const addBtn     = el.querySelector('#vid-add-btn');

  const rawUrl = urlInput?.value?.trim();
  const bloco  = blocoSel?.value || '';

  _setStatus(statusEl, '');

  const youtubeId = _extrairYoutubeId(rawUrl);
  if (!youtubeId) {
    _setStatus(statusEl, 'URL inválida. Use um link do YouTube (youtu.be ou youtube.com/watch).', 'erro');
    return;
  }

  if (M.videos[youtubeId]) {
    _setStatus(statusEl, 'Esta videoaula já está na sua biblioteca.', 'erro');
    return;
  }

  addBtn.disabled = true;
  _setStatus(statusEl, 'Buscando informações do vídeo…');

  let titulo = 'Videoaula';
  let canal  = '';

  try {
    const oembedUrl = `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=${encodeURIComponent(youtubeId)}&format=json`;
    const resp = await fetch(oembedUrl);
    if (resp.ok) {
      const data = await resp.json();
      titulo = data.title  || titulo;
      canal  = data.author_name || canal;
    }
  } catch {
    // oEmbed falhou — usa título genérico
  }

  const vid = {
    youtubeId,
    titulo,
    canal,
    bloco,
    assistido: false,
    addedAt: serverTimestamp(),
  };

  M.videos[youtubeId] = { ...vid, addedAt: new Date() };
  await _salvarVideo(vid);

  // Atualiza lista na tela
  const lista = el.querySelector('#vid-lista');
  if (lista) {
    const vazio = lista.querySelector('.vid-vazio');
    if (vazio) vazio.remove();

    const cardEl = document.createElement('div');
    cardEl.innerHTML = _htmlCard(M.videos[youtubeId]);
    lista.prepend(cardEl.firstElementChild);
    _bindLista(lista.parentElement);
  }

  urlInput.value = '';
  blocoSel.value = '';
  addBtn.disabled = false;
  _setStatus(statusEl, `"${titulo}" adicionada com sucesso!`, 'ok');
  setTimeout(() => _setStatus(statusEl, ''), 3000);
}

async function _toggleAssistido(el, youtubeId) {
  const vid = M.videos[youtubeId];
  if (!vid) return;

  vid.assistido = !vid.assistido;
  await _salvarVideo(vid);

  const card = el.querySelector(`.vid-card[data-id="${youtubeId}"]`);
  const btn  = el.querySelector(`[data-acao="assistido"][data-id="${youtubeId}"]`);
  if (card) card.classList.toggle('assistido', vid.assistido);
  if (btn) {
    btn.classList.toggle('ativo', vid.assistido);
    btn.textContent = vid.assistido ? '✓ Assistida' : 'Marcar assistida';
  }
}

async function _removerDaLista(el, youtubeId) {
  delete M.videos[youtubeId];
  await _removerVideo(youtubeId);

  const card = el.querySelector(`.vid-card[data-id="${youtubeId}"]`);
  card?.remove();

  const lista = el.querySelector('#vid-lista');
  if (lista && !lista.querySelector('.vid-card')) {
    lista.innerHTML = _htmlVazio();
  }
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _extrairYoutubeId(url) {
  if (!url) return null;
  // youtu.be/ID
  const curto = url.match(/youtu\.be\/([A-Za-z0-9_-]{11})/);
  if (curto) return curto[1];
  // youtube.com/watch?v=ID
  const longo = url.match(/[?&]v=([A-Za-z0-9_-]{11})/);
  if (longo) return longo[1];
  // youtube.com/embed/ID
  const embed = url.match(/\/embed\/([A-Za-z0-9_-]{11})/);
  if (embed) return embed[1];
  return null;
}

function _nomeBloco(bloco) {
  return { basicos: 'CB', complementares: 'CC', especificos: 'CE' }[bloco] || bloco;
}

function _setStatus(el, msg, tipo = '') {
  if (!el) return;
  el.textContent = msg;
  el.className = `vid-add-status${tipo ? ' ' + tipo : ''}`;
}

function _esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
