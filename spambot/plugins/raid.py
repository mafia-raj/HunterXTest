import random
from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10
from spambot.helpers.gspam import GSPAM
from telethon import events


myraid = False
fraid = False

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/mraid'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/mraid'))
async def mraid(e):
    if e.sender_id in MY_USERS:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await MafiaBot1.get_me()
        global myraid
        if e.is_reply is True:
            replied = await e.get_reply_message()
            get_name = replied.sender.first_name
            get_id = replied.sender.id
            tag = f"[{get_name}](tg://user?id={get_id})"
            try:
                if get_id in DEV_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                elif get_id == OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                elif get_id in CO_OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                elif get_id  in SUDO_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                elif get_id == me.id:
                    await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                else:
                    await e.client.send_message(e.chat_id, f"`Mention Raid Activated On` {tag}!")
                    myraid = True
                    while myraid == True:
                        myMessage = random.choice(GSPAM)
                        await e.client.send_message(e.chat_id, f"{tag} {myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            text = e.raw_text[7:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Mention Raid!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    if get_id in DEV_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                    elif get_id == OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                    elif get_id in CO_OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                    elif get_id  in SUDO_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                    elif get_id == me.id:
                        await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                    else:
                        await e.client.send_message(e.chat_id, f"`Mention Raid Activated On` {tag}!")
                        myraid = True
                        while myraid == True:
                            myMessage = random.choice(GSPAM)
                            await e.client.send_message(e.chat_id, f"{tag} {myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")


@Hellboy1.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/sraid'))
@HHellbo7.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/sraid'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/sraid'))
async def sraid(e):
    if e.sender_id in MY_USERS:
        global myraid
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                myraid = False
                await e.client.send_message(e.chat_id, f"`Mention Raid Dectivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[7:]
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Mention Raid!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    myraid = False
                    await e.client.send_message(e.chat_id, f"`Reply Raid Dectivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
 
@Hellboy1.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/raid'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/raid'))
async def raid(e):
    if e.sender_id in MY_USERS:
        global fraid
        fraid = True
        await e.client.send_message(e.chat_id, "`Raid Activated Successfully`")
        while fraid == True:
            myMessage = random.choice(GSPAM)
            await e.client.send_message(e.chat_id, myMessage)


@Hellboy1.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/draid'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/draid'))
async def draid(e):
    if e.sender_id in MY_USERS:
        global fraid
        fraid = False
        await e.client.send_message(e.chat_id, "`Raid Stopped Successfully`")
