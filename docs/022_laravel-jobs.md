---
title: Jobs et Queues
group: Laravel
summary: Décaler les traitements longs : email, PDF, export, notifications.
order: 22
slug: laravel-jobs
tags: jobs, queue, worker, dispatch, ShouldQueue
---

## Pourquoi les queues ?

Si une demande HTTP doit générer un gros PDF ou envoyer un email, on peut répondre rapidement au navigateur et faire traiter une tâche par un worker.

## Créer un Job

```bash
php artisan make:job ExportInvoices
```

```php
namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ExportInvoices implements ShouldQueue
{
    use Queueable;

    public function __construct(public int $userId) {}

    public function handle(): void
    {
        // Export CSV/PDF puis notification...
    }
}
```

## Envoyer le job dans une queue

```php
ExportInvoices::dispatch(auth()->id());
```

```bash
php artisan queue:work
```

**Attention :** avec `QUEUE_CONNECTION=sync`, le job s'exécute immédiatement dans la requête, donc pas en arrière-plan. Pour l'asynchrone, utiliser une connexion de queue appropriée (`database`, `redis`, etc.) et un worker actif.

## Event / Listener / Job

- **Event** : « une facture est payée ».
- **Listener** : « à cet événement, déclencher une confirmation ».
- **Job** : « effectuer l'envoi concret du mail ou l'export ».

Un listener peut lui-même être mis en queue avec `ShouldQueue`.

[Référence officielle : Queues](https://laravel.com/docs/13.x/queues)
