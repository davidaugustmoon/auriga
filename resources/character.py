#!/usr/bin/env python3

import resources.space

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
        :param id - int: An auto-generated unique id for this object.
        :param name - str: The name of this character.
        :param description - str: A description of this character.
        :param capacity - int: The maximum item capacity this character can
               carry.
        :param location - Space: The current location of this character.
        :param response - list of str: This character's responses when 
               spoken to by a player. The current response is indexed by the
               player event enum list.
        """
        self.id = id(self)
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location
        if response:
            self.response = response
        else:
            self.response = []

    def get_id(self):
        """
        Get the unique id of this object

        :return int: The unique id of this object.
        """
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def get_location(self):
        return self.location

    def set_location(self, new_location):
        self.location = new_location

    def get_response(self):
        return self.response

    def to_json_dict(self):
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['description'] = self.description
        json_dict['capacity'] = self.capacity
        json_dict['location'] = self.location.get_id()
        json_dict['response'] = self.response
        return json_dict

    def print_details(self):
        """
        For testing
        """
        print("Id: {}".format(self.id))
        print("Name: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))

    def print_response(self, index):
        print("\n[{0}] {1}".format(self.name.upper(), self.response[index]))
