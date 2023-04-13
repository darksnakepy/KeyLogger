import os
import random

chars = 0

def randomPath():
    path_list = ["%tmp%", "%appdata%", "%localappdata%"]
    return random.choice(path_list)

def randomFileName():
    return str(chars) + 'I' + str(random.randint(1000000, 9999999)) + '.txt'