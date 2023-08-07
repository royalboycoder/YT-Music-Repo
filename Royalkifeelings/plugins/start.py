from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Royalkifeelings.callmusic.config import BOT_NAME, BOT_USERNAME
from Royalkifeelings import bot as Royalboyamit
from Royalkifeelings.callmusic.config import GROUP_SUPPORT, UPDATES_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("ᴡᴇᴇᴋs", 60 * 60 * 24 * 7),
    ("ᴅᴀʏ", 60**2 * 24),
    ("ʜᴏᴜʀ", 60**2),
    ("ᴍɪɴ", 60),
    ("sᴇᴄ", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Royalboyamit.on_message(filters.command(["start", "help"]) & ~filters.group)
async def start(_, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/f26f1b65bd824a87909a0.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🥀 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐀𝐦 𝐀𝐧 📀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝
𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐕𝐂 𝐏𝐥𝐚𝐲𝐞𝐫 » 𝐅𝐨𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦
𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐀𝐧𝐝 𝐆𝐫𝐨𝐮𝐩𝐬 ✨ ...

💐 𝐅𝐞𝐞𝐥 𝐅𝐫𝐞𝐞 𝐓𝐨: 🕊️ 𝐀𝐝𝐝 𝐌𝐞 𝐢𝐧 𝐘𝐨𝐮𝐫
𝐆𝐫𝐨𝐮𝐩 🌺 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 🌿 𝐒𝐮𝐩𝐞𝐫 𝐇𝐢𝐠𝐡
𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 🥀 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐂ʀᴇᴀᴛᴏʀ : [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/royal_boy_amit)
┣★ 𝐔ᴘᴅᴀᴛᴇ𝐒 : [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/royalkifeelings_12)
┣★ 𝐒ᴜᴘᴘᴏʀᴛ : [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/royalkifeelings)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇ𝐒ᴛɪᴏɴ𝐒 ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [𝐋ᴇɢᴇɴᴅ 𝐎ᴡɴᴇʀ](https://t.me/royal_boy_amit) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✯ 𝐉ᴏɪɴ 𝐌ʏ 𝐂ʜᴀᴛ 𝐆ʀᴏᴜᴘ ✯", url=f"https://t.me/royalkifeelings")
                ]
                
           ]
        ),
    )
