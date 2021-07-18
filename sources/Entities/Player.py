import pygame
from sources.Entities.Entity import Entity
from sources.Settings import SETTINGS


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
		if self.rect.x + self.speed > SETTINGS["WIDTH"]:
			self.player.beams.remove(self)
		self.rect.x += self.speed

	def draw(self, window):
		pass

class Player(pygame.sprite.Sprite, Entity):
	def __init__(self, spawner):
		super().__init__()
		self.sounds = {
			'destroyed': pygame.mixer.Sound("assets/sounds/player_destroyed.ogg"),
			'hit': pygame.mixer.Sound("assets/sounds/player_hit.ogg"),
			'shoot': pygame.mixer.Sound("assets/sounds/player_shoot.ogg"),
		}
		for sounds in self.sounds.values():
			sounds.set_volume(SETTINGS['SOUNDS_VOLUME'])
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
		self.ms = 3
		self.attack_speed = 1
		self.score = 0
		self.hp = 3
		self.elapsed_time = 0
		self.group = pygame.sprite.GroupSingle(self)
		self.beams = pygame.sprite.Group()
		self.spawner = spawner

	def destroy(self):
		self.sounds['destroyed'].play()

	def hit(self, enemy_attack=1):
		self.hp -= enemy_attack
		self.sounds['hit'].play()
		if self.hp <= 0:
			self.destroy()

	def up(self):
		if self.rect.y - self.ms > 0:
			self.image = self.images[pygame.K_UP]
			self.velocity_y = -self.ms

	def down(self):
		if self.rect.y < SETTINGS["HEIGHT"] - self.rect.height:
			self.image = self.images[pygame.K_DOWN]
			self.velocity_y = self.ms

	def left(self):
		if self.rect.x - self.ms > 0:
			self.image = self.images[pygame.K_LEFT]
			self.velocity_x = -self.ms

	def right(self):
		if self.rect.x < SETTINGS["WIDTH"] - self.rect.width:
			self.image = self.images[pygame.K_RIGHT]
			self.velocity_x = self.ms

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
			self.beams.add(PlayerBeam(self, self.rect.x + self.rect.width, self.rect.y + (self.rect.height / 2)))
			self.sounds['shoot'].play()
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
		for beam in self.beams:
			beam.update(elapsed_time)
		collide_player_right_enemies = pygame.sprite.groupcollide(self.group, self.spawner.right_enemies_group, False, True)
		collide_player_beam_right_enemies = pygame.sprite.groupcollide(self.beams, self.spawner.right_enemies_group, True, True)
		collide_player_enemies_beams = pygame.sprite.groupcollide(self.group, self.spawner.enemies_beam, False, True)
		if collide_player_right_enemies or collide_player_enemies_beams:
			self.hit()
		if collide_player_beam_right_enemies:
			self.score += 100

	def draw(self, window):
		self.group.draw(window)
		self.beams.draw(window)
