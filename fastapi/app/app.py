import respx
import httpx


async def main() -> None:
    # Minimal demo wiring
    from app.utils.settings import settings
    from app.clients.payment_client import PaymentClient
    from app.db.payments_repository import PaymentsRepository

    client = PaymentClient(
        api_key=settings.payment_api_key,
        base_url=settings.payment_base_url,
        timeout_seconds=settings.request_timeout_seconds,
    )
    repo = PaymentsRepository()

    # Mock the external provider call so the demo runs offline.
    with respx.mock:
        respx.post(f"{settings.payment_base_url.rstrip('/')}/payments").mock(
            return_value=httpx.Response(
                200,
                json={"id": "prov_123", "amount": 100, "currency": "EUR"},
            )
        )
        payment = await client.create_payment(
            amount=100,
            currency="EUR",
            idempotency_key="demo-payment-001",
        )

    stored = repo.save(payment)
    print(stored)
