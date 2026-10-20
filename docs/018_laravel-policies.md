---
title: Middleware, Policies et permissions
group: Laravel
summary: Différences entre authentification, autorisations de ressources et Form Requests.
order: 18
slug: laravel-policies
tags: middleware, policy, gate, authorization, auth
---

## Middleware : filtrer la requête

```php
Route::middleware('auth')->group(function () {
    Route::get('/invoices', [InvoiceController::class, 'index']);
});
```

## Policy : contrôler les droits sur une facture

```bash
php artisan make:policy InvoicePolicy --model=Invoice
```

```php
namespace App\Policies;

use App\Models\Invoice;
use App\Models\User;

class InvoicePolicy
{
    public function update(User $user, Invoice $invoice): bool
    {
        return $invoice->user_id === $user->id;
    }
}
```

```php
public function update(Request $request, Invoice $invoice)
{
    $this->authorize('update', $invoice);
    // Puis validation et modification...
}
```

Selon le contrôleur de base / la version Laravel, l'appel à `authorize()` via le trait `AuthorizesRequests` peut nécessiter que celui-ci soit activé ; alternative universelle : `Gate::authorize('update', $invoice)`.

## Authorization avec Gate

```php
use Illuminate\Support\Facades\Gate;

Gate::authorize('update', $invoice);
```

## Middleware personnalisé

```bash
php artisan make:middleware EnsureUserIsAdmin
```

```php
public function handle(Request $request, Closure $next)
{
    if (! $request->user()?->is_admin) {
        abort(403);
    }
    return $next($request);
}
```

Le middleware ne doit pas remplacer les contrôles d'autorisation métier spécifiques à un objet.

## À retenir

- Middleware `auth` : est-ce que tu es connecté ?
- Policy `update` : as-tu le droit de modifier **cette** facture ?
- Validation : les données reçues sont-elles conformes ?

[Référence officielle : Authorization](https://laravel.com/docs/13.x/authorization)
