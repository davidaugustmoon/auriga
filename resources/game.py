#!/usr/bin/env python3

# Standard Library
import sys
import os
import datetime
import json
import subprocess
import time

# Third Party
from termios import tcflush, TCIFLUSH

# Auriga
from resources.space import Space
from resources.item import Item
from resources.character import Character
from resources.player import Player, DEFAULT_CAPACITY
from resources.exit import Exit
from parser.parser import Parser

# The parser will determine one of the listed game commands based on the user input
GO = "go"
TAKE = "take"
DROP = "drop"
TALK = "talk"
LOOK = "look"
SAVEGAME = "savegame"
QUIT = "quit"
LOOK_AT = "look at"
LISTEN = "listen"
PULL = "pull"
PUSH = "push"
CHARGE = "recharge"
USE = "use"
WAIT = "wait"
HELP = "help"
INVENTORY = "inventory"
LOADGAME = "loadgame"
commands = [GO, TAKE, DROP, TALK, LOOK, SAVEGAME, QUIT, LOOK_AT, LISTEN,
            PULL, PUSH, CHARGE, USE, WAIT, HELP, INVENTORY, LOADGAME]

BACKGROUND_MUSIC = "dark_rumble.wav"
EVENT_MUSIC = "epic_combat.wav"

class Game(object):
    def __init__(self, player=None):
        if player:
            self.player = player
        self.event_status = 0 # set accordingly for player achievments
        self.event_status_list = [False, False, False, False, False, False, False, False]
        self.spaces = []
        self.characters = []
        self.exits = []
        self.items = []
        self.background_music = None
        self.event_music = None

    def get_spaces(self):
        """Return all of the space objects in the game.
        """
        return self.spaces

    def get_characters(self):
        """Return all of the character objects in the game.
        """
        return self.characters

    def get_exits(self):
        """Return all of the exit objects in the game.
        """
        return self.exits

    def get_items(self):
        """Return all of the item objects in the game.
        """
        return self.items

    def print_objects(self):
        """Print all space names, character names, and item names in the game.
        for testing
        """
        print("Spaces: {}".format([s.name for s in self.spaces]))
        print("Characters: {}".format([c.name for c in self.characters]))
        print("Items: {}".format([i.name for i in self.items]))

    def start_music(self, sound_file):
        """Plays a music wav file.
        Returns the pid of the subprocess that started the wav file.
        """
        # supress output from playing sound file
        devnull = open(os.devnull, 'wb')
        music = subprocess.Popen(["aplay", "sounds/" + sound_file],
                                  stdout=subprocess.PIPE, stderr=devnull)
        return music

    def kill_music(self):
        """Kills any music processes currently playing.
        """
        if self.background_music is not None \
           and self.background_music.poll() is None:
            self.background_music.kill()

        if self.event_music is not None \
           and self.event_music.poll() is None:
            self.event_music.kill()

    def start(self):
        """Start the game. This is the main game loop. This loop does not exit
        until the game is finished.
        """
        self.background_music = self.start_music(BACKGROUND_MUSIC)

        p = Parser()
        if self.event_status < 1:
            print("\n" * 100)
            self.game_intro()
            print("\n" * 100)

        playing = True
        while playing:
            # If background music loop has stopped, restart it.
            if self.background_music.poll() is not None:
                self.background_music = self.start_music(BACKGROUND_MUSIC)

            self.check_upgrades()
            self.check_energy()
            self.check_event_status()
            cur_location = self.player.get_location()
            print_space_info(cur_location, self.event_status)
            print_player_info(self.player)
            cur_location.set_visited(True)

            player_command = get_command()
            cmd_action, cmd_exit, cmd_direction, cmd_item, cmd_character = Parser.action_requested(player_command)

            print("\n" * 100)
            if cmd_action == GO:
                self.player.go_exit(self.event_status, direction=cmd_direction, exit_name=cmd_exit)

            elif cmd_action == TAKE:
                self.player.take(cmd_item)

            elif cmd_action == DROP:
                self.player.drop(cmd_item)

            elif cmd_action == TALK:
                self.player.talk(cmd_character, self.event_status)

            elif cmd_action == LOOK:
                self.player.look(self.event_status)

            elif cmd_action == SAVEGAME:
                tmp_save_dir = input("Enter the save name\n> ")
                if tmp_save_dir:
                    save_dir = tmp_save_dir
                else:
                    save_dir = None
                self.save(save_dir)

            elif cmd_action == QUIT:
                print("Exiting the game...")
                self.kill_music()
                return

            elif cmd_action == LOOK_AT:
                self.player.look_at(cmd_item)

            elif cmd_action == LISTEN:
                self.player.listen()

            elif cmd_action == PULL:
                self.pull(cmd_item)

            elif cmd_action == PUSH:
                self.push(cmd_item)

            elif cmd_action == CHARGE:
                self.player.charge()

            elif cmd_action == USE:
                self.use(cmd_item)

            elif cmd_action == WAIT:
                pass

            elif cmd_action == HELP:
                self.help()

            elif cmd_action == INVENTORY:
                self.player.print_inventory()

            elif cmd_action == LOADGAME:
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
                print("\n" * 100)
                self.load_game(os.path.join(saved_games_dir, user_game))
            else:
                print("Huh? That doesn't make any sense.")

    def get_event_status(self):
        """Return the event status that corresponds to the player's current
        achievements.
        """
        return self.event_status

    def set_player(self, new_player):
        """Set the main player in the game.

        :param new_player - Player: The player in the game
        """
        self.player = new_player

    def get_player(self):
        """ Return the main player in the game.
        """
        return self.player

    def get_player_location(self):
        """Return the player's current location.
        """
        return self.player.location

    def get_player_items(self):
        """Return a list of the player's currently held items.
        """
        return self.player.items

    def set_event_status(self, new_event_status):
        """Set the event status of the game, that corresponds to the player's
        current achievements.
        """
        self.event_status = new_event_status

    def check_event_status(self):
        """This should be over-written in a child class.
        """
        pass

    def check_energy(self):
        """Check the player's current energy level. If it is low, print a
        warning. If the player runs out of energy, terminate the game.
        """
        if self.player.get_energy() <= 0:
            print("\nSorry, you ran out of energy and died.")
            print("Maybe the AI program will bring you back again...")
            sys.exit()
        elif self.player.get_energy() < 15:
            print("\nYou're getting low on energy.")
            print("You'll need to find a charger quick!")

    def to_json_dict(self):
        """Write all of the game fields to a json dict. Writes the ids of
        objects.
        """
        json_dict = {}
        json_dict['event_status'] = self.event_status
        json_dict['event_status_list'] = self.event_status_list
        json_dict['spaces'] = [s.get_id() for s in self.spaces]
        json_dict['characters'] = [c.get_id() for c in self.characters]
        json_dict['exits'] = [e.get_id() for e in self.exits]
        json_dict['items'] = [i.get_id() for i in self.items]
        return json_dict

    def save(self, dir_name=None):
        """
        Saves game data in the following structure
        /saved_games/
            game_name_YYYY-MM-DD HH:MM:SS/
                player/
                    player_name.json
                game/
                    game_name.json
                items/
                    item_name.json
                    ...
                characters/
                    character_name.json
                    ...
                spaces/
                    space_name.json
                    ...
                exits/
                    exit_id.json
                    ...
        """
        root_dir = os.getcwd()
        cur_datetime = str(datetime.datetime.now()).split(".")[0]  # remove fractional seconds
        if not dir_name:
            dir_name = "game_" + cur_datetime + "/"
        save_dir = root_dir + "/saved_games/" + dir_name + "_" + cur_datetime + "/"

        # Check if the filepath already exists
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Game
        game_dir = save_dir + "game/"
        os.makedirs(game_dir)
        with open(game_dir + "game.json", "w") as file_handle:
            game_dict = self.to_json_dict()
            json.dump(game_dict, file_handle)

        # Player
        player_dir = save_dir + "player/"
        os.makedirs(player_dir)
        with open(player_dir + "player.json", "w") as file_handle:
            player_dict = self.player.to_json_dict()
            json.dump(player_dict, file_handle)

        # Items
        items_dir = save_dir + "items/"
        os.makedirs(items_dir)
        for i in self.items:
            with open(items_dir + i.get_name() + "_" + str(i.get_id()) + ".json", "w") as file_handle:
                item_dict = i.to_json_dict()
                json.dump(item_dict, file_handle)

        # Characters
        characters_dir = save_dir + "characters/"
        os.makedirs(characters_dir)
        for c in self.characters:
            with open(characters_dir + c.get_name() + "_" + str(c.get_id()) + ".json", "w") as file_handle:
                character_dict = c.to_json_dict()
                json.dump(character_dict, file_handle)

        # Spaces
        spaces_dir = save_dir + "spaces/"
        os.makedirs(spaces_dir)
        for s in self.spaces:
            with open(spaces_dir + s.get_name() + "_" + str(s.get_id()) + ".json", "w") as file_handle:
                spaces_dict = s.to_json_dict()
                json.dump(spaces_dict, file_handle)

        # Exits
        exits_dir = save_dir + "exits/"
        os.makedirs(exits_dir)
        for e in self.exits:
            with open(exits_dir + e.get_name() + "_" + str(e.get_id()) + ".json", "w") as file_handle:
                exits_dict = e.to_json_dict()
                json.dump(exits_dict, file_handle)

    def load_game(self, load_dir):
        """Load a game instance from json files.

        :param load_dir - str: The full filepath to the game instance's top level
                        directory.
        """
        self.reset_game_fields()
        # Set Game data
        game_space_ids = []
        game_character_ids = []
        game_item_ids = []
        game_exit_ids = []
        with open(os.path.join(load_dir, "game/game.json")) as file_handle:
            game_data = json.load(file_handle)
            self.event_status = game_data['event_status']
            self.event_status_list = game_data['event_status_list']
            game_space_ids = game_data['spaces']
            game_character_ids = game_data['characters']
            game_exit_ids = game_data['exits']
            game_item_ids = game_data['items']

        # Create Player
        player_item_ids = []
        with open(os.path.join(load_dir, "player/player.json")) as file_handle:
            player_data = json.load(file_handle)
            player_name = player_data['name']
            player_alive = player_data['alive']
            player_energy = player_data['energy']
            player_capacity = player_data['capacity']
            player_description = player_data['description']
            player_items = player_data['items']
            player_location = player_data['location']
            new_player = Player(name=player_name, description=player_description, capacity=player_capacity,
                                alive=player_alive, energy=player_energy, items=player_items,
                                location=player_location)
            # Add player to Game
            self.player = new_player

        # Create Items
        item_files = os.listdir(os.path.join(load_dir, "items"))
        for file in item_files:
            with open(os.path.join(load_dir, "items", file)) as file_handle:
                item_data = json.load(file_handle)
                item_name = item_data['name']
                item_visible = item_data['visible']
                item_locked = item_data['locked']
                item_weight = item_data['weight']
                item_description = item_data['description']
                item_id = item_data['id']

                i = Item(new_id=item_id, name=item_name, visible=item_visible, locked=item_locked,
                         weight=item_weight, description=item_description)
                self.items.append(i)

        # Create Characters
        character_files = os.listdir(os.path.join(load_dir, "characters"))
        for file in character_files:
            with open(os.path.join(load_dir, "characters", file)) as file_handle:
                char_data = json.load(file_handle)
                char_name = char_data['name']
                char_response = char_data['response']
                char_description = char_data['description']
                char_id = char_data['id']

                c = Character(new_id=char_id, name=char_name, description=char_description, response=char_response)
                self.characters.append(c)

        # Create Spaces
        space_files = os.listdir(os.path.join(load_dir, "spaces"))
        for file in space_files:
            with open(os.path.join(load_dir, "spaces", file)) as file_handle:
                space_data = json.load(file_handle)
                space_name = space_data['name']
                space_long_description = space_data['long_description']
                space_short_description = space_data['short_description']
                space_visited = space_data['visited']
                space_id = space_data['id']
                space_characters = space_data['characters']
                space_exits = space_data['exits']
                space_items = space_data['items']

                s = Space(new_id=space_id, name=space_name, long_description=space_long_description,
                          short_description=space_short_description, visited=space_visited,
                          items=space_items, characters=space_characters, exits=space_exits)
                self.spaces.append(s)

        # Create Exits
        exit_files = os.listdir(os.path.join(load_dir, "exits"))
        for file in exit_files:
            with open(os.path.join(load_dir, "exits", file)) as file_handle:
                exit_data = json.load(file_handle)
                exit_space = exit_data['space']
                exit_name = exit_data['name']
                exit_direction = exit_data['direction']
                exit_unlock_item = exit_data['unlock_item']
                exit_visible = exit_data['visible']
                exit_id = exit_data['id']
                exit_locked = exit_data['locked']
                exit_description = exit_data['description']

                e = Exit(new_id=exit_id, space=exit_space, name=exit_name, direction=exit_direction,
                         unlock_item=exit_unlock_item, visible=exit_visible, locked=exit_locked,
                         description=exit_description)
                self.exits.append(e)

        # Set player location
        loc_id = self.player.location
        self.player.location = self.get_object_by_id(self.spaces, loc_id)

        # Set player items
        player_item_ids = self.player.items
        new_player_items = []
        for item_id in player_item_ids:
            cur_item = self.get_object_by_id(self.items, item_id)
            new_player_items.append(cur_item)
        self.player.items = new_player_items

        # Place items, characters, and exits in spaces
        for space in self.spaces:
            item_ids = space.items
            character_ids = space.characters
            exit_ids = space.exits
            space.items = []
            space.characters = []
            space.exits = []
            # items
            for item_id in item_ids:
                item_obj = self.get_object_by_id(self.items, item_id)
                space.items.append(item_obj)
            # characters
            for character_id in character_ids:
                character_obj = self.get_object_by_id(self.characters, character_id)
                space.characters.append(character_obj)
            # exits
            for exit_id in exit_ids:
                exit_obj = self.get_object_by_id(self.exits, exit_id)
                space.exits.append(exit_obj)

        # Link spaces to exits, and add unlock items
        for exit in self.exits:
            space_id = exit.space
            item_id = exit.unlock_item
            exit.space = None
            exit.unlock_item = None
            exit.space = self.get_object_by_id(self.spaces, space_id)
            exit.unlock_item = self.get_object_by_id(self.items, item_id)

    def help(self):
        """Print a help menu for the player.
        """
        print("GAME HELP")
        print("Command\t\t\t\tDescription\n")
        print("{0} <{1}> || <{2}>:\t{3}".format(GO, "direction", "exit", "Move through an exit."))
        print("{0} <{1}>:\t\t\t{2}".format(TAKE, "item", "Take an item."))
        print("{0} <{1}>:\t\t\t{2}".format(DROP, "item", "Drop an item."))
        print("{0} <{1}>:\t\t{2}".format(TALK, "character", "Talk to a character."))
        print("{0}:\t\t\t\t{1}".format(LOOK, "Look around the space you are currently in."))
        print("{0}:\t\t\t{1}".format(SAVEGAME, "Save your current game."))
        print("{0}:\t\t\t\t{1}".format(QUIT, "Quit the game."))
        print("{0} <{1}>:\t\t\t{2}".format(LOOK_AT, "item", "Look more closely at an item."))
        print("{0}:\t\t\t\t{1}".format(LISTEN, "Listen more closely to the sounds around you."))
        print("{0} <{1}>:\t\t\t{2}".format(PULL, "item", "Pull an item."))
        print("{0} <{1}>:\t\t\t{2}".format(PUSH, "item", "Push an item."))
        print("{0}:\t\t\t{1}".format(CHARGE, "Charge your batteries in a charger."))
        print("{0} <{1}>:\t\t\t{2}".format(USE, "item", "Use an item you are carrying."))
        print("{0}:\t\t\t\t{1}".format(WAIT, "Wait for something to happen."))
        print("{0}:\t\t\t\t{1}".format(HELP, "Print this help message."))
        print("{0}:\t\t\t{1}".format(INVENTORY, "Print the items you are currently carrying."))
        print("{0}:\t\t\t{1}".format(LOADGAME, "Load a previously saved game."))

    def use(self, item_name):
        """Player uses an item, should be over-written in a child class.
        """
        pass

    def get_object_by_name(self, object_list, object_name):
        """Return an object by its name. Intended to be used for retrieving
        a character, item, or space in the game class.
        """
        obj = None
        for i in object_list:
            if i.get_name().lower() == object_name.lower():
                obj = i
                break
        return obj

    def get_object_by_id(self, object_list, object_id):
        """Return an object by its id. Intended to be use for retreiving
        a character, item, or space in the game class.
        """
        obj = None
        for i in object_list:
            if i.get_id() == object_id:
                obj = i
                break
        return obj

    def check_upgrades(self):
        """Check if the player is carrying any items that give them an upgrade.
        """
        if "hmi-25" in self.player.get_item_names():
            self.player.set_capacity(DEFAULT_CAPACITY + 25)
        if "hmi-50" in self.player.get_item_names():
            self.player.set_capacity(DEFAULT_CAPACITY + 50)

    def reset_game_fields(self):
        """Reset all fields to empty.
        """
        self.player = None
        self.event_status = 0 # set accordingly for player achievments
        self.event_status_list = [False, False, False, False, False, False, False, False]
        self.spaces = []
        self.characters = []
        self.exits = []
        self.items = []

def get_command():
    """Get a single line command from the user.
    """
    tcflush(sys.stdin, TCIFLUSH)
    command = input("\nEnter a command\n>>> ")
    return command

def print_space_info(space, event_index):
    """Print details about a particular space.

    :param space - Space: The space to print details about
    :param event_index - int: The int that corresponds to the player's current
                       achievements
    """
    space.print_details(event_index)

def print_player_info(player):
    """Print information about the player.

    :param player - Player: The player to print information about
    """
    print("\nPLAYER INFO:")
    player.print_energy()
    print("Current location: {}".format(player.location.name))
    print("Carrying: {0}/{1}".format(player.get_items_total_weight(), player.get_capacity()))
