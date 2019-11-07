#Drew Arocha 2019 
#cutB verision 1.00
#TO-DO:
# -Implement a way to know whos player1/2
# -Eff
# -Connect over wifi
# -Handle for Buffering and Blocking?
# -Test on windows bc I may need to use selector not threads

import pygame
import socket


#setting up the client side socket with IPV4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.84.129.230'
port = 5555

#pygame window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNum = 0


#handles connecting to the server bc sometimes it can throw an error
def connect():
        try:
            s.connect((host, port))
            return s.client.recv(2048).decode()
        except:
            pass

#handles sending data to server
def send(data):
    try:
        #you have to turn data into bytes before sending thru a server so thats what this is doing
        s.send(str.encode(data))
        return s.recv(2048).decode()
    except socket.error as e:
         print(e)


#sets up the simple test square
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

#you cant send tuples so you have to convert to str/int
#this one is for well, reading data. 
# it allows data we recv to be read as ints for use in the pos of the player
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

#same as above but this one creates the x and y for sending
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(window, player, player2):
    window.fill((255,255,255))
    pygame.mouse.set_visible(True)
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


#I feel like all this is understandable, if not lmk
def main():
    run = True
    p = Player(100,100,100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,0,255))
    connect()
    while run:
        #s.connect((host,port))
        p2Pos = read_pos(send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                p.move()
                send(make_pos((p.x, p.y)))
                print(pygame.mouse.get_pos())

             
        redrawWindow(window, p, p2)

main()