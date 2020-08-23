import pytest

from agile.tests.factory.agile_factory import AgileFactory
from agile.filters import AgileFilter
from agile.models import Agile


@pytest.mark.django_db
class TestAgileFilters:
    def test_value_filter(self):
        AgileFactory.create_batch(4, type="principle")
        AgileFactory.create_batch(3, type="value")
        filtered = AgileFilter(data={"type": "value"}, queryset=Agile.objects.all())
        assert filtered.qs.count() == 3

    def test_principle_filter(self):
        AgileFactory.create_batch(4, type="principle")
        AgileFactory.create_batch(3, type="value")
        filtered = AgileFilter(data={"type": "principle"}, queryset=Agile.objects.all())
        assert filtered.qs.count() == 4

    def test_name_filter(self):
        AgileFactory.create(name="test 1", type="value")
        AgileFactory.create(name="test 2", type="principle")
        AgileFactory.create(name="test 3", type="principle")
        filtered = AgileFilter(
            data={"name__icontains": " 3"}, queryset=Agile.objects.all()
        )
        assert filtered.qs.count() == 1
