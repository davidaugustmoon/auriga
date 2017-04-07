#!/usr/bin/env python

from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player


def main():
    # Create spaces
    s1 = Space(name="space_one")
    s2 = Space(name="space_two")
    s3 = Space(name="space_three")
    s4 = Space(name="space_four")

    i1 = Item(name="item_one")
    i2 = Item(name="item_two")
    i3 = Item(name="item_three")
    i4 = Item(name="item_four")

    c1 = Character(name="character_one")
    c2 = Character(name="character_two")
    c3 = Character(name="character_three")
    c4 = Character(name="character_four")

    p1 = Player(name="player_one")
    p1.set_location(s3)
    p1.add_item(i3)

    p2 = Player(name="player_two")
    p2.set_location(s4)

    p1.print_details()
    p2.print_details()


    s1.add_item(i3)
    s1.add_character(c1)
    s1.add_connection(s2)

    s1.set_name("A New Name")

    s1.print_details()
    s2.print_details()
    s3.print_details()
    s4.print_details()



    # kitchen = Space(name="Kitchen", short_description="A clean and modern kitchen.")
    # dungeon = Space(name="Dungeon", short_description="A dark and muggy stone room.")
    # bathroom = Space(name="Bathroom", short_description="A smelly and dirty stall.")

    # # Connect spaces
    # kitchen.add_connection(dungeon)
    # bathroom.add_connection()

    # # Create characters
    # mike = Character(name="Mike", description="An old man.")

    # # Create items
    # key = Item(name="key", size=10, description="A small shiny key.")
    # # hammer = Item(name="hammer", size=50, description="A large sledge-hammer.")

    # # Add items to spaces
    # # kitchen.add_item(key)
    # # dungeon.add_item(hammer)

    # # Add characters to spaces
    # bathroom.add_character(mike)

    # # Items
    # key.print_details()
    # # hammer.print_details()

    # # Spaces
    # kitchen.print_details()
    # dungeon.print_details()
    # bathroom.print_details()

    # print("\nSPACE OBJECTS")
    # print(kitchen)
    # print(dungeon)
    # print(bathroom)
    # print("\n")


if __name__ == "__main__":
    main()
