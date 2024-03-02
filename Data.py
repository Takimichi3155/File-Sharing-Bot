# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
├ /start - Start Bot
├ /about - About this Bot
├ /help - Help this Bot Command
├ /ping - To check live bots
└ /uptime - To view bot status

❏ Commands For BOT Admin
 ├ /logs - To view bot logs
 ├ /setvar - To set the var with the dibot command
 ├ /delvar - To delete var with dibot command
 ├ /getvar - To view any
 ├  /users - To view bot user statistics
 ├ /batch - To link more than one file
 ├ /speedtest - To test bot server speed
 └ /broadcast - To send a broadcast message to the pen

👨‍💻 Develoved by </b><a href='https://t.me/aye_ujjwal'>@aye_ujjwal</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:

 ᴛʜɪꜱ ɪꜱ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @aye_ujjwal.

 • ᴍʏ ꜱᴇɴꜱᴇɪ 💕: @{}
 • ᴍᴀɪɴ: <a href='https://t.me/Otaku_Vision_M'>Pyrogram</a>
 • ᴄᴏɴᴛᴀᴄᴛ ꜰᴏʀ ʀᴇᴘᴏ: <a href='https://t.me/aye_ujjwal'>@ᴀʏᴇ_ᴜᴊᴊᴡᴀʟ v4</a>

👨‍💻 Develoved by </b><a href='https://t.me/aye_ujjwal'>@aye_ujjwal</a>
"""
