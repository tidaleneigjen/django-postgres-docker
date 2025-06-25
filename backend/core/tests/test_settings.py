from django.conf import settings
from django.test import TestCase, override_settings


class SettingsTests(TestCase):

    @override_settings(DEBUG=True)
    def test_debug_mode_true(self):
        self.assertTrue(settings.DEBUG, "DEBUG should be True in development")

    def test_database_configuration(self):
        db = settings.DATABASES["default"]
        self.assertEqual(db["ENGINE"], "django.db.backends.postgresql")
        for key in ["NAME", "USER", "PASSWORD", "HOST", "PORT"]:
            self.assertIn(key, db, f"{key} missing from DATABASES config")
