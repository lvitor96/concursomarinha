/**
 * sync.js — Gerenciamento de conectividade e sincronização offline/online.
 */

let _onlineCallback = null;
let _offlineCallback = null;
let _estado = null;

/**
 * Inicia o monitoramento de conectividade.
 * @param {object} estado — objeto de estado global do app
 */
function iniciarSync(estado) {
  _estado = estado;
  atualizarStatusOnline();

  window.addEventListener('online',  aoFicarOnline);
  window.addEventListener('offline', aoFicarOffline);
}

function aoFicarOnline() {
  if (_estado) _estado.online = true;
  _esconderBannerOffline();
  _mostrarToast('✓ Conexão restaurada — sincronizando...');
  if (_onlineCallback) _onlineCallback();
}

function aoFicarOffline() {
  if (_estado) _estado.online = false;
  _mostrarBannerOffline();
  if (_offlineCallback) _offlineCallback();
}

function atualizarStatusOnline() {
  if (navigator.onLine) {
    _esconderBannerOffline();
    if (_estado) _estado.online = true;
  } else {
    _mostrarBannerOffline();
    if (_estado) _estado.online = false;
  }
}

/**
 * Registra callbacks para eventos de conectividade.
 */
function aoReconectar(fn) { _onlineCallback = fn; }
function aoDesconectar(fn) { _offlineCallback = fn; }

function _mostrarBannerOffline() {
  const banner = document.getElementById('banner-offline');
  if (banner) banner.classList.remove('oculto');
}

function _esconderBannerOffline() {
  const banner = document.getElementById('banner-offline');
  if (banner) banner.classList.add('oculto');
}

/* Utilitário global de toast — acessível sem importar app.js */
let _toastTimer = null;

function _mostrarToast(mensagem, duracao = 2500) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = mensagem;
  toast.classList.add('visivel');
  clearTimeout(_toastTimer);
  _toastTimer = setTimeout(() => toast.classList.remove('visivel'), duracao);
}

export { iniciarSync, aoReconectar, aoDesconectar, atualizarStatusOnline };
