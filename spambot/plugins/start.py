from spambot import *

from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10

from telethon import events, Button





data  = [

    Button.url("Channel", url="t.me/ITS_HELLL_BOYYY"),

    Button.url("Repo", url="https://GitHub.com/Jatindalal875/"),

    Button.url("Group", url="t.me/EAGLE_MAFIA_CLUB")

]





@Hellboy1.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy2.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy3.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy3.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy5.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy6.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy7.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy8.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy9.on(events.NewMessage(incoming=True, pattern='/start'))

@Hellboy10.on(events.NewMessage(incoming=True, pattern='/start'))



async def start(e):

    if e.chat_id is e.sender_id:

        name = e.sender.first_name

        user_id = e.sender_id

        mention = f"[{name}](tg://user?id={user_id})"

        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"

        creator = f"[Hellboy](tg://user?id={1761766352})"

        sudo_user = ""

        if e.sender_id in MY_USERS:

            sudo_user = "True"

        else:

            sudo_user = "False"

        ON_START = f"""

Hey {mention},



This Is Hellboy Spam Bot!



Owner:- {myOwner}



Sudo:- {sudo_user}



Creator:- {creator}

    """

        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
