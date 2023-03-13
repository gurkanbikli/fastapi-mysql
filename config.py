import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL", "mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_DB: int = os.getenv("REDIS_DB", 0)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", None)


configuration = Settings()
