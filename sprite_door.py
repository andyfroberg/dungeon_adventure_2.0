import pygame

### Citation 001 - How to create a Zelda style game in python
#   https://www.youtube.com/watch?v=cwWi05Icpw0
#
# The sprite functionality of this game was heavily influenced by the
# above video which explains how to use sprites in Pygame.
class SpriteDoor(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/door_50x50_v2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
### End Citation 001