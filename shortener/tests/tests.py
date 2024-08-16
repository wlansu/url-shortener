import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_create_url(api_client: Client) -> None:
    url = reverse("api-1.0.0:create_url")
    data = {"original_url": "https://example.com"}
    response = api_client.post(
        url, data, format="json", content_type="application/json"
    )
    assert response.status_code == 200
    assert "short_code" in response.json()


@pytest.mark.django_db
def test_create_expired_url(api_client: Client) -> None:
    url = reverse("api-1.0.0:create_url")
    data = {
        "original_url": "https://example.com",
        "expires_at": "2024-04-23T10:20:30.400+02:30",
    }
    response = api_client.post(
        url, data, format="json", content_type="application/json"
    )
    assert response.status_code == 404


@pytest.mark.parametrize(
    "invalid_url",
    [
        "invalid-url",
        "example.com",
        "httpl://example.com",
        "httpss://example.com",
    ],
)
@pytest.mark.django_db
def test_create_url_invalid_data(api_client: Client, invalid_url: str) -> None:
    url = reverse("api-1.0.0:create_url")
    data = {"original_url": invalid_url}
    response = api_client.post(
        url, data, format="json", content_type="application/json"
    )
    assert response.status_code == 422


@pytest.mark.django_db
def test_visit_url_invalid_short_code(api_client: Client) -> None:
    url = reverse("api-1.0.0:visit_url", args=["invalid"])
    response = api_client.get(url)
    assert response.status_code == 404
