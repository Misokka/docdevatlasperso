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
