from .frowen import User, Bot
from pyrogram import idle


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
print("Bot Stopped!"
