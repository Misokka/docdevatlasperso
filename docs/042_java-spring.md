---
title: Spring Boot : rôle et architecture
group: Java & Symfony
summary: Controller, Service, Repository et injection de dépendances dans une API Java.
order: 42
slug: java-spring
tags: spring boot, controller, service, repository, restcontroller, jpa
---

## Pourquoi Spring Boot ?

Spring Boot simplifie le développement d'applications Java en fournissant notamment configuration automatique, serveur HTTP embarqué et intégration de l'écosystème Spring. On peut le comparer à Laravel dans le sens où il apporte une infrastructure de framework au langage.

## Le flux à retenir

```text
Navigateur / API Client
       ↓ GET /invoices
InvoiceController    → reçoit HTTP
       ↓
InvoiceService       → logique métier
       ↓
InvoiceRepository    → accès aux données
       ↓
Base de données
```

Le résultat remonte dans l'autre sens. Le Service **n'appelle pas le Controller** pour lui signaler la requête : c'est le Controller qui reçoit la requête.

## Controller : route HTTP

```java
@RestController
@RequestMapping("/invoices")
public class InvoiceController {
    private final InvoiceService service;

    public InvoiceController(InvoiceService service) {
        this.service = service;
    }

    @GetMapping
    public List<Invoice> index() {
        return service.getAllInvoices();
    }
}
```

## Service : logique métier

```java
@Service
public class InvoiceService {
    private final InvoiceRepository repository;

    public InvoiceService(InvoiceRepository repository) {
        this.repository = repository;
    }

    public List<Invoice> getAllInvoices() {
        return repository.findAll();
    }
}
```

## Repository : accès BDD

```java
public interface InvoiceRepository extends JpaRepository<Invoice, Long> {
}
```

`JpaRepository` vient de Spring Data JPA ; **JPA est une spécification**, pas en soi l'ORM. Hibernate en est une implémentation courante.

## Injection de dépendances

Le constructeur reçoit `InvoiceService` plutôt que de faire `new InvoiceService()` : Spring fournit cet objet via son conteneur. Cela réduit le couplage et facilite les tests.

## À expliquer à un ancien développeur

« Spring Boot nous aide à structurer une API Java. Les Controllers reçoivent les requêtes, les Services portent la logique métier et les Repositories interrogent la base. On utilise des classes et des interfaces, avec un typage statique. »

[Spring Boot Documentation](https://docs.spring.io/spring-boot/index.html)
