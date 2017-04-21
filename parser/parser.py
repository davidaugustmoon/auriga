# utility function to check for enumerable non-string
# cite: http://stackoverflow.com/a/19944281
from collections import Iterable

def enum_check(obj):
    return not isinstance(obj, str) and isinstance(obj, Iterable)


class Parser:
    """A basic natural-language parser for Auriga user input."""

    ## Constants
    ARTICLES = ["a", "an", "the"]

    DIRECTIONS = ["n", "e", "s", "w", "ne", "nw", "se", "sw", "up", "down"]

    ALT_DIR_NAMES = {
            "north":        "n",
            "east":         "e",
            "south":        "s",
            "west":         "w",
            "northeast":    "ne",
            "northwest":    "nw",
            "southeast":    "se",
            "southwest":    "sw",
            "above":        "up",
            "below":        "down"
            }

    # create list of room names (possibly from Space or Map file)
    #LOCATIONS = Game.get_room_names()
    LOCATIONS = ["cleanroom", "hangar", "lab", "storehouse"]

    ALT_LOC_NAMES = {
            "clean room": "cleanroom",
            "computer lab": "lab"
            }

    ITEMS = ["ssd1", "ssd2", "ssd3", "yo-yo", "zip tie", "ac adapter",
            "badge", "dongle1", "dongle2", "macbook pro"]

    ALT_ITEM_NAMES = {
            "small ssd":                "ssd1",
            "small ssd drive":          "ssd1",
            "small hard drive":         "ssd1",
            "small drive":              "ssd1",
            "medium ssd":               "ssd2",
            "medium ssd drive":         "ssd2",
            "medium hard drive":        "ssd2",
            "medium drive":             "ssd2",
            "engineer badge":           "badge",
            "employee badge":           "badge",
            "pin badge":                "badge",
            "pin":                      "badge",
            "ethernet cord":            "ethernet",
            "ethernet cable":           "ethernet",
            "mbp":                      "macbook pro"
            }

    CHARACTERS = ["stuffed robot bear", "collapsed robot", "pr2",
            "kelt2a", "wasp12", "jim"]

    ALT_CHAR_NAMES = {
            "robobear":                 "stuffed robot bear",
            "robo-bear":                "stuffed robot bear"
            }

    # verbs and corresponding methods
#    ACTIONS = {
#            # drop
#            "drop":     Player.drop,
#            "deposit":  Player.drop,
#            "leave":    Player.drop,
#            "place":    Player.drop,
#            "put":      Player.drop,
#            "set":      Player.drop, # down
#            "throw":    Player.drop,
#            
#            # move
#            "go":       Player.move,
#
#            # listen
#            "listen":   Player.listen,
#            "hear":     Player.listen,
#            
#            # look
#            "look":     Player.look,
#            "check":    Player.look,
#            "inspect":  Player.look,
#            "view":     Player.look,
#
#            # adjust
#            "adjust":   Player.adjust,
#            "loosten":  Player.adjust,
#            "tighten":  Player.adjust,
#
#            # quit
#            "quit":     Game.quit,
#            "bye":      Game.quit,
#            "exit":     Game.quit,
#
#            # save
#            "save":     Game.save,
#
#            # take
#            "take":     Player.take,
#            "clutch":   Player.take,
#            "gather":   Player.take,
#            "grab":     Player.take,
#            "pick":     Player.take, # up
#            "pilfer":   Player.take,
#            "steal":    Player.take,
#
#            # talk
#            "talk":     Player.talk,
#            "say":      Player.talk,
#            "speak":    Player.talk,
#            "tell":     Player.talk,
#
#            # wait
#            "wait":     Game.wait,
#            "chill":    Game.wait,
#            "nap":      Game.wait,
#            "pause":    Game.wait,
#            "relax":    Game.wait,
#            "rest":     Game.wait,
#            "sleep":    Game.wait
#            }

    PREPOSITIONS = ["about", "above", "across", "after", "against",
            "along", "among", "around", "at", "before", "behind",
            "below", "beneath", "beside", "between", "by", "down",
            "during", "except", "for", "from", "front", "in", "inside",
            "instead", "into", "like", "near", "of", "off", "on",
            "onto", "out", "outside", "over", "past", "since", "through",
            "to", "top", "toward", "under", "underneath", "until", "up",
            "upon", "with", "within", "without"]

    def __init__(self):
        print("Creating new Parser")

    def create_multiword_list(string):
        return string.split()

    def parse_command(string):
        return Parser.create_multiword_list(string)

    def remove_articles(input_list):
        return [word for word in input_list 
                if word not in Parser.ARTICLES]

    def get_verb(input_list):
        action = input_list[0]
        verb_func = None

        if action in Parser.ACTIONS:
            #verb_func = Parser.ACTIONS[action]
            del input_list[0]

        return verb_func

    def get_prepositions(input_list):
        return [word for word in input_list
                if word in Parser.PREPOSITIONS]

    def get_identity(input_list, core_list, alt_list):
        if core_list is None or not enum_check(core_list):
            # throw error
            return

        for elmt in core_list:
            if elmt in input_list:
                elmt_mw = Parser.create_multiword_list(elmt)
                for i in range(len(input_list)):
                    if elmt_mw == input_list[i:i + len(elmt_mw)]:
                        return elmt

        if enum_check(alt_list):
            for elmt in alt_list:
                alt_name = Parser.create_multiword_list(elmt)
                for i in range(len(input_list)):
                    if alt_name == input_list[i:i + len(alt_name)]:
                        return alt_list[elmt]

        return None


    def get_location(input_list):
        return get_identity(input_list, Parser.LOCATIONS,
                Parser.ALT_LOC_NAMES)

    def get_item(input_list):
        return get_identity(input_list, Parser.ITEMS,
                Parser.ALT_ITEM_NAMES)

    def get_character(input_list):
        return get_identity(input_list, Parser.CHARACTERS,
                Parser.ALT_CHAR_NAMES)

    def get_direction(input_list):
        NON_DIR_PREPS = list((set(Parser.PREPOSITIONS) - 
                set(Parser.DIRECTIONS)) - set(Parser.ALT_DIR_NAMES))

        # strip out all unambiguous prepositions
        input_list = [word for word in input_list 
                if word not in NON_DIR_PREPS]

        direction = input_list[0]

        if ((direction not in Parser.DIRECTIONS) and
           (direction not in Parser.ALT_DIR_NAMES)):
            return None

        if direction in Parser.ALT_DIR_NAMES:
            return ALT_DIR_NAMES[direction]
        
        return direction


    ## this method will be part of another class but for now
    ## it will encapsulate the basic strategy for parsing out
    ## and running a command input by the user.
    def run_action(player, cmd_str):

        if cmd_str is None:
            return

        cmd_list = Parser.parse_command(cmd_str.lower())

        # check whether first word is a verb
        # get the verb's corresponding method
        verb = Parser.get_verb(cmd_list)

        # remove all articles
        cmd_list = Parser.remove_articles(cmd_list)
        
        # if it is a verb, check whether it is a MOVE verb
        if verb is None or verb is Player.move:
            verb = Player.move

            # ignore any prepositions, only look for locations or directions

            # if it is not a verb, check whether it is a location
            location_string = Parser.get_location_string(cmd_list)

            # if it is not a verb, check whether it is a direction
            direction_string = Parser.get_direction_string(cmd_list)

            # apply the MOVE action
            if location_string is not None and direction_string is None:
                verb(player, location, "location")
                return

            elif direction_string is not None and location_string is None:
                verb(player, direction, "direction")
                return

            # MOVE command ambiguous or poorly defined

        # if it is not a verb, location, or direction, return
        if verb is None:
            # print error message stating could not understand
            # user instructions
            return


        # check the following strings for params to the verb method

        # first check for an object - this would be a direct object
        # determine the object from possible synonyms
        item = get_item(cmd_list)
        character = None

        if item is None:
            character = get_character(cmd_list)

        # check for any prepositions
        # store these in a list
        # if none, then apply the action if valid and return
        preps = get_prepositions(cmd_list)

        if character is None:
            verb(player)
            return

        if item is None:
            verb(player, character)
            return

        # check for an object - this would be an indirect object
        # determine the object from possible synonyms
        character = get_character(cmd_list)
        
        if character is not None:
            verb(player, item, character)
            return

        # something went wrong, so return an error
        return

## TEST CODE

# test_loc = "clean room"
# test_command = "go clean room"
# test_command2 = "go to the clean room"
# location = None

# print("\nCommand: ", test_loc)
# command_parsed = Parser.parse_command(test_loc)
# location = Parser.get_location_string(command_parsed)
# if location is None:
#     print("No location specified")
# else:
#     print("Location: ", location)

# print("\nCommand: ", test_command)
# command_parsed = Parser.parse_command(test_command)
# location = Parser.get_location_string(command_parsed)
# if location is None:
#     print("No location specified")
# else:
#     print("Location: ", location)

# print("\nCommand: ", test_command2)
# command_parsed = Parser.parse_command(test_command2)
# location = Parser.get_location_string(command_parsed)
# if location is None:
#     print("No location specified")
# else:
#     print("Location: ", location)

# in_list = ["a", "happy", "child", "in", "the", "rain"]
# in_list = Parser.remove_articles(in_list);
# print(in_list)
