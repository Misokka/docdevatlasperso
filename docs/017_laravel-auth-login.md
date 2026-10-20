---
title: Authentification : login, session, logout
group: Laravel
summary: LoginController complet : Auth::attempt, regeneration de session, logout et middleware guest/auth.
order: 17
slug: laravel-auth-login
tags: login, Auth::attempt, Auth::logout, session, guest, auth
---

## Login : on ne crée pas un utilisateur

À la connexion, Laravel cherche un utilisateur et vérifie que son mot de passe correspond au hash enregistré. **Ne fais pas `User::create()` dans le login.**

## LoginController : affichage et connexion

```php
namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Validation\ValidationException;

class LoginController extends Controller
{
    public function create()
    {
        return view('auth.login');
    }

    public function store(Request $request)
    {
        $credentials = $request->validate([
            'email' => 'required|email',
            'password' => 'required|string',
        ]);

        if (! Auth::attempt($credentials)) {
            throw ValidationException::withMessages([
                'email' => 'Identifiants incorrects.',
            ]);
        }

        $request->session()->regenerate();
        return redirect()->intended('/dashboard');
    }

    public function destroy(Request $request)
    {
        Auth::logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return redirect('/login');
    }
}
```

**`Auth::attempt()`** est le mot-clé à chercher dans la doc. En production, utiliser aussi une limitation des tentatives de connexion (rate limiting).

## Formulaire login

```blade
<form action="/login" method="POST">
    @csrf
    <input type="email" name="email" value="{{ old('email') }}" required>
    <input type="password" name="password" required>
    <button type="submit">Se connecter</button>
</form>
```

## Routes login / logout / espace protégé

```php
use App\Http\Controllers\Auth\LoginController;

Route::middleware('guest')->group(function () {
    Route::get('/login', [LoginController::class, 'create'])->name('login');
    Route::post('/login', [LoginController::class, 'store']);
});

Route::middleware('auth')->group(function () {
    Route::get('/dashboard', fn () => view('dashboard'));
    Route::post('/logout', [LoginController::class, 'destroy']);
});
```

## Concepts de sécurité

- **Authentification** : vérifier qui est connecté.
- **Autorisation** : vérifier ce que l'utilisateur peut faire (Policies, Gates).
- `auth` : refuse une route protégée aux non connectés.
- `guest` : réservé aux visiteurs non connectés.
- CSRF : protège contre les requêtes intersites non autorisées ; **ne remplace pas l'authentification**.

## Codes HTTP et Laravel

| Code | Idée |
|---|---|
| 401 | Non authentifié (souvent API) |
| 403 | Identifié mais non autorisé |
| 404 | Route ou ressource introuvable |
| 419 | Session expirée / jeton CSRF problématique (usage Laravel web) |
| 422 | Erreurs de validation, souvent pour JSON |

[Référence officielle : Manually Authenticating Users](https://laravel.com/docs/13.x/authentication#manually-authenticating-users)
