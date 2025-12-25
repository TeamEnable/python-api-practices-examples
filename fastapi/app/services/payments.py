from app.clients.payment_client import PaymentClient
from app.db.payments_repository import PaymentsRepository

from app.config import settings


client = PaymentClient(
        api_key=settings.payment_api_key,
        base_url=settings.payment_base_url,
        timeout_seconds=settings.request_timeout_seconds,
    )
repo = PaymentsRepository()


async def create_payment(*, amount: int, currency: str) -> dict:
    payment = await client.create_payment(
        amount=amount,
        currency=currency,
        idempotency_key="demo-payment-001",
    )
    return repo.save(payment)
