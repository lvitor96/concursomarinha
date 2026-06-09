/**
 * edital.js — Módulo Edital Ativo
 * Mostra status do edital vigente, estrutura da prova e prontidão do candidato.
 * Dados: data/edital.json (estático) + Firestore questoesStatus (prontidão)
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import { collection, getDocs } from 'firebase/firestore';

/* ── Entry point ─────────────────────────────────────────────── */
export async function iniciarEdital() {
  const el = document.getElementById('painel-edital');
  if (!el) return;

  el.innerHTML = `<div style="padding:32px;text-align:center;"><div class="spinner" style="border-color:var(--cor-borda);border-top-color:var(--cor-secundaria);margin:auto;"></div></div>`;

  const [dados, prontidao] = await Promise.all([
    _carregarDados(),
    _carregarProntidao(),
  ]);

  if (!dados) {
    el.innerHTML = `<div class="estado-vazio"><div class="estado-vazio-emoji">⚠️</div><div class="estado-vazio-texto">Erro ao carregar dados do edital.</div></div>`;
    return;
  }

  _renderHome(el, dados, prontidao);
}

/* ── Dados ───────────────────────────────────────────────────── */
async function _carregarDados() {
  try {
    const r = await fetch('./data/edital.json');
    return await r.json();
  } catch {
    return null;
  }
}

async function _carregarProntidao() {
  const usuario = obterUsuario();
  if (!usuario) return {};

  const contagem = { basicos: 0, complementares: 0, especificos: 0 };
  try {
    const snap = await getDocs(collection(db, 'users', usuario.uid, 'questoesStatus'));
    snap.forEach(d => {
      const { bloco, respondida } = d.data();
      if (respondida && contagem[bloco] !== undefined) contagem[bloco]++;
    });
  } catch {
    // offline
  }
  return contagem;
}

/* ── Render ──────────────────────────────────────────────────── */
function _renderHome(el, dados, prontidao) {
  const semEdital = dados.status === 'sem_edital';
  const total = dados.estrutura_prova.reduce((s, b) => s + b.qtd, 0);

  el.innerHTML = `
    <div class="painel-header" data-emoji="📋">
      <div class="painel-header-label">Edital</div>
      <div class="painel-header-titulo">Edital Ativo</div>
      <div class="painel-header-sub">Estrutura da prova · Referência do concurso</div>
    </div>

    ${semEdital ? _htmlBannerSemEdital(dados) : _htmlBannerAtivo(dados)}

    <!-- Estrutura da prova -->
    <div class="edt-secao-titulo">Estrutura da Prova Objetiva</div>
    <div class="edt-blocos">
      ${dados.estrutura_prova.map(b => _htmlBloco(b, prontidao[b.id] || 0)).join('')}
      <div class="edt-total-card">
        <span class="edt-total-label">Total de questões</span>
        <span class="edt-total-num">${total}</span>
      </div>
    </div>

    <!-- Minha prontidão -->
    <div class="edt-secao-titulo">Minha Prontidão</div>
    <div class="edt-prontidao">
      ${dados.estrutura_prova.map(b => _htmlProntidao(b, prontidao[b.id] || 0)).join('')}
    </div>

    <!-- Último edital de referência -->
    <div class="edt-secao-titulo">Último Edital de Referência</div>
    ${_htmlUltimoEdital(dados.ultimo_edital)}

    <!-- Histórico de bancas -->
    <div class="edt-secao-titulo">Histórico de Editais</div>
    <div class="edt-historico">
      ${dados.bancas_historico.map(b => _htmlHistoricoItem(b)).join('')}
    </div>

    <!-- Links de monitoramento -->
    <div class="edt-secao-titulo">Monitorar Novo Edital</div>
    <div class="edt-links">
      ${dados.links_monitoramento.map(l => _htmlLink(l)).join('')}
    </div>

    <div style="height:80px;"></div>
  `;
}

/* ── HTML helpers ────────────────────────────────────────────── */
function _htmlBannerSemEdital(dados) {
  return `
    <div class="edt-banner edt-banner-alerta">
      <div class="edt-banner-icone">⏳</div>
      <div class="edt-banner-corpo">
        <div class="edt-banner-titulo">Sem edital ativo</div>
        <div class="edt-banner-msg">${_esc(dados.mensagem)}</div>
      </div>
    </div>`;
}

function _htmlBannerAtivo(dados) {
  return `
    <div class="edt-banner edt-banner-ativo">
      <div class="edt-banner-icone">🔔</div>
      <div class="edt-banner-corpo">
        <div class="edt-banner-titulo">Edital em andamento!</div>
        <div class="edt-banner-msg">${_esc(dados.mensagem)}</div>
      </div>
    </div>`;
}

function _htmlBloco(b, respondidas) {
  return `
    <div class="edt-bloco-card">
      <div class="edt-bloco-sigla" style="background:${_esc(b.cor)};">${_esc(b.sigla)}</div>
      <div class="edt-bloco-info">
        <div class="edt-bloco-nome">${_esc(b.nome)}</div>
        <div class="edt-bloco-desc">${_esc(b.descricao)}</div>
      </div>
      <div class="edt-bloco-qtd">${b.qtd}<span>Q</span></div>
    </div>`;
}

function _htmlProntidao(b, respondidas) {
  // Usa qtd da prova como referência de cobertura desejada
  const meta = b.qtd * 3; // meta: 3× o nº de questões da prova
  const pct  = Math.min(100, Math.round(respondidas / meta * 100));
  const nivel = pct >= 80 ? 'alta' : pct >= 40 ? 'media' : 'baixa';
  const labels = { alta: 'Boa cobertura', media: 'Em progresso', baixa: 'Iniciar' };

  return `
    <div class="edt-pront-item">
      <div class="edt-pront-header">
        <span class="tag tag-bloco-${_esc(b.id)}">${_esc(b.sigla)}</span>
        <span class="edt-pront-nome">${_esc(b.nome)}</span>
        <span class="edt-pront-nivel edt-nivel-${nivel}">${labels[nivel]}</span>
      </div>
      <div class="barra-progresso-container">
        <div class="barra-progresso" style="width:${pct}%;background:${_esc(b.cor)};"></div>
      </div>
      <div class="edt-pront-detalhe">${respondidas} questões praticadas · meta sugerida: ${meta}</div>
    </div>`;
}

function _htmlUltimoEdital(e) {
  const linhas = [
    ['Banca',        e.banca],
    ['Número',       e.numero],
    ['Publicação',   _formatarData(e.publicacao)],
    ['Cargo',        e.cargo],
    ['Especialidade',e.especialidade],
    ['Jornada',      e.jornada],
    ['Tipo',         e.tipo],
    ['Vagas',        e.vagas],
    ['Inscrições',   e.periodo_inscricao],
    ['Prova',        e.prova_objetiva],
  ];

  return `
    <div class="edt-ref-card">
      <div class="edt-ref-titulo">${_esc(e.titulo)}</div>
      <div class="edt-ref-grid">
        ${linhas.map(([l, v]) => v ? `
          <div class="edt-ref-label">${_esc(l)}</div>
          <div class="edt-ref-valor">${_esc(v)}</div>` : '').join('')}
      </div>
    </div>`;
}

function _htmlHistoricoItem(b) {
  const corTipo = b.tipo === 'Efetivo'
    ? 'background:rgba(34,197,94,.12);color:#16a34a;'
    : 'background:rgba(59,130,246,.12);color:#2563eb;';
  return `
    <div class="edt-hist-item">
      <span class="edt-hist-ano">${b.ano}</span>
      <div class="edt-hist-info">
        <span class="edt-hist-nome">${_esc(b.nome)}</span>
        <span class="edt-hist-num">${_esc(b.numero)}</span>
      </div>
      <span class="edt-hist-tipo" style="${corTipo}">${_esc(b.tipo)}</span>
    </div>`;
}

function _htmlLink(l) {
  return `
    <a class="edt-link-card" href="${_esc(l.url)}" target="_blank" rel="noopener noreferrer">
      <span class="edt-link-nome">${_esc(l.nome)}</span>
      <span class="edt-link-seta">↗</span>
    </a>`;
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _formatarData(iso) {
  if (!iso) return '';
  const [ano, mes, dia] = iso.split('-');
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  return `${parseInt(dia, 10)} de ${meses[+mes - 1]} de ${ano}`;
}

function _esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
