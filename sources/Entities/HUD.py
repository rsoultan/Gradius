import pygame
from sources.Entities.Entity import Entity


class HUD(Entity):
    def __init__(self, player, font):
        self.player = player
        self.font = font

    def event(self, event):
        pass

    def update(self, elapsed_time):
        pass

    def draw(self, window):
        window.blit(self.font.render(f"Health {self.player.hp} Movement Speed {self.player.ms} Attack Speed {self.player.attack_speed} Score {self.player.score}", 1, (255,255,255)), (20, 20))
