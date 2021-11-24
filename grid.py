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
        self.SPRITE = pygame.transform.scale(pygame.image.load('/Users/hanimalik/Downloads/Cactus/Cactus.png'))
        self.X_POS = random.randint(50, 300)
        self.Y_POS = random.randint(50, 450)

class Building:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('/Users/hanimalik/Downloads/Building/village_red.png'))
        self.X_POS = 6
        self.Y_POS = 1

#Number of Cacti that spawn
num_of_cacti = 10
cacti = [Cactus() for x in range (num_of_cacti)]

#We must assign our tiles to the correct texture pack
SAND = pygame.image.load('./textures/sand.png')
DIRT = pygame.image.load('./textures/dirt.png')
WATER = pygame.image.load ('./textures/water.png')



    




