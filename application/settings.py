from pydantic import MongoDsn
from pydantic_settings import BaseSettings


class MongoSettings(BaseSettings):
    MONGO_HOST: str | None = "localhost"
    MONGO_PORT: int | None = 27017
    MONGO_NAME: str | None = "mobgo"

    @property
    def MONGO_DATABASE_URI(self) -> MongoDsn:
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_NAME}"


class Settings(MongoSettings):
    TOKEN: str | None

    class Config:
        env_file = "infra-rlt/.env"


settings: Settings = Settings()

TYPES = ("hour", "day", "week", "month")
