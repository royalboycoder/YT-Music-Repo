from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12000"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "")
