# Shows: boundary, timeouts, error mapping, retries, idempotency key.

import httpx
from app.retries.retry_helper import retry
from app.config import settings


class PaymentError(RuntimeError):
    pass


class PaymentClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout_seconds: float | None = None,
    ) -> None:
        self.api_key = api_key or settings.payment_api_key
        self.base_url = (base_url or settings.payment_base_url).rstrip("/")
        self.timeout_seconds = timeout_seconds or settings.request_timeout_seconds
        self.client = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

    async def create_payment(
        self, amount: int, currency: str, idempotency_key: str
    ) -> dict:
        if amount <= 0:
            raise ValueError("amount must be > 0")

        async def _call() -> dict:
            # if we mock the provider
            if self.base_url.startswith("mock://"):
                return {"id": "prov_mock_123", "amount": amount, "currency": currency}

            r = await self.client.post(
                f"{self.base_url}/payments",
                json={"amount": amount, "currency": currency},
                headers={"Idempotency-Key": idempotency_key},
                timeout=self.timeout_seconds,
            )

            # Map provider errors into a domain error (keeps services/endpoints clean)
            if r.status_code >= 500:
                raise PaymentError(f"provider 5xx: {r.status_code}")
            if r.status_code >= 400:
                raise PaymentError(f"provider 4xx: {r.status_code} {r.text}")

            return r.json()

        def _should_retry(exc: Exception) -> bool:
            # Retry transient issues only
            if isinstance(exc, httpx.RequestError):
                return True
            if isinstance(exc, PaymentError) and "5xx" in str(exc):
                return True
            return False

        try:
            return await retry(
                _call, attempts=3, backoff_seconds=0.3, should_retry=_should_retry
            )
        except httpx.RequestError as exc:
            raise PaymentError(f"network issue: {exc}") from exc
