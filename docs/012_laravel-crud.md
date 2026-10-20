---
title: CRUD complet : contrôleur et Blade
group: Laravel
summary: Les six méthodes essentielles, les formulaires et la validation dans un même endroit.
order: 12
slug: laravel-crud
tags: crud, store, update, destroy, create, edit, blade
---

## Contrôleur : lecture, création, modification, suppression

```php
namespace App\Http\Controllers;

use App\Models\Invoice;
use Illuminate\Http\Request;
use Illuminate\View\View;

class InvoiceController extends Controller
{
    public function index(): View
    {
        return view('invoices.index', [
            'invoices' => Invoice::orderBy('id', 'desc')->get(),
        ]);
    }

    public function create(): View
    {
        return view('invoices.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'client' => 'required|string|max:255',
            'amount' => 'required|numeric|min:0',
            'status' => 'required|in:paid,pending',
        ]);

        Invoice::create($validated);
        return redirect('/invoices');
    }

    public function edit(Invoice $invoice): View
    {
        return view('invoices.edit', compact('invoice'));
    }

    public function update(Request $request, Invoice $invoice)
    {
        $validated = $request->validate([
            'client' => 'required|string|max:255',
            'amount' => 'required|numeric|min:0',
            'status' => 'required|in:paid,pending',
        ]);
        $invoice->update($validated);
        return redirect('/invoices');
    }

    public function destroy(Invoice $invoice)
    {
        $invoice->delete();
        return redirect('/invoices');
    }
}
```

Pour que `Invoice $invoice` soit injecté, la route doit utiliser `{invoice}`. Dans une route `{id}`, utilise plutôt `findOrFail($id)`.

## Modèle Eloquent

```php
class Invoice extends Model
{
    protected $fillable = ['client', 'amount', 'status'];
}
```

Si la table ne possède pas `created_at` et `updated_at` :

```php
public $timestamps = false;
```

## Formulaire de création

```blade
<form action="/invoices" method="POST">
    @csrf
    <input name="client" value="{{ old('client') }}">
    <input type="number" step="0.01" name="amount" value="{{ old('amount') }}">
    <select name="status">
        <option value="pending">En attente</option>
        <option value="paid">Payée</option>
    </select>
    <button type="submit">Créer</button>
</form>
```

## Formulaire de modification

```blade
<form action="/invoices/{{ $invoice->id }}" method="POST">
    @csrf
    @method('PUT')
    <input name="client" value="{{ old('client', $invoice->client) }}">
    <input name="amount" value="{{ old('amount', $invoice->amount) }}">
    <input name="status" value="{{ old('status', $invoice->status) }}">
    <button type="submit">Modifier</button>
</form>
```

## Bouton de suppression

```blade
<form action="/invoices/{{ $invoice->id }}" method="POST">
    @csrf
    @method('DELETE')
    <button type="submit">Supprimer</button>
</form>
```

Le HTML n'envoie directement que `GET` et `POST` ; `@method()` permet à Laravel d'interpréter les verbes supplémentaires.
