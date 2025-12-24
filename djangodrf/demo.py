import os
import sys
from pathlib import Path

# Ensure the Django project package is on sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "app"))

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from services.payments import create_payment


class DemoUser:
    """
    Minimal stand-in for a Django user.
    Keeps the demo simple and offline.
    """

    is_authenticated = False
    id = None


def main() -> None:
    result = create_payment(
        user=DemoUser(),
        amount=100,
        currency="EUR",
    )
    print(result)


if __name__ == "__main__":
    main()
