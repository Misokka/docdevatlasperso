---
title: Performances, N+1 et bonnes pratiques
group: Laravel
summary: Pagination, eager loading, transactions, sélection SQL et index.
order: 27
slug: laravel-performances
tags: performance, n+1, eager, transaction, pagination
---

## Ne récupère pas tout si tu peux filtrer en BDD

```php
// À éviter sur des données volumineuses
Invoice::all()->where('status', 'paid');

// Préférable
Invoice::where('status', 'paid')->get();
```

## Ne calcule pas une somme en PHP sans raison

```php
$total = Invoice::where('status', 'pending')->sum('amount');
$count = Invoice::where('status', 'pending')->count();
```

Une boucle PHP reste utile pour un traitement applicatif spécifique ; pour agréger un grand volume de données, privilégie généralement l'opération SQL adaptée.

## Pagination et colonnes utiles

```php
$invoices = Invoice::query()
    ->select('id', 'client_id', 'amount', 'status')
    ->orderByDesc('id')
    ->paginate(20);
```

## Prévenir le N+1

```php
$invoices = Invoice::with('client')->get();
```

## Transaction : tout ou rien

```php
use Illuminate\Support\Facades\DB;

DB::transaction(function () use ($invoice) {
    $invoice->update(['status' => 'paid']);
    // Enregistrer un paiement associé si besoin.
});
```

## Index

Un index SQL peut accélérer les recherches sur `email` ou certaines colonnes filtrées, mais a un coût en espace et en écritures. Vérifier le plan d'exécution avant de multiplier les index.

[Référence officielle : Database](https://laravel.com/docs/13.x/database)
