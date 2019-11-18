#Drew Arocha 2019
#cutB version 1.00
import socket
from _thread import *
import sys

server = '10.84.129.230' #note to self: change this to ip
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

s.listen(5)         

#this is so we can have multiple clients on the same server     
def threaded_client(c, player):
    c.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(c.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            c.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    c.close()

#currentPlayer has no use right now
#it should be used to track whos who but idc about that right now
currentPlayer = 0
while True:
    c, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (c, currentPlayer))
    currentPlayer += 1