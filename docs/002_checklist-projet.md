---
title: Checklist de prise en main d’un projet
group: Commencer
summary: Une démarche fiable pour comprendre un projet existant, le modifier et vérifier le résultat.
order: 2
slug: checklist-projet
tags: checklist, méthodologie, autonomie, projet, diagnostic
---

## Objectif

Cette checklist aide à prendre en main une base de code inconnue avant d’y apporter une modification ciblée. Elle convient notamment à une tâche impliquant une boucle PHP, un test automatisé ou une page MVC.

**Priorité :** lire l'existant, comprendre le chemin d'une requête, modifier une fonctionnalité simple et vérifier le résultat sans exposer de données sensibles.

## Déroulement recommandé

1. **Lire la demande** et la reformuler : « Je dois afficher les factures payées et calculer leur total. »
2. Regarder le projet : `routes/web.php` → Controller → Model → Blade / frontend → `.env` sans afficher les secrets.
3. Vérifier que la page de départ fonctionne avant de modifier quoi que ce soit.
4. Faire une modification **minimale**, pas une refonte.
5. Relancer la page, vérifier les cas pertinents et documenter le choix.
6. En cas de blocage : consulter la documentation officielle, isoler le problème et demander une précision utile.

## Le squelette d'une tâche Laravel

```php
// routes/web.php
Route::get('/invoices', [InvoiceController::class, 'index']);

// InvoiceController.php
public function index(): View
{
    $invoices = Invoice::where('status', 'paid')->get();

    return view('invoices.index', compact('invoices'));
}
```

```blade
@foreach ($invoices as $invoice)
    <tr>
        <td>{{ $invoice->client }}</td>
        <td>{{ $invoice->amount }} €</td>
    </tr>
@endforeach
```

## Si la tâche utilise Vue.js

Si le choix technique est libre et que l’interactivité reste limitée, Blade peut suffire. Si Vue fait partie de l’architecture du projet, commence par la structure minimale et consulte la documentation officielle si nécessaire.

## À éviter

- Conclure trop vite avant d'avoir regardé le code et les logs.
- Prétendre connaître une API inconnue ou réciter du code non compris.
- Confondre `Invoice::all()` (déjà exécuté) et `Invoice::where(...)->get()` (requête construite puis exécutée).
- Copier du code externe sans comprendre ce qu'il fait.
- Publier des fichiers `.env`, jetons ou données clients dans une documentation publique.

## Expliquer une décision technique

Une explication efficace contient **ce que c'est → à quoi ça sert → un exemple concret**. Si une information manque, indique précisément la limite actuelle et la source à consulter plutôt que d'improviser.
