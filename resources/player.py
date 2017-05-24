#!/usr/bin/env python3

import resources.item
import resources.space

DEFAULT_NAME = "PLAYER 1"
DEFAULT_DESCRIPTION = "This is a player."
DEFAULT_CAPACITY = 50

class Player(object):
    """
    This is a base class for a player. It is intended to be used in a
    text adventure game.
    """
    def __init__(self, name=DEFAULT_NAME, description=DEFAULT_DESCRIPTION, items=None,
                 capacity=DEFAULT_CAPACITY, location=None, alive=True, energy=100):
        """
        :param name - str: The name of this player.
        :param description - str: A description of this player.
        :param capacity - int: The maximum item capacity this player can
               carry.
        :param items - list of Item: A list of Items the player is carrying.
        :param location - Space: The current location of this player.
        :param alive - bool: True --> This player is alive.
               False --> This player is dead.
               Note: This may be used to terminate a game, or change a game
                     state.
        """
        self.name = name
        self.description = description
        self.capacity = capacity
        if items:
            self.items = items
        else:
            self.items = []
        if location:
            self.location = location
        else:
            self.location = location
        self.alive = alive
        self.energy = energy
        self.max_energy = energy

    def get_name(self):
        """
        Get the name of the player

        :return str: The name of the player
        """
        return self.name

    def set_name(self, new_name):
        """
        Set the name of the player
        
        :param str - new_name: The name to assign the player.
        """
        self.name = new_name

    def get_description(self):
        """
        Get the player description

        :return str: A description of the player
        """
        return self.description

    def set_description(self, new_description):
        """
        Set the description of the player

        :param str - new_description: The description to set for the player
        """
        self.description = new_description

    def get_capacity(self):
        """
        Get the player's maximum carrying capacity

        :return int: The maximum weight a player can carry.
        """
        return self.capacity

    def set_capacity(self, new_capacity):
        """
        Set the player's maximum carrying capacity

        :param int - new_capacity: The maximum carrying capacity to set for the player
        """
        self.capacity = new_capacity

    def get_items(self):
        """
        Get the list of items currently carried by the player

        :return list of Item: The list of Item objects currently carried by the player
        """
        return self.items

    def set_items(self, new_items_list):
        """
        Set the list of Item objects currently carried by the player

        :param list of Item - new_item_list: The new list of Item objects carried by the player
        """
        self.items = new_items_list

    def add_item(self, item_to_add):
        """
        Add an Item to the player's currently carried items

        :param Item - item_to_add: The Item to add to the player's currently carried items
        """
        self.items.append(item_to_add)

    def remove_item(self, item_to_remove):
        """
        Remove an Item from the player's currently carried items

        :param Item - item_to_remove: The Item to remove from the player's currently carried items
        """
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)

    def get_item_names(self):
        """
        Get a list of the names of all of the Item objects currently carried by the player

        :return list of str: The list of Item names of all of the objects carried by the player
        """
        return [i.name for i in self.items]

    def get_items_total_weight(self):
        total_weight = 0
        for i in self.items:
            total_weight += i.get_weight()
        return total_weight

    def get_location(self):
        """
        Get the player's current location

        :return Space: The Space the player currently occupies
        """
        return self.location

    def set_location(self, new_location):
        """
        Set the player's current location

        :param Space - new_location: The new Space the player will occupy
        """
        self.location = new_location

    def get_alive(self):
        """
        Get whether the player is currently alive.

        :return Bool: True if the player is alive; False if the player is not alive
        """
        return self.alive

    def set_alive(self, new_alive):
        """
        Set whether the player is alive or not

        :param Bool - new_alive: True will set the player to be alive; False will set
                                 the player to not be alive
        """
        self.alive = new_alive

    def get_energy(self):
        """
        Get a player's current energy level

        :return int: The player's current energy level
        """
        return self.energy

    def set_energy(self, new_energy):
        """
        Set a player's energy level

        :param int - new_energy: The energy level to set for the player
        """
        if new_energy < 0:
            self.energy = 0
        else:
            self.energy = new_energy

    def go_exit(self, event_status, direction=None, exit_name=None):
        exit = None
        possible_exits = []

        print()
        # Get any exits that match the passed direction or exit name
        for e in self.location.get_exits():
            if direction and e.is_visible() and (e.get_direction().lower() == direction.lower()):
                possible_exits.append(e)
            if exit_name and (e.get_name().lower() == exit_name):
                possible_exits.append(e)

        if len(possible_exits) == 1:
            exit = possible_exits[0]
        # Multiple possible exits, check if one matches both name and direction
        elif len(possible_exits) > 1:
            for pe in possible_exits:
                if pe.get_name() == exit_name and pe.get_direction() == direction:
                    exit = pe
            if not exit:
                print("You need to be more specic.")
                return None
        else:
            print("Invalid direction and/or exit name.")
            return None

        if exit:
            # Check if the exit is locked
            if exit.is_locked():
                # Check if the player has the Item to unlock the Exit
                if exit.get_unlock_item() in self.items:
                    self.energy -= 3
                    new_space = exit.get_space()
                    self.location = new_space
                    # new_space.print_details(event_status)
                    # new_space.set_visited(True)
                else:
                    print("Sorry, that exit is locked!")
                    return None
            else:
                self.energy -= 3
                new_space = exit.get_space()
                self.location = new_space
        else:
            print("You can't go {0} here.".format(direction))
            return None

    def take(self, item_name):
        """
        Pick up an item from the player's current location.

        :param Item - item: The Item to take
        """
        print()
        item = None
        for i in self.location.get_items():
            if item_name and (i.get_name().lower() == item_name.lower()):
                item = i
        # Check that the given item is in the player's current location.
        if item:
            # Check that the item is not locked
            if not item.get_locked():
                # Check that the player can carry that much weight.
                if (self.get_items_total_weight() + item.get_weight()) < self.capacity:
                    self.add_item(item)
                    self.location.remove_item(item)
                    print("{0} took the {1}".format(self.name, item.get_name()))
                    self.energy -= 2
                else:
                    print("The {0} is too heavy!".format(item.get_name()))
            else:
                print("You can't pick up the {0}".format(item.get_name()))
        else:
            print("That item is not here.")

    def talk(self, character_name, game_state_index):
        print()
        character = None
        for c in self.location.get_characters():
            if character_name and (c.name.lower() == character_name.lower()):
                character = c
        if character:
            self.energy -= 1
            character.print_response(game_state_index)
        else:
            print("That character is not here.")

    def drop(self, item_name):
        print()
        item = None
        for i in self.items:
            if item_name and (i.name.lower() == item_name.lower()):
                item = i
        if item:
            self.location.add_item(item)
            self.remove_item(item)
            self.energy -= 1
            print("{0} dropped the {1}.".format(self.name, item_name))
        else:
            print("You can't drop that.")

    def look(self, event_status):
        print(self.location.print_long_description(event_status))
        self.energy -= 1

    def look_at(self, item_name):
        item = None
        for i in self.location.get_items():
            if item_name and (i.get_name() == item_name):
                item = i
                break

        if item:
            print("You looked at the {0}".format(item_name))
            print(item.get_description())
            self.energy -= 1
        else:
            print("{0} isn't here...".format(item_name))

    def charge(self):
        is_charger = False
        # Check current location for charger
        for i in self.location.get_items():
            if i.name == "charger":
                is_charger = True
                break

        if is_charger:
            print("Feel the snake bite enter your veins!")
            self.set_energy(self.max_energy)
        else:
            print("Sorry, there is no charger here.\nYou are probably going to die...")

    def listen(self):
        print("You hear nothing...but the rest is good.")
        self.energy += 1

    def print_inventory(self):
        if self.items:
            print("Your Inventory (Item, Weight):")
            for i in self.items:
                print("({0}, {1}) ".format(i.get_name(), i.get_weight()), end="")
            print()
        else:
            print("You're not carrying anything...")
        self.energy -= 1

    def print_details(self):
        """
        Print details about the player
        """
        print("\nName: {}".format(self.name.upper()))
        print("Description: {}".format(self.description))
        print("Carrying: {0}/{1}".format(self.get_items_total_weight(), self.capacity))
        print("Items: {}".format(self.get_item_names()))
        print("location: {}".format(self.location.name))
        print("Is alive: {}".format(self.alive))

    def print_energy(self):
        energy_level = "+" * int(self.energy)
        print("Energy: {}".format(energy_level))

    def to_json_dict(self):
        json_dict = {}
        json_dict['name'] = self.name
        json_dict['description'] = self.description
        json_dict['capacity'] = self.capacity
        json_dict['items'] = [i.get_id() for i in self.items]
        json_dict['location'] = self.location.get_id()
        json_dict['alive'] = self.alive
        json_dict['energy'] = self.energy
        return json_dict
