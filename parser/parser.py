#!/usr/bin/env python3

# utility function to check for enumerable non-string
# cite: http://stackoverflow.com/a/19944281
from collections import Iterable
import json
import os

def enum_check(obj):
    """
    Verifies that _obj_ is an iterable object but not a string.
    """
    return not isinstance(obj, str) and isinstance(obj, Iterable)


class Parser:
    """
    A basic natural-language command parser for Auriga user input.
    """

    ### LITERALS ###

    literals_dir = os.getcwd() + '/parser/literals/'

    # words to completely ignore
    with open(literals_dir + 'articles.json', 'r') as a:
        ARTICLES = json.load(a)

    # these six directions represent the location of a possible space exit
    with open(literals_dir + 'directions.json', 'r') as d:
        DIRECTIONS = json.load(d)
    with open(literals_dir + 'directions_alt.json', 'r') as d:
        ALT_DIR_NAMES = json.load(d)

    # these canonical names actually represent types of exits
    with open(literals_dir + 'exits.json', 'r') as e:
        EXITS = json.load(e)

    with open(literals_dir + 'exits_alt.json', 'r') as e:
        ALT_EXIT_NAMES = json.load(e)

    with open(literals_dir + 'items.json', 'r') as i:
        ITEMS = json.load(i)

    with open(literals_dir + 'items_alt.json', 'r') as i:
        ALT_ITEM_NAMES = json.load(i)

    with open(literals_dir + 'characters.json', 'r') as c:
        CHARACTERS = json.load(c)

    with open(literals_dir + 'characters_alt.json', 'r') as c:
        ALT_CHAR_NAMES = json.load(c)

    # commands
    with open(literals_dir + 'actions.json', 'r') as a:
        ACTIONS = json.load(a)

    with open(literals_dir + 'prepositions.json', 'r') as p:
        PREPOSITIONS = json.load(p)


    def create_multiword_list(string):
        """
        Split space-separated string into tokens.
        
        :param str - string: raw string, possibly containing whitespace

        :return list: string tokens after separating at whitespace
        """
        return string.split()


    def parse_command(string):
        """
        Wrapper for create_multiword_list().

        :param str - string: command to parse

        :return list: elements of command
        """
        return Parser.create_multiword_list(string)


    def remove_articles(input_list):
        """
        Returns list of strings after removing all occurrences of "a", "an", and "the".

        :param list - input_list: list of strings

        :return list: list of strings after removing articles
        """
        return [word for word in input_list 
                if word not in Parser.ARTICLES]


    def get_verb(input_list):
        """
        Returns the canonical name for an action either the Player or Game can execute,
        unless the list does not contain a valid synonym for any action.

        :param list - input_list: list of strings

        :return str: the canonical name for an action, or None
        """
        if len(input_list) == 0:
            return None

        action = input_list[0]
        verb = None

        if action in Parser.ACTIONS:
            verb = Parser.ACTIONS[action]
            del input_list[0]

        return verb


    def get_prepositions(input_list):
        """
        Returns a list containing every preposition found in the input string list.

        :param list - input_list: list of strings

        :return list: a list of all strings determined to be prepositions
        """
        return [word for word in input_list
                if word in Parser.PREPOSITIONS]


    def get_identity(input_list, core_list, alt_list):
        """
        Searches through all elements of core_list and keys of alt_list for
        a single word in input_list.  The first name found in input_list that
        matches an element of core_list is returned.  If none is found, the
        first name found in input_list that matches a key of alt_list causes
        this method to return that key's value.  If still no matching word
        is found, returns None.

        Note: Only depend on this method when you can accept whichever match
        is discovered initially.  Do not depend on the order in which strings
        appear in their corresponding lists.

        Citation: http://stackoverflow.com/a/2587419 for creating a new
            sorted list based on string length.

        :param list - input_list: list containing strings to search for in
               other parameters
        :param list - core_list: list with canonical names only
        :param list - alt_list: dictionary with synonym names as keys mapped
               to canonical names as values

        :return str: the matching/corresponding canonical name if found,
               otherwise none
        """
        if core_list is None or not enum_check(core_list):
            # throw error
            return None

        # see if any canonical names are in input_list, looking
        # at longer names first
        for elmt in sorted(core_list, key=len, reverse=True):
            #if elmt in input_list:
            # turn multi-word name into ordered word list
            elmt_mw = Parser.create_multiword_list(elmt.lower())

            for i in range(len(input_list)):
                if elmt_mw == input_list[i:i + len(elmt_mw)]:
                    # return matched name
                    return elmt

        # see if any synonym names are in input_list, looking
        # at longer names first
        if enum_check(alt_list):

            for elmt in sorted(alt_list, key=len, reverse=True):
                # turn multi-word key into ordered word list
                alt_name = Parser.create_multiword_list(elmt.lower())

                for i in range(len(input_list)):
                    if alt_name == input_list[i:i + len(alt_name)]:
                        # return canonical name for matched synonym
                        return alt_list[elmt]

        # no match found
        return None


    def get_exit_type(input_list):
        """
        Searches for an Exit name or synonym in a list and returns the canonical Exit type
        for the first match.  If no match, returns None.

        Note: if multiple Exit names/synonyms are in input_list, the result is indeterminate.

        :param list - input_list: parsed list of strings from command

        :return str: type of Exit, or None.
        """
        return Parser.get_identity(input_list, Parser.EXITS,
                Parser.ALT_EXIT_NAMES)


    def get_item(input_list):
        """
        Searches for an Item name or synonym in a list and returns the canonical Item name
        for the first match.  If no match, returns None.

        Note: if multiple Item names/synonyms are in input_list, the result is indeterminate.

        :param list - input_list: parsed list of strings from command

        :return str: canonical name of matched Item, or None.
        """
        return Parser.get_identity(input_list, Parser.ITEMS,
                Parser.ALT_ITEM_NAMES)


    def get_character(input_list):
        """
        Searches for a Character name or synonym in a list and returns the canonical Character
        name for the first match.  If no match, returns None.

        Note: if multiple Character names/synonyms are in input_list, the result is indeterminate.

        :param list - input_list: parsed list of strings from command

        :return str: canonical name of matched Character, or None.
        """
        return Parser.get_identity(input_list, Parser.CHARACTERS,
                Parser.ALT_CHAR_NAMES)


    def get_direction(input_list):
        """
        Searches for a direction or shorthand for one in a list and returns the canonical
        direction name for the first match.  If no match, returns None.

        A direction refers to the location of an Exit in a Space that leads to an adjacent
        Space.  The direction to reach a room's Exit may not be the opposite of the
        direction to reach the Exit's other end in an adjacent room, however.

        Note: if multiple direction names/synonyms are in input_list, the result is
        indeterminate.

        :param list - input_list: parsed list of strings from command

        :return str: canonical name of matched direction, or None.
        """
        NON_DIR_PREPS = list((set(Parser.PREPOSITIONS) - 
                set(Parser.DIRECTIONS)) - set(Parser.ALT_DIR_NAMES))

        # strip out all unambiguous prepositions
        input_list = [word for word in input_list 
                if word not in NON_DIR_PREPS]

        # deals with commands like "under"
        if len(input_list) == 0:
            return None

        direction = input_list[0]

        if ((direction not in Parser.DIRECTIONS) and
           (direction not in Parser.ALT_DIR_NAMES)):
            return None

        if direction in Parser.ALT_DIR_NAMES:
            return Parser.ALT_DIR_NAMES[direction]
        
        return direction

    

    def action_requested(cmd_str):
        '''
        Return disambiguated command request parsed from user input in the form of 
        a five-tuple: (action, location, direction, item, character)
        
        action =     command name or actual method pointer, None if invalid
        exit =       identity name of exit type to use, or None
        direction =  cardinal direction name specifying location of exit, or None
        item =       identity name of item action applied to, or None
        character =  identity name of character action applied to, or None
        '''

        if cmd_str is None:
            return (None, None, None, None, None)

        cmd_list = Parser.parse_command(cmd_str.lower())

        # check whether first word is a verb
        # get the verb's corresponding method
        action = Parser.get_verb(cmd_list)

        # remove all articles
        cmd_list = Parser.remove_articles(cmd_list)
        
        # if it is a verb, check whether it is a MOVE verb
        if action is None or action == "go":
            action = "go"

            # ignore any prepositions, only look for locations or directions

            # if it is not a verb, check whether it is a location
            exit = Parser.get_exit_type(cmd_list)

            # if it is not a verb, check whether it is a direction
            direction = Parser.get_direction(cmd_list)

            # MOVE to a specific space
            if exit and direction is None:
                return (action, exit, None, None, None)

            # MOVE through an exit in a particular direction
            if direction and exit is None:
                return (action, None, direction, None, None)

            # MOVE command ambiguous or poorly defined
            return (None, None, None, None, None)

        # check the following strings for params to the verb method
        item = Parser.get_item(cmd_list)
        character = Parser.get_character(cmd_list)

        # TODO: find more verbs that need prep to distinguish desired action
        preps = Parser.get_prepositions(cmd_list)
        
        # manually disambiguate certain verbs and automate detection for rest
        if action == "look" and "at" in preps:
            if "around" not in preps:
                action = "look at"
            else:
                action = None

        return (action, None, None, item, character)


def main():
    while True:
        print()
        cmd = input("What do you want to do? (q to quit)\n")

        if cmd == 'q':
            break

        print()

        action, exit, direction, item, character = Parser.action_requested(cmd)

        if action: 
            print("Action: {0}".format(action))
            
            if exit:
                print("Exit: {0}".format(exit))

            if direction:
                print("Direction: {0}".format(direction))
            
            if item:
                print("Item: {0}".format(item))

            if character:
                print("Character: {0}".format(character))

        else:
            print("ERROR: Invalid command")

if __name__ == "__main__":
    main()