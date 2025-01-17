from typing import Union
import json
import yt_dlp
import re
import asyncio
import os
import glob
import random
import logging
from pyrogram.enums import ChatMemberStatus
from Royalkifeelings import BOT_USERNAME
from Royalkifeelings.helper.inline import stream_markup, audio_markup
from Royalkifeelings.handler.chatname import CHAT_TITLE
from Royalkifeelings.helper.filters import command, other_filters
from Royalkifeelings.helper.queues import QUEUE, add_to_queue
from Royalkifeelings import call_py, Royalboyamit as user
from Royalkifeelings import bot as Royalboyamit
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython.__future__ import VideosSearch
from Royalkifeelings.handler.thumbnail import play_thumb, queue_thumb

IMAGE_THUMBNAIL = "https://te.legra.ph/file/ead56db6ded46455bcb2f.jpg"


def cookie_txt_file():
    folder_path = f"{os.getcwd()}/cookies"
    filename = f"{os.getcwd()}/cookies/logs.csv"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    with open(filename, 'a') as file:
        file.write(f'Choosen File : {cookie_txt_file}\n')
    return f"""cookies/{str(cookie_txt_file).split("/")[-1]}"""


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "--cookies", cookie_txt_file(),
        "-g",
        "-f",
        "best[height<=?2160][width<=?1440]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Royalboyamit.on_message(command(["vplay", f"vplay@{BOT_USERNAME}"]) & other_filters)
async def vplay(c: Royalboyamit, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text("ʏᴏᴜ'ʀᴇ ᴀɴ __ᴀɴᴏɴʏᴍᴏᴜs__ ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != ChatMemberStatus.ADMINISTRATOR:
        await m.reply_text(
            f"**💡 ᴛᴏ ᴜsᴇ ᴍᴇ, ɪ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ **ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ** ᴡɪᴛʜ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ **ᴘᴇʀᴍɪssɪᴏɴs**:\n\n» ❌ __ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__\n» ❌ __ɪɴᴠɪᴛᴇ ᴜsᴇʀs__\n» ❌ __ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__\n\nᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʏᴘᴇ /ʀᴇʟᴏᴀᴅ**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
        "**💡 ᴛᴏ ᴜsᴇ ᴍᴇ, ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴘᴇʀᴍɪssɪᴏɴ ʙᴇʟᴏᴡ:**"
        + "\n\n» ❌ __ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__\n\nᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʀʏ ᴀɢᴀɪɴ.")
        return
    if not a.can_delete_messages:
        await m.reply_text(
        "**💡 ᴛᴏ ᴜsᴇ ᴍᴇ, ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴘᴇʀᴍɪssɪᴏɴ ʙᴇʟᴏᴡ:**"
        + "\n\n» ❌ __ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__\n\nᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʀʏ ᴀɢᴀɪɴ.")
        return
    if not a.can_invite_users:
        await m.reply_text(
        "**💡 ᴛᴏ ᴜsᴇ ᴍᴇ, ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴘᴇʀᴍɪssɪᴏɴ ʙᴇʟᴏᴡ:**"
        + "\n\n» ❌ __ᴀᴅᴅ ᴜsᴇʀs__\n\nᴏɴᴄᴇ ᴅᴏɴᴇ, ᴛʀʏ ᴀɢᴀɪɴ.")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot) 
        if b.status == "kicked":
            await c.unban_chat_member(chat_id, ubot)
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
            await user.join_chat(invitelink)
    except UserNotParticipant:
        try:
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
            await user.join_chat(invitelink)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await m.reply_text(
                f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`"
            )

    if replied:
        if replied.video or replied.document:
            loser = await replied.reply("🔍")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await loser.edit(
                        "» __ᴏɴʟʏ 𝟽𝟸𝟶, 𝟺𝟾𝟶, 𝟹𝟼𝟶 ᴀʟʟᴏᴡᴇᴅ__ \n💡 **ɴᴏᴡ sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ɪɴ 𝟽𝟸𝟶ᴘ**"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                elif replied.document:
                    songname = replied.document.file_name[:70]
            except BaseException:
                songname = "Video"

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = audio_markup(user_id)
                await m.reply_photo(
                    photo=playimg,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ơɯ ❤️ Ʌɗɗəɗ Ʋɪԃҽᴏ Søŋʛ 💫\n\n**ƦɛqʉʂƮɜɖ Ɓɤ :{m.from_user.mention()}**")
            else:
                if Q == 720:
                    esport = HighQualityVideo()
                elif Q == 480:
                    esport = MediumQualityVideo()
                elif Q == 360:
                    esport = LowQualityVideo()
                await loser.edit("🫀")
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(
                        dl,
                        HighQualityAudio(),
                        esport,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = audio_markup(user_id)
                await m.reply_photo(
                    photo=playimg,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ø̛ɯ 😄 ℘ɭʌɤɪɴʛ 📀 Ʌʈ🤟\n\nƦɛqʉʂƮɜɖ Ɓɤ :{requester}",
                )
        else:
            if len(m.command) < 2:
                await m.reply_photo(
                    photo=f"https://graph.org/file/b54b89d9d4f7efe4fbd75.jpg",
                    caption=f"**𝐔𝐬ᴀɢᴇ: /play 🤖 𝐆𝐢𝐯𝐞 🙃 𝐒𝐨𝐦𝐞 💿 𝐐𝐮𝐞𝐫𝐲 😍 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲 🥀 𝐕𝐢𝐝𝐞𝐨 🌸 𝐒𝐨𝐧𝐠 🍁 𝐍𝐚𝐦𝐞...**", 
             ) 
            else:
                loser = await c.send_message(chat_id, f"**Şєʌɾƈɦɪɲʛ ຖơɯ...**"
                      )
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                Q = 360
                esport = HighQualityVideo()
                if search == 0:
                    await loser.edit("❌ **🌸𝗦𝗼𝗻𝗴 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱 ✌ 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗣𝗿𝗼𝗯𝗹𝗲𝗺**")
                else:
                    songname = search[0]
                    title = search[0]
                    url = search[1]
                    duration = search[2]
                    thumbnail = search[3]
                    userid = m.from_user.id
                    gcname = m.chat.title
                    videoid = search[4]
                    playimg = await play_thumb(videoid)
                    queueimg = await queue_thumb(videoid)
                    dlurl = f"https://www.youtubepp.com/watch?v={videoid}"
                    shub, ytlink = await ytdl(url)
                    if shub == 0:
                        await loser.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Video", Q
                            )
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            buttons = stream_markup(user_id, videoid)
                            await m.reply_photo(
                                photo=playimg,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ø̛ɯ 😄 ℘ɭʌɤɪɴʛ 📀 Ʌʈ🤟\n\nƦɛqʉʂƮɜɖ Ɓɤ :{requester}",
                            )
                        else:
                            try:
                                await loser.edit(
                            f"**Ƥɾơƈєƨƨɪɲʛ ຖơɯ...**"
                        )
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioVideoPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                        esport,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                                await loser.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                buttons = stream_markup(user_id, dlurl)
                                await m.reply_photo(
                                    photo=playimg,
                                    reply_markup=InlineKeyboardMarkup(buttons),
                                    caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ø̛ɯ 😄 ℘ɭʌɤɪɴʛ 🤟\n\nƦɛqʉʂƮɜɖ Ɓɤ :{requester}",
                                )
                            except Exception as ep:
                                await loser.delete()
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply_photo(
                     photo=f"https://graph.org/file/b54b89d9d4f7efe4fbd75.jpg",
                     caption=f"**𝐔𝐬ᴀɢᴇ: /play 🤖 𝐆𝐢𝐯𝐞 🙃 𝐒𝐨𝐦𝐞 💿 𝐐𝐮𝐞𝐫𝐲 😍 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲 🥀 𝐕𝐢𝐝𝐞𝐨 🌸 𝐒𝐨𝐧𝐠 🍁 𝐍𝐚𝐦𝐞...**", 
         ) 
        else:
            loser = await c.send_message(chat_id, f"**Şєʌɾƈɦɪɲʛ ຖơɯ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            esport = HighQualityVideo()
            if search == 0:
                await loser.edit("❌ **🌸𝗦𝗼𝗻𝗴 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱 ✌ 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗣𝗿𝗼𝗯𝗹𝗲𝗺.**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                videoid = search[4]
                playimg = await play_thumb(videoid)
                queueimg = await queue_thumb(videoid)
                dlurl = f"https://www.youtubepp.com/watch?v={videoid}"               
                shub, ytlink = await ytdl(url)
                if shub == 0:
                    await loser.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await loser.delete()
                        requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        buttons = stream_markup(user_id, dlurl)
                        await m.reply_photo(
                            photo=playimg,
                            reply_markup=InlineKeyboardMarkup(buttons),
                            caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ø̛ɯ ❤️ Ʌɗɗəɗ Søŋʛ 💫🤟\n** :{requester}",
                        )
                    else:
                        try:
                            await loser.edit(
                            f"**Ƥɾơƈєƨƨɪɲʛ ຖơɯ...**"
                        )
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                    esport,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            buttons = stream_markup(user_id, dlurl)
                            await m.reply_photo(
                                photo=playimg,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"**✰ ϔƭ Ɱϋƨɪƈ Ρɭʌϔɪɲʛ ₦ø̛ɯ 😄 ℘ɭʌɤɪɴʛ 📀 Ʌʈ 🤟 \n\nƦɛqʉʂƮɜɖ Ɓɤ :{requester}",
                            )
                        except Exception as ep:
                            await loser.delete()
                            await m.reply_text(f"🚫 error: `{ep}`")

