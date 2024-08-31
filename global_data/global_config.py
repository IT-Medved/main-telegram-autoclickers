import os

API_ID = os.getenv("API_ID", 111111111)
API_HASH = os.getenv("API_HASH", "111111111")
CHAT_ID = os.getenv("CHAT_ID", "111111")
# api tokens for tg bots, if USE_TH_BOT=True (get in @BotFather)
CHAT_TOKEN = os.getenv("CHAT_TOKEN", "111111")
REF_CODE= os.getenv("REF_CODE", "111111")


ACC_DELAY = [60, 180] # delay between connections to accounts in seconds
BIG_SLEEP = [14400,21600] # sleep between cycles in bots
USE_PROXY = False
PROXY_TYPE = "socks5" # http/socks5

# if you want to turn off the bot, select False in the corresponding line
CONECTED_BOTS = {
    "./1_blum" : True,
    "./2_cryptorank" : True,
    "./3_yescoin" : True,
    "./4_dotcoin" : True,
    "./5_pocketfi" : True,
    "./6_muskempire" : True,
    "./7_hamsterkombat" : True,
    "./8_okxracer" : True,
    "./9_lostdogs" : True,
    "./10_major" : True,
    "./11_nomis" : True,
    "./12_cats" : True,
}

USE_TG_BOT = False


BLUM_BOT_TOKEN = CHAT_TOKEN
CRYPTORANK_BOT_TOKEN = CHAT_TOKEN
YESCOIN_BOT_TOKEN = CHAT_TOKEN
DOTCOIN_BOT_TOKEN = CHAT_TOKEN
POCKETFI_BOT_TOKEN = CHAT_TOKEN
MUSKEMPIRE_BOT_TOKEN = CHAT_TOKEN
HAMSTERKOMBAT_BOT_TOKEN = CHAT_TOKEN
OKXRACER_BOT_TOKEN = CHAT_TOKEN
LOSTDOGS_BOT_TOKEN = CHAT_TOKEN
MAJOR_BOT_TOKEN = CHAT_TOKEN
NOMIS_BOT_TOKEN = CHAT_TOKEN
CATS_BOT_TOKEN = CHAT_TOKEN

# don't change
message = """
███████╗ █████╗ ██╗  ██╗██╗    ██╗███████╗██████╗
██╔════╝██╔══██╗╚██╗██╔╝██║    ██║██╔════╝██╔══██╗
█████╗  ███████║ ╚███╔╝ ██║ █╗ ██║█████╗  ██████╔╝
██╔══╝  ██╔══██║ ██╔██╗ ██║███╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██╔╝ ██╗╚███╔███╔╝███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝
GitHub Repository: https://github.com/FaxWeb7/main-telegram-autoclickers
"""
petyaPaths = [
    './1_blum',
    './2_cryptorank',
    './3_yescoin',
    './7_hamsterkombat',
    './8_okxracer',
    './10_major',
    './11_nomis',
    './12_cats',
]
shamhiPaths = [
    './4_dotcoin',
    './5_pocketfi',
    './6_muskempire',
    './9_lostdogs',
]