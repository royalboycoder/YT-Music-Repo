from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from Royalkifeelings.callmusic.config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID, SESSION_NAME
from Royalkifeelings.plugins import ALL_PLUGINS

bot = Client(
    "Royalkifeelings",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

Royalboyamit = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
)

user = PyTgCalls(
    Royalboyamit,
    cache_duration=100,
    overload_quiet_mode=True,
)

call_py = PyTgCalls(Royalboyamit, overload_quiet_mode=True)

OWNER_NAME = "Royal_boy_amit"
F_OWNER = OWNER_ID[0]

with Client("Royalkifeelings", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    x = app.get_me()
    BOT_ID = x.id
    BOT_NAME = x.first_name + (x.last_name or "")
    BOT_USERNAME = x.username
    BOT_MENTION = x.mention
    BOT_DC_ID = x.dc_id
with Royalboyamit as ass:
    getass = ass.get_me()
    ASSISTANT_USERNAME = getass.username
