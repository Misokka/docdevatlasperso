---
title: Observers, notifications et mails
group: Laravel
summary: Réagir aux opérations Eloquent et notifier les utilisateurs.
order: 23
slug: laravel-observers
tags: observer, created, updated, mail, notification
---

## Observer : le cycle de vie d'un modèle

```bash
php artisan make:observer InvoiceObserver --model=Invoice
```

```php
class InvoiceObserver
{
    public function created(Invoice $invoice): void
    {
        // Action après la création.
    }

    public function updated(Invoice $invoice): void
    {
        // Action après une mise à jour.
    }
}
```

On peut enregistrer l'observer dans la phase de bootstrap de l'application selon la version, par exemple `Invoice::observe(InvoiceObserver::class)` depuis `AppServiceProvider::boot()`.

## Notifications

```bash
php artisan make:notification InvoiceOverdueNotification
```

```php
$user->notify(new InvoiceOverdueNotification($invoice));
```

L'utilisateur doit disposer du trait / comportement `Notifiable`, ce qui est généralement le cas du modèle `User` d'un projet Laravel standard.

## Mailable

```bash
php artisan make:mail InvoicePaidMail
```

```php
use Illuminate\Support\Facades\Mail;

Mail::to($user->email)->send(new InvoicePaidMail($invoice));
```

Les classes Mail peuvent être envoyées par queue pour ne pas bloquer la requête.

## Faut-il tout créer ?

Non. Un petit CRUD ne nécessite ni Observer, ni Event, ni Job. Ces outils servent quand les responsabilités deviennent plus complexes.

[Référence officielle : Notifications](https://laravel.com/docs/13.x/notifications) · [Mail](https://laravel.com/docs/13.x/mail)
