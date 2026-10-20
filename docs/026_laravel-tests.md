---
title: Tests Feature et Unit avec Laravel
group: Laravel
summary: Tester une route, la validation et une règle métier ; commandes Artisan/PHPUnit.
order: 26
slug: laravel-tests
tags: testing, feature, unit, phpunit, pest
---

## Feature test : une route HTTP

```bash
php artisan make:test InvoiceIndexTest
php artisan test
```

```php
namespace Tests\Feature;

use App\Models\Invoice;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class InvoiceIndexTest extends TestCase
{
    use RefreshDatabase;

    public function test_invoices_page_works(): void
    {
        Invoice::factory()->create(['status' => 'paid']);

        $response = $this->get('/invoices');
        $response->assertOk();
    }
}
```

L'exemple suppose que le modèle possède une factory et que les éventuels middlewares requis sont pris en charge dans le test. `RefreshDatabase` doit être exécuté sur une **base de test**, jamais la base réelle.

## Tester une validation

```php
$response = $this->post('/invoices', [
    'client' => '',
    'amount' => -10,
    'status' => 'unknown',
]);

$response->assertSessionHasErrors(['client', 'amount', 'status']);
```

## Test Unit : une règle isolée

Un test Unit doit cibler une fonction ou un Service sans requête HTTP complète ; si le test touche à Eloquent et à la BDD, il faut prévoir l'environnement adapté.

## Choisir des cas utiles

Un test simple et pertinent vaut mieux qu'une grosse suite de tests artificiels. Teste les cas limites : montant négatif, statut invalide, facture inexistante, utilisateur non autorisé.

[Référence officielle : Testing](https://laravel.com/docs/13.x/testing)
