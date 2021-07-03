import pygame

from .Scene import GameSceneIds, create_scene
from .Button import Button
from .Settings import SETTINGS

class Game():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Pygame shoot them up")
		pygame.key.set_repeat(1, 1)
		self.clock = pygame.time.Clock()
		self.dt = 0
		self.window = None
		self.font = pygame.font.SysFont("arial", 32)
		self.scene = create_scene(self, GameSceneIds.MAIN_MENU)
		self.is_running = True
		self.nb_loop_ingame = 0

	def run(self):
		self.window = pygame.display.set_mode(SETTINGS["resolution"])
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
		total_seconds = self.nb_loop_ingame // SETTINGS["fps"]
		seconds = total_seconds % 60
		minutes = total_seconds // 60
		hours = total_seconds // 3600
		self.nb_loop_ingame += 1
		pygame.display.set_caption(f"Game time: {hours}:{minutes}:{seconds} FPS: {int(self.clock.get_fps())}")
		self.dt = self.clock.tick(SETTINGS["fps"])
		pygame.display.flip()
		self.scene.update(self.dt)

	def draw(self, window):
		self.window.fill((0, 0, 0))
		self.scene.draw(window)