import unittest
from resources.player import Player
from resources.item import Item
from resources.space import Space
from auriga import Auriga

class TestPlayer(unittest.TestCase):
    """Tests for player.py"""

    def test_set_name(self):
        test_string = "R2-D2"
        test_player = Player()
        test_player.set_name(test_string)
        self.assertEqual(test_player.get_name(), test_string)

    def test_set_description(self):
        test_string = "Adorable spunky droid"
        test_player = Player()
        test_player.set_description(test_string)
        self.assertEqual(test_player.get_description(), test_string)

    def test_set_capacity(self):
        test_int = 69
        test_player = Player()
        test_player.set_capacity(test_int)
        self.assertEqual(test_player.get_capacity(), test_int)

    def test_set_items(self):
        test_item_one = Item(name="Test_Item_One", weight=2)
        test_item_two = Item(name="Test_Item_Two", weight=4)
        test_item_three = Item(name="Test_Item_Three", weight=8)
        test_player = Player()

        test_list = [test_item_one]
        test_player.set_items(test_list)
        self.assertEqual(test_player.get_items(), test_list)

        test_list = [test_item_one, test_item_two]
        test_player.set_items(test_list)
        self.assertEqual(test_player.get_items(), test_list)

        test_list = [test_item_one, test_item_two, test_item_three]
        test_player.set_items(test_list)
        self.assertEqual(test_player.get_items(), test_list)

    def test_add_item(self):
        test_item_one = Item(name="Test_Item_One", weight=2)
        test_item_two = Item(name="Test_Item_Two", weight=4)
        test_item_three = Item(name="Test_Item_Three", weight=8)

        test_inventory = []
        test_player = Player(items=test_inventory)
        self.assertEqual(test_player.get_items(), test_inventory)

        test_player.add_item(test_item_one)
        self.assertIn(test_item_one, test_player.get_items())

        test_player.add_item(test_item_two)
        self.assertIn(test_item_two, test_player.get_items())

        test_player.add_item(test_item_three)
        self.assertIn(test_item_three, test_player.get_items())

    def test_remove_item(self):
        test_item_one = Item(name="Test_Item_One", weight=2)
        test_item_two = Item(name="Test_Item_Two", weight=4)
        test_item_three = Item(name="Test_Item_Three", weight=8)

        test_inventory = [test_item_one, test_item_two, test_item_three]
        test_player = Player(items=test_inventory)
        self.assertEqual(test_player.get_items(), test_inventory)

        test_player.remove_item(test_item_one)
        self.assertNotIn(test_item_one, test_player.get_items())

        test_player.remove_item(test_item_two)
        self.assertNotIn(test_item_two, test_player.get_items())

        test_player.remove_item(test_item_three)
        self.assertNotIn(test_item_three, test_player.get_items())

    def test_get_item_names(self):
        test_item_one = Item(name="Test_Item_One", weight=2)
        test_item_two = Item(name="Test_Item_Two", weight=4)

        test_inventory = []
        test_player = Player(items=test_inventory)

        test_list = [test_item_one.name]
        test_player.add_item(test_item_one)
        self.assertEqual(test_player.get_item_names(), test_list)

        test_list = [test_item_one.name, test_item_two.name]
        test_player.add_item(test_item_two)
        self.assertEqual(test_player.get_item_names(), test_list)

        test_list = [test_item_two.name]
        test_player.remove_item(test_item_one)
        self.assertEqual(test_player.get_item_names(), test_list)

    def test_get_items_total_weight(self):
        test_item_one = Item(name="Test_Item_One", weight=2)
        test_item_two = Item(name="Test_Item_Two", weight=4)
        test_item_three = Item(name="Test_Item_Three", weight=8)
        test_inventory = []

        test_player = Player(items=test_inventory)
        self.assertEqual(0, test_player.get_items_total_weight())

        test_player.add_item(test_item_one)
        self.assertEqual(2, test_player.get_items_total_weight())

        test_player.add_item(test_item_three)
        self.assertEqual(10, test_player.get_items_total_weight())

        test_player.remove_item(test_item_one)
        self.assertEqual(8, test_player.get_items_total_weight())

    def test_set_location(self):
        #TODO: Finish these tests
        test_player = Player()
        test_game = Auriga(test_player)

        test_player.set_location(test_game.assembly_room)
        self.assertEqual(test_player.get_location(), test_game.assembly_room)

        test_player.set_location(test_game.clean_room)
        self.assertEqual(test_player.get_location(), test_game.clean_room)


    def test_set_alive(self):
        test_player = Player()
        self.assertTrue(test_player.get_alive())

        test_player.set_alive(False)
        self.assertFalse(test_player.get_alive())

        test_player.set_alive(True)
        self.assertTrue(test_player.get_alive())


    def test_set_energy(self):
        test_player = Player()
        self.assertEqual(100, test_player.get_energy())

        test_player.set_energy(80)
        self.assertEqual(80, test_player.get_energy())

        test_player.set_energy(-15)
        self.assertEqual(0, test_player.get_energy())

    def test_go_exit(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_game_player.set_location(test_game.assembly_room)
        self.assertIsNone(test_game_player.go_exit(0, direction="east"))

        #TODO: Figure out how to get this to not return 'None'
        assembly_room_exits = [i.name for i in test_game.assembly_room.get_exits()]
        assembly_room_exits_status = [i.is_locked() for i in test_game.assembly_room.get_exits()]
        print(assembly_room_exits)
        print(assembly_room_exits_status)
        test_game.push("button")

        print(assembly_room_exits)
        print(assembly_room_exits_status)
        self.assertIsNotNone(test_game_player.go_exit(0, direction="east",
         exit_name="sliding_door"))

    def test_take(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_game_player.set_location(test_game.assembly_room)

        test_item = "screwdriver"
        bad_item = "charger"
        energy_before = test_game_player.get_energy()
        test_game_player.take(test_item)
        test_player_inventory = [i.name for i in test_game_player.get_items()]
        self.assertIn(test_item, test_player_inventory)
        self.assertNotIn(bad_item, test_player_inventory)
        self.assertEqual(test_game_player.get_energy(), energy_before - 2)

        test_item = "drive"
        energy_before = test_game_player.get_energy()
        test_game_player.take(test_item)
        test_player_inventory = [i.name for i in test_game_player.get_items()]
        self.assertNotIn(test_item, test_player_inventory)

    def test_talk(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_game_player.set_location(test_game.assembly_room)

        test_character = "pr-2"
        energy_before = test_game_player.get_energy()
        test_game_player.talk(test_character, 0)
        self.assertEqual(test_game_player.get_energy(), energy_before - 1)

        test_character = "c-3po"
        energy_before = test_game_player.get_energy()
        test_game_player.talk(test_character,0)
        self.assertEqual(test_game_player.get_energy(), energy_before)

    def test_drop(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_room = test_game.assembly_room
        test_game_player.set_location(test_room)

        test_item = "screwdriver"
        test_game_player.take(test_item)
        energy_before = test_game_player.get_energy()
        test_game_player.drop(test_item)
        room_items = [i.name for i in test_room.get_items()]
        player_items = [i.name for i in test_game_player.get_items()]
        self.assertIn(test_item, room_items)
        self.assertNotIn(test_item, player_items)
        self.assertEqual(test_game_player.get_energy(), energy_before - 1)

        test_item = "cables"
        energy_before = test_game_player.get_energy()
        test_game_player.drop(test_item)
        room_items = [i.name for i in test_room.get_items()]
        player_items = [i.name for i in test_game_player.get_items()]
        self.assertNotIn(test_item, room_items)
        self.assertEqual(test_game_player.get_energy(), energy_before)

    def test_look(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_room = test_game.assembly_room
        test_game_player.set_location(test_room)

        energy_before = test_game_player.get_energy()
        test_game_player.look(0)
        self.assertEqual(test_game_player.get_energy(), energy_before - 1)

        energy_before = test_game_player.get_energy()
        test_game_player.look(1)
        self.assertNotEqual(test_game_player.get_energy(), energy_before)

    def test_look_at(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_room = test_game.assembly_room
        test_game_player.set_location(test_room)

        test_item = "screwdriver"
        energy_before = test_game_player.get_energy()
        test_game_player.look_at(test_item)
        self.assertEqual(test_game_player.get_energy(), energy_before - 1)

        test_item = "cables"
        energy_before = test_game_player.get_energy()
        test_game_player.look_at(test_item)
        self.assertEqual(test_game_player.get_energy(), energy_before)

    def test_charge(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player

        test_room = test_game.assembly_room
        test_game_player.set_location(test_room)
        test_game_player.set_energy(80)
        test_game_player.charge()
        self.assertEqual(test_game_player.get_energy(), test_game_player.max_energy)

        test_room = test_game.testing_hangar
        test_game_player.set_location(test_room)
        test_game_player.set_energy(80)
        test_game_player.charge()
        self.assertNotEqual(test_game_player.get_energy(), test_game_player.max_energy)

    def test_listen(self):
        test_player = Player()
        test_game = Auriga(test_player)
        test_game_player = test_game.player
        test_room = test_game.assembly_room
        test_game_player.set_location(test_room)

        test_game_player.set_energy(80)
        energy_before = test_game_player.get_energy()
        test_game_player.listen()
        self.assertEqual(test_game_player.get_energy(), energy_before + 1)

if __name__ == '__main__':
    unittest.main()
