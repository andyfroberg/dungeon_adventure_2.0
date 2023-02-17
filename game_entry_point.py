from view_console import ViewConsole
from controller_console import ControllerConsole
from model import Model


class GameEntryPoint:
    pass


if __name__ == "__main__":
    m = Model()
    v = ViewConsole()
    c = ControllerConsole(m, v)

    # m.register_controller(c)
    # v.register_controller(c)

    # v.show_start_screen()
    # c.set_up_game()