import requests
from django.conf import settings

from retries.retry_helper import retry_sync


class PaymentError(RuntimeError):
    pass


class PaymentClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout_seconds: float | None = None,
    ) -> None:
        self.api_key = api_key or settings.PAYMENT_API_KEY
        self.base_url = (base_url or settings.PAYMENT_BASE_URL).rstrip("/")
        self.timeout_seconds = timeout_seconds or settings.PAYMENT_TIMEOUT_SECONDS

    def create_payment(self, amount: int, currency: str, idempotency_key: str) -> dict:
        if amount <= 0:
            raise ValueError("amount must be > 0")
            # As a result, we will get a `500` here (for v0.1, that’s acceptable). 
            # v0.2 improvement: handle that via input validation / serializer.

        # Offline mode: keep the mocking at the client boundary.
        if self.base_url.startswith("mock://"):
            return {"id": "prov_mock_123", "amount": amount, "currency": currency}

        def _call() -> dict:
            r = requests.post(
                f"{self.base_url}/api/payments",
                json={"amount": amount, "currency": currency},
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Idempotency-Key": idempotency_key,
                },
                timeout=self.timeout_seconds,
            )

            if r.status_code >= 500:
                raise PaymentError(f"provider 5xx: {r.status_code}")
            if r.status_code >= 400:
                raise PaymentError(f"provider 4xx: {r.status_code} {r.text}")

            return r.json()

        def _should_retry(exc: Exception) -> bool:
            # retry transient network issues + provider 5xx mapped errors
            if isinstance(exc, requests.RequestException):
                return True
            return isinstance(exc, PaymentError) and "5xx" in str(exc)

        try:
            return retry_sync(
                _call, attempts=3, backoff_seconds=0.3, should_retry=_should_retry
            )
        except requests.RequestException as exc:
            raise PaymentError(f"network issue: {exc}") from exc
