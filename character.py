#!/usr/bin/env python

import space

DEFAULT_NAME = "Character"
DEFAULT_DESCRIPTION = "This is a character."
DEFAULT_RESPONSE = "Hi..."

class Character(object):
    """
    This is a base class for a character. It is intended to be used in a
    text adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION,
                 capacity=0, location=None, response=DEFAULT_RESPONSE):
        """
        :param name - str: The name of this character.
        :param description - str: A description of this character.
        :param capacity - int: The maximum item capacity this character can
               carry.
        :param location - Space: The current location of this character.
        :param response - str: This character's response when spoken to by
               a player.
        """
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location
        self.response = response

    def print_details(self):
        print("Name: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))


    #TODO getters and setters for all of the properties above.