---
title: Pièges et erreurs à ne plus refaire
group: Commencer
summary: Des corrections précises pour des erreurs fréquentes en PHP, Laravel, SQL et Vue.
order: 4
slug: anti-erreurs
tags: erreurs, pièges, dépannage, mémorisation
---

## Laravel : collections contre requêtes

```php
// ⚠ all() exécute déjà la requête, where() agit sur la collection.
Invoice::all()->where('status', 'paid');

// ✅ filtre directement dans la base.
Invoice::where('status', 'paid')->get();

// ✅ filtre + trie + limite dans la base.
Invoice::where('status', 'paid')->orderBy('amount', 'desc')->limit(5)->get();
```

`orderBy()` appartient au **query builder**. Une collection possède plutôt `sortBy()` / `sortByDesc()`.

## Laravel : formulaire et Eloquent

```blade
<form action="/invoices/{{ $invoice->id }}" method="POST">
    @csrf
    @method('PUT')
    <input name="client" value="{{ old('client', $invoice->client) }}">
    <button type="submit">Modifier</button>
</form>
```

```php
$invoice = Invoice::findOrFail($id);
$invoice->update($validated); // PAS $invoice->Invoice::update(...)
$invoice->delete();           // aucun id à passer à delete() d'instance
```

Pour un formulaire HTML `DELETE`, utiliser aussi `@csrf` et `@method('DELETE')`.

## Laravel : validation cohérente avec la base

```php
$validated = $request->validate([
    'client' => 'required|string',
    'amount' => 'required|numeric|min:0',
    'status' => 'required|in:paid,pending',
]);
```

Ne pas mettre `unpaid` si les valeurs réellement utilisées dans la base sont `paid` et `pending`.

## PHP : ne pas écraser un accumulateur

```php
$total = 0;
foreach ($invoices as $invoice) {
    if ($invoice['status'] === 'pending') {
        $total += $invoice['amount']; // pas simplement =
    }
}
```

Ne jamais écrire `$i++` à l'intérieur d'une expression qui devrait seulement lire l'index.

## SQL : égalité et jointures

```sql
-- SQL utilise = et non ===.
WHERE invoices.status = 'paid'
```

Un `LEFT JOIN` suivi de `WHERE invoices.status = 'paid'` élimine les clients sans facture correspondante. Si tu veux conserver tous les clients, mets le filtre dans `ON` et utilise `COUNT(invoices.id)` / `COALESCE(SUM(...), 0)`.

## Vue : les trois oublis classiques

```js
import { ref, onMounted } from 'vue';
const invoices = ref([]);

async function loadInvoices() {
    const response = await fetch('/api/invoices');
    invoices.value = await response.json();
}

onMounted(loadInvoices); // pas loadInvoices()
```

## Next.js et Vue ne sont pas interchangeables

- Vue : `.vue`, `ref()`, `props`, `emit`, `v-if`, `v-for`.
- Next.js App Router : `app/invoices/page.tsx`, **Server Components** par défaut, directive exacte `'use client'` pour les composants interactifs.
- JavaScript `const` : interdit la **réaffectation**, mais les propriétés d'un objet déclaré `const` peuvent évoluer.
