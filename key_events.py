import pygame
import sys

#Library for all key events


#Image path for Han
img_path = './sprites/han/han_'
#f_path = 
#b_path = 
r_path = img_path + 'r'
l_path = img_path + 'l'

#f_images = [f_path+str(f)+'.png' for f in range()]
#b_images = [b_path+str(b)+'.png' for b in range()]
r_images = [r_path+str(r)+'.png' for r in range(7)]
l_images = [l_path+str(l)+'.png' for l in range(7)]

#Image path for Wolf 
img_path = './sprites/wolfie/wolfie_'
wolfie_f_path = img_path + 'f'
wolfie_b_path = img_path + 'b'
wolfie_r_path = img_path + 'r'
wolfie_l_path = img_path + 'l'

wolfie_f_images = [wolfie_f_path +str(f) + '.png' for f in range(6)]
wolfie_b_images = [wolfie_b_path + str(b) + '.png' for b in range(6)]
wolfie_r_images = [wolfie_r_path + str(r) + '.png' for r in range(5)]
wolfie_l_images = [wolfie_l_path + str(l) + '.png' for l in range(5)]


class KeyEvents:
    def __init__(self, PLAYER):
        self.PLAYER = PLAYER
        self.counter = 0
        self.wolfie_counter = 0
        self.wolfie_counter_lr = 0
        self.movement = .25
        self.blasts = 0
        
    def global_events(self):
        if self.PLAYER.TRANSFORM:
            self.movement = .5
        else:
            self.movement = .25
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def key_down(self):
        self.PLAYER.PLAYER_POS[1] += self.movement
        self.PLAYER.DIRECTION = 'd'

        #self.PLAYER.SPRITE_POS = pygame.image.load(f_images[self.counter])
        #self.counter = (self.counter + 1) % len(f_images)

        #if self.PLAYER.TRANSFORM:
            #self.PLAYER.WOLFIE = pygame.image.load(wolfie_f_images[self.wolfie_counter])
            #self.wolfie_counter = (self.wolfie_counter + 1) % len(wolfie_f_images)
    
    def key_up(self):
        self.PLAYER.PLAYER_POS[1] -= self.movement
        self.PLAYER.DIRECTION = 'u'

        #self.PLAYER.SPRITE_POS = pygame.image.load(b_images[self.counter])
        #self.counter = (self.counter + 1) % len(b_images)

        #if self.PLAYER.TRANSFORM:
            #self.PLAYER.WOLFIE = pygame.image.load(wolfie_b_images[self.wolfie_counter])
            #self.wolfie_counter = (self.wolfie_counter + 1) % len(wolfie_b_images)

    def key_left(self):
        self.PLAYER.PLAYER_POS[0] -= self.movement
        self.PLAYER.DIRECTION = 'l'

        #self.PLAYER.SPRITE_POS = pygame.image.load(l_images[self.counter])
        #self.counter = (self.counter + 1) % len(l_images)

        #if self.PLAYER.TRANSFORM:
        #self.PLAYER.WOLFIE = pygame.image.load(wolfie_l_images[self.wolfie_counter_lr])
        #self.wolfie_counter_lr = (self.wolfie_counter_lr + 1) % len(wolf_l_images)

    def key_right(self):
        self.PLAYER.PLAYER_POS[0] += self.movement
        self.PLAYER.DIRECTION = 'r'

        #self.PLAYER.SPRITE_POS = pygame.image.load(r_images[self.counter])
        #self.counter = (self.counter + 1) % len(r_images)

        #if self.PLAYER.TRANSFORM:
            #self.PLAYER.WOLFIE = pygame.image.load(wolfie_r_images[self.wolfie_counter_lr])
            #self.wolfie_counter_lr = (self.wolfie_counter_lr + 1) % len(wolfie_r_images)

    def key_space(self):
        if self.PLAYER_WEAPON:
            self.PLAYER.PLAYER_INV.remove(self.PLAYER.WEAPON)
            self.PLAYER.WEAPON.PLACED = True

            #Drop weapons at current location
            if self.PLAYER.DIRECTION == 'd':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER_POS[0]
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER_POS[1] - 1
            elif self.PLAYER.DIRECTION == 'u':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER.POS[0]
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER.POS[1] + 1
            elif self.PLAYER.DIRECTION == 'r' :
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER.POS[0] - 1
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER.POS[1]
            elif self.PLAYER.DIRECTION == 'l':
                self.PLAYER.WEAPON.POS[0] = self.PLAYER.PLAYER.POS[0] + 1
                self.PLAYER.WEAPON.POS[1] = self.PLAYER.PLAYER.POS[1]

        self.PLAYER.WEAPON = False

    def key_w(self):
        self.PLAYER_TRANSFORMING()






