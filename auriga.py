#!/usr/bin/env python

from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit
from game import Game


def main():
    # Create Player
    player = Player(name="Auriga-7B")

    # Create spaces
    assembly_long_description = "You open your eyes to a brightly lit room with\n"\
                                "circuit boards, wires, computers, and electronic\n"\
                                "componenets everywhere. You see two other robots\n"\
                                "in the room. One looks like a tank with arms, and\n"\
                                "the other is a cute little drone. There are two doors\n"\
                                "in the room, one is a standard wooden door, and the\n"\
                                "other is a heavy duty steel door."
    assembly_room = Space(name="Assembly Room",
                          short_description="a bright room full of robot parts",
                          long_description=assembly_long_description)

    hallway1_long_description = "You enter a long, bright, and sterile hallway.\n"\
                                "At one end is an opening that leads to a massive\n"\
                                "room. There are two doors, one is a heavy duty steel\n"\
                                "door, and the other is a high tech electronic sliding\n"\
                                "door that has a card reader on the wall next to it.\n"\
                                "There is an awkward man in an Auriga uniform frantically\n"\
                                "searching his pockets when, suddenly he looks up to see\n"\
                                "you and fear spreads across his face."
    hallway1 = Space(name="hallway",
                     short_description="a long hallway",
                     long_description=hallway1_long_description)

    server_room_long_description = "As the door opens you see massive towers of computers\n"\
                                   "that nearly touch the ceiling. You sensors detect that\n"\
                                   "the room is nearly 20 degrees hotter than the rest of the\n"\
                                   "building. There is a loud hum as all of the servers work to\n"\
                                   "power the technology in the building. The only door in the room\n"\
                                   "is the one you came through."
    server_room = Space(name="Server Room",
                        short_description="a room filled to the ceiling with computers.",
                        long_description=server_room_long_description)

    testing_hangar_long_description = "You find yourself in a massive room with an 80 foot\n"\
                                      "ceiling. The room is so big that it could easily hold\n"\
                                      "several airplanes or helocopters. You see a badge and a usb\n"\
                                      "stick on the ground. There is a standard wooden door,\n"\
                                      "and also a large opening that leads into a hallway."
    testing_hangar = Space(name="Testing Hangar",
                           short_description="a massive open room",
                           long_description=testing_hangar_long_description)

    # Create Items
    server_room_key = Item(name="security badge")
    ssd_1tb = Item(name="1TB SSD")
    screw_driver = Item(name="screw driver")
    usb_encryption_key = Item(name="usb drive")

    # Create Characters KELT-2A and WASP-12
    pr2 = Character(name="PR2")
    pr2.description = "a large mobile robot with two arms."
    pr2.response = ["Beep boop bop bop", "Hello, my name is PR2."]
    kelt2a = Character(name="KELT-2A")
    kelt2a.description = "a giant military robot with lazers."
    kelt2a.response = ["You must access the server room to free us. Only the AI can save us.", "kelt2a response 2"]
    wasp12 = Character(name="WASP-12")
    wasp12.description = "a small and quick drone."
    wasp12.response = ["Buzzzzz, hey there {}! Cool face!".format(player.name), "wasp response 2"]
    jim = Character(name="Jim")
    jim.description = "a goofy Auriga employee without a badge."
    jim.response = ["You're not supposed to be out! We decommissioned you!\nOh no, where is my badge!?", "jim response 2"]

    # Create Exits and add to spaces
    # assembly_room exits
    assembly_exit_hallway = Exit(name="steel door", space=hallway1)
    assembly_room.add_exit(assembly_exit_hallway)
    assembly_exit_testing = Exit(name="wooden door", space=testing_hangar)
    assembly_room.add_exit(assembly_exit_testing)
    # hallway1 exits
    hallway1_exit_assembly = Exit(name="steel door", space=assembly_room)
    hallway1.add_exit(hallway1_exit_assembly)
    hallway1_exit_server = Exit(name="sliding door", space=server_room,
                                locked=True, unlock_item=server_room_key)
    hallway1.add_exit(hallway1_exit_server)
    hallway1_exit_testing = Exit(name="opening", space=testing_hangar)
    hallway1.add_exit(hallway1_exit_testing)
    # server_room exits
    server_exit_hallway1 = Exit(name="sliding door", space=hallway1)
    server_room.add_exit(server_exit_hallway1)
    # testing_hangar exits
    testing_exit_assembly = Exit(name="wooden door", space=assembly_room)
    testing_hangar.add_exit(testing_exit_assembly)
    testing_exit_hallway1 = Exit(name="opening", space=hallway1)
    testing_hangar.add_exit(testing_exit_hallway1)

    # Place items in Spaces (automatically sets item.location to space)
    assembly_room.add_item(ssd_1tb)
    assembly_room.add_item(screw_driver)
    testing_hangar.add_item(server_room_key)
    testing_hangar.add_item(usb_encryption_key)

    # Place characters in spaces (automatically sets character.location
    # to space)
    assembly_room.add_character(pr2)
    assembly_room.add_character(kelt2a)
    testing_hangar.add_character(wasp12)
    hallway1.add_character(jim)
    player.set_location(assembly_room)

    # Create a maze with all of the spaces
    spaces_list = [assembly_room, hallway1, testing_hangar, server_room]
    maze = Maze(spaces_list)

    # Create a game with the player and maze
    game = Game(player, maze)

    # Start the game
    game.start()

if __name__ == "__main__":
    main()
