import pygame
from pygame.locals import *
import time
import random
from Sprites import *
from Audio import *


class Score:
    def __init__(self,score):
        self.score = score
        self.font = pygame.font.Font(None,50)


    def add_one(self):
        self.score += 1

    def show(self, screen):
        self.text = self.font.render(f"SCORE:{self.score}",True,('white'),("darkgreen"))
        screen.blit(self.text,(0,30))

def create_screen():
    screen = pygame.display.set_mode([750,800])
    pygame.display.set_caption("fire")
    return screen


def load_background_image():
    background = pygame.image.load("./images/background.png").convert()
    background2 = pygame.transform.rotozoom(background,0,0.5)
    return background2

def load_game_over_image():
    gameover = pygame.image.load("./images/gameover.png")
    gameover = pygame.transform.rotozoom(gameover,0,2)
    return gameover



def main():
    pygame.init()

    screen = create_screen()
    background2 = load_background_image()
    gameover = load_game_over_image()
    monkey,cloud1,cloud2,cloud3,banana,banana1,banana2,fire = create_multiple_sprites()
    audio = AudioManager()
    audio.play_music()
    groups = make_group([banana, banana1, banana2])
    score = Score(0)
    all_sprites = [cloud3,cloud1,banana,banana1,banana2,monkey,fire,cloud2]
    hit_fire = None

    while True:
        screen.blit(background2,(0,0))
        show_all_sprites(all_sprites, screen)
        score.show(screen)
        time.sleep(0.1)

        if hit_fire: # if game over
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            screen.blit(gameover,(100,250))

        else: # not game over
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                monkey.move_left()
            if keys[pygame.K_d]:
                monkey.move_right()

            hit_banana = pygame.sprite.spritecollideany(monkey,groups)
            if hit_banana:
                monkey.isCollided = True
                hit_banana.pos_y = -50
                hit_banana.pos_x = random.randint(50, 600)
                audio.play_sound('banana', monkey.rect)
                score.add_one()

            hit_fire = pygame.sprite.collide_rect(monkey,fire)
            if hit_fire:
                monkey.isCollided = True
                audio.play_sound('fire', monkey.rect)
                audio.stop_music()
                #music = pygame.mixer.music.stop()

            update_all_sprite_positions(all_sprites)

        pygame.display.update()


if __name__ == '__main__':
    main()
