from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8,  Hellboy9, Hellboy10
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
Hellboy Spam Bot Is Alive!

My Master:- {master}

Bot Version:- `{BOT_VERSION}`

Telethon Version:- `{version.__version__}`

{BIO_MSG}
"""

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/alive'))
@HHellbo8.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/alive'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
