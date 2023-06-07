import random
from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10
from spambot.helpers.plinks import PLINKS
from telethon import events

a = False

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/pspam'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/pspam'))
async def pspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        elif e.raw_text[6:] == "":
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        
@Hellboy1.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy2.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy3.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy4.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy5.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy6.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy7.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy8.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy9.on(events.NewMessage(incoming=True, pattern="/pstop"))
@Hellboy10.on(events.NewMessage(incoming=True, pattern="/pstop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "Porn Spam Stopped Successfully")