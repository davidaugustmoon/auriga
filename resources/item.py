#!/usr/bin/env python3


DEFAULT_DESCRIPTION = "an item"

class Item(object):
    """
    This is a base class for an item. Items are intended to be placed in
    spaces, carried by characters, or carried by a player in a text
    adventure game.
    """
    def __init__(self, name, weight=5, description=DEFAULT_DESCRIPTION,
                 visible=True, locked=False):
        """
        :param id - int: An auto-generated unique id for this object.
        :param name - str: The name of this item.
        :param weight - int: The weight of this item. This can be any metric
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
        self.id = id(self)
        self.name = name
        self.weight = weight
        self.description = description
        self.visible = visible
        self.locked = locked


    #TODO setters for all properties above.
    def get_id(self):
        """
        Get the unique id of this object

        :return int: The unique id of this object.
        """
        return self.id

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_description(self):
        return self.description

    def get_visible(self):
        return self.visible

    def get_locked(self):
        return self.locked

    def to_json_dict(self):
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['weight'] = self.weight
        json_dict['description'] = self.description
        json_dict['visible'] = self.visible
        json_dict['locked'] = self.locked
        return json_dict

    def print_details(self):
        """
        For testing
        """
        print("\nId: {}".format(self.id))
        print("Name: {}".format(self.name.upper()))
        print("Size: {}".format(self.weight))
        print("Description: {}".format(self.description))
