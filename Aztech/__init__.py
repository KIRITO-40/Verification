import os
import logging
import time
from pyrogram import Client

# --------- version ----------

__version__="0.0.1"

# --------- Logger --------

FORMAT = "[Aztech] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("Aztech_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

# --------- Vars -----------

API_ID = 10582318

API_HASH = "ae5cb28621683b35873d9f71e7279471"

BOT_TOKEN = "5325337803:AAEWNKsYHmsDaU4yi5riipewOM2VC837-i8"

LOGS_CHANNEL = "-851491994"

# --------- Clients ----------


Verify = Client("Aztech",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN, plugins=dict(root="{}/modules".format(__name__)))
