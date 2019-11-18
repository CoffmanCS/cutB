# This is where the py game code will go. 
import pygame
 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 20, 91)
GREEN = (39, 204, 110)
RED = (39, 130, 204)
BLUE = (255, 118, 33)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    super().__init__()
    width = 40
    height = 60
    self.image = pygame.Surface([width, height])
    self.image.fill(RED)
    
def main():
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)