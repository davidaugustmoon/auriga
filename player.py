#!/usr/bin/env python

import item
import space

DEFAULT_NAME = "Player 1"
DEFAULT_DESCRIPTION = "This is a player."

class Player(object):
    """
    This is a base class for a player. It is intended to be used in a
    text adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION,
                 capacity=0, location=None, alive=True):
        """
        :param name - str: The name of this player.
        :param description - str: A description of this player.
        :param capacity - int: The maximum item capacity this player can
               carry.
        :param items - list of Item: A list of Items the player is carrying.
        :param location - Space: The current location of this player.
        :param alive - bool: True --> This player is alive.
               False --> This player is dead.
               Note: This may be used to terminate a game, or change a game
                     state.
        """
        self.name = name
        self.description = description
        self.capacity = capacity
        self.items = []
        self.location = location
        self.alive = alive

    def add_item(self, item_to_add):
        self.items.append(item_to_add)

    def set_location(self, new_location):
        self.location = new_location

    def print_details(self):
        print("\nName: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))
        print("Capacity: {}".format(self.capacity))
        print("Items: {}".format([i.name for i in self.items]))
        print("location: {}".format(self.location.name))
        print("Is alive: {}".format(self.alive))

    #TODO getters and setters for all of the properties above.
