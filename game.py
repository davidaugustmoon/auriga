#!/usr/bin/env python

from maze import Maze
from space import Space
from item import Item
from character import Character
from player import Player
from exit import Exit

commands = ["go", "take", "talk"]

class Game(object):

    def __init__(self, player, maze):
        self.player = player
        self.maze = maze
        self.event_status = 0 # increments for player achievments

    def start(self):
        self.player.location.print_long_description()
        self.player.location.visited = True
        playing = True
        while playing:
            cur_location = self.player.location
            print_player_info(self.player)
            print
            print_space_info(cur_location)
            print

            user_command = get_command()
            parsed_command = parse_command(user_command)
            command = parsed_command[0]
            action = int(parsed_command[1])

            # Go
            if command == commands[0]:
                exit = cur_location.exits[action - 1]
                if not exit.locked:
                    new_space = exit.space
                    go_space(self.player, new_space)
                else:
                    if exit.unlock_item in self.player.items:
                        new_space = exit.space
                        go_space(self.player, new_space)
                    else:
                        print("It's locked!")

            # Take
            elif command == commands[1]:
                item_to_take = cur_location.items[action - 1]
                take(self.player, cur_location, item_to_take)
            # Talk
            elif command == commands[2]:
                character = cur_location.characters[action - 1]
                talk(self.event_status, character)

# Obviously these will all be completely re-done by the parser, this is 
# just to demonstrate a simple version of the game. This parser only 
# handles input in the form 'go 1', 'talk 2', 'take 1', etc.
def get_command():
    command = raw_input("Command: ")
    return command

def parse_command(command):
    return command.split(" ")

def go_space(player, space):
    player.location = space
    if space.visited:
        space.print_short_description()
    else:
        space.print_long_description()
    space.visited = True

def take(player, location, item):
    player.take_item(item)
    location.items.remove(item)

def talk(index, character):
    character.print_response(index)

def print_space_info(space):
    print("\nSPACE INFO:")
    space.print_short_description()
    space.print_details()

def print_player_info(player):
    print("\nPLAYER INFO:")
    print("Current location: {}".format(player.location.name))
    print("Capacity: {}".format(player.capacity))
    player.print_items()