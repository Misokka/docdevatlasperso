---
title: Symfony : MVC, Doctrine, services
group: Java & Symfony
summary: Les bases de Symfony à retrouver : routing, controller, Twig, Doctrine et autowiring.
order: 43
slug: symfony-bases
tags: symfony, doctrine, twig, mvc, dependency injection
---

## Symfony dans une application web

Comme Laravel, Symfony est un framework PHP. Une route appelle un Controller, qui récupère des données et retourne une réponse HTML (souvent Twig) ou JSON.

## Controller Symfony

```php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class InvoiceController extends AbstractController
{
    #[Route('/invoices', name: 'invoice_index')]
    public function index(): Response
    {
        return $this->render('invoices/index.html.twig', [
            'title' => 'Liste des factures',
        ]);
    }
}
```

## Doctrine : persistance et repositories

Dans de nombreux projets Symfony, Doctrine ORM gère les entités et leurs relations ; les repositories servent à retrouver les données. En Laravel, on utilise souvent directement les modèles Eloquent.

## Template Twig

```html
<h1>{{ title }}</h1>
{% for invoice in invoices %}
    <p>{{ invoice.amount }}</p>
{% endfor %}
```

## Service / Dependency Injection

```php
class InvoiceController extends AbstractController
{
    public function __construct(private InvoiceService $invoiceService) {}
}
```

Symfony peut injecter automatiquement un service enregistré / autowirable. Une dépendance se fournit au Controller au lieu d'être créée avec `new` dans chaque action.

## À retenir

- Laravel → Blade + Eloquent + Artisan.
- Symfony → Twig + Doctrine (souvent) + Console Symfony.
- Deux frameworks PHP, utilisant routing, controllers, services, injection de dépendances, architecture modulaire.

[Symfony Documentation](https://symfony.com/doc/current/index.html)
