import unittest
from room import Room
from adventurer import Adventurer
from dungeon import Dungeon
from dungeon_adventure import DungeonAdventure
from gremlin import Gremlin
from model import Model
from dungeon_character_factory import DungeonCharacterFactory
from player import Player
from controller_2d import Controller2D
from view import View


class DungeonTests(unittest.TestCase):
    """This class tests the main functionality of the DrawingProgram
    and related classes."""

    ########################################
    # Tests for Adventurer
    ########################################
    def test_adventurer_init(self):
        """
        Tests the init method of Adventurer
        """
        a = Adventurer("Test")
        self.assertEqual(isinstance(a, Adventurer), True)

    def test_adventurer_hp_prop(self):
        a = Adventurer("Test")
        test = a.hp
        self.assertEqual(test, a.hp)

    def test_adventurer_hp_set_hp(self):
        a = Adventurer("Test")
        a.hp = 90
        self.assertEqual(a.hp, 90)

    def test_adventurer_get_inv(self):
        a = Adventurer("Test")
        inv = a.get_inv()
        self.assertEqual(type(inv), dict)

    def test_adventurer_get_inv_keys(self):
        a = Adventurer("Test")
        inv = a.get_inv()
        keys = ["healing", "vision", "abstraction", "encapsulation", "inheritance", "polymorphism"]
        self.assertEqual(list(inv.keys()), keys)

    def test_adventurer_get_inv_values(self):
        a = Adventurer("Test")
        inv = a.get_inv()
        vals = [0, 0, False, False, False, False]
        self.assertEqual(list(inv.values()), vals)

    def test_adventurer_is_dead_false(self):
        a = Adventurer("Test")
        self.assertEqual(a.get_is_dead(), False)

    def test_adventurer_set_dead(self):
        a = Adventurer("Test")
        a.set_is_dead(True)
        self.assertEqual(a.get_is_dead(), True)

    def test_adventurer_use_health_potion(self):
        a = Adventurer("Test")
        pre = a.hp
        a.use_health_potion()
        post = a.hp
        self.assertGreater(post, pre)

    def test_adventurer_take_pit_damage(self):
        a = Adventurer("Test")
        pre = a.hp
        a.take_pit_damage()
        post = a.hp
        self.assertGreater(pre, post)

    ########################################
    # Tests for Room
    ########################################
    def test_room_init(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(isinstance(r, Room), True)

    def test_room_get_vp_visited(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.get_vp_visited(), False)

    def test_room_set_vp_visited(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.set_vp_visited(True)
        self.assertEqual(r.get_vp_visited(), True)

    def test_room_get_visited(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.get_visited(), False)

    def test_room_set_visited(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.set_visited(True)
        self.assertEqual(r.get_visited(), True)

    def test_room_get_contains_player(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.get_contains_player(), False)

    def test_room_set_contains_player(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.set_contains_player(True)
        self.assertEqual(r.get_contains_player(), True)

    def test_room_get_exit(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.get_exit(), False)

    def test_room_set_exit(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.set_exit(True)
        self.assertEqual(r.get_exit(), True)

    def test_room_get_entrance(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.get_entrance(), False)

    def test_room_set_entrance(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.set_entrance(True)
        self.assertEqual(r.get_entrance(), True)

    def test_room_exit_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.is_exit, False)

    def test_room_exit_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.is_exit = True
        self.assertEqual(r.is_exit, True)

    def test_room_entrance_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.is_entrance, False)

    def test_room_entrance_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.is_entrance = True
        self.assertEqual(r.is_entrance, True)

    def test_room_north_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.north, False)

    def test_room_north_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.north = True
        self.assertEqual(r.north, True)

    def test_room_south_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.south, False)

    def test_room_south_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.south = True
        self.assertEqual(r.south, True)

    def test_room_east_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.east, False)

    def test_room_east_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.east = True
        self.assertEqual(r.east, True)

    def test_room_west_prop(self):
        """
        Tests the init method of Room
        """
        r = Room()
        self.assertEqual(r.west, False)

    def test_room_west_prop_set(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.west = True
        self.assertEqual(r.west, True)

    def test_room_add_doors(self):
        """
        Tests the init method of Room
        """
        r = Room()
        r.add_doors(True, True, True, True)
        self.assertEqual(r.north and r.south and r.east and r.west, True)

    def test_room_get_top(self):
        """
        Tests the init method of Room
        """
        r = Room()
        s = r.get_top()
        self.assertEqual(s, "* * *")

    def test_room_get_mid(self):
        """
        Tests the init method of Room
        """
        r = Room()
        s = r.get_mid()
        self.assertEqual(s, "*   *")

    def test_room_get_bottom(self):
        """
        Tests the init method of Room
        """
        r = Room()
        s = r.get_bottom()
        self.assertEqual(s, "* * *")



    ########################################
    # Tests for Dungeon
    ########################################
    def test_dungeon_init(self):
        """
        Tests the init method of Dungeon
        """
        d = Dungeon(Adventurer("A"))
        self.assertEqual(isinstance(d, Dungeon), True)

    def test_dungeon_get_adventurer(self):
        """
        Tests the init method of Dungeon
        """
        d = Dungeon(Adventurer("A"))
        self.assertEqual(isinstance(d.get_adventurer(), Adventurer), True)

    def test_get_current_location(self):
        d = Dungeon(Adventurer("Andy"))
        loc = d.get_current_location()
        self.assertEqual(loc, d.get_current_location())

    def test_set_current_location(self):
        d = Dungeon(Adventurer("Andy"))
        d.set_current_location(3, 2)
        self.assertEqual([3, 2], d.get_current_location())

    ########################################
    # Tests for DungeonAdventure
    ########################################
    def test_dungeonadventure_init(self):
        """
        Tests the init method of DungeonAdventure
        """
        da = DungeonAdventure(Adventurer("A"))
        self.assertEqual(isinstance(da, DungeonAdventure), True)

    def test_dungeonadventure_set_player_name(self):
        """
        Tests the set_player_name() function
        """
        da = DungeonAdventure(Adventurer("A"))
        da.set_player_name("B")
        self.assertEqual(da.get_player_name(), "B")

    def test_dungeonadventure_get_dungeon(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        self.assertEqual(isinstance(da.get_dungeon(), Dungeon), True)

    def test_dungeonadventure_get_quit(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        self.assertEqual(da.get_quit(), False)

    def test_dungeonadventure_set_quit(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        da.set_quit(True)
        self.assertEqual(da.get_quit(), True)

    def test_dungeonadventure_get_player_has_won(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        self.assertEqual(da.get_player_has_won(), False)

    def test_dungeonadventure_set_player_has_won(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        da.set_player_has_won(True)
        self.assertEqual(da.get_player_has_won(), True)

    def test_dungeonadventure_get_player_is_dead(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        self.assertEqual(da.get_player_is_dead(), False)

    def test_dungeonadventure_set_player_is_dead(self):
        """
        """
        da = DungeonAdventure(Adventurer("A"))
        da.set_player_is_dead(True)
        self.assertEqual(da.get_player_is_dead(), True)

    def test_dungeonadventure_get_player_name(self):
        """
        Tests the get_player_name() function
        """
        da = DungeonAdventure(Adventurer("A"))
        da.get_player_name()
        self.assertEqual(da.get_player_name(), "A")

    ########################################
    # Tests for Gremlin
    ########################################
    def test_Gremlin_init(self):
        a = Gremlin("B")
        self.assertEqual(isinstance(a, Gremlin), True)

    def test_monster_stats(self):
        self.assertEqual(self.Gremlin.get_monster_stats(), {
            "heal_prob": 0.4,
            "heal_range": [20, 40]
        })

    ########################################
    # Tests for Model
    ########################################

    def test_model_init(self):
        """
        Tests the init method of Model
        """
        model = Model()
        self.assertEqual(isinstance(model, Model), True)


    def test_player(self):
        """

        :return:
        """
        model = Model()
        player = Player()
        model.player = player
        self.assertEqual(model.player, player)

    def test_win(self):
        model = Model()
        self.assertFalse(model.win)
        model.win = True
        self.assertTrue(model.win)

    def test_gameover(self):
        """

        :return:
        """
        model = Model()
        self.assertFalse(model.gameover)
        model.gameover = True
        self.assertTrue(model.gameover)

    def test_opponent(self):
        """

        :return:
        """
        model = Model()
        opponent = DungeonCharacterFactory.create_thief('Opponent')
        model.opponent = opponent
        self.assertEqual(model, opponent)

    def test_player_setter(self):
        """

        """
        model = Model()
        player = Player()
        model.player = player
        assert model.player == player

    def test_set_player_name(self):
        name = "John"
        self.model.player_name = name
        self.assertEqual(self.model.player_name, name)

    def test_player_name(self):
        """

        """
        model = Model()
        model.player_name = "Player 1"
        self.assertEqual(model.player_name, "Player 1")


    def test_register_view(self):
        self.model.register_view(self.view)
        self.assertIn(self.view, self.model._Model__views)

    def test_set_invalid_opponent(self):
        model = Model()
        with self.assertRaises(ValueError):
            self.model.opponent = "invalid_opponent"

    def test_dungeon_property(self):
        dungeon = Dungeon()
        game = DungeonAdventure()
        game.dungeon = dungeon
        self.assertEqual(game.dungeon, dungeon)

    def test_model_property(self):

        model = Model()
        self.__model = model
        self.assertEqual(self.__model, model)

    def test_get_player_inventory(self):
        """
        Test get_player_inventory method
        """
        expected_inventory = {'sword': 1, 'shield': 1}
        self.__player_inventory = expected_inventory
        self.assertEqual(self.get_player_inventory(), expected_inventory)

    def test_main_menu_property(self):
        """
        Test main_menu property getter and setter
        """
        self.main_menu = True
        self.assertTrue(self.main_menu)
        self.main_menu = False
        self.assertFalse(self.main_menu)

    def test_start_menu_property(self):
        """
        Test start_menu property getter and setter
        """
        self.start_menu = True
        self.assertTrue(self.start_menu)
        self.start_menu = False
        self.assertFalse(self.start_menu)

    def test_pause_menu_property(self):
        """
        Test pause_menu property getter and setter
        """
        self.pause_menu = True
        self.assertTrue(self.pause_menu)
        self.pause_menu = False
        self.assertFalse(self.pause_menu)

    ########################################
    # Tests for View
    ########################################

    def test_controller2D_init(self):
        self.assertIsNotNone(self.controller)
        self.assertIsInstance(self.controller, Controller2D)
        self.assertIsInstance(self.controller._Controller2D__model, Model)
        self.assertIsNone(self.controller._Controller2D__view)
        self.assertTrue(self.controller._Controller2D__running)
        self.assertFalse(self.controller._Controller2D__mouse_clicked)
        self.assertIsNone(self.controller._Controller2D__current_battle_dc)
        self.assertDictEqual(self.controller._Controller2D__display_once, {'get_to_exit': 0})

    def test_add_view(self):
        view = 'test_view'
        self.controller.add_view(view)
        self.assertEqual(self.controller._Controller2D__view, view)













if __name__ == '__main__':
    unittest.main()