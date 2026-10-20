---
title: Docker : images, conteneurs et Compose
group: Outils & Web
summary: Environnement local Laravel + PostgreSQL, Dockerfile, volumes et commandes.
order: 44
slug: docker-bases
tags: docker, compose, image, container, volume, dockerfile
---

## À quoi sert Docker ?

Docker permet de construire et exécuter des applications dans des conteneurs, avec des dépendances et une configuration prévisibles. C'est utile pour reproduire un environnement sur plusieurs machines.

- **Image** : modèle (ex. `postgres:17`).
- **Conteneur** : instance démarrée à partir d'une image.
- **Volume** : stockage persistant, utile pour une BDD.
- **Dockerfile** : instructions de construction de **ta propre image**.
- **Compose** : décrit plusieurs services dans un fichier YAML.

Un service Compose utilisant une image publique (`postgres:17`) **n'a pas besoin d'un Dockerfile**.

## docker-compose.yml minimal

```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: invoicing
      POSTGRES_USER: app
      POSTGRES_PASSWORD: local_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

C'est un exemple **local**, pas une configuration sécurisée de production. En prod, les mots de passe doivent être gérés de manière adaptée.

## Dockerfile simple (exemple PHP CLI)

```dockerfile
FROM php:8.3-cli
WORKDIR /app
COPY . /app
CMD ["php", "-v"]
```

Pour lancer réellement Laravel en conteneur, il faut aussi les extensions PHP, Composer, et généralement des services et commandes supplémentaires.

## Commandes essentielles

```bash
docker compose up -d
docker compose ps
docker compose logs -f db
docker compose exec db psql -U app -d invoicing
docker compose down
```

**Attention :** `docker compose down -v` supprime également les volumes associés du projet, avec leurs données.

## Où se trouve la BDD ?

Dans le conteneur PostgreSQL, ses données sont stockées dans le volume. Recréer le conteneur ne doit pas effacer la BDD tant que le volume est conservé.

[Docker — Compose](https://docs.docker.com/compose/)
