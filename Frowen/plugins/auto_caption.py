# Lx 0980

from pyrogram import Client, filters, enums

CAPTION_DATA = {}

@Client.on_message(filters.command("set"))
async def set_caption(client, message):
    caption = await client.ask("Send me Your Channel Caption", parse_mode=enums.ParseMode.HTML)
    caption = caption.text
    if not caption:
        return await message.reply_text("Error!\n Try Again 🌐")
    channel_id = str(-1001547532818)
    CAPTION_DATA[channel_id] = {
        "caption": caption
    }
    caption = CAPTION_DATA.get(channel_id)
    caption = caption.get("caption")
    if not caption:
        await message.reply_text("Caption not setted!")
        return 
    await message.reply_text(f"Caption Successfully Set! ✅\n\n {caption}")
    

@Client.on_message(filters.channel & (filters.video | filters.document))
async def auto_caption(bot, message):
    channel_id = str(message.chat.id)
    caption = CAPTION_DATA.get(channel_id)
    try:
        m_caption = caption.get("caption")
    except AttributeError:
        m_caption = "@DefaultCaption"  # @DefaultCaption
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Here is your caption: {m_caption}"
    )


    
