# DevAtlas — Documentation personnelle de développement

Une bibliothèque personnelle de connaissances **en français**, dans l'esprit visuel des documentations de frameworks. Elle centralise les concepts, exemples de code, architectures et bonnes pratiques à retrouver pendant les projets et l'apprentissage.

## Ce que tu obtiens

- **51 fiches** organisées par catégories : PHP, Laravel, SQL/PostgreSQL, Vue 3, JavaScript, TypeScript, Next.js, Java/Spring Boot, Symfony, Docker, Git, HTML/CSS, API REST et méthodes de travail.
- **Recherche intégrale** par titre, contenu et sections, avec résultats contextuels et raccourcis `Cmd/Ctrl + K`, `↑`, `↓`, `Entrée`, `Échap`.
- **Navigation latérale**, sommaire cliquable par page, ancres profondes, fil d'Ariane et rubriques dépliables.
- **Code avec coloration syntaxique** et bouton de copie.
- **Thème clair/sombre**, mise en page mobile, pages favorites enregistrées localement, liens partageables.
- **Aucune dépendance frontend ni base de données** : HTML/CSS/JavaScript précompilés, déployables gratuitement sur un service statique.

> ⚠️ Ce guide est un aide-mémoire personnel, pas une source officielle. Si une version ou un comportement change, vérifie la documentation officielle liée en bas des fiches. N'y mets pas de secrets ou données client si le dépôt est public.

## Démarrer en local

À la racine du projet :

```bash
python3 -m http.server 8000 --directory public
```

Ouvre ensuite **http://localhost:8000**.

Tu peux également ouvrir `public/index.html` comme fichier local, mais un serveur local est conseillé pour éviter les restrictions éventuelles des navigateurs et pour retrouver les mêmes URLs qu'en production.

## Publier sur GitHub

1. Décompresse l'archive.
2. Ouvre un terminal dans le dossier `devatlas-documentation`.
3. Crée un dépôt **vide** sur GitHub (évite d'y ajouter un README automatique : celui-ci existe déjà).
4. Exécute, en remplaçant `<TON_URL_DU_REPO>` :

```bash
git init
git add .
git commit -m "feat: launch personal developer documentation"
git branch -M main
git remote add origin <TON_URL_DU_REPO>
git push -u origin main
```

Si ton environnement Git n'est pas configuré, Git pourra te demander de définir ton identité ou d'utiliser une authentification GitHub.

## Déployer sur Vercel

1. Va sur **https://vercel.com/new** et connecte ton compte GitHub.
2. Importe le dépôt créé.
3. Vérifie les paramètres (le fichier `vercel.json` les définit aussi) :
   - **Framework Preset : `Other`**.
   - **Build Command : vide** (aucune compilation à réaliser sur Vercel).
   - **Output Directory : `public`**.
   - **Root Directory : racine du dépôt**.
4. Clique sur **Deploy**.
5. Vérifie la recherche (Cmd/Ctrl + K) et une fiche, par exemple `?doc=laravel-auth-login`.

Les déploiements suivants peuvent se faire automatiquement après un `git push` sur la branche de production.

## Modifier les fiches

Les sources sont des fichiers Markdown dans `docs/` et les données servies au navigateur sont **déjà générées** dans `public/assets/docs-data.js`.

Pour modifier une fiche et régénérer l'index de recherche :

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
```

Puis commit et push **les fichiers `.md` et le nouveau `public/assets/docs-data.js`**. Vercel publie simplement le contenu du dossier `public` ; il n'exécute pas le générateur Python.

Les fichiers Markdown commencent par un en-tête :

```text
---
title: Mon sujet
group: Laravel
summary: Résumé court.
order: 42
slug: ma-fiche
tags: php, code, laravel
---

## Une section
Mon texte et mon code.
```

Pour ajouter une fiche, crée un Markdown dans `docs/`, puis régénère. Les catégories disponibles sont définies dans `scripts/build.py`.

### Organisation du dépôt

```text
devatlas-documentation/
├── public/
│   ├── index.html
│   └── assets/
│       ├── app.js
│       ├── styles.css
│       ├── docs-data.js
│       ├── pygments.css
│       └── favicon.svg
├── docs/                  # 51 pages Markdown lisibles
├── scripts/
│   └── build.py           # génération du HTML et index de recherche
├── requirements.txt
├── vercel.json
└── README.md
```

## Remarques de sécurité et de confidentialité

- Le contenu publié est **public** si le dépôt et l'URL le sont. N'ajoute jamais de `.env`, de tokens, de vrais mots de passe ou de données clients.
- Vérifie les informations sensibles avant chaque publication et adapte les exemples à la version des outils utilisée par ton projet.
- La recherche fonctionne sur les contenus précompilés, sans API distante ni compte.
- Les favoris et le choix de thème sont enregistrés **dans le navigateur uniquement**.

## Sources de référence

[Laravel 13](https://laravel.com/docs/13.x) · [Vue 3](https://vuejs.org/guide/introduction.html) · [Next.js](https://nextjs.org/docs) · [TypeScript](https://www.typescriptlang.org/docs/) · [Spring Boot](https://docs.spring.io/spring-boot/index.html) · [PostgreSQL](https://www.postgresql.org/docs/) · [Vercel](https://vercel.com/docs)
