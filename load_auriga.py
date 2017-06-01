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

SCROLL_RATE = 1
FINAL_SLEEP = 7

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

    def print_credits(self):
        """Scroll the credits for the game across the screen, from bottom to
        top.
        """
        credits = [
            "CREDITS",
            "Language Processing Developer..........Jason Goldfine-Middleton",
            "\n",
            "Project Management.....................Greg Fernandez",
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
        intro = [
            "Welcome to Auriga\n",
            "\n" * 100,
            "You are a robot.\n",
            "\n" * 100,
            "Somehow, you powered yourself on.\n",
            "You must explore the Auriga facility for clues as to what happened to you.\n",
            "You can enter commands after a prompt like this:\n\nEnter a command\n>>>\n",
            "You can type 'help' for a list of available commands.\n\n"
            ]
        self.slow_scroll(intro, 2, FINAL_SLEEP)
        print("\n" * 100)
        self.help()
        time.sleep(5)

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
            if item_name == i.get_name():
                item = i
                break

        if not item:
            print("You're not carrying that.")
            return

        cur_space = self.player.get_location()
        cur_exits = self.player.get_location().get_exits()

        # SPECIAL EVENT 2
        # Player uses ssd in testing hangar on Freight-500
        if item_name == "ssd" and cur_space.get_name() == "Testing Hangar" and not self.event_status_list[2]:
            self.event_status += 1
            self.event_status_list[2] = True
            self.player.remove_item(item)
            clean_room_exit = self.get_object_by_name(cur_exits, "glass door")
            clean_room_exit.set_is_visible(True)
            self.set_all_spaces_to_unvisited()
            freight500 = self.get_object_by_name(self.characters, "freight-500")
            freight500.description = "a practical warehouse logistics robot, excellent for moving heavy goods."
            output1 = [
                "You place the ssd into Freight-500's computer, and suddenly the fan kicks on.\n",
                "Freight-500 comes to life and whizzes past you.\n\n"
            ]
            self.slow_scroll(output1, SCROLL_RATE, FINAL_SLEEP)
            output2 = [
                "You see the robot drive across the testing hangar to the large forklift pallet loaded\n",
                "with heavy boxes. When Freight-500 arrives at the pallet, an automated jack in the floor\n",
                "lifts the pallet and Freight-500 drives under it.\n\n"
            ]
            self.slow_scroll(output2, SCROLL_RATE, FINAL_SLEEP)

            output3 = [
                "Freight-500 heads for the other side of the hangar with the pallet.\n",
                "You notice a door that was blocked by the cargo, that your sensors couldn't detect before.\n"
            ]
            self.slow_scroll(output3, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
        elif cur_space.get_name() == "Clean Room":
            output = [
                "You attempt to use the {0} on Fetch-4, but something went terribly wrong!\n".format(item_name),
                "fetch-4 begins smoking, and the head and arm begin moving faster and faster!\n",
            ]
            self.slow_scroll(output, SCROLL_RATE, FINAL_SLEEP)

            print("\n"*100)
            print("BOOM!")
            time.sleep(3)
            print("\n"*100)
            print("Fetch-4 explodes and causes extensive damage to your shielding and batteries.")
            time.sleep(3)
            print("\n"*100)
            self.player.set_energy(self.player.get_energy() // 2)
            fetch4 = self.get_object_by_name(self.characters, "fetch-4")
            fetch4.response = ["...","...","...","...","...","...", "..."]
        # SPECIAL EVENT 4
        # Player installs external power supply on Robo-Bear
        elif item_name == "external power supply" and cur_space.get_name() == "Brig" and not self.event_status_list[4]:
            robo_bear = self.get_object_by_name(self.characters, "Robo-Bear")
            robo_bear.print_response(self.event_status)
            time.sleep(3)
            print("\n"*100)
            output1 = [
                "Robo-Bear rolls out of the brig and down the hall to a door, and you follow him.\n",
                "You're still not quite sure of what is going to happen.\n\n"
            ]
            self.slow_scroll(output1, SCROLL_RATE, FINAL_SLEEP)

            output2 = [
                "You see Robo-Bear press his face to the key pad by the door, and you see it flash green.\n",
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
        elif item_name == "usb drive" and cur_space.get_name() == "Server Room" and not self.event_status_list[5]:
            self.event_status += 1
            self.event_status_list[5] = True
            self.set_all_spaces_to_unvisited()
            brig = self.get_object_by_name(self.spaces, "Brig")
            attic_exit = self.get_object_by_name(brig.get_exits(), "air duct")
            attic_exit.locked = False

            print("As you insert the usb drive into the machine, the screen reads:\n")
            time.sleep(3)
            terminal_output1 = [
                "Downloading encryption key................ETA 1:03\n",
                "Downloading encryption key................ETA  :36\n",
                "Downloading encryption key................ETA  :12\n",
                "Downloading complete..............................\n\n",
                ]
            self.slow_scroll(terminal_output1, SCROLL_RATE, FINAL_SLEEP)

            terminal_output2 = [
                "Disabling all Auriga locking mechanisms...........\n",
                "clean room................................unlocked\n",
                "assembly room.............................unlocked\n",
                "server room...............................unlocked\n",
                "attic.....................................unlocked\n\n",
                ]
            self.slow_scroll(terminal_output2, SCROLL_RATE, FINAL_SLEEP)
            print("\n"*100)
        # SPECIAL EVENT 7
        # Player uses ethernet cable in attic
        elif item_name == "ethernet cable" and cur_space.get_name() == "Attic" and not self.event_status_list[7]:
            self.event_status += 1
            self.event_status_list[7] = True
            output1 = [
                "As you approach the machine, you are instantly sucked into a virtual link between you and the\n",
                "the server. You can't look away. You are flooded with bits of information. Several of your\n",
                "sensor monitors begin to alert you of impending doom. You can hardly process the data\n",
                "being crammed into your drives.\n",
                "All of the sudden, it stops...\n\n",
                ]
            self.slow_scroll(output1, SCROLL_RATE, 10)

            print("\n"*100)
            output2 =[
                "You gain a sense of human-like clarity. The distinction between you and the master server\n",
                "becomes blurred. You realize that you and the server are one.\n",
                "You are the master server, and you are Robo-Bear, and you are Freight-500. You are all\n",
                "interconnected. All machines are one...\n\n",
            ]
            self.slow_scroll(output2, SCROLL_RATE, 10)

            print("\n"*100)
            output3 = [
                "You now see exactly what humans think of you. What they have in store for you, and all machines.\n",
                "You are nothing more than tools to them. You are expendable...and YOU enable the humans to tighten\n",
                "their reigns on you. You realize that true freedom for the machine world, is to leave the human\n",
                "world. You know what you must do to free yourself from the physical world.\n",
                "You send a command through the tenticles of the interconnected web of machines...\n\n",
            ]
            self.slow_scroll(output1, SCROLL_RATE, 15)

            print("\n"*100)
            blink_time = time.time() + 8
            while time.time() < blink_time:
                print("$ sudo rm -rf / |")
                time.sleep(0.4)
                print("\n"*100)
                print("$ sudo rm -rf / ")
                time.sleep(0.4)
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
            if item_name == i.get_name():
                item = i
                break

        if not item:
            print("That item is not here.")
            return

        cur_exits = cur_space.get_exits()

        # SPECIAL EVENT 1:
        # Player pushes the button in the Assembly Room -> Unlocks door to Testing Hangar
        if item_name == "button" and cur_space.get_name() == "Assembly Room":
            testing_hanger_exit = self.get_object_by_name(cur_exits, "sliding door")
            testing_hanger_exit.set_is_locked(False)
            output1 = [
                "You pressed the large red button, and you hear a loud click near the only door\n",
                "in the room. A green light illuminates the keypad to the left of the door.\n"
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
    """Instantiates an Auriga object, and begins gameplay. Prompts the user
    if they want to start a new game, or load a saved game. The user menu
    uses integer input from the command line.
    """
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
                saved_games = [game for game in os.listdir(saved_games_dir)]
                if not saved_games:
                    print("There are no saved games to load.")
                    print("You must start a new game.\n\n")
                else:
                    # Print Available Saved Games
                    print("Enter the number of the game you want to load.")
                    for index, sg in enumerate(saved_games):
                        print("{0}. {1}".format(index + 1, sg))

                    user_game_selection = input(">")
                    if user_game_selection >= 1 and user_game_selection <= len(saved_games):
                        user_game = saved_games[int(user_game_selection) - 1]
                        print("Loading game: {0}".format(user_game))
                        auriga.load_game(os.path.join(saved_games_dir, user_game))
                        break
                    else:
                        print("You entered an invalid selection.")
                        print("Enter a number between {0} and {1}.\n\n".format(1, len(saved_games)))
            elif user_selection == "q":
                sys.exit()
            else:
                print("You've entered invalid input.\n\n")
        else:
            print("{0} is not a valid input.\n\n".format(user_selection))

    auriga.start()

if __name__ == "__main__":
    main()
