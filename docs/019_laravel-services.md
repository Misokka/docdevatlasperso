---
title: Services et injection de dépendances
group: Laravel
summary: Externaliser la logique métier, comprendre le container et constructor injection.
order: 19
slug: laravel-services
tags: services, injection, container, autowiring
---

## Pourquoi créer un Service ?

Un Controller traite la requête HTTP, mais un calcul complexe ou une règle métier réutilisée mérite parfois sa propre classe.

```php
// app/Services/InvoiceService.php
namespace App\Services;

use App\Models\Invoice;

class InvoiceService
{
    public function getPendingTotal(): float
    {
        return (float) Invoice::where('status', 'pending')->sum('amount');
    }
}
```

**`app/Services` n'est pas obligatoire** : ce dossier est un choix d'organisation.

## Injection dans un contrôleur

```php
use App\Services\InvoiceService;

class InvoiceController extends Controller
{
    public function __construct(private InvoiceService $invoiceService) {}

    public function index()
    {
        $total = $this->invoiceService->getPendingTotal();
        return view('invoices.index', compact('total'));
    }
}
```

Ici, Laravel peut fournir automatiquement `InvoiceService` si ses dépendances sont résolubles : c'est l'**injection de dépendances** via le **Service Container**.

## Résolution manuelle, si nécessaire

```php
$service = app(InvoiceService::class);
$total = $service->getPendingTotal();
```

## Pourquoi c'est utile ?

- Contrôleurs plus lisibles.
- Logique métier testable indépendamment de HTTP.
- Services réutilisables ailleurs (Job, commande, autre Controller).
- On peut remplacer une implémentation dans les tests.

## `bind()` vs `singleton()`

```php
$this->app->bind(InvoiceService::class, fn () => new InvoiceService());
$this->app->singleton(InvoiceService::class, fn () => new InvoiceService());
```

- `bind` : résolution vers une nouvelle instance.
- `singleton` : une instance partagée dans le cycle de vie du conteneur.

Pour une classe simple sans dépendance particulière, un binding explicite n'est souvent **pas nécessaire**.

[Référence officielle : Service Container](https://laravel.com/docs/13.x/container)
