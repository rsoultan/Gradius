from enum import Enum

import pygame

from .Button import Button
from .Entity import Entity
from .Player import Player


class GameSceneIds(Enum):
	MAIN_MENU = 0
	GAME = 1
	GAME_OVER = 2

class Scene(Entity):
    def __init__(self, id, entities):
        self.id = id
        self.entities = entities

    def event(self, event):
        for entity in self.entities:
            entity.event(event)

    def update(self, elapsed_time):
        for entity in self.entities:
            entity.update(elapsed_time)

    def draw(self, window):
        for entity in self.entities:
            entity.draw(window)

def switch_scene(*argv):
    game = argv[0][0]
    next_scene_id = argv[0][1]
    game.scene = create_scene(game, next_scene_id)

def create_scene(game, scene_id):
    if scene_id == GameSceneIds.MAIN_MENU:
        entities = [
            Button(pygame.color.Color(255, 255, 255), pygame.Rect(200, 200, 400, 200), switch_scene, game, GameSceneIds.GAME)
        ]
        return Scene(scene_id, entities)
    elif scene_id == GameSceneIds.GAME:
        entities = [
            Player()
        ]
        return Scene(scene_id, entities)