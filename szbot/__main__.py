

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from szbot import sz
from szbot import LOGGER
from pyrogram.errors import UserNotParticipant #fsub
from pyrogram import idle, filters
from config import IMAGE, BOT_USERNAME
from helpers.database.add_user import AddUserToDatabase
from helpers.database import db

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** â¹ï¸\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again ð"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel ð£", url=f"https://t.me/szteambots") 
        ]]      
    )

@sz.on_message(filters.command("start"))
async def start(client, message): 
    await AddUserToDatabase(client, message)    
    try: #fsub start
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return   #fsub end
    total_users = await db.total_users_count()     
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        button = [
    [
        InlineKeyboardButton(text="â¤ï¸ My Help â¤ï¸",callback_data="help"),
        InlineKeyboardButton(text="ð» Support ð»", url="http://t.me/slbotzone")
    ],   
    [
        InlineKeyboardButton(text="â³ Add Me To Your Group â³", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]  
        text = f"""

Hello {message.from_user.mention} ð
I am an advance **Live Time Countdown Bot**  with more features.

ðI can countdown to your important events in **Public Groups**. 
ðUse me to keep track of how much time is left for the event 

If you want to know how to use this bot just
touch on `Help` Button ð¨

User count ; `{total_users}`

â¬ââââââââââââââ¬
ð¤ ððð©ððð¢ð£ðð ðð¬ :- [SL Bot Zero](https://t.me/szteambots)
ð¦ Powered By :- `ãSZâ¢ã`
â¬ââââââââââââââ¬

â ï¸copyright Â©ï¸ 2021 TeLe TiPs. ** All Rights Reserved** 
"""    
    else:
        button = None
    await message.reply_photo(
                    photo=f"{IMAGE}",
                    reply_markup=InlineKeyboardMarkup(button),
                    caption=text,
                    disable_web_page_preview=True)


@sz.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client, message):    
    await AddUserToDatabase(client, message)
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return   #fsub end
    total_users = await db.total_users_count()  
    text = f""" Hello {message.from_user.mention} ð
I am an advance **Live Time Countdown Bot**  with more features.

ðI can countdown to your important events in **Public Groups**. 
ðUse me to keep track of how much time is left for the event 

If you want to know how to use this bot just
touch on `Contact Me PM for Help` Button ð¨

User count ; `{total_users}`

â¬ââââââââââââââ¬
ð¤ ðð²ðð²ð¹ð¼ð½ð²ð± ðð :- [SZ TEAM](https://t.me/szteambots)
ð¦ Powered By :- `ãSZâ¢ã`
â¬ââââââââââââââ¬

â ï¸copyright Â©ï¸ 2021 TeLe TiPs. ** All Rights Reserved** """

    await message.reply_photo(
                    photo=f"{IMAGE}",
                    reply_markup=InlineKeyboardMarkup(botton),
                    caption=text,
                    disable_web_page_preview=True)
botton = [
    [
        InlineKeyboardButton(text="Updates Channel",url="http://t.me/szteambots"),
        InlineKeyboardButton(text="Support Chat", url="http://t.me/slbotzone")
    ],   
    [
        InlineKeyboardButton(text="Contact Me PM for Help", url=f"http://t.me/{BOT_USERNAME}?start=help"),
    ],
]     

@sz.on_message(filters.command(["help"]))
async def help(sz, message):
    await message.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=False,
        reply_markup=btton) 

btton = [
    [
        InlineKeyboardButton(text="Updates Channel",url="http://t.me/szteambots"),
        InlineKeyboardButton(text="Support Chat", url="http://t.me/slbotzone")
    ],   
    [
        InlineKeyboardButton(text="Back", callback_data="start"),
    ],
]


HELP_TEXT = f"""

**How To Setup This Bot In Your Group** â

â  **Step 1** - Start bot & click [â³ Add Me To Your Group â³](http://t.me/{BOT_USERNAME}?startgroup=new) Button.

ð° [Add This bot to your group](http://t.me/{BOT_USERNAME}?startgroup=new).


â  **Step 2** - **Make Admin** ð®ð»ââï¸

ð° Don't forget to make your bot admin of the group
with this permissions     
     â __Pin message__   
     â __Ban users__ 
     â __Add users__ 
     â __Add Admin__

â  **Step 3** - **Commands** ( /set  &  /stopc )ð¹

ð° Send the command below in correct format to the group.

â Format should be like

 /set seconds "event"

**Example**: /set 86400 "TIME LEFT UNTIL NEW DAY"

ð¨ For your Knowledge : ** 86400 s = 24h/1 day**

That's all Finish !!

â¬ââââââââââââââ¬
ð¤ áªáá¯ááªOá­áá :- [SZ Team](https://t.me/supunmabot)
ð¦ Powered By :- `ãSZâ¢ã`
â¬ââââââââââââââ¬

DO NOT do more than two (2) countdowns at the same time using the same bot. 
`Reason: Telegram floodwait`

â ï¸copyright Â©ï¸ 2021 TeLe TiPs. ** All Rights Reserved** 
"""


sz.start()
LOGGER.info("""
starting wait man....\\\\\..////..\\\.. now ok !!!!!
""")
idle()
