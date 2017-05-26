#!/usr/bin/env python3

import unittest
from parser import Parser

class TestParser(unittest.TestCase):

    def test_remove_articles(self):

        self.assertTrue('a' not in Parser.remove_articles(['a', 'big', 'day']))
        self.assertTrue('big' in Parser.remove_articles(['a', 'big', 'day']))
        self.assertTrue('day' in Parser.remove_articles(['a', 'big', 'day']))

        self.assertTrue('those' not in Parser.remove_articles(
            ['whose', 'are', 'those']))
        self.assertTrue('whose' in Parser.remove_articles(
            ['whose', 'are', 'those']))
        self.assertTrue('are' in Parser.remove_articles(
            ['whose', 'are', 'those']))

        self.assertTrue('the' not in Parser.remove_articles(['the']))
        self.assertTrue(' the' in Parser.remove_articles([' the']))


    def test_get_verb_invalid(self):

        self.assertIsNone(Parser.get_verb(['', 'sail', 'home']))
        self.assertIsNone(Parser.get_verb(['dear', 'me']))
        self.assertIsNone(Parser.get_verb([]))
        self.assertIsNone(Parser.get_verb(['read1']))
        self.assertIsNone(Parser.get_verb(['you', 'go']))


    def test_get_verb_valid(self):

        CANONICAL_ACTIONS = [
                'drop', 'go', 'listen', 'look', 'pull', 'push', 'recharge',
                'take', 'talk', 'use', 'wait', 'help', 'inventory',
                'loadgame', 'savegame', 'quit'
                ]

        for verb in CANONICAL_ACTIONS:
            self.assertEqual(verb, Parser.get_verb([verb]))

        for verb in Parser.ACTIONS:
            if verb not in CANONICAL_ACTIONS:
                self.assertNotEqual(verb, Parser.get_verb([verb]))

        self.assertNotEqual('look at', Parser.get_verb(['look', 'at']))

        for verb in Parser.ACTIONS:
            self.assertIsNotNone(Parser.get_verb([verb]))


    def test_get_verb_len(self):

        lst = []
        Parser.get_verb(lst)
        self.assertEqual(0, len(lst))

        lst = ['']
        Parser.get_verb(lst)
        self.assertEqual(1, len(lst))

        lst = ['go']
        Parser.get_verb(lst)
        self.assertEqual(0, len(lst))

        lst = ['go', 'north']
        Parser.get_verb(lst)
        self.assertEqual(1, len(lst))

        lst = ['don\'t', 'go']
        Parser.get_verb(lst)
        self.assertEqual(2, len(lst))

        lst = ['go', 'go', 'go']
        Parser.get_verb(lst)
        self.assertEqual(2, len(lst))

        lst = ['clutch', 'the', 'thing']
        Parser.get_verb(lst)
        self.assertEqual(2, len(lst))


    def test_get_prepositions(self):

        self.assertNotIn('an', Parser.get_prepositions(
            ['read', 'em', 'an', 'weep']))
        self.assertIn('up', Parser.get_prepositions(
            ['y\'all', 'all', 'up', 'in', 'my', 'grill']))
        self.assertIn('in', Parser.get_prepositions(
            ['y\'all', 'all', 'up', 'in', 'my', 'grill']))

        self.assertEqual(0, len(Parser.get_prepositions(['go', 'home'])))
        self.assertEqual(1, len(Parser.get_prepositions(['go', 'out'])))
        self.assertEqual(1, len(Parser.get_prepositions(['go', 'up'])))
        self.assertEqual(1, len(Parser.get_prepositions(['go', 'under'])))
  

    def test_get_exit_type(self):

        self.assertEqual('sliding door', Parser.get_exit_type(
            ['sliding', 'door']))

        self.assertEqual('saloon doors', Parser.get_exit_type(
            ['saloon', 'doors']))

        self.assertEqual('air duct', Parser.get_exit_type(
            ['air', 'duct']))

        self.assertEqual('steel door', Parser.get_exit_type(
            ['steel', 'door']))

        self.assertEqual('hallway', Parser.get_exit_type(
            ['hallway']))

        self.assertEqual('elevator', Parser.get_exit_type(
            ['elevator']))

        self.assertEqual('glass door', Parser.get_exit_type(
            ['glass', 'door']))

        self.assertEqual('opening', Parser.get_exit_type(
            ['opening']))

        self.assertEqual('hallway', Parser.get_exit_type(
            ['hall', 'way']))

        self.assertEqual('air duct', Parser.get_exit_type(
            ['use', 'vent', 'path']))

        self.assertIsNone(Parser.get_exit_type(['talk', 'to', 'me']))
        self.assertIsNone(Parser.get_exit_type([]))
        self.assertIsNone(Parser.get_exit_type(['']))
        self.assertIsNone(Parser.get_exit_type(['north']))


    def test_get_item(self):

        self.assertIsNone(Parser.get_item(['read', 'my', 'lips', 'no', 'new']))
        self.assertIsNone(Parser.get_item([]))
        self.assertIsNone(Parser.get_item(['']))
        
        self.assertEqual('ssd', Parser.get_item(['solid', 'state', 'drive']))
        self.assertEqual('ssd', Parser.get_item(['solid', 'state']))
        self.assertEqual('ssd', Parser.get_item(['an', 'ssd', 'item']))
        self.assertEqual('ssd', Parser.get_item(['large', 'ssd']))
        self.assertEqual('ssd', Parser.get_item(['hard', 'disk']))
        self.assertEqual('ssd', Parser.get_item(['hard', 'drive']))

        self.assertNotEqual('ssd', Parser.get_item(['hard', 'to', 'disk']))
        self.assertNotEqual('ssd', Parser.get_item([' ssd']))

        self.assertEqual('small bucket', Parser.get_item(
            ['one', 'small', 'bucket']))
        self.assertEqual('large bucket', Parser.get_item(
            ['one', 'large', 'bucket']))
        self.assertEqual('large bucket', Parser.get_item(
            ['one', 'small', 'large', 'bucket']))
        self.assertNotEqual(Parser.get_item(['small', 'bucket']),
                Parser.get_item(['large', 'bucket']))

        # at one point 'usb cable' erroneously resolved to 'usb'
        self.assertEqual('usb cord', Parser.get_item(
            ['usb', 'cable']))

    def test_get_character(self):

        self.assertIsNone(Parser.get_character(['read', 'my', 'lips', 'no', 'new']))
        self.assertIsNone(Parser.get_character([]))
        self.assertIsNone(Parser.get_character(['']))
        
        self.assertEqual('wasp-12', Parser.get_character(['wasp-12']))
        self.assertEqual('wasp-12', Parser.get_character(['wasp12']))
        self.assertEqual('wasp-12', Parser.get_character(['wasp', '12']))
        self.assertEqual('wasp-12', Parser.get_character(['it\'s', 'wasp12']))

        self.assertNotEqual('wasp-12', Parser.get_character(['was-p12']))
        self.assertNotEqual('wasp-12', Parser.get_character(['wasp1']))
        self.assertNotEqual('wasp-12', Parser.get_character(['wasp-12 ']))
        self.assertNotEqual('wasp-12', Parser.get_character(['wasp', 'to', '12']))

        self.assertEqual('robo-bear', Parser.get_character(
            ['one', 'stuffed', 'robot', 'bear']))
        self.assertEqual('robo-bear', Parser.get_character(
            ['one', 'robobear']))
        self.assertEqual('robo-bear', Parser.get_character(
            ['the', 'holy', 'robo-bear']))


    def test_get_direction(self):

        self.assertEqual('north', Parser.get_direction(['n']))
        self.assertEqual('down', Parser.get_direction(['below']))
        self.assertEqual('south', Parser.get_direction(['south']))
        self.assertEqual('west', Parser.get_direction(['w', 'n']))
        self.assertEqual('west', Parser.get_direction(['w', 'n', 'e', 's']))
        self.assertEqual('up', Parser.get_direction(['up']))

        # make sure direction is first word
        self.assertIsNone(Parser.get_direction(
            ['which', 'way', 'is', 'up']))
        self.assertIsNone(Parser.get_direction(
            ['which', 'way', 'is', 'north']))
        self.assertIsNone(Parser.get_direction(['the', 'north']))

        self.assertIsNone(Parser.get_direction(['which', 'way']))
        self.assertIsNone(Parser.get_direction(['up?']))
        self.assertIsNone(Parser.get_direction(['up ']))
        self.assertIsNone(Parser.get_direction(['']))
        self.assertIsNone(Parser.get_direction([]))


    def test_get_identity(self):

        # canonical food names
        core_list = ['jolly ranchers', 'french fries', 'greens',
                'tacos', 'sizzling rice soup']

        # aliases for above food names
        alt_list = {
                # JOLLY RANCHERS
                'candy':            'jolly ranchers',
                'hard candy':       'jolly ranchers',
                'jolly ranchers':   'jolly ranchers',
                # FRENCH FRIES
                'fries':            'french fries',
                'fried potatoes':   'french fries',
                'taters':           'french fries',
                # GREENS
                'green salad':      'greens',
                'salad':            'greens',
                'lettuce':          'greens',
                'mixed greens':     'greens',
                'garden mix':       'greens',
                'lettuces':         'greens',
                # TACOS
                'tacos':            'tacos',
                'tortillas':        'tacos',
                'taco':             'tacos',
                # SIZZLING RICE SOUP
                'porridge':         'sizzling rice soup',
                'rice soup':        'sizzling rice soup',
                'rice porridge':    'sizzling rice soup'
                }

        input_list = ['i', 'want', 'candy']
        self.assertEqual('jolly ranchers',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['candy']
        self.assertEqual('jolly ranchers',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['jolly', 'ranchers']
        self.assertEqual('jolly ranchers',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['jolly ranchers']
        self.assertNotEqual('jolly ranchers',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['ranchers', 'jolly']
        self.assertNotEqual('jolly ranchers',
                Parser.get_identity(input_list, core_list, alt_list))

        input_list = ['eat', 'moar', 'fries']
        self.assertEqual('french fries',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['eat', 'fewer', 'french', 'fries']
        self.assertEqual('french fries',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['fried', 'potatoes']
        self.assertEqual('french fries',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['fried', 'potato']
        self.assertNotEqual('french fries',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['', 'taters']
        self.assertEqual('french fries',
                Parser.get_identity(input_list, core_list, alt_list))

        input_list = ['ten', 'green', 'salads']
        self.assertNotEqual('greens',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['salad', 'greens']
        self.assertEqual('greens',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['garden', 'bell', 'mix']
        self.assertNotEqual('greens',
                Parser.get_identity(input_list, core_list, alt_list))

        input_list = ['taco', 'is', 'your', 'friend']
        self.assertEqual('tacos',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['attack', 'of', 'the', 'tacos ']
        self.assertNotEqual('tacos',
                Parser.get_identity(input_list, core_list, alt_list))

        input_list = ['rice', 'sizzling', 'soup']
        self.assertNotEqual('sizzling rice soup',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['sizzling rice soup']
        self.assertNotEqual('sizzling rice soup',
                Parser.get_identity(input_list, core_list, alt_list))
        input_list = ['sizzling', 'rice', 'soup']
        self.assertEqual('sizzling rice soup',
                Parser.get_identity(input_list, core_list, alt_list))


    def test_action_requested_go(self):
        (action, exit, direction, item, character) = Parser.action_requested(
                'go out the sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'go sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'go out the slide door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'go up to the sliding door')
        self.assertIsNone(action)
        self.assertIsNone(exit)
        self.assertIsNone(direction)

        (action, exit, direction, item, character) = Parser.action_requested(
                'go sliding into door')
        self.assertIsNone(action)
        self.assertIsNone(exit)

        (action, exit, direction, item, character) = Parser.action_requested(
                'go out the sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')
        
        (action, exit, direction, item, character) = Parser.action_requested(
                'go door')
        self.assertIsNone(action)
        self.assertIsNone(exit)

        (action, exit, direction, item, character) = Parser.action_requested(
                'go north')
        self.assertEqual(action, 'go')
        self.assertEqual(direction, 'north')

        (action, exit, direction, item, character) = Parser.action_requested(
                'go n')
        self.assertEqual(action, 'go')
        self.assertEqual(direction, 'north')

        (action, exit, direction, item, character) = Parser.action_requested(
                'out the sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'out the slide door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')

        (action, exit, direction, item, character) = Parser.action_requested(
                'up to the sliding door')
        self.assertIsNone(action)
        self.assertIsNone(exit)

        (action, exit, direction, item, character) = Parser.action_requested(
                'sliding into door')
        self.assertIsNone(action)
        self.assertIsNone(exit)

        (action, exit, direction, item, character) = Parser.action_requested(
                'out the sliding door')
        self.assertEqual(action, 'go')
        self.assertEqual(exit, 'sliding door')
        
        (action, exit, direction, item, character) = Parser.action_requested(
                'door')
        self.assertIsNone(action)
        self.assertIsNone(exit)

        (action, exit, direction, item, character) = Parser.action_requested(
                'don\'t go')
        self.assertIsNone(action)

        (action, exit, direction, item, character) = Parser.action_requested(
                'north')
        self.assertEqual(action, 'go')
        self.assertEqual(direction, 'north')

        (action, exit, direction, item, character) = Parser.action_requested(
                'n')
        self.assertEqual(action, 'go')
        self.assertEqual(direction, 'north')

    def test_action_requested_other(self):
        (action, exit, direction, item, character) = Parser.action_requested(
                'drop the security badge')
        self.assertEqual(action, 'drop')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'drop security badge')
        self.assertEqual(action, 'drop')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'drop the badge')
        self.assertEqual(action, 'drop')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'throw the security badge')
        self.assertEqual(action, 'drop')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'use the security badge on jim')
        self.assertEqual(action, 'use')
        self.assertEqual(item, 'security badge')
        self.assertEqual(character, 'jim')

        (action, exit, direction, item, character) = Parser.action_requested(
                'utilize pin jim')
        self.assertEqual(action, 'use')
        self.assertEqual(item, 'security badge')
        self.assertEqual(character, 'jim')

        (action, exit, direction, item, character) = Parser.action_requested(
                'utilize jim pin')
        self.assertEqual(action, 'use')
        self.assertEqual(item, 'security badge')
        self.assertEqual(character, 'jim')

        (action, exit, direction, item, character) = Parser.action_requested(
                'look at jim')
        self.assertEqual(action, 'look at')
        self.assertEqual(character, 'jim')

        (action, exit, direction, item, character) = Parser.action_requested(
                'look at pin')
        self.assertEqual(action, 'look at')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'look over at badge')
        self.assertEqual(action, 'look at')
        self.assertEqual(item, 'security badge')

        (action, exit, direction, item, character) = Parser.action_requested(
                'look')
        self.assertEqual(action, 'look')

        (action, exit, direction, item, character) = Parser.action_requested(
                'view the room')
        self.assertEqual(action, 'look')
        self.assertIsNone(item)
        self.assertIsNone(character)

        (action, exit, direction, item, character) = Parser.action_requested(
                'boost up the battery')
        self.assertEqual(action, 'recharge')
        self.assertIsNone(item)

        (action, exit, direction, item, character) = Parser.action_requested(
                'clutch into robobear')
        self.assertEqual(action, 'take')
        self.assertEqual(character, 'robo-bear')

        (action, exit, direction, item, character) = Parser.action_requested(
                'clutch that little robo-bear')
        self.assertEqual(action, 'take')
        self.assertEqual(character, 'robo-bear')

        (action, exit, direction, item, character) = Parser.action_requested(
                'look over at')
        self.assertEqual(action, 'look at')

        (action, exit, direction, item, character) = Parser.action_requested(
                'don\'t quit')
        self.assertIsNone(action)

        (action, exit, direction, item, character) = Parser.action_requested(
                '')
        self.assertIsNone(action)

        (action, exit, direction, item, character) = Parser.action_requested(
                'is what it is')
        self.assertIsNone(action)

        (action, exit, direction, item, character) = Parser.action_requested(
                'LOOK OUT!')
        self.assertEqual(action, 'look')

        (action, exit, direction, item, character) = Parser.action_requested(
                'grab the usb cord')
        self.assertEqual(action, 'take')
        self.assertEqual(item, 'usb cord')

        (action, exit, direction, item, character) = Parser.action_requested(
                'grab the usb cable')
        self.assertEqual(action, 'take')
        self.assertEqual(item, 'usb cord')

        (action, exit, direction, item, character) = Parser.action_requested(
                'grab the usb')
        self.assertEqual(action, 'take')
        self.assertEqual(item, 'usb drive')

        (action, exit, direction, item, character) = Parser.action_requested(
                ' Look ')
        self.assertEqual(action, 'look')


if __name__ == '__main__':
    unittest.main(exit = False)
