#!/usr/bin/env python

import sys

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
        self.event_status = 0 # increments for player achievments

    def start(self):
        self.player.get_location().print_long_description(self.event_status)
        self.player.get_location().set_visited(True)
        p = Parser()

        # Do stuff with the parser now
        playing = True
        while playing:
            self.check_energy()
            cur_location = self.player.get_location()
            self.check_event_status()
            print_player_info(self.player)
            print_space_info(cur_location)

            user_command = get_command()
            parsed_command = parse_command(user_command)
            command = parsed_command[0]
            if len(parsed_command) >= 2:
                action = int(parsed_command[1])

            if command == GO:
                exit = cur_location.exits[action - 1]
                self.player.go_exit(exit, self.event_status)

            elif command == TAKE:
                item_to_take = cur_location.items[action - 1]
                self.player.take(item_to_take)

            elif command == DROP:
                item_to_drop = self.player.get_items()[action - 1]
                self.player.drop(item_to_drop)

            elif command == TALK:
                character = cur_location.characters[action - 1]
                self.player.talk(character, self.event_status)

            elif command == LOOK:
                pass

            elif command == SAVE:
                pass

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

    def increment_event_status(self):
        self.event_status += 1

    def check_energy(self):
        if self.player.get_energy() <= 0:
            print("Sorry, you ran out of energy and died.")
            print("Maybe the AI program will bring you back again...")
            sys.exit()

# Obviously these will all be completely re-done by the parser, this is 
# just to demonstrate a simple version of the game. This parser only 
# handles input in the form 'go 1', 'talk 2', 'take 1', etc.
def get_command():
    command = raw_input("Command: ")
    return command

def parse_command(command):
    return command.split(" ")

def print_space_info(space):
    print("\nSPACE INFO:")
    space.print_details()

def print_player_info(player):
    print("\nPLAYER INFO:")
    print("Energy: {}".format(player.get_energy()))
    print("Current location: {}".format(player.location.name))
    print("Carrying: {0}/{1}".format(player.get_items_total_weight(), player.get_capacity()))
    print("Items: {}".format(player.get_item_names()))