import asyncio
import importlib

from pytgcalls import idle

from Royalkifeelings.callmusic import BOT_USERNAME, bot, call_py
from Royalkifeelings.callmusic.plugins import ALL_PLUGINS

loop = asyncio.get_event_loop()


async def Royalkifeelings.callmusic_boot():
    for all_module in ALL_PLUGINS:
        importlib.import_module("Royalkifeelings.callmusic.plugins." + all_module)
    await bot.start()
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(Royalkifeelings.callmusic_boot())
