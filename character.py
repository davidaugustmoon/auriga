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
                 capacity=0, location=None, response=None):
        """
        :param name - str: The name of this character.
        :param description - str: A description of this character.
        :param capacity - int: The maximum item capacity this character can
               carry.
        :param location - Space: The current location of this character.
        :param response - list of str: This character's responses when 
               spoken to by a player. The current response is indexed by the
               player event enum list.
        """
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location
        if response:
            self.response = response
        else:
            self.response = []

    def print_details(self):
        print("Name: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))

    def print_response(self, index):
        print("[{0}] {1}".format(self.name.upper(), self.response[index]))


    #TODO getters and setters for all of the properties above.