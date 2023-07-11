# (c) Lx 0989
# Year : 2023

from pyrogram import Client, filters 
from Frowen.frowen import Bot, User

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply_text("Bot Started!")

@User.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply_text("UserBot Started!")

    
  
