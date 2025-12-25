import asyncio
import httpx
import respx

from app.config import settings
from app.services.payments import create_payment


async def main() -> None:
    # Mock the external provider call so the demo runs offline.
    with respx.mock:
        respx.post(f"{settings.payment_base_url.rstrip('/')}/payments").mock(
            return_value=httpx.Response(
                200,
                json={"id": "prov_123", "amount": 100, "currency": "EUR"},
            )
        )

        stored = await create_payment(amount=100, currency="EUR")

    print(stored)


if __name__ == "__main__":
    asyncio.run(main())