---
title: Artisan, migrations et seeders
group: Laravel
summary: Créer modèle, migration, controller, remplir la base et inspecter les routes.
order: 25
slug: laravel-migrations
tags: artisan, make:model, migration, seed, sqlite
---

## Les commandes qui servent vraiment

```bash
php artisan make:model Invoice -m
php artisan make:controller InvoiceController --resource
php artisan make:request StoreInvoiceRequest
php artisan make:seeder InvoiceSeeder
php artisan make:policy InvoicePolicy --model=Invoice
php artisan make:job ExportInvoices
php artisan make:event InvoicePaid
php artisan route:list
php artisan migrate:status
```

`--resource` prépare les méthodes du Controller ; il ne crée pas les routes de ton application.

## Migration de table invoices

```php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::create('invoices', function (Blueprint $table) {
    $table->id();
    $table->foreignId('client_id')->constrained()->cascadeOnDelete();
    $table->decimal('amount', 10, 2);
    $table->string('status')->default('pending');
    $table->timestamps();
});
```

## Une ligne Seeder

```php
DB::table('invoices')->insert([
    'client_id' => 1,
    'amount' => 120,
    'status' => 'paid',
    'created_at' => now(),
    'updated_at' => now(),
]);
```

```bash
php artisan migrate
php artisan db:seed --class=InvoiceSeeder
```

## Attention aux timestamps

```php
class Invoice extends Model
{
    public $timestamps = false; // seulement si table sans created_at/updated_at
}
```

## SQLite / PostgreSQL

Dans `.env`, Laravel peut se connecter à `sqlite`, `pgsql`, `mysql` selon le driver disponible. Vérifie toujours la base réellement utilisée avant une migration.

**Jamais de `migrate:fresh` sur la base de quelqu'un sans autorisation explicite : cette commande détruit les tables.**

[Référence officielle : Migrations](https://laravel.com/docs/13.x/migrations)
