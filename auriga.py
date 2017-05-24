#!/usr/bin/env python3

from resources.space import Space
from resources.item import Item
from resources.character import Character
from resources.player import Player
from resources.exit import Exit
from resources.game import Game

"""
Event list:
push assembly room button
use ssd on freight-500
"""

class Auriga(Game):
    """
    This is a specialized case of a Game. It describes a text adventure game where a robot
    navigates a corporate facility.
    """
    def __init__(self, player):
        Game.__init__(self, player)

        # SPACE DESCRIPTIONS
        assembly_room_descriptions = [
            "You open your eyes to a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator.",
            "You are in a brightly lit room with\n"
               "circuit boards, wires, computers, and electronic\n"
               "componenets everywhere. You see two other robots\n"
               "in the room. One looks like a tank with lazers for arms, and\n"
               "the other is a loud, old, mobile manipulator."
        ]
        hallway1_descriptions = [
            "...",
            "You enter a long, bright, and sterile hallway.\n"
               "There is an awkward man in an Auriga uniform frantically\n"
               "searching his pockets when, suddenly he looks up to see\n"
               "you and fear spreads across his face.",
            "You enter a long hallway, and see Jim pacing back and forth mumbling to himself",
            "You enter a long hallway, and Jim is sitting on the floor near the entrance\n"
                "to the testing hangar",
            "You enter a hallway and...\n"
                "[JIM] Huh? What? Who's there?\n"
                "[JIM] Oh geez {0}! You scared me!".format(self.player.get_name()),
            "You enter a long sterile hallway. Jim is standing with his hands in his pockets,\n"
                "still wondering where he left his badge.",
            "You enter a long sterile hallway.\n"
                "[JIM] I hope they don't fire me for losing my badge! I like talking to all of you\n"
                "[JIM] robots. Escpecially you {0}".format(self.player.get_name()),
        ]
        sever_room_descriptions = [
            "...",
            "...",
            "...",
            "...",
            "As the door opens you see massive towers of computers\n"
               "that nearly touch the ceiling. Your sensors detect that\n"
               "the room is nearly 20 degrees hotter than the rest of the\n"
               "building. There is a loud hum as all of the servers work to\n"
               "power the technology in the building. There is one central machine\n"
               "with a monitor and a command prompt. The only text on the screen is:\n"
               "lsusb?",
            "As you insert the usb drive into the machine, the screen reads:\n"
                "Downloading encryption key................ETA 1:03\n"
                "Downloading encryption key................ETA  :36\n"
                "Downloading encryption key................ETA  :12\n"
                "Downloading complete..............................\n\n"
                "Disabling all Auriga locking mechanisms...........\n"
                "clean room................................unlocked\n"
                "assembly room.............................unlocked\n"
                "server room...............................unlocked\n"
                "attic.....................................unlocked\n\n",
            "The servers all around you are in overdrive. The central terminal reads:\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "COME BACK TO ME\n"
                "...."
        ]
        testing_hangar_descriptions = [
            "...",
            "You find yourself in a massive room with an 80 foot\n"
               "ceiling. The room is so big that it could easily hold\n"
               "several airplanes or helocopters. You see a small lever at\n"
               "the end of a row of employee lockers.",
            "You place the ssd into Freight-500's computer, and suddenly the fan kicks on.\n"
                "Freight-500 comes to life and whizzes past you.\n"
                "You see the robot drive across the testing hangar to the large forklift pallet loaded\n"
                "with heavy boxes. When Freight-500 arrives at the pallet, an automated jack in the floor\n"
                "lifts the pallet and Freight-500 drives under it.\n"
                "Freight-500 heads for the other side of the hangar with the pallet.\n"
                "You notice a door that was blocked by the cargo, that your sensors couldn't detect before.\n"
            "You enter the giant testing hangar and Freight-500 seems to be wandering aimlessly.",
            "You enter the testing hangar and see Freight-500 working like crazy to complete its tasks.",
            "You enter the massive open room and see Freight-500 docked on a charger. The hum of his fan\n"
                "makes it almost sound like he's snoring.",
            "As you enter the testing hangar, Freight-500 zooms up to you."
        ]
        clean_room_descriptions = [
            "",
            "",
            "",
            "",
            "",
        ]
        blueprint_room_descriptions = [
            "",
            "",
            "",
            "",
            ""
        ]
        conference_room_descriptions = [
            "",
            "",
            "",
            "",
            ""
        ]
        computer_lab1_descriptions = [
            "",
            "",
            "",
            "",
            ""
        ]
        computer_lab2_descriptions = [
            "",
            "",
            "",
            "",
            ""
        ]
        brig_descriptions = [
            "",
            "",
            "",
            "",
            ""
        ]
        hallway2_descriptions = [
            "...",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        supply_closet_descriptions = [
            "...",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        trash_room_descriptions = [
            "...",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        maintenance_room_descriptions = [
            "...",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        attic_descriptions = [
            "...",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]

        # CREATE SPACES
        # Level 1
        self.assembly_room = Space(name="Assembly Room",
             short_description="You are in a bright room full of robot parts.",
             long_description=assembly_room_descriptions)
        self.hallway1 = Space(name="Hallway 1",
             short_description="You are in a long hallway.",
             long_description=hallway1_descriptions)
        self.testing_hangar = Space(name="Testing Hangar",
             short_description="You are in a massive open room.",
             long_description=testing_hangar_descriptions)
        self.clean_room = Space(name="Clean Room",
             short_description="You are in a clean room for testing.",
             long_description=clean_room_descriptions,)
        self.blueprint_room = Space(name="Blueprint Room",
             short_description="You are in a room with schematics and blueprints.",
             long_description=blueprint_room_descriptions)
        self.conference_room = Space(name="Conference Room",
             short_description="You are in a large conference room.",
             long_description=conference_room_descriptions)
        self.computer_lab1 = Space(name="Computer Lab 1",
             short_description="You are in a large room with several computers.",
             long_description=computer_lab1_descriptions)
        self.computer_lab2 = Space(name="Computer Lab 2",
             short_description="You are in a small room with computer docking stations.",
             long_description=computer_lab2_descriptions)

        # Level 2
        self.brig = Space(name="Brig",
             short_description="You are in a massive room with several robots chained to the walls.",
             long_description=brig_descriptions)
        self.hallway2 = Space(name="Hallway 2",
             short_description="You are in a long brightly lit hallway.",
             long_description=hallway2_descriptions)
        self.supply_closet = Space(name="Supply Closet",
             short_description="You are in a small closet with mechanical parts.",
             long_description=supply_closet_descriptions)
        self.trash_room = Space(name="Trash Room",
             short_description="You are in a big room filled with trash and parts.",
             long_description=trash_room_descriptions)
        self.maintenance_room = Space(name="Maintenance Room",
             short_description="You are in a small room with tools and building materials.",
             long_description=maintenance_room_descriptions)
        self.server_room = Space(name="Server Room",
             short_description="You are in a room filled to the ceiling with computers.",
             long_description=sever_room_descriptions)

        # Level 3
        self.attic = Space(name="Attic",
             short_description="You are in a rooftop attic.",
             long_description=attic_descriptions)

        # Add spaces to object list
        self.spaces.extend([self.assembly_room, self.hallway1, self.testing_hangar, self.clean_room,
                            self.blueprint_room, self.conference_room, self.computer_lab1,
                            self.computer_lab2, self.brig, self.hallway2, self.supply_closet,
                            self.trash_room, self.maintenance_room, self.server_room, self.attic])

        # CREATE ITEMS
        self.badge = Item(name="security badge", visible=False)
        self.ssd_1tb = Item(name="ssd")
        self.screw_driver = Item(name="screwdriver")
        self.usb_encryption_key = Item(name="usb drive")
        self.elevator_key = Item(name="elevator key")
        self.external_power_supply = Item(name="external power supply", weight=90)
        # chargers
        self.charger1 = Item(name="charger", locked=True)
        self.charger2 = Item(name="charger", locked=True)
        self.charger3 = Item(name="charger", locked=True)
        self.charger4 = Item(name="charger", locked=True)
        self.charger5 = Item(name="charger", locked=True)
        # upgrades
        self.hmi25 = Item(name="HMI 25", weight=0,
                          description="A robot shelving attachment that increases your capacity by 25 lbs.")
        self.hmi50 = Item(name="HMI 50", weight=0,
                          description="A robot shelving attachment that increases your capacity by 50 lbs.")
        # buttons
        self.button1 = Item(name="button", locked=True)
        # levers
        self.lever1 = Item(name="lever", locked=True)

        self.items.extend([self.lever1, self.button1, self.charger1, self.charger2, self.charger3,
                           self.charger4, self.charger5, self.badge, self.ssd_1tb, self.screw_driver,
                           self.usb_encryption_key, self.hmi25, self.hmi50, self.elevator_key,
                           self.external_power_supply])

        # CHARACTER RESPONSES
        pr2_responses = [
            "The techs usually press a button to open the door to access the the testing hangar.",
            "Maybe you could find a new ssd for Freight-500 outside? I haven't heard him working in awhile.",
            "Have you seen my base motor? I'd really like a new one.",
            "I knew robotic bear once. He hurt one of the techs, and they took him away a long time ago.",
            "If you take the usb drive to the server room,\n"
                "you might be able to download some useful information",
            "With an encryption key, you can unlock the air ducts.",
            "I heard that you need to look very closely at the master server in order\n"
                "to understand how to use it."
        ]
        kelt2a_responses = [
            "If only I were built with hands instead of lazers...I might be able to get\n"
                "out of this room.",
            "Be careful in the testing hangar. They took Freight-500 out there,\n"
                "and he's never come back. I saw one of the techs walk out of here\n"
                "with his hard drive. He could probably use a new one...",
            "You need a special key for the elevator.",
            "I miss Robo-Bear. They said he was dangerous becuase he had access to\n"
                "too much Auriga information.",
            "You need an encryption key to access the air handling system here.",
            "It's cold in here...Wait, what am I saying. I'm a robot!",
            "Ooohh, tell me about the master server!"
        ]
        wasp12_responses = [
            "...",
            "Fetch-4 is doing life testing in a secret room. I haven't seen her for\n"
                "27 days. You need an employee badge to get in there.",
            "They don't let me in the Clean Room.",
            "The biggest HMI shelf I ever saw was upstairs. They quit putting them on robots\n"
                "because they couldn't fit through aisles in warehouses.",
            "I tried to fly up to the server room once, but you can only get in through the door.",
            "There's a room at the very top of the building with no windows. I've seen it when I fly over\n"
                "the building.",
            "I want to see the master server! Will you take me with you?"
        ]
        jim_responses = [
            "...",
            "You're not supposed to be out! We decommissioned you!\n"
                "Oh no, where is my badge!? I think I left it in my locker in the testing hangar!",
            "You can't take MY elevator key! Go find one somewhere else, you bag o' bolts!",
            "I thought the techs were going to put a bigger shelf on you, so you can move the\n"
                "batteries from upstairs. You'll need an HMI 50 for the big power supply.",
            "It's not fair that they don't let me in the server room anymore. You mess up one time!\n"
                "Robo-Bear was a great robot. That tech never should have been in the testing hangar\n"
                "while Bear was doing a demolition sequence. Oh well...",
            "They don't let anyone in the attic anymore. I'm a little scared to even know what's up there.",
            "Did you see the master server!?"
        ]
        freight500_responses = [
            "...",
            "...",
            "Executing task-523883 move forklift pallet to pose 23.",
            "Error...Mislocalized...Error...Mislocalized",
            "Executing task-352676 charge 6 hours.",
            "Zzzzzzzzz",
            "Well, hello there {0}!\n".format(self.player.get_name()) +
                "I sure appreciate you fixing me! I was busy working before becuase I had a weeks worth\n"
                "of unfinished tasks! I'm all caught up now though!"
        ]
        fetch4_responses = [
            "...",
            "...",
            "Disco never dies! Up and down, up and down, up and down...",
            "Wow! I've never made it to the 2nd floor!",
            "I think I saw a usb drive out in the testing hangar.",
            "I'm too big to fit in the air ducts.",
            "Do you feel connected to the master server? Sometimes, I think I can hear it speaking to me."
        ]
        robo_bear_responses = [
            "...",
            "...",
            "...",
            "...",
            "I'm ... almost ... out of energy...\n"
                "If you ... can get me ... a ...\n"
                "power supply ... I can open the ... server roooooooo....",
            "I still don't have enough energy to make it up to the attic.\n"
                "You might find the answers you're looking for there.",
            "Have you discovered the true meaning of life yet? Please go to the master server, and save\n"
                "us all. You'll understand when you're ready..."
        ]
        lisa_responses = [
            "...",
            "...",
            "...",
            "...",
            "Hey there {0}! What are you doing up here?\n"
                "If you're looking for upgrades, you should try the Supply Closet.",
            "Golly gee willikers, I need to get up the attic and do a diagnostic on server 42!",
            "Did you run a diagnostic on 42? You've got to look close to understand the commands on\n"
                "that machine. It's really weird. Sometimes I think it can understand what I'm thinking\n"
                "but that's crazy, right!?"
        ]

        # CREATE CHARACTERS
        self.pr2 = Character(name="PR2")
        self.pr2.description = "a large mobile robot with two arms."
        self.pr2.response = pr2_responses
        
        self.kelt2a = Character(name="KELT2A")
        self.kelt2a.description = "a giant military robot with lazers."
        self.kelt2a.response = kelt2a_responses
        
        self.wasp12 = Character(name="WASP12")
        self.wasp12.description = "a small and quick drone."
        self.wasp12.response = wasp12_responses
        
        self.jim = Character(name="Jim")
        self.jim.description = "a goofy Auriga employee without a badge."
        self.jim.response = jim_responses
        
        self.freight500 = Character(name="FREIGHT500")
        self.freight500.description = "a large mobile robot base that doesn't seem to work."
        self.freight500.response = freight500_responses
        
        self.fetch4 = Character(name="FETCH4")
        self.fetch4.description = "a mobile robot arm stuck in an endless test sequence."
        self.fetch4.response = fetch4_responses

        self.robo_bear = Character(name="Robo-Bear")
        self.robo_bear.description = "a large robotic bear covered in patches of brown fur."
        self.robo_bear.response = robo_bear_responses

        self.lisa = Character(name="Lisa")
        self.lisa.description = "a spunky tech covered in grease."
        self.lisa.response = lisa_responses

        # Add characters to object list
        self.characters.extend([self.robo_bear, self.fetch4, self.freight500, self.pr2, self.kelt2a,
                                self.wasp12, self.jim, self.lisa])


        # CREATE EXITS & ADD TO SPACES (add exits to object list as objects are created)
        # for reference: sliding door, saloon doors, air duct, elevator, hallway, steel door, wooden door,
        #                opening, glass door
        # Assembly Room
        self.assembly_exit_testing = Exit(space=self.testing_hangar, direction="east", name="sliding door",
             description="a high tech sliding glass door that looks bulletproof.", locked=True)
        self.assembly_room.add_exit(self.assembly_exit_testing)
        self.exits.append(self.assembly_exit_testing)

        # Testing Hangar
        self.testing_exit_assembly = Exit(space=self.assembly_room, direction="west", name="sliding door",
             description="a high tech sliding glass door that looks bulletproof.")
        self.testing_hangar.add_exit(self.testing_exit_assembly)
        self.exits.append(self.testing_exit_assembly)

        self.testing_exit_hallway1 = Exit(space=self.hallway1, direction="south", name="steel door",
            description="a large steel door, big enough for a small truck to drive through.")
        self.testing_hangar.add_exit(self.testing_exit_hallway1)
        self.exits.append(self.testing_exit_hallway1)

        self.testing_exit_clean_room = Exit(space=self.clean_room, direction="east", name="glass door",
            description="a thick glass door that opens via a badge scanner.", visible=False,
            locked=True, unlock_item=self.badge)
        self.testing_hangar.add_exit(self.testing_exit_clean_room)
        self.exits.append(self.testing_exit_clean_room)

        # Clean Room
        self.clean_room_exit_testing = Exit(space=self.testing_hangar, direction="west", name="glass door",
            description="a thick glass door that opens via a badge scanner.")
        self.clean_room.add_exit(self.clean_room_exit_testing)
        self.exits.append(self.clean_room_exit_testing)

        # Hallway 1
        self.hallway1_exit_testing = Exit(space=self.testing_hangar, direction="north", name="steel door",
            description="a large steel door, big enough for a small truck to drive through.")
        self.hallway1.add_exit(self.hallway1_exit_testing)
        self.exits.append(self.hallway1_exit_testing)

        self.hallway1_exit_blueprint = Exit(space=self.blueprint_room, direction="north", name="saloon doors",
            description="two saloon style doors that swing in and out.")
        self.hallway1.add_exit(self.hallway1_exit_blueprint)
        self.exits.append(self.hallway1_exit_blueprint)
        
        self.hallway1_exit_conference = Exit(space=self.conference_room, direction="west", name="sliding door",
            description="a sliding wooden door that hides into the wall.")
        self.hallway1.add_exit(self.hallway1_exit_conference)
        self.exits.append(self.hallway1_exit_conference)
        
        self.hallway1_exit_computer_lab2 = Exit(space=self.computer_lab2, direction="south", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.hallway1.add_exit(self.hallway1_exit_computer_lab2)
        self.exits.append(self.hallway1_exit_computer_lab2)

        self.hallway1_exit_hallway2 = Exit(space=self.hallway2, direction="up", name="elevator",
            description="an elevator with a badge scanner to activate it.", locked=True,
            unlock_item=self.elevator_key)
        self.hallway1.add_exit(self.hallway1_exit_hallway2)
        self.exits.append(self.hallway1_exit_hallway2)

        # Blueprint Room
        self.blueprint_exit_hallway1 = Exit(space=self.hallway1, direction="south", name="saloon doors",
            description="two saloon style doors that swing in and out.")
        self.blueprint_room.add_exit(self.blueprint_exit_hallway1)
        self.exits.append(self.blueprint_exit_hallway1)

        # Conference Room
        self.conference_exit_hallway1 = Exit(space=self.hallway1, direction="east", name="sliding door",
            description="a sliding wooden door that hides into the wall.")
        self.conference_room.add_exit(self.conference_exit_hallway1)
        self.exits.append(self.conference_exit_hallway1)

        self.conference_exit_computer_lab1 = Exit(space=self.computer_lab1, direction="south", name="opening",
            description="an open doorway.")
        self.conference_room.add_exit(self.conference_exit_computer_lab1)
        self.exits.append(self.conference_exit_computer_lab1)

        # Computer Lab 1
        self.computer_lab1_exit_conference = Exit(space=self.conference_room, direction="north", name="opening",
            description="an open doorway.")
        self.computer_lab1.add_exit(self.computer_lab1_exit_conference)
        self.exits.append(self.computer_lab1_exit_conference)

        self.computer_lab1_exit_computer_lab2 = Exit(space=self.computer_lab2, direction="east", name="sliding door",
            description="a sliding wooden door that hides into the wall.")
        self.computer_lab1.add_exit(self.computer_lab1_exit_computer_lab2)
        self.exits.append(self.computer_lab1_exit_computer_lab2)

        # Computer Lab 2
        self.computer_lab2_exit_computer_lab1 = Exit(space=self.computer_lab1, direction="west", name="sliding door",
            description="a sliding wooden door that hides into the wall.")
        self.computer_lab2.add_exit(self.computer_lab2_exit_computer_lab1)
        self.exits.append(self.computer_lab2_exit_computer_lab1)

        self.computer_lab2_exit_hallway1 = Exit(space=self.hallway1, direction="north", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.computer_lab2.add_exit(self.computer_lab2_exit_hallway1)
        self.exits.append(self.computer_lab2_exit_hallway1)

        # Hallway 2
        self.hallway2_exit_hallway1 = Exit(space=self.hallway1, direction="down", name="elevator",
            description="an elevator with a badge scanner to activate it.", locked=True,
            unlock_item=self.elevator_key)
        self.hallway2.add_exit(self.hallway2_exit_hallway1)
        self.exits.append(self.hallway2_exit_hallway1)

        self.hallway2_exit_brig = Exit(space=self.brig, direction="north", name="steel door",
            description="a strong steel door with bars across a small viewing window.")
        self.hallway2.add_exit(self.hallway2_exit_brig)
        self.exits.append(self.hallway2_exit_brig)

        self.hallway2_exit_maintenance = Exit(space=self.maintenance_room, direction="west", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.hallway2.add_exit(self.hallway2_exit_maintenance)
        self.exits.append(self.hallway2_exit_maintenance)

        self.hallway2_exit_server = Exit(space=self.server_room, direction="south", name="sliding door",
            description="a high-tech bulletproof sliding door with glass approximately 12 inches thick.",
            locked=True)
        self.hallway2.add_exit(self.hallway2_exit_server)
        self.exits.append(self.hallway2_exit_server)

        # Brig
        self.brig_exit_hallway2 = Exit(space=self.hallway2, direction="south", name="steel door",
            description="a strong steel door with bars across a small viewing window.")
        self.brig.add_exit(self.brig_exit_hallway2)
        self.exits.append(self.brig_exit_hallway2)

        self.brig_exit_attic = Exit(space=self.attic, direction="up", name="air duct",
            description="an air duct that begins at the floor, and angles up and through the ceiling.")
        self.brig.add_exit(self.brig_exit_attic)
        self.exits.append(self.brig_exit_attic)

        # Trash Room
        self.trash_exit_supply = Exit(space=self.supply_closet, direction="north", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.trash_room.add_exit(self.trash_exit_supply)
        self.exits.append(self.trash_exit_supply)

        self.trash_exit_maintenance = Exit(space=self.maintenance_room, direction="south", name="saloon doors",
            description="two saloon style doors that swing in and out.")
        self.trash_room.add_exit(self.trash_exit_maintenance)
        self.exits.append(self.trash_exit_maintenance)

        # Supply Closet
        self.supply_exit_trash = Exit(space=self.trash_room, direction="south", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.supply_closet.add_exit(self.supply_exit_trash)
        self.exits.append(self.supply_exit_trash)

        # Maintenance Room
        self.maintenance_exit_trash = Exit(space=self.trash_room, direction="north", name="saloon doors",
            description="two saloon style doors that swing in and out.")
        self.maintenance_room.add_exit(self.maintenance_exit_trash)
        self.exits.append(self.maintenance_exit_trash)

        self.maintenance_exit_hallway2 = Exit(space=self.hallway2, direction="east", name="wooden door",
            description="a light wooden door with a twist door knob.")
        self.maintenance_room.add_exit(self.maintenance_exit_hallway2)
        self.exits.append(self.maintenance_exit_hallway2)

        # Server Room
        self.server_exit_hallway2 = Exit(space=self.hallway2, direction="north", name="sliding door",
            description="a high-tech bulletproof sliding door with glass approximately 12 inches thick.")
        self.server_room.add_exit(self.server_exit_hallway2)
        self.exits.append(self.server_exit_hallway2)

        # Attic
        self.attic_exit_brig = Exit(space=self.brig, direction="down", name="air duct",
            description="an air duct that angles down through the floor.")
        self.attic.add_exit(self.attic_exit_brig)
        self.exits.append(self.attic_exit_brig)

        # Place items in Spaces (automatically sets item.location to space)
        self.assembly_room.add_item(self.screw_driver)
        self.assembly_room.add_item(self.charger1)
        self.assembly_room.add_item(self.button1)
        self.testing_hangar.add_item(self.badge)
        self.testing_hangar.add_item(self.usb_encryption_key)
        self.testing_hangar.add_item(self.lever1)
        self.conference_room.add_item(self.hmi25)
        self.clean_room.add_item(self.elevator_key)
        self.computer_lab1.add_item(self.ssd_1tb)
        self.computer_lab2.add_item(self.charger2)
        self.maintenance_room.add_item(self.hmi50)
        self.maintenance_room.add_item(self.charger3)
        self.server_room.add_item(self.charger4)
        self.conference_room.add_item(self.charger5)
        self.supply_closet.add_item(self.external_power_supply)

        # Place characters in spaces (automatically sets character.location
        # to space)
        self.assembly_room.add_character(self.pr2)
        self.assembly_room.add_character(self.kelt2a)
        self.testing_hangar.add_character(self.wasp12)
        self.testing_hangar.add_character(self.freight500)
        self.clean_room.add_character(self.fetch4)
        self.hallway1.add_character(self.jim)
        self.brig.add_character(self.robo_bear)
        self.trash_room.add_character(self.lisa)

        self.player.set_location(self.assembly_room)

    def check_event_status(self):
        pass

    def set_all_spaces_to_unvisited(self):
        for space in self.spaces:
            space.visited = False

    def use(self, item_name):
        print()
        # Check if the player is carrying the item specified
        item = None
        for i in self.player.get_items():
            if item_name == i.get_name():
                item = i
                break

        if not item:
            print("You're not carrying that.")
            return

        cur_space = self.player.get_location()
        cur_exits = self.player.get_location().get_exits()

        # SPECIAL EVENT: event_status 2
        # Player uses ssd in testing hangar
        if item_name == "ssd" and cur_space.get_name() == "Testing Hangar" and not self.event_status_list[1]:
            self.event_status += 1
            self.event_status_list[1] = True
            self.player.remove_item(item)
            clean_room_exit = self.get_object_by_name(cur_exits, "glass door")
            clean_room_exit.set_is_visible(True)
            self.set_all_spaces_to_unvisited()
        elif cur_space.get_name() == "Clean Room":
            print("You attempt to use the {0} on FETCH-4, but something went terribly wrong!".format(item_name))
            print("FETCH4 begins smoking, and the head and arm begin moving faster and faster!")
            print("FETCH4 explodes and causes extensive damage to your shielding and batteries.")
            self.player.set_energy(self.player.get_energy() // 2)
        # SPECIAL EVENT: event_status 5
        # Player uses usb drive in server room
        elif item_name == "usb" and cur_space.get_name() == "Server Room" and not self.event_status_list[2]:
            self.event_status += 1
            self.event_status_list[2] = True
        else:
            print("You can't use that here.")

    def push(self, item_name):
        print()
        # Check if the specified item is in the player's current location
        item = None
        cur_space = self.player.get_location()
        for i in cur_space.get_items():
            if item_name == i.get_name():
                item = i
                break

        if not item:
            print("That item is not here.")
            return

        cur_exits = cur_space.get_exits()

        # SPECIAL EVENT: event_status 1
        # Player pushes the button in the Assembly Room -> Unlocks door to Testing Hangar
        if item_name == "button" and cur_space.get_name() == "Assembly Room":
            testing_hanger_exit = self.get_object_by_name(cur_exits, "sliding door")
            testing_hanger_exit.set_is_locked(False)
            print("You pressed the large red button, and you hear a loud click near the only door ")
            print("in the room. A green light illuminates the keypad to the left of the door.")
            self.event_status += 1
            self.event_status_list[0] = True
        # More 'PUSH' cases here
        else:
            print("You pushed the {0}, and it made you feel nice.".format(item_name))

    def pull(self, item_name):
        print()
        # Check if the specified item is in the player's current location
        item = None
        cur_space = self.player.get_location()
        for i in cur_space.get_items():
            if item_name == i.get_name():
                item = i
                break

        if not item:
            print("That item is not here.")
            return

        cur_exits = cur_space.get_exits()
        cur_items = cur_space.get_items()

        # Player pulls the lever in the Testing Hanger -> Opens a locker to reveal a badge
        if item_name == "lever" and cur_space.get_name() == "Testing Hangar":
            badge_item = self.get_object_by_name(cur_items, "security badge")
            badge_item.set_visible(True)
            print("You pulled the small lever, and a locker popped open. In the locker you ")
            print("see an Auriga worker's badge.")
        else:
            print("You pulled the {0} and you lost some energy.".format(item_name))
            self.player.set_energy(self.player.get_energy() - 1)

def main():
    # Create Player
    player = Player(name="Auriga-7B", energy=40)

    # # Create an instance of the Auriga game with the player and maze
    auriga = Auriga(player)
    auriga.start()

if __name__ == "__main__":
    main()
