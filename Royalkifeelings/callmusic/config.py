from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "BQC86fAAMe1iNm7anvlApEpatr3c5tyB4WyvtqW6dRX27-PYRzXaihpI78yNpm6lffAhoN9tOG2mGAV2ER0qh8-WE5PLYieWk5KWQOFM3VbpamK_gTI8flWzGw1g0etAqvXXUvWjJXUHslREhSfW-3JlVf78BhhiG5nzbWKaKa_juOFlXSg77dbyfDT0qSdE-Jhz0ym00azqQ38w7Ron9OINKVhnOkvZv_ezm4L_5P4uOi3teeEBq6h1eVgaiUBo564XMORQROAu7ZNNwUg8P6Ebv5lte7ylYiC_tEaX2es0wbemyHWG5NOF8O2-VrtScqI_0vnhxkpNqXlkZEflAbNzI3JPKQAAAAHF-rqIAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "GrooveXrobot")
BOT_TOKEN = getenv("BOT_TOKEN", "5256748757:AAF1y2mzvFPvLRUEr8kl8l6g_13wo3Wjcz0")
API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/bgt_chat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/bgt_chat")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7698499481").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7694947402").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12000"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","Yt-New")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://graph.org/file/fb54122a20bce19326a44-d01adc766e60899495.jpg")
