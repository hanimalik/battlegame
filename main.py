import pygame, sys
from pygame.display import toggle_fullscreen
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

#Defining game objects and their instances
PLAYER = heroes.HAN()
key_events = KeyEvents(PLAYER)
STAFF = items.STAFF()
#SWORD = items.SWORD()
#SHIELD = items.SHIELD()
BOSS = enemies.BOSS()
PORTAL = enemies.PORTAL()
BUILDING = BUILDING()
OWNER = heroes.OWNER()

#Sorting game objects into groups
GAME_ITEMS = [STAFF]
GAME_WEAPONS = [STAFF]
BANDIT_LIST = []
blasts_list = []

#Fonts for health, inv,
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)
portal_path = './textures/portal/portal_'
portal_images = [portal_path +str(p) + '.png' for p in range(1, 7)]

#Timed Events

# BOSS MOVEMENT
pygame.time.set_timer(USEREVENT, 400)
# SPAWN BANDITS
pygame.time.set_timer(USEREVENT + 1, 7500)
#PORTAL FRAMES
pygame.time.set_timer(USEREVENT + 2, 400)
#MOVE BANDITS
pygame.time.set_timer(USEREVENT + 3, 1000)
#BLAST TRAVELS ON PATH
pygame.time.set_timer(USEREVENT + 4, 100)

GAME_OVER = False

#Game Loop
while not GAME_OVER:

    BOSS_VUNERABLE_IF = [bandit for bandit in BANDIT_LIST if bandit.APPEAR == True]

    if len(BOSS_VUNERABLE_IF) < 1:
        BOSS.VUNERABLE = True
    else:
        BOSS.VUNERABLE = False

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == QUIT:
            key_events.quit()

        if keys[K_w] and keys[K_t]:
            key_events.key_w()


        #Move Right
        if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
            key_events.key_right()

        #Move Left
        if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
            key_events.key_left()
        
        #Move Up
        if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
            key_events.key_up()
        
        #Move Down
        if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
            key_events.key_down()

        #Place down items
        if (keys[K_SPACE]):
            key_events.key_space()

        #Blasts from Staff
        if (keys[K_f]):
            if PLAYER.WEAPON == STAFF:
                blasts_list.append(heroes.BLAST(math.ceil(PLAYER.PLAYER_POS[0]), math.ceil(PLAYER.PLAYER_POS[1]), PLAYER.DIRECTION))


        #Timed Events

        #Boss Portal Movement
        if (event.type == USEREVENT):
            if PORTAL.FRAME < 5:
                PORTAL.FRAME += 1
            else:
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                PORTAL.POS = [x, y]
                BOSS.BOSS_POS = [x, y]
                PORTAL.FRAME = 1

        #Generator for Bandit entities
        elif (event.type == USEREVENT + 1):
            NEW_BANDIT = enemies.BANDIT()
            NEW_BANDIT.PORTAL = enemies.PORTAL()
            BANDIT_LIST.append(NEW_BANDIT)

        #Bandit Portal Generator
        elif (event.type == USEREVENT + 2):
            for bandit in BANDIT_LIST:
                if bandit.PORTAL_APPEAR and bandit.PORTAL.FRAME < 5:
                    bandit.PORTAL.FRAME += 1
                elif not bandit.SUMMONED:
                    bandit.PORTAL_APPEAR = False
                    bandit.APPEAR = True
                    bandit.SUMMONED = True
                    bandit.POS = [bandit.PORTAL.POS[0], bandit.PORTAL.POS[1]]

        #Making bandits hunt down Han, cause damage
        elif (event.type == USEREVENT + 3):
            for bandit in BANDIT_LIST:
                if bandit.APPEAR:
                    if PLAYER.PLAYER_POS == bandit.POS:
                        PLAYER.HEALTH -= 10
                    for coordinate in range(len(bandit.POS)):
                        if PLAYER.PLAYER_POS[coordinate] > bandit.POS[coordinate]:
                            bandit.POS[coordinate] += 1
                        else:
                            bandit.POS[coordinate] -= 1
        #BLASTS MOVEMENT ANIMATION
        elif (event.type == USEREVENT + 4):
            for blast in blasts_list:
                if blast.DIRECTION == 'd':
                    blast.POS[1] += 1
                elif blast.DIRECTION == 'u':
                    blast.POS[1] -= 1
                elif blast.DIRECTION == 'l':
                    blast.POS[0] -= 1
                elif blast.DIRECTION == 'r':
                    blast.POS[0] += 1
    
        #PICKUP ITEMS
        for item in GAME_ITEMS:
            if PLAYER.PLAYER_POS == item.POS and item.PLACED:
                PLAYER.PLAYER_INV.append(item)
                item.PLACED = False
                if item in GAME_WEAPONS:
                    PLAYER.WEAPON = item

    '''
    Rendering Grid, Sprites and Views
    '''
    #Render Game Grid
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
    
    #Render Han
    if PLAYER.TRANSFORM:
        DISPLAYSURFACE.blit(PLAYER.WOLFIE, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
    else:
        DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
    
    #Render Building
    DISPLAYSURFACE.blit(BUILDING.SPRITE, (BUILDING.X_POS*TILESIZE, BUILDING.Y_POS*TILESIZE))

    #RENDER OWNER
    OWNER.APPEARED = True
    if OWNER.APPEARED:
        if PLAYER.TRANSFORM:
            DISPLAYSURFACE.blit(OWNER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE + 20, PLAYER.PLAYER_POS[1]*TILESIZE + 35))
        else:
            DISPLAYSURFACE.blit(OWNER.SPRITE_POS, (BUILDING.X_POS*TILESIZE, BUILDING.Y_POS*TILESIZE))

    #RENDER ARMED ITEMS FOR SPRITE
    if PLAYER.WEAPON:
        DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    #Render bandits and portal
    for bandit in BANDIT_LIST:
        if bandit.PORTAL_APPEAR:
            DISPLAYSURFACE.blit(pygame.image.load(portal_images[bandit.PORTAL.FRAME]), (bandit.PORTAL.POS[0]*TILESIZE, bandit.PORTAL.POS[1]*TILESIZE))
        if bandit.APPEAR:
            DISPLAYSURFACE.blit(bandit.BANDIT, (bandit.POS[0]*TILESIZE, bandit.POS[1]*TILESIZE))
    
    #Render items
    for item in GAME_ITEMS:
        if item.PLACED == True:
            DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))
    
    #RENDER BLASTS
    for blast in blasts_list:
        if blast.POS == BOSS.BOSS_POS and BOSS.VUNERABLE:
            print('BOSS HEALTH', BOSS.HEALTH)
            BOSS.HEALTH -= 10
        for bandit in BANDIT_LIST:
            if blast.POS == bandit.POS:
                bandit.APPEAR = False
                BANDIT_LIST.remove(bandit)
                blasts_list.remove(blast)
        if blast.POS[0] > MAPWIDTH or blast.POS[0] < 0 or blast.POS[1] > MAPHEIGHT or blast.POS[1] < 0:
                blasts_list.remove(blast)

        DISPLAYSURFACE.blit(blast.IMAGE, (blast.POS[0]*TILESIZE, blast.POS[1]*TILESIZE))
    
    #Render Player inventory
    INVENTORY_POSITION = 250
    for item in PLAYER.PLAYER_INV:
        DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
        INVENTORY_POSITION += 10
        INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
        DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+15))
        INVENTORY_POSITION += 100

    #Render Han Health Bar
    PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('YOUR HEALTH:', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT+TILESIZE-500))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.HEALTH), True, GREEN, BLACK), (225, MAPHEIGHT+TILESIZE - 500))

    #Render Boss Health Bar
    BOSS_HEALTH_BAR_TEXT = HEALTHFONT.render('ENEMY HEALTH:', True, RED, BLACK)
    DISPLAYSURFACE.blit(BOSS_HEALTH_BAR_TEXT, (650, MAPHEIGHT*TILESIZE-500))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(BOSS.HEALTH), True, RED, BLACK), (900, MAPHEIGHT*TILESIZE-500))

    #Render Cacti
    for cactus in sorted(cacti, key=lambda t: t.Y_POS):
        DISPLAYSURFACE.blit(cactus.SPRITE, (cactus.X_POS, cactus.Y_POS))
    
    #Render Boss and Portal
    DISPLAYSURFACE.blit(pygame.image.load(portal_images[PORTAL.FRAME]), (BOSS.BOSS_POS[0]*TILESIZE, BOSS.BOSS_POS[1]*TILESIZE))
    DISPLAYSURFACE.blit(BOSS.BOSS, (BOSS.BOSS_POS[0]*TILESIZE, BOSS.BOSS_POS[1]*TILESIZE))

    pygame.display.update()
    
    if BOSS.HEALTH <= 0:
        GAME_OVER = True
        print('GAME OVER, VICTORY!')

    if PLAYER.HEALTH <= 0:
        GAME_OVER = True
        print('GAME OVER, DEFEATED')


#END OF GAME LOOP
