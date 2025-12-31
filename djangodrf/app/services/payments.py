from clients.payment_client import PaymentClient
from db.payments_repository import PaymentsRepository

from django.conf import settings


client = PaymentClient(
    api_key=settings.PAYMENT_API_KEY,
    base_url=settings.PAYMENT_BASE_URL,
)
repo = PaymentsRepository()


def create_payment(amount: int, currency: str) -> dict:
    payment = client.create_payment(
        amount=amount,
        currency=currency,
    )
    return repo.save(payment)
