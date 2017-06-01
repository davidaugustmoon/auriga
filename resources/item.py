#!/usr/bin/env python3


DEFAULT_DESCRIPTION = "an item"
DEFAULT_NAME = "default name"

class Item(object):
    """
    This is a base class for an item. Items are intended to be placed in
    spaces, carried by characters, or carried by a player in a text
    adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, new_id=None, weight=1, description=DEFAULT_DESCRIPTION,
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
        if new_id:
            self.id = new_id
        else:
            self.id = id(self)
        self.name = name
        self.weight = weight
        self.description = description
        self.visible = visible
        self.locked = locked

    def get_id(self):
        """Return the unique id of this item.
        """
        return self.id

    def set_id(self, new_id):
        """Set the unique id of this item.

        new_id - str: A unique id for this item
        """
        self.id = new_id

    def get_name(self):
        """Return the name of this item.
        """
        return self.name

    def get_weight(self):
        """Return the weight of this item.
        """
        return self.weight

    def get_description(self):
        """Return a description of this item.
        """
        return self.description

    def get_visible(self):
        """Return whether this item is visible to the player.
        """
        return self.visible

    def set_visible(self, visible_value):
        """Set whether this item is visible to the player.
        
        visible_value - Bool: Whether the player can see this item
        """
        self.visible = visible_value

    def get_locked(self):
        """Return whether this item is locked to the player.
        True  --> Player cannot pick up the item
        False --> Player can pick up the item
        """
        return self.locked

    def set_locked(self, locked_value):
        """Set whether the player can pick up this item.

        locked_value - Bool: Whether the player can pick up this item
        """
        self.locked = locked_value

    def to_json_dict(self):
        """Write the fields of this item to a json dict.
        """
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['weight'] = self.weight
        json_dict['description'] = self.description
        json_dict['visible'] = self.visible
        json_dict['locked'] = self.locked
        return json_dict

    def print_details(self):
        """Print details about this item.
        For testing
        """
        print("\nId: {}".format(self.id))
        print("Name: {}".format(self.name.upper()))
        print("Size: {}".format(self.weight))
        print("Description: {}".format(self.description))
