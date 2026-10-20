---
title: Java : fondamentaux du langage
group: Java & Symfony
summary: Langage orienté objet, typage statique, bytecode/JVM, classe, objet, interface.
order: 41
slug: java-fondamentaux
tags: java, jvm, class, object, interface, extends, implements
---

## Java en une phrase

Java est un **langage orienté objet, à typage statique**, compilé en bytecode généralement exécuté par une **JVM**. Il est utilisé notamment pour les applications d'entreprise et les API backend.

## Java vs JavaScript

- **Java** : types vérifiés à la compilation ; bytecode exécuté sur JVM ; Spring Boot pour le backend.
- **JavaScript** : langage à typage dynamique ; exécuté par navigateur ou Node.js ; Vue.js / Next.js dans le frontend.

## Une classe, un objet, un constructeur

```java
public class Invoice {
    private double amount;

    public Invoice(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }
}

Invoice invoice = new Invoice(120.0);
```

- **Classe** : modèle avec attributs et méthodes.
- **Objet** : instance concrète d'une classe.
- **Constructeur** : initialise une nouvelle instance.
- `private` : accessible uniquement depuis la classe.
- `public` : accessible depuis l'extérieur.
- `protected` : accessible dans les contextes d'héritage prévus par Java (nuance de package).

## Héritage et interface

```java
abstract class Animal {
    public abstract void crier();
}

interface Nageur {
    void nager();
}

class Chien extends Animal implements Nageur {
    @Override public void crier() { System.out.println("Wouf"); }
    @Override public void nager() { System.out.println("Je nage"); }
}
```

Une classe ne peut étendre qu'une seule classe Java, mais peut implémenter plusieurs interfaces. **Une interface n'est pas une instance d'une classe abstraite.**

## Différence entre `static` et instance

Une méthode `static` appartient à la classe ; une méthode d'instance nécessite un objet.

[Documentation officielle Java](https://docs.oracle.com/en/java/)
