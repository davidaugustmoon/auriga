#!/usr/bin/env python3

# Standard Library
import os
import sys

# Local
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
    def __init__(self, player=None):
        Game.__init__(self, player)

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

        # SPECIAL EVENT: event_status 1
        # Player uses ssd in testing hangar
        if item_name == "ssd" and cur_space.get_name() == "Testing Hangar" and not self.event_status_list[1]:
            self.event_status += 1
            self.event_status_list[1] = True
            self.player.remove_item(item)
            clean_room_exit = self.get_object_by_name(cur_exits, "glass door")
            clean_room_exit.set_is_visible(True)
            print("You place the ssd into Freight-500's computer, and suddenly the fan kicks on.")
            print("Freight-500 comes to life and whizzes past you.")
            print("You see the robot drive across the testing hangar to the large forklift pallet loaded ")
            print("with heavy boxes. When Freight-500 arrives at the pallet, an automated jack in the floor ")
            print("lifts the pallet and Freight-500 drives under it.")
            print("Freight-500 heads for the other side of the hangar with the pallet.")
            print("You notice a door that was blocked by the cargo, that your sensors couldn't detect before.")
        elif cur_space.get_name() == "Clean Room":
            print("You attempt to use the {0} on FETCH-4, but something went terribly wrong!".format(item_name))
            print("FETCH-4 begins smoking, and the head and arm begin moving faster and faster!")
            print("FETCH-4 explodes and causes extensive damage to your shielding and batteries.")
            self.player.set_energy(self.player.get_energy() // 2)
        # SPECIAL EVENT: event_status 2
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

        # SPECIAL EVENT: event_status 0
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
            # The badge item is revealed
            if badge_item:
                badge_item.set_visible(True)
                print("You pulled the small lever, and a locker popped open. In the locker you ")
                print("see an Auriga worker's badge.")
            # The badge item has already been revealed
            else:
                print("You pulled the small lever, but nothing happens.")
        else:
            print("You pulled the {0} and you lost some energy.".format(item_name))
            self.player.set_energy(self.player.get_energy() - 1)

def main():
    # Create an instance of the Auriga game
    auriga = Auriga()

    # Load Game Menu
    while True:
        print("Would you like to start a new game, or load an existing saved game?")
        print("Enter the number of your choice.")
        print("1. New Game")
        print("2. Load Saved Game")
        print("Enter 'q' to quit.")
        valid_input = ["1", "2", "q"]
        user_selection = input(">").lower()

        if user_selection in valid_input:
            if user_selection == "1":
                print("Loading a new game...")
                auriga.load_game(os.path.join(os.getcwd(), "init_auriga", "init_auriga"))
                break
            elif user_selection == "2":
                saved_games_dir = os.path.join(os.getcwd(), "saved_games")

                # Print Available Saved Games
                print("Enter the number of the game you want to load.")
                saved_games = [game for game in os.listdir(saved_games_dir)]
                for index, sg in enumerate(saved_games):
                    print("{0}. {1}".format(index + 1, sg))

                # TODO error checking on user input
                user_game_selection = input(">")
                user_game = saved_games[int(user_game_selection) - 1]
                print("Loading game: {0}".format(user_game))
                auriga.load_game(os.path.join(saved_games_dir, user_game))
                break
            elif user_selection == "q":
                sys.exit()
            else:
                print("You've entered invalid input.")
        else:
            print("{0} is not a valid input.".format(user_selection))

    auriga.start()

if __name__ == "__main__":
    main()
