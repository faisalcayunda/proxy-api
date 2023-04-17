from pydantic import BaseSettings
from functools import lru_cache


class Configuration(BaseSettings):
    THE_API_BASE_URL: str

    class Config:
        env_file = ".env"


@lru_cache
def get_config() -> Configuration:
    return Configuration()
