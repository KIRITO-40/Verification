from pyrogram.types import Message, filters
from Aztech import Verify as pbot

PIC = "https://telegra.ph//file/ba29f6d17057c64640c3c.jpg"

@pbot.on_message(filters.command("start"))
async def start(_, msg:Message):
    await msg.reply_photo(PIC, caption="Hello")
     
