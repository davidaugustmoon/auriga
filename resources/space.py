#!/usr/bin/env python3


DEFAULT_NAME = "Space"
DEFAULT_SHORT_DESCRIPTION = "a room."
DEFAULT_LONG_DESCRIPTION = "a large open room with disco music playing in the background."

"""
This is a base class for a space. The space is intended to be used in
a text adventure game.
"""
class Space(object):
    def __init__(self, name=DEFAULT_NAME, items=None, characters=None,
                 long_description=None, short_description=DEFAULT_SHORT_DESCRIPTION,
                 visited=False):
        """
        :param id - int: An auto-generated unique id for this object.
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
        self.id = id(self)
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

    def get_id(self):
        """
        Get the unique id of this object

        :return int: The unique id of this object.
        """
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name_to_set):
        self.name = name_to_set

    def get_items(self):
        return self.items

    def set_items(self, new_items_list):
        self.items = new_items_list

    def add_item(self, item_to_add):
        self.items.append(item_to_add)
        item_to_add.location = self

    def remove_item(self, item_to_remove):
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)

    def get_exits(self):
        return self.exits

    def set_exits(self, new_exit_list):
        self.exits = new_exit_list

    def add_exit(self, exit):
        self.exits.append(exit)

    def remove_exit(self, exit_to_remove):
        if exit_to_remove in self.exits:
            self.exits.remove(exit_to_remove)

    def get_characters(self):
        return self.characters

    def set_characters(self, new_characters_list):
        self.characters = new_characters_list

    def add_character(self, character_to_add):
        self.characters.append(character_to_add)
        character_to_add.location = self

    def remove_character(self, character_to_remove):
        if character_to_remove in self.characters:
            self.characters.remove(character_to_remove)

    def get_visited(self):
        return self.visited

    def set_visited(self, new_visited):
        self.visited = new_visited

    def print_description(self, index):
        if self.visited:
            print("\n{0}".format(self.short_description))
        else:
            print("\n{0}".format(self.long_description[index]))

    def print_short_description(self):
        print("\n{0}".format(self.short_description))

    def print_long_description(self, index):
        print("\n{0}".format(self.long_description[index]))

    def print_exits(self):
        for exit in self.exits:
            print("{0} is {1}".format(exit.get_direction(), exit.get_description()).capitalize())

    def print_items(self):
        print("Items: ", end="")
        for item in self.items:
            print("{0}  ".format(item.get_name()), end="")
        print()

    def print_characters(self):
        print("Characters: ", end="")
        for character in self.characters:
            print("{0}  ".format(character.get_name()), end="")
        print()

    def to_json_dict(self):
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['long_description'] = self.long_description
        json_dict['characters'] = [c.get_id() for c in self.characters]
        json_dict['items'] = [i.get_id() for i in self.items]
        json_dict['short_description'] = self.short_description
        json_dict['exits'] = [e.get_id() for e in self.exits]
        return json_dict

    def print_details(self, event_index):
        self.print_description(event_index)
        self.print_exits()
        print("\n", end="")
        self.print_characters()
        self.print_items()
