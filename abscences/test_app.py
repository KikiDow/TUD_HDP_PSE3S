from django.apps import apps
from django.test import TestCase
from .apps import AbscencesConfig

class TestAbscencesConfig(TestCase):

    def test_app(self):
        self.assertEqual("abscences", AbscencesConfig.name)
        self.assertEqual("abscences", apps.get_app_config("abscences").name)