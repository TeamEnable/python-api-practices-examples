import pytest
import respx
import httpx

from app.clients.payment_client import PaymentClient


@pytest.mark.asyncio
@respx.mock
async def test_payment_client_does_not_retry_on_4xx():
    base_url = "https://api.payment.example"
    respx.post(f"{base_url}/payments").mock(
        return_value=httpx.Response(400, text="bad request")
    )

    client = PaymentClient(api_key="x", base_url=base_url)
    with pytest.raises(RuntimeError):
        await client.create_payment(100, "EUR")
