---
title: Fonctions natives PHP
group: PHP
summary: array_map, array_filter, array_reduce, count, isset et fonctions fléchées.
order: 7
slug: php-fonctions
tags: array_map, array_filter, array_reduce, arrow
---

## `array_filter()` — ne garder que certains éléments

```php
$paid = array_filter($invoices, fn($invoice) => $invoice['status'] === 'paid');
// Les clés originales sont conservées ; array_values($paid) les réindexe.
```

## `array_map()` — transformer chaque élément

```php
$names = array_map(fn($invoice) => $invoice['client'], $invoices);
```

## `array_reduce()` — produire un accumulateur

```php
$total = array_reduce(
    $invoices,
    fn($sum, $invoice) => $sum + ($invoice['status'] === 'paid' ? $invoice['amount'] : 0),
    0
);
```

## `isset`, `empty`, `??`

```php
$data = ['amount' => 0, 'client' => 'Alice'];
isset($data['amount']);       // true (0 n'est pas null)
empty($data['amount']);       // true (0 est considéré vide)
$status = $data['status'] ?? 'pending';
```

## `array_key_exists` vs `isset`

```php
$data = ['note' => null];
isset($data['note']);             // false
array_key_exists('note', $data);  // true
```

## Quand préférer une boucle ?

Pour rendre un parcours explicite, utilise `foreach`, `for` ou `while`. `array_reduce()` est utile pour exprimer une réduction, mais une boucle classique reste souvent plus lisible lorsque le traitement comporte plusieurs étapes.
