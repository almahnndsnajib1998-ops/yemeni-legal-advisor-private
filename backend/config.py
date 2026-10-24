import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "المستشار القانوني اليمني الذكي"
    app_env: str = "development"
    database_url: str = ""
    secret_key: str = ""
    ai_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
