from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Python FastAPIA Example"
    sqlalchemy_database_url: str

    class Config:
        env_file = ".env"
