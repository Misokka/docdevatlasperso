---
title: Validation, Form Requests et sécurité
group: Laravel
summary: validate(), required, numeric, confirmed, unique, fillable et old().
order: 15
slug: laravel-validation
tags: validation, request, fillable, required, unique, csrf
---

## Validation simple dans un Controller

```php
$validated = $request->validate([
    'client' => 'required|string|max:255',
    'amount' => 'required|numeric|min:0',
    'status' => 'required|in:paid,pending',
]);

Invoice::create($validated);
```

En cas d'échec, Laravel renvoie les erreurs adaptées à une requête web (redirection) ou à une demande JSON (réponse 422), selon le contexte.

## Règles récurrentes

| Règle | Signification |
|---|---|
| `required` | Obligatoire |
| `string` | Chaîne |
| `numeric` | Numérique |
| `min:0` | Minimum 0 pour une valeur numérique |
| `email` | Format email |
| `unique:users,email` | Valeur absente de la colonne email des autres utilisateurs |
| `confirmed` | Correspond à `<champ>_confirmation` |
| `in:paid,pending` | Valeur parmi celles-ci |
| `exists:clients,id` | Clé présente dans la table clients |

## Form Request : déplacer la validation

```bash
php artisan make:request StoreInvoiceRequest
```

```php
class StoreInvoiceRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true; // ou logique d'autorisation métier
    }

    public function rules(): array
    {
        return [
            'client' => 'required|string',
            'amount' => 'required|numeric|min:0',
            'status' => 'required|in:paid,pending',
        ];
    }
}
```

```php
public function store(StoreInvoiceRequest $request)
{
    Invoice::create($request->validated());
    return redirect('/invoices');
}
```

## Validation vs `$fillable`

`validate()` vérifie **la conformité des données reçues** ; `$fillable` autorise **les attributs pouvant être remplis automatiquement** par `create()` / `update()`. Ce sont deux protections complémentaires, indépendantes.

```php
class Invoice extends Model
{
    protected $fillable = ['client', 'amount', 'status'];
}
```

## Formulaire et erreurs

```blade
<input name="client" value="{{ old('client') }}">
@error('client')
    <p>{{ $message }}</p>
@enderror
```

Un formulaire POST/PUT/PATCH/DELETE sur les routes `web` doit transmettre un jeton `@csrf`.

[Référence officielle : validation](https://laravel.com/docs/13.x/validation)
