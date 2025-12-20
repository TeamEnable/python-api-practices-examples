import pytest
from app.retries.retry_helper import retry


@pytest.mark.asyncio
async def test_retry_succeeds_after_failures():
    attempts = {"n": 0}

    async def flaky():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise RuntimeError("transient")
        return "ok"

    result = await retry(flaky, attempts=5, backoff_seconds=0.0)
    assert result == "ok"
    assert attempts["n"] == 3
