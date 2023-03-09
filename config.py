from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f0f1f6aef799e282ba0a1.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f0f1f6aef799e282ba0a1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("قناة المبرمج", "https://t.me/W_II_Y")
SUPPORT_CHANNEL = getenv("جروب الدعم", "https://t.me/+wxZC6M1nTBQyNmU8")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1420171187").split()))


FAILED = "https://telegra.ph/file/f0f1f6aef799e282ba0a1.jpg"
