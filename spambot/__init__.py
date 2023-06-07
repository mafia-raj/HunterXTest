import asyncio
import logging
from telethon import TelegramClient
from spambot.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
BOT_TOKEN6 = Config.BOT_TOKEN6
BOT_TOKEN7 = Config.BOT_TOKEN7
BOT_TOKEN8 = Config.BOT_TOKEN8
BOT_TOKEN9 = Config.BOT_TOKEN9
BOT_TOKEN10 = Config.BOT_TOKEN10
OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "HellboySpamBot"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "Eagle_Mafia_Club"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://te.legra.ph/file/5135ac513a382c35c3650.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "Hellboy Spam Bot Ready To Fuck Haters!"


BOT_VERSION = 1.0

GOD_USERS = [1761766352]
DEV_USERS = [5331427205]
MY_USERS = [1761766352]
LIMIT = [1761766352]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global Hellboy1
    global Hellboy2
    global Hellboy3
    global Hellboy4
    global Hellboy5
    global Hellboy6
    global Hellboy7
    global Hellboy8
    global Hellboy9
    global Hellboy10

    if BOT_TOKEN1:
        print("Working On Bot Token 1!")
        try:
            Hellboy1 = TelegramClient("HellboySpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK!")
            await Hellboy1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot1"
            Hellboy1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2!")
        try:
            Hellboy2 = TelegramClient("HellboySpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!")
            await Hellboy2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot2"
            Hellboy2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await hellboy2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            pass
    
    if BOT_TOKEN3:
        print("Working On Bot Token 3!")
        try:
            Hellboy3 = TelegramClient("HellboySpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK!")
            await Hellboy3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot3"
            Hellboy3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await HellboySpamBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4!")
        try:
            Hellboy4 = TelegramClient("HellboySpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK!")
            await Hellboy4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot4"
            Hellboy4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5!")
        try:
            Hellboy5 = TelegramClient("HellboySpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK!")
            await Hellboy5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot5"
            Hellboy5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

    if BOT_TOKEN6:
        print("Working On Bot Token 6!")
        try:
            Hellboy6 = TelegramClient("HellboySpamBot6", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 6 OK!")
            await Hellboy6.start(bot_token=BOT_TOKEN6)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot6"
            Hellboy6 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy6.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass
         
    if BOT_TOKEN7:

        print("Working On Bot Token 7!")
        try:
            Hellboy7 = TelegramClient ("HellboySpamBot7", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 7 OK!")
            await Hellboy7.start(bot_token=BOT_TOKEN7)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 7 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot7"
            Hellboy7 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy7.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass
         
    if BOT_TOKEN8:
        print("Working On Bot Token 8!")
        try:
            Hellboy8 = TelegramClient("HellboySpamBot8", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 8 OK!")
            await Hellboy8.start(bot_token=BOT_TOKEN8)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 8 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot8"
            Hellboy8 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy8.start(bot_token=BOT_TOKEN8)
        except Exception as e:
            pass
         
    if BOT_TOKEN9:
        print("Working On Bot Token 9!")
        try:
            Hellboy9 = TelegramClient("HellboySpamBot9", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token9 OK!")
            await Hellboy9.start(bot_token=BOT_TOKEN9)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 9 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot9"
            Hellboy9 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy9.start(bot_token=BOT_TOKEN9)
        except Exception as e:
            pass
         
    if BOT_TOKEN10:
        print("Working On Bot Token 10!")
        try:
            Hellboy10 = TelegramClient("HellboySpamBot10", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 10 OK!")
            await Hellboy10.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 10 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellboySpamBot10"
            Hellboy10 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await Hellboy10.start(bot_token=BOT_TOKEN10)
        except Exception as e:
            pass
          
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
