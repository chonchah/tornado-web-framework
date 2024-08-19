const staticCacheName = 'recipe-manager-static';
const dynamicCacheName = 'recipe-manager-dynamic';

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(staticCacheName).then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/src/style.css',
        '/src/main.js',
        '/src/components/Recepis.vue',
        '/src/components/EditRecipe.vue',
        '/src/components/NewRecipe.vue',
        '/src/components/Card.vue',
        '/src/components/Modal.vue',
        '/src/components/buttons/floating-danger.vue',
        '/src/models/Recipe.ts',
        '/src/firebase.js',
        '/firebase.json',
        '/package.json',
        '/vite.config.js',
        '/postcss.config.js',
        '/tailwind.config.js',
        '/src/assets/*'
      ]);
    }),
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys
          .filter((key) => key !== staticCacheName && key !== dynamicCacheName)
          .map((key) => caches.delete(key)),
      );
    }),
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cacheRes) => {
      return (
        cacheRes ||
        fetch(event.request).then((res) => {
          return caches.open(dynamicCacheName).then((cache) => {
            cache.put(event.request.url, res.clone());
            return res;
          });
        })
      );
    }),
  );
});

