#!/usr/bin/env python3

import space

DEFAULT_NAME = "Door"
DEFAULT_DESCRIPTION = "a flimsy wooden door."
DIRECTIONS = ["north", "south", "east", "west", "up", "down"]

class Exit(object):
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION,
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
        self.id = id(self)
        self.name = name
        self.description = description
        self.space = space
        self.locked = locked
        self.visible = visible
        self.unlock_item = unlock_item
        self.direction = direction

    def get_id(self):
        """
        Get the unique id of this object

        :return int: The unique id of this object.
        """
        return self.id

    def get_name(self):
        """
        Get the name of the exit.

        :return str: The name of the exit.
        """
        return self.name

    def set_name(self, new_name):
        """
        Set the name of the exit.

        :param str - new_name: The name to set the exit to.
        """
        self.name = new_name

    def get_description(self):
        """
        Get a detailed description of the exit.

        :return str: A detailed description of the exit.
        """
        return self.description

    def get_space(self):
        """
        Get the space that this exit leads to.

        :return Space: The Space that this exit leads to.
        """
        return self.space

    def is_locked(self):
        """
        Get whether this exit is locked.

        :return Bool: True if the exit is locked; False if the exit is not locked.
        """
        return self.locked

    def is_visible(self):
        """
        Get whether this exit is visible.

        :return Bool: True if the exit is visible; False if the exit is not visible.
        """
        return self.visible

    def get_unlock_item(self):
        """
        Get the item required to unlock this exit.

        :return Item: The Item required to unlock this exit.
        """
        return self.unlock_item

    def get_direction(self):
        """
        Get the cardinal direction of this exit in a Space.

        :return str: The cardinal direction of this exit in a Space.
        """
        return self.direction

    def to_json_dict(self):
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
