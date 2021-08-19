#!/usr/bin/python3
import sys
from colorama import Fore

#Game Instructions
def showinstructions():
    print(Fore.CYAN + "Welcome to TextCraft!")
    print(Fore.RED + 'You wakeup in a strange and dark room. \nYou see one door leading out and a table in the middle of the room with a note on it.')
    print('''Commands:
        go [direction]
        get [item]
        go [chest]
        attack [beast]
        use [item]
        read [note]
        destroy [wall]''')

#Player Status
def showstatus():
    print('====================')
    print('You are in the ' + currentroom)
    print('Inventory :' + str(inventory))
    # if "chest" in rooms[currentroom]:
    #     print('You see a ' + rooms[currentroom]['chest'])
    if "item" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom]['item'])
    if currentroom == 'hallway_1':
        print("You walk into the room and see two more tunnels.\nOne straight ahead to the north and one to the west")
    if currentroom == 'hallway_2':
        print("As you walk into the next room, you see 4 tunnels.\nOne to the north, to the east, to the west, and the one you came through from the south.")
    if currentroom == 'hallway_3':
        print('You walk into a wide area.\nYou see a tunnel continue to the north.\nThere is also a tunnel to both the east and the west.')
    if currentroom == 'echo_room':
        print('You enter a small room with.\nThere is a tunnel behind you to the east.\nThere is also a tunnel to the north.')
    print("Type 'help' for available commands, or 'q' to quit.")
    print('====================')

#Setting Variables
inventory = []
player_name = (input(Fore.RED + "What is your name?"))
currentroom = "strange_room"
# def f():
#     global currentroom 
#     currentroom = "strange_room"
#     print(currentroom)

# Room and Navigation Layout
rooms = {
    'strange_room' : {
        'north' : 'hallway_1',
        'item' : 'note'
    },
    'hallway_1' : {
        'north' : 'hallway_2',
        'west' : 'hermit_hut'
    },
    'hermit_hut' : {
        'east' : 'hallway_1',
        'chest' : 'chest1'
    },
    'chest1' : {
        'item' : 'sword',
        'east' : 'hermit_hut'
    },
    'hallway_2' : {
        'north' : 'hallway_3',
        'south' : 'hallway_1',
        'east' : 'bear_cave',
        'west' : 'echo_room'
    },
    'bear_cave' : {
        'item' : 'pickaxe',
        'beast' : 'bear',
        'west' : 'hallway_2'
    },    
    'echo_room' : {
        'north' : 'armor_room',
        'east' : 'hallway_2'    
    },
    'armor_room' : {
        'east' : 'hallway_3',
        'south' : 'echo_room',
        'chest' : 'chest3'
    },
    'hallway_3' : {
        'north' : 'monster_lair',
        'south' : 'hallway_2'
    },
    'monster_lair' : {
        'north' : 'blocked_in',
        'south' : 'hallway_3',
        'west' : 'monster_chest'
    },
    'monster_chest' : {
        'east' : 'monster_lair',
        'item' : 'diamonds'
    },
    'blocked_in' : {
        'north' : 'escape_room',
        'south' : 'monster_lair',
        'wall' : 'brick'
    },
    'escape_room' : {
        'south' : 'blocked_in',
        'item' : 'horse'
    }
}

showinstructions()

#Defining specific movements and actions within rooms. 
def strange_room():
    move[0] = input('>')
    if move[0] == "read note" and ('note') in inventory:
        with open("note.txt", "r") as letter1:
            letter = letter1.read()
            print(letter)
def hermit_hut():
    print("It is a dark room with a strange man standing behind a what looks like a chest.")
    chest_1() 
def bear_cave():
    print("As you enter the cave, you see a bear sleeping.\nUnder the bears arm, you see what looks like a tool of some sort.")
    with open("sleepingbear.txt", "r") as bear:
        bears = bear.read()
        print(bears)
    print("Will you kill the bear to get the tool?\nWill you leave a sleeping bear to sleep?")
    move[0] = input('>')
    if move[0] == 'attack bear':
        if 'sword' in inventory: 
            print('You have killed the bear!\nYou see that the tool under the bear is a pickaxe.')
            with open("pickaxe.txt", "r") as tool:
                pickaxe = tool.read()
                print(pickaxe)
                del rooms['bear_cave']['beast']
        else:
            print("Probably shouldn't have done that bear-handed...\nPlease try again.\nA weapon may be useful.")
            sys.exit() 
    if move[0] == 'get pickaxe': 
        if 'beast' in rooms[currentroom] and 'bear' in rooms[currentroom]['beast']:
            print("You woke a sleeping bear.\nThat was not a good idea.\nYou have been mauled.\nGood Bye!")
            sys.exit()
        else:
            print("This might come in handy!")
            pass
def armor_room():
    print('It looks like you found a workshop.\nThere are tools everywhere and pieces metal and cloth strung about.\nIs that a chest?')
    chest_1()
def monster_lair():
    print("Is that a DRAGON?????\nIt looks like he is blocking the only exit.\nFight of Flight!")
    with open("dragon2.txt", "r") as drago:
        dragon = drago.read()
        print(dragon)
    print(player_name + ' versus Drago the Dragon.\nWho will win?')
    move[0] = input('>')
    if move[0] == 'attack dragon':
        if 'sword' and 'armor' in inventory: 
            print('With sheer luck, you killed the dragon with the first blow.\nYou now see a small cave to the west.\nYou also see what looks like the way out to the north.')
            del rooms['dragon_lair']['beast']
        elif 'sword' in inventory:
            print("You might want to think about your life choices.\nFind something to protect you next time.\nTry Again!!!")
            sys.exit()
        elif 'armor' in inventory:
            print("You attacked a dragon with no weapon?\nDarwin Award Winner.\nTry Again!!!")
            with open("darwin.txt", "r") as tool:
                darwin = tool.read()
                print(darwin)
            sys.exit()
        else:
            print('You obviously did not think this plan out.\nNext time, think before you act.')
            sys.exit()
    if move[0] == 'go chest':
        chest_1()
def chest_1():
    with open("chest.txt", "r") as tool:
        chest = tool.read()
        print(chest)
        if currentroom == "hermit_hut":
            print(Fore.YELLOW + "It is dangerous to go alone, take this..." + Fore.RED)
    move[0] = input('>')
    if "go chest" in move[0]:
        if currentroom == "hermit_hut":
            with open("sword.txt", "r") as tool:
                sword = tool.read()
                print(sword)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if "go chest" in move[0]:
        if currentroom == "armor_room":
            with open("armor.txt", "r") as tool:
                armor = tool.read()
                print(armor)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if "go chest" in move[0]:
        if currentroom == "monster_lair":
            with open("diamond.txt", "r") as tool:
                diamond = tool.read()
                print(diamond)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    # if "get" in move[0]:
    #     if "item" in rooms['chest1'] and move[0] in rooms['chest1']['item']:
    #         inventory.append(move[0])
    #         print("You picked up a " + move[0] + '!')
    #         del rooms['chest1']['item']
    #     else:
    #         print('Unable to get ' + move[1] + '!')
def escape_room():
    with open("horse.txt", "r") as tool:
                horse = tool.read()
                print(horse)
    print('Congratulations,' + player_name + '! Against all odds, you made it out alive.\nYou see a horse, now you can live your lifelong dream.\nGet that horse and ride off into the sunset.')
    if move[0] == 'get' :
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            inventory += [move[1]]
        with open("sunset.txt", "r") as tool:
                sunset = tool.read()
                print(sunset)
                sys.exit()     
def blocked_in():
    print('It looks like the path ahead is blocked.\nDo you have the tools to break through?')
    move[0] = input('>')
    if move[0] == 'destroy wall':
        if 'pickaxe' in inventory: 
            print('Using the pickaxe, you are able to clear your path out.')
            del rooms['wall']['brick']
        else:
            print('You do not have the right tools for the job.')
    if move[0] == 'go north':
        if 'wall' in rooms[currentroom] and 'brick' in rooms[currentroom]['wall']:
            print("You are unable to move forward. A brick wall is blocking your way.")
#General Game Control Setup
while True:
    showstatus()
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split(" ", 1)
    if move[0] == 'go':
        if move[1] in rooms[currentroom]:
            currentroom = rooms[currentroom][move[1]]
        else:
            print('There is nothing in this direction!')
    if move[0] == 'get' :
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            inventory += [move[1]]
            print("You picked up a " + move[1] + '!')
            del rooms[currentroom]['item']
        else:
            print('Unable to get ' + move[1] + '!')
    # if move[0] == 'enter':
    #     if move[1] in rooms[currentroom]:
    #         currentroom = rooms[currentroom][move[1]]
    #     else:
    #         print('There is nothing to open!')
    if move[0] == 'help':
        print('''Commands:
        go [direction]
        go [chest]
        get [item]
        attack [monster]
        use [item]
        read [note]
        destroy [wall]''')
    if move[0] == 'q' :
        break
    # else:
    #     print('Invalid Entry! Please Try Again...')
            

    if currentroom == 'hermit_hut':
        hermit_hut()
    if currentroom == 'strange_room':
        strange_room()
    if currentroom == 'bear_cave':
        bear_cave()
    if currentroom == 'monster_lair':
        monster_lair()
    if currentroom == 'escape_room':
        escape_room()


