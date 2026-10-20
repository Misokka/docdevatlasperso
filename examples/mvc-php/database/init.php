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
