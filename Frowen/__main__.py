# (c) Lx 0980
# Yeat : 2023

from Frowen import API_ID, API_HASH, BOT_TOKEN

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
    bot_token=BOT_TOKEN,
    plugins={
        'root': 'Frowen.plugins'
    }
)

User.start()
print("Userbot Started!")
# Start Bot Client
Bot.start()
print("Bot Started!")
# Loop Clients till Disconnects
idle()
# Stop User Client
User.stop()
print("\n")
print("Userbot Stopped!")
# Stop Bot Client
Bot.stop()
print("Bot Stopped!")
