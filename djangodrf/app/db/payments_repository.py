from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class StoredPayment:
    id: str
    amount: int
    currency: str
    provider_id: str
    created_at: datetime


class PaymentsRepository:
    def save(self, provider_payload: dict) -> dict:
        return StoredPayment(
            id="p_local_001",
            amount=int(provider_payload.get("amount", 0)),
            currency=str(provider_payload.get("currency", "EUR")),
            provider_id=str(provider_payload.get("id", "p_provider_unknown")),
            created_at=datetime.utcnow(),
        ).__dict__
