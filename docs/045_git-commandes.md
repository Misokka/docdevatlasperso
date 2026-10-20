---
title: Git : branches, merge, rebase, stash
group: Outils & Web
summary: Procédure pour récupérer main, résoudre les conflits et conserver un historique propre.
order: 45
slug: git-commandes
tags: git, github, gitlab, merge, rebase, stash, reset
---

## Mise à jour d'une branche feature

```bash
git status
git fetch origin
git switch feature/login
git rebase origin/main
```

Tu peux aussi mettre à jour ta branche locale `main` avec `pull`, revenir sur la feature, puis faire `git rebase main`. `fetch` évite de devoir changer de branche.

## Résoudre des conflits pendant un rebase

```bash
# Modifier les fichiers conflictuels puis :
git add fichier.php
git rebase --continue
# ou annuler :
git rebase --abort
```

Un rebase peut exiger plusieurs résolutions de conflit, commit après commit.

## Merge vs Rebase

| Outil | Effet |
|---|---|
| `git merge main` | Réunit les historiques, éventuellement via un commit de fusion. |
| `git rebase main` | Rejoue les commits de ta branche sur la nouvelle base ; réécrit les commits. |

Évite de rebaser sans concertation une branche partagée par plusieurs personnes, car cela peut perturber leur historique.

## Stash : sauvegarder provisoirement son travail

```bash
git stash push -u -m "wip login"
git stash list
git stash pop
```

Utile avant de changer de branche, mais pas nécessaire quand l'arbre de travail est déjà propre.

## Annuler des modifications

```bash
git restore fichier.php                  # annule modifications non indexées
git restore --staged fichier.php         # retire de l'index
git revert <commit_hash>                 # crée un commit inverse
```

`reset --hard` est potentiellement destructeur : ne l'utilise pas sans savoir ce que tu perds.

## Envoyer sur GitHub

```bash
git add .
git commit -m "feat: add invoice listing"
git push -u origin feature/login
```

[Git — Documentation officielle](https://git-scm.com/docs)
