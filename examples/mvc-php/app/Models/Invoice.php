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
