import pygame

class SpriteDoor(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/door_50x50_v2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)