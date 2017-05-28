import unittest
from resources.player import Player
from resources.item import Item
from resources.space import Space
from auriga import Auriga

class TestPlayer(unittest.TestCase):
    """Tests for player.py"""

    def test_set_name(self):
        test_string = 'Logan'
        test_player = Player()
        test_player.set_name(test_string)
        self.assertEqual(test_player.get_name(), test_string)

    def test_set_description(self):
        test_string = 'Dude who gives no fucks in cutting bitches up.'
        test_player = Player()
        test_player.set_description(test_string)
        self.assertEqual(test_player.get_description(), test_string)

    def test_set_capacity(self):
        test_int = 69
        test_player = Player()
        test_player.set_capacity(test_int)
        self.assertEqual(test_player.get_capacity(), test_int)

    def test_set_items(self):
        test_item_one = Item(name='Shitty_Item_One', weight=2)
        test_item_two = Item(name='Shitty_Item_Two', weight=4)
        test_item_three = Item(name='Shitty_Item_Three', weight=8)
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
        test_item_one = Item(name='Shitty_Item_One', weight=2)
        test_item_two = Item(name='Shitty_Item_Two', weight=4)
        test_item_three = Item(name='Shitty_Item_Three', weight=8)

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
        test_item_one = Item(name='Shitty_Item_One', weight=2)
        test_item_two = Item(name='Shitty_Item_Two', weight=4)
        test_item_three = Item(name='Shitty_Item_Three', weight=8)

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
        test_item_one = Item(name='Shitty_Item_One', weight=2)
        test_item_two = Item(name='Shitty_Item_Two', weight=4)

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
        test_item_one = Item(name='Shitty_Item_One', weight=2)
        test_item_two = Item(name='Shitty_Item_Two', weight=4)
        test_item_three = Item(name='Shitty_Item_Three', weight=8)
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
        test_player.set_location(test_game.assembly_room)
        self.assertIsNotNone(test_player.go_exit(0, direction="east"))



if __name__ == '__main__':
    unittest.main()
