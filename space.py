#!/usr/bin/env python

DEFAULT_NAME = "Space"
DEFAULT_LONG_DESCRIPTION = "This is a space."
DEFAULT_SHORT_DESCRIPTION = "Space."

"""
This is a base class for a space. The space is intended to be used in
a text adventure game.
"""
class Space(object):
    def __init__(self, name=DEFAULT_NAME, long_description=DEFAULT_LONG_DESCRIPTION,
                 short_description=DEFAULT_SHORT_DESCRIPTION, visible=True, locked=False):
        """
        :param name - str: The name of this space.
        :param items - list of Item: The list of Item objects in this space.
        :param characters - list of Character: The list of Character objects
               in this space.
        :param long_description - str: A detailed description of this space.
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
        self.items = []
        self.characters = []
        self.long_description = long_description
        self.short_description = short_description
        self.exits = []
        self.visible = visible
        self.locked = locked
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

    def add_character(self, character_to_add):
        self.characters.append(character_to_add)

    def print_short_description(self):
        print(self.short_description)

    def print_long_description(self):
        print(self.long_description)

    def print_details(self):
        print("\nName: {}".format(self.name.upper()))
        print("Exits: {}".format([c.name for c in self.exits]))
        print("Items: {}".format([i.name for i in self.items]))
        print("Characters: {}".format([c.name for c in self.characters]))
        print("Description: {}".format(self.short_description))