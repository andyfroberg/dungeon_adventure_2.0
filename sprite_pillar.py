import pygame


class SpritePillar(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/pillar_a_50x50.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)