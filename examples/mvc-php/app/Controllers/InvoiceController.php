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
