from game_difficulty import GameDifficulty

class Settings:
    # Window Settings
    SCREEN_RESOLUTION = (700, 500)  # (width, height)
    FPS = 60  # Frames per second
    PIXEL_SCALE = 50
    SPRITE_SCALE = 1
    WINDOW_TOP_LEFT = (0, 0)  # "Origin" point of window at top left of screen

    # Game Difficulty
    GAME_DIFFICULTY = GameDifficulty.NORMAL

    # Player Stats
    PLAYER_START_POS = (2.25, 1)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05
    PLAYER_BOUNDING_RECT = 0.25

    # Dungeon Character Stats

    # Room Settings
    ROOM_MIN_WIDTH = 3
    ROOM_MIN_HEIGHT = 3
    ROOM_MAX_WIDTH = 14
    ROOM_MAX_HEIGHT = 8

    # Sprite Values
    EXIT = 'e'
    OPEN_FLOOR = 'F'
    BRICK_WALL = 'B'
    GATE = 'G'
    DOOR = 'D'  # No longer needed? Check codebase for 'Settings.DOOR' occurrences
    PIT = 'X'
    ROCK = 'R'
    PRIESTESS = 'p'
    THIEF = 'T'
    WARRIOR = 'W'
    GREMLIN = 'g'
    OGRE = 'o'
    SKELETON = 'S'
    PILLAR_A = 'A'
    PILLAR_E = 'E'
    PILLAR_I = 'I'
    PILLAR_P = 'P'

    # Sprite Paths - World sprites
    SPRITE_PATHS = {
        'brick': 'sprites/brick_brown_50x50_v3.png',
        'door': 'sprites/door_50x50_v2.png',
        'exit': 'sprites/exit_stairs_50x50.png',
        'floor': 'sprites/floor_50x50_v1.png',
        'gate': 'sprites/gate_50x50_v2.png',
        'pit': 'sprites/pit_50x50.png',
        'rock': 'sprites/rock_50x50_v1.png',
        'dungeon_key': 'sprites/pillar_a_50x50.png',
        'pillar_a': 'sprites/pillar_a_50x50.png',
        'pillar_e': 'sprites/pillar_e_50x50.png',
        'pillar_i': 'sprites/pillar_i_50x50.png',
        'pillar_p': 'sprites/pillar_p_50x50.png',
        'priestess': 'sprites/warrior_sp_1.png',
        'thief': 'sprites/warrior_sp_1.png',
        'warrior': 'sprites/warrior_sp_1.png',
        'gremlin': 'sprites/warrior_sp_1.png',
        'ogre': 'sprites/warrior_sp_1.png',
        'skeleton': 'sprites/warrior_sp_1.png',
    }

    SPRITE_BRICK_PATH = 'sprites/brick_brown_50x50_v3.png'
    SPRITE_DOOR_PATH = 'sprites/door_50x50_v2.png'
    SPRITE_FLOOR_PATH = 'sprites/floor_50x50_v1.png'
    SPRITE_GATE_PATH = 'sprites/gate_50x50_v2.png'
    SPRITE_ROCK_PATH = 'sprites/rock_50x50_v1.png'

    # Sprite Paths - Item Sprites
    DUNGEON_KEY_PATH = 'sprites/pillar_a_50x50.png'  # need new sprite
    PILLAR_A_PATH = 'sprites/pillar_a_50x50.png'
    PILLAR_E_PATH = 'sprites/pillar_e_50x50.png'
    PILLAR_I_PATH = 'sprites/pillar_i_50x50.png'
    PILLAR_P_PATH = 'sprites/pillar_p_50x50.png'

    # Sprite Paths - Characters
    HERO_PRIESTESS_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    HERO_THIEF_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    HERO_WARRIOR_PATH = 'sprites/warrior_sp_1.png'  # Create new sprite for this
    MONSTER_GREMLIN_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite
    MONSTER_OGRE_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite
    MONSTER_SKELETON_PATH = 'sprites/warrior_sp_1.png'  # Need to create sprite


    # Menu Paths
    GAME_OVER_PATH = 'menu/game_over_v2.png'
    GAME_OVER_MENU_PATH = 'menu/game_over_menu.png'

    # Battle Overlay Text Paths
    ATTACK_SUCCESS_PATH = 'battle/attack_success.png'
    ATTACK_FAILED_PATH = 'battle/attack_failed.png'
    CRUSHING_SUCCESS_PATH = 'battle/crushing_success.png'
    CRUSHINGS_FAILED_PATH = 'battle/crushing_failed.png'
    HEAL_SUCCESS_PATH = 'battle/heal_success.png'
    HEAL_FAILED_PATH = 'battle/heal_failed.png'
    SUPRISE_SUCCESS_PATH = 'battle/surprise_success.png'
    SURPRISE_FAILED_PATH = 'battle/surprise_failed.png'
    ENEMY_ATTACK_SUCCESS_PATH = 'battle/opponent_attack_success.png'
    ENEMY_ATTACK_FAILED_PATH = 'battle/opponent_attack_failed.png'
    ENEMY_HEAL_SUCCESS_PATH = 'battle/opponent_heal_success_2.png'
    ENEMY_HEAL_FAILED_PATH = 'battle/opponent_heal_failed.png'
    BATTLE_WON_PATH = 'battle/battle_won.png'

    # Background colors
    BG_BLACK = (0, 0, 0)
    ROOM_BG_FLOOR_COLOR = (178, 178, 178)  # Medium gray to match floor color

    # User Interface
    # Button sizes (get rid of "magic numbers")
    BUTTON_WIDTH = 323
    BUTTON_HEIGHT = 46
    BUTTON_WIDTH_SMALL = 242
    BUTTON_HEIGHT_SMALL = 34
    # Button positions
    BUTTON_X_LEFT_JUST = 50
    BUTTON_Y_LEFT_JUST_FIRST = 50
    BUTTON_Y_LEFT_JUST_NTH_SPACING = 50
    BUTTON_SMALL_X_LEFT_JUST = 50
    BUTTON_SMALL_Y_LEFT_JUST_FIRST = 50
    BUTTON_SMALL_Y_LEFT_JUST_NTH_SPACING = 50
    # Battle UI buttons


    # HUD
    HUD_RECT = (0, 400, 700, 100)
    HUD_POS_HEALTH = (20, 450)
    HUD_POS_PILLAR_A = (450, 430)
    HUD_POS_PILLAR_E = (500, 430)
    HUD_POS_PILLAR_I = (550, 430)
    HUD_POS_PILLAR_P = (600, 430)
    HUD_POS_POTION_HEALTH = (220, 430)

    # Battle HUD
    BATTLE_HUD_RECT = (200, 190, 250, 200)
    BATTLE_MSG_RECT = (130, 10, 400, 100)


    # Collision Detection
    COLLISION_TOLERANCE = 1

    # Monster's Vision Distance
    MONSTER_VISION_DISTANCE = 3

    # Dungeon Character Stats
    DC_STATS = {
        'priestess': {
            "hp": 75,
            "attack_speed": 5,
            "hit_prob": 0.7,
            "damage_range": (25, 45),
            "block_prob": 0.3,
        },
        'thief': {
            "hp": 75,
            "attack_speed": 6,
            "hit_prob": 0.8,
            "damage_range": (20, 40),
            "block_prob": 0.4,
        },
        'warrior': {
            "hp": 125,
            "attack_speed": 4,
            "hit_prob": 0.8,
            "damage_range": (35, 60),
            "block_prob": 0.2,
        },
        'gremlin': {
            "hp": 70,
            "attack_speed": 5,
            "hit_prob": 0.8,
            "damage_range": (15, 30),
            "heal_prob": 0.4,
            "heal_range": (20, 40),
        },
        'ogre': {
            "hp": 200,
            "attack_speed": 2,
            "hit_prob": 0.6,
            "damage_range": (30, 60),
            "heal_prob": 0.1,
            "heal_range": (30, 60),
        },
        'skeleton': {
            "hp": 100,
            "attack_speed": 3,
            "hit_prob": 0.8,
            "damage_range": (30, 50),
            "heal_prob": 0.3,
            "heal_range": (30, 50),
        },
    }
