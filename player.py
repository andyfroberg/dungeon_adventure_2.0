import pygame
from settings import Settings
from player_sprite import PlayerSprite


class Player:
    def __init__(self):
        self.__name = ''
        self.__x = Settings.PLAYER_START_POS[0]
        self.__y = Settings.PLAYER_START_POS[1]
        self.speed = Settings.PLAYER_SPEED
        self.player_sprite = PlayerSprite(self, [self.game.dungeon.visible_sprites])

    def update(self, keys_pressed):
        # Update player location
        self.move(keys_pressed)

    def move(self, keys):
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1 * self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1 * self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        if self.can_move_x(dx):
            self.x += dx
            self.player_sprite.rect.x += dx * Settings.PIXEL_SCALE

        if self.can_move_y(dy):
            self.y += dy
            self.player_sprite.rect.y += dy * Settings.PIXEL_SCALE

        # If the player hits a door, then take them to the new room.
        if self.can_pass_through_door(dx, dy):
            self.game.dungeon.load_room(RoomFactory.build_room())
            self.set_pos_new_room(dx, dy)

    def can_move_x(self, dx):
        return (int(self.x + dx),
                int(self.y)) not in self.game.dungeon.visible_room

    def can_move_y(self, dy):
        return (int(self.x),
                int(self.y + dy)) not in self.game.dungeon.visible_room

    def can_pass_through_door(self, dx, dy):
        new_pos = (int(self.x + dx), int(self.y + dy))

        return new_pos in self.game.dungeon.visible_room \
               and self.game.dungeon.visible_room[new_pos] == 2

    def set_pos_new_room(self, dx, dy):
        # Precondition - already have checked that door_pos is in
        # dungeon.visible_room (in pass_through_door() function)
        door_pos = (int(self.x + dx), int(self.y + dy))

        # heading north
        if door_pos[1] == 0:
            self.y = game.dungeon.current_room_size[1] - 1
            self.player_sprite.rect.y = (game.dungeon.current_room_size[
                                             1] - 1) * Settings.PIXEL_SCALE
        # heading south
        elif door_pos[1] == self.game.dungeon.current_room_size[1] - 1:
            self.y = 1
            self.player_sprite.rect.y = 1 * Settings.PIXEL_SCALE
        # heading west
        elif door_pos[0] == 0:
            self.x = self.game.dungeon.current_room_size[0] - 1
            self.player_sprite.rect.x = (game.dungeon.current_room_size[
                                             0] - 1) * Settings.PIXEL_SCALE
        # heading east
        else:
            self.x = 1
            self.player_sprite.rect.x = 1 * Settings.PIXEL_SCALE

    def draw(self):
        # Tile((self.x, self.y), [self.visible_sprites])

        # PlayerSprite(self, [self.game.dungeon.visible_sprites])
        # self.game.dungeon.visible_sprites.update()
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    # @property
    # def won(self) -> bool:
    #     return self.__won
    #
    # @won.setter
    # def won(self, won: bool) -> None:
    #     self.__won = won
    #
    # @property
    # def alive(self) -> bool:
    #     return self.__alive
    #
    # @alive.setter
    # def alive(self, alive: bool) -> None:
    #     self.__alive = alive
    #
    # @property
    # def hero(self) -> Hero:
    #     return self.__hero
    #
    # @hero.setter
    # def hero(self, hero: Hero) -> None:
    #     self.__hero = hero
