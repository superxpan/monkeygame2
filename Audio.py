import pygame


class AudioManager:
    def __init__(self):
        pygame.mixer.music.load("./sounds/background_music.mp3")
        self.fire_sound = pygame.mixer.Sound("./sounds/A_oh_SE.wav")
        self.banana_sound = pygame.mixer.Sound("./sounds/coin_SE.wav")
        pygame.mixer.set_num_channels(8)
    def play_music(self):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def stop_music(self):
        music = pygame.mixer.music.stop()

    def play_sound(self, sound_name,rect):
        if sound_name == 'banana':
            channel = self.banana_sound.play()
        elif sound_name == 'fire':
            channel = self.fire_sound.play()
        else:
            channel = None

        if channel is not None:
            left, right = self.stero_pan(rect)
            channel.set_volume(left, right)

    def stero_pan(self,rect):
        right_volume = rect.x / 800
        left_volume = 1.0 - right_volume
        return (left_volume, right_volume)
