from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8,  Hellboy9, Hellboy10
from telethon import events
from datetime import datetime

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/ping'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Ping Pong!\n\nHellboy Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nPing:- {ms} ms\n\nHellboy Spam Bot On Fire")
