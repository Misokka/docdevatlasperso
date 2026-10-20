---
title: Events et Listeners
group: Laravel
summary: Découpler les actions à déclencher lorsqu’une facture est payée.
order: 21
slug: laravel-events
tags: event, listener, dispatch, facture
---

## Idée métier

Quand une facture est réglée, tu peux vouloir envoyer un reçu et enregistrer une notification. Le Controller ne doit pas connaître tous les traitements annexes.

## Créer un événement

```bash
php artisan make:event InvoicePaid
php artisan make:listener SendPaymentConfirmation --event=InvoicePaid
```

```php
// app/Events/InvoicePaid.php
namespace App\Events;

use App\Models\Invoice;
use Illuminate\Foundation\Events\Dispatchable;

class InvoicePaid
{
    use Dispatchable;

    public function __construct(public Invoice $invoice) {}
}
```

## Déclencher un événement

```php
// Après avoir réellement enregistré le paiement avec succès...
InvoicePaid::dispatch($invoice);
```

## Listener : réagir

```php
// app/Listeners/SendPaymentConfirmation.php
namespace App\Listeners;

use App\Events\InvoicePaid;

class SendPaymentConfirmation
{
    public function handle(InvoicePaid $event): void
    {
        // Exemple : déclencher l'envoi d'un reçu
        // SendInvoiceEmail::dispatch($event->invoice);
    }
}
```

## Découverte des listeners

Laravel peut découvrir les listeners placés dans `app/Listeners` selon la configuration et les conventions de la version, ou tu peux les enregistrer explicitement. Vérifie la configuration réelle du projet.

## Event vs Observer

Un **Event** représente un fait métier explicite : « InvoicePaid ». Un **Observer** est plutôt lié au cycle de vie Eloquent : `created`, `updated`, `deleted`.

[Référence officielle : Events](https://laravel.com/docs/13.x/events)
