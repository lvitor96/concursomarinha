/**
 * sw.js — Service Worker do SEDF Estudos
 * Estratégia: Cache-first para assets estáticos, Network-first para dados.
 */

const CACHE_VERSION = 'v4';
const CACHE_STATIC  = `sedf-static-${CACHE_VERSION}`;
const CACHE_DYNAMIC = `sedf-dynamic-${CACHE_VERSION}`;

const ASSETS_ESTATICOS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/css/main.css',
  '/css/dark.css',
  '/js/app.js',
  '/js/firebase.js',
  '/js/auth.js',
  '/js/sync.js',
  '/icons/icon.svg',
  '/css/questoes.css',
  '/css/resumos.css',
  '/css/cronograma.css',
  '/js/questoes.js',
  '/js/resumos.js',
  '/js/cronograma.js',
  '/data/topicos.json',
  '/data/questoes.json',
  '/data/resumos.json',
];

const FIREBASE_SDK_BASE = 'https://www.gstatic.com/firebasejs/10.12.2';
const FIREBASE_MODULES = [
  `${FIREBASE_SDK_BASE}/firebase-app.js`,
  `${FIREBASE_SDK_BASE}/firebase-auth.js`,
  `${FIREBASE_SDK_BASE}/firebase-firestore.js`,
  `${FIREBASE_SDK_BASE}/firebase-storage.js`,
];

const FONTS_URLS = [
  'https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap',
];

// ── Install: pré-cache dos assets estáticos ──────────────────
self.addEventListener('install', (event) => {
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE_STATIC).then(async (cache) => {
      // Cache local assets (sempre funciona)
      await cache.addAll(ASSETS_ESTATICOS);

      // Cache Firebase SDK modules (melhor esforço — não bloqueia install)
      const firebase_cache = FIREBASE_MODULES.map(url =>
        fetch(url, { mode: 'cors' })
          .then(res => cache.put(url, res))
          .catch(() => {/* ignora falhas de rede no install */})
      );
      await Promise.allSettled(firebase_cache);
    })
  );
});

// ── Activate: remove caches antigos ─────────────────────────
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key !== CACHE_STATIC && key !== CACHE_DYNAMIC)
          .map(key => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

// ── Fetch: estratégia por tipo de recurso ────────────────────
self.addEventListener('fetch', (event) => {
  const url = event.request.url;

  // Ignora requests não-GET
  if (event.request.method !== 'GET') return;

  // Firestore / Firebase Auth APIs → network only (offline persistence é do SDK)
  if (
    url.includes('firestore.googleapis.com') ||
    url.includes('identitytoolkit.googleapis.com') ||
    url.includes('securetoken.googleapis.com')
  ) {
    return; // deixa passar sem SW
  }

  // Firebase SDK modules → Cache first (raramente mudam)
  if (url.startsWith(FIREBASE_SDK_BASE)) {
    event.respondWith(cacheFirst(event.request, CACHE_STATIC));
    return;
  }

  // Google Fonts → Cache dinâmico
  if (url.includes('fonts.googleapis.com') || url.includes('fonts.gstatic.com')) {
    event.respondWith(staleWhileRevalidate(event.request, CACHE_DYNAMIC));
    return;
  }

  // Assets locais estáticos → Cache first
  if (url.startsWith(self.location.origin)) {
    event.respondWith(cacheFirst(event.request, CACHE_STATIC));
    return;
  }

  // Demais requests → network com fallback
  event.respondWith(networkFirst(event.request));
});

// ── Estratégias de cache ─────────────────────────────────────

async function cacheFirst(request, cacheName) {
  const cached = await caches.match(request);
  if (cached) return cached;

  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(cacheName);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    // Fallback para index.html em navegação
    if (request.mode === 'navigate') {
      return caches.match('/index.html');
    }
    return new Response('Offline', { status: 503 });
  }
}

async function networkFirst(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_DYNAMIC);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cached = await caches.match(request);
    if (cached) return cached;
    if (request.mode === 'navigate') {
      return caches.match('/index.html');
    }
    return new Response('Offline', { status: 503 });
  }
}

async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);

  const fetchPromise = fetch(request).then(response => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  }).catch(() => null);

  return cached || fetchPromise || new Response('Offline', { status: 503 });
}

// ── Mensagens do client ──────────────────────────────────────
self.addEventListener('message', (event) => {
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
  }
});
