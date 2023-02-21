from hero import Hero


class Player:
    def __init__(self, name: str, hero: Hero) -> None:
        self.__name = name
        self.__won = False
        self.__alive = True
        self.__quit_game = False
        self.__hero = hero  # User of this class should pass in a concrete Hero (e.g., Warrior, Priestess, or Thief)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def won(self) -> bool:

        return self.__won

    @won.setter
    def won(self, won: bool) -> None:
        self.__won = won

    @property
    def alive(self) -> bool:
        return self.__alive

    @alive.setter
    def alive(self, alive: bool) -> None:
        self.__alive = alive

    @property
    def hero(self) -> Hero:
        return self.__hero

    @hero.setter
    def hero(self, hero: Hero) -> None:
        self.__hero = hero