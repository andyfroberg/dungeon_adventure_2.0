import pygame
from settings import Settings

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.image = pygame.image.load(
            'sprites/warrior_sp_1.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(player.x * Settings.PIXEL_SCALE,  # Might need to be topleft=...
                    player.y * Settings.PIXEL_SCALE))
