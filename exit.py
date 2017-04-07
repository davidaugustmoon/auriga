#!/usr/bin/env python

import space

DEFAULT_NAME = "Door"
DEFAULT_DESCRIPTION = "A wooden door."

class Exit(object):
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION, space=None, locked=False, visible=True, unlock_item=None):
        """
        An exit to a Space.
        :param str - name: The name of the exit.
               e.g. "Door", "Tunnel"
        :param str - description: A detailed description of the exit.
               e.g. "A large steel door", "A long dark tunnel"
        :param Space - space: The Space that is connected to.
        :param bool - locked: True --> Exit is locked, and can't be used
               unless the player holds/uses the 'unlock_item'
               False --> Exit is unlocked.
        :param bool - visible: True --> Exit is visible to the player.
               False --> Exit is not visible to the player.
        :param Item - unlock_item: The item that is required to unlock this
               exit.
        """
        self.name = name
        self.description = description
        self.space = space
        self.locked = locked
        self.visible = visible
        self.unlock_item = unlock_item