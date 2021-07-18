import pygame

from sources.Entities.Button import Button
from sources.Entities.Player import Player
from sources.Entities.Scene import GameSceneIds, create_scene, switch_scene
from sources.Settings import SETTINGS


class Game():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Pygame shoot them up")
		pygame.key.set_repeat(1, 1)
		self.clock = pygame.time.Clock()
		self.seconds = 3590
		self.window = None
		self.font = pygame.font.Font("assets/fonts/ArcadeAlternate.ttf", 32)
		self.scene = create_scene(self, GameSceneIds.MAIN_MENU)
		self.is_running = True

	def run(self):
		self.window = pygame.display.set_mode((SETTINGS["WIDTH"], SETTINGS['HEIGHT']))
		pygame.mixer.music.set_volume(SETTINGS['MUSICS_VOLUME'])
		while self.is_running:
			self.event()
			self.update()
			self.draw(self.window)

	def event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_running = False
				break
			self.scene.event(event)

	def update(self):
		dt = self.clock.tick(SETTINGS["FPS"]) / 1000
		self.seconds += dt
		pygame.display.flip()
		self.scene.update(dt)
		if self.scene.id == GameSceneIds.GAME:
			for entity in self.scene.entities:
				if isinstance(entity, Player):
					if entity.hp <= 0:
						switch_scene(self, GameSceneIds.MAIN_MENU)

	def draw(self, window):
		self.scene.draw(window)