---
title: Authentification : inscription
group: Laravel
summary: RegisterController complet avec validation, hash, User::create et connexion initiale.
order: 16
slug: laravel-auth-inscription
tags: auth, register, inscription, Hash::make, User::create
---

## Ce qui change par rapport à un CRUD Invoice

L'inscription crée bien un utilisateur (`store()`), mais doit vérifier l'unicité de l'email, **ne jamais stocker un mot de passe en clair**, et gérer la session / la connexion après création.

## Modèle User : authentifiable

```php
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable
{
    protected $fillable = ['name', 'email', 'password'];
    protected $hidden = ['password', 'remember_token'];
}
```

`Authenticatable` permet d'utiliser le modèle dans le système d'auth Laravel. `$hidden` retire ces attributs de la sérialisation du modèle ; ce n'est pas un mécanisme de contrôle d'accès en base.

## RegisterController complet, version manuelle

```php
namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;

class RegisterController extends Controller
{
    public function create()
    {
        return view('auth.register');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255|unique:users,email',
            'password' => 'required|string|min:8|confirmed',
        ]);

        $user = User::create([
            'name' => $validated['name'],
            'email' => $validated['email'],
            'password' => Hash::make($validated['password']),
        ]);

        Auth::login($user);
        $request->session()->regenerate();

        return redirect('/dashboard');
    }
}
```

`confirmed` attend un champ de formulaire `password_confirmation`. Un projet Laravel moderne peut aussi utiliser le cast `hashed` sur `password` : il faut connaître la configuration de son modèle avant de dupliquer des mécanismes.

## Vue Blade d'inscription

```blade
<form action="/register" method="POST">
    @csrf
    <input name="name" value="{{ old('name') }}" required>
    <input type="email" name="email" value="{{ old('email') }}" required>
    <input type="password" name="password" required>
    <input type="password" name="password_confirmation" required>
    <button type="submit">S'inscrire</button>
</form>
```

## Routes

```php
use App\Http\Controllers\Auth\RegisterController;

Route::middleware('guest')->group(function () {
    Route::get('/register', [RegisterController::class, 'create']);
    Route::post('/register', [RegisterController::class, 'store']);
});
```

## En vrai projet

Privilégier une solution d'authentification Laravel éprouvée (starter kit / Fortify, selon le projet) plutôt que coder soi-même toutes les protections. Ajouter selon les besoins vérification d'email, reset du mot de passe et limitations anti-bruteforce.

[Documentation Laravel — Authentication](https://laravel.com/docs/13.x/authentication) · [Starter kits](https://laravel.com/docs/13.x/starter-kits)
