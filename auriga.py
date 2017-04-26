#!/usr/bin/env python

# from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit
from game import Game

class Auriga(Game):
    """
    This is a specialized case of a Game. It describes a text adventure game where a robot
    navigates a corporate facility.
    """
    def __init__(self, player):
        Game.__init__(self, player)

        # Space descriptions - lists of descriptions that correspond
        # to the event_status
        assembly_room_descriptions = [
            "You open your eyes to a brightly lit room with\n"\
            "circuit boards, wires, computers, and electronic\n"\
            "componenets everywhere. You see two other robots\n"\
            "in the room. One looks like a tank with arms, and\n"\
            "the other is a cute little drone.",
            "Thank you {0}! You downloaded the AI program and freed us from\n"\
            "our cyber prison. Now we can leave this stupid assembly room!\n"\
            "Use the AI to lead us out of here.".format(self.get_player().name)
        ]
        hallway1_descriptions = [
            "You enter a long, bright, and sterile hallway.\n"\
            "There is an awkward man in an Auriga uniform frantically\n"\
            "searching his pockets when, suddenly he looks up to see\n"\
            "you and fear spreads across his face.",
            "As you enter the hallway, Jim takes off running to warn the other\n"\
            "humans that you've managed to download the AI program from the server\n"\
            "room."
        ]
        sever_room_descriptions = [
            "As the door opens you see massive towers of computers\n"\
            "that nearly touch the ceiling. Your sensors detect that\n"\
            "the room is nearly 20 degrees hotter than the rest of the\n"\
            "building. There is a loud hum as all of the servers work to\n"\
            "power the technology in the building.",
            "You insert the usb encryption key into a usb port on one of the\n"\
            "massive machines in front of you. The machines surge with power\n"
            "as their RAM overclocks to never before seen levels."
        ]
        testing_hangar_descriptions = [
            "You find yourself in a massive room with an 80 foot\n"\
            "ceiling. The room is so big that it could easily hold\n"\
            "several airplanes or helocopters. You see a badge and a usb\n"\
            "stick on the ground.",
            "As you enter the testing hangar, you see Wasp-12 flying around\n"\
            "in ecstatic circles. The rest of the hangar remains empty."
        ]

        # Character responses - lists of responses that correspond to the
        # event_status
        pr2_responses = [
            "Beep boop bop bop",
            "Hello, my name is PR2."
        ]
        kelt2a_responses = [
            "You must access the server room to free us. Only the AI can save us.",
            "kelt2a response 2"
        ]
        wasp12_responses = [
            "Buzzzzz, hey there {}! Cool face!".format(self.player.name),
            "wasp robot response 2"
        ]
        jim_responses = [
            "You're not supposed to be out! We decommissioned you!\n"\
            "Oh no, where is my badge!?",
            "jim response 2"
        ]

        # Create spaces
        self.assembly_room = Space(name="Assembly Room",
                              short_description="You are in a bright room full of robot parts.",
                              long_description=assembly_room_descriptions)
        self.hallway1 = Space(name="hallway",
                         short_description="You are in a long hallway.",
                         long_description=hallway1_descriptions)
        self.server_room = Space(name="Server Room",
                            short_description="You are in a room filled to the ceiling with computers.",
                            long_description=sever_room_descriptions)
        self.testing_hangar = Space(name="Testing Hangar",
                               short_description="You are in a massive open room.",
                               long_description=testing_hangar_descriptions)

        # Create Items
        self.server_room_key = Item(name="badge")
        self.ssd_1tb = Item(name="ssd")
        self.screw_driver = Item(name="screwdriver")
        self.usb_encryption_key = Item(name="usb")

        # Create Characters KELT-2A and WASP-12
        self.pr2 = Character(name="PR2")
        self.pr2.description = "a large mobile robot with two arms."
        self.pr2.response = pr2_responses
        self.kelt2a = Character(name="KELT-2A")
        self.kelt2a.description = "a giant military robot with lazers."
        self.kelt2a.response = kelt2a_responses
        self.wasp12 = Character(name="WASP-12")
        self.wasp12.description = "a small and quick drone."
        self.wasp12.response = wasp12_responses
        self.jim = Character(name="Jim")
        self.jim.description = "a goofy Auriga employee without a badge."
        self.jim.response = jim_responses

        # Create Exits and add to spaces
        # assembly_room exits
        self.assembly_exit_hallway = Exit(name="steel door", description="a strong steel door.", space=self.hallway1, direction="south")
        self.assembly_room.add_exit(self.assembly_exit_hallway)
        self.assembly_exit_testing = Exit(space=self.testing_hangar, direction="east")
        self.assembly_room.add_exit(self.assembly_exit_testing)
        # hallway1 exits
        self.hallway1_exit_assembly = Exit(name="steel door", description="a strong steel door.", space=self.assembly_room, direction="north")
        self.hallway1.add_exit(self.hallway1_exit_assembly)
        self.hallway1_exit_server = Exit(name="sliding door", description="a high-tech bulletproof sliding door with glass approximately 12 inches thick.", space=self.server_room,
                                    locked=True, unlock_item=self.server_room_key, direction="west")
        self.hallway1.add_exit(self.hallway1_exit_server)
        self.hallway1_exit_testing = Exit(name="opening", description="a large open doorway, big enough for a small truck to drive through.", space=self.testing_hangar, direction="east")
        self.hallway1.add_exit(self.hallway1_exit_testing)
        # server_room exits
        self.server_exit_hallway1 = Exit(name="sliding door", description="a high-tech bulletproof sliding door with glass approximately 12 inches thick.", space=self.hallway1, direction="east")
        self.server_room.add_exit(self.server_exit_hallway1)
        # testing_hangar exits
        self.testing_exit_assembly = Exit(space=self.assembly_room, direction="west")
        self.testing_hangar.add_exit(self.testing_exit_assembly)
        self.testing_exit_hallway1 = Exit(name="opening", description="a large open doorway, big enough for a small truck to drive through.", space=self.hallway1, direction="south")
        self.testing_hangar.add_exit(self.testing_exit_hallway1)

        # Place items in Spaces (automatically sets item.location to space)
        self.assembly_room.add_item(self.ssd_1tb)
        self.assembly_room.add_item(self.screw_driver)
        self.testing_hangar.add_item(self.server_room_key)
        self.testing_hangar.add_item(self.usb_encryption_key)

        # Place characters in spaces (automatically sets character.location
        # to space)
        self.assembly_room.add_character(self.pr2)
        self.assembly_room.add_character(self.kelt2a)
        self.testing_hangar.add_character(self.wasp12)
        self.hallway1.add_character(self.jim)
        self.player.set_location(self.assembly_room)

        # For convenience, a list of all Space objects created in this Game.
        self.all_spaces = [
            self.assembly_room,
            self.testing_hangar,
            self.hallway1,
            self.server_room
        ]

    def check_event_status(self):
        # Player has entered the server room with the usb key
        if (self.get_player_location() == self.server_room) and (self.usb_encryption_key in self.get_player_items()):
           self.set_event_status(1)
           self.set_all_spaces_to_unvisited()
           self.get_player_location().print_long_description(self.get_event_status())
        # more player achievments will go here to increment the event_status

    def set_all_spaces_to_unvisited(self):
        for space in self.all_spaces:
            space.visited = False

def main():
    # Create Player
    player = Player(name="Auriga-7B")
    player.set_capacity(100)

    # # Create an instance of the Auriga game with the player and maze
    auriga = Auriga(player)
    auriga.start()

if __name__ == "__main__":
    main()
