---
title: Relations Eloquent : clients et factures
group: Laravel
summary: hasMany, belongsTo, clés étrangères, with() et le problème N+1.
order: 14
slug: laravel-relations
tags: hasMany, belongsTo, with, n+1, client_id
---

## Où placer `client_id` ?

Une facture **appartient à un** client ; un client **possède plusieurs** factures. Donc `client_id` est une clé étrangère dans la table **invoices**.

## Modèle Client : `hasMany`

```php
use Illuminate\Database\Eloquent\Relations\HasMany;

class Client extends Model
{
    public function invoices(): HasMany
    {
        return $this->hasMany(Invoice::class);
    }
}
```

## Modèle Invoice : `belongsTo`

```php
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Invoice extends Model
{
    public function client(): BelongsTo
    {
        return $this->belongsTo(Client::class);
    }
}
```

## Utiliser les relations

```php
$client = Client::findOrFail(1);
$clientInvoices = $client->invoices; // Collection

$invoice = Invoice::findOrFail(10);
echo $invoice->client->name;
```

## Éviter le problème N+1

```php
// ⚠ peut faire une requête pour les factures + une par facture.
$invoices = Invoice::all();
foreach ($invoices as $invoice) {
    echo $invoice->client->name;
}
```

```php
// ✅ Eager loading : généralement deux requêtes.
$invoices = Invoice::with('client')->get();
foreach ($invoices as $invoice) {
    echo $invoice->client->name;
}
```

Le bénéfice est particulièrement visible avec beaucoup de factures.

## Filtrer selon une relation

```php
$clients = Client::whereHas('invoices', function ($query) {
    $query->where('status', 'pending');
})->get();
```

[Référence officielle : Eloquent relationships](https://laravel.com/docs/13.x/eloquent-relationships)
