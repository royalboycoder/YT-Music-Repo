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
    await message.reply_text(
        f"""**𝐇𝐞𝐥𝐥𝐨 {BOT_NAME}✨ 𝐓𝐡𝐢𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 😎🤟
📡 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [𝐋σⱱəᴙ 𝐖σᴙɭɗ 𝐂ɦɑʈʈɪŋʛ 𝐇ʋB](https://t.me/royalkifeelings) 💞...**""",
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐃𝐃 𝐌𝐄 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "✯ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ✯", url=f"https://t.me/royalkifeelings_12"),

                    InlineKeyboardButton(
                        "✯ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✯", url=f"https://t.me/royalkifeelings"),
                ],
                [
                    InlineKeyboardButton(
                        text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/royal_boy_amit")
                ]
           ]
        ),
      disable_web_page_preview=True,
     )


@Royalboyamit.on_message(filters.command(["repo", "Royalboyamit"]))
async def help(client: Royalboyamit, message: Message):
    await message.reply_text(
        text=f"**⏤͟͞•꯭꯭𝗞𝗮𝗮𝗹 𝗠𝘂𝘀𝗶𝗰 👅 𝗜𝘀 𝗮𝗻 𝗽𝗼𝘄𝗲𝗿𝗳𝘂𝗹 🌏 𝗺𝘂𝘀𝗶𝗰 𝘀𝗼𝘂𝗿𝗰𝗲 🚬 𝗠𝗮𝗸𝗲 𝘂𝗿 𝗳𝗿𝗼𝗸 ⚜️ 𝗮𝗻𝗱 𝗴𝗶𝘃𝗲 𝗼𝗻𝗲 ⭐ 𝗳𝗼𝗿 𝗼𝘂𝗿 𝗵𝗮𝗿𝗱 𝘄𝗼𝗿𝗸 🥀**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭐ 𝗥𝗲𝗽𝗼 ✨", url=f"https://te.legra.ph/file/a615d91c0ef7caaa70fdd.mp4"
                    )
                ]
            ]
        ),
    )

@Royalboyamit.on_message(filters.command(["amit"]) & filters.group)
async def start(client: Royalboyamit, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>☣ **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✯ 𝐎𝐰𝐧𝐞𝐫-𝐱𝐃 ✯", url=f"https://t.me/royal_boy_amit"
                    ),
                    InlineKeyboardButton(
                        "✯ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✯", url=f"https://t.me/royalkifeelings"
                    ),
                ]
            ]
        ),
    )
