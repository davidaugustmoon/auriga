# Auriga
Auriga is a command-line text adventure game developed for Oregon State University's CS467 Capstone Course by David Moon, Jason Goldfine-Middleton, and Gregory Fernandez.
This game is compatible with Linux/UNIX operating systems and Python >= 3.3.

You begin the game as a robot that has mysteriously powered on. You must navigate
the Auriga facility while keeping your batteries charged, and find a way to free 
yourself from corporate shackles. Talk to characters and other robots throughout
the game to determine what to do next. Use items to unlock exits, increase your 
abilities, and solve puzzles to advance through the game.

### Starting the Game
From the project root directory, run the following shell command:
```bash
python3 load_auriga.py
```

### Player Commands

* **go** \<*direction*\>        Move through an exit
* **go** \<*exit*\>:            Move through an exit.
* **take** \<*item*\>:          Take an item.
* **drop** \<*item*\>:          Drop an item.
* **talk** \<*character*\>:     Talk to a character.
* **look**:                     Look around the space you are currently in.
* **savegame**:                 Save your current game.
* **quit**:                     Quit the game.
* **look at** \<*item*\>:       Look more closely at an item.
* **listen**:                   Listen more closely to the sounds around you.
* **pull** \<*item*\>:          Pull an item.
* **push** \<*item*\>:          Push an item.
* **recharge**:                 Charge your batteries in a charger.
* **use** \<*item*\>:           Use an item you are carrying.
* **wait**:                     Wait for something to happen.
* **help**:                     Print list of commands.
* **inventory**:                Print the items you are currently carrying.
* **loadgame**:                 Load a previously saved game.

### Cheat Sheet
This list of commands and actions will navigate you through the entire game from start to finish. This is intended to aid graders on this assignment. It is not intended to be used when "playing" the game.

Push the button to unlock the exit to the east.
```
push button
```

Go through the exit to the east that leads to the Testing Hangar.
```
go east
```

Take the USB drive.
```
take usb
```

Pull the lever to reveal an Auriga security badge.
```
pull lever
```

Take the Auriga security badge.
```
take badge
```

Go through the exit to the south that leads to Hallway 1.
```
go south
```

Go through the exit to the west that leads to the Conference Room.
```
go west
```

Recharge your batteries so you don't run out of energy.
```
recharge
```

Go through the exit to the south that leads to Computer Lab 1.
```
go south
```

Take the SSD.
```
take ssd
```

Go through the exit to the east that leads to Computer Lab 2.
```
go east
```

Take the Ethernet cable.
```
take ethernet
```

Go through the exit to the north that leads to Hallway 1.
```
go north
```

Go through one of the exits to the north that leads to the Testing Hangar
```
go steel door
```

Use the SSD to install it on a broken FREIGHT-500. FREIGHT-500 will come to
life and move a pallet of cargo that was blocking an exit.
```
use ssd
```

Go through the exit to the east, that was previously hidden, and leads to the
Clean Room.
```
go east
```

Take the elevator key in the Clean Room.
```
take key
```

Not really necessary, but it's kind of funny.
```
use usb
```

Go through the exit to the west that leads to the Testing Hangar.
```
go west
```

Go through the exit to the south that leads to Hallway 1.
```
go south
```

Go up in the elevator to Hallway 2.
*Note:* The elevator key found in the Clean Room unlocks the elevator.
```
go up
```

Go through the exit to the west that leads to the Maintenance Room.
```
go west
```

Take the HMI-50 shelving attachment.
*Note:* This increases your carrying capacity by 50 lbs.
```
take hmi-50
```

Recharge your batteries so you don't run out of energy.
```
recharge
```

Go through the exit to the north that leads to the Trash Room.
```
go north
```

Go through the exit to the north that leads to the Supply Closet.
```
go north
```

Take the external power supply.
```
take battery
```

Go through the exit to the south that leads to the Trash Room.
```
go south
```

Go through the exit to the south that leads to the Maintenance Room.
```
go south
```

Recharge your batteries so you don't run out of energy.
```
recharge
```

Go through the exit to the north that leads to the Brig.
```
go north
```

Use the external power supply on Robo-Bear. Robo-Bear will lead you out into
Hallway 2 and unlock the exit to the south, which leads to the Server Room.
```
use battery
```

Go through the exit to the south that leads to the Server Room.
```
go south
```

Use the USB drive to download an encryption key and disable all locking mechanisms.
```
use usb
```

Recharge your batteries so you don't run out of energy.
```
recharge
```

Go through the exit to the north that leads to Hallway 2.
```
go north
```

Go through the exit to the north that leads to the Brig.
```
go north
```

Go through the exit that leads up to the Attic.
```
go up
```

Plug the Ethernet cable into the master server.
```
use ethernet
```


**GAME OVER**
