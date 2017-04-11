#!/usr/bin/env python

from __future__ import print_function

DEFAULT_NAME = "Space"
DEFAULT_SHORT_DESCRIPTION = "Space."

"""
This is a base class for a space. The space is intended to be used in
a text adventure game.
"""
class Space(object):
    def __init__(self, name=DEFAULT_NAME, items=None, characters=None,
                 long_description=None, short_description=DEFAULT_SHORT_DESCRIPTION,
                 visited=False):
        """
        :param name - str: The name of this space.
        :param items - list of Item: The list of Item objects in this space.
        :param characters - list of Character: The list of Character objects
               in this space.
        :param long_description - list of str: A list of detailed descriptions
               of this space. A list of descriptions allows for indexing based
               on the state of the space.
        :param short_description - str: A brief description of this space.
        :param exits - list of exits: A list of exits in this
               space.
        :param visible - boolean: True --> this space is visible;
               False --> this space is not visible.
               Note: This can be used to hide a space from a player until
                     they have accomplished some task.
        :param locked - boolean: True --> this space is locked;
               False --> this space is unlocked
               Note: This can be used to not allow a player to enter a space
                     until they have accomplished some task.
        """
        self.name = name
        if items:
            self.items = items
        else:
            self.items = []
        if characters:
            self.characters = characters
        else:
            self.characters = []
        if long_description:
            self.long_description = long_description
        else:
            self.long_description = []
        self.short_description = short_description
        self.exits = []
        self.visited = False
    #TODO getters and setters for all properties above

    def get_name(self):
        return self.name

    def set_name(self, name_to_set):
        self.name = name_to_set

    def get_items(self):
        return self.items

    def set_items(self, new_items_list):
        self.items = new_items_list

    def add_exit(self, exit):
        self.exits.append(exit)

    def add_item(self, item_to_add):
        self.items.append(item_to_add)
        item_to_add.location = self

    def add_character(self, character_to_add):
        self.characters.append(character_to_add)
        character_to_add.location = self

    def print_short_description(self):
        print("\n{0}".format(self.short_description))

    def print_long_description(self, index):
        print("\n{0}".format(self.long_description[index]))

    def print_exits(self):
        print("Exits: ", end="")
        for counter, e in enumerate(self.exits):
            print(counter + 1, ".", e.name, "  ", end="")
        print()

    def print_items(self):
        print("Items: ", end="")
        for counter, i in enumerate(self.items):
            print(counter + 1, ".", i.name, "  ", end="")
        print()

    def print_characters(self):
        print("Characters: ", end="")
        for counter, c in enumerate(self.characters):
            print(counter + 1, ".", c.name, "  ", end="")
        print()

    def print_details(self):
        self.print_exits()
        self.print_items()
        self.print_characters()