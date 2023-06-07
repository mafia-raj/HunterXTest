import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from spambot import *
from spambot import Hellboy1, Hellboy2, Hellboy3, Hellboy4, Hellboy5, Hellboy6, Hellboy7, Hellboy8, Hellboy9, Hellboy10

def load_plugs(plugname):
    modules = Path(f"spambot/plugins/{plugname}.py")
    myfiles = f"spambot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["spambot.plugins." + plugname] = load
    print("HellboySpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import spambot
import spambot.userNeeds
import spambot.help
import spambot.helpers.callbackQuery

print("\n\nHellboy Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        Hellboy1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy5.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy6.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy7.disconnect()
    except Exception as e:
       print(e)
       pass
    try:
        Hellboy8.disconnect()
    except Exception as e:
       print(e)
       pass
    try:
        Hellboy9.disconnect()
    except Exception as e:
       print(e)
       pass
    try:
        Hellboy10.disconnect()
    except Exception as e:
       print(e)
       pass
  else:
    try:
        Hellboy1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy6.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy7.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellbo8.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy9.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Hellboy10.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
