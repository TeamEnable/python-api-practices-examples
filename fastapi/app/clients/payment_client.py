import httpx
import uuid


class PaymentClient:
    def __init__(self, api_key: str, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(headers={"Authorization": f"Bearer {api_key}"})

    async def create_payment(self, amount: int, currency: str) -> dict:
        # Offline-by-default stub
        if self.base_url.startswith("mock://"):
            return {
                "id": f"prov_{uuid.uuid4().hex[:8]}",
                "amount": amount,
                "currency": currency,
            }

        try:
            payload = {"amount": amount, "currency": currency}
            r = await self.client.post(
                f"{self.base_url}/payments",
                json=payload,
                timeout=5,
            )
        except httpx.RequestError as exc:
            raise RuntimeError(f"Payment provider unreachable: {exc}") from exc

        if r.status_code >= 400:
            raise RuntimeError(f"Payment provider error: {r.text}")

        return r.json()
