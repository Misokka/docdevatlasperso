---
title: Next.js : SSR, CSR, rendu et API
group: Next.js
summary: SSR vs CSR, API route handlers et règles simples de récupération de données.
order: 40
slug: next-rendering
tags: ssr, csr, server, api, fetch, routes
---

## SSR vs CSR

| Terme | Signification |
|---|---|
| SSR | HTML préparé côté serveur et envoyé au navigateur. |
| CSR | Interface rendue côté client, via JavaScript. |
| SSG | Pages générées à l'avance, lorsque cette stratégie est adaptée. |

L'interactivité peut s'ajouter après l'arrivée du HTML ; le choix de rendu n'est pas identique à la distinction Server/Client Components.

## Route Handler dans App Router

```ts
// app/api/health/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
    return NextResponse.json({ ok: true });
}
```

## API Laravel séparée

Si Laravel est le backend, Next.js peut faire des appels vers l'API Laravel. Attention à l'authentification, aux cookies/CORS et à la destination serveur ou navigateur des requêtes.

## `loading.tsx`

```tsx
// app/invoices/loading.tsx
export default function Loading() {
    return <p>Chargement des factures…</p>;
}
```

Le composant est utilisé par Next pendant la suspension du segment de route correspondant ; pas besoin d'afficher soi-même ce fichier dans `page.tsx`.

## Quand choisir Blade, Vue ou Next ?

- **Blade** : rendu HTML Laravel simple, efficace, idéal pour petit CRUD MVC.
- **Vue** : composants réactifs côté frontend, intégrables dans Laravel ou en SPA.
- **Next** : environnement React avec routing, rendu serveur et fonctionnalités fullstack.
