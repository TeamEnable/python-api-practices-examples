import pytest

from app.clients.payment_client import PaymentClient
from app.config import settings


@pytest.mark.asyncio
async def test_payment_client_mock_provider_returns_payload() -> None:
    # Ensure offline default (or override explicitly)
    client = PaymentClient(
        api_key=settings.payment_api_key,
        base_url="mock://payment-provider",
    )

    payload = await client.create_payment(amount=100, currency="EUR")

    assert isinstance(payload, dict)
    assert payload["amount"] == 100
    assert payload["currency"] == "EUR"
    assert isinstance(payload["id"], str)
    assert payload["id"].startswith("prov_")

