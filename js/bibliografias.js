/**
 * bibliografias.js — Módulo Bibliografias
 * Cards por categoria, busca por título/autor, links externos e Drive.
 */

let _dados = null;
let _busca = '';

// ── Entrada ──────────────────────────────────────────────────
export async function iniciarBibliografias() {
  const painel = document.getElementById('painel-bibliografias');
  if (!painel) return;

  if (!_dados) {
    try {
      const resp = await fetch('./data/bibliografias.json');
      _dados = await resp.json();
    } catch {
      painel.innerHTML = `
        <div class="estado-vazio">
          <div class="estado-vazio-emoji">⚠️</div>
          <div class="estado-vazio-texto">Não foi possível carregar as bibliografias.<br>Verifique a conexão e tente novamente.</div>
        </div>`;
      return;
    }
  }

  const total = _dados.categorias.reduce((s, c) => s + c.obras.length, 0);

  painel.innerHTML = `
    <div class="painel-header" data-emoji="📖">
      <div class="painel-header-label">Material de Apoio</div>
      <div class="painel-header-titulo">Bibliografias</div>
      <div class="painel-header-sub">${total} obras · ${_dados.categorias.length} categorias</div>
    </div>

    <div class="bib-busca-wrap">
      <input id="bib-busca" class="bib-busca-input" type="search"
        placeholder="Buscar por título ou autor…" autocomplete="off"
        value="${_escHtml(_busca)}">
    </div>

    <div id="bib-conteudo" class="bib-conteudo"></div>
    <div style="height:80px;"></div>
  `;

  _renderizarConteudo();

  painel.querySelector('#bib-busca').addEventListener('input', e => {
    _busca = e.target.value.toLowerCase().trim();
    _renderizarConteudo();
  });
}

// ── Renderização ─────────────────────────────────────────────
function _renderizarConteudo() {
  const el = document.getElementById('bib-conteudo');
  if (!el || !_dados) return;

  const cats = _dados.categorias
    .map(cat => ({
      ...cat,
      obras: cat.obras.filter(o => {
        if (!_busca) return true;
        return o.titulo.toLowerCase().includes(_busca) ||
               o.autor.toLowerCase().includes(_busca);
      }),
    }))
    .filter(cat => cat.obras.length > 0);

  if (cats.length === 0) {
    el.innerHTML = `
      <div class="estado-vazio">
        <div class="estado-vazio-emoji">🔍</div>
        <div class="estado-vazio-texto">Nenhuma obra encontrada para essa busca.</div>
      </div>`;
    return;
  }

  el.innerHTML = cats.map(cat => _htmlCategoria(cat)).join('');
}

function _htmlCategoria(cat) {
  return `
    <div class="bib-categoria">
      <div class="bib-categoria-header">
        <span class="bib-categoria-emoji">${cat.emoji}</span>
        <h3 class="bib-categoria-nome">${_escHtml(cat.nome)}</h3>
        <span class="bib-categoria-count">${cat.obras.length}</span>
      </div>
      <div class="bib-obras">
        ${cat.obras.map(_htmlCard).join('')}
      </div>
    </div>`;
}

function _htmlCard(obra) {
  const relClass = obra.relevancia === 'alta' ? 'alta' : 'media';
  const relLabel = obra.relevancia === 'alta' ? '🔴 Alta' : '🟡 Média';

  const metaPartes = [
    obra.autor ? `<span class="bib-autor">${_escHtml(obra.autor)}</span>` : '',
    obra.ano   ? `<span class="bib-meta-sep">·</span><span class="bib-ano">${obra.ano}</span>` : '',
    obra.editora ? `<span class="bib-meta-sep">·</span><span class="bib-editora">${_escHtml(obra.editora)}</span>` : '',
  ].filter(Boolean).join('');

  const topicosHtml = obra.topicos?.length
    ? `<div class="bib-topicos">${obra.topicos.map(t => `<span class="bib-topico-tag">${_escHtml(t)}</span>`).join('')}</div>`
    : '';

  const btnAcessar = obra.linkExterno
    ? `<a href="${obra.linkExterno}" target="_blank" rel="noopener noreferrer" class="bib-btn bib-btn-acessar">🔗 Acessar</a>`
    : '';

  const btnDrive = obra.tipo !== 'legislacao'
    ? `<a href="https://drive.google.com/drive/search?q=${encodeURIComponent(obra.titulo)}" target="_blank" rel="noopener noreferrer" class="bib-btn bib-btn-drive">📁 Abrir no Drive</a>`
    : '';

  return `
    <div class="bib-card">
      <div class="bib-card-topo">
        <span class="bib-relevancia bib-relevancia-${relClass}">${relLabel}</span>
      </div>
      <div class="bib-card-titulo">${_escHtml(obra.titulo)}</div>
      <div class="bib-card-meta">${metaPartes}</div>
      <p class="bib-resumo">${_escHtml(obra.resumo)}</p>
      ${topicosHtml}
      ${btnAcessar || btnDrive ? `<div class="bib-acoes">${btnAcessar}${btnDrive}</div>` : ''}
    </div>`;
}

// ── Helpers ──────────────────────────────────────────────────
function _escHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
