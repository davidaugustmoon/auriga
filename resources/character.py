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
    def __init__(self, new_id=None, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION, response=None):
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
        if new_id:
            self.id = new_id
        else:
            self.id = id(self)
        self.name = name
        self.description = description
        if response:
            self.response = response
        else:
            self.response = []

    def get_id(self):
        """Return the unique id for this character.
        """
        return self.id

    def set_id(self, new_id):
        """Set the unique id for this character.

        :param new_id - str: The unique id to set for this character.
        """
        self.id = new_id

    def get_name(self):
        """Return the name of this character.
        """
        return self.name

    def set_name(self, new_name):
        """Set the name of this character.

        :param new_name - str: The name to set for this character
        """
        self.name = new_name

    def get_description(self):
        """Return a description of this character.
        """
        return self.description

    def set_description(self, new_description):
        """Set the description of this character.

        :param new_description - str: The description to set for this character
        """
        self.description = new_description

    def get_response(self):
        """Return a list of this character's responses. The index in the
        response list corresponds to the event_status int in a game object.
        """
        return self.response

    def set_response(self, response_list):
        """Set the response list for this character.

        :param response_list - list of str: The list of repsonses for this character
                                     in a game
        """
        self.response = response_list

    def to_json_dict(self):
        """Write the fields of this character to a JSON dict.
        """
        json_dict = {}
        json_dict['id'] = self.id
        json_dict['name'] = self.name
        json_dict['description'] = self.description
        json_dict['response'] = self.response
        return json_dict

    def print_details(self):
        """Print details about this character.
        For testing
        """
        print("Id: {}".format(self.id))
        print("Name: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))

    def print_response(self, index):
        """Print this character's reponse for the given index.

        :param index - int: The index of the response to print
        """
        print("\n[{0}] {1}".format(self.name.upper(), self.response[index]))
