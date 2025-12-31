from clients.payment_client import PaymentClient
from django.conf import settings


def test_payment_client_mock_provider_returns_payload() -> None:
    client = PaymentClient(
        api_key=settings.PAYMENT_API_KEY,
        base_url="mock://payment-provider",
    )

    payload = client.create_payment(amount=100, currency="EUR")

    assert isinstance(payload, dict)
    assert payload["amount"] == 100
    assert payload["currency"] == "EUR"
    assert isinstance(payload["id"], str)
    assert payload["id"].startswith("prov_")

