import requests
from datetime import datetime
from pyrogram import filters, Client
from Royalkifeelings import bot as Royalboyamit
# ping checker

@Royalboyamit.on_message(filters.command(["ping"], ["/", ".", "!"]))
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("**» 𝐊ᴀᴀʟ 𝐌ᴜsɪᴄ**")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"**🤖 Poɴɢ\n»** `{mp} ms`")

