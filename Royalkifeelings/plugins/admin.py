from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Royalkifeelings.helper.decorators import authorized_users_only
from Royalkifeelings.helper.filters import command, other_filters
from Royalkifeelings.helper.queues import QUEUE, clear_queue
from Royalkifeelings.handler.thumbnail import play_thumb, queue_thumb
from Royalkifeelings.helper.utils import skip_current_song, skip_item
from Royalkifeelings.callmusic.config import BOT_USERNAME
from Royalkifeelings import bot as Royalboyamit
from Royalkifeelings import call_py

@Royalboyamit.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        f"**ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ʀᴇʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ʙᴀʙʏ​ {m.from_user.mention()}.**"
    )


@Royalboyamit.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ")
        elif op == 1:
            await m.reply(f"**ɴᴏ ᴍᴏʀᴇ ǫᴜᴇᴜᴇ ɪᴀᴍ ʟᴇᴀᴠɪɴɢ ᴠᴄ ʙʏᴇ ғʀɴᴅs.**")
        elif op == 2:
            await m.reply("**ʙʏᴇ ʙʀᴏ ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ 😐🥀🥺.**")
        else:
            await m.reply(f"**✯ 𝖲ᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ ✯\n│ \n└ʙʏ : {m.from_user.mention()}⛄**")
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **ʀᴇᴍᴏᴠᴇᴅ sᴏɴɢ ғʀᴏᴍ ǫᴜᴇᴜᴇ:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Royalboyamit.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply(f"➻ **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ** ❄\n│ \n└ʙʏ : {m.from_user.mention()}🥀")
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪs sᴛɪsʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"➻ **sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ** 🥺\n│ \n└ʙʏ : {m.from_user.mention()}🥀."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"➻ **sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ** 💫\n│ \n└ʙʏ : {m.from_user.mention()} 🥀"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_message(command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                f"🎧 ᴠᴏɪᴄᴇᴄʜᴀᴛ ᴍᴜᴛᴇᴅ ʙʏ : {m.from_user.mention()}​!"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                f"🎧 ᴠᴏɪᴄᴇᴄʜᴀᴛ ᴜɴᴍᴜᴛᴇᴅ ʙʏ : {m.from_user.mention()} ​!."
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(
            "ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs."
        )
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs button !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ ʜᴀs ᴘᴀᴜsᴇᴅ"
                )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`", )
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Royalboyamit.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(
            "ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs."
        )
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ The Streaming has Resumed")
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Royalboyamit.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(
            "ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs."
        )
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text(
                "✅ **ᴛʜɪs sᴛʀᴇᴀᴍɪɴɢ ʜᴀs ᴇɴᴅᴇᴅ**")
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Royalboyamit.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(
            "ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs."
        )
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇsғᴜʟʟʏ ᴍᴜᴛᴇᴅ")
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Royalboyamit.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer(
            "you're an Anonymous Admin !\n\n» revert back to user account from admin rights."
        )
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇsғᴜʟʟʏ ᴜɴᴍᴜᴛᴇᴅ")
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`")
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Royalboyamit.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(f"✅ **ᴠᴏʟᴜᴍᴇ sᴇᴛ ᴛᴏ** `{range}`%")
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ**")


@Royalboyamit.on_callback_query(filters.regex("cbskip"))
async def cbskip(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    queue = await skip_current_song(chat_id)
    if queue == 0:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ", show_alert=True)
    elif queue == 1:
        await query.answer(
            "» ᴛʜᴇʀᴇ's ɴᴏ ᴍᴏʀᴇ ᴍᴜsɪᴄ ɪɴ ǫᴜᴇᴜᴇ ᴛᴏ sᴋɪᴘ, ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.",
            show_alert=True,
        )
    elif queue == 2:
        await query.answer(
            "🗑️ ᴄʟᴇᴀʀɪɴɢ ᴛʜᴇ **ǫᴜᴇᴜᴇs**\n\n» **ᴜsᴇʀʙᴏᴛ** ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ.",
            show_alert=True,
        )
    else:
        await query.answer("ɢᴏᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ, ᴘʀᴏᴄᴄᴇssɪɴɢ...")
        await query.message.delete()
        await m.reply_photo(
            photo=playimg,
            text=f"✅ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐍𝐞𝐱𝐭 𝐒𝐨𝐧𝐠\n𝐅𝐫𝐨𝐦 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 💞..",
        )
        remove_if_exists(message)
