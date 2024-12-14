from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "10035836"))
API_HASH = getenv("API_HASH", "2c782854a7292db305eb6c0be74cc28a")
BOT_TOKEN = getenv("BOT_TOKEN", "8068753850:AAHY7h68xwjt6G0IS1ynrpWyiDP2MV-BsDw")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuxLk0RaKb6YHWqIbggdmhk-Q4I9pJbx8d9CY7SmhFN6pcNuf3yEqJxeCU_S45eedLWtjL64Rc9PVoE5t6AtZ-o6RLeLfksmi5Jtde3_SrqzqMDj01GdjdEP9BLklYCHib4WoCH3w0xrS9znBDUGjpQZt8wvHRO_eNFONB7Tk6UXrOsgbHij7srv0u2gpHpZXrUZmUT-rZPf-qlOdRXj8twbl84EoCgAlMv3qOAoiM43LwTt1MJ_I3_LKPsJPxoLWugawWNxRQwkv9QYyDgl2-utKpbEFm83JCHjyKIR8S2tgWg8q84IAQqD2leGNEndvv7sGoXsmyu04NZcYzslrNho=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "vvvvvvvvvvvvvvvvvvvvvvvvvvvvg")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "eb_7Bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LINKASKR")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LINKASKR")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
