---
title: PostgreSQL : index et transactions
group: SQL & BDD
summary: Index pour recherches par email, EXPLAIN, contraintes et transactions.
order: 31
slug: postgresql-index
tags: postgres, index, explain, transaction, btree
---

## Problème : une recherche par email est lente

Une table `users` contient un million d'utilisateurs. Sans index pertinent, PostgreSQL peut devoir parcourir de nombreuses lignes.

```sql
CREATE INDEX idx_users_email ON users(email);
```

Pour une colonne utilisée comme identifiant unique, une **contrainte UNIQUE** fournit aussi un index adapté :

```sql
ALTER TABLE users ADD CONSTRAINT users_email_unique UNIQUE (email);
```

## Lire le plan d'exécution

```sql
EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'alice@example.com';
```

Un index peut améliorer les lectures, mais prend de l'espace et ajoute du coût aux écritures. Le planificateur peut choisir de ne pas l'utiliser si ce n'est pas rentable.

## Transactions

```sql
BEGIN;
UPDATE invoices SET status = 'paid' WHERE id = 10;
INSERT INTO payments (invoice_id, amount) VALUES (10, 120);
COMMIT;
```

En cas d'échec avant `COMMIT`, on peut utiliser `ROLLBACK` pour annuler la transaction.

## Types et clés étrangères

```sql
CREATE TABLE invoices (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id BIGINT NOT NULL REFERENCES clients(id),
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0)
);
```

Le type de la clé étrangère doit être compatible avec celui de la clé référencée.

[Documentation officielle PostgreSQL](https://www.postgresql.org/docs/current/index.html)
