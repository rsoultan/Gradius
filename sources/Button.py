import pygame

from sources.Entity import Entity


class Button(Entity):
    def __init__(self, color, rect, on_click, *on_click_params):
        self.color = color
        self.rect = rect
        self.on_click = on_click
        self.on_click_params = on_click_params
        self.hover = False
        self.pressed = False
        self.clicked = False
    
    def event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
            mouse_pressed = pygame.mouse.get_pressed()
            if self.pressed and event.type == pygame.MOUSEBUTTONUP:
                self.clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressed[0]:
                self.pressed = True
        else:
            self.hover = False
            self.pressed = False

    def update(self, elapsed_time):
        if self.clicked:
            self.on_click(self.on_click_params)
            self.clicked = False

    def draw(self, window):
        grey = (200, 200, 200)
        black = (150, 150, 150)
        if self.clicked:
            pygame.draw.rect(window, (255, 0, 0), self.rect)
        elif self.pressed:
            pygame.draw.rect(window, black, self.rect)
        elif self.hover:
            pygame.draw.rect(window, grey, self.rect)
        else:
            pygame.draw.rect(window, self.color, self.rect)
