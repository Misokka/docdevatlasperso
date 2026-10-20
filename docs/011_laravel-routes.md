---
title: Routes, verbes HTTP et MVC
group: Laravel
summary: GET, POST, PUT, PATCH, DELETE, route model binding et resource controllers.
order: 11
slug: laravel-routes
tags: routes, web.php, resource, artisan
---

## Routes CRUD manuelles

```php
use App\Http\Controllers\InvoiceController;

Route::get('/invoices', [InvoiceController::class, 'index']);
Route::get('/invoices/create', [InvoiceController::class, 'create']);
Route::post('/invoices', [InvoiceController::class, 'store']);
Route::get('/invoices/{id}/edit', [InvoiceController::class, 'edit']);
Route::put('/invoices/{id}', [InvoiceController::class, 'update']);
Route::delete('/invoices/{id}', [InvoiceController::class, 'destroy']);
```

**Ordre important :** déclarer `/invoices/create` avant une route dynamique comme `/invoices/{id}` si elles pourraient entrer en conflit.

## Resource controller

```bash
php artisan make:controller InvoiceController --resource
php artisan make:model Invoice -m
php artisan route:list
```

```php
Route::resource('invoices', InvoiceController::class);
```

`Route::resource()` enregistre un ensemble de routes CRUD, mais **`make:controller --resource` ne déclare pas automatiquement les routes**.

## Route Model Binding

```php
Route::get('/invoices/{invoice}', [InvoiceController::class, 'show']);

public function show(Invoice $invoice)
{
    return view('invoices.show', compact('invoice'));
}
```

Si le modèle n'existe pas, Laravel renvoie généralement une 404.

## Protection d'une route

```php
Route::middleware('auth')->group(function () {
    Route::get('/invoices', [InvoiceController::class, 'index']);
});
```

## GET vs POST vs PUT vs PATCH vs DELETE

- `GET` : lire sans modifier l'état serveur.
- `POST` : créer ou déclencher une opération.
- `PUT` : remplacer une ressource (convention REST).
- `PATCH` : mise à jour partielle.
- `DELETE` : supprimer.

[Référence officielle : routing](https://laravel.com/docs/13.x/routing)
