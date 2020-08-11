from pathlib import Path

import pytest

from django.core.management import call_command


@pytest.fixture(scope="class")
def django_db_setup(django_db_setup, django_db_blocker):
    from django.conf import settings

    with django_db_blocker.unblock():
        call_command("loaddata", Path(settings.BASE_DIR) / "agile/fixtures/fixtures.json")
