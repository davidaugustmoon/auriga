#!/usr/bin/env python3

# Standard Library
import sys
import os
import datetime
import json

# Auriga
from resources.space import Space
from resources.item import Item
from resources.character import Character
from resources.player import Player, DEFAULT_CAPACITY
from resources.exit import Exit
from parser.parser import Parser

# The parser should determine one of the listed game commands based on the user input
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
CHARGE = "charge"
USE = "use"
WAIT = "wait"
HELP = "help"
INVENTORY = "inventory"
LOADGAME = "loadgame"
commands = [GO, TAKE, DROP, TALK, LOOK, SAVEGAME, QUIT, LOOK_AT, LISTEN,
            PULL, PUSH, CHARGE, USE, WAIT, HELP, INVENTORY, LOADGAME]

class Game(object):
    def __init__(self, player):
        self.player = player
        self.event_status = 0 # set accordingly for player achievments
        self.event_status_list = [False, False, False, False, False]
        self.spaces = []
        self.characters = []
        self.exits = []
        self.items = []

    def get_spaces(self):
        return self.spaces

    def get_characters(self):
        return self.characters

    def get_exits(self):
        return self.exits

    def get_items(self):
        return self.items

    def print_objects(self):
        """
        for testing
        """
        print("Spaces: {}".format([s.name for s in self.spaces]))
        print("Characters: {}".format([c.name for c in self.characters]))
        print("Items: {}".format([i.name for i in self.items]))

    def start(self):
        p = Parser()
        print("\n" * 100)

        playing = True
        while playing:
            self.check_upgrades()
            self.check_energy()
            cur_location = self.player.get_location()
            self.check_event_status()
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
                sys.exit()

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
                self.load_game()
            else:
                print("Huh? That doesn't make any sense.")


    def check_event_status(self):
        print("check_event_status() should be overridden in the child class.")

    def get_event_status(self):
        return self.event_status

    def get_player(self):
        return self.player

    def get_player_location(self):
        return self.player.location

    def get_player_items(self):
        return self.player.items

    def get_event_status(self):
        return self.event_status

    def set_event_status(self, new_event_status):
        self.event_status = new_event_status

    def check_energy(self):
        if self.player.get_energy() <= 0:
            print("Sorry, you ran out of energy and died.")
            print("Maybe the AI program will bring you back again...")
            sys.exit()
        elif self.player.get_energy() < 25:
            print("You're getting low on energy.")
            print("You'll need to find a charger quick!")

    def to_json_dict(self):
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
            with open(items_dir + i.get_name() + ".json", "w") as file_handle:
                item_dict = i.to_json_dict()
                json.dump(item_dict, file_handle)

        # Characters
        characters_dir = save_dir + "characters/"
        os.makedirs(characters_dir)
        for c in self.characters:
            with open(characters_dir + c.get_name() + ".json", "w") as file_handle:
                character_dict = c.to_json_dict()
                json.dump(character_dict, file_handle)

        # Spaces
        spaces_dir = save_dir + "spaces/"
        os.makedirs(spaces_dir)
        for s in self.spaces:
            with open(spaces_dir + s.get_name() + ".json", "w") as file_handle:
                spaces_dict = s.to_json_dict()
                json.dump(spaces_dict, file_handle)
            # print("saving space: {}".format(s.get_name()))

        # Exits
        exits_dir = save_dir + "exits/"
        os.makedirs(exits_dir)
        for e in self.exits:
            with open(exits_dir + str(e.get_id()) + ".json", "w") as file_handle:
                exits_dict = e.to_json_dict()
                json.dump(exits_dict, file_handle)

    def load_game(self):
        pass

    def help(self):
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
        print("{0}:\t\t\t\t{1}".format(CHARGE, "Charge your batteries in a charger."))
        print("{0} <{1}>:\t\t\t{2}".format(USE, "item", "Use an item you are carrying."))
        print("{0}:\t\t\t\t{1}".format(WAIT, "Wait for something to happen."))
        print("{0}:\t\t\t\t{1}".format(HELP, "Print this help message."))
        print("{0}:\t\t\t{1}".format(INVENTORY, "Print the items you are currently carrying."))
        print("{0}:\t\t\t{1}".format(LOADGAME, "Load a previously saved game."))

    def use(self, item_name):
        print("This function should be over-written in the child class.")

    def get_object_by_name(self, object_list, object_name):
        obj = None
        for i in object_list:
            if i.get_name() == object_name:
                obj = i
                break
        return obj

    def get_object_by_id(self, object_list, object_id):
        obj = None
        for i in object_list:
            if i.get_id() == object_id:
                obj = i
                break
        return obj

    def check_upgrades(self):
        if "HMI 25" in self.player.get_item_names():
            self.player.set_capacity(DEFAULT_CAPACITY + 25)
        if "HMI 50" in self.player.get_item_names():
            self.player.set_capacity(DEFAULT_CAPACITY + 50)

# Obviously these will all be completely re-done by the parser, this is 
# just to demonstrate a simple version of the game. This parser only 
# handles input in the form 'go 1', 'talk 2', 'take 1', etc.
def get_command():
    command = input("\nEnter a command\n>>> ")
    return command

def parse_command(command):
    return command.split(" ")

def print_space_info(space, event_index):
    # print("\nSPACE INFO:")
    space.print_details(event_index)

def print_player_info(player):
    print("\nPLAYER INFO:")
    player.print_energy()
    print("Current location: {}".format(player.location.name))
    print("Carrying: {0}/{1}".format(player.get_items_total_weight(), player.get_capacity()))
    # print("Items: {}".format(player.get_item_names()))
