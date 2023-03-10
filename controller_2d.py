import pygame
import sys
from model import Model
from view_2d import View2D

class Controller2D:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__view = None
        self.__running = True
        self.__mouse_clicked = False

    def run(self):
        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Get the keys the player is pressing this loop iteration.
                keys = pygame.key.get_pressed()

                self.__mouse_clicked = False  # Reset to avoid multiple clicks
                self.handle_menu_events(event)

            # Check if player can move
            # Check colliderect() with all sprites in the room
            self.check_player_can_move(self.__model.player,
                                       self.__model.dungeon, self.__view, keys)

            # Check player collision with items
            self.check_item_collision()

            # Check door collisions
            self.check_door_collision()

            # Check player collision with monsters


            # Update model -does this need to be split into multiple funcs now?
            # ie model might not just be able to "update" based on logic
            # above
            self.__model.update(keys)

    def add_view(self, view):
        self.__view = view

    def check_player_can_move(self, player, dungeon, view, keys):
        # Iterate over all world sprites, colliderect()
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1 * player.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1 * player.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = player.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = player.speed

        player_rect = view.player_sprite.rect

        for w_sprite in view.world_sprites:
            w_rect = w_sprite.rect
            if w_rect.colliderect(player_rect.x + dx, player_rect.y,
                                  view.player_sprite.width,
                                  view.player_sprite.height):
                if dx < 0:  # Moving west
                    dx = w_rect.right - player_rect.left
                elif dy >= 0:  # Moving east (or not moving)
                    dy = w_rect.left - player_rect.right

            if w_rect.colliderect(player_rect.x, player_rect.y + dy,
                                  view.player_sprite.width,
                                  view.player_sprite.height):
                if dy < 0:  # Moving north
                    dy = w_rect.bottom - player_rect.top
                elif dy >= 0:  # Moving south (or not moving)
                    dy = w_rect.top - player_rect.bottom

        # Update player pos
        player_rect.x += dx
        player_rect.y += dy

    def handle_menu_events(self, event):
        if self.__model.main_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.__view.menus['main'].buttons:
                    bounding_rect = pygame.Rect(button.rect)
                    if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                        if button.name == 'new game':
                            self.model.main_menu = False  # start new game
                        elif button.name == 'load game':
                            pass  # load saved game
                        elif button.name == 'options':
                            pass  # options menu

        if self.__model.pause_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.__view.menus['pause'].buttons:
                    bounding_rect = pygame.Rect(button.rect)
                    if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                        if button.name == 'continue':
                            self.model.pause_menu = False
                        elif button.name == 'save game':
                            pass  # save game
                        elif button.name == 'load game':
                            pass  # load saved game
                        elif button.name == 'options':
                            pass  # options menu

    def check_item_collision(self):
        if self.__view:
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for item in self.__view.item_sprites:
                if p_rect.colliderect(item.rect):
                    self.__model.player.pickup_item(item)
                    self.__view.menus['hud'].add_item(item)
                    self.__view.item_sprites.remove(item)
                    self.__view.item_sprites.update()

    def check_door_collision(self):
        if self.__view:
            print(str(self.__view.door_sprites))
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for door in self.__view.door_sprites:
                if p_rect.colliderect(door.rect):
                    # self.__model.player.use_key()
                    # self.__view.menus['hud'].add_item(item)
                    self.__view.door_sprites.remove(door)
                    self.__view.door_sprites.update()

    @property
    def model(self):
        return self.__model

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, is_running: bool):
        # Validate input
        self.__running = is_running


if __name__ == "__main__":
    pass
    # game = Controller2D()
    # view = View2D(game.model)
    # game.run()