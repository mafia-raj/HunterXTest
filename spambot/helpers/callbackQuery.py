from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10
from spambot.help import
from spambot.helpers.commands import *
from telethon import events


@Hellboy1.on(events.CallbackQuery(data=b'alive'))
@Hellboy2.on(events.CallbackQuery(data=b'alive'))
@Hellboy3.on(events.CallbackQuery(data=b'alive'))
@Hellboy4.on(events.CallbackQuery(data=b'alive'))
@Hellboy5.on(events.CallbackQuery(data=b'alive'))
@Hellboy6.on(events.CallbackQuery(data=b'alive'))
@Hellboy7.on(events.CallbackQuery(data=b'alive'))
@Hellboy8.on(events.CallbackQuery(data=b'alive'))
@Hellboy9.on(events.CallbackQuery(data=b'alive'))
@Hellboy9.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'ping'))
@Hellboy2.on(events.CallbackQuery(data=b'ping'))
@Hellboy3.on(events.CallbackQuery(data=b'ping'))
@Hellboy4.on(events.CallbackQuery(data=b'ping'))
@Hellboy5.on(events.CallbackQuery(data=b'ping'))
@Hellboy6.on(events.CallbackQuery(data=b'ping'))
@Hellboy7.on(events.CallbackQuery(data=b'ping'))
@Hellboy8.on(events.CallbackQuery(data=b'ping'))
@Hellboy9.on(events.CallbackQuery(data=b'ping'))
@Hellboy10.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'raid'))
@Hellboy2.on(events.CallbackQuery(data=b'raid'))
@Hellboy3.on(events.CallbackQuery(data=b'raid'))
@Hellboy4.on(events.CallbackQuery(data=b'raid'))
@Hellboy5.on(events.CallbackQuery(data=b'raid'))
@Hellboy6.on(events.CallbackQuery(data=b'raid'))
@Hellboy7.on(events.CallbackQuery(data=b'raid'))
@Hellboy8.on(events.CallbackQuery(data=b'raid'))
@Hellboy9.on(events.CallbackQuery(data=b'raid'))
@Hellboy10.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy2.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy3.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy4.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy5.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy6.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy7.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy8.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy9.on(events.CallbackQuery(data=b'replyraid'))
@Hellboy10.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'spam'))
@Hellboy2.on(events.CallbackQuery(data=b'spam'))
@Hellboy3.on(events.CallbackQuery(data=b'spam'))
@Hellboy4.on(events.CallbackQuery(data=b'spam'))
@Hellboy5.on(events.CallbackQuery(data=b'spam'))
@Hellboy6.on(events.CallbackQuery(data=b'spam'))
@Hellboy7.on(events.CallbackQuery(data=b'spam'))
@Hellboy8.on(events.CallbackQuery(data=b'spam'))
@Hellboy9.on(events.CallbackQuery(data=b'spam'))
@Hellboy10.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'pspam'))
@Hellboy2.on(events.CallbackQuery(data=b'pspam'))
@Hellboy3.on(events.CallbackQuery(data=b'pspam'))
@Hellboy4.on(events.CallbackQuery(data=b'pspam'))
@Hellboy5.on(events.CallbackQuery(data=b'pspam'))
@Hellboy6.on(events.CallbackQuery(data=b'pspam'))
@Hellboy7.on(events.CallbackQuery(data=b'pspam'))
@Hellboy8.on(events.CallbackQuery(data=b'pspam'))
@Hellboy9.on(events.CallbackQuery(data=b'pspam'))
@Hellboy10.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'extras'))
@Hellboy2.on(events.CallbackQuery(data=b'extras'))
@Hellboy3.on(events.CallbackQuery(data=b'extras'))
@Hellboy4.on(events.CallbackQuery(data=b'extras'))
@Hellboy5.on(events.CallbackQuery(data=b'extras'))
@Hellboy6.on(events.CallbackQuery(data=b'extras'))
@Hellboy7.on(events.CallbackQuery(data=b'extras'))
@Hellboy8.on(events.CallbackQuery(data=b'extras'))
@Hellboy9.on(events.CallbackQuery(data=b'extras'))
@Hellboy10.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@Hellboy1.on(events.CallbackQuery(data=b'back'))
@Hellboy2.on(events.CallbackQuery(data=b'back'))
@Hellboy3.on(events.CallbackQuery(data=b'back'))
@Hellboy4.on(events.CallbackQuery(data=b'back'))
@Hellboy5.on(events.CallbackQuery(data=b'back'))
@Hellboy6.on(events.CallbackQuery(data=b'back'))
@Hellboy7.on(events.CallbackQuery(data=b'back'))
@Hellboy8.on(events.CallbackQuery(data=b'back'))
@Hellboy9.on(events.CallbackQuery(data=b'back'))
@Hellboy10.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 