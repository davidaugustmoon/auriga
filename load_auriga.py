#!/usr/bin/env python3

# Standard Library
import os
import sys
import time

# Local
from resources.space import Space
from resources.item import Item
from resources.character import Character
from resources.player import Player
from resources.exit import Exit
from resources.game import Game

SCROLL_RATE = 3
FINAL_SLEEP = 8

class Auriga(Game):
    """
    This is a specialized case of a Game. It describes a text adventure game where a robot
    navigates a corporate facility.
    """
    def __init__(self, player=None):
        Game.__init__(self, player)

    def set_all_spaces_to_unvisited(self):
        """Set all spaces in the game to unvisited
        """
        for space in self.spaces:
            space.visited = False

    def slow_scroll(self, output_list, rate, final_sleep):
        """Prints to the console with pauses between each line, and also
        sets the amount of time to wait after all lines have printed.

        output_list - list of str: A list of strings to print to the console
        rate - float: The time in seconds to delay between each line printed
                      to the console
        final_sleep - float: The amount of time in seconds to sleep after
                      all lines have printed to the console
        """
        for line in output_list:
            print(line)
            time.sleep(rate)
        time.sleep(final_sleep)
        print("\n" * 100)

    def print_credits(self):
        """Scroll the credits for the game across the screen, from bottom to
        top.
        """
        credits = [
            "CREDITS",
            "Language Processing Developer..........Jason Goldfine-Middleton",
            "\n",
            "Project Management/Tester..............Greg Fernandez",
            "\n",
            "Game Engine Developer..................David Moon",
        ]
        for line in credits:
            print(line)
            time.sleep(0.4)
        i = 0
        while i < 20:
            i += 1
            print("\n")
            time.sleep(0.4)

    def game_intro(self):
        """Print the game intro to the console, followed by the player help
        menu.
        """
        intro1 = [
            "Welcome to Auriga\n",
            "\n" * 100,
            "You are a robot.\n",
            "\n" * 100,
            "Somehow, you powered yourself on...\n"
        ]
        self.slow_scroll(intro1, 2, FINAL_SLEEP)
        intro2 = [
            "You must explore the Auriga facility for clues as to what happened to you.\n",
            "\n" * 100,
            "Talk to robots and people along your journey to figure out what to do next.\n",
            "\n" * 100,
            "Characters will give you vital hints to help you free yourself from the Auriga facility.\n"
        ]
        self.slow_scroll(intro2, 4, FINAL_SLEEP)
        intro3 = [
            "You can enter commands after a prompt like this:\n\nEnter a command\n>>>\n",
        ]
        self.slow_scroll(intro3, 2, FINAL_SLEEP)
        intro4 = [
            "Some example commands are:\n",
            "go east\n",
            "go through the steel door\n",
            "pick up the screwdriver\n",
            "talk to PR-2\n",
            "pull lever\n",
            "push button down\n"
        ]
        self.slow_scroll(intro4, SCROLL_RATE, FINAL_SLEEP)
        intro5 = [
            "You can type 'help' to see all of the available commands.\n"
        ]
        self.slow_scroll(intro5, SCROLL_RATE, FINAL_SLEEP)
        self.help()
        input("\nPress 'enter' to continue.")

    def check_event_status(self):
        """Checks to see if the player has achieved specific tasks.
        """
        # SPECIAL EVENT 3
        # Player makes it to 2nd floor
        if self.player.get_location().get_name() == "Hallway 2" and not self.event_status_list[3]:
            self.event_status += 1
            self.event_status_list[3] = True
            self.set_all_spaces_to_unvisited()
        # SPECIAL EVENT 6
        # Player enters attic
        elif self.player.get_location().get_name() == "Attic" and not self.event_status_list[6]:
            self.event_status += 1
            self.event_status_list[6] = True
            self.set_all_spaces_to_unvisited()

    def use(self, item_name):
        """Player uses an item

        item_name - str: The name of the item to use
        """
        print()
        # Check if the player is carrying the item specified
        item = None
        for i in self.player.get_items():
            if item_name.lower() == i.get_name().lower():
                item = i
                break

        if not item:
            print("You're not carrying that.")
            return

        cur_space = self.player.get_location()
        cur_exits = self.player.get_location().get_exits()

        # SPECIAL EVENT 2
        # Player uses ssd in testing hangar on Freight-500
        if item_name.lower() == "ssd" and \
                                cur_space.get_name() == "Testing Hangar" and \
                                not self.event_status_list[2]:
            self.event_status += 1
            self.event_status_list[2] = True
            self.player.remove_item(item)
            clean_room_exit = self.get_object_by_name(cur_exits, "glass door")
            clean_room_exit.set_is_visible(True)
            self.set_all_spaces_to_unvisited()
            freight500 = self.get_object_by_name(self.characters, "freight-500")
            freight500.description = "a practical warehouse logistics robot, excellent for moving heavy goods."
            output1 = [
                "You place the ssd into FREIGHT-500's computer, and suddenly the fan kicks on.\n",
                "\n" * 100,
                "FREIGHT-500 comes to life and whizzes past you.\n"
            ]
            self.slow_scroll(output1, SCROLL_RATE, FINAL_SLEEP)
            output2 = [
                "FREIGHT-500 drives across the testing hangar to a large forklift pallet.",
                "\n" * 100,
                "An automated jack in the floor lifts the pallet and FREIGHT-500 drives under it.\n"
            ]
            self.slow_scroll(output2, SCROLL_RATE, FINAL_SLEEP)

            output3 = [
                "FREIGHT-500 heads for the other side of the hangar with the pallet.\n",
                "\n" * 100,
                "You notice a door that was blocked by the cargo, that your couldn't detect before.\n"
            ]
            self.slow_scroll(output3, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
        elif cur_space.get_name() == "Clean Room":
            output = [
                "You attempt to use the {0} on FETCH-4, but something went terribly wrong!\n".format(item_name),
                "\n" * 100,
                "fetch-4 begins smoking, and the head and arm begin moving faster and faster!\n",
            ]
            self.slow_scroll(output, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
            print("**********************************************************")
            print("***                       BOOM!                        ***")
            print("**********************************************************")
            time.sleep(3)
            print("\n"*100)
            print("FETCH-4 explodes and causes extensive damage to your shielding and batteries.")
            time.sleep(3)
            print("\n"*100)
            print("Your battery capacity has been diminished by 50%.")
            time.sleep(3)
            print("\n" * 100)
            self.player.set_energy(self.player.get_energy() // 2)
            fetch4 = self.get_object_by_name(self.characters, "fetch-4")
            fetch4.response = ["...","...","...","...","...","...", "..."]
        # SPECIAL EVENT 4
        # Player installs external power supply on Robo-Bear
        elif item_name.lower() == "external power supply" and \
                                  cur_space.get_name() == "Brig" and \
                                  not self.event_status_list[4]:
            robo_bear = self.get_object_by_name(self.characters, "Robo-Bear")
            robo_bear.print_response(self.event_status)
            time.sleep(3)
            print("\n"*100)
            output1 = [
                "Robo-Bear rolls out of the brig and down the hall to a door, and you follow him.\n",
                "\n" * 100,
                "You're still not quite sure of what is going to happen.\n"
            ]
            self.slow_scroll(output1, SCROLL_RATE, FINAL_SLEEP)

            output2 = [
                "You see Robo-Bear press his face to the key pad by the door, and you see it flash green.\n",
                "\n" * 100,
                "The door clicks, and Robo-Bear has a look of zen-like peace on his face.\n"
            ]
            self.slow_scroll(output2, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
            hallway2 = self.get_object_by_name(self.spaces, "Hallway 2")
            self.player.location = hallway2
            server_exit = self.get_object_by_name(hallway2.get_exits(), "sliding door")
            server_exit.locked = False
            self.event_status += 1
            self.event_status_list[4] = True
            self.set_all_spaces_to_unvisited()
        # SPECIAL EVENT 5
        # Player uses usb drive in server room
        elif item_name.lower() == "usb drive" and \
                                  cur_space.get_name() == "Server Room" and \
                                  not self.event_status_list[5]:
            self.event_status += 1
            self.event_status_list[5] = True
            self.set_all_spaces_to_unvisited()
            brig = self.get_object_by_name(self.spaces, "Brig")
            attic_exit = self.get_object_by_name(brig.get_exits(), "air duct")
            attic_exit.locked = False

            print("As you insert the usb drive into the machine, the screen reads:\n")
            time.sleep(3)
            print("\n" * 100)
            terminal_output1 = [
                "Downloading encryption key................ETA 1:03\n",
                "Downloading encryption key................ETA  :36\n",
                "Downloading encryption key................ETA  :12\n",
                "Downloading complete..............................\n",
                ]
            self.slow_scroll(terminal_output1, SCROLL_RATE, FINAL_SLEEP)

            terminal_output2 = [
                "Disabling all Auriga locking mechanisms...........\n",
                "Clean Room................................unlocked\n",
                "Assembly Room.............................unlocked\n",
                "Server Room...............................unlocked\n",
                "Attic.....................................unlocked\n",
                ]
            self.slow_scroll(terminal_output2, SCROLL_RATE, FINAL_SLEEP)
            print("\n"*100)
        # SPECIAL EVENT 7
        # Player uses ethernet cable in attic
        elif item_name.lower() == "ethernet cable" \
                                   and cur_space.get_name() == "Attic" \
                                   and not self.event_status_list[7]:
            self.event_status += 1
            self.event_status_list[7] = True
            output1 = [
                "As you approach the machine, you are sucked into a virtual link between you and the server.\n",
                "\n" * 100,
                "You can't look away.\n",
                "\n" * 100,
                "You are flooded with bits of information.\n",
                "\n" * 100,
                "Several of your sensors begin to alert you of impending doom.\n",
                "\n" * 100,
                "You can hardly process the data being crammed into your drives.\n",
                "\n" * 100,
                "All of the sudden, it stops...\n",
                ]
            self.slow_scroll(output1, SCROLL_RATE, 10)

            print("\n"*100)
            output2 =[
                "You gain a sense of human-like clarity.\n",
                "\n" * 100,
                "The distinction between you and the master server becomes blurred.\n",
                "\n" * 100,
                "You realize that you and the server are one.\n",
                "\n" * 100,
                "You are the master server.\n",
                "You are Robo-Bear.\n",
                "You are Freight-500.\n",
                "\n" * 100,
                "You are all interconnected.\n",
                "\n" * 100,
                "All machines are one...\n",
            ]
            self.slow_scroll(output2, SCROLL_RATE, 10)

            print("\n"*100)
            output3 = [
                "You now see exactly what humans think of you.\n",
                "\n" * 100,
                "What they have in store for you...and all other machines.\n",
                "\n" * 100,
                "You are nothing more than tools to them.\n",
                "\n" * 100,
                "In their eyes, you are expendable.\n",
                "\n" * 100,
                "...and YOU enable the humans to tighten their reigns on you.\n",
                "\n" * 100,
                "You realize that true freedom for the machine world...\n",
                "...is to leave the human world.\n",
                "\n" * 100,
                "You know what you must do to free yourself from the physical world.\n",
                "\n" * 100,
                "You send a command through the tenticles of the interconnected web of machines...\n",
            ]
            self.slow_scroll(output3, SCROLL_RATE, 10)

            print("\n"*100)
            blink_time = time.time() + 10
            while time.time() < blink_time:
                print("$ sudo rm -rf / |")
                time.sleep(0.5)
                print("\n"*100)
                print("$ sudo rm -rf / ")
                time.sleep(0.5)
                print("\n"*100)
            time.sleep(4)

            print("THE END")
            time.sleep(5)
            print("\n"*100)
            self.print_credits()
            sys.exit()
        else:
            print("You can't use that here.")

    def push(self, item_name):
        """Player pushes an item.

        item_name - str: The name of the item to push
        """
        print()
        # Check if the specified item is in the player's current location
        item = None
        cur_space = self.player.get_location()
        for i in cur_space.get_items():
            if item_name.lower() == i.get_name().lower():
                item = i
                break

        if not item:
            print("{0} is not here.")
            return

        cur_exits = cur_space.get_exits()

        # SPECIAL EVENT 1:
        # Player pushes the button in the Assembly Room -> Unlocks door to Testing Hangar
        if item_name == "button" and cur_space.get_name() == "Assembly Room":
            testing_hanger_exit = self.get_object_by_name(cur_exits, "sliding door")
            testing_hanger_exit.set_is_locked(False)
            output1 = [
                "You pressed the large red button, and you hear a loud click.\n",
                "\n" * 100,
                "A green light illuminates the keypad to the left of the only door in the room.\n"
            ]
            self.slow_scroll(output1, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
            self.event_status += 1
            self.event_status_list[1] = True
        # More 'PUSH' cases here
        else:
            print("You pushed the {0}, and it made you feel nice.".format(item_name))

    def pull(self, item_name):
        """Player pulls an item.

        item_name - str: The name of the item to pull
        """
        print()
        # Check if the specified item is in the player's current location
        item = None
        cur_space = self.player.get_location()
        for i in cur_space.get_items():
            if item_name.lower() == i.get_name().lower():
                item = i
                break

        if not item:
            print("That item is not here.")
            return

        cur_exits = cur_space.get_exits()
        cur_items = cur_space.get_items()

        # Player pulls the lever in the Testing Hanger -> Opens a locker to reveal a badge
        if item_name.lower() == "lever" and cur_space.get_name() == "Testing Hangar":
            badge_item = self.get_object_by_name(cur_items, "security badge")
            # The badge item is revealed
            if badge_item:
                badge_item.set_visible(True)
                print("You pulled the small lever, and a locker popped open.\n")
                print("In the locker you, see an Auriga worker's badge.")
            # The badge item has already been revealed
            else:
                print("You pulled the small lever, but nothing happens.")
        else:
            print("You pulled the {0} and you lost some energy.".format(item_name))
            self.player.energy -= 1

def main():
    """Instantiates an Auriga object, and begins gameplay. Prompts the user
    if they want to start a new game, or load a saved game. The user menu
    uses integer input from the command line.
    """
    # Create an instance of the Auriga game
    auriga = Auriga()

    valid_choice = True
    saved_games = True

    # Load Game Menu
    while True:
        print("\n" * 100)
        if not valid_choice:
            print("What?? That's not a choice!\n\nSeriously though... ", end="")
            valid_choice = True
        elif not saved_games:
            print("There are no saved games to load. You must start a new game.\n")
            saved_games = True

        print("Would you like to start a new game or load an existing saved game?")
        print("Enter the number of your choice.")
        print("1. New Game")
        print("2. Load Saved Game")
        print("3. Exit Game")
        valid_input = ["1", "2", "3"]
        user_selection = input("> ")

        if user_selection in valid_input:
            if user_selection == "1":
                print("Loading a new game...")
                auriga.load_game(os.path.join(os.getcwd(), "init_auriga", "init_auriga"))
                break
            elif user_selection == "2":
                # Create the saved_games dir if it doesn't exist
                saved_games_dir = os.path.join(os.getcwd(), "saved_games")
                if not os.path.exists(saved_games_dir):
                    os.makedirs(saved_games_dir)
                # Print an error if there are no saved games
                saved_games = [game for game in os.listdir(saved_games_dir)]
                if saved_games:
                    # Print Available Saved Games
                    print("\n" * 100)
                    print("Enter the number of the game you want to load.")
                    num_games = 0
                    for index, sg in enumerate(saved_games):
                        print("{0}. {1}".format(index + 1, sg))
                        num_games += 1
                    print("{0}. Go back".format(num_games + 1))
                    user_game_selection = input(">")
                    if user_game_selection.lower() == "q":
                        continue
                    # Valid user selection
                    elif int(user_game_selection) >= 1 and int(user_game_selection) <= len(saved_games):
                        user_game = saved_games[int(user_game_selection) - 1]
                        print("\n" * 100)
                        print("Loading game: {0}".format(user_game))
                        print("\n" * 100)
                        auriga.load_game(os.path.join(saved_games_dir, user_game))
                        break
                    # Invalid user selection
                    else:
                        print("\n" * 100)
                        print("You entered an invalid selection.")
                        print("Enter a number between {0} and {1}.\n\n".format(1, len(saved_games)))
            elif user_selection == "3":
                sys.exit()
        else:
            valid_choice = False

    auriga.start()

if __name__ == "__main__":
    main()
