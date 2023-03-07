import pygame
from item_sprite import ItemSprite
from world_sprite import WorldSprite
from player_sprite import PlayerSprite
from settings import Settings


class SpriteFactory:

    # World sprites
    SPRITE_BRICK_PATH = 'sprites/brick_brown_50x50_v3.png'
    SPRITE_DOOR_PATH = 'sprites/door_50x50_v2.png'
    SPRITE_FLOOR_PATH = 'sprites/floor_50x50_v1.png'
    SPRITE_GATE_PATH = 'sprites/gate_50x50_v2.png'
    SPRITE_ROCK_PATH = 'sprites/rock_50x50_v1.png'

    # Item Sprites
    DUNGEON_KEY_PATH = 'sprites/pillar_a_50x50.png'  # need new sprite
    PILLAR_A_PATH = 'sprites/pillar_a_50x50.png'
    PILLAR_E_PATH = 'sprites/pillar_e_50x50.png'
    PILLAR_I_PATH = 'sprites/pillar_i_50x50.png'
    PILLAR_P_PATH = 'sprites/pillar_p_50x50.png'

    # Characters
    HERO_PRIESTESS_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    HERO_THIEF_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    HERO_WARRIOR_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    MONSTER_GREMLIN_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite
    MONSTER_OGRE_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite
    MONSTER_SKELETON_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite

    @staticmethod
    def create_brick():
        brick = WorldSprite(SpriteFactory.SPRITE_BRICK_PATH, position, groups)

