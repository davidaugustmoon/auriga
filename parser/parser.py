class Parser:
    """A basic natural-language parser for Auriga user input."""

    ## Constants
    ARTICLES = ["a", "an", "the"]

    DIRECTIONS = ["north", "east", "south", "west", 
            "northeast", "northwest", "southeast", "southwest",
            "n", "e", "s", "w", "ne", "nw", "se", "sw",
            "up", "down", "above", "below"]

    # create list of room names
    #LOCATIONS = Game.get_room_names()
    LOCATIONS = ["cleanroom", "hangar", "lab", "storehouse"]

    ALT_LOC_NAMES = {
            "clean room": "cleanroom",
            "computer lab": "lab"
            }

    # create list of room name synonyms
    # might actually want to have a 2D list, or else a dictionary
    SYNONYMS = { }

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

    # for testing functions as variable values
    def test():
        print("Haiyah!")

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

    def get_location_string(input_list):
        for loc in Parser.LOCATIONS:
            if loc in input_list:
                return loc

        for loc in Parser.ALT_LOC_NAMES:
            alt_loc_name = Parser.create_multiword_list(loc)
            for i in range(len(input_list)):
                if alt_loc_name == input_list[i:i+len(alt_loc_name)]:
                    return Parser.ALT_LOC_NAMES[loc]

        return None

    def get_direction_string(input_list):
        NON_DIR_PREPS = list(set(Parser.PREPOSITIONS) - 
                set(Parser.DIRECTIONS))

        # strip out all unambiguous prepositions
        input_list = [word for word in input_list 
                if word not in NON_DIR_PREPS]

        direction = input_list[0]

        if direction not in Parser.DIRECTIONS:
            return None
        else
            return direction


    ## this method will be part of another class but for now
    ## it will encapsulate the basic strategy for parsing out
    ## and running a command input by the user.
    def run_action(cmd_str):
        if cmd_str is None:
            return

        cmd_list = Parser.parse_command(cmd_str.lower())

        # check whether first word is a verb
        verb = Parser.get_verb(cmd_list)

        # remove all articles
        cmd_list = Parser.remove_articles(cmd_list)
        
        # if it is a verb, check whether it is a MOVE verb
        if verb is None or verb is Player.move:

        # if it is not a verb, check whether it is a location
            location_string = Parser.get_location_string(cmd_list)

        # if it is not a verb, check whether it is a direction
            direction_string = Parser.get_direction_string(cmd_list)

            # apply the MOVE action
            if location_string is not None and direction_string is None:
                verb(location, "location")
            elif direction_string is not None and location_string is None:
                verb(direction, "direction")

            # MOVE command ambiguous or poorly defined
            # print error and do nothing
            else
                # print error message stating could not understand
                # user instructions
                return

            # ignore any prepositions, only look for locations or directions

            # if the direction is invalid or location is hidden,
            # locked, or not adjacent, print error message for player

            # otherwise move player to new location and start next
            # turn

        # if it is not a verb, location, or direction, return

        # get the verb's corresponding method

        # check the following strings for params to the verb method

        # first check for an object - this would be a direct object
        # determine the object from possible synonyms

        # check for any prepositions
        # store these in a list
        # if none, then apply the action if valid and return

        # check for an object - this would be an indirect object
        # determine the object from possible synonyms

        # apply the action if valid and return

# just testing some Python features
FUNC_DICT = {
        "about": Parser.test,
        "below": None
        }

next_func = None

if "about" in FUNC_DICT:
    next_func = FUNC_DICT["about"]

if next_func is not None:
    next_func()

test_loc = "clean room"
test_command = "go clean room"
test_command2 = "go to the clean room"
location = None

print("\nCommand: ", test_loc)
command_parsed = Parser.parse_command(test_loc)
location = Parser.get_location_string(command_parsed)
if location is None:
    print("No location specified")
else:
    print("Location: ", location)

print("\nCommand: ", test_command)
command_parsed = Parser.parse_command(test_command)
location = Parser.get_location_string(command_parsed)
if location is None:
    print("No location specified")
else:
    print("Location: ", location)

print("\nCommand: ", test_command2)
command_parsed = Parser.parse_command(test_command2)
location = Parser.get_location_string(command_parsed)
if location is None:
    print("No location specified")
else:
    print("Location: ", location)

in_list = ["a", "happy", "child", "in", "the", "rain"]
in_list = Parser.remove_articles(in_list);

print(in_list)

print(list(set(Parser.DIRECTIONS) - set(Parser.PREPOSITIONS)))
