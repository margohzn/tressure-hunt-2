import pygame 
import random
import time 
from pygame.locals import * 

screen_width = 900
screen_height = 800 


def change_background(image):
    image = pygame.image.load(image)
    bg = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(bg, (0,0))




pygame.init()
pygame.display.set_caption("Tressure Hunt")
screen = pygame.display.set_mode([screen_width, screen_height])


#player sprite  (pirate is the player sprite)

class Pirate(pyagme.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pirate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

#player sprite (stone is the player sprite)

class Stone(pygame.sprite.Sprite):
    def __init__(self, img_name):
        super().__init()
        self.img = pygame.image.load(img_name).convert_alpha()
        self.img = pygame.transform.scale(self.img, (30,30))
        self.rect = self.img.get_rect()


# list of image names for stone class 
images = ["images/stone1.png", "images/stone2.png", "images/stone3.png"]

# creating spirte groups (like in flappybird with the pipes and the birds)
stone_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# creating stone sprites object
for i in range(100):
    stone = Stone(random.choice(images))
    stone.rect.x = random.randrange(screen_width)
    stone.rect.y = random.randrange(screen_height)
    # adding stone sprite to the groups
    stone_group.add(stone)


#creat pirate sprite object
pirate = Pirate()
all_sprites.add(pirate)




