---
title: Débogage PHP et lecture d’existant
group: PHP
summary: Diagnostiquer un résultat incohérent, des logs et les erreurs fréquentes.
order: 9
slug: php-debogage
tags: bug, debug, logs, php
---

## Méthode de diagnostic en cinq temps

1. Reproduire le bug avec des données connues.
2. Vérifier la **valeur réellement affichée** et l'attendu métier.
3. Remonter de la vue au contrôleur puis au modèle / à la requête.
4. Isoler la condition ou l'accumulateur incorrect.
5. Corriger localement, relancer et vérifier un autre cas.

## Exemple d'accumulateur cassé

```php
$total = 0;
foreach ($invoices as $invoice) {
    if ($invoice->status === 'pending') {
        $total = $invoice->amount; // écrase à chaque tour
    }
}
```

La correction est `$total += $invoice->amount;`. Si le résultat final correspond à **la dernière facture**, soupçonne un écrasement dans une boucle.

## Inspecter des variables

```php
var_dump($invoices);  // PHP brut
print_r($invoices);   // affichage rapide
// Laravel :
dump($invoices);
dd($invoices);        // affiche puis interrompt
```

## Consulter les logs Laravel

```bash
# Logs habituels dans storage/logs/
php artisan route:list
php artisan optimize:clear
```

## Sécurité pendant le diagnostic

Ne pas exposer le `.env` ni les données des clients. Ne pas lancer `migrate:fresh` sur une base réelle. Consigne les étapes de reproduction et vérifie la correction sur un environnement isolé.
