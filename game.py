#!/usr/bin/env python

import sys

# from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit

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
                if not exit.locked:
                    new_space = exit.space
                    self.go_space(self.player, new_space, self.event_status)
                else:
                    if exit.unlock_item in self.player.items:
                        new_space = exit.space
                        self.go_space(self.player, new_space, self.event_status)
                    else:
                        print("\nIt's locked!")

            elif command == TAKE:
                item_to_take = cur_location.items[action - 1]
                self.take(item_to_take)

            elif command == DROP:
                item_to_drop = self.player.get_items()[action - 1]
                self.drop(item_to_drop)

            elif command == TALK:
                character = cur_location.characters[action - 1]
                self.talk(self.event_status, character)

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

    def go_space(self, player, space, index):
        cur_energy = self.player.get_energy()
        self.player.set_energy(cur_energy - 3)
        self.player.set_location(space)
        if space.visited:
            space.print_short_description()
        else:
            space.print_long_description(index)
        space.visited = True

    def take(self, item):
        cur_energy = self.player.get_energy()
        self.player.set_energy(cur_energy - 2)
        cur_location = self.player.get_location()
        # Check that the given item is in the player's current location.
        if item in cur_location.get_items():
            # Check that the player can carry that much weight.
            if (self.player.get_items_total_weight() + item.get_weight()) < self.player.get_capacity():
                self.player.add_item(item)
                cur_location.remove_item(item)
                print("{0} took the {1}".format(self.player.get_name(), item.get_name()))
            else:
                print("The {0} is too heavy!".format(item.get_name()))

    def talk(self, index, character):
        cur_energy = self.player.get_energy()
        self.player.set_energy(cur_energy - 1)
        cur_location = self.player.get_location()
        if character in cur_location.get_characters():
            character.print_response(index)
        else:
            print("That person's not here...")

    def drop(self, item_to_drop):
        cur_location = self.player.get_location()
        if item_to_drop in self.player.get_items():
            cur_location.add_item(item_to_drop)
            self.player.remove_item(item_to_drop)
        else:
            print("You can't drop that.")

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