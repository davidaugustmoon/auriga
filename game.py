#!/usr/bin/env python3

import sys
import os
import datetime
import json

# from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit
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
        TODO Still need to save game and player data
        """
        root_dir = os.getcwd()
        cur_datetime = str(datetime.datetime.now()).split(".")[0]  # remove fractional seconds
        if not dir_name:
            dir_name = "game_" + cur_datetime + "/"
        save_dir = root_dir + "/saved_games/" + dir_name + "/"

        # Check if the filepath already exists
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Open the json file and write all of the game objects to it.
        objects_dict = {}
        with open(save_dir + "objects.json", "wb") as file_handle:
            # Game
            objects_dict['game'] = self.to_json_dict()

            # Player
            objects_dict['player'] = self.player.to_json_dict()

            # Items
            items = []
            for i in self.items:
                items.append(i.to_json_dict())
            objects_dict['items'] = items

            # Characters
            characters = []
            for c in self.characters:
                characters.append(c.to_json_dict())
            objects_dict['characters'] = characters

            # Spaces
            spaces = []
            for s in self.spaces:
                spaces.append(s.to_json_dict())
            objects_dict['spaces'] = spaces

            # Exits
            exits = []
            for e in self.exits:
                exits.append(e.to_json_dict())
            objects_dict['exits'] = exits

            json.dump(objects_dict, file_handle)

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
