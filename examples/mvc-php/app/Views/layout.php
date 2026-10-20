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
