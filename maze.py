#!/usr/bin/env python

import space

class Maze(object):
    """
    This is a base class for a Maze or Map in a text adventure game. It is
    comprised of Spaces.
    Note: 'Maze' was used instead of 'Map' becuase map is a keyword in python.
    """
    def __init__(self, spaces=[]):
        """
        :param spaces - list of Space: This is a list of all spaces that make
               up this Maze.
        """
        self.spaces = spaces

    #TODO getters and setters for all properties above.

    def add_space(self, space_to_add):
        """
        Add a space to this Maze.
        :param space_to_add - Space: The Space to add to this Maze.
        :param connections - list of Space: A list of all spaces that the
               space_to_add is connected to.
        """
        self.spaces.append(space_to_add)

    def connect_two_spaces(self, space1, space2):
        """
        Create a connection between two spaces in this maze.
        :param space1 - Space: A space in this maze.
        :param space2 - Space: A space in this maze.
        """
        space1.add_connection(space2)
