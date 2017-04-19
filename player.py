#!/usr/bin/env python

from __future__ import print_function

import item
import space

DEFAULT_NAME = "PLAYER 1"
DEFAULT_DESCRIPTION = "This is a player."

class Player(object):
    """
    This is a base class for a player. It is intended to be used in a
    text adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION,
                 capacity=0, location=None, alive=True, energy=100):
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
        self.energy = energy

    def get_name(self):
        """
        Get the name of the player

        :return str: The name of the player
        """
        return self.name

    def set_name(self, new_name):
        """
        Set the name of the player
        
        :param str - new_name: The name to assign the player.
        """
        self.name = new_name

    def get_description(self):
        """
        Get the player description

        :return str: A description of the player
        """
        return self.description

    def set_description(self, new_description):
        """
        Set the description of the player

        :param str - new_description: The description to set for the player
        """
        self.description = new_description

    def get_capacity(self):
        """
        Get the player's maximum carrying capacity

        :return int: The maximum weight a player can carry.
        """
        return self.capacity

    def set_capacity(self, new_capacity):
        """
        Set the player's maximum carrying capacity

        :param int - new_capacity: The maximum carrying capacity to set for the player
        """
        self.capacity = new_capacity

    def get_items(self):
        """
        Get the list of items currently carried by the player

        :return list of Item: The list of Item objects currently carried by the player
        """
        return self.items

    def set_items(self, new_items_list):
        """
        Set the list of Item objects currently carried by the player

        :param list of Item - new_item_list: The new list of Item objects carried by the player
        """
        self.items = new_items_list

    def add_item(self, item_to_add):
        """
        Add an Item to the player's currently carried items

        :param Item - item_to_add: The Item to add to the player's currently carried items
        """
        self.items.append(item_to_add)

    def remove_item(self, item_to_remove):
        """
        Remove an Item from the player's currently carried items

        :param Item - item_to_remove: The Item to remove from the player's currently carried items
        """
        if item_to_remove in self.items:
            self.item.remove(item_to_remove)

    def get_item_names(self):
        """
        Get a list of the names of all of the Item objects currently carried by the player

        :return list of str: The list of Item names of all of the objects carried by the player
        """
        return [i.name for i in self.items]

    def get_items_total_weight(self):
        total_weight = 0
        for i in self.items:
            total_weight += i.get_weight()
        return total_weight

    def get_location(self):
        """
        Get the player's current location

        :return Space: The Space the player currently occupies
        """
        return self.location

    def set_location(self, new_location):
        """
        Set the player's current location

        :param Space - new_location: The new Space the player will occupy
        """
        self.location = new_location

    def get_alive(self):
        """
        Get whether the player is currently alive.

        :return Bool: True if the player is alive; False if the player is not alive
        """
        return self.alive

    def set_alive(self, new_alive):
        """
        Set whether the player is alive or not

        :param Bool - new_alive: True will set the player to be alive; False will set
                                 the player to not be alive
        """
        self.alive = new_alive

    def get_energy(self):
        """
        Get a player's current energy level

        :return int: The player's current energy level
        """
        return self.energy

    def set_energy(self, new_energy):
        """
        Set a player's energy level

        :param int - new_energy: The energy level to set for the player
        """
        if new_energy < 0:
            self.energy = 0
        else:
            self.energy = new_energy

    def print_details(self):
        """
        Print details about the player
        """
        print("\nName: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))
        print("Carrying: {0}/{1}".format(self.get_items_total_weight(), self.capacity))
        print("Items: {}".format(self.get_item_names()))
        print("location: {}".format(self.location.name))
        print("Is alive: {}".format(self.alive))