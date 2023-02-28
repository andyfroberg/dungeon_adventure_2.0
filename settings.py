from game_difficulty import GameDifficulty

class Settings:
    # Game Setup
    SCREEN_RESOLUTION = (700, 500)  # (width, height)
    FPS = 60  # Frames per second
    PIXEL_SCALE = 50
    SPRITE_SCALE = 1

    # Game Difficulty
    GAME_DIFFICULTY = GameDifficulty.NORMAL

    # Player Stats
    PLAYER_START_POS = (2, 2)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05

    # Dungeon Character Stats

    # Room Settings
    ROOM_MIN_WIDTH = 3
    ROOM_MIN_HEIGHT = 3
    ROOM_MAX_WIDTH = 14
    ROOM_MAX_HEIGHT = 8
    OPEN_FLOOR = 0
    BRICK_WALL = 1
    DOOR = 2
    ROCK = 3


