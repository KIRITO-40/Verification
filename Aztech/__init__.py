import os
import time
from pyrogram import Client

# --------- version ----------

__version__="0.0.1"

# --------- Code -----------

API_ID = 10582318

BOT_TOKEN = ""

LOGS_CHANNEL = ""

# --------- Clients ----------


Aztech = Client("Aztech",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN, plugins=dict(root="{}/modules".format(__name__)))
