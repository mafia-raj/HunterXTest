from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8,  Hellboy9, Hellboy10
from telethon import events

a = False

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/spam'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/spam'))
async def spam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[6:8])
            spam = text[8:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                    await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/bigspam'))
async def bigspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[9:15])
            spam = text[15:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                            await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@Hellboy1.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy2.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy3.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy4.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy5.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy6.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy7.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy8.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy9.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Hellboy10.on(events.NewMessage(incoming=True, pattern='/mspam'))
async def mspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[7:13])
            if e.is_reply == False:
                await e.client.send_message(e.chat_id, "Please reply to a media and enter how many times you want send that media!")
            elif e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.media
                for i in range(counts):
                    await e.client.send_file(e.chat_id, replied_message)
            else:
                await e.client.send_message(e.chat_id, "Some thing went wrong! Please reply to a media and enter how many times you want send that media!")
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Please enter how many times you want to spam in reply of media!")

@Hellboy1.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy2.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy3.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy4.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy5.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy6.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy7.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy8.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy9.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Hellboy10.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@Hellboy1.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy2.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy3.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy4.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy5.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy6.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy7.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy8(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy9.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Hellboy10.on(events.NewMessage(incoming=True, pattern="/ustop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
