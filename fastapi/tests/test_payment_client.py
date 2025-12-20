import pytest
import respx
import httpx

from app.clients.payment_client import PaymentClient, PaymentError


@pytest.mark.asyncio
@respx.mock
async def test_payment_client_sends_idempotency_key_and_retries_on_5xx():
    base_url = "https://api.payment.example"
    route = respx.post(f"{base_url}/payments")

    # First call fails (5xx), second succeeds
    route.side_effect = [
        httpx.Response(500, text="oops"),
        httpx.Response(200, json={"id": "prov_123", "amount": 100, "currency": "EUR"}),
    ]

    client = PaymentClient(api_key="x", base_url=base_url, timeout_seconds=1.0)
    result = await client.create_payment(100, "EUR", idempotency_key="abc-123")

    assert result["id"] == "prov_123"
    assert route.called
    # Ensure header presence
    assert route.calls[0].request.headers["Idempotency-Key"] == "abc-123"


@pytest.mark.asyncio
@respx.mock
async def test_payment_client_does_not_retry_on_4xx():
    base_url = "https://api.payment.example"
    respx.post(f"{base_url}/payments").mock(
        return_value=httpx.Response(400, text="bad request")
    )

    client = PaymentClient(api_key="x", base_url=base_url)
    with pytest.raises(PaymentError):
        await client.create_payment(100, "EUR", idempotency_key="abc-123")
