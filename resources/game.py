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
from resources.player import Player
from resources.exit import Exit
from parser.parser import Parser

# The parser should determine one of the listed game commands based on the user input
GO = "go"
TAKE = "take"
DROP = "drop"
TALK = "talk"
LOOK = "look"
SAVE = "save"
QUIT = "quit"
commands = [GO, TAKE, DROP, TALK, LOOK, SAVE, QUIT]

class Game(object):
    def __init__(self, player):
        self.player = player
        self.event_status = 0 # set accordingly for player achievments
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

        playing = True
        while playing:
            self.check_energy()
            cur_location = self.player.get_location()
            self.check_event_status()
            print_space_info(cur_location, self.event_status)
            print_player_info(self.player)
            cur_location.set_visited(True)

            # Do stuff with the parser here
            user_command = get_command()
            print("\n") # formatting
            parsed_command = parse_command(user_command)
            command = parsed_command[0]
            if len(parsed_command) >= 2:
                action = parsed_command[1]

            if command == GO:
                direction = action.lower()
                self.player.go_exit(direction, self.event_status)

            elif command == TAKE:
                item_name = action.lower()
                self.player.take(item_name)

            elif command == DROP:
                item_name = action.lower()
                self.player.drop(item_name)

            elif command == TALK:
                character_name = action.lower()
                self.player.talk(character_name, self.event_status)

            elif command == LOOK:
                pass

            elif command == SAVE:
                tmp_save_dir = input("Enter the save name\n> ")
                if tmp_save_dir:
                    save_dir = tmp_save_dir
                else:
                    save_dir = None
                self.save(save_dir)

            elif command == QUIT:
                print("Exiting the game...")
                sys.exit()
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

    def to_json_dict(self):
        json_dict = {}
        json_dict['event_status'] = self.event_status
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
            print("saving space: {}".format(s.get_name()))

        # Exits
        exits_dir = save_dir + "exits/"
        os.makedirs(exits_dir)
        for e in self.exits:
            with open(exits_dir + str(e.get_id()) + ".json", "w") as file_handle:
                exits_dict = e.to_json_dict()
                json.dump(exits_dict, file_handle)

    def load(self):
        pass

# Obviously these will all be completely re-done by the parser, this is 
# just to demonstrate a simple version of the game. This parser only 
# handles input in the form 'go 1', 'talk 2', 'take 1', etc.
def get_command():
    command = input("Command: ")
    return command

def parse_command(command):
    return command.split(" ")

def print_space_info(space, event_index):
    # print("\nSPACE INFO:")
    space.print_details(event_index)

def print_player_info(player):
    print("\nPLAYER INFO:")
    print("Energy: {}".format(player.get_energy()))
    print("Current location: {}".format(player.location.name))
    print("Carrying: {0}/{1}".format(player.get_items_total_weight(), player.get_capacity()))
    print("Items: {}".format(player.get_item_names()))
