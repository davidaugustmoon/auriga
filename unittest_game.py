#!/usr/bin/env python3

import unittest
from resources.game import Game
from resources.player import Player
from resources.item import Item
from resources.space import Space
from resources.exit import Exit
from resources.character import Character
import generate_auriga


class TestGame(unittest.TestCase):
    """Tests for game.py"""

    """
    Setup function
    """

    """
    Test get_object_by_name()
    1. empty list of objects -> return None
    2. object not in list -> return None
    3. empty string object name -> None
    4. positive test of object name in list
    """
    def test_get_object_by_name(self):
        rdm_player = Player(name="Rick")
        rdm_item = Item(name="Portal Gun")
        rdm_space = Space(name="Garage")
        rdm_exit = Exit(name="Portal")
        rdm_character = Character(name="Morty")
        rdm_test_objects = [rdm_player, rdm_item, rdm_space, rdm_exit, rdm_character]
        test_game = Game(rdm_player)

        test_result = test_game.get_object_by_name(rdm_test_objects, rdm_player.name)
        self.assertEqual(test_result, rdm_player)

        test_result = test_game.get_object_by_name(rdm_test_objects, "Portal")
        self.assertEqual(test_result, rdm_exit)
        self.assertNotEqual(test_result, rdm_item)

        test_result = test_game.get_object_by_name(rdm_test_objects, "Portal ")
        self.assertNotEqual(test_result, rdm_item)
        self.assertNotEqual(test_result, rdm_exit)

if __name__ == "__main__":
    unittest.main()
