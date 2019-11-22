#Drew Arocha 2019
#cutB version 1.02
import pygame
import socket
import pickle
from threading import Thread
import errno
import sys
import time
#setting up the client side socket with IPV4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234

#pygame window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNum = 0

def connect():
        try:
            s.connect((host, port))
        except:
            pass
#Recieves the dict
def get_dict():     
    f = b''
    try:

        msg = s.recv(2048)
        f += msg
        print('got from client', pickle.loads(f))
        return pickle.loads(f) 


    except EOFError as e:
        return {}

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        
    def move(self):
        self.x , self.y = pygame.mouse.get_pos()
        self.update()
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(window, player, player2):
    window.fill((255,255,255))
    pygame.mouse.set_visible(True)
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

d = {}
key = len(d) 
def make_pos(dict):
    d.update(dict)
    print(d)

def send_pos(dict):
    data = pickle.dumps(dict)
    s.sendall(data)
    print('sent!')

def main():
    run = True
    p = Player(100,100,100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,0,255))
    connect()
    d = get_dict()
    print(d)

    while run:
        #Sets up blocking &updates the dict
        try:
            s.setblocking(False)
            d.update(get_dict())
        except socket.error as e:   #can throw an error so we check for that
            if e == "[Errno 35] Resource temporarily unavailable":
                time.sleep(0)
                continue
                raise e

        make_pos(d)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                p.move()
                d.update({len(d)-1: pygame.mouse.get_pos()})
                send_pos(d)


        redrawWindow(window, p, p2)


main()
