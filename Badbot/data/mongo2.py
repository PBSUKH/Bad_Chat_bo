from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from Badbot import LOGGER_ID

TEMP_MONGODB = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"


if config.MONGO_DB is None:
    LOGGER(__name__).warning(
        "𝐍o 𝐌ONGO 𝐃B 𝐔RL 𝐅ound.. 𝐘our 𝐁ot 𝐖ill 𝐖ork 𝐎n 𝐕𝐈𝐏 𝐌𝐔𝐒𝐈𝐂 𝐃atabase"
    )
    temp_client = Client(
        "Badbot",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB)
    _mongo_sync_ = MongoClient(config.MONGO_DB)
    mongodb = _mongo_async_.Badbot
    pymongodb = _mongo_sync_.Badbot
