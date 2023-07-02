# (c) Lx 0989
# Year : 2023

from pyrogram import Client, filters

@Client.on_message()
async def start(bot, message):
  await bot.send_messages(chat_id=chatid)

    
  
