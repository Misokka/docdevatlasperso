---
title: Vue 3 : ref, reactive, computed, watch
group: Vue.js
summary: Différencier un état réactif, une valeur calculée et un effet secondaire.
order: 33
slug: vue-reactivity
tags: ref, reactive, computed, watch, value, state
---

## `ref()` : une valeur réactive

```js
import { ref } from 'vue';

const invoices = ref([]);
invoices.value = [{ id: 1, amount: 120 }];
```

**Dans le JavaScript**, utiliser `.value`. **Dans le template**, Vue déplie généralement les refs de premier niveau.

## `reactive()` : un objet réactif

```js
import { reactive } from 'vue';

const user = reactive({ name: 'Alice', age: 28 });
user.name = 'Bob';
```

En pratique, `ref()` peut aussi contenir des objets et des tableaux : ce n'est pas limité aux valeurs primitives.

## `computed()` : dériver une valeur

```js
import { ref, computed } from 'vue';

const invoices = ref([{ amount: 120 }, { amount: 80 }]);
const total = computed(() =>
    invoices.value.reduce((sum, invoice) => sum + Number(invoice.amount), 0)
);
```

`total` se recalcule automatiquement lorsque ses dépendances réactives changent. Tu l'utilises pour les **valeurs dérivées** (sommes, filtres, compteur).

## `watch()` : déclencher une action

```js
import { ref, watch } from 'vue';

const search = ref('');
watch(search, (newValue, oldValue) => {
    console.log('Recherche modifiée :', newValue);
    // Par exemple, déclencher un appel API ou synchroniser une URL.
});
```

**Attention :** `watch()` ne signifie pas « attendre qu'une API soit chargée ». Il observe une donnée réactive pour déclencher un effet secondaire quand elle change.

## Exemple de filtre calculé

```js
const statusFilter = ref('all');
const filteredInvoices = computed(() =>
    statusFilter.value === 'all'
        ? invoices.value
        : invoices.value.filter(invoice => invoice.status === statusFilter.value)
);
```

[Vue — Reactivity](https://vuejs.org/guide/essentials/reactivity-fundamentals.html) · [Computed](https://vuejs.org/guide/essentials/computed.html) · [Watchers](https://vuejs.org/guide/essentials/watchers.html)
