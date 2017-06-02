#!/usr/bin/env python3


DEFAULT_NAME = "Space"
DEFAULT_SHORT_DESCRIPTION = "a room."
DEFAULT_LONG_DESCRIPTION = "a large open room with disco music playing in the background."

"""
This is a base class for a space. The space is intended to be used in
a text adventure game.
"""
class Space(object):
    def __init__(self, new_id=None, name=DEFAULT_NAME, items=None, characters=None,
                 long_description=None, short_description=DEFAULT_SHORT_DESCRIPTION,
                 visited=False, exits=None):
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
        :param exits - list of Exit: A list of exits in this
               space.
        :param visible - bool: True --> this space is visible;
               False --> this space is not visible.
               Note: This can be used to hide a space from a player until
                     they have accomplished some task.
        :param locked - bool: True --> this space is locked;
               False --> this space is unlocked
               Note: This can be used to not allow a player to enter a space
                     until they have accomplished some task.
        """
        if new_id:
            self.id = new_id
        else:
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
        if exits:
            self.exits = exits
        else:
            self.exits = []
        self.visited = False

    def get_id(self):
        """Return the unique id of this space.
        """
        return self.id

    def set_id(self, new_id):
        """Set the unique id of this space.

        :param new_id - str: The unique id to set for this space
        """
        self.id = new_id

    def get_name(self):
        """Return the name of this space.
        """
        return self.name

    def set_name(self, name_to_set):
        """Set the name of this space.

        :param name_to_set - str: The name to set for this space
        """
        self.name = name_to_set

    def get_items(self):
        """Return a list of items in this space.
        """
        return self.items

    def set_items(self, new_items_list):
        """Set the list of items in this space.

        :param new_items_list - list of Item: The list of item objects in this
                                        space
        """
        self.items = new_items_list

    def add_item(self, item_to_add):
        """Add an item to this space.

        :param item_to_add - Item: The item to add to this space
        """
        self.items.append(item_to_add)
        item_to_add.location = self

    def remove_item(self, item_to_remove):
        """Remove an item from this space.

        :param item_to_remove - Item: The item to remove from this space
        """
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)

    def get_exits(self):
        """Return a list of exits in this space.
        """
        return self.exits

    def set_exits(self, new_exit_list):
        """Set the list of exits in this space.

        :param new_exit_list - list of Exit: The list of exits to set for this
                                      space
        """
        self.exits = new_exit_list

    def add_exit(self, exit):
        """Add an exit to this space.

        :param exit - Exit: The exit to add to this space
        """
        self.exits.append(exit)

    def remove_exit(self, exit_to_remove):
        """Remove an exit from this space.

        :param exit_to_remove - Exit: The exit to remove from this space
        """
        if exit_to_remove in self.exits:
            self.exits.remove(exit_to_remove)

    def get_characters(self):
        """Return a list of characters in this space.
        """
        return self.characters

    def set_characters(self, new_characters_list):
        """Set the list of characters in this space.

        :param new_character_list - list of Character: The list of characters in
                                                this space
        """
        self.characters = new_characters_list

    def add_character(self, character_to_add):
        """Add a character to this space.

        :param character_to_add - Character: The character to add to this space
        """
        self.characters.append(character_to_add)

    def remove_character(self, character_to_remove):
        """Remove a character from this space.

        :param character_to_remove - Character: The character to remove from this
                                         space
        """
        if character_to_remove in self.characters:
            self.characters.remove(character_to_remove)

    def get_visited(self):
        """Return whether the player has visited this space.
        """
        return self.visited

    def set_visited(self, new_visited):
        """Set whether the player has visited this space.

        :param new_visited - bool: Whether the player has visited this space
        """
        self.visited = new_visited

    def print_description(self, index):
        """Print the description of this space for the given index. If the
        space has been visited, a short description is printed. If the space
        has not been visited, a more detailed description is printed.

        :param index - int: The index of the description to print for this space
        """
        if self.visited:
            print("\n{0}".format(self.short_description))
        else:
            print("\n{0}".format(self.long_description[index]))

    def print_short_description(self):
        """Print the short description of this space.
        """
        print("\n{0}".format(self.short_description))

    def print_long_description(self, index):
        """Print a detailed description of this space, for the given index.

        :param index - int: The index of the description to print for this space
        """
        print("\n{0}".format(self.long_description[index]))

    def print_exits(self):
        """Print the direction and description of all exits visible in this
        space.
        """
        for exit in self.exits:
            if exit.is_visible():
                print("{0} is {1}".format(exit.get_direction(), exit.get_description()).capitalize())

    def print_items(self):
        """Print the name of all visible items in this space.
        """
        print("Items: ", end="")
        for item in self.items:
            if item.get_visible():
                print("{0}  ".format(item.get_name()), end="")
        print()

    def print_characters(self):
        """Print the names of all characters in this space.
        """
        print("Characters: ", end="")
        for character in self.characters:
            print("{0}  ".format(character.get_name()), end="")
        print()

    def to_json_dict(self):
        """Write the fields of this space to a JSON dict. For objects, their
        IDs are written to the dict.
        """
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['long_description'] = self.long_description
        json_dict['characters'] = [c.get_id() for c in self.characters]
        json_dict['items'] = [i.get_id() for i in self.items]
        json_dict['short_description'] = self.short_description
        json_dict['exits'] = [e.get_id() for e in self.exits]
        json_dict['visited'] = self.visited
        return json_dict

    def print_details(self, event_index):
        """Print details about this event. Description, exits, characters,
        and items.
        """
        self.print_description(event_index)
        self.print_exits()
        print("\n", end="")
        self.print_characters()
        self.print_items()
