# MVC PHP natif

Mini-application de factures utilisant PHP, PDO et SQLite, sans framework externe.

## Lancer le projet

Depuis ce dossier :

```bash
php database/init.php
php -S localhost:8000 router.php
```

Ouvrir ensuite :

- http://localhost:8000/invoices
- http://localhost:8000/invoices/1

Une route comme `/invoices/999` retourne une réponse HTTP 404.
