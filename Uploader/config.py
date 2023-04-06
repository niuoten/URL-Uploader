# MIT License

# Copyright (c) 2023 by niuoten & Aj Freddy

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    WEBHOOK = os.environ.get("BOT_TOKEN", False)
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # file /video dpwnload location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "None")
    # If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."

    # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "None")
    # If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    OWNER_ID = int(os.environ.get("OWNER_ID", "12356"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x)
                      for x in os.environ.get("AUTH_USERS", "0").split()})
    AUTH_USERS.append(OWNER_ID)
