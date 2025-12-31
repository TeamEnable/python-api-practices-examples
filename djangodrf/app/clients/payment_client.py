import requests
import uuid


class PaymentClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def create_payment(self, amount: int, currency: str) -> dict:
        # Offline-by-default stub
        if self.base_url.startswith("mock://"):
            return {
                "id": f"prov_{uuid.uuid4().hex[:8]}",
                "amount": amount,
                "currency": currency,
            }

        url = f"{self.base_url}/payments"
        try:
            payload = {"amount": amount, "currency": currency}
            r = requests.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=5,
            )
            r.raise_for_status()
            return r.json()
        except Exception as exc:
            raise RuntimeError(f"Payment provider unreachable: {exc}") from exc
