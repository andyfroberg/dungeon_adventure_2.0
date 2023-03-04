import pygame

class SpriteBrick(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/brick_brown_50x50_v3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
