---
title: HTML sémantique, Flexbox et Grid
group: Outils & Web
summary: Comprendre la sémantique, formulaires, accessibilité, Flexbox et CSS Grid.
order: 46
slug: html-css
tags: html, css, flexbox, grid, button, semantic
---

## Pourquoi HTML sémantique ?

Les éléments comme `<header>`, `<nav>`, `<main>`, `<section>`, `<article>` et `<footer>` décrivent le rôle du contenu. Ils facilitent l'accessibilité et la compréhension de la structure.

**`<head>`** contient des métadonnées pour le navigateur : il ne représente pas le `<header>` visible de la page.

## Bouton vs div cliquable

```html
<button type="submit">Enregistrer</button>
```

Un vrai `button` gère nativement les interactions clavier et l'accessibilité d'un bouton. Une `div` cliquable ne fournit pas automatiquement ces comportements.

## Flexbox : disposition sur un axe

```css
.invoice-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}
```

Parfait pour placer un montant à gauche et un statut à droite.

## CSS Grid : lignes et colonnes

```css
.invoice-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
}

@media (max-width: 768px) {
    .invoice-grid { grid-template-columns: 1fr; }
}
```

Parfait pour afficher six cartes en trois colonnes et deux lignes.

## Accessibilité et formulaires

```html
<label for="email">Adresse email</label>
<input id="email" name="email" type="email" autocomplete="email" required>
```

Associer `label` et `input` via `for` / `id`, prévoir un focus visible et des messages d'erreur compréhensibles.
