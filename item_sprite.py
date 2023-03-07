import pygame


class ItemSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)