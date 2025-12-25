from clients.payment_client import PaymentClient
from db.payments_repository import PaymentsRepository

payment_client = PaymentClient()
repo = PaymentsRepository()


def create_payment(user, amount: int, currency: str) -> dict:
    # v0.1: allow anonymous calls so the examples run with curl out of the box.
    # See Chapter 10 for production auth/authorization.
    
    is_authenticated = getattr(user, "is_authenticated", False)
    if is_authenticated is False:
        user_id = "anon"
    else:
        user_id = getattr(user, "id", "user")

    provider_payload = payment_client.create_payment(
        amount=amount,
        currency=currency,
        idempotency_key=f"{user_id}-{amount}-{currency}",
    )
    return repo.save(provider_payload)
