import pytest
from rest_framework.test import APIClient
from django.test import override_settings


@pytest.mark.django_db
@override_settings(PAYMENT_BASE_URL="mock://payment-provider")
def test_payments_view_post_works_offline():
    client = APIClient()

    resp = client.post(
        "/api/payments/",
        {"amount": 100, "currency": "EUR"},
        format="json",
    )

    assert resp.status_code == 200
    data = resp.json()
    assert data["amount"] == 100
    assert data["currency"] == "EUR"
    assert data["provider_id"].startswith("prov_")
