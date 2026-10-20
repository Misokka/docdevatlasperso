---
title: Questions fréquentes et points de compréhension
group: Méthodes
summary: Définitions courtes pour distinguer les concepts courants du développement web.
order: 49
slug: questions-frequentes
tags: questions, concepts, java, vue, laravel, docker, git
---

## Laravel

**Pourquoi Laravel ?** Framework PHP qui accélère le développement web avec routing, MVC, Eloquent, validation, système d'authentification et outils Artisan.

**Service Provider ?** Point d'enregistrement/configuration des services dans le conteneur Laravel, notamment au démarrage. Ce n'est pas un Service métier.

**Middleware ?** Filtre des requêtes, par exemple pour exiger une connexion via `auth`.

**`$fillable` ?** Contrôle les attributs pouvant être assignés automatiquement avec `create()` / `update()` ; protège du mass assignment.

## Vue.js

**À quoi sert Vue ?** Framework frontend pour des interfaces réactives composées de composants `.vue`, avec `ref`, `v-if`, `v-for`, props et événements.

**`ref` vs `reactive` ?** `ref()` enveloppe une valeur et s'utilise avec `.value` en JavaScript ; `reactive()` rend réactif un objet directement.

**Computed vs watch ?** `computed` produit une valeur dérivée ; `watch` déclenche une réaction à un changement.

## Java & Spring Boot

**Java vs JavaScript ?** Java : statiquement typé, orienté objet, compilé en bytecode JVM. JavaScript : dynamiquement typé, utilisé dans le navigateur et avec Node.js.

**Pourquoi Spring Boot ?** Simplifie le démarrage et la structuration d'applications backend Java grâce à Spring, la configuration automatique, l'injection de dépendances et l'écosystème web/persistance.

**Organisation ?** Controller (HTTP) → Service (métier) → Repository (BDD).

## Docker

**Image vs conteneur ?** L'image est un modèle ; le conteneur en est une instance exécutée. Compose décrit plusieurs services, le Dockerfile sert à construire une image, le volume persiste des données.

## Git

**Merge vs rebase ?** `merge` rapproche deux historiques, éventuellement par commit de fusion. `rebase` rejoue des commits sur une nouvelle base et réécrit leur identité.

## SQL

**LEFT vs INNER JOIN ?** INNER conserve seulement les correspondances ; LEFT conserve toutes les lignes de la table de gauche.

**WHERE vs HAVING ?** WHERE filtre les lignes avant l'agrégation ; HAVING filtre les groupes après GROUP BY.

## HTML/CSS

**Flexbox vs Grid ?** Flexbox pour un axe ; Grid pour les lignes et colonnes.

**Pourquoi button et pas div ?** Sémantique, comportement clavier et accessibilité natifs.

## Méthode de résolution

Isoler le problème, lire les logs et la documentation, puis proposer une correction vérifiable. Si le blocage persiste ou présente un risque, partager le contexte et les tentatives déjà réalisées avant de solliciter un collègue.
