---
title: TypeScript : type, interface et union
group: JavaScript & TypeScript
summary: Typage statique, inférence, type/interface, unions et pièges de any.
order: 38
slug: typescript-bases
tags: typescript, type, interface, any, types, union
---

## Pourquoi TypeScript ?

TypeScript ajoute un **système de types statiques** à JavaScript. Les erreurs de type peuvent être détectées pendant le développement / la compilation. Les annotations TypeScript ne constituent **pas une validation de sécurité à l'exécution**.

```ts
let amount: number = 120;
let client: string = 'Alice';
const isPaid: boolean = true;
```

TypeScript infère souvent les types ; il n'est pas nécessaire d'annoter chaque variable.

## `type` : alias, unions et objets

```ts
type InvoiceStatus = 'paid' | 'pending';

type Invoice = {
    id: number;
    client: string;
    amount: number;
    status: InvoiceStatus;
};
```

## `interface` : forme d'un objet

```ts
interface Invoice {
    id: number;
    client: string;
    amount: number;
    status: 'paid' | 'pending';
}
```

**Les deux peuvent décrire un objet.** Les `interface` supportent notamment l'extension et la fusion de déclarations ; `type` est plus général pour les unions, tuples et alias d'autres types.

## Propriété optionnelle et fonction typée

```ts
interface User {
    id: number;
    email: string;
    phone?: string;
}

function getInvoiceTotal(invoices: Invoice[]): number {
    return invoices.reduce((sum, invoice) => sum + invoice.amount, 0);
}
```

## `unknown` vs `any`

```ts
let raw: unknown = JSON.parse('{"amount":120}');
// raw.amount : interdit tant qu'on n'a pas vérifié la structure.
```

`any` désactive largement la vérification, alors que `unknown` exige de vérifier avant usage. C'est généralement plus sûr pour des données externes.

## Ne pas confondre TypeScript et sécurité backend

Même avec des types TS, il faut **toujours valider les entrées côté Laravel**. Les types sont effacés à l'exécution JavaScript.

[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
