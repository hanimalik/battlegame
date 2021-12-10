#start with importing pygame and other necessary libraries
import pygame
import random

#Creating tiles and assigning them to different elements.
SAND = 0
DIRT = 1
WATER = 2
WALL = 3
CACTUS_0 = 4
CACTUS_1 = 5
CACTUS_2 = 6
#Colors
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (170, 0 ,0)
GREEN = (60, 179, 113)
BLUE = (30, 144, 255)

#Now we have to create classes for each object that we want
#to display onto the map.
class Cactus:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/cacti/cactus.png'), (75, 75))
        self.X_POS = random.randint(50, 300)
        self.Y_POS = random.randint(50, 450)

class BUILDING:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./sprites/building.png'), (300, 300))
        self.X_POS = 10 
        self.Y_POS = 0

#Number of Cacti that spawn
num_of_cacti = 5
cacti = [Cactus() for x in range (num_of_cacti)]

#We must assign our tiles to the correct texture pack
TEXTURES = {
    SAND: pygame.image.load('./textures/sand.png'),
    DIRT: pygame.image.load('./textures/dirt.png'),
    WATER: pygame.image.load ('./textures/water.png'),
    CACTUS_0: pygame.image.load('./textures/cacti/cactus.png'),
}
#Tiles that will be displayed
GRID = [
    [SAND, SAND, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, SAND, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND],
    [SAND, SAND, SAND, SAND, WATER, WATER, WATER, WATER, WATER, WATER, WATER, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND, SAND]
]

#Dimensions of the game, set the display, configuration
TILESIZE = 50
MAPWIDTH = 20
MAPHEIGHT = 10
pygame.init()
pygame.display.set_caption('The Final Battle')

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))





    




