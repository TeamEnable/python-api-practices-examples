from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    payment_api_key: str = "dev-key"
    payment_base_url: str = "mock://payment-provider"

    environment: str = "dev"

    model_config = ConfigDict(
        env_prefix="",
        case_sensitive=False,
        extra="ignore",  # ignore unexpected env vars
    )


settings = Settings()
