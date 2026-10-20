---
title: JavaScript : Promise, async / await, fetch
group: JavaScript & TypeScript
summary: Comprendre le flux async et la différence entre attendre localement et bloquer le programme.
order: 37
slug: javascript-async
tags: promise, async, await, fetch, event loop, response.json
---

## Les trois règles

1. Une **Promise** représente un résultat futur (réussi ou échoué).
2. Toute fonction `async` retourne une Promise.
3. `await` suspend la suite de **sa fonction async**, pas le reste de l'application.

```js
async function loadInvoices() {
    const response = await fetch('/api/invoices');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const invoices = await response.json();
    return invoices;
}
```

`fetch` ne rejette pas automatiquement la Promise pour chaque HTTP 404/500 : vérifier `response.ok` si l'on veut traiter les erreurs de statut.

## L'ordre des console.log

```js
async function loadInvoices() {
    console.log('A');
    await fetch('/api/invoices');
    console.log('B');
}

console.log('C');
loadInvoices();
console.log('D');
```

Dans le scénario normal où `fetch` reste asynchrone, l'ordre est **C, A, D, B**. Le fetch démarre à son appel et `B` s'exécute après sa résolution.

## Traitement des erreurs

```js
async function load() {
    try {
        const response = await fetch('/api/invoices');
        if (!response.ok) throw new Error('Requête échouée');
        return await response.json();
    } catch (error) {
        console.error(error);
        return [];
    }
}
```

## Promise.all : plusieurs appels en parallèle

```js
const [clients, invoices] = await Promise.all([
    fetch('/api/clients').then(r => r.json()),
    fetch('/api/invoices').then(r => r.json()),
]);
```

Une seule Promise rejetée fait rejeter `Promise.all()`. Pour inspecter tous les résultats, voir `Promise.allSettled()`.
