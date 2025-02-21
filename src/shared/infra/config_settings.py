from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigSettings(BaseSettings):
    db_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return ConfigSettings()
