from django.test import TestCase

from agile.models import Agile


class AgileMethodTests(TestCase):
    def test_get_values(self):
        """Tests expected Agile type values from fixtures."""
        self.assertTrue(Agile.objects.get_values().count(), 4)

    def test_get_principles(self):
        """Tests expected Agile type principles from fixtures."""
        self.assertTrue(Agile.objects.get_principles().count(), 12)
