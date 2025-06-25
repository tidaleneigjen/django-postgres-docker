from django.test import TestCase
from django.urls import resolve


class UrlTests(TestCase):
    def test_admin_url_resolves(self):
        resolver = resolve('/admin/')
        self.assertEqual(resolver.app_name, 'admin')

    def test_root_status_code(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 301, 302, 404])

