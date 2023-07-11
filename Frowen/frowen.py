# (c) Lx 0980
# Yeat : 2023

from Frowen import API_ID, API_HASH, USER_SESSION, BOT_TOKEN

from pyrogram import Client, idle

Bot = Client(
    "frowen",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={
        'root': 'Frowen.plugins'
    }
)

User = Client(
    "User-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=USER_SESSION,
    plugins={
        'root': 'Frowen.plugins'
    }
)


