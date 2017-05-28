import unittest
from resources.player import Player
from resources.item import Item
from resources.space import Space
from auriga import Auriga

class TestSpace(unittest.TestCase):
    """Tests for space.py"""

    def test_add_item(self):
        test_room = Space(name="Test Room")
        test_item = Item(name="Pencil")
        test_room.add_item(test_item)

        items_in_room = [i.name for i in test_room.get_items()]
        self.assertIn(test_item.name, items_in_room)
        self.assertEqual(test_item.location, test_room)

    def test_remove_item(self):
        test_room = Space(name="Test Room")
        test_item_one = Item(name="Pencil")
        test_item_two = Item(name="Pen")
        test_item_three = Item(name="Eraser")
        test_room.add_item(test_item_one)
        test_room.add_item(test_item_two)
        test_room.add_item(test_item_three)

        test_room.remove_item(test_item_one)
        self.assertNotIn(test_item_one, test_room.get_items())
        self.assertIn(test_item_two, test_room.get_items())
        self.assertIn(test_item_three, test_room.get_items())

        test_room.remove_item(test_item_three)
        self.assertNotIn(test_item_three, test_room.get_items())
        self.assertIn(test_item_two, test_room.get_items())
        self.assertNotIn(test_item_one, test_room.get_items())

if __name__ == "__main__":
    unittest.main()
