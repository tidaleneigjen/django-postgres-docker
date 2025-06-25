import os
from django.conf import settings
from django.test import TestCase


class EnvironmentVariableTests(TestCase):

    def test_db_name_exists(self):
        self.assertTrue(settings.DATABASES['default']['NAME'])

