from controller_2d import Controller2D
from view_2d import View2D

if __name__ == "__main__":
    game = Controller2D()
    view = View2D(game.model)
    game.register_view(view)
    game.run()
