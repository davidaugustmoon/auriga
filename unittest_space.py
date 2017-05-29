import unittest
from resources.player import Player
from resources.item import Item
from resources.space import Space
from resources.exit import Exit
from resources.character import Character
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

    def test_add_exit(self):
        test_room = Space(name="Test Room")
        test_exit = Exit(name="Test Exit")
        fake_exit = Exit(name="Not An Exit")

        test_room.add_exit(test_exit)
        test_room_exits = [i.name for i in test_room.get_exits()]
        self.assertIn(test_exit.name, test_room_exits)
        self.assertNotIn(fake_exit.name, test_room_exits)

    def test_remove_exit(self):
        test_room = Space(name="Test Room")
        first_test_exit = Exit(name="Test Exit")
        second_test_exit = Exit(name="Another Test Exit")
        third_test_exit = Exit(name="Yet Another Test Exit")
        test_exits = [first_test_exit, second_test_exit, third_test_exit]

        test_room.set_exits(test_exits)
        test_room.remove_exit(first_test_exit)
        test_room_exits = [i.name for i in test_room.get_exits()]
        self.assertNotIn(first_test_exit.name, test_room_exits)
        self.assertIn(second_test_exit.name, test_room_exits)
        self.assertIn(third_test_exit.name, test_room_exits)

        test_room.set_exits(test_exits)
        test_room.remove_exit(third_test_exit)
        test_room.remove_exit(first_test_exit)
        test_room_exits = [i.name for i in test_room.get_exits()]
        self.assertNotIn(third_test_exit.name, test_room_exits)
        self.assertIn(second_test_exit.name, test_room_exits)
        self.assertNotIn(first_test_exit.name, test_room_exits)

    def test_add_character(self):
        test_room = Space(name="Test Room")
        first_test_character = Character(name="R2-D2")
        second_test_character = Character(name="C-3PO")
        fake_test_character = Character(name="R4-D4")

        test_room.add_character(first_test_character)
        test_room_characters = [i.name for i in test_room.get_characters()]
        self.assertIn(first_test_character.name, test_room_characters)
        self.assertNotIn(second_test_character.name, test_room_characters)
        self.assertNotIn(fake_test_character.name, test_room_characters)

        test_room.add_character(second_test_character)
        test_room_characters = [i.name for i in test_room.get_characters()]
        self.assertIn(first_test_character.name, test_room_characters)
        self.assertIn(second_test_character.name, test_room_characters)
        self.assertNotIn(fake_test_character.name, test_room_characters)

    def test_remove_character(self):
        test_room = Space(name="Test Room")
        first_test_chrctr = Character(name="R2-D2")
        second_test_chrctr = Character(name="C-3PO")
        third_test_chrctr = Character(name="R4-D4")
        test_chrctrs = [first_test_chrctr, second_test_chrctr, third_test_chrctr]
        test_room.set_characters(test_chrctrs)

        test_room.remove_character(first_test_chrctr)
        test_room_chrctrs = [i.name for i in test_room.get_characters()]
        self.assertNotIn(first_test_chrctr.name, test_room_chrctrs)
        self.assertIn(second_test_chrctr.name, test_room_chrctrs)
        self.assertIn(third_test_chrctr.name, test_room_chrctrs)

if __name__ == "__main__":
    unittest.main()
