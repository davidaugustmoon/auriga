#!/usr/bin/env python

from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit


def main():
    # Create spaces
    s1 = Space(name="space_one")
    s2 = Space(name="space_two")
    s3 = Space(name="space_three")
    s4 = Space(name="space_four")

    # Create Items
    i1 = Item(name="item_one")
    i2 = Item(name="item_two")
    i3 = Item(name="item_three")
    i4 = Item(name="item_four")

    # Create Characters
    c1 = Character(name="character_one")
    c2 = Character(name="character_two")
    c3 = Character(name="character_three")
    c4 = Character(name="character_four")

    # Create Player
    p1 = Player(name="player_one")
    p1.set_location(s3)
    p1.add_item(i3)

    # Create Exits
    # Note: Will probably need to crate recipricol exits for all exits in the
    #       actual game, but this is just for testing.
    #s1 exits
    e1_3 = Exit(name="Steel door", space=s3)
    s1.add_exit(e1_3)
    e1_4 = Exit(name="Long tunnel", space=s4)
    s1.add_exit(e1_4)
    #s2 exits
    e2_1 = Exit(name="Large hole", space=s1)
    s2.add_exit(e2_1)
    e2_4 = Exit(name="Elevator", space=s4)
    s2.add_exit(e2_4)

    # Place items in Spaces
    s2.add_item(i1)
    s2.add_item(i4)
    s4.add_item(i2)

    # Place characters in spaces
    s1.add_character(c1)
    s1.add_character(c2)
    s2.add_character(c3)
    s3.add_character(c4)


    s1.print_details()
    s2.print_details()
    s3.print_details()
    s4.print_details()


if __name__ == "__main__":
    main()
