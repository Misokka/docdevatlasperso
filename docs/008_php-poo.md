---
title: PHP orienté objet
group: PHP
summary: Classes, propriétés, constructeurs, héritage, interfaces et visibilité.
order: 8
slug: php-poo
tags: class, public, private, protected, interface, extends
---

## Classe et objet

```php
class Invoice
{
    public function __construct(
        private string $client,
        private float $amount
    ) {}

    public function getAmount(): float
    {
        return $this->amount;
    }
}

$invoice = new Invoice('Alice', 120.0);
echo $invoice->getAmount();
```

Une **classe** décrit une structure et des comportements. Un **objet** est une instance concrète.

## Visibilité : `public`, `private`, `protected`

- `public` : accessible partout.
- `private` : accessible uniquement dans la classe qui la définit.
- `protected` : accessible aussi dans les classes enfants.

## Héritage et interfaces

```php
interface Notifiable
{
    public function notify(string $message): void;
}

class Client implements Notifiable
{
    public function notify(string $message): void
    {
        echo $message;
    }
}
```

Une interface définit un **contrat**. Une classe peut l'implémenter. `extends` sert à hériter d'une classe.

## Types et nullabilité

```php
function findInvoice(int $id): ?Invoice
{
    return null; // ?Invoice : Invoice ou null
}
```

## PHP vs JavaScript

PHP s'exécute généralement sur le serveur lors de la requête HTTP ; JavaScript s'exécute souvent dans le navigateur ou côté serveur via Node.js. Les deux ont une syntaxe proche par endroits, mais leurs environnements et leurs modèles d'exécution diffèrent.
