def can_create_payment(user) -> bool:
    # Keep it explicit and boring; expand later
    return getattr(user, "is_authenticated", False)
