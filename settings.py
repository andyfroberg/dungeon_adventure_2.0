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
    OPEN_FLOOR = 'F'
    BRICK_WALL = 'B'
    GATE = "G"
    DOOR = 'D'
    ROCK = 'R'
    OGRE = 'o'

    # Backgrounge colors
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



