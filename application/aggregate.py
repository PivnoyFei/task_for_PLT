from datetime import datetime, time

from dateutil.relativedelta import relativedelta

from db import MongoManager
from schemas import AggregateOut
from settings import settings

client = MongoManager(settings.MONGO_DATABASE_URI)


class Aggregate:
    def __init__(self) -> None:
        self.data: dict = {
            "hour": ("%Y-%m-%dT%H:00:00", relativedelta(hours=1)),
            "day": ("%Y-%m-%dT00:00:00", relativedelta(days=1)),
            "week": ("%Y-%U-1T00:00:00", relativedelta(weeks=1)),
            "month": ("%Y-%m-01T00:00:00", relativedelta(months=1)),
        }

    async def aggregate_result(
        self,
        dt_from: datetime,
        dt_upto: datetime,
        group_type: str,
    ) -> AggregateOut:
        group = {"$dateToString": {"format": self.data[group_type][0], "date": "$dt"}}
        bounds_end = (
            dt_upto + self.data[group_type][1]
            if dt_upto.time() == time(minute=0, second=0)
            else dt_upto
        )
        items = [
            {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
            {
                "$densify": {
                    "field": "dt",
                    "range": {
                        "step": 1,
                        "unit": group_type,
                        "bounds": [dt_from, bounds_end],
                    },
                }
            },
            {"$group": {"_id": group, "dataset": {"$sum": "$value"}}},
            {"$sort": {"_id": 1}},
        ]

        query = await client.aggregate(items).to_list(None)
        return AggregateOut(
            dataset=[entry["dataset"] for entry in query],
            labels=[entry["_id"] for entry in query],
        )
