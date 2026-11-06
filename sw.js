/* Service worker de Micro-X: deja el juego disponible sin conexión. */
const CACHE = 'microx-v13';   // súbelo (v2, v3…) cuando publiques una versión nueva
const FILES = ['./', './index.html', './manifest.webmanifest',
  './fonts/anton.woff2', './icons/icon-192.png', './icons/icon-512.png', './icons/icon-maskable-512.png', './icons/apple-touch-icon.png'];

self.addEventListener('install', e => {
  // 'reload' evita copias viejas del caché HTTP al instalar una versión nueva
  e.waitUntil(caches.open(CACHE).then(c => Promise.all(FILES.map(f => fetch(new Request(f, { cache: 'reload' })).then(r => c.put(f, r))))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
// Primero la red (para recibir actualizaciones); si no hay conexión, la copia guardada.
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request.mode === 'navigate' ? e.request : new Request(e.request.url, { cache: 'no-cache', credentials: 'same-origin' })).then(r => {
      const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return r;
    }).catch(() => caches.match(e.request).then(m => m || caches.match('./index.html')))
  );
});
