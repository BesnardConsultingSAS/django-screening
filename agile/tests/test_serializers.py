import pytest

from typing import Dict

from agile.models import Agile
from agile.serializers import AgileSerializer


@pytest.mark.django_db
class TestAgileSerializer:
    @pytest.fixture
    def agile_fixture(self, db) -> Agile:
        return Agile.objects.create(name="name", description="description")

    @pytest.fixture
    def default_value(self, agile_fixture) -> Dict[str, Dict[str, str]]:
        return {
            "page": agile_fixture,
            "data": {
                "name": "Responding to change over following a plan.",
                "description": "Circumstances change and sometimes customers demand extra.",
            },
        }

    def test_valid(self, default_value):
        serializer = AgileSerializer(data=default_value["data"])
        assert serializer.is_valid()

    def test_save(self, default_value):
        serializer = AgileSerializer(data=default_value["data"])
        serializer.is_valid()
        instance = serializer.save()
        assert instance.name == default_value["data"]["name"]
        assert instance.description == default_value["data"]["description"]
