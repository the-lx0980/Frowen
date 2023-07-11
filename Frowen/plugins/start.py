# (c) Lx 0989
# Year : 2023

from pyrogram import Client, filters 

@Client.on_message(filters.private & filters.command("start"))
async def start(bot, message):
  await message.reply_text("Bot Started!")

    
  
