---
title: SQL : SELECT, WHERE et CRUD
group: SQL & BDD
summary: Les bases PostgreSQL / SQLite, le filtre, le tri, INSERT, UPDATE et DELETE.
order: 28
slug: sql-select
tags: sql, select, where, insert, update, delete, order by
---

## Structure de deux tables

```sql
CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);
```

Le type `INTEGER PRIMARY KEY` de cet exemple est pratique en SQLite. PostgreSQL utilise couramment `GENERATED ... AS IDENTITY` ou `SERIAL` pour générer les identifiants.

## `SELECT`, `WHERE`, `AND`, `ORDER BY`

```sql
SELECT id, client_id, amount, status
FROM invoices
WHERE status = 'paid' AND amount >= 100
ORDER BY amount DESC;
```

## `INSERT`, `UPDATE`, `DELETE`

```sql
INSERT INTO invoices (id, client_id, amount, status)
VALUES (7, 1, 150, 'pending');

UPDATE invoices SET status = 'paid' WHERE id = 7;

DELETE FROM invoices WHERE id = 7;
```

**Toujours vérifier la clause `WHERE` avant de faire `UPDATE` / `DELETE`.**

## `LIMIT` et `OFFSET`

```sql
SELECT * FROM invoices ORDER BY id DESC LIMIT 5;
```

## Alias et égalité

```sql
SELECT i.amount AS invoice_amount FROM invoices AS i WHERE i.status = 'paid';
```

En SQL, l'égalité s'écrit `=`, pas `===`.
