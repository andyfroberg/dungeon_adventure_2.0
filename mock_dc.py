class MockDC:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__damage = 25
        self.__block_prob = 0.2

    @staticmethod
    def attack(self, opponent):
        opponent.take_damage()

    def take_damage(self, opponent):
        self.__hp -= opponent.get_damage()

    def get_damage(self):
        return self.__damage
