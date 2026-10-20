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
