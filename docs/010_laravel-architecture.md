---
title: Architecture et cycle MVC
group: Laravel
summary: Comment une requête traverse route, middleware, controller, service, modèle et vue.
order: 10
slug: laravel-architecture
tags: mvc, structure, lifecycle, web.php, directory
---

## Arborescence d'une application Laravel

```text
app/
├── Http/
│   ├── Controllers/InvoiceController.php
│   ├── Requests/StoreInvoiceRequest.php
│   ├── Middleware/EnsureUserIsAdmin.php
│   └── Resources/InvoiceResource.php
├── Models/Invoice.php
├── Services/InvoiceService.php           # convention personnelle
├── Providers/AppServiceProvider.php
├── Events/InvoicePaid.php
├── Listeners/SendConfirmation.php
├── Jobs/ExportInvoices.php
├── Policies/InvoicePolicy.php
└── Observers/InvoiceObserver.php
bootstrap/app.php
bootstrap/providers.php
routes/web.php
routes/api.php                           # si installé/configuré
resources/views/invoices/index.blade.php
database/migrations/
database/seeders/
config/
storage/logs/
tests/Feature/
```

**Important :** `Services/`, `Actions/`, `Repositories/`, `Observers/` et bien d'autres dossiers ne sont pas créés par défaut. Crée-les seulement quand c'est utile.

## Le trajet d'une requête

1. Navigateur → `GET /invoices`.
2. Laravel identifie la route dans `routes/web.php`.
3. Le middleware `auth` vérifie si l'utilisateur est connecté.
4. Le `InvoiceController@index` appelle Eloquent ou un Service.
5. Eloquent lit les factures en base.
6. Le Controller transmet les données à Blade.
7. Laravel renvoie le HTML au navigateur.

## Version basique

```php
// routes/web.php
use App\Http\Controllers\InvoiceController;
Route::get('/invoices', [InvoiceController::class, 'index']);
```

```php
namespace App\Http\Controllers;

use App\Models\Invoice;
use Illuminate\View\View;

class InvoiceController extends Controller
{
    public function index(): View
    {
        $invoices = Invoice::all();
        return view('invoices.index', compact('invoices'));
    }
}
```

```blade
<h1>Liste des factures</h1>
@foreach($invoices as $invoice)
    <p>{{ $invoice->client }} — {{ $invoice->amount }} €</p>
@endforeach
```

## Qui fait quoi ?

| Élément | Responsabilité |
|---|---|
| Route | Associe URL + verbe HTTP à un traitement. |
| Middleware | Filtre la requête (auth, droits, etc.). |
| Controller | Orchestre la requête et prépare la réponse. |
| Model / Eloquent | Données, relations, accès BDD. |
| Service | Logique métier réutilisable, si nécessaire. |
| Blade | HTML rendu côté serveur. |
| API Resource | Réponse JSON structurée. |

[Référence officielle : structure Laravel](https://laravel.com/docs/13.x/structure)
