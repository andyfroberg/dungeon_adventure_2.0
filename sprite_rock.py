import pygame


class SpriteRock(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/rock_50x50_v1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
