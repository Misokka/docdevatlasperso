---
title: SQL : GROUP BY, HAVING, SUM, COUNT
group: SQL & BDD
summary: Sommes par client, HAVING vs WHERE et erreurs de regroupement.
order: 30
slug: sql-aggregation
tags: group by, having, sum, count, avg, aggregation
---

## Total des factures en attente par client

```sql
SELECT clients.name,
       SUM(invoices.amount) AS total_pending
FROM clients
INNER JOIN invoices ON invoices.client_id = clients.id
WHERE invoices.status = 'pending'
GROUP BY clients.id, clients.name
ORDER BY total_pending DESC;
```

## `WHERE` filtre les lignes, `HAVING` filtre les groupes

```sql
SELECT clients.id, clients.name, COUNT(invoices.id) AS paid_count
FROM clients
INNER JOIN invoices ON invoices.client_id = clients.id
WHERE invoices.status = 'paid'
GROUP BY clients.id, clients.name
HAVING COUNT(invoices.id) >= 3;
```

- `WHERE invoices.status = 'paid'` : ne prendre que les factures payées **avant** le regroupement.
- `GROUP BY clients.id, clients.name` : rassembler les lignes par client.
- `HAVING COUNT(invoices.id) >= 3` : conserver seulement les clients avec au moins trois factures payées.

## Les agrégations les plus utiles

```sql
SELECT COUNT(*) AS total_count,
       SUM(amount) AS total_amount,
       AVG(amount) AS average_amount,
       MIN(amount) AS smallest,
       MAX(amount) AS largest
FROM invoices
WHERE status = 'paid';
```

## Point clé

`SUM(amount)` donne un total et regroupe, tandis que sélectionner directement `invoices.amount` donne le montant **de chaque facture**. Vérifie bien l'énoncé.
