/**
 * estatisticas.js — Painel de Estatísticas
 * Fontes: cronograma/log, questoesStatus, progresso, daily/*, simulados
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import {
  doc, getDoc, collection, getDocs,
  query, orderBy, limit,
} from 'firebase/firestore';

export async function iniciarEstatisticas() {
  const el = document.getElementById('painel-estatisticas');
  if (!el) return;

  _renderizarEsqueleto(el);

  const usuario = obterUsuario();
  if (!usuario) return;

  const [logRes, statusRes, progressoRes, dailyRes, simRes, questoesRes] = await Promise.allSettled([
    getDoc(doc(db, 'users', usuario.uid, 'cronograma', 'log')),
    getDocs(collection(db, 'users', usuario.uid, 'questoesStatus')),
    getDocs(collection(db, 'users', usuario.uid, 'progresso')),
    getDocs(collection(db, 'users', usuario.uid, 'daily')),
    getDocs(query(collection(db, 'users', usuario.uid, 'simulados'), orderBy('data', 'desc'), limit(3))),
    fetch('./data/questoes.json').then(r => r.json()),
  ]);

  const log         = logRes.status === 'fulfilled' && logRes.value.exists() ? logRes.value.data() : {};
  const statusDocs  = statusRes.status    === 'fulfilled' ? statusRes.value.docs    : [];
  const progDocs    = progressoRes.status === 'fulfilled' ? progressoRes.value.docs : [];
  const dailyDocs   = dailyRes.status     === 'fulfilled' ? dailyRes.value.docs     : [];
  const simDocs     = simRes.status       === 'fulfilled' ? simRes.value.docs       : [];
  const questoes    = questoesRes.status  === 'fulfilled' ? (questoesRes.value.questoes ?? []) : [];

  _renderizarDados(el, { log, statusDocs, progDocs, dailyDocs, simDocs, questoes });
}

/* ── Esqueleto ───────────────────────────────────────────────── */
function _renderizarEsqueleto(el) {
  el.innerHTML = `
    <div class="painel-header" data-emoji="📊">
      <div class="painel-header-label">Estatísticas</div>
      <div class="painel-header-titulo">Seu progresso</div>
      <div class="painel-header-sub">Carregando dados…</div>
    </div>
    <div style="padding:32px;text-align:center;">
      <div class="spinner" style="border-color:var(--cor-borda);border-top-color:var(--cor-secundaria);margin:auto;"></div>
    </div>
  `;
}

/* ── Renderização principal ──────────────────────────────────── */
function _renderizarDados(el, { log, statusDocs, progDocs, dailyDocs, simDocs, questoes }) {
  const hoje = new Date().toISOString().slice(0, 10);

  // ── Streak ──────────────────────────────────────────────────
  const streak = _calcularStreak(log, hoje);

  // ── Horas totais ─────────────────────────────────────────────
  const minutosTotais = Object.entries(log)
    .filter(([k]) => k !== '_ts')
    .reduce((s, [, v]) => s + (v?.minutos ?? 0), 0);
  const horasStr = minutosTotais >= 60
    ? `${Math.floor(minutosTotais / 60)}h${minutosTotais % 60 > 0 ? (minutosTotais % 60) + 'm' : ''}`
    : `${minutosTotais}m`;

  // ── Questões únicas respondidas + acerto ─────────────────────
  let totalRespondidas = 0, totalAcertos = 0;
  const respondidosPorBloco = { basicos: 0, complementares: 0, especificos: 0 };
  const acertosPorBloco     = { basicos: 0, complementares: 0, especificos: 0 };
  statusDocs.forEach(d => {
    const data = d.data();
    if (data.respondida) {
      totalRespondidas++;
      if (data.correta) totalAcertos++;
      if (respondidosPorBloco[data.bloco] !== undefined) {
        respondidosPorBloco[data.bloco]++;
        if (data.correta) acertosPorBloco[data.bloco]++;
      }
    }
  });
  const acertoGeralPct = totalRespondidas > 0 ? Math.round(totalAcertos / totalRespondidas * 100) : 0;

  // ── Totais do banco por bloco ─────────────────────────────────
  const totalPorBloco = { basicos: 0, complementares: 0, especificos: 0 };
  questoes.forEach(q => { if (totalPorBloco[q.bloco] !== undefined) totalPorBloco[q.bloco]++; });

  // ── Últimos 14 dias (questões respondidas/dia) ────────────────
  const daily14 = _ultimos14Dias(dailyDocs);

  // ── Tópicos a reforçar ────────────────────────────────────────
  const topicosReforco = _topicosParaReforcar(progDocs);

  // ── Heatmap ───────────────────────────────────────────────────
  const heatmap = _gerarHeatmap(log);

  el.innerHTML = `
    <div class="painel-header" data-emoji="📊">
      <div class="painel-header-label">Estatísticas</div>
      <div class="painel-header-titulo">Seu progresso</div>
      <div class="painel-header-sub">Baseado nos seus dados de estudo</div>
    </div>

    <!-- Heatmap -->
    ${_htmlHeatmap(heatmap)}

    <!-- Stat cards -->
    <div class="est-stats-grid">
      ${_statCard(horasStr,                 'Horas estudadas',     'var(--cor-secundaria)')}
      ${_statCard(streak > 0 ? streak + ' 🔥' : '0', 'Sequência de dias', 'var(--cor-acento)')}
      ${_statCard(totalRespondidas,         'Questões únicas',     'var(--cor-primaria)')}
      ${_statCard(totalRespondidas > 0 ? acertoGeralPct + '%' : '—', 'Acerto geral', acertoGeralPct >= 81 ? 'var(--cor-sucesso)' : acertoGeralPct >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)')}
    </div>

    <!-- Por bloco -->
    <div class="secao">
      <div class="secao-header"><h3 class="secao-titulo">Progresso por Bloco</h3></div>
      <div class="card" style="padding:14px;">
        ${_htmlBlocos(respondidosPorBloco, acertosPorBloco, totalPorBloco)}
      </div>
    </div>

    <!-- Últimos 14 dias -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Últimos 14 dias — questões/dia</h3></div>
      <div class="card" style="padding:14px 14px 28px;">
        ${_htmlBarrasV(daily14)}
      </div>
    </div>

    <!-- Tópicos a reforçar -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Tópicos para reforçar</h3></div>
      <div class="card" style="padding:0;">
        ${topicosReforco.length
          ? topicosReforco.map(t => _htmlTopicoItem(t)).join('')
          : '<p class="est-vazio">Responda pelo menos 5 questões por tópico para ver o ranking.</p>'}
      </div>
    </div>

    <!-- Últimos simulados -->
    <div class="secao" style="padding-top:0;">
      <div class="secao-header"><h3 class="secao-titulo">Últimos simulados</h3></div>
      <div class="card" style="padding:0;margin-bottom:80px;">
        ${simDocs.length
          ? simDocs.map(d => _htmlSimItem(d.data())).join('')
          : '<p class="est-vazio">Nenhum simulado realizado ainda.</p>'}
      </div>
    </div>
  `;
}

/* ── Heatmap ─────────────────────────────────────────────────── */
function _gerarHeatmap(log) {
  // Começa no domingo 11 semanas atrás
  const hoje = new Date();
  const domInicio = new Date(hoje);
  domInicio.setDate(hoje.getDate() - hoje.getDay() - 11 * 7);
  domInicio.setHours(12, 0, 0, 0);

  const semanas = [];
  for (let w = 0; w < 12; w++) {
    const semana = [];
    for (let d = 0; d < 7; d++) {
      const dia = new Date(domInicio);
      dia.setDate(domInicio.getDate() + w * 7 + d);
      const key      = dia.toISOString().slice(0, 10);
      const diaSem   = dia.getDay();
      const esSab    = diaSem === 6;
      const futuro   = dia > hoje;
      const minutos  = !esSab && !futuro ? (log[key]?.minutos ?? 0) : null;
      const level    = minutos === null ? null
                      : minutos === 0   ? 0
                      : minutos <= 30   ? 1
                      : minutos <= 60   ? 2
                      : minutos <= 120  ? 3
                      : 4;
      semana.push({ key, diaSem, esSab, futuro, minutos, level });
    }
    semanas.push(semana);
  }
  return semanas;
}

function _htmlHeatmap(semanas) {
  // Gera células na ordem correta para grid-auto-flow: column
  // 6 linhas (Dom=0…Sex=5), 12 colunas (semanas)
  const DIAS = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex'];
  const diasLabels = DIAS.map(d =>
    `<div class="est-heatmap-day-label">${d}</div>`
  ).join('');

  // Coleta as células em ordem: para cada semana, para cada dia Dom-Sex
  const celulas = [];
  semanas.forEach(semana => {
    semana
      .filter(c => !c.esSab)
      .forEach(c => {
        const attrs = c.futuro
          ? 'data-futuro="true"'
          : c.level !== null
          ? `data-level="${c.level}" title="${c.key}: ${c.minutos ?? 0} min"`
          : '';
        celulas.push(`<div class="est-cell" ${attrs}></div>`);
      });
  });

  return `
    <div class="est-heatmap-wrap">
      <div class="est-heatmap-titulo">Atividade — últimas 12 semanas</div>
      <div class="est-heatmap-body">
        <div class="est-heatmap-days">${diasLabels}</div>
        <div class="est-heatmap-grid">${celulas.join('')}</div>
      </div>
      <div class="est-heatmap-legenda">
        <span>Menos</span>
        <div class="est-heatmap-legenda-celula" style="background:var(--cor-borda);"></div>
        <div class="est-heatmap-legenda-celula" style="background:#bbf7d0;"></div>
        <div class="est-heatmap-legenda-celula" style="background:#4ade80;"></div>
        <div class="est-heatmap-legenda-celula" style="background:#16a34a;"></div>
        <div class="est-heatmap-legenda-celula" style="background:#14532d;"></div>
        <span>Mais</span>
      </div>
    </div>`;
}

/* ── Stat cards ──────────────────────────────────────────────── */
function _statCard(valor, label, cor) {
  return `
    <div class="est-stat-card">
      <div class="est-stat-valor" style="color:${cor};">${valor}</div>
      <div class="est-stat-label">${label}</div>
    </div>`;
}

/* ── Por bloco ───────────────────────────────────────────────── */
function _htmlBlocos(respondidos, acertos, totais) {
  const blocos = [
    { key: 'basicos',        sigla: 'CB', nome: 'Conhecimentos Básicos' },
    { key: 'complementares', sigla: 'CC', nome: 'Conhecimentos Complementares' },
    { key: 'especificos',    sigla: 'CE', nome: 'Conhecimentos Específicos' },
  ];

  return blocos.map(b => {
    const cobertura = totais[b.key] > 0 ? Math.round(respondidos[b.key] / totais[b.key] * 100) : 0;
    const acerto    = respondidos[b.key] > 0 ? Math.round(acertos[b.key] / respondidos[b.key] * 100) : 0;
    const corAcerto = acerto >= 81 ? 'var(--cor-sucesso)' : acerto >= 70 ? 'var(--cor-atencao)' : acerto > 0 ? 'var(--cor-erro)' : 'var(--cor-texto-leve)';

    return `
      <div class="est-bloco-item">
        <div class="est-bloco-header">
          <div class="est-bloco-nome">
            <span class="tag tag-bloco-${b.key}">${b.sigla}</span>
            ${b.nome}
          </div>
        </div>
        <div class="est-barra-dupla">
          <div class="est-barra-row">
            <span class="est-barra-tipo">Cobertura</span>
            <div class="est-barra-track">
              <div class="est-barra-fill" style="width:${cobertura}%;background:var(--cor-primaria);"></div>
            </div>
            <span style="font-size:11px;font-weight:700;color:var(--cor-primaria);width:36px;text-align:right;">${cobertura}%</span>
          </div>
          <div class="est-barra-row">
            <span class="est-barra-tipo">Acerto</span>
            <div class="est-barra-track">
              <div class="est-barra-fill" style="width:${acerto}%;background:${corAcerto};"></div>
            </div>
            <span style="font-size:11px;font-weight:700;color:${corAcerto};width:36px;text-align:right;">${respondidos[b.key] > 0 ? acerto + '%' : '—'}</span>
          </div>
        </div>
      </div>`;
  }).join('');
}

/* ── Últimos 14 dias ─────────────────────────────────────────── */
function _ultimos14Dias(dailyDocs) {
  const map = {};
  dailyDocs.forEach(d => { map[d.id] = d.data().respondidas ?? 0; });

  const dias = [];
  for (let i = 13; i >= 0; i--) {
    const d = new Date();
    d.setDate(d.getDate() - i);
    const key = d.toISOString().slice(0, 10);
    dias.push({ key, val: map[key] ?? 0, label: `${d.getDate()}/${d.getMonth() + 1}` });
  }
  return dias;
}

function _htmlBarrasV(dias) {
  const max = Math.max(...dias.map(d => d.val), 1);
  return `
    <div class="est-barras-v">
      ${dias.map(d => {
        const pct = Math.round(d.val / max * 100);
        return `
          <div class="est-barra-v-wrap">
            <div class="est-barra-v" style="height:${Math.max(pct, 2)}%;" title="${d.key}: ${d.val} questões"></div>
            <span class="est-barra-v-label">${d.label}</span>
          </div>`;
      }).join('')}
    </div>`;
}

/* ── Tópicos a reforçar ──────────────────────────────────────── */
function _topicosParaReforcar(progDocs) {
  return progDocs
    .map(d => ({ id: d.id, ...d.data() }))
    .filter(t => (t.respondidas ?? 0) >= 5)
    .sort((a, b) => (a.percentualAcerto ?? 100) - (b.percentualAcerto ?? 100))
    .slice(0, 5);
}

function _htmlTopicoItem(t) {
  const pct = t.percentualAcerto ?? 0;
  const cor = pct >= 81 ? 'var(--cor-sucesso)' : pct >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)';
  return `
    <div class="est-topico-item">
      <div class="est-topico-nome" title="${t.id}">${_formatarTopicoId(t.id)}</div>
      <div class="est-topico-qtd">${t.acertos ?? 0}/${t.respondidas ?? 0}</div>
      <div class="est-topico-pct" style="color:${cor};">${pct}%</div>
    </div>`;
}

function _formatarTopicoId(id) {
  // 'pt-gramatica' → 'Pt — Gramatica'
  return id
    .split('-')
    .map(p => p.charAt(0).toUpperCase() + p.slice(1))
    .join(' — ');
}

/* ── Simulados ───────────────────────────────────────────────── */
function _htmlSimItem(h) {
  const pct  = h.pct ?? 0;
  const cor  = pct >= 81 ? 'var(--cor-sucesso)' : pct >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)';
  const data = h.data?.toDate
    ? h.data.toDate().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: '2-digit' })
    : '—';
  const blocos = h.porBloco
    ? Object.entries(h.porBloco)
        .filter(([, d]) => d.total > 0)
        .map(([b, d]) => {
          const p = Math.round(d.acertos / d.total * 100);
          return `${_sigla(b)} ${p}%`;
        })
        .join(' · ')
    : '';
  return `
    <div class="est-sim-item">
      <div class="est-sim-pct" style="color:${cor};">${pct}%</div>
      <div class="est-sim-info">
        <div class="est-sim-data">${data} · ${h.total ?? 0} questões · ${_formatarTempo(h.tempoUsado ?? 0)}</div>
        <div class="est-sim-detalhe">${blocos}</div>
      </div>
    </div>`;
}

/* ── Streak ──────────────────────────────────────────────────── */
function _calcularStreak(log, hoje) {
  const cur = new Date(hoje + 'T12:00:00');
  if (!log[hoje]?.minutos) cur.setDate(cur.getDate() - 1);
  let streak = 0;
  for (let i = 0; i < 366; i++) {
    const key = cur.toISOString().slice(0, 10);
    if (log[key]?.minutos > 0) { streak++; cur.setDate(cur.getDate() - 1); }
    else break;
  }
  return streak;
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _sigla(b) {
  return { basicos: 'CB', complementares: 'CC', especificos: 'CE' }[b] ?? b;
}

function _formatarTempo(seg) {
  const h = Math.floor(seg / 3600);
  const m = Math.floor((seg % 3600) / 60);
  if (h > 0) return `${h}h${m > 0 ? m + 'm' : ''}`;
  return `${m}min`;
}
