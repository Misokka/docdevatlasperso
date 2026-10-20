---
title: SQL : INNER JOIN et LEFT JOIN
group: SQL & BDD
summary: Joindre des clients et factures sans perdre les clients qui n’ont pas de facture.
order: 29
slug: sql-jointures
tags: inner join, left join, clients, invoices, foreign key
---

## INNER JOIN : lignes correspondantes

```sql
SELECT clients.name, invoices.amount, invoices.status
FROM invoices
INNER JOIN clients ON invoices.client_id = clients.id
WHERE invoices.status = 'paid'
ORDER BY invoices.amount DESC;
```

Un client sans facture n'apparaît pas.

## LEFT JOIN : conserver la table de gauche

```sql
SELECT clients.name, invoices.id AS invoice_id
FROM clients
LEFT JOIN invoices ON invoices.client_id = clients.id;
```

Le client sans facture apparaît avec `invoice_id = NULL`.

## Compter toutes les factures, y compris zéro

```sql
SELECT clients.id, clients.name, COUNT(invoices.id) AS invoice_count
FROM clients
LEFT JOIN invoices ON invoices.client_id = clients.id
GROUP BY clients.id, clients.name
ORDER BY clients.name;
```

**Ne pas utiliser `COUNT(*)`** si l'objectif est d'obtenir 0 pour une ligne sans correspondance : `COUNT(*)` compte aussi la ligne du LEFT JOIN avec colonnes `NULL`.

## Compter les factures payées sans exclure les clients

```sql
SELECT clients.name, COUNT(invoices.id) AS paid_invoice_count
FROM clients
LEFT JOIN invoices
    ON invoices.client_id = clients.id
    AND invoices.status = 'paid'
GROUP BY clients.id, clients.name
ORDER BY clients.name;
```

La condition `status = 'paid'` est dans **`ON`**. Si on la plaçait dans `WHERE`, les clients sans facture payée disparaîtraient.

## Total payé par client, y compris zéro

```sql
SELECT clients.name,
       COALESCE(SUM(invoices.amount), 0) AS total_paid
FROM clients
LEFT JOIN invoices
    ON invoices.client_id = clients.id
    AND invoices.status = 'paid'
GROUP BY clients.id, clients.name;
```

## Quand utiliser quoi ?

| Besoin | Jointure |
|---|---|
| Seulement les factures associées à un client | INNER JOIN |
| Tous les clients, même sans facture | LEFT JOIN en partant de clients |
| Tous les clients + uniquement leurs factures payées | LEFT JOIN avec `status` dans `ON` |
