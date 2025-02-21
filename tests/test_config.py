from functools import lru_cache
from dotenv import load_dotenv
from src.shared.infra.config_settings import ConfigSettings


@lru_cache
def get_test_settings() -> ConfigSettings:
    load_dotenv(".env.test", override=True)
    return ConfigSettings()
