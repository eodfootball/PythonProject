#!/usr/bin/python3
import sys
from colorama import Fore

#Setting Variables
currentroom = "strange_room"
inventory = []
player_name = (input(Fore.RED + "What is your name? "))
tool = ''
move = ''
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
        'chest' : 'chest1',
        'back' : 'hallway_1'
    },
    'chest1' : {
        'item' : 'sword',
        'back' : 'hermit_hut'
    },
    'hallway_2' : {
        'north' : 'hallway_3',
        'south' : 'hallway_1',
        'east' : 'bear_cave',
        'west' : 'echo_room',
        'back' : 'hallway_1'
    },
    'bear_cave' : {
        'item' : 'pickaxe',
        'beast' : 'bear',
        'west' : 'hallway_2',
        'back' : 'hallway_2'
    },    
    'echo_room' : {
        'north' : 'armor_room',
        'east' : 'hallway_2',
        'back' : 'hallway_2'    
    },
    'armor_room' : {
        'east' : 'hallway_3',
        'south' : 'echo_room',
        'chest' : 'chest3',
        'back' : 'echo_room'
    },
    'chest3' : {
        'back' : 'armor_room',
        'item' : 'armor'
    },
    'hallway_3' : {
        'north' : 'monster_lair',
        'south' : 'hallway_2',
        'back' : 'hallway_2'
    },
    'monster_lair' : {
        'north' : 'escape_room',
        'south' : 'hallway_3',
        'chest' : 'monster_chest',
        'beast' : 'dragon',
        'back' : 'hallway_3'
    },
    'monster_chest' : {
        'back' : 'monster_lair',
        'item' : 'diamonds'
    
    },
    'escape_room' : {
        'south' : 'escape_room',
        'item' : 'horse',
        'back' : 'escape_room'
    }
}

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
def showstatus(currentroom):
    print('====================')
    print('You are in ' + currentroom)
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
        print('You walk into a wide area.\nYou see a tunnel continue to the north, something looks to be lighting up the next room.\nBe Careful.')
    if currentroom == 'echo_room':
        print('You enter a small room with.\nThere is a tunnel behind you to the east.\nThere is also a tunnel to the north.')
    print("Type 'help' for available commands, or 'q' to quit.")
    print('====================')

showinstructions()                                                                  

#Defining specific movements and actions within rooms. 
def strange_room():
    move[0] = input('>').lower()
    if move[0] == "read note" and ('note') in inventory:
        with open("note.txt", "r") as letter1:
            letter = letter1.read()
            print(letter)
def hermit_hut():
    print("It is a dark room with a strange man standing behind a what looks like a chest.")
    with open("chest.txt", "r") as tool:
        chest = tool.read()
        print(chest) 
def bear_cave(): 
    if 'beast' in rooms[currentroom] and 'bear' in rooms[currentroom]['beast']:
        bear_text = '''
        As you enter the cave, you see a bear sleeping.
        Under the bears arm, you see what looks like a tool of some sort.'''
        print(bear_text)
        with open("sleepingbear.txt", "r") as bear:
            bears = bear.read()
            print(bears)
    see_pickaxe = '''
    Will you kill the bear to get the tool?
    Will you leave a sleeping bear to sleep?'''
    print(see_pickaxe)
    move[0] = input('>').lower()
    if move[0] == 'attack bear':
        if 'sword' in inventory: 
            kill_bear = '''
            You have killed the bear!
            You see that the tool under the bear is a pickaxe.'''
            print(kill_bear)
            with open("pickaxe.txt", "r") as tool:
                pickaxe = tool.read()
                print(pickaxe)
                del rooms['bear_cave']['beast']
        else:
            bear_death = '''
            Probably shouldn't have done that bear-handed...
            Please try again.
            A weapon may be useful.'''
            print(bear_death)
            sys.exit() 
    if move[0] == 'get pickaxe': 
        if 'beast' in rooms[currentroom] and 'bear' in rooms[currentroom]['beast']:
            get_axe = '''
            You woke a sleeping bear.
            That was not a good idea.
            You have been mauled.
            Good Bye!'''
            print(get_axe)
            sys.exit()
        else:
            print("This might come in handy!")
            pass
def armor_room():
    armor_text = '''
    It looks like you found a workshop.
    There are tools everywhere and pieces metal and cloth strung about.
    Is that a chest?'''
    print(armor_text)
    with open("chest.txt", "r") as tool:
        chest = tool.read()
        print(chest)
    chest_1(currentroom)
def monster_lair(): 
    if 'beast' in rooms[currentroom] and 'dragon' in rooms[currentroom]['beast']:
        print("Is that a DRAGON?????\nIt looks like he is blocking the only exit.\nFight of Flight!")
        with open("dragon2.txt", "r") as drago:
            dragon = drago.read()
            print(dragon)
        print(player_name + ' versus Drago the Dragon.\nWho will win?')
    move[0] = input('>').lower()
    if move[0] == 'attack dragon':
        if 'sword' in inventory and 'armor' in inventory: 
            kill_dragon ='''With sheer luck, you killed the dragon with the first blow.
            You now see a small chest in the corner.
            You also see what looks like the way out to the north.'''
            print(kill_dragon)
            del rooms['monster_lair']['beast']
            with open("chest.txt", "r") as tool:
                chest = tool.read()
                print(chest)
        elif 'sword' in inventory:
            sword_only ='''
            You might want to think about your life choices.
            Find something to protect yourself with next time.
            Try Again!!!'''
            print(sword_only)
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
        chest_1(currentroom)
    if move[0] == 'go north':
        if 'beast' in rooms[currentroom] and 'dragon' in rooms[currentroom]['beast']:
            print("You were unable to run past the dragon.\nYou became lunch.\nTry again later.")
            sys.exit()
def chest_1(currentroom):
    if currentroom == "chest1":
        if 'item' in rooms[currentroom] and 'sword' in rooms[currentroom]['item']:
            with open("sword.txt", "r") as tool:
                sword = tool.read()
                print(sword)
            print(Fore.YELLOW + "It is dangerous to go alone, take this..." + Fore.RED)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if currentroom == "chest3":
        if 'item' in rooms[currentroom] and 'armor' in rooms[currentroom]['item']:
            with open("shield1.txt", "r") as tool:
                armor = tool.read()
                print(armor)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if currentroom == "monster_chest":
        if 'item' in rooms[currentroom] and 'diamond' in rooms[currentroom]['item']:
            with open("diamonds.txt", "r") as tool:
                diamond = tool.read()
                print(diamond)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
def escape_room():
    with open("horse.txt", "r") as tool:
                horse = tool.read()
                print(horse)
    print('Congratulations,' + player_name + '! Against all odds, you made it out alive.\nYou see a horse, now you can live your lifelong dream.\nGet that horse and ride off into the sunset.')
    if move[0] == 'get':
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            inventory.append(move[1])
            del rooms[currentroom]['item']
        with open("sunset.txt", "r") as tool:
                sunset = tool.read()
                print(sunset)
                sys.exit()     
#General Game Control Setup
while True:
    showstatus(currentroom)
    move = ''
    while move == '':
        move = input('What is your move? ')
    move = move.lower().split(' ', 1)
    if move[0] == 'get' :
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            inventory.append(move[1])
            print("You picked up a " + move[1] + '!')
            del rooms[currentroom]['item']
        else:
            print('Unable to get ' + move[1] + '!')
    elif move[0] == 'go':
        if move[1] in rooms[currentroom]:
            currentroom = rooms[currentroom][move[1]]
        else:
            print('There is nothing in this direction!')
    elif move[0] == 'help':
        print('''Commands:
        go [direction]
        go [chest]
        get [item]
        attack [monster]
        use [item]
        read [note]
        destroy [wall]''')
    elif move[0] == 'q' :
        sys.exit()
    # room_function()
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
    if currentroom == 'chest1' or 'chest3':
        chest_1(currentroom)
    if currentroom == 'armor_room':
        armor_room()
    
   
    
    


