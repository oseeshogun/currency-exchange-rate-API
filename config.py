from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    currency_api_net_api_key: str = ""
    currency_api_com_api_key: str = ""

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
