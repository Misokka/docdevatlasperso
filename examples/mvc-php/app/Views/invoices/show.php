<h1>Facture #<?= (int) $invoice['id'] ?></h1>

<dl class="card">
    <dt>Client</dt>
    <dd><?= htmlspecialchars($invoice['client'], ENT_QUOTES, 'UTF-8') ?></dd>

    <dt>Montant</dt>
    <dd><?= number_format((float) $invoice['amount'], 2, ',', ' ') ?> €</dd>

    <dt>Statut</dt>
    <dd><?= htmlspecialchars($invoice['status'], ENT_QUOTES, 'UTF-8') ?></dd>
</dl>
