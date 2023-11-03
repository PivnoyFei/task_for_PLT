from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorLatentCommandCursor

from settings import settings


class MongoManager:
    def __init__(self, db_url: str, db_name: str | None = settings.MONGO_NAME) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(db_url)[db_name]

    def aggregate(
        self,
        items: list,
        collection: str | None = "collection_name",
    ) -> AsyncIOMotorLatentCommandCursor:
        return self.client[collection].aggregate(items)
