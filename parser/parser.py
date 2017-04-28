# utility function to check for enumerable non-string
# cite: http://stackoverflow.com/a/19944281
from collections import Iterable

def enum_check(obj):
    return not isinstance(obj, str) and isinstance(obj, Iterable)


class Parser:
    """A basic natural-language parser for Auriga user input."""

    ### CONSTANTS ###

    # words to completely ignore
    ARTICLES = ["a", "an", "the"]

    # these six directions represent the location of a possible space exit
    # classes using the Parser will need to verify that there is a valid
    # exit in the direction specified inside the current room
    DIRECTIONS = ["north", "east", "south", "west", "up", "down"]

    ALT_DIR_NAMES = {
            "n":        "north",
            "e":        "east",
            "s":        "south",
            "w":        "west",
            "above":    "up",
            "below":    "down"
            }

    # these canonical names actually represent types of exits
    # classes using the Parser will need to verify that there is a valid
    # exit of the type specified inside the current room
    EXITS = ["sliding door", "saloon doors", "air duct", "stairway", "hallway"]

    ALT_EXIT_NAMES = {
            # SLIDING DOOR
            "slide door":           "sliding door",

            # SALOON DOORS
            "saloon":               "saloon doors",
            "saloon door":          "saloon doors",
            "swinging door":        "saloon doors",
            "swinging doors":       "saloon doors",

            # AIR DUCT
            "airway":               "air duct",
            "duct":                 "air duct",
            "airduct":              "air duct",
            "vent":                 "air duct",
            "air vent":             "air duct",
            "air duct tunnel":      "air duct",
            "airduct tunnel":       "air duct",
            "tunnel":               "air duct",
            "air tunnel":           "air duct",

            # STAIRWAY
            "stairs":               "stairway",
            "staircase":            "stairway",
            "stair case":           "stairway",
            "stair way":            "stairway",
            "stairwell":            "stairway",
            "stair well":           "stairway",

            # HALLWAY
            "hall way":             "hallway",
            "hall":                 "hallway"
            }

    ITEMS = ["security badge", "usb drive", "ssd", "small bucket", "large bucket",
            "button", "screwdriver", "camera", "ac adapter", "usb cord"]

    ALT_ITEM_NAMES = {
            # SECURITY BADGE
            "badge":                    "security badge"
            "engineer badge":           "security badge",
            "employee badge":           "security badge",
            "pin badge":                "security badge",
            "pin":                      "security badge",
            "keycard":                  "security badge",

            # USB DRIVE
            "external":                 "usb drive",
            "external drive":           "usb drive",
            "external hard drive":      "usb drive",
            "flash drive":              "usb drive",
            "flashdrive":               "usb drive",
            "thumb drive":              "usb drive",
            "thumbdrive":               "usb drive",

            # SOLID STATE DRIVE
            "solid state drive":        "ssd",
            "solid state":              "ssd",
            "ss drive":                 "ssd",
            "hard drive":               "ssd",
            "drive":                    "ssd",
            "hard disk":                "ssd",
            "ss disk":                  "ssd",
            "solid state disk":         "ssd",

            # SMALL BUCKET
            "small backpack":           "small bucket",
            "small pail":               "small bucket",
            "tiny bucket":              "small bucket",
            
            # LARGE BUCKET
            "large backpack":           "large bucket",
            "large pail":               "large bucket",
            "big bucket":               "large bucket",

            # BUTTON
            "switch":                   "button",
            "wall button":              "button",
            "wall switch":              "button",
            "wall panel":               "button",
            "panel":                    "button",
            
            # SCREWDRIVER
            "tool":                     "screwdriver",
            
            # CAMERA
            "cam":                      "camera",
            "video camera":             "camera",
            "videocam":                 "camera",
            "cctv":                     "camera",
            "surveillance camera":      "camera",
            
            # AC ADAPTER
            "power adapter":            "ac adapter",
            "adapter":                  "ac adapter",
            "adaptor":                  "ac adapter",
            
            # USB CORD
            "cord":                     "usb cord",
            "charge cord":              "usb cord",
            "charge cable":             "usb cord",
            "charging cord":            "usb cord",
            "charging cable":           "usb cord",
            "cable":                    "usb cord",
            "usb cable":                "usb cord",
            "power cord":               "usb cord",
            "power cable":              "usb cord",
            "adapter cord":             "usb cord",
            "adapter cable":            "usb cord"
            }

    CHARACTERS = ["stuffed robot bear", "collapsed robot", "pr2",
            "kelt2a", "wasp12", "jim", "freight500", "fetch71"]

    ALT_CHAR_NAMES = {
            # STUFFED ROBOT BEAR
            "robobear":                 "stuffed robot bear",
            "robo-bear":                "stuffed robot bear",

            # COLLAPSED ROBOT
            "trashed robot":            "collapsed robot"

            # PR2


            # KELT-2A


            # WASP-12


            # JIM


            # FREIGHT-500



            # FETCH-71
            }

    # verbs and corresponding methods
    ACTIONS = {
            ## ACTION FUNCTIONS ##

            # DROP
            "drop":         "drop",
            "deposit":      "drop",
            "leave":        "drop",
            "place":        "drop",
            "put":          "drop",
            "set":          "drop",
            "throw":        "drop",
            
            # GO
            "go":           "go",
            "move":         "go",
            "walk":         "go",
            "enter":        "go",
            "leave":        "go",

            # LISTEN
            "listen":       "listen",
            "hear":         "listen",
            "ears":         "listen",
            
            # LOOK (AROUND)
            "look":         "look",         # preposition could change this
            "view":         "look",

            # LOOK AT
            "check":        "look at",
            "inspect":      "look at",

            # PULL
            "pull":         "pull",
            "tug":          "pull",
            "yank":         "pull",

            # PUSH
            "push":         "push",
            "press":        "push",
            "lean":         "push",

            # RECHARGE
            "recharge":     "recharge",
            "power":        "recharge",
            "plug":         "recharge",
            "boost":        "recharge",
            "reboost":      "recharge",
            "restore":      "recharge",
            "battery":      "recharge",
            "energize":     "recharge",
            "reenergize":   "recharge",
            "re-energize":  "recharge",
            "charge":       "charge",

            # TAKE
            "take":         "take",
            "clutch":       "take",
            "gather":       "take",
            "grab":         "take",
            "pick":         "take",
            "pilfer":       "take",
            "steal":        "take",

            # TALK
            "talk":         "talk",
            "say":          "talk",
            "speak":        "talk",
            "tell":         "talk",

            # WAIT
            "wait":         "wait",
            "chill":        "wait",
            "nap":          "wait",
            "pause":        "wait",
            "relax":        "wait",
            "rest":         "wait",
            "sleep":        "wait",


            ## UTILITY FUNCTIONS ##

            # HELP
            "help":         "help",
            "h":            "help",
            "?":            "help",

            # INVENTORY
            "inventory":    "inventory",
            "list":         "inventory",

            #LOADGAME
            "loadgame":     "loadgame",
            "load":         "loadgame",

            # SAVEGAME
            "savegame":     "savegame",
            "save":         "savegame",

            # QUIT
            "quit":         "quit",
            "bye":          "quit",
            "exit":         "quit"
            }

    PREPOSITIONS = ["about", "above", "across", "after", "against",
            "along", "among", "around", "at", "before", "behind",
            "below", "beneath", "beside", "between", "by", "down",
            "during", "except", "for", "from", "front", "in", "inside",
            "instead", "into", "like", "near", "of", "off", "on",
            "onto", "out", "outside", "over", "past", "since", "through",
            "to", "top", "toward", "under", "underneath", "until", "up",
            "upon", "with", "within", "without"]

    def __init__(self):
        pass

    def create_multiword_list(string):
        return string.split()

    def parse_command(string):
        return Parser.create_multiword_list(string)

    def remove_articles(input_list):
        return [word for word in input_list 
                if word not in Parser.ARTICLES]

    def get_verb(input_list):
        action = input_list[0]
        verb = None

        if action in Parser.ACTIONS:
            verb = Parser.ACTIONS[action]
            del input_list[0]

        return verb

    def get_prepositions(input_list):
        return [word for word in input_list
                if word in Parser.PREPOSITIONS]

    def get_identity(input_list, core_list, alt_list):
        if core_list is None or not enum_check(core_list):
            # throw error
            return None

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


    def get_exit_type(input_list):
        return get_identity(input_list, Parser.EXITS,
                Parser.ALT_EXIT_NAMES)

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

    
    ## prototype of method to return disambiguated request parsed
    ## from user input in the form of a five-tuple:
    ## (action, location, direction, item, character)
    ##
    ## action =     command name or actual method pointer, None if invalid
    ## exit =       identity name of exit type to use, or None
    ## direction =  cardinal direction name specifying location of exit, or None
    ## item =       identity name of item action applied to, or None
    ## character =  identity name of character action applied to, or None
    ##
    ## this method will use the logic of the run_action() method defined below
    def action_requested(cmd_str):
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
            if exit is not None and direction is None:
                return (action, exit, None, None, None)

            # MOVE through an exit in a particular direction
            if direction is not None and exit is None:
                return (action, None, direction, None, None)

            # MOVE command ambiguous or poorly defined
            return (None, None, None, None, None)

        # check the following strings for params to the verb method
        item = get_item(cmd_list)
        character = get_character(cmd_list)

        # TODO: find more verbs that need prep to distinguish desired action
        preps = get_prepositions(cmd_list)
        
        if action == "look" and "at" in preps and "around" not in preps:
            action == "inspect"

        return (action, None, None, item, character)
