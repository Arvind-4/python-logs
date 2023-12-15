from decouple import config
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    elasticSearchHost: str = config(
        "ELASTIC_SEARCH_HOST", default="localhost", cast=str
    )
    elasticSearchPort: int = config("ELASTIC_SEARCH_PORT", default=9200, cast=int)


@lru_cache()
def get_settings():
    return Settings()
