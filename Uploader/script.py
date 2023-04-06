# MIT License

# Copyright (c) 2023 by niuoten & Aj Freddy

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
Hi {} 

I am Powerful Url Uploader Bot
 
"""

    HELP_TEXT = """

# Send me the Google Drive | ytdl | direct links.

# Select the desired option.

# Then be relaxed your file will be uploaded soon..
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b> My Name</b> : Url Uploader Bot

<b> Channel</b> : <a href="https://t.me/estkan3a">@estkan3a</a>

<b> Heroku</b> : <a href="https://heroku.com/">Heroku</a>

<b> Language :</b> <a href="https://www.python.org/">Python 3.10.5 and up </a>

<b>🇵🇲 Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.30</a>

<b>Developer :</b> <a href="https://t.me/Aj_Freddy">@Aj_Freddy</a>

"""

    PROGRESS = """
   Speed : {3}/s\n\n
   Done : {1}\n\n
  Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
  Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""
    ID_TEXT = """
  Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

   First Name : <b>{}</b>

  Second Name : <b>{}</b>

  Username : <b>@{}</b>

  Telegram Id : <code>{}</code>

  Profile Link : <b>{}</b>

  Dc : <b>{}</b>

  Language : <b>{}</b>

  Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(' Help', callback_data='help'),
            InlineKeyboardButton('  About', callback_data='about')
        ], [
            InlineKeyboardButton(' Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(' Home', callback_data='home'),
            InlineKeyboardButton(' About', callback_data='about')
        ], [
            InlineKeyboardButton(' Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(' Home', callback_data='home'),
            InlineKeyboardButton(' Help', callback_data='help')
        ], [
            InlineKeyboardButton(' Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(' Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download ... \n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n Uploading Please Wait ... "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = " Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
