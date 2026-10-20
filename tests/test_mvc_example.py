import shutil
import socket
import subprocess
import tempfile
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/mvc-php"


def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class NativeMvcHttpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if shutil.which("php") is None:
            raise unittest.SkipTest("PHP n'est pas disponible")

        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.project = Path(cls.temporary_directory.name) / "mvc-php"
        shutil.copytree(EXAMPLE, cls.project)
        subprocess.run(
            ["php", "database/init.php"],
            cwd=cls.project,
            check=True,
            capture_output=True,
            text=True,
        )

        cls.port = free_port()
        cls.server = subprocess.Popen(
            ["php", "-S", f"127.0.0.1:{cls.port}", "router.php"],
            cwd=cls.project,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(40):
            try:
                urllib.request.urlopen(
                    f"http://127.0.0.1:{cls.port}/invoices", timeout=0.2
                ).close()
                break
            except Exception:
                time.sleep(0.05)
        else:
            raise RuntimeError("Le serveur PHP n'a pas démarré")

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "server"):
            cls.server.terminate()
            cls.server.wait(timeout=5)
        if hasattr(cls, "temporary_directory"):
            cls.temporary_directory.cleanup()

    def request(self, path):
        try:
            with urllib.request.urlopen(
                f"http://127.0.0.1:{self.port}{path}", timeout=2
            ) as response:
                return response.status, response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            try:
                return error.code, error.read().decode("utf-8")
            finally:
                error.close()

    def test_invoice_list_is_rendered(self):
        status, body = self.request("/invoices")
        self.assertEqual(200, status)
        self.assertIn("Factures", body)
        self.assertIn("Atelier Dupont", body)

    def test_existing_invoice_detail_is_rendered(self):
        status, body = self.request("/invoices/1")
        self.assertEqual(200, status)
        self.assertIn("Facture #1", body)
        self.assertIn("Atelier Dupont", body)

    def test_missing_or_invalid_invoice_returns_404(self):
        for path in ("/invoices/999", "/invoices/invalide"):
            with self.subTest(path=path):
                status, body = self.request(path)
                self.assertEqual(404, status)
                self.assertIn("introuvable", body.lower())


if __name__ == "__main__":
    unittest.main()
