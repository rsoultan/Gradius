import pygame
from sources.Entities.Entity import Entity
from sources.Settings import SETTINGS


class BackgroundScrolling(pygame.sprite.Sprite, Entity):
    def __init__(self):
        super().__init__()
        self.music = pygame.mixer.music.load("assets/sounds/game.ogg")
        pygame.mixer.music.play()
        self.image = pygame.image.load("assets/images/game_background.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rel_x = self.rect.x % self.rect.width

    def event(self, event):
        pass

    def update(self, elapsed_time):
        self.rect.x -= 1
        self.rel_x = self.rect.x % self.rect.width
        if self.rect.x < -self.rect.width:
            self.rect.x = 0

    def draw(self, window):
        window.blit(self.image, (self.rel_x - self.rect.width, 0))
        if self.rel_x < SETTINGS['WIDTH']:
            window.blit(self.image, (self.rel_x, 0))
