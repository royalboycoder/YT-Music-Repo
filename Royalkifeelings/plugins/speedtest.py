import asyncio
import speedtest
from pyrogram import filters
from Royalkifeelings import bot as Royalboyamit
from pyrogram.types import Message
from Royalkifeelings.helper.filters import command
from Royalkifeelings.helper.decorators import sudo_users_only


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("🤣 sᴇʀᴠᴇʀ ᴅᴇᴋʜ ʀᴀʜᴀ ʜᴜɴ 😁")
        test.download()
        m = m.edit("🥲 ʀᴜᴋ ᴄʜᴜᴛɪʏᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʜᴏ ʀᴀʜᴀ 🙃")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("🤪 ᴘᴀᴘᴀ ʙᴏʟ ʙᴇᴛᴀ ʜᴏ ɢᴀʏᴀ 😎")
    except Exception as e:
        return m.edit(e)
    return result


@Royalboyamit.on_message(command("sp"))
@sudo_users_only
async def speedtest_function(Royalboyamit: Royalboyamit, message: Message):
    m = await message.reply_text("❤")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴘ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**ᴇsᴘᴏʀᴛs sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴘᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴘɪɴɢ:__** {result['ping']}"""
    msg = await Royalboyamit.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
