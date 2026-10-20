---
title: Service Providers : register et boot
group: Laravel
summary: Bootstrap de Laravel, bindings, configuration et cycle de démarrage.
order: 20
slug: laravel-providers
tags: providers, register, boot, singleton, appserviceprovider
---

## Différence entre Service et Provider

- **Service** (`InvoiceService`) : fait une opération métier.
- **Service Provider** (`AppServiceProvider`) : enregistre/configure des services lors du démarrage de Laravel.

## Exemple de Provider

```php
namespace App\Providers;

use App\Services\InvoiceService;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->singleton(InvoiceService::class, function () {
            return new InvoiceService();
        });
    }

    public function boot(): void
    {
        // Initialisations possibles après enregistrement des providers
    }
}
```

Laravel peut généralement résoudre un service concret simple sans ce code : cet exemple explique le mécanisme, ce n'est pas une obligation.

## `register()` vs `boot()`

| Méthode | But |
|---|---|
| `register()` | Enregistrer des bindings dans le Service Container, **sans** y mettre les initialisations dépendantes des autres providers. |
| `boot()` | Initialiser des comportements une fois les providers enregistrés : par ex. View Composer. |

## Où les Providers sont-ils déclarés ?

Dans les structures Laravel modernes :

```php
// bootstrap/providers.php
return [
    App\Providers\AppServiceProvider::class,
];
```

## Pourquoi un fournisseur de dépendances ?

Pour associer une interface à son implémentation, définir une instance partagée ou configurer un service tiers.

```php
$this->app->bind(
    App\Contracts\PaymentGateway::class,
    App\Services\StripePaymentGateway::class
);
```

Le contrôleur peut ensuite demander l'interface au constructeur. Laravel choisit l'implémentation enregistrée.

[Référence officielle : Service Providers](https://laravel.com/docs/13.x/providers)
