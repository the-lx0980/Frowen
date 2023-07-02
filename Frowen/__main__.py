# (c) Lx 0980
# Yeat : 2023

from Frowen import API_ID, API_HASH, BOT_TOKEN

from pyrogram import Client

frowen = Client(
    "frowen",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={
        'root': 'Frowen.plugins'
    }
)

frowen.run()



frowen.run()
