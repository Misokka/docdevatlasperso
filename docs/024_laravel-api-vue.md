---
title: Laravel + Vue 3 : API JSON et Vite
group: Laravel
summary: Guide complet d’une intégration avec route JSON, Blade, Vite et Vue.
order: 24
slug: laravel-api-vue
tags: api, vue, vite, fetch, json, web.php, intégration
---

## L'architecture de l'exercice

```text
Navigateur /demo/vue/invoices
    ↓
Laravel rend un Blade avec <div id="invoice-app">
    ↓
Vite charge resources/js/vue-invoices.js
    ↓
Vue monte InvoiceApp.vue
    ↓
fetch('/demo/vue/invoices/data')
    ↓
Laravel retourne DebugInvoice::all() en JSON
    ↓
invoices.value reçoit le tableau
    ↓
v-for affiche les lignes
```

## 1. Installer Vue et plugin Vite

```bash
npm install vue
npm install -D @vitejs/plugin-vue
```

## 2. Contrôleur Laravel avec page et données

```php
namespace App\Http\Controllers;

use App\Models\DebugInvoice;

class VueInvoiceController extends Controller
{
    public function index()
    {
        return view('demo.vue-invoices.index');
    }

    public function data()
    {
        return response()->json(
            DebugInvoice::query()->select('id', 'client', 'amount', 'status')->get()
        );
    }
}
```

## 3. Routes (ici, sous web.php)

```php
use App\Http\Controllers\VueInvoiceController;

Route::get('/demo/vue/invoices', [VueInvoiceController::class, 'index']);
Route::get('/demo/vue/invoices/data', [VueInvoiceController::class, 'data']);
```

Ici, l'API est accessible dans `web.php` pour un projet de démonstration. Un projet API séparée peut utiliser `routes/api.php` selon sa configuration et ses exigences d'authentification.

## 4. Blade : point de montage Vue

```blade
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Factures Vue</title>
    @vite('resources/js/vue-invoices.js')
</head>
<body>
    <div id="invoice-app"></div>
</body>
</html>
```

## 5. Entry point JavaScript

```js
// resources/js/vue-invoices.js
import { createApp } from 'vue';
import InvoiceApp from './components/InvoiceApp.vue';

createApp(InvoiceApp).mount('#invoice-app');
```

## 6. Vite avec Vue

```js
// vite.config.js (extrait)
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
    plugins: [
        laravel({ input: ['resources/js/vue-invoices.js'], refresh: true }),
        vue(),
    ],
});
```

Si le projet possède déjà d'autres `input` Laravel, il faut **les conserver** en ajoutant le nouveau point d'entrée, pas les remplacer.

## 7. Le composant Vue le plus simple

```vue
<script setup>
import { onMounted, ref } from 'vue';

const invoices = ref([]);

async function loadInvoices() {
    const response = await fetch('/demo/vue/invoices/data');
    if (!response.ok) throw new Error('Erreur API');
    invoices.value = await response.json();
}

onMounted(loadInvoices);
</script>

<template>
    <h1>Liste des factures</h1>
    <table>
        <tbody>
            <tr v-for="invoice in invoices" :key="invoice.id">
                <td>{{ invoice.client }}</td>
                <td>{{ invoice.amount }} €</td>
            </tr>
        </tbody>
    </table>
</template>
```

Dans une vraie UI, gérer aussi `loading`, erreurs et une réponse JSON qui ne serait pas le tableau attendu.

## 8. Démarrer l'ensemble

```bash
php artisan serve
npm run dev
```

Laravel sert l'API et le Blade ; Vite sert les modules et le rechargement frontend en développement.

[Vue — Composition API](https://vuejs.org/guide/essentials/reactivity-fundamentals.html) · [Laravel — Vite](https://laravel.com/docs/13.x/vite)
