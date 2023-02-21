from hero import Hero
from dungeon_character import DungeonCharacter
import random
from room import Room


class Thief(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage
    def special(self, opponent: DungeonCharacter) -> None:
        """
        surprise attack
        :return:
        """
        surprise_attack = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        successful = 0.4
        caught = 0.2
        normal = 0.4
        if chance <= caught:
            pass
        elif chance <= successful:
            opponent.hp -= surprise_attack * 2
        else:
            opponent.hp -= surprise_attack

    def battle(self, opponent: DungeonCharacter):
        if self.attack_speed > opponent.attack_speed:
            while self.attack_speed > opponent.attack_speed:
                self.attack(opponent)
                self.attack_speed -= 1
        elif self.attack_speed == opponent.attack_speed:
            pass
        else:
            while self.attack_speed < opponent.attack_speed:
                opponent.attack(self)
                opponent.attack_speed -= 1

    def move(self, room):
        """This method updates the current location of the Adventurer"""
        # check to make sure a room is being passed
        if isinstance(room, Room):
            self._location = room
        else:
            raise TypeError("That's not a room...")
