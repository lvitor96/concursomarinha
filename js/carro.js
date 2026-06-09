/**
 * carro.js — Modo Carro
 * Reproduz resumos (versão curta) em áudio via Web Speech API (SpeechSynthesis).
 * Sem dependência externa. Funciona offline após primeiro carregamento.
 */

/* ── Estado ─────────────────────────────────────────────────── */
const M = {
  resumos:    [],       // todos os resumos carregados
  fila:       [],       // índices na ordem de reprodução
  indice:     0,        // posição atual na fila
  tocando:    false,
  utterance:  null,
  audioAtual: null,     // Audio element (Google TTS)
  filtroBloco:'',
};

const TTS_KEY_STORAGE   = 'sedf-tts-key';
const TTS_VOICE_STORAGE = 'sedf-tts-voice';
const DEFAULT_VOICE     = 'pt-BR-Neural2-B';
const TTS_KEY_DEFAULT   = 'AIzaSyBtPdRCRr5xsFuZ1xGleTfuV7YDJtXoPII';

const synth = window.speechSynthesis;

/* ── Entry point ─────────────────────────────────────────────── */
export async function iniciarCarro() {
  const el = document.getElementById('painel-carro');
  if (!el) return;

  el.innerHTML = `<div style="padding:32px;text-align:center;"><div class="spinner" style="border-color:var(--cor-borda);border-top-color:var(--cor-secundaria);margin:auto;"></div></div>`;

  if (!M.resumos.length) {
    try {
      const r = await fetch('./data/resumos.json');
      const d = await r.json();
      M.resumos = d.resumos || [];
    } catch {
      el.innerHTML = `<div class="estado-vazio"><div class="estado-vazio-emoji">⚠️</div><div class="estado-vazio-texto">Erro ao carregar resumos.</div></div>`;
      return;
    }
  }

  if (!synth && !localStorage.getItem(TTS_KEY_STORAGE) && !TTS_KEY_DEFAULT) {
    el.innerHTML = `<div class="estado-vazio"><div class="estado-vazio-emoji">🔇</div><div class="estado-vazio-texto">Seu navegador não suporta síntese de voz.<br>Configure uma chave Google Cloud TTS nas Configurações ou use Chrome/Edge/Safari.</div></div>`;
    return;
  }

  _pararTudo();
  _construirFila();
  _renderHome(el);
}

/* ── Fila ────────────────────────────────────────────────────── */
function _construirFila() {
  const lista = M.filtroBloco
    ? M.resumos.filter(r => r.bloco === M.filtroBloco)
    : [...M.resumos];

  // Ordena: alta → media → baixa
  const ordem = { alta: 0, media: 1, baixa: 2 };
  lista.sort((a, b) => (ordem[a.incidencia] ?? 2) - (ordem[b.incidencia] ?? 2));

  M.fila = lista;
  M.indice = 0;
}

/* ── Render ──────────────────────────────────────────────────── */
function _renderHome(el) {
  const total    = M.fila.length;
  const atual    = M.fila[M.indice];
  const ttsKey       = localStorage.getItem(TTS_KEY_STORAGE);
  const effectiveKey = ttsKey || TTS_KEY_DEFAULT;
  const ttsVoice     = localStorage.getItem(TTS_VOICE_STORAGE) || DEFAULT_VOICE;

  const bannerTTS = effectiveKey
    ? `<div style="margin:0 16px 12px;padding:10px 14px;background:var(--cor-sucesso-bg,#e8f5e9);border:1px solid var(--cor-sucesso);border-radius:var(--raio-sm);font-size:12px;color:var(--cor-texto);">
        🎙️ Google Cloud TTS ativo · Voz: <strong>${ttsVoice}</strong>${!ttsKey ? ' · <em>chave padrão</em>' : ''}
      </div>`
    : `<div style="margin:0 16px 12px;padding:10px 14px;background:var(--cor-atencao-bg);border:1px solid var(--cor-atencao);border-radius:var(--raio-sm);font-size:12px;color:var(--cor-texto);">
        ⚠️ Usando Web Speech API (voz do sistema). Configure uma <strong>Chave Google Cloud TTS</strong> nas <button onclick="app.navegarPara('config')" style="background:none;border:none;padding:0;cursor:pointer;font-size:12px;font-weight:700;color:var(--cor-primaria);text-decoration:underline;">Configurações</button> para voz mais natural.
      </div>`;

  el.innerHTML = `
    <div class="car-header">
      <div class="car-icone">🚗</div>
      <div class="car-titulo">Modo Carro</div>
      <div class="car-sub">Resumos em áudio — mãos livres</div>
    </div>
    ${bannerTTS}

    <!-- Filtro de bloco -->
    <div class="car-filtro-wrap">
      <button class="car-filtro-btn ${!M.filtroBloco ? 'ativo':''}" data-bloco="">Todos</button>
      <button class="car-filtro-btn ${M.filtroBloco==='basicos' ? 'ativo':''}" data-bloco="basicos">CB — Básicos</button>
      <button class="car-filtro-btn ${M.filtroBloco==='complementares' ? 'ativo':''}" data-bloco="complementares">CC — Compl.</button>
      <button class="car-filtro-btn ${M.filtroBloco==='especificos' ? 'ativo':''}" data-bloco="especificos">CE — Música</button>
    </div>

    <!-- Card do conteúdo atual -->
    <div class="car-card" id="car-card">
      ${atual ? _htmlCard(atual, M.indice, total) : '<div class="car-vazio">Nenhum resumo disponível.</div>'}
    </div>

    <!-- Controles de reprodução -->
    <div class="car-controles">
      <button class="car-btn car-btn-prev" id="car-prev" ${M.indice === 0 ? 'disabled' : ''}>
        <span>⏮</span><span class="car-btn-label">Anterior</span>
      </button>
      <button class="car-btn car-btn-play" id="car-play">
        <span id="car-play-icone">${M.tocando ? '⏸' : '▶'}</span>
        <span class="car-btn-label" id="car-play-label">${M.tocando ? 'Pausar' : 'Reproduzir'}</span>
      </button>
      <button class="car-btn car-btn-next" id="car-next" ${M.indice >= total - 1 ? 'disabled' : ''}>
        <span>⏭</span><span class="car-btn-label">Próximo</span>
      </button>
    </div>

    <!-- Barra de progresso da fila -->
    <div class="car-progresso-wrap">
      <div class="car-progresso-info">
        <span>${M.indice + 1} de ${total} resumos</span>
        <span id="car-status-txt" class="car-status">${M.tocando ? '🔊 Reproduzindo…' : '⏹ Parado'}</span>
      </div>
      <div class="barra-progresso-container">
        <div class="barra-progresso" id="car-barra" style="width:${total > 1 ? Math.round(M.indice/(total-1)*100) : 100}%;background:var(--cor-acento);"></div>
      </div>
    </div>

    <!-- Lista de resumos -->
    <div class="car-lista-titulo">Fila de reprodução</div>
    <div class="car-lista" id="car-lista">
      ${M.fila.map((r, i) => _htmlItemLista(r, i)).join('')}
    </div>
    <div style="height:80px;"></div>
  `;

  _bindControles(el);
  _bindFiltros(el);
  _bindLista(el);
  _scrollParaAtivo(el);
}

function _htmlCard(resumo, idx, total) {
  const texto = _limparMarkdown(resumo.versaoCurta || resumo.versaoCompleta || resumo.nome);
  const incLabel = { alta: '🔴 Alta incidência', media: '🟡 Média', baixa: '🟢 Baixa' }[resumo.incidencia] || '';
  return `
    <div class="car-card-titulo">${_esc(resumo.nome)}</div>
    <div class="car-card-meta">
      <span class="tag tag-bloco-${_esc(resumo.bloco)}">${_blocoSigla(resumo.bloco)}</span>
      <span class="car-incidencia">${incLabel}</span>
    </div>
    <div class="car-card-texto" id="car-texto">${_esc(texto.slice(0, 300))}…</div>`;
}

function _htmlItemLista(resumo, idx) {
  const ativo = idx === M.indice;
  return `
    <button class="car-lista-item ${ativo ? 'ativo' : ''}" data-idx="${idx}">
      <span class="car-lista-num">${idx + 1}</span>
      <div class="car-lista-info">
        <div class="car-lista-nome">${_esc(resumo.nome)}</div>
        <span class="tag tag-bloco-${_esc(resumo.bloco)}" style="font-size:9px;">${_blocoSigla(resumo.bloco)}</span>
      </div>
      ${ativo && M.tocando ? '<span class="car-lista-tocando">🔊</span>' : ''}
    </button>`;
}

/* ── Controles ───────────────────────────────────────────────── */
function _bindControles(el) {
  el.querySelector('#car-play')?.addEventListener('click', _togglePlay);
  el.querySelector('#car-prev')?.addEventListener('click', () => _irPara(M.indice - 1, el));
  el.querySelector('#car-next')?.addEventListener('click', () => _irPara(M.indice + 1, el));
}

function _bindFiltros(el) {
  el.querySelectorAll('.car-filtro-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      _pararTudo();
      M.filtroBloco = btn.dataset.bloco;
      _construirFila();
      _renderHome(el);
    });
  });
}

function _bindLista(el) {
  el.querySelectorAll('.car-lista-item').forEach(btn => {
    btn.addEventListener('click', () => {
      _irPara(parseInt(btn.dataset.idx, 10), el);
    });
  });
}

function _togglePlay() {
  if (M.tocando) {
    _pausar();
  } else {
    _reproduzir();
  }
}

async function _sintetizarAudio(texto) {
  const key   = localStorage.getItem(TTS_KEY_STORAGE) || TTS_KEY_DEFAULT;
  if (!key) return null;
  const voice = localStorage.getItem(TTS_VOICE_STORAGE) || DEFAULT_VOICE;
  const resp  = await fetch(
    `https://texttospeech.googleapis.com/v1/text:synthesize?key=${key}`,
    {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        input:       { text: texto },
        voice:       { languageCode: 'pt-BR', name: voice },
        audioConfig: { audioEncoding: 'MP3' },
      }),
    }
  );
  if (!resp.ok) throw new Error(`TTS API error: ${resp.status}`);
  const data = await resp.json();
  return data.audioContent; // base64 MP3
}

async function _reproduzir() {
  const resumo = M.fila[M.indice];
  if (!resumo) return;

  const texto     = _limparMarkdown(resumo.versaoCurta || resumo.nome);
  const textoFull = `${resumo.nome}. ${texto}`;

  _pararTudo();
  M.tocando = true;
  _atualizarUI();

  // Tenta Google Cloud TTS primeiro
  try {
    const b64 = await _sintetizarAudio(textoFull);
    if (b64) {
      const audio = new Audio(`data:audio/mp3;base64,${b64}`);
      M.audioAtual = audio;
      audio.onended = () => {
        M.tocando    = false;
        M.audioAtual = null;
        _atualizarUI();
        if (M.indice < M.fila.length - 1) {
          M.indice++;
          _atualizarUI();
          setTimeout(_reproduzir, 800);
        }
      };
      audio.onerror = () => {
        M.tocando    = false;
        M.audioAtual = null;
        _atualizarUI();
      };
      audio.play();
      return;
    }
  } catch (err) {
    console.warn('Google TTS falhou, usando Web Speech API:', err);
  }

  // Fallback: Web Speech API
  if (!synth) {
    M.tocando = false;
    _atualizarUI();
    return;
  }

  const utt = new SpeechSynthesisUtterance(textoFull);
  utt.lang  = 'pt-BR';
  utt.rate  = 1.0;
  utt.pitch = 1.0;

  utt.onstart = () => {
    M.utterance = utt;
    _atualizarUI();
  };

  utt.onend = () => {
    M.tocando   = false;
    M.utterance = null;
    _atualizarUI();
    if (M.indice < M.fila.length - 1) {
      M.indice++;
      _atualizarUI();
      setTimeout(_reproduzir, 800);
    }
  };

  utt.onerror = () => {
    M.tocando   = false;
    M.utterance = null;
    _atualizarUI();
  };

  synth.speak(utt);
}

function _pausar() {
  if (M.audioAtual) {
    M.audioAtual.pause();
    M.audioAtual = null;
  } else if (synth?.speaking) {
    synth.cancel();
  }
  M.tocando   = false;
  M.utterance = null;
  _atualizarUI();
}

function _pararTudo() {
  if (M.audioAtual) {
    M.audioAtual.pause();
    M.audioAtual = null;
  }
  if (synth) synth.cancel();
  M.tocando   = false;
  M.utterance = null;
}

function _irPara(idx, el) {
  _pararTudo();
  M.indice = Math.max(0, Math.min(idx, M.fila.length - 1));
  _renderHome(el);
}

/* ── Atualização parcial da UI ──────────────────────────────── */
function _atualizarUI() {
  const playBtn    = document.getElementById('car-play');
  const playIcone  = document.getElementById('car-play-icone');
  const playLabel  = document.getElementById('car-play-label');
  const statusTxt  = document.getElementById('car-status-txt');
  const barra      = document.getElementById('car-barra');
  const lista      = document.getElementById('car-lista');
  const prevBtn    = document.getElementById('car-prev');
  const nextBtn    = document.getElementById('car-next');
  const card       = document.getElementById('car-card');
  const total      = M.fila.length;

  if (playIcone) playIcone.textContent = M.tocando ? '⏸' : '▶';
  if (playLabel) playLabel.textContent  = M.tocando ? 'Pausar' : 'Reproduzir';
  if (statusTxt) statusTxt.textContent  = M.tocando ? '🔊 Reproduzindo…' : '⏹ Parado';
  if (barra)     barra.style.width      = total > 1 ? `${Math.round(M.indice/(total-1)*100)}%` : '100%';
  if (prevBtn)   prevBtn.disabled       = M.indice === 0;
  if (nextBtn)   nextBtn.disabled       = M.indice >= total - 1;

  if (card && M.fila[M.indice]) {
    card.innerHTML = _htmlCard(M.fila[M.indice], M.indice, total);
  }

  if (lista) {
    lista.innerHTML = M.fila.map((r, i) => _htmlItemLista(r, i)).join('');
    _bindLista(document.getElementById('painel-carro'));
    _scrollParaAtivo(document.getElementById('painel-carro'));
  }
}

function _scrollParaAtivo(el) {
  if (!el) return;
  const ativo = el.querySelector('.car-lista-item.ativo');
  if (ativo) setTimeout(() => ativo.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 100);
}

/* ── Utilitários ─────────────────────────────────────────────── */
function _limparMarkdown(texto) {
  return String(texto || '')
    .replace(/#{1,6}\s/g, '')       // remove headings
    .replace(/\*\*(.*?)\*\*/g, '$1') // bold
    .replace(/\*(.*?)\*/g, '$1')     // italic
    .replace(/`(.*?)`/g, '$1')       // code
    .replace(/^[-*•]\s/gm, '. ')     // bullets
    .replace(/\n+/g, '. ')           // newlines
    .replace(/\.{2,}/g, '.')         // double dots
    .trim();
}

function _blocoSigla(bloco) {
  return { basicos: 'CB', complementares: 'CC', especificos: 'CE' }[bloco] || bloco;
}

function _esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
