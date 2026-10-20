---
title: JavaScript : variables, types, fonctions
group: JavaScript & TypeScript
summary: var/let/const, ==/===, fonctions fléchées et objets.
order: 36
slug: javascript-bases
tags: javascript, const, let, var, this, ===
---

## `var`, `let`, `const`

```js
let count = 0;
count = 1;                // OK : réaffectation

const invoice = { amount: 120 };
invoice.amount = 150;    // OK : propriété modifiable
// invoice = {} ;        // NON : réaffectation interdite
```

- `var` : portée de **fonction**, pas de bloc. Historique, à éviter pour du nouveau code.
- `let` : portée de **bloc**, réaffectation possible.
- `const` : portée de **bloc**, **pas de réaffectation** (ne rend pas un objet immuable).

## Comparer des valeurs

```js
'2' == 2;   // true : conversion implicite
'2' === 2;  // false : types différents
```

On préfère `===` pour réduire les conversions implicites surprenantes.

## Fonctions classiques et fléchées

```js
function total(a, b) { return a + b; }
const add = (a, b) => a + b;
```

Une arrow function ne possède pas son propre `this` : elle capture le `this` lexical environnant. Attention aux méthodes d'objets quand `this` doit désigner l'objet.

## `null`, `undefined`, `??`, `?.`

```js
let name;                   // undefined
const client = null;        // null explicite
const label = name ?? 'Inconnu';
const email = user?.profile?.email; // pas d'erreur si parent null/undefined
```

## `map`, `filter`, `reduce`

```js
const invoices = [{amount:120,status:'paid'}, {amount:80,status:'pending'}];
const paid = invoices.filter(i => i.status === 'paid');
const amounts = invoices.map(i => i.amount);
const total = invoices.reduce((sum, i) => sum + i.amount, 0);
```

- `map` transforme et retourne un tableau.
- `filter` conserve les éléments validant un prédicat.
- `reduce` accumule vers un résultat de type libre : nombre, objet, tableau, etc.
