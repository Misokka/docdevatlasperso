---
title: Vue 3 : fetch, async et onMounted
group: Vue.js
summary: Le composant minimal que tu as reconstitué : chargement JSON puis tableau.
order: 34
slug: vue-fetch
tags: fetch, async, await, onMounted, invoices, composition
---

## Le script minimal à connaître par cœur

```vue
<script setup>
import { onMounted, ref } from 'vue';

const invoices = ref([]);

async function loadInvoices() {
    const response = await fetch('/api/invoices');
    invoices.value = await response.json();
}

onMounted(loadInvoices);
</script>
```

- `ref([])` : initialise un tableau réactif.
- `fetch()` : démarre la requête HTTP.
- `await fetch(...)` : attend la réponse **dans cette fonction**, sans bloquer tout JavaScript.
- `await response.json()` : attend la lecture du corps JSON.
- `.value` : remplace le contenu réactif.
- `onMounted(loadInvoices)` : transmet la **fonction** à Vue ; ne pas écrire `loadInvoices()` ici.

## Template minimal

```vue
<template>
    <table>
        <thead><tr><th>Client</th><th>Montant</th></tr></thead>
        <tbody>
            <tr v-for="invoice in invoices" :key="invoice.id">
                <td>{{ invoice.client }}</td>
                <td>{{ invoice.amount }} €</td>
            </tr>
        </tbody>
    </table>
</template>
```

## Variante robuste : erreur et chargement

```js
const isLoading = ref(true);
const error = ref('');

async function loadInvoices() {
    isLoading.value = true;
    error.value = '';
    try {
        const response = await fetch('/api/invoices');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        invoices.value = await response.json();
    } catch (err) {
        error.value = 'Impossible de charger les factures.';
    } finally {
        isLoading.value = false;
    }
}
```

## Attention au format de la réponse

Si l'API Laravel retourne `{ data: [...] }` (par exemple avec une API Resource), écris `invoices.value = (await response.json()).data`. Si l'API retourne directement `[...]`, la forme minimale est correcte.

[Vue — Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html)
