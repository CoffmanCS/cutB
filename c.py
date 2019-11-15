#Drew Arocha 2019
#cutB version 1.01
import pygame
import socket
import pickle

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
            return s.client.recv(2048).decode()
        except:
            pass

#Recieves the dict
def get_dict():     
    f = b''
    msg = s.recv(2048)
    f += msg
    return pickle.loads(f) 

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
    print(dict)
    d.update(dict)
    print(d)
    print(d.get(len(d)-1))
    
def send_pos(dict):
    data = pickle.dumps(dict)
    s.send(data)


def main():
    run = True
    p = Player(100,100,100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,0,255))
    connect()
    d = get_dict()
    make_pos(d)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                p.move()
                d.update({len(d)-1: pygame.mouse.get_pos()})
                send_pos(d)
                print(d)
                print(pygame.mouse.get_pos())


        redrawWindow(window, p, p2)

main()