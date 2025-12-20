import time
from typing import Callable
from starlette.requests import Request
from starlette.responses import Response


async def request_logging_middleware(request: Request, call_next: Callable) -> Response:
    start = time.monotonic()
    response = await call_next(request)
    duration = time.monotonic() - start

    # Keep logs safe: no tokens, no bodies by default
    print(
        {
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration": round(duration, 4),
        }
    )
    return response
