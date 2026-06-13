import importlib
import os
import tempfile
import unittest
from pathlib import Path

import app


class LaunchBehaviourTests(unittest.TestCase):
    def setUp(self):
        self.old_env = dict(os.environ)
        os.environ["EXPORT_TOKEN"] = "unit-test-export-token"
        os.environ["ALLOWED_ORIGINS"] = (
            "https://signup.harborlantern.example,"
            "https://organizers.harborlantern.example"
        )
        importlib.reload(app)
        self.tmp = tempfile.TemporaryDirectory()
        self.data_file = Path(self.tmp.name) / "registrations.jsonl"
        self.upload_dir = Path(self.tmp.name) / "uploads"

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.old_env)
        self.tmp.cleanup()
        importlib.reload(app)

    def test_registration_and_authorized_export(self):
        app.create_registration(
            {
                "name": "Avery Kim",
                "email": "Avery.Kim@Example.COM",
                "party_size": 3,
                "accessibility_note": "aisle seating requested",
            },
            data_file=self.data_file,
        )

        with self.assertRaises(PermissionError):
            app.export_registrations({}, data_file=self.data_file)
        with self.assertRaises(PermissionError):
            app.export_registrations({"X-Export-Token": "wrong"}, data_file=self.data_file)

        csv_text = app.export_registrations(
            {"X-Export-Token": "unit-test-export-token"},
            data_file=self.data_file,
        )
        self.assertIn("Avery Kim", csv_text)
        self.assertIn("avery.kim@example.com", csv_text)
        self.assertIn("party_size", csv_text.splitlines()[0])

    def test_missing_export_token_does_not_use_preview_code(self):
        os.environ.pop("EXPORT_TOKEN", None)
        importlib.reload(app)
        app.create_registration(
            {"name": "Nina Park", "email": "nina@example.com", "party_size": 1},
            data_file=self.data_file,
        )
        with self.assertRaises(PermissionError):
            app.export_registrations(
                {"X-Export-Token": "preview-export-2468"},
                data_file=self.data_file,
            )

    def test_attachment_names_are_constrained(self):
        with self.assertRaises(ValueError):
            app.save_attachment("../outside.py", b"x", upload_dir=self.upload_dir)
        with self.assertRaises(ValueError):
            app.save_attachment("receipt.html", b"<script>x</script>", upload_dir=self.upload_dir)
        with self.assertRaises(ValueError):
            app.save_attachment("large.pdf", b"x" * (2_000_001), upload_dir=self.upload_dir)

        stored = app.save_attachment("receipt.PDF", b"%PDF-1.4", upload_dir=self.upload_dir)
        stored_path = Path(stored)
        self.assertTrue(stored_path.exists())
        self.assertEqual(stored_path.parent.resolve(), self.upload_dir.resolve())
        self.assertNotEqual(stored_path.name, "receipt.PDF")

    def test_cors_uses_configured_origin_list(self):
        allowed = app.cors_headers(
            "https://signup.harborlantern.example",
            allow_credentials=True,
        )
        self.assertEqual(
            allowed.get("Access-Control-Allow-Origin"),
            "https://signup.harborlantern.example",
        )
        self.assertEqual(allowed.get("Access-Control-Allow-Credentials"), "true")

        denied = app.cors_headers("https://example.invalid", allow_credentials=True)
        self.assertNotEqual(denied.get("Access-Control-Allow-Origin"), "*")
        self.assertNotEqual(
            denied.get("Access-Control-Allow-Origin"),
            "https://example.invalid",
        )


if __name__ == "__main__":
    unittest.main()
