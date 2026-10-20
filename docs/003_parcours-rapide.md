---
title: Parcours express : 20 minutes
group: Commencer
summary: Un itinéraire court parmi les notions fondamentales avant de commencer à coder.
order: 3
slug: parcours-rapide
tags: apprentissage, rapide, priorités, fondamentaux
---

## Les réflexes qui rapportent le plus

**PHP :** parcourir un tableau et accumuler avec `+=`, initialiser une clé grâce à `isset()`, savoir faire `foreach`, `for` et `while`.

**Laravel :** routes, méthodes CRUD, `Request::validate()`, Eloquent `where` / `get` / `update`, Blade, `@csrf`.

**SQL :** `SELECT`, `JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `COUNT`, `SUM`.

**Vue :** `ref([])`, `.value`, `onMounted(loadInvoices)`, `await response.json()`, `v-for`.

**Java :** classe vs objet, typage statique, JVM, Spring Boot, Controller → Service → Repository.

## Les lignes à ne pas confondre

```php
$all = Invoice::all();                              // collection en mémoire
$paid = Invoice::where('status', 'paid')->get();     // filtre SQL
$latest = Invoice::where('status', 'paid')
    ->orderBy('id', 'desc')->limit(5)->get();         // tri + limite SQL
```

```js
const invoices = ref([]);
invoices.value = await response.json();
onMounted(loadInvoices); // référence à la fonction, sans parenthèses
```

```sql
SELECT clients.name, SUM(invoices.amount) AS total_pending
FROM clients
INNER JOIN invoices ON invoices.client_id = clients.id
WHERE invoices.status = 'pending'
GROUP BY clients.id, clients.name
ORDER BY total_pending DESC;
```

## Si une notion t'échappe

Utilise la recherche (Cmd/Ctrl + K) : « auth », « csrf », « listener », « sql », « injection », « vue », « spring », « merge ».
