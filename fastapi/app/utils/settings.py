from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Keep names explicit and boring
    payment_api_key: str = "dev-key"
    payment_base_url: str = "mock://payment-provider"
    request_timeout_seconds: float = 5.0

    environment: str = "dev"


settings = Settings()
