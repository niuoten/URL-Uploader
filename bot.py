# MIT License

# Copyright (c) 2023 by niuoten & Aj Freddy 

import os
from pyrogram import Client, idle

if bool(os.environ.get("WEBHOOK")):
    from Uploader.config import Config
else:
    from sample_config import Config

import os

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="Uploader")
    Uploadbot = Client("All-Url-Uploader",
                       bot_token=Config.BOT_TOKEN,
                       api_id=Config.API_ID,
                       api_hash=Config.API_HASH,
                       plugins=plugins)
    logger.info("Bot Started :)")
    Uploadbot.run()
    idle()
    logger.info("Bot Stoped ;)")
