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

    # create list of room name synonyms
    # might actually want to have a 2D list, or else a dictionary
    SYNONYMS = { }

    # verbs and corresponding methods
    ACTIONS = {
            # drop
            "drop":     Player.drop,
            "deposit":  Player.drop,
            "leave":    Player.drop,
            "place":    Player.drop,
            "put":      Player.drop,
            "set":      Player.drop, # down
            "throw":    Player.drop,
            
            # move
            "go":       Player.move,

            # listen
            "listen":   Player.listen,
            "hear":     Player.listen,
            
            # look
            "look":     Player.look,
            "check":    Player.look,
            "inspect":  Player.look,
            "view":     Player.look,

            # adjust
            "adjust":   Player.adjust,
            "loosten":  Player.adjust,
            "tighten":  Player.adjust,

            # quit
            "quit":     Game.quit,
            "bye":      Game.quit,
            "exit":     Game.quit,

            # save
            "save":     Game.save,

            # take
            "take":     Player.take,
            "clutch":   Player.take,
            "gather":   Player.take,
            "grab":     Player.take,
            "pick":     Player.take, # up
            "pilfer":   Player.take,
            "steal":    Player.take,

            # talk
            "talk":     Player.talk,
            "say":      Player.talk,
            "speak":    Player.talk,
            "tell":     Player.talk,

            # wait
            "wait":     Game.wait,
            "chill":    Game.wait,
            "nap":      Game.wait,
            "pause":    Game.wait,
            "relax":    Game.wait,
            "rest":     Game.wait,
            "sleep":    Game.wait
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
        print("Creating new Parser")

    def test():
        print("Haiyah!")


FUNC_DICT = {
        "about": Parser.test,
        "below": None
        }

next_func = None

if "about" in FUNC_DICT:
    next_func = FUNC_DICT["about"]

if next_func is not None:
    next_func()

print(list(set(Parser.DIRECTIONS) - set(Parser.PREPOSITIONS)))
