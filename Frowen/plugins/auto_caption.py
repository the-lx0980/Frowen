# Lx 0980

from pyrogram import Client, filters

CAPTION_DATA = {}

@Client.on_message(filters.channel & filters.command("set"))
async def set_caption(bot, message):
    caption = await bot.message.chat.ask("Send me Your Channel Caption", parse_mode=enums.ParseMode.HTML)
    if not caption:
        return await message.reply_text("Error!\n Try Again 🌐")
    channel_id = str(message.chat.id)
    CAPTION_DATA[channel_id] = {
        "caption": caption
    }
    caption = CAPTION_DATA.get(channel_id)
    caption = caption.get("caption")
    if not caption:
        await message.reply_text("Caption not setted!")
        return 
    await message.reply_text(f"Caption Successfully Set! ✅\n\n {caption}")
    


