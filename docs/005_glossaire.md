---
title: Mini-glossaire technique
group: Commencer
summary: Les définitions courtes à retrouver pendant une discussion technique.
order: 5
slug: glossaire
tags: lexique, definitions, termes
---

## Termes de backend

| Terme | Sens concret |
|---|---|
| MVC | Séparer données (Model), traitement HTTP (Controller) et rendu (View). |
| ORM | Faire des requêtes à la BDD via des objets / méthodes du langage. |
| Middleware | Intercepter une requête HTTP avant ou après le contrôleur. |
| Dependency Injection | Fournir à une classe les objets dont elle dépend. |
| Service Container | Résoudre et construire les dépendances. |
| Service Provider | Enregistrer/configurer des services dans Laravel. |
| Event | Signaler un fait métier, ex. facture payée. |
| Listener | Réagir à un événement. |
| Job / Queue | Représenter / exécuter une tâche, parfois en arrière-plan. |
| Policy | Décider si un utilisateur a le droit d'agir sur une ressource. |
| N+1 | Plusieurs requêtes SQL inutiles déclenchées dans une boucle. |

## Termes frontend

| Terme | Sens concret |
|---|---|
| Reactive state | Donnée dont le changement entraîne la mise à jour de l'interface. |
| `ref()` | État réactif Vue ; `.value` dans le JavaScript. |
| `computed()` | Valeur dérivée et mise en cache selon ses dépendances réactives. |
| `watch()` | Réaction/effet secondaire à un changement de donnée. |
| Props | Données transmises d'un parent à un enfant. |
| Emit | Événement envoyé d'un enfant à un parent dans Vue. |
| Promise | Représente l'issue future d'une opération asynchrone. |
| SSR | Génération du HTML côté serveur. |
| CSR | Rendu/interaction côté client. |

## Termes bases de données et outils

| Terme | Sens concret |
|---|---|
| JOIN | Rapprocher des lignes de plusieurs tables selon une relation. |
| Index | Structure accélérant certaines recherches en BDD. |
| Transaction | Groupe d'opérations réussi intégralement ou annulé. |
| Docker image | Modèle immuable pour créer des conteneurs. |
| Docker container | Instance en exécution d'une image. |
| Volume | Stockage persistant hors cycle de vie du conteneur. |
| Merge | Fusion d'historiques Git. |
| Rebase | Rejouer ses commits sur une nouvelle base, en réécrivant leur identité. |
