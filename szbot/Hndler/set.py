from szbot import sz
from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.raw.functions.messages import UpdatePinnedMessage
from pyrogram.types import InlineKeyboardButton
from config import BOT_USERNAME

@sz.on_message(filters.command('set'))
async def set_timer(client, message):
    text = f"""
๐โโ๏ธ**Hey**{message.from_user.mention},

๐ป You can't use this command in bot pm so Try this command 
In your [Group](https://t.me/slbotzone) If you don't have any group yet , create public 
group first after [add me as admin in your group](https://t.me/{BOT_USERNAME}?startgroup=true) with this permissions
     
     โ __Pin message__     
     โ __Ban users__
     โ __Add users__
     โ __Add Admin__

๐ฐ Then type /reload command & ** Re-Use Help menu** 

โฌโโโโโโโโโโโโโโฌ
๐ค แชแแฏแแชOแญแแ :- [supun maduranga](https://t.me/supunmabot)
๐ฆ Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ

โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
"""
    Info = [
            [
                InlineKeyboardButton('support', url="https://t.me/slbotzone"),
                InlineKeyboardButton(',แดแดแดแดแดแดs', url='https://t.me/szteambots'),
            ],
            [
                InlineKeyboardButton('โ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแดโ โ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]
        ]
    global stoptimer
    try:
        if message.chat.id>1:
            return await message.reply_photo(
                photo = "",
                caption = text,
                reply_markup=Info)
        elif not (await client.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            return await message.reply_text(
                text = 
f"""๐จ Sorry{message.from_user.mention}, 

**only admins**๐ฎ๐ปโโ๏ธ  can execute this command In This group

โ But you can create Your public group and adding me as admin & 
use me without any problem.

โฌโโโโโโโโโโโโโโฌ
๐ค แชแแฏแแชOแญแแ :- [supun maduranga](https://t.me/supunmabot)
๐ฆ Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ

โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
""", reply_markup=Info           
         )    
        
        elif len(message.command)<3:
            return await message.reply_text(
f"""

โโ **Incorrect format.**โโ

{message.from_user.mention}โ Format should be like

 /set seconds "event"

 **Example**:/set 86400 "TIME LEFT UNTIL NEW DAY"

{message.from_user.mention}๐จ For your Knowledge : ** 86400 s = 24h/1 day**

**โ ๏ธWARNING:**

DO NOT do more than two (2) countdowns at the same time using the same bot. 
`Reason: Telegram floodwait`

โฌโโโโโโโโโโโโโโฌ
๐ค แชแแฏแแชOแญแแ :- [supun maduranga](https://t.me/supunmabot)
๐ฆ Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ

โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
 """,reply_markup=Inf)    
        else:
            user_input_time = int(message.command[1])
            user_input_event = str(message.command[2])
            get_user_input_time = await sz.send_message(message.chat.id, user_input_time)
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if 0<user_input_time<=10:
                while user_input_time and not stoptimer:
                    s=user_input_time%60
                    countdown_sz="""
** Live Countdown Timer is now started!**โณ                    


Event: {}

Time : {:02d} **s**


โฌโโโโโโโโโโโโโโฌ
**Your Time Is Limited**,So Don't Waste It 
โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
โฌโโโโโโโโโโโโโโฌ

""".format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(countdown_sz)
                    await asyncio.sleep(1)
                    user_input_time -=1
                await finish_countdown.edit("""
โฐโฐ  **TIME'S UP!!!**              

Your Time's has up

Your event :{}
Your Time :{:02d} **s**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""".format(user_input_event, s))
            elif 10<user_input_time<60:
                while user_input_time>0 and not stoptimer:
                    s=user_input_time%60
                    countdown_sz="""
 **Live Countdown Timer is now started!**โณ                    


Event: {}

Time : {:02d} **s**


โฌโโโโโโโโโโโโโโฌ
**Your Time Is Limited**,So Don't Waste It 
โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
โฌโโโโโโโโโโโโโโฌ

""".format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(countdown_sz)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("""
โฐโฐ  **TIME'S UP!!!**               

Your Time's has up

Your event :{}
Your Time :{:02d} **s**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""".format(user_input_event, s))
            elif 60<=user_input_time<3600:
                while user_input_time>0 and not stoptimer:
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    countdown_sz="""
**Live Countdown Timer is now started!**โณ                    


Event: {}

Time : {:02d} **s**


โฌโโโโโโโโโโโโโโฌ
**Your Time Is Limited**,So Don't Waste It 
โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
โฌโโโโโโโโโโโโโโฌ

""".format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(countdown_sz)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("""
โฐโฐ  **TIME'S UP!!!**               

Your Time's has up

Your event :{}
Your Time :{:02d} **s**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""".format(user_input_event, s))
            elif 3600<=user_input_time<86400:
                while user_input_time>0 and not stoptimer:
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    countdown_sz="""
**Live Countdown Timer is now started!**โณ                    


Event: {}

Time : {:02d} **s**


โฌโโโโโโโโโโโโโโฌ
**Your Time Is Limited**,So Don't Waste It 
โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
โฌโโโโโโโโโโโโโโฌ

""".format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(countdown_sz)
                    await asyncio.sleep(7)
                    user_input_time -=7
                await finish_countdown.edit("""
โฐโฐ  **TIME'S UP!!!**               

Your Time's has up

Your event :{}
Your Time :{:02d} **s**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""".format(user_input_event, s))
            elif user_input_time>=86400:
                while user_input_time>0 and not stoptimer:
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    countdown_sz="""
**Live Countdown Timer is now started!**โณ                    


Event: {}

Time : {:02d} **s**


โฌโโโโโโโโโโโโโโฌ
**Your Time Is Limited**,So Don't Waste It 
โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
โฌโโโโโโโโโโโโโโฌ

""".format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(countdown_sz)
                    await asyncio.sleep(9)
                    user_input_time -=9
                await finish_countdown.edit("""
โฐโฐ  **TIME'S UP!!!**               

Your Time's has up

Your event :{}
Your Time :{:02d} **s**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""".format(user_input_event, s))
            else:
                await get_user_input_time.edit(f"๐คท๐ปโโ๏ธ I can't countdown from {user_input_time}")
                await get_user_input_time.unpin()
    except FloodWait as e:
        await asyncio.sleep(e.x)


Inf = [
            [
                InlineKeyboardButton('support', url="https://t.me/slbotzone"),
                InlineKeyboardButton(',แดแดแดแดแดแดs', url='https://t.me/szteambots'),
            ]
        ] 

@sz.on_message(filters.command('stop'))
async def stop_timer(Client, message):
    global stoptimer
    try:
        if (await sz.get_chat_member(message.chat.id,message.from_user.id)).can_manage_chat:
            stoptimer = True
            await message.reply("""
๐ ** Countdown stopped.**

I will be unpin this message if you want you can set new 
Time again !!!!!

โฌโโโโโโโโโโโโโโฌ  
๐ค Powered By :- `ใSZโขใ`
โฌโโโโโโโโโโโโโโฌ               
""")
        else:
            await message.reply_text(
                text = f"""๐จ Sorry{message.from_user.mention}, 
                **only admins**๐ฎ๐ปโโ๏ธ  can execute this command In This group

                โ But you can create Your public group and adding me as admin & 
                use me without any problem.

                โฌโโโโโโโโโโโโโโฌ
                ๐ค แชแแฏแแชOแญแแ :- [supun maduranga](https://t.me/supunmabot)
                ๐ฆ Powered By :- `ใSZโขใ`
                โฌโโโโโโโโโโโโโโฌ

                โ ๏ธcopyright ยฉ๏ธ 2021 TeLe TiPs. ** All Rights Reserved** 
                """, reply_markup=Ifo                           
            )    
    except FloodWait as e:
        await asyncio.sleep(e.x)


Ifo = [
            [
                InlineKeyboardButton('support', url="https://t.me/slbotzone"),
                InlineKeyboardButton(',แดแดแดแดแดแดs', url='https://t.me/szteambots'),
            ],
            [
                InlineKeyboardButton('โ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแดโ โ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]
        ]
