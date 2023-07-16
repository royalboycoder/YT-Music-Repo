from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "BQCU-QOEzmxmU32qjmbkchP1M3JVoy_T_7699WG4dO-sQqSBC3s5g82IPslYJfs16JpJMTujuZUYIttzwHncDfjxvRl69V75fSU4SBeLj6WRmC6DaGi6GdmDXFwoeTQODM-eFYo3p_iBJtQnx5XxGFFpT_OA_MqoLr7oBjYCFUXB4ZPtzi0kWOwcouq2tkU-Hy5wILLFZFwiO8MXt-813l9KiQaA1hZ1VzDboL8INVHsRGyq5j5f3-cQJ3kbDpZeTQvsvpoAgpB2d5Xc-8TsWy9j6zL6GrRdE9TJbqK-xN-7Uusyzq2SyKYSufv699iN4JOkKyhjW_kJXWb5f9EsN172AAAAAUViqG8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "KAALXMUSIC34bot")
BOT_TOKEN = getenv("BOT_TOKEN", "5434884471:AAF3N39kLOTOlosoOGUUf1gSn9c8JeWSevA")
API_ID = int(getenv("API_ID", "9797600"))
API_HASH = getenv("API_HASH", "9c33a79118c2cb1bf13401a37bf3d70c")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6256455516").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5459060847").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","Kaal")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
