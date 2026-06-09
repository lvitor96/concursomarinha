/**
 * questoes.js — Módulo: Banco de Questões
 * Modos: Treino (feedback imediato) | Simulado (cronometrado) | Revisão (erros/dúvidas)
 */

import { db } from './firebase.js';
import { obterUsuario } from './auth.js';
import {
  doc, setDoc, getDoc, collection, getDocs,
  serverTimestamp, writeBatch, increment,
} from 'firebase/firestore';

/* ═══════════════════════════════════════════════
   ESTADO DO MÓDULO
   ═══════════════════════════════════════════════ */
const M = {
  todos: [],         // todas as questões carregadas do JSON
  marcacoes: {},     // { questaoId: 'facil'|'duvida'|'errei'|'importante' } — Firestore
  progresso: {},     // { topicoId: { respondidas, acertos } } — Firestore
  carregado: false,

  filtros: {
    blocos: [],       // [] = todos
    disciplina: '',
    banca: '',
    incidencia: '',
    quantidade: 10,
    modo: 'treino',   // 'treino'|'simulado'|'revisao'
  },

  sessao: {
    modo: null,
    questoes: [],
    atual: 0,
    respostas: {},    // { questaoId: { escolhida, correta, tempo, marcacao } }
    timerInterval: null,
    tempoTotal: 12600, // 3h30min em segundos
    tempoRestante: 12600,
    iniciada: false,
    finalizada: false,
    tempoInicio: null,
  },
};

/* ═══════════════════════════════════════════════
   INICIALIZAÇÃO
   ═══════════════════════════════════════════════ */
export async function iniciarQuestoes() {
  if (!M.carregado) {
    await Promise.all([_carregarQuestoes(), _carregarDadosUsuario()]);
    M.carregado = true;
  }
  _renderizarView('menu');
}

async function _carregarQuestoes() {
  try {
    const res = await fetch('./data/questoes.json');
    const dados = await res.json();
    M.todos = dados.questoes || [];
  } catch (e) {
    console.error('Erro ao carregar questões:', e);
    M.todos = [];
  }
}

async function _carregarDadosUsuario() {
  const usuario = obterUsuario();
  if (!usuario) return;

  try {
    const [marcacoesSnap, progressoSnap] = await Promise.all([
      getDocs(collection(db, 'users', usuario.uid, 'questoesStatus')),
      getDocs(collection(db, 'users', usuario.uid, 'progresso')),
    ]);

    marcacoesSnap.forEach(d => { M.marcacoes[d.id] = d.data().marcacao; });
    progressoSnap.forEach(d => { M.progresso[d.id] = d.data(); });
  } catch (e) {
    // offline — dados ficam em cache do Firestore
    console.warn('Carregando dados offline:', e);
  }
}

/* ═══════════════════════════════════════════════
   ROTEADOR DE VIEWS
   ═══════════════════════════════════════════════ */
function _renderizarView(view) {
  const painel = document.getElementById('painel-questoes');
  if (!painel) return;

  // Remove listeners antigos clonando o nó
  const novo = painel.cloneNode(false);
  painel.parentNode.replaceChild(novo, painel);
  const el = document.getElementById('painel-questoes');

  switch (view) {
    case 'menu':     el.innerHTML = _htmlMenu();    _bindMenu(el);    break;
    case 'questao':  el.innerHTML = _htmlQuestao(); _bindQuestao(el); break;
    case 'resultado-treino': el.innerHTML = _htmlResultadoTreino(); _bindResultadoTreino(el); break;
    case 'analise':  el.innerHTML = _htmlAnalise(); _bindAnalise(el); break;
  }

  el.scrollTop = 0;
}

/* ═══════════════════════════════════════════════
   VIEW: MENU
   ═══════════════════════════════════════════════ */
function _htmlMenu() {
  const modoApp = document.body.dataset.modo;
  const total = M.todos.length;
  const respondidas = Object.values(M.progresso).reduce((a, p) => a + (p.respondidas || 0), 0);
  const acertos    = Object.values(M.progresso).reduce((a, p) => a + (p.acertos || 0), 0);
  const pctAcerto  = respondidas > 0 ? Math.round(acertos / respondidas * 100) : 0;
  const classeAcerto = pctAcerto >= 81 ? 'sucesso' : pctAcerto >= 70 ? 'atencao' : pctAcerto > 0 ? 'erro' : '';
  const revisaoPendente = Object.values(M.marcacoes).filter(m => m === 'errei' || m === 'duvida').length;

  const modoCarro = modoApp === 'carro';
  if (modoCarro) {
    return `
      <div class="painel-header" data-emoji="❓">
        <div class="painel-header-label">Banco de Questões</div>
        <div class="painel-header-titulo">Questões</div>
      </div>
      <div class="q-aviso-carro">
        <div style="font-size:48px;">🚗</div>
        <div style="font-family:var(--fonte-titulo);font-size:18px;font-weight:700;color:var(--cor-texto);">Modo Carro ativo</div>
        <div style="font-size:14px;color:var(--cor-texto-leve);max-width:260px;line-height:1.6;">
          Questões requerem atenção visual. Mude para <strong>Modo Mesa</strong> ou <strong>Modo Metrô</strong> para praticar.
        </div>
        <button class="btn btn-primario btn-sm" id="q-btn-mudar-modo">Mudar modo de estudo</button>
      </div>`;
  }

  const qtdModoMetro = modoApp === 'metro' ? 10 : null;

  return `
    <div class="painel-header" data-emoji="❓">
      <div class="painel-header-label">Banco de Questões</div>
      <div class="painel-header-titulo">Questões</div>
      <div class="painel-header-sub">${total} questões disponíveis</div>
    </div>

    <!-- Stats -->
    <div class="q-stats">
      <div class="q-stat">
        <div class="q-stat-num">${respondidas}</div>
        <div class="q-stat-label">Respondidas</div>
      </div>
      <div class="q-stat">
        <div class="q-stat-num ${classeAcerto}">${respondidas > 0 ? pctAcerto + '%' : '—'}</div>
        <div class="q-stat-label">Acerto</div>
      </div>
      <div class="q-stat">
        <div class="q-stat-num ${revisaoPendente > 0 ? 'atencao' : ''}">${revisaoPendente}</div>
        <div class="q-stat-label">p/ Revisar</div>
      </div>
    </div>

    <!-- Modos -->
    <div class="secao" style="padding-top:0">
      <div class="secao-header">
        <h3 class="secao-titulo">Modo de estudo</h3>
      </div>
      <div class="q-menu-modos">
        <button class="q-modo-card ativo" data-modo-treino="treino">
          <span class="q-modo-emoji">🎓</span>
          <span class="q-modo-nome">Treino</span>
          <span class="q-modo-sub">Gabarito imediato</span>
        </button>
        ${modoApp !== 'metro' ? `
        <button class="q-modo-card" data-modo-treino="simulado">
          <span class="q-modo-emoji">⏱️</span>
          <span class="q-modo-nome">Simulado</span>
          <span class="q-modo-sub">3h30 cronometrado</span>
        </button>` : ''}
        <button class="q-modo-card ${revisaoPendente === 0 ? 'desabilitado' : ''}" data-modo-treino="revisao" ${revisaoPendente === 0 ? 'disabled' : ''}>
          <span class="q-modo-emoji">🔄</span>
          <span class="q-modo-nome">Revisão</span>
          <span class="q-modo-sub">${revisaoPendente} p/ revisar</span>
        </button>
      </div>
    </div>

    <!-- Filtros por bloco -->
    <div class="q-filtros-section">
      <div class="q-filtros-titulo">Filtrar por bloco</div>
      <div class="q-filtros-chips" id="chips-bloco">
        <button class="q-chip ativo" data-bloco="">Todos</button>
        <button class="q-chip basicos" data-bloco="basicos">Básicos (CB)</button>
        <button class="q-chip complementares" data-bloco="complementares">Complementares (CC)</button>
        <button class="q-chip especificos" data-bloco="especificos">Específicos (CE)</button>
      </div>
    </div>

    <!-- Filtros por incidência -->
    <div class="q-filtros-section">
      <div class="q-filtros-titulo">Filtrar por incidência</div>
      <div class="q-filtros-chips" id="chips-incidencia">
        <button class="q-chip ativo" data-incidencia="">Todas</button>
        <button class="q-chip" data-incidencia="alta" style="border-color:var(--cor-incidencia-alta)">🔴 Alta</button>
        <button class="q-chip" data-incidencia="media" style="border-color:var(--cor-incidencia-media)">🟡 Média</button>
        <button class="q-chip" data-incidencia="baixa">⚪ Baixa</button>
      </div>
    </div>

    <!-- Filtros por banca -->
    <div class="q-filtros-section">
      <div class="q-filtros-titulo">Filtrar por banca</div>
      <div class="q-filtros-chips" id="chips-banca">
        <button class="q-chip ativo" data-banca="">Todas</button>
        <button class="q-chip" data-banca="quadrix-2022">Quadrix 2022 ★</button>
        <button class="q-chip" data-banca="quadrix-2025">Quadrix 2025</button>
        <button class="q-chip" data-banca="iades-2023">IADES 2023</button>
        <button class="q-chip" data-banca="quadrix-2021">Quadrix 2021</button>
      </div>
    </div>

    <!-- Quantidade -->
    <div class="q-filtros-section">
      <div class="q-select-row">
        <span class="q-select-label">Quantidade de questões</span>
        <select class="q-select" id="select-quantidade">
          ${modoApp === 'metro' ? '<option value="5">5 questões</option>' : ''}
          <option value="10" ${M.filtros.quantidade === 10 ? 'selected' : ''}>10 questões</option>
          ${modoApp !== 'metro' ? `
          <option value="20" ${M.filtros.quantidade === 20 ? 'selected' : ''}>20 questões</option>
          <option value="50" ${M.filtros.quantidade === 50 ? 'selected' : ''}>50 questões</option>
          <option value="0">Todas disponíveis</option>` : ''}
        </select>
      </div>
    </div>

    <!-- Botão iniciar -->
    <button class="q-btn-iniciar" id="q-btn-iniciar">
      ▶ Iniciar ${M.filtros.modo === 'simulado' ? 'Simulado' : 'Treino'}
    </button>

    ${total === 0 ? `<div class="estado-vazio"><div class="estado-vazio-emoji">📭</div><div class="estado-vazio-texto">Nenhuma questão no banco ainda.</div></div>` : ''}
  `;
}

function _bindMenu(el) {
  // Modo Carro: botão mudar
  el.querySelector('#q-btn-mudar-modo')?.addEventListener('click', () => {
    document.getElementById('btn-mudar-modo')?.click();
  });

  // Cards de modo (treino/simulado/revisão)
  el.querySelectorAll('[data-modo-treino]').forEach(btn => {
    btn.addEventListener('click', () => {
      el.querySelectorAll('[data-modo-treino]').forEach(b => b.classList.remove('ativo'));
      btn.classList.add('ativo');
      M.filtros.modo = btn.dataset.modoTreino;
      const btnIniciar = el.querySelector('#q-btn-iniciar');
      if (btnIniciar) {
        btnIniciar.innerHTML = `▶ Iniciar ${M.filtros.modo === 'simulado' ? 'Simulado' : M.filtros.modo === 'revisao' ? 'Revisão' : 'Treino'}`;
      }
    });
  });

  // Chips bloco
  el.querySelectorAll('[data-bloco]').forEach(chip => {
    chip.addEventListener('click', () => {
      el.querySelectorAll('[data-bloco]').forEach(c => c.classList.remove('ativo'));
      chip.classList.add('ativo');
      M.filtros.blocos = chip.dataset.bloco ? [chip.dataset.bloco] : [];
    });
  });

  // Chips incidência
  el.querySelectorAll('[data-incidencia]').forEach(chip => {
    chip.addEventListener('click', () => {
      el.querySelectorAll('[data-incidencia]').forEach(c => c.classList.remove('ativo'));
      chip.classList.add('ativo');
      M.filtros.incidencia = chip.dataset.incidencia;
    });
  });

  // Chips banca
  el.querySelectorAll('[data-banca]').forEach(chip => {
    chip.addEventListener('click', () => {
      el.querySelectorAll('[data-banca]').forEach(c => c.classList.remove('ativo'));
      chip.classList.add('ativo');
      M.filtros.banca = chip.dataset.banca;
    });
  });

  // Quantidade
  el.querySelector('#select-quantidade')?.addEventListener('change', (e) => {
    M.filtros.quantidade = parseInt(e.target.value) || 0;
  });

  // Iniciar
  el.querySelector('#q-btn-iniciar')?.addEventListener('click', _iniciarSessao);
}

/* ═══════════════════════════════════════════════
   LÓGICA DE SESSÃO
   ═══════════════════════════════════════════════ */
function _iniciarSessao() {
  const modo = M.filtros.modo;

  // Filtrar questões
  let questoes = [...M.todos];

  if (modo === 'revisao') {
    const idsRevisao = Object.entries(M.marcacoes)
      .filter(([, m]) => m === 'errei' || m === 'duvida')
      .map(([id]) => id);
    questoes = questoes.filter(q => idsRevisao.includes(q.id));
  } else {
    if (M.filtros.blocos.length > 0) {
      questoes = questoes.filter(q => M.filtros.blocos.includes(q.bloco));
    }
    if (M.filtros.incidencia) {
      questoes = questoes.filter(q => q.incidencia === M.filtros.incidencia);
    }
    if (M.filtros.banca) {
      questoes = questoes.filter(q => q.banca === M.filtros.banca);
    }
  }

  // Embaralhar
  questoes = _embaralhar(questoes);

  // Limitar quantidade
  const qtd = M.filtros.quantidade;
  if (qtd > 0 && questoes.length > qtd) {
    questoes = questoes.slice(0, qtd);
  }

  if (questoes.length === 0) {
    _mostrarToast('Nenhuma questão encontrada com esses filtros.');
    return;
  }

  // Configurar sessão
  const tempoTotal = modo === 'simulado' ? 12600 : 0;
  M.sessao = {
    modo,
    questoes,
    atual: 0,
    respostas: {},
    timerInterval: null,
    tempoTotal,
    tempoRestante: tempoTotal,
    iniciada: true,
    finalizada: false,
    tempoInicio: Date.now(),
  };

  _renderizarView('questao');

  if (modo === 'simulado') _iniciarTimer();
}

function _embaralhar(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ═══════════════════════════════════════════════
   TIMER (SIMULADO)
   ═══════════════════════════════════════════════ */
function _iniciarTimer() {
  M.sessao.timerInterval = setInterval(() => {
    M.sessao.tempoRestante--;
    _atualizarTimer();
    if (M.sessao.tempoRestante <= 0) {
      _finalizarSessao();
    }
  }, 1000);
}

function _pararTimer() {
  if (M.sessao.timerInterval) {
    clearInterval(M.sessao.timerInterval);
    M.sessao.timerInterval = null;
  }
}

function _atualizarTimer() {
  const timerEl = document.querySelector('.q-timer');
  if (!timerEl) return;
  timerEl.textContent = _formatarTempo(M.sessao.tempoRestante);
  if (M.sessao.tempoRestante <= 300) timerEl.classList.add('urgente');
}

function _formatarTempo(seg) {
  const h = Math.floor(seg / 3600);
  const m = Math.floor((seg % 3600) / 60);
  const s = seg % 60;
  if (h > 0) return `${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  return `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}

/* ═══════════════════════════════════════════════
   VIEW: QUESTÃO
   ═══════════════════════════════════════════════ */
function _htmlQuestao() {
  const s = M.sessao;
  const q = s.questoes[s.atual];
  const total = s.questoes.length;
  const pct = Math.round((s.atual / total) * 100);
  const respondida = s.respostas[q.id];
  const modo = s.modo;

  const letras = ['A', 'B', 'C', 'D', 'E'];

  const htmlAlternativas = letras
    .filter(l => q.alternativas[l])
    .map(l => {
      let cls = '';
      let icone = '';
      if (respondida) {
        cls += ' desabilitada';
        if (l === q.gabarito) { cls += ' correta'; icone = '✓'; }
        else if (l === respondida.escolhida) { cls += ' errada'; icone = '✗'; }
      }
      return `
        <button class="q-alternativa${cls}" data-letra="${l}">
          <span class="q-alt-letra">${l}</span>
          <span class="q-alt-texto">${q.alternativas[l]}</span>
          ${icone ? `<span class="q-alt-icone">${icone}</span>` : ''}
        </button>`;
    }).join('');

  const blocoLabel = { basicos: 'CB', complementares: 'CC', especificos: 'CE' }[q.bloco] || q.bloco;
  const corBloco = { basicos: 'var(--cor-basicos)', complementares: 'var(--cor-complementares)', especificos: 'var(--cor-especificos)' }[q.bloco];

  return `
    <!-- Header da sessão -->
    <div class="q-header-sessao">
      <button class="q-btn-voltar" id="q-btn-voltar" title="Voltar ao menu">‹</button>
      <div class="q-progresso-wrapper">
        <div class="q-progresso-texto">Questão ${s.atual + 1} de ${total}</div>
        <div class="q-progresso-barra">
          <div class="q-progresso-fill" style="width:${pct}%"></div>
        </div>
      </div>
      ${modo === 'simulado'
        ? `<div class="q-timer">${_formatarTempo(s.tempoRestante)}</div>`
        : `<div style="font-size:11px;color:rgba(255,255,255,.6);font-weight:600;text-transform:uppercase;">${modo === 'revisao' ? '🔄 REVISÃO' : '🎓 TREINO'}</div>`
      }
    </div>

    <!-- Card da questão -->
    <div class="q-card">
      <div class="q-card-meta">
        <span class="tag" style="background:${corBloco}22;color:${corBloco};">${blocoLabel}</span>
        <span class="tag tag-incidencia-${q.incidencia}">${q.incidencia === 'alta' ? '🔴 Alta' : q.incidencia === 'media' ? '🟡 Média' : '⚪ Baixa'}</span>
        <span class="tag tag-primaria">${_nomeBanca(q.banca)} ${q.ano}</span>
      </div>
      <div class="q-card-enunciado">${_formatarEnunciado(q.enunciado)}</div>
      <div class="q-alternativas" id="q-alternativas">${htmlAlternativas}</div>
    </div>

    <!-- Feedback (treino — aparece após responder) -->
    <div id="q-feedback-container"></div>

    <!-- Marcação (aparece após responder no treino) -->
    <div id="q-marcacao-container"></div>

    <!-- Barra de ação -->
    <div class="q-barra-acao">
      ${modo === 'simulado' ? `
        <button class="q-btn-nav secundario" id="q-btn-anterior" ${s.atual === 0 ? 'disabled' : ''}>‹ Anterior</button>
      ` : ''}
      <button class="q-btn-nav primario" id="q-btn-proximo" ${!respondida && modo !== 'simulado' ? 'disabled' : ''}>
        ${s.atual === total - 1 ? (modo === 'simulado' ? '📋 Entregar' : '📊 Ver resultado') : 'Próxima ›'}
      </button>
    </div>
  `;
}

function _formatarEnunciado(texto) {
  return texto.replace(/'/g, ''').replace(/"/g, '"').replace(/\n/g, '<br>');
}

function _nomeBanca(id) {
  const nomes = {
    'quadrix-2022': 'Quadrix', 'quadrix-2025': 'Quadrix',
    'quadrix-2021': 'Quadrix', 'quadrix-2016': 'Quadrix',
    'iades-2023': 'IADES',
  };
  return nomes[id] || id;
}

function _bindQuestao(el) {
  const s = M.sessao;

  // Botão voltar
  el.querySelector('#q-btn-voltar')?.addEventListener('click', () => {
    if (confirm('Sair da sessão? O progresso desta sessão será perdido.')) {
      _pararTimer();
      _renderizarView('menu');
    }
  });

  // Alternativas
  el.querySelectorAll('.q-alternativa:not(.desabilitada)').forEach(btn => {
    btn.addEventListener('click', () => {
      const letra = btn.dataset.letra;
      _responderQuestao(letra);
    });
  });

  // Anterior (simulado)
  el.querySelector('#q-btn-anterior')?.addEventListener('click', () => {
    if (s.atual > 0) {
      s.atual--;
      _renderizarView('questao');
    }
  });

  // Próxima
  el.querySelector('#q-btn-proximo')?.addEventListener('click', () => {
    if (s.atual === s.questoes.length - 1) {
      _finalizarSessao();
    } else {
      s.atual++;
      _renderizarView('questao');
    }
  });

  // Se questão já respondida (voltar no simulado): mostrar feedback se treino
  const q = s.questoes[s.atual];
  const respondida = s.respostas[q.id];
  if (respondida && s.modo === 'treino') {
    _mostrarFeedbackTreino(el, q, respondida.escolhida);
  }
}

/* ═══════════════════════════════════════════════
   RESPONDER QUESTÃO
   ═══════════════════════════════════════════════ */
function _responderQuestao(escolhida) {
  const s = M.sessao;
  const q = s.questoes[s.atual];
  const correta = q.gabarito === escolhida;
  const tempoResposta = Date.now() - s.tempoInicio;

  s.respostas[q.id] = { escolhida, correta, tempo: tempoResposta };

  // Salvar progresso no Firestore (assíncrono, não bloqueia)
  _salvarProgresso(q, correta);

  if (s.modo === 'treino' || s.modo === 'revisao') {
    // Atualiza visual das alternativas
    const altsEl = document.getElementById('q-alternativas');
    if (altsEl) {
      altsEl.querySelectorAll('.q-alternativa').forEach(btn => {
        const l = btn.dataset.letra;
        btn.classList.add('desabilitada');
        if (l === q.gabarito) {
          btn.classList.add('correta');
          btn.querySelector('.q-alt-icone')?.remove();
          btn.insertAdjacentHTML('beforeend', '<span class="q-alt-icone">✓</span>');
        } else if (l === escolhida) {
          btn.classList.add('errada');
          btn.insertAdjacentHTML('beforeend', '<span class="q-alt-icone">✗</span>');
        }
      });
    }

    // Mostrar feedback
    const el = document.getElementById('painel-questoes');
    _mostrarFeedbackTreino(el, q, escolhida);

    // Habilitar botão próxima
    const btnProximo = document.getElementById('q-btn-proximo');
    if (btnProximo) btnProximo.disabled = false;
  } else {
    // Simulado: apenas atualiza a alternativa selecionada e vai para próxima
    const el = document.getElementById('painel-questoes');
    const altsEl = el?.querySelector('#q-alternativas');
    if (altsEl) {
      altsEl.querySelectorAll('.q-alternativa').forEach(btn => {
        btn.classList.add('desabilitada');
        if (btn.dataset.letra === escolhida) btn.classList.add('selecionada');
      });
    }
    // Ir para próxima automaticamente
    setTimeout(() => {
      if (s.atual < s.questoes.length - 1) {
        s.atual++;
        _renderizarView('questao');
      } else {
        _finalizarSessao();
      }
    }, 400);
  }
}

/* ═══════════════════════════════════════════════
   VIEW: FEEDBACK TREINO (inline)
   ═══════════════════════════════════════════════ */
function _mostrarFeedbackTreino(el, q, escolhida) {
  const correta = q.gabarito === escolhida;
  const marcacaoAtual = M.marcacoes[q.id] || '';

  const feedbackEl = el?.querySelector('#q-feedback-container');
  if (!feedbackEl) return;

  feedbackEl.innerHTML = `
    <div class="q-feedback ${correta ? 'acerto' : 'erro'}">
      <div class="q-feedback-header">
        <span>${correta ? '✓ Correto!' : '✗ Incorreto'}</span>
        ${!correta ? `<span style="font-size:12px;opacity:.85;">Gabarito: ${q.gabarito}</span>` : ''}
      </div>
      <div class="q-feedback-body">${q.explicacao || 'Sem explicação disponível.'}</div>
    </div>
  `;

  const marcacaoEl = el?.querySelector('#q-marcacao-container');
  if (!marcacaoEl) return;

  const opcoes = [
    { valor: 'facil',      emoji: '✅', label: 'Fácil' },
    { valor: 'duvida',     emoji: '🟡', label: 'Dúvida' },
    { valor: 'errei',      emoji: '❌', label: 'Errei' },
    { valor: 'importante', emoji: '⭐', label: 'Import.' },
  ];

  marcacaoEl.innerHTML = `
    <div class="q-marcacao">
      <div class="q-marcacao-label">Marcar questão</div>
      <div class="q-marcacao-opcoes">
        ${opcoes.map(o => `
          <button class="q-marcacao-btn ${marcacaoAtual === o.valor ? 'ativo' : ''}" data-marcacao="${o.valor}">
            <span class="q-marcacao-emoji">${o.emoji}</span>
            ${o.label}
          </button>
        `).join('')}
      </div>
    </div>
  `;

  // Bind marcação
  marcacaoEl.querySelectorAll('[data-marcacao]').forEach(btn => {
    btn.addEventListener('click', () => {
      const val = btn.dataset.marcacao;
      const anterior = M.marcacoes[q.id];
      M.marcacoes[q.id] = anterior === val ? null : val;
      marcacaoEl.querySelectorAll('[data-marcacao]').forEach(b => {
        b.classList.toggle('ativo', b.dataset.marcacao === M.marcacoes[q.id]);
      });
      _salvarMarcacao(q.id, M.marcacoes[q.id]);
    });
  });
}

/* ═══════════════════════════════════════════════
   FINALIZAR SESSÃO
   ═══════════════════════════════════════════════ */
function _finalizarSessao() {
  _pararTimer();
  M.sessao.finalizada = true;
  _renderizarView('analise');
}

/* ═══════════════════════════════════════════════
   VIEW: ANÁLISE FINAL
   ═══════════════════════════════════════════════ */
function _htmlAnalise() {
  const s = M.sessao;
  const total = s.questoes.length;
  const respondidas = Object.keys(s.respostas).length;
  const acertos = Object.values(s.respostas).filter(r => r.correta).length;
  const pct = respondidas > 0 ? Math.round(acertos / respondidas * 100) : 0;
  const emoji = pct >= 81 ? '🟢' : pct >= 70 ? '🟡' : '🔴';
  const textoDesempenho = pct >= 81 ? 'Ótimo resultado!' : pct >= 70 ? 'Quase lá!' : 'Precisa reforçar';

  // Desempenho por bloco
  const porBloco = {};
  s.questoes.forEach(q => {
    if (!porBloco[q.bloco]) porBloco[q.bloco] = { total: 0, acertos: 0 };
    porBloco[q.bloco].total++;
    if (s.respostas[q.id]?.correta) porBloco[q.bloco].acertos++;
  });

  const nomesBloco = { basicos: 'Conhecimentos Básicos', complementares: 'Conhecimentos Complementares', especificos: 'Conhecimentos Específicos' };
  const coresBloco = { basicos: 'var(--cor-basicos)', complementares: 'var(--cor-complementares)', especificos: 'var(--cor-especificos)' };

  const htmlBlocos = Object.entries(porBloco).map(([bloco, dados]) => {
    const p = dados.total > 0 ? Math.round(dados.acertos / dados.total * 100) : 0;
    const cor = p >= 81 ? 'var(--cor-sucesso)' : p >= 70 ? 'var(--cor-atencao)' : 'var(--cor-erro)';
    return `
      <div class="q-relatorio-item">
        <div class="q-relatorio-item-dot" style="background:${coresBloco[bloco]}"></div>
        <div class="q-relatorio-item-nome">${nomesBloco[bloco] || bloco}</div>
        <div style="font-size:11px;color:var(--cor-texto-leve);">${dados.acertos}/${dados.total}</div>
        <div class="q-relatorio-item-pct" style="color:${cor};">${p}%</div>
      </div>`;
  }).join('');

  // Não respondidas (simulado)
  const naoRespondidas = total - respondidas;

  const tempoTotal = s.modo === 'simulado'
    ? _formatarTempo(s.tempoTotal - s.tempoRestante)
    : _formatarTempo(Math.floor((Date.now() - s.tempoInicio) / 1000));

  return `
    <!-- Cabeçalho do relatório -->
    <div class="q-relatorio-header">
      <div class="q-relatorio-emoji">${emoji}</div>
      <div class="q-relatorio-titulo">${textoDesempenho}</div>
      <div class="q-relatorio-pct">${pct}%</div>
      <div class="q-relatorio-sub">${acertos} de ${respondidas} questões corretas · ${tempoTotal}</div>
    </div>

    <div class="q-relatorio-corpo">

      <!-- Resumo numérico -->
      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Resumo da sessão</div>
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
        ${naoRespondidas > 0 ? `
        <div class="q-relatorio-item">
          <span style="font-size:16px;">⬜</span>
          <div class="q-relatorio-item-nome">Não respondidas</div>
          <div class="q-relatorio-item-pct" style="color:var(--cor-texto-leve);">${naoRespondidas}</div>
        </div>` : ''}
        <div class="q-relatorio-item">
          <span style="font-size:16px;">⏱️</span>
          <div class="q-relatorio-item-nome">Tempo total</div>
          <div class="q-relatorio-item-pct">${tempoTotal}</div>
        </div>
      </div>

      <!-- Por bloco -->
      ${Object.keys(porBloco).length > 1 ? `
      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Desempenho por bloco</div>
        ${htmlBlocos}
      </div>` : ''}

      <!-- Gabarito completo -->
      <div class="q-relatorio-card">
        <div class="q-relatorio-card-header">Gabarito — questão por questão</div>
        ${s.questoes.map((q, i) => {
          const r = s.respostas[q.id];
          const ico = !r ? '⬜' : r.correta ? '✅' : '❌';
          return `
          <div class="q-relatorio-item" style="cursor:pointer;" data-questao-idx="${i}" id="relatorio-q-${i}">
            <span style="font-size:14px;flex-shrink:0;">${ico}</span>
            <div class="q-relatorio-item-nome" style="font-size:12px;">${i + 1}. ${q.enunciado.slice(0, 60)}...</div>
            ${r ? `<div style="font-size:12px;font-weight:700;color:${r.correta ? 'var(--cor-sucesso)' : 'var(--cor-erro)'};">${r.escolhida}</div>` : ''}
          </div>`;
        }).join('')}
      </div>

      <!-- Ações -->
      <div style="display:flex;gap:10px;">
        <button class="btn btn-outline" style="flex:1;" id="q-btn-novo-treino">Nova sessão</button>
        <button class="btn btn-primario" style="flex:1;" id="q-btn-revisar-erros">Revisar erros</button>
      </div>

    </div>
  `;
}

function _bindAnalise(el) {
  el.querySelector('#q-btn-novo-treino')?.addEventListener('click', () => {
    _pararTimer();
    _renderizarView('menu');
  });

  el.querySelector('#q-btn-revisar-erros')?.addEventListener('click', () => {
    // Configura revisão para os erros desta sessão
    const erros = Object.entries(M.sessao.respostas)
      .filter(([, r]) => !r.correta)
      .map(([id]) => id);

    if (erros.length === 0) {
      _mostrarToast('Parabéns! Nenhum erro para revisar! 🎉');
      return;
    }

    // Marcar como "errei" automaticamente
    erros.forEach(id => {
      M.marcacoes[id] = 'errei';
      _salvarMarcacao(id, 'errei');
    });

    M.filtros.modo = 'revisao';
    _iniciarSessao();
  });

  // Clique em questão no gabarito: re-exibir questão
  el.querySelectorAll('[data-questao-idx]').forEach(item => {
    item.addEventListener('click', () => {
      const idx = parseInt(item.dataset.questaoIdx);
      M.sessao.atual = idx;
      _renderizarView('questao');
    });
  });
}

/* ═══════════════════════════════════════════════
   VIEW: RESULTADO TREINO (mantido para compatibilidade — não usado diretamente)
   ═══════════════════════════════════════════════ */
function _htmlResultadoTreino() { return _htmlAnalise(); }
function _bindResultadoTreino(el) { _bindAnalise(el); }

/* ═══════════════════════════════════════════════
   PERSISTÊNCIA NO FIRESTORE
   ═══════════════════════════════════════════════ */
async function _salvarProgresso(questao, correta) {
  const usuario = obterUsuario();
  if (!usuario) return;

  const topicoId = questao.topico;
  const atual = M.progresso[topicoId] || { respondidas: 0, acertos: 0 };
  atual.respondidas++;
  if (correta) atual.acertos++;
  atual.percentualAcerto = Math.round(atual.acertos / atual.respondidas * 100);
  atual.ultimaAtividade = new Date().toISOString();

  M.progresso[topicoId] = atual;

  try {
    await setDoc(
      doc(db, 'users', usuario.uid, 'progresso', topicoId),
      { ...atual, ultimaAtividade: serverTimestamp() },
      { merge: true }
    );
  } catch (e) {
    // offline — será sincronizado depois pelo Firestore
  }

  // Tracking diário + status por questão (alimenta o dashboard)
  const hoje = new Date().toISOString().slice(0, 10);
  try {
    await Promise.all([
      setDoc(
        doc(db, 'users', usuario.uid, 'daily', hoje),
        { respondidas: increment(1), acertos: increment(correta ? 1 : 0), atualizadoEm: serverTimestamp() },
        { merge: true }
      ),
      setDoc(
        doc(db, 'users', usuario.uid, 'questoesStatus', questao.id),
        { respondida: true, correta, bloco: questao.bloco, atualizadoEm: serverTimestamp() },
        { merge: true }
      ),
    ]);
  } catch (e) {
    // offline
  }
}

async function _salvarMarcacao(questaoId, marcacao) {
  const usuario = obterUsuario();
  if (!usuario) return;

  try {
    if (!marcacao) {
      // Remover marcação
      await setDoc(
        doc(db, 'users', usuario.uid, 'questoesStatus', questaoId),
        { marcacao: null, atualizadoEm: serverTimestamp() },
        { merge: true }
      );
    } else {
      await setDoc(
        doc(db, 'users', usuario.uid, 'questoesStatus', questaoId),
        { marcacao, atualizadoEm: serverTimestamp() },
        { merge: true }
      );
    }
  } catch (e) {
    // offline
  }
}

/* ═══════════════════════════════════════════════
   UTILITÁRIOS
   ═══════════════════════════════════════════════ */
function _mostrarToast(msg) {
  if (window.app?.mostrarToast) {
    window.app.mostrarToast(msg);
  }
}
