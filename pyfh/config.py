from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = "127.0.0.1"
    db_port: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()
