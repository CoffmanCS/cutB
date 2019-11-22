#Drew Arocha 2019
#cutB version 1.02
import socket
from _thread import *
import sys
import pickle
import random
import select
import time

server = socket.gethostname()
#'10.84.129.230' 
#note to self: change this to ip
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

def get_dict():     
    f = b''
    msg = c.recv(2048)
    f += msg
    print('got it!')
    return pickle.loads(f) 

def update_clients(dict):
    playernum = len(clients)
    d = {playernum:(random.randint(1,100), random.randint(1,100))}
    clients.update(d)
    print(clients)

def send_clients(dict):
    data = pickle.dumps(dict)
    c.sendall(data)


clients = {}
s.listen(5)      

def update_pos():
    clients.update(get_dict())
    send_clients(clients)
    print(clients)

def game_thread(c):
    while True:
        try:
            send_clients(clients)
            update_pos()
        except:
            break
    print('disconn')
    c.close()

currentPlayer = 0
while True:
    c, addr = s.accept()
    print("Connected to:", addr)
    update_clients(clients)
    print('here')
    start_new_thread(game_thread,(c,))
    print(clients)
    currentPlayer += 1
