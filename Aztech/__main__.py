# ------- imports --------

import asyncio
from Aztech import Verify
from pyrogram import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

loop = asyncio.get_event_loop()

# -------- Codes ----------

IMG = "https://telegra.ph//file/ba29f6d17057c64640c3c.jpg"

async def main():
    await Verify.start()
    await Verify.send_photo(-851491994, photo = IMG , caption = "Verification Bot Started",
                   reply_markup=InlineKeyboardMarkup([
                       [InlineKeyboardButton(text="Support", url=f"https://t.me/AztechSupport"),
                        InlineKeyboardButton(text="Network", url=f"https://t.me/AztechNetwork")]]),)
    print("Bot Started")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(main())



