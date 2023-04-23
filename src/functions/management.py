import os
import random
import win32ui

chars = 0
appList = []

def randomPath():
    path_list = ["%tmp%", "%appdata%", "%localappdata%"]
    return random.choice(path_list)

def randomFileName():
    return str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'

def getOsname():
    return os.getenv()

def isAppRunning(WindowName, app_list):
    try:
        for _ in appList:
            if win32ui.FindWindow(None, WindowName) in app_list:
                print("")
    except Exception as e:
        return e

def addApp(app_name):
    return appList.append(app_name)

def printList(list):
    return "".join(list)