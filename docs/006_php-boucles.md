---
title: Boucles PHP & tableaux
group: PHP
summary: foreach, for, while, filtres, compteurs et regroupements de factures.
order: 6
slug: php-boucles
tags: php, foreach, for, while, isset, sum
---

## `foreach` — parcourir un tableau

```php
$invoices = [
    ['id' => 1, 'client' => 'Alice', 'amount' => 120, 'status' => 'paid'],
    ['id' => 2, 'client' => 'Bob', 'amount' => 80, 'status' => 'pending'],
    ['id' => 3, 'client' => 'Alice', 'amount' => 200, 'status' => 'paid'],
];

foreach ($invoices as $invoice) {
    echo $invoice['client'];
}
```

## Filtrer + compter + additionner

```php
function summarizePaidInvoices(array $invoices): array
{
    $count = 0;
    $total = 0;

    foreach ($invoices as $invoice) {
        if ($invoice['status'] === 'paid') {
            $count++;
            $total += $invoice['amount'];
        }
    }

    return ['count' => $count, 'total' => $total];
}
```

## Regrouper les montants par client

```php
function getPendingTotalsByClient(array $invoices): array
{
    $totals = [];

    foreach ($invoices as $invoice) {
        if ($invoice['status'] !== 'pending') {
            continue;
        }
        $client = $invoice['client'];
        if (!isset($totals[$client])) {
            $totals[$client] = 0;
        }
        $totals[$client] += $invoice['amount'];
    }

    return $totals;
}
```

`isset($totals[$client])` vérifie que cette clé existe et contient une valeur non `null`. Ici, on l'utilise pour initialiser un total au premier passage.

## `for` — indexer un tableau

```php
function getPendingRideIds(array $rides): array
{
    $ids = [];
    for ($i = 0; $i < count($rides); $i++) {
        if ($rides[$i]['status'] === 'pending'
            && $rides[$i]['amount'] >= 40) {
            $ids[] = $rides[$i]['id'];
        }
    }
    return $ids;
}
```

`$i` représente la position du tableau, **pas nécessairement l'identifiant métier**.

## `while` — continuer tant que...

```php
function firstHighValuePaidRide(array $rides): ?int
{
    $index = 0;
    while ($index < count($rides)) {
        if ($rides[$index]['status'] === 'paid'
            && $rides[$index]['amount'] >= 50) {
            return $rides[$index]['id'];
        }
        $index++;
    }
    return null;
}
```

**Distinction :** `while` indique jusqu'à quand continuer le parcours ; `if` indique si l'élément courant correspond à ce qu'on cherche.

## Écueils classiques

- Écraser le total avec `=` au lieu d'accumuler avec `+=`.
- Incrémenter `$i` plusieurs fois et sauter des éléments.
- Oublier de retourner un tableau vide quand rien ne correspond.
- Confondre `$invoice['amount']` (tableau associatif PHP) et `$invoice->amount` (attribut d'objet Eloquent).
