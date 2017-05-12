#!/usr/bin/env python3

from resources.space import Space
from resources.item import Item
from resources.character import Character
from resources.player import Player
from resources.exit import Exit
from resources.game import Game

class Auriga(Game):
    """
    This is a specialized case of a Game. It describes a text adventure game where a robot
    navigates a corporate facility.
    """
    def __init__(self, player):
        Game.__init__(self, player)

        # SPACE DESCRIPTIONS
        assembly_room_descriptions = [
            "You open your eyes to a brightly lit room with\n"\
            "circuit boards, wires, computers, and electronic\n"\
            "componenets everywhere. You see two other robots\n"\
            "in the room. One looks like a tank with arms, and\n"\
            "the other is a cute little drone.",
            "long description 2",
            "long description 3",
            "long description 4",
            "long description 5"
        ]
        hallway1_descriptions = [
            "You enter a long, bright, and sterile hallway.\n"\
            "There is an awkward man in an Auriga uniform frantically\n"\
            "searching his pockets when, suddenly he looks up to see\n"\
            "you and fear spreads across his face.",
            "long description 2",
            "long description 3",
            "long description 4",
            "long description 5"
        ]
        sever_room_descriptions = [
            "As the door opens you see massive towers of computers\n"\
            "that nearly touch the ceiling. Your sensors detect that\n"\
            "the room is nearly 20 degrees hotter than the rest of the\n"\
            "building. There is a loud hum as all of the servers work to\n"\
            "power the technology in the building.",
            "long description 2",
            "long description 3",
            "long description 4",
            "long description 5"
        ]
        testing_hangar_descriptions = [
            "You find yourself in a massive room with an 80 foot\n"\
            "ceiling. The room is so big that it could easily hold\n"\
            "several airplanes or helocopters. You see a usb\n"\
            "stick on the ground, and a small lever at the end of a row\n"\
            "of employee lockers.",
            "long description 2",
            "long description 3",
            "long description 4",
            "long description 5"
        ]
        clean_room_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        blueprint_room_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        conference_room_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        computer_lab1_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        computer_lab2_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        brig_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        hallway2_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        supply_closet_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        trash_room_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        maintenance_room_descriptions = [
            "long description 1",
            "long description 2",
            "long description 3",
            "long description 4",
            "long_description 5"
        ]
        attic_descriptions = [
            "long description 1",
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
        self.badge = Item(name="badge", visible=False)
        self.ssd_1tb = Item(name="ssd")
        self.screw_driver = Item(name="screwdriver")
        self.usb_encryption_key = Item(name="usb")
        self.charger1 = Item(name="charger", locked=True)
        self.button1 = Item(name="button", locked=True)
        self.lever1 = Item(name="lever", locked=True)
        self.items.extend([self.lever1, self.button1, self.charger1, self.badge, self.ssd_1tb,
                           self.screw_driver, self.usb_encryption_key])

        # CHARACTER RESPONSES
        pr2_responses = [
            "The techs usually press a button to open the door to access the\n"\
            "testing hangar.",
            "response 2."
        ]
        kelt2a_responses = [
            "Be careful in the testing hangar. They took Freight-500 out there,\n"
            "and he's never come back. I saw one of the techs walk out of here\n"
            "with his hard drive. He could probably use a new one...",
            "response 2"
        ]
        wasp12_responses = [
            "Fetch-4 is doing life testing in a secret room. I haven't seen her for\n"
            "27 days. You need an employee badge to get in there.",
            "wasp robot response 2"
        ]
        jim_responses = [
            "You're not supposed to be out! We decommissioned you!\n"\
            "Oh no, where is my badge!? I think I left it in my locker in the\n"
            "testing hangar.",
            "response 2"
        ]
        freight500_responses = [
            "...",
            "response 2"
        ]
        fetch4_responses = [
            "NA",
            "Disco never dies! Up and down, up and down, up and down...",
            "response 3"
        ]

        # CREATE CHARACTERS
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
        self.freight500 = Character(name="FREIGHT-500")
        self.freight500.description = "a large mobile robot base that doesn't seem to work."
        self.freight500.response = freight500_responses
        self.fetch4 = Character(name="FETCH-4")
        self.fetch4.description = "a mobile robot arm stuck in an endless test sequence."
        self.fetch4.response = fetch4_responses

        # Add characters to object list
        self.characters.extend([self.fetch4, self.freight500, self.pr2, self.kelt2a, self.wasp12, self.jim])


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
            description="an elevator with a badge scanner to activate it.")
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
            description="an elevator with a badge scanner to activate it.")
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
            description="a high-tech bulletproof sliding door with glass approximately 12 inches thick.")
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
        self.assembly_room.add_item(self.ssd_1tb)
        self.assembly_room.add_item(self.screw_driver)
        self.assembly_room.add_item(self.charger1)
        self.assembly_room.add_item(self.button1)
        self.testing_hangar.add_item(self.badge)
        self.testing_hangar.add_item(self.usb_encryption_key)
        self.testing_hangar.add_item(self.lever1)

        # Place characters in spaces (automatically sets character.location
        # to space)
        self.assembly_room.add_character(self.pr2)
        self.assembly_room.add_character(self.kelt2a)
        self.testing_hangar.add_character(self.wasp12)
        self.testing_hangar.add_character(self.freight500)
        self.clean_room.add_character(self.fetch4)
        self.hallway1.add_character(self.jim)
        self.player.set_location(self.assembly_room)

    def check_event_status(self):
        pass
    #     # Player has entered the server room with the usb key
    #     if (self.get_player_location() == self.server_room) and (self.usb_encryption_key in self.get_player_items()):
    #        self.set_event_status(1)
    #        self.set_all_spaces_to_unvisited()
    #        self.get_player_location().print_long_description(self.get_event_status())
    #     # more player achievments will go here to increment the event_status

    def set_all_spaces_to_unvisited(self):
        for space in self.spaces:
            space.visited = False

    def use(self, item_name):
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

        # SPECIAL EVENT: Player uses ssd in testing hangar
        if item_name == "ssd" and cur_space.get_name() == "Testing Hangar" and not self.event_status_list[0]:
            self.event_status += 1
            self.event_status_list[0] = True
            self.player.remove_item(item)
            clean_room_exit = self.get_object_by_name(cur_exits, "glass door")
            clean_room_exit.set_is_visible(True)
            freight500_responses = [
                "Error...mislocalized. Error...mislocalized.",
                "response 2",
                "response 3"
            ]
            self.freight500.set_response(freight500_responses)
            print("You place the ssd into Freight-500's computer, and suddenly the fan kicks on ")
            print("Freight-500 comes to life and whizzes past you.\n")
            print("[FREIGHT-500] Executing task-523883 move forklift pallet to pose 23.")
            print("\n...\n")
            print("Freight-500 drove across the testing hangar to the large forklift pallet loaded ")
            print("with heavy boxes. When Freight-500 arrived at the pallet, an automated jack in the floor ")
            print("lifted the pallet and Freight-500 drove under it.")
            print("Freight-500 headed for the other side of the hangar with the pallet.")
            print("You notice a door you couldn't see before, that was blocked by the cargo.")
        elif cur_space.get_name() == "Clean Room":
            print("You attempt to use the {0} on FETCH-4, but something went terribly wrong!".format(item_name))
            print("FETCH-4 begins smoking, and the head and arm begin moving faster and faster!")
            print("FETCH-4 explodes and causes extensive damage to your shielding and batteries.")
            self.player.set_energy(self.player.get_energy() // 2)
        # SPECIAL EVENT: Player uses usb drive in server room
        elif item_name == "usb" and cur_space.get_name() == "Server Room" and not self.event_status_list[1]:
            self.event_status += 1
            self.event_status_list[1] = True
        else:
            print("You can't use that here.")


    def push(self, item_name):
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

        # Player pushes the button in the Assembly Room -> Unlocks door to Testing Hangar
        if item_name == "button" and cur_space.get_name() == "Assembly Room":
            testing_hanger_exit = self.get_object_by_name(cur_exits, "sliding door")
            testing_hanger_exit.set_is_locked(False)
            print("You pressed the large red button, and you hear a loud click near the only door ")
            print("in the room. A green light illuminates the keypad to the left of the door.")
        # More 'PUSH' cases here
        else:
            print("You pushed the {0}, and it made you feel nice.".format(item_name))

    def pull(self, item_name):
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
            badge_item = self.get_object_by_name(cur_items, "badge")
            badge_item.set_visible(True)
            print("You pulled the small lever, and a locker popped open. In the locker you ")
            print("see an Auriga worker's badge.")
        else:
            print("You pulled the {0} and you lost some energy.".format(item_name))
            self.player.set_energy(self.player.get_energy() - 1)

def main():
    # Create Player
    player = Player(name="Auriga-7B", capacity=50)

    # # Create an instance of the Auriga game with the player and maze
    auriga = Auriga(player)
    auriga.start()

if __name__ == "__main__":
    main()
