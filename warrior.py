from hero import Hero
from dungeon_character import DungeonCharacter
import random
from room import Room


class Warrior(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)

    def attack(self, opponent: DungeonCharacter) -> None:
        # sucess = True
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage
        # else:
        #      sucess = False


    def special(self, opponent: DungeonCharacter) -> None:
        """
        Crushing blow
        :return:
        """
        special_hit_prob = 0.4
        damage = random.randint(75, 175)
        chance = random.random()# chance to hit
        if chance <= special_hit_prob:
            opponent.hp -= damage

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