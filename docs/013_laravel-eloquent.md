---
title: Eloquent : lire, filtrer, trier
group: Laravel
summary: all(), where(), get(), first(), findOrFail(), sum(), count() et collections.
order: 13
slug: laravel-eloquent
tags: eloquent, where, get, all, first, count, sum, orderBy
---

## La différence essentielle : Builder vs Collection

```php
$all = Invoice::all(); // exécute SQL maintenant → Collection

$query = Invoice::where('status', 'paid'); // construit Query Builder
$paid = $query->get();                       // exécute SQL → Collection
```

Ne pas confondre ces deux opérations :

```php
Invoice::all()->where('status', 'paid'); // filtre en mémoire
Invoice::where('status', 'paid')->get(); // filtre en SQL
```

## Les requêtes courantes

```php
$invoices = Invoice::all();
$paid = Invoice::where('status', 'paid')->get();
$latest = Invoice::where('status', 'paid')
    ->orderBy('id', 'desc')->limit(5)->get();

$one = Invoice::find(10);       // modèle ou null
$required = Invoice::findOrFail(10); // modèle ou exception 404
$first = Invoice::where('status', 'pending')->first(); // modèle ou null
```

## Agrégation directement en base

```php
$count = Invoice::where('status', 'pending')->count();
$total = Invoice::where('status', 'pending')->sum('amount');
$max = Invoice::max('amount');
```

## Créer, modifier, supprimer

```php
$invoice = Invoice::create([
    'client' => 'Alice',
    'amount' => 120,
    'status' => 'paid',
]);

$invoice->update(['status' => 'pending']);
$invoice->delete();
```

`create()` et `update()` avec un tableau nécessitent de contrôler l'attribution de masse via `$fillable` ou `$guarded`.

## Pagination

```php
$invoices = Invoice::orderByDesc('id')->paginate(20);
```

```blade
@foreach($invoices as $invoice)
  <p>{{ $invoice->client }}</p>
@endforeach
{{ $invoices->links() }}
```

## Collections en mémoire

```php
$collection = Invoice::all();
$filtered = $collection->where('status', 'paid');
$sorted = $filtered->sortByDesc('amount');
```

**À retenir :** `sortByDesc()` pour une collection, `orderBy('amount', 'desc')` pour la requête SQL.

[Référence officielle : Eloquent](https://laravel.com/docs/13.x/eloquent)
