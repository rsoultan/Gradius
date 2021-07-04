import pygame

from .Settings import SETTINGS
from .Entity import Entity

class PlayerBeam(pygame.sprite.Sprite, Entity):
	def __init__(self, player, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/images/player_beam.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 24
		self.player = player

	def event(self, event):
		pass

	def update(self, elapsed_time):
		if self.rect.x + self.speed > SETTINGS["resolution"][0]:
			self.player.attacks_group.remove(self)
		self.rect.x += self.speed

	def draw(self, window):
		window.draw

class Player(pygame.sprite.Sprite, Entity):
	def __init__(self):
		super().__init__()
		self.images = {
			pygame.K_UP: pygame.image.load("assets/images/player/player_up.png").convert_alpha(),
			pygame.K_DOWN: pygame.image.load("assets/images/player/player_down.png").convert_alpha(),
			pygame.K_LEFT: pygame.image.load("assets/images/player/player_still.png").convert_alpha(),
			pygame.K_RIGHT: pygame.image.load("assets/images/player/player_still.png").convert_alpha()
		}
		self.moves = {
			pygame.K_UP: False,
			pygame.K_DOWN: False,
			pygame.K_LEFT: False,
			pygame.K_RIGHT: False
		}
		self.image = self.images[pygame.K_RIGHT]
		self.rect = self.image.get_rect()
		self.rect.x = 180
		self.rect.y = 360
		self.velocity_x = 0
		self.velocity_y = 0
		self.move_speed = 3
		self.elapsed_time = 0
		self.attack_speed = 500
		self.player_group = pygame.sprite.GroupSingle()
		self.player_group.add(self)
		self.attacks_group = pygame.sprite.Group()

	def up(self):
		if self.rect.y - self.move_speed > 0:
			self.image = self.images[pygame.K_UP]
			self.velocity_y = -self.move_speed

	def down(self):
		if self.rect.y < SETTINGS["resolution"][1] - self.rect.height:
			self.image = self.images[pygame.K_DOWN]
			self.velocity_y = self.move_speed

	def left(self):
		if self.rect.x - self.move_speed > 0:
			self.image = self.images[pygame.K_LEFT]
			self.velocity_x = -self.move_speed

	def right(self):
		if self.rect.x < SETTINGS["resolution"][0] - self.rect.width:
			self.image = self.images[pygame.K_RIGHT]
			self.velocity_x = self.move_speed

	def event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key in self.moves:
				self.moves[event.key] = True
		if event.type == pygame.KEYUP:
			if event.key in self.moves:
				self.moves[event.key] = False

	def update(self, elapsed_time):
		self.elapsed_time += elapsed_time
		self.velocity_x = 0
		self.velocity_y = 0
		if self.elapsed_time > self.attack_speed:
			self.elapsed_time -= self.attack_speed
			self.attacks_group.add(PlayerBeam(self, self.rect.x + self.rect.width, self.rect.y + (self.rect.height / 2)))
		if self.moves[pygame.K_UP] and not self.moves[pygame.K_DOWN]:
			self.up()
		if self.moves[pygame.K_DOWN] and not self.moves[pygame.K_UP]:
			self.down()
		if self.moves[pygame.K_LEFT] and not self.moves[pygame.K_RIGHT]:
			self.left()
		if self.moves[pygame.K_RIGHT] and not self.moves[pygame.K_LEFT]:
			self.right()
		if not self.moves[pygame.K_UP] and not self.moves[pygame.K_DOWN] and not self.moves[pygame.K_LEFT] and not self.moves[pygame.K_RIGHT]:
			self.image = self.images[pygame.K_RIGHT]
		self.rect = pygame.Rect(self.rect.x + self.velocity_x, self.rect.y + self.velocity_y, self.rect.width, self.rect.height)
		for beam in self.attacks_group:
			beam.update(elapsed_time)

	def draw(self, window):
		self.player_group.draw(window)
		self.attacks_group.draw(window)