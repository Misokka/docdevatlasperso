---
title: Créer un MVC en PHP natif
group: PHP
summary: Construire une mini-application de factures avec routeur, contrôleur, modèle PDO, vues et SQLite.
order: 10
slug: php/mvc-php-natif
tags: MVC, PHP natif, routeur, PDO, controller, model, view, front controller, SQLite
---

## Objectif et principe MVC

Cette mini-application affiche une liste de factures et le détail de chacune, sans Laravel, Symfony ni dépendance externe. Elle permet de suivre tout le trajet d’une requête :

```text
Navigateur → Routeur → Contrôleur → Modèle → SQLite → Vue HTML
```

Chaque élément possède une responsabilité précise :

- **Model** : accède aux données et porte la logique associée. Ici, `Invoice` exécute les requêtes PDO.
- **View** : produit la présentation HTML à partir des données reçues.
- **Controller** : reçoit la demande, appelle le modèle et transmet les données à la vue.
- **Router** : associe une méthode HTTP et une URL à la bonne action du contrôleur.
- **Front Controller** : point d’entrée unique de l’application. Toutes les requêtes dynamiques passent par `public/index.php`.

Dans Laravel, ces rôles existent aussi, mais le framework fournit déjà le routeur, le conteneur de services, les réponses HTTP, Blade, Eloquent, la gestion des erreurs et de nombreux mécanismes de sécurité. Ici, cette infrastructure minimale est construite manuellement pour comprendre ce que le framework orchestre.

## Architecture du projet

```text
mvc-php/
├── app/
│   ├── Controllers/
│   │   └── InvoiceController.php
│   ├── Models/
│   │   └── Invoice.php
│   └── Views/
│       ├── layout.php
│       └── invoices/
│           ├── index.php
│           ├── show.php
│           └── not-found.php
├── config/
│   └── database.php
├── database/
│   ├── database.sqlite       # généré par init.php
│   └── init.php
├── public/
│   └── index.php
├── router.php
└── README.md
```

Le dossier `public/` est la racine web. Les classes, la configuration et la base ne sont donc pas servies directement par le serveur HTTP.

## 1. Front Controller et routes — `public/index.php`

Ce fichier charge les deux classes, construit leurs dépendances puis distribue uniquement les requêtes `GET`. L’identifiant capturé dans l’URL doit être un entier positif. Une route inconnue, un identifiant invalide ou une facture absente produit une réponse HTTP 404.

```php
<?php

declare(strict_types=1);

use App\Controllers\InvoiceController;
use App\Models\Invoice;

require dirname(__DIR__) . '/app/Models/Invoice.php';
require dirname(__DIR__) . '/app/Controllers/InvoiceController.php';

try {
    $database = require dirname(__DIR__) . '/config/database.php';
    $model = new Invoice($database);
    $controller = new InvoiceController(
        $model,
        dirname(__DIR__) . '/app/Views'
    );

    $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
    $path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/';

    if ($method !== 'GET') {
        http_response_code(405);
        header('Allow: GET');
        echo 'Méthode non autorisée';
    } elseif ($path === '/') {
        header('Location: /invoices', true, 302);
    } elseif ($path === '/invoices') {
        $controller->index();
    } elseif (preg_match('#^/invoices/([^/]+)$#', $path, $matches) === 1) {
        $id = filter_var(
            $matches[1],
            FILTER_VALIDATE_INT,
            ['options' => ['min_range' => 1]]
        );

        $id === false ? $controller->notFound() : $controller->show($id);
    } else {
        $controller->notFound();
    }
} catch (Throwable $error) {
    error_log($error->getMessage());
    http_response_code(500);
    echo 'Une erreur interne est survenue.';
}
```

Le détail technique est envoyé dans les logs avec `error_log()`, tandis que le navigateur ne reçoit qu’un message générique. Cela évite d’exposer un chemin local, une requête SQL ou une trace d’exécution.

## 2. Connexion PDO SQLite — `config/database.php`

Le chemin de la base est calculé à partir du projet : aucun secret ni mot de passe n’est nécessaire pour SQLite. PDO est configuré pour lever des exceptions et retourner des tableaux associatifs.

```php
<?php

declare(strict_types=1);

$databasePath = dirname(__DIR__) . '/database/database.sqlite';

return new PDO('sqlite:' . $databasePath, null, null, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
]);
```

## 3. Modèle — `app/Models/Invoice.php`

Le modèle ignore tout du HTML et des routes. `find()` utilise une requête préparée pour l’identifiant reçu depuis l’URL.

```php
<?php

declare(strict_types=1);

namespace App\Models;

use PDO;

final class Invoice
{
    public function __construct(private PDO $database)
    {
    }

    public function all(): array
    {
        $statement = $this->database->query(
            'SELECT id, client, amount, status FROM invoices ORDER BY id DESC'
        );

        return $statement->fetchAll();
    }

    public function find(int $id): ?array
    {
        $statement = $this->database->prepare(
            'SELECT id, client, amount, status FROM invoices WHERE id = :id'
        );
        $statement->execute(['id' => $id]);
        $invoice = $statement->fetch();

        return $invoice === false ? null : $invoice;
    }
}
```

## 4. Contrôleur — `app/Controllers/InvoiceController.php`

`index()` récupère toutes les factures. `show()` demande une facture au modèle et délègue l’affichage à une vue. `render()` capture la vue spécifique, puis l’insère dans le layout commun.

```php
<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Models\Invoice;

final class InvoiceController
{
    public function __construct(
        private Invoice $invoices,
        private string $viewsPath,
    ) {
    }

    public function index(): void
    {
        $this->render('invoices/index', [
            'title' => 'Factures',
            'invoices' => $this->invoices->all(),
        ]);
    }

    public function show(int $id): void
    {
        $invoice = $this->invoices->find($id);

        if ($invoice === null) {
            $this->notFound();
            return;
        }

        $this->render('invoices/show', [
            'title' => 'Facture #' . $invoice['id'],
            'invoice' => $invoice,
        ]);
    }

    public function notFound(): void
    {
        http_response_code(404);
        $this->render('invoices/not-found', [
            'title' => 'Facture introuvable',
        ]);
    }

    private function render(string $view, array $data = []): void
    {
        extract($data, EXTR_SKIP);

        ob_start();
        require $this->viewsPath . '/' . $view . '.php';
        $content = (string) ob_get_clean();

        require $this->viewsPath . '/layout.php';
    }
}
```

`http_response_code(404)` est essentiel : afficher seulement « introuvable » avec un statut 200 tromperait le navigateur, les moteurs de recherche et les clients HTTP.

## 5. Layout commun — `app/Views/layout.php`

Le titre est échappé avec `htmlspecialchars()`. La règle `color-scheme` rend les contrôles et couleurs natives compatibles avec les préférences claires et sombres du système.

```html+php
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= htmlspecialchars($title, ENT_QUOTES, 'UTF-8') ?></title>
    <style>
        :root { color-scheme: light dark; font-family: system-ui, sans-serif; }
        body { max-width: 900px; margin: 0 auto; padding: 2rem 1rem; }
        a { color: #6d5dfc; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: .75rem; border-bottom: 1px solid #8885; text-align: left; }
        .card { padding: 1rem; border: 1px solid #8885; border-radius: .75rem; }
    </style>
</head>
<body>
    <nav><a href="/invoices">Toutes les factures</a></nav>
    <main>
        <?= $content ?>
    </main>
</body>
</html>
```

## 6. Liste — `app/Views/invoices/index.php`

Les chaînes provenant de la base sont échappées. L’identifiant est converti en entier et le montant est formaté avant affichage.

```html+php
<h1>Factures</h1>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Client</th>
            <th>Montant</th>
            <th>Statut</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($invoices as $invoice): ?>
            <tr>
                <td><?= (int) $invoice['id'] ?></td>
                <td><?= htmlspecialchars($invoice['client'], ENT_QUOTES, 'UTF-8') ?></td>
                <td><?= number_format((float) $invoice['amount'], 2, ',', ' ') ?> €</td>
                <td><?= htmlspecialchars($invoice['status'], ENT_QUOTES, 'UTF-8') ?></td>
                <td><a href="/invoices/<?= (int) $invoice['id'] ?>">Voir</a></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>
```

## 7. Détail — `app/Views/invoices/show.php`

```html+php
<h1>Facture #<?= (int) $invoice['id'] ?></h1>

<dl class="card">
    <dt>Client</dt>
    <dd><?= htmlspecialchars($invoice['client'], ENT_QUOTES, 'UTF-8') ?></dd>

    <dt>Montant</dt>
    <dd><?= number_format((float) $invoice['amount'], 2, ',', ' ') ?> €</dd>

    <dt>Statut</dt>
    <dd><?= htmlspecialchars($invoice['status'], ENT_QUOTES, 'UTF-8') ?></dd>
</dl>
```

### Vue 404 — `app/Views/invoices/not-found.php`

```html
<h1>Facture introuvable</h1>
<p>La facture demandée n’existe pas.</p>
```

## 8. Initialisation SQLite — `database/init.php`

Le script crée la table, remet les données de démonstration dans un état connu et insère trois factures avec une requête préparée. La transaction évite une initialisation partielle.

```php
<?php

declare(strict_types=1);

$database = require dirname(__DIR__) . '/config/database.php';

$database->exec(
    <<<'SQL'
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT NOT NULL,
        amount NUMERIC NOT NULL CHECK (amount >= 0),
        status TEXT NOT NULL CHECK (status IN ('pending', 'paid'))
    )
    SQL
);

$database->beginTransaction();

try {
    $database->exec('DELETE FROM invoices');
    $database->exec("DELETE FROM sqlite_sequence WHERE name = 'invoices'");

    $insert = $database->prepare(
        'INSERT INTO invoices (client, amount, status)
         VALUES (:client, :amount, :status)'
    );

    $fixtures = [
        ['client' => 'Atelier Dupont', 'amount' => 1250.00, 'status' => 'paid'],
        ['client' => 'Studio Horizon', 'amount' => 780.50, 'status' => 'pending'],
        ['client' => 'Maison Rivière', 'amount' => 2100.00, 'status' => 'paid'],
    ];

    foreach ($fixtures as $invoice) {
        $insert->execute($invoice);
    }

    $database->commit();
    echo "Base SQLite initialisée avec 3 factures.\n";
} catch (Throwable $error) {
    $database->rollBack();
    fwrite(STDERR, "Impossible d'initialiser la base SQLite.\n");
    exit(1);
}
```

## 9. Routeur du serveur intégré — `router.php`

Le serveur PHP intégré appelle ce script pour chaque requête. Un véritable fichier public peut être servi directement ; toutes les autres URL sont envoyées au Front Controller.

```php
<?php

declare(strict_types=1);

$path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/';
$publicFile = __DIR__ . '/public' . $path;

if ($path !== '/' && is_file($publicFile)) {
    return false;
}

require __DIR__ . '/public/index.php';
```

## Lancer le projet

Le projet complet se trouve dans `examples/mvc-php/`. PHP doit disposer des extensions `PDO` et `pdo_sqlite`, généralement activées par défaut.

```bash
cd examples/mvc-php
php database/init.php
php -S localhost:8000 router.php
```

Visite ensuite :

- `http://localhost:8000/invoices` pour le tableau des trois factures ;
- `http://localhost:8000/invoices/1` pour le détail de la première facture ;
- `http://localhost:8000/invoices/999` pour vérifier la réponse HTTP 404.

Pour vérifier le statut sans navigateur :

```bash
curl -i http://localhost:8000/invoices/999
```

La première ligne doit contenir `HTTP/1.1 404 Not Found`.

## Cheminement d’une requête

Pour `GET /invoices/1` :

1. `router.php` transmet l’URL à `public/index.php`.
2. Le Front Controller valide `1` et appelle `InvoiceController::show(1)`.
3. Le contrôleur appelle `Invoice::find(1)`.
4. Le modèle exécute la requête préparée avec PDO sur SQLite.
5. Le contrôleur transmet la facture à `invoices/show.php`.
6. La vue spécifique est insérée dans `layout.php`, puis le HTML est envoyé au navigateur.

## Bonnes pratiques présentes

- PDO lève des exceptions et prépare chaque requête qui contient une valeur externe.
- L’identifiant de route doit être un entier strictement positif.
- Une ressource absente retourne réellement le statut HTTP 404.
- Les données affichées sont échappées avec `htmlspecialchars()`.
- Les erreurs internes sont journalisées sans exposer leur détail au navigateur.
- Le modèle ne génère pas de HTML, la vue n’exécute pas de SQL et le contrôleur coordonne les deux.
- Aucun mot de passe ni secret n’est codé en dur.

## Correspondances avec Laravel

| PHP natif | Laravel |
|---|---|
| Routeur manuel | `routes/web.php` |
| Contrôleur PHP | `InvoiceController` |
| Modèle PDO | Modèle Eloquent |
| `require` d'une vue | `return view()` |
| Requête préparée PDO | Query Builder / Eloquent |
| Configuration de connexion manuelle | Configuration de base de données Laravel |

Lorsque l’application grandit, un framework apporte des composants éprouvés pour la validation, les middlewares, l’injection de dépendances, les migrations, les tests, la sécurité et la gestion des erreurs. Le MVC natif reste très utile pour comprendre ces mécanismes et pour de petits outils, mais reconstruire toute cette infrastructure augmente vite le coût de maintenance.
