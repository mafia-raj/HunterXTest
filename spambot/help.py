from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Pspam", b'pspam')
], [
    Button.inline("Extras", b'extras')
], [
    Button.url("Channel", "t.me/ITS_HELLL_BOYYY"),
    Button.url("Group", "t.me/ITS_HELLL_BOYYY")
]

BACK = [
    Button.inline("Back", b'back')
]

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/help'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        

