from controller_2d import Controller2D
from view_2d import View2D

if __name__ == "__main__":
    game = Controller2D()
    view = View2D(game.model)
    game.add_view(view)
    game.main_loop()