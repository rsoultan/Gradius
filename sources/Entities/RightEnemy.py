from random import randint

import pygame
from sources.Entities.Entity import Entity
from sources.Settings import SETTINGS


class EnemyBeam(pygame.sprite.Sprite, Entity):
	def __init__(self, enemy, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/images/enemy_beam.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		self.speed = enemy.speed * 2
		self.enemy = enemy

	def event(self, event):
		pass

	def update(self, elapsed_time):
		if self.rect.x - self.speed < -self.rect.width:
			self.enemy.beam_group.remove(self)
		self.rect.x -= self.speed

	def draw(self, window):
		pass

class RightEnemy(pygame.sprite.Sprite, Entity):
	def __init__(self, enemies_group, beam_group):
		super().__init__()
		self.image = pygame.image.load("assets/images/right_enemy.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = SETTINGS['WIDTH']
		self.rect.y = randint(40, 525)
		self.speed = randint(6, 12)
		self.elapsed_time = 0.0
		self.enemies_group = enemies_group
		self.beam_group = beam_group

	def event(self, event):
		pass

	def update(self, elapsed_time):
		self.elapsed_time += elapsed_time
		if self.elapsed_time > 1:
			self.elapsed_time -= 1
			self.beam_group.add(EnemyBeam(self, self.rect.x - (self.rect.width / 2), self.rect.y + (self.rect.height / 2)))
		if self.rect.x < -self.rect.width:
			self.enemies_group.remove(self)
		self.rect.x -= self.speed

	def draw(self, window):
		pass
