---
title: Next.js : App Router et composants
group: Next.js
summary: Server vs Client Components, use client, page.tsx, layout.tsx, loading.tsx.
order: 39
slug: next-app-router
tags: nextjs, server component, client component, use client, app router
---

## Un framework React

Next.js ajoute notamment routing, rendu serveur, conventions de fichiers et fonctionnalités fullstack à React.

## Structure de l'App Router

```text
app/
├── layout.tsx
├── page.tsx
└── invoices/
    ├── page.tsx
    ├── loading.tsx
    └── [id]/
        └── page.tsx
components/
└── InvoiceButton.tsx
```

- `app/invoices/page.tsx` → `/invoices`.
- `app/invoices/[id]/page.tsx` → route dynamique `/invoices/123`.
- `loading.tsx` → interface de chargement pour le segment concerné.
- `layout.tsx` → enveloppe partagée par les pages enfant.

## Server Component : par défaut

```tsx
// app/invoices/page.tsx
import InvoiceButton from '@/components/InvoiceButton';

export default async function Page() {
    const response = await fetch('https://example.org/api/invoices', { cache: 'no-store' });
    if (!response.ok) throw new Error('API indisponible');
    const invoices = await response.json();

    return <main><h1>Factures</h1><InvoiceButton /></main>;
}
```

Cet exemple suppose un endpoint public d'exemple ; adapte l'URL, les règles de cache et l'authentification à ton vrai projet.

## Client Component : interaction

```tsx
'use client';

import { useState } from 'react';

export default function InvoiceButton() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(n => n + 1)}>Clics : {count}</button>;
}
```

**`'use client'` doit être écrit exactement ainsi**, en haut du fichier concerné. Un Server Component peut rendre un Client Component. Pour les besoins interactifs, mettre uniquement les parties nécessaires en client.

## Props dans React / Next

Le parent fournit des **props** à l'enfant ; pour remonter une action, on passe souvent une fonction callback dans le cadre de composants client compatibles. **`emit` est le terme de Vue.js, pas React.**

[Next.js — App Router](https://nextjs.org/docs/app) · [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
