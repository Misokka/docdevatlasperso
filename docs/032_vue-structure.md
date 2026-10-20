---
title: Vue 3 : structure d’un composant
group: Vue.js
summary: Structure SFC avec script setup, template et style ; v-for, v-if et directives.
order: 32
slug: vue-structure
tags: vue, script setup, template, v-for, v-if
---

## Fichier Single File Component (`.vue`)

```vue
<script setup>
import { ref } from 'vue';

const count = ref(0);
function increment() {
    count.value++;
}
</script>

<template>
    <button @click="increment">Compteur : {{ count }}</button>
</template>

<style scoped>
button { padding: 10px; }
</style>
```

`<script setup>` est une syntaxe concise de la Composition API. Les variables déclarées sont accessibles dans le template.

## Directives essentielles

| Directive | Utilité |
|---|---|
| `v-if` | Ajoute / retire conditionnellement un élément du DOM. |
| `v-else` | Alternative au `v-if`. |
| `v-show` | Garde l'élément dans le DOM et agit sur son affichage CSS. |
| `v-for` | Répète un élément pour chaque donnée. |
| `:key` | Donne une identité stable à chaque ligne. |
| `v-model` | Lie un champ de saisie à une donnée. |
| `@click` | Écoute un clic. |
| `:class` | Associe une valeur dynamique à un attribut. |

## Table de factures

```vue
<template>
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

La clé peut être n'importe quelle valeur stable et unique (ID numérique, UUID, chaîne). **Elle ne commence pas obligatoirement à 1.**

[Documentation Vue — Template Syntax](https://vuejs.org/guide/essentials/template-syntax.html)
