import asyncio
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")


async def retry(
    func: Callable[[], Awaitable[T]],
    *,
    attempts: int = 3,
    backoff_seconds: float = 0.5,
    should_retry: Callable[[Exception], bool] | None = None,
) -> T:
    last_exc: Exception | None = None

    for attempt in range(attempts):
        try:
            return await func()
        except Exception as exc:
            last_exc = exc
            if should_retry is not None and not should_retry(exc):
                raise
            if attempt == attempts - 1:
                break
            await asyncio.sleep(backoff_seconds * (attempt + 1))

    assert last_exc is not None
    raise last_exc
