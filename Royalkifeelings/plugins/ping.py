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
    await loda.edit_text(f"**🦋 𝒀𝒕 🌷 𝑴𝒖𝒔𝒊𝒄 🍀 𝑩𝒐𝒕 🥀 𝑰𝒔 🌺 𝑹𝒖𝒏𝒏𝒊𝒏𝒈 💐 𝑵𝒐𝒘 🍁 𝑷𝒚𝑻𝒈-𝑪𝒂𝒍𝒍 🍃** `{mp} ms`")

