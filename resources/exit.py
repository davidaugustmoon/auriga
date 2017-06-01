#!/usr/bin/env python3

import resources.space

DEFAULT_NAME = "Door"
DEFAULT_DESCRIPTION = "a flimsy wooden door."
DIRECTIONS = ["north", "south", "east", "west", "up", "down"]

class Exit(object):
    def __init__(self, new_id=None, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION,
                 space=None, locked=False, visible=True, unlock_item=None,
                 direction="north"):
        """
        An exit to a Space.
        :param id - int: An auto-generated unique id for this object.
        :param str - name: The name of the exit.
               e.g. "Door", "Tunnel"
        :param str - description: A detailed description of the exit.
               e.g. "A large steel door", "A long dark tunnel"
        :param Space - space: The Space that this exit leads to.
        :param bool - locked: True --> Exit is locked, and can't be used
               unless the player holds/uses the 'unlock_item'
               False --> Exit is unlocked.
        :param bool - visible: True --> Exit is visible to the player.
               False --> Exit is not visible to the player.
        :param Item - unlock_item: The item that is required to unlock this
               exit.
        :param str - direction: The direction of the Exit from the Space it exits.
        """
        if new_id:
            self.id = new_id
        else:
            self.id = id(self)
        self.name = name
        self.description = description
        self.space = space
        self.locked = locked
        self.visible = visible
        self.unlock_item = unlock_item
        self.direction = direction

    def get_id(self):
        """Return the unique id of this exit.
        """
        return self.id

    def set_id(self, new_id):
        """Set the unique id of this exit.

        new_id - str: The unique id to set for this exit
        """
        self.id = new_id

    def get_name(self):
        """Return the name of this exit. This is intended to be a short
        description of the exit. "steel door", "hole", "large opening", etc.
        """
        return self.name

    def set_name(self, new_name):
        """Set the name of the exit.

        new_name - str: The name to set for this exit.
        """
        self.name = new_name

    def get_description(self):
        """Return a description of this exit.
        """
        return self.description

    def get_space(self):
        """Return the space that this exit leads to.
        """
        return self.space

    def is_locked(self):
        """Return if this exit is locked to a player.
        """
        return self.locked

    def set_is_locked(self, lock_value):
        """Set whether this exit is locked to the player.

        lock_value - Bool: Whether this exit is locked to the player
        """
        self.locked = lock_value

    def is_visible(self):
        """Return whether this exit is visible to the player.
        """
        return self.visible

    def set_is_visible(self, visible_value):
        """Set whether this exit is visible to the player.

        visible_value - Bool: Whether this exit is visible to the player
        """
        self.visible = visible_value

    def get_unlock_item(self):
        """Return the item required to unlock this exit to the player.
        """
        return self.unlock_item

    def get_direction(self):
        """Return the cardinal direction of this exit. (north, south,
        east, west, up, down)
        """
        return self.direction

    def to_json_dict(self):
        """Write the fields of this exit to a json dict. Writes any object's
        id to the dict.
        """
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['description'] = self.description
        json_dict['space'] = self.space.get_id()
        json_dict['locked'] = self.locked
        json_dict['visible'] = self.visible
        if self.unlock_item:
            json_dict['unlock_item'] = self.unlock_item.get_id()
        else:
            json_dict['unlock_item'] = None
        json_dict['direction'] = self.direction
        return json_dict
