import pytest

from django.test import Client


@pytest.fixture
def api_client():
    return Client()
