import pygame
from pygame.locals import *
import random

class Monkey(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("./images/monkey.png").convert_alpha()
        self.__current_frame__ = 0
        self.scale = 0.6
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image=pygame.transform.rotozoom(self.image1,0,self.scale)
        self.rect = self.image.get_rect()
        self.isCollided = False
        self.rect.width = self.rect.width/2 - 40
        self.rect.height = self.rect.height/2
        self.rect.x = self.pos_x + 15
        self.rect.y = self.pos_y

        self.num_frame_per_row = 2
        self.num_frame_per_col = 2
        self.frame_height = self.image.get_height()/self.num_frame_per_col
        self.frame_width = self.image.get_width()/self.num_frame_per_row


    def update_position(self):
        self.__current_frame__ = (self.__current_frame__+1)%12
        self.rect.x = self.pos_x + 15
        self.rect.y = self.pos_y

    def show(self, screen):
        y = int(self.__current_frame__/6)*self.frame_height
        x = (int(self.__current_frame__/3)%2)*self.frame_width
        screen.blit(self.image, dest=(self.pos_x,self.pos_y), area=(x, y, self.frame_width, self.frame_height))

    def move_right(self):
        if self.pos_x < 700:
            self.pos_x += 18

    def move_left(self):
        if self.pos_x > 0:
            self.pos_x -= 18

class Cloud:
    def __init__(self, pos_x, pos_y, dx, scale):
        self.image = pygame.image.load("./images/cloud.png").convert_alpha()
        self.__current_frame__ = 0
        self.scale = scale
        self.image=pygame.transform.rotozoom(self.image,0,self.scale)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.pos_x_offset = 300

    def update_position(self):
        self.__current_frame__ = (self.__current_frame__+1)%8
        self.pos_x = (self.pos_x+self.dx)%(700+self.pos_x_offset)

    def show(self, screen):
        ax = 0*self.scale
        ay = int(self.__current_frame__/4)* 64 * self.scale
        screen.blit(self.image, dest=(self.pos_x-self.pos_x_offset,self.pos_y), area=(ax,ay,128*self.scale,64*self.scale))


class Fire:
    def __init__(self,pos_x, pos_y, dy):
        self.image= pygame.image.load("./images/fire.png").convert_alpha()
        self.pos_x = random.randint(50, 600)
        self.pos_y = pos_y - random.randint(100, 300)
        self.scale = 0.2
        self.dy = dy
        self.__current_frame__ = 0
        self.image=pygame.transform.rotozoom(self.image,0,self.scale)
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width/4
        self.rect.height = self.rect.height/2 - 30
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.num_frame_per_row = 4
        self.num_frame_per_col = 2
        self.frame_height = self.image.get_height()/self.num_frame_per_col
        self.frame_width = self.image.get_width()/self.num_frame_per_row



    def update_position(self):
        self.__current_frame__ = (self.__current_frame__+1)%8
        self.pos_y = self.pos_y+self.dy
        if self.pos_y >= 800:
            self.pos_x = random.randint(50, 600)
            self.pos_y = -random.randint(200, 500)
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def show(self, screen):
        y = int(self.__current_frame__/4)*self.frame_height
        x = (int(self.__current_frame__/1)%4)*self.frame_width
        screen.blit(self.image, dest=(self.pos_x,self.pos_y), area=(x, y, self.frame_width, self.frame_height))

class Banana(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, dy, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/banana.png").convert_alpha()
        self.pos_x = random.randint(50, 600)
        self.pos_y = pos_y - random.randint(100, 300)
        self.dy = dy
        self.scale = 1
        self.rect = self.image.get_rect()
        self.rect.y = self.pos_y
        self.rect.x = self.pos_x
        self.name = name
        self.rect.height = self.rect.height - 10

    def update_position(self):
        self.pos_y = self.pos_y+self.dy
        if self.pos_y >= 800:
            self.pos_x = random.randint(50, 600)
            self.pos_y = -random.randint(200, 500)
        self.rect.y = self.pos_y
        self.rect.x = self.pos_x

    def show(self, screen):
        screen.blit(self.image, dest=(self.pos_x,self.pos_y), area=(0,0,66,82))

def create_multiple_sprites():
    monkey = Monkey(330,640)
    cloud1 = Cloud(200, 0, 2, 1.3)
    cloud2 = Cloud(400, 50, 4, 2)
    cloud3 = Cloud(700, 10, 4, 0.8)
    banana = Banana(350,0,8, 'b0')
    banana1 = Banana(100,0,10, 'b1')
    banana2 = Banana(100,0,10, 'b3')
    fire = Fire(100,0,15)
    return monkey,cloud1,cloud2,cloud3,banana,banana1,banana2,fire

def make_group(sprites:list):
    group = pygame.sprite.Group()
    for s in sprites:
        group.add(s)
    return group

def update_all_sprite_positions(sprites:list):
    for s in sprites:
        s.update_position()

def show_all_sprites(sprites:list, screen):
    for s in sprites:
        s.show(screen)
