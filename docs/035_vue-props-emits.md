---
title: Vue : props, emits et formulaires
group: Vue.js
summary: Communication entre parent et enfant, sélection de statut et v-model.
order: 35
slug: vue-props-emits
tags: props, emit, defineProps, defineEmits, v-model
---

## Le sens de communication

- **Props : parent → enfant** (données).
- **Emit : enfant → parent** (événements).

## Enfant : StatusFilter.vue

```vue
<script setup>
const props = defineProps({
    modelValue: { type: String, required: true },
});
const emit = defineEmits(['update:modelValue']);

function onChange(event) {
    emit('update:modelValue', event.target.value);
}
</script>

<template>
    <select :value="props.modelValue" @change="onChange">
        <option value="all">Toutes</option>
        <option value="paid">Payées</option>
        <option value="pending">En attente</option>
    </select>
</template>
```

## Parent : InvoiceApp.vue

```vue
<script setup>
import { ref } from 'vue';
import StatusFilter from './StatusFilter.vue';

const status = ref('all');
</script>

<template>
    <StatusFilter v-model="status" />
    <p>Filtre actuel : {{ status }}</p>
</template>
```

La convention `modelValue` + `update:modelValue` est compatible avec `v-model` sur un composant. On peut aussi utiliser une prop `status` et un événement `change` personnalisé.

## `v-model` sur un champ natif

```vue
<script setup>
import { ref } from 'vue';
const search = ref('');
</script>

<template>
    <input v-model="search" placeholder="Chercher un client">
    <p>{{ search }}</p>
</template>
```

## Erreur à éviter

Les composants Vue **n'utilisent pas** `use client` de Next.js. Vue n'a pas le système Server/Client Components de Next.js à confondre avec props et emits.

[Vue — Component Props](https://vuejs.org/guide/components/props.html) · [Events](https://vuejs.org/guide/components/events.html)
