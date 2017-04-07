#!/usr/bin/env python

DEFAULT_NAME = "Item"
DEFAULT_DESCRIPTION = "This is an item."

class Item(object):
    """
    This is a base class for an item. Items are intended to be placed in
    spaces, carried by characters, or carried by a player in a text
    adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, size=0, description=DEFAULT_DESCRIPTION,
                 visible=True, locked=False):
        """
        :param name - str: The name of this item.
        :param size - int: The size of this item. This can be any metric
               relative to a player or character's capacity to hold items.
               i.e. lbs, kg, gallons, GB, etc.
        :param description - str: A description of this item."
        :param visible - boolean: True --> This item is visible.
               False --> This item is not visible.
               Note: This can be used to hide an item from a player until
                     they have accomplished some task.
        :param locked - boolean: True --> This item can be picked up.
               False --> This item cannot be picked up.
               Note: This can be used to not allow a player to pick up
                     an item until they have accomplished some task.
        """
        self.name = name
        self.size = size
        self.description = description
        self.visible = visible
        self.locked = locked


    #TODO getters and setters for all properties above.

    def print_details(self):
        print("\nName: {}".format(self.name.upper()))
        print("Size: {}".format(self.size))
        print("Description: {}".format(self.description))