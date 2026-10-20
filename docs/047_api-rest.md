---
title: API REST et statuts HTTP
group: Outils & Web
summary: GET/POST/PUT/PATCH/DELETE, HTTP 401/403/404/422 et JSON.
order: 47
slug: api-rest
tags: api, rest, http, 401, 403, 404, 422, put, patch
---

## Verbes HTTP

| Verbe | Rôle |
|---|---|
| GET | Lire une ressource |
| POST | Créer ou déclencher une opération |
| PUT | Remplacer entièrement une ressource (convention REST) |
| PATCH | Appliquer une modification partielle |
| DELETE | Supprimer |

Un `PUT` est censé être idempotent : répéter exactement la requête doit laisser le serveur dans le même état. Un `PATCH` n'est pas forcément idempotent.

## Codes HTTP à retenir

| Code | Sens | Exemple |
|---|---|---|
| 200 | OK | Liste récupérée |
| 201 | Created | Facture créée |
| 204 | No Content | Suppression sans corps |
| 400 | Bad Request | Requête mal formée |
| 401 | Non authentifié | Jeton d'auth absent ou invalide |
| 403 | Interdit | Authentifié mais droits insuffisants |
| 404 | Introuvable | Facture ou route absente |
| 422 | Unprocessable Content | Validation échouée |
| 500 | Erreur serveur | Exception non gérée |

## Exemple API Laravel

```php
Route::get('/api/invoices', function () {
    return response()->json(
        Invoice::query()->select('id', 'client', 'amount', 'status')->get()
    );
});
```

Cet exemple montre simplement une réponse JSON : en production, ajouter authentification, autorisation, pagination et sérialisation cohérente si nécessaire.

## CORS, CSRF, Sanctum

- **CORS** : règles navigateur pour les appels entre origines différentes.
- **CSRF** : protection contre les actions intersites non autorisées avec cookies de session.
- **Sanctum** : solution Laravel d'authentification notamment pour SPA / API selon la configuration.

Pour une API stateless avec bearer token, les besoins CSRF diffèrent de ceux d'une SPA utilisant les cookies de session.
