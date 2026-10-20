---
title: Deux exercices pratiques reproductibles
group: Méthodes
summary: Modifier une page MVC et diagnostiquer un accumulateur incorrect pas à pas.
order: 48
slug: exercices-pratiques
tags: test, exercice, mvc, boucle, bug, diagnostic
---

## Exercice 1 : modifier une page Laravel

**Point de départ :** une route `/invoices`, un Controller `index()` qui fait `Invoice::all()` et un Blade qui affiche un tableau.

**Consigne 1 :** n'afficher que les factures payées, compter leurs lignes, calculer le montant total avec une boucle PHP.

```php
public function index(): View
{
    $invoices = Invoice::where('status', 'paid')->get();
    $count = 0;
    $total = 0;

    foreach ($invoices as $invoice) {
        $count++;
        $total += $invoice->amount;
    }

    return view('invoices.index', compact('invoices', 'count', 'total'));
}
```

**Consigne 2 :** total par client, sans casser la liste ni les compteurs.

```php
$totalsByClient = [];
foreach ($invoices as $invoice) {
    $name = $invoice->client;
    if (!isset($totalsByClient[$name])) {
        $totalsByClient[$name] = 0;
    }
    $totalsByClient[$name] += $invoice->amount;
}
```

## Exercice 2 : le bug caché

**Symptôme :** trois factures `pending`, le montant affiché correspond pourtant à la dernière facture uniquement (ex. 60 €), au lieu du total (ex. 325 €).

```php
// Bug :
$pendingAmount = $invoice->amount;
// Correction :
$pendingAmount += $invoice->amount;
```

Puis ajouter `$totalInvoicesPending++` dans la même condition `if` et transmettre la variable à Blade.

## Critères de vérification

- La demande est comprise avant de modifier le code.
- La route, le Controller, le Model et le template Blade sont identifiés.
- La modification reste ciblée et cohérente avec l'architecture existante.
- La page est vérifiée après la modification.
- Les résultats incorrects sont diagnostiqués à partir de données connues.

## Dans quel ordre travailler ?

**Comprendre → Modifier → Tester → Expliquer.** Cette démarche rend le changement traçable et limite les régressions.
