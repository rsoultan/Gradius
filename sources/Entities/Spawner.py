import pygame
from sources.Entities.Entity import Entity
from sources.Entities.RightEnemy import RightEnemy


class Spawner(Entity):
    def __init__(self, level=0):
        super().__init__()
        self.level = level
        self.right_enemies_group = pygame.sprite.Group()
        self.enemies_beam = pygame.sprite.Group()
        self.elapsed_time = 0.0

    def event(self, event):
        pass

    def update(self, elapsed_time):
        self.elapsed_time += elapsed_time
        if self.elapsed_time > 1:
            self.elapsed_time -= 1
            self.right_enemies_group.add(RightEnemy(self.right_enemies_group, self.enemies_beam))
        self.enemies_beam.update(elapsed_time)
        self.right_enemies_group.update(elapsed_time)

    def draw(self, window):
        self.right_enemies_group.draw(window)
        self.enemies_beam.draw(window)
