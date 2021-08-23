#!/usr/bin/python3
import sys
from colorama import Fore
import re

#Setting Variables
currentroom = "StrangeRoom"
inventory = []
player_name = (input(Fore.RED + "What is your name? "))
tool = ''
move = ''
game_instructions = '''
Commands:
    go [direction]
    get [item]
    open [chest]
    attack [beast]
    use [item]
    read [note]
    break [wall]
    '''
# Room and Navigation Layout
rooms = {
    'StrangeRoom' : {
        'north' : 'SouthHallway',
        'item' : 'note'
    },
    'SouthHallway' : {
        'north' : 'MainHall',
        'west' : 'HermitHut'
    },
    'HermitHut' : {
        'east' : 'SouthHallway',
        'chest' : 'SwordChest',
        'back' : 'SouthHallway'
    },
    'SwordChest' : {
        'item' : 'sword',
        'back' : 'HermitHut'
    },
    'MainHall' : {
        'north' : 'NorthHallway',
        'south' : 'SouthHallway',
        'east' : 'BearCave',
        'west' : 'EchoRoom',
        'back' : 'SouthHallway'
    },
    'BearCave' : {
        'item' : 'pickaxe',
        'beast' : 'bear',
        'west' : 'MainHall',
        'back' : 'MainHall'
    },    
    'EchoRoom' : {
        'north' : 'ArmorRoom',
        'east' : 'MainHall',
        'back' : 'MainHall'    
    },
    'ArmorRoom' : {
        'east' : 'NorthHallway',
        'south' : 'EchoRoom',
        'chest' : 'ArmorChest',
        'back' : 'EchoRoom'
    },
    'ArmorChest' : {
        'back' : 'ArmorRoom',
        'item' : 'armor'
    },
    'NorthHallway' : {
        'north' : 'DragonLair',
        'south' : 'MainHall',
        'back' : 'MainHall'
    },
    'DragonLair' : {
        'north' : 'BlockedIn',
        'south' : 'NorthHallway',
        'chest' : 'DragonChest',
        'beast' : 'dragon',
        'back' : 'NorthHallway'
    },
    'DragonChest' : {
        'back' : 'DragonLair',
        'item' : 'diamonds'
    },
    'BlockedIn' : {
        'back' : 'DragonLair',
        'beast' : 'wall',
        'south' : 'DragonLair',
        'north' : 'EscapeRoom'
    },
    'EscapeRoom' : {
        'south' : 'BlockedIn',
        'item' : 'horse',
        'back' : 'BlockedIn'
    }
}
#Game Instructions
def showinstructions():
    print(Fore.CYAN + "Welcome to TextCraft!")
    welcome_message = '''
    You wakeup in a strange and dark room. 
    You see one door leading out and a table in the middle of the room with a note on it.
    '''
    print(Fore.RED + welcome_message)
    print(game_instructions)

#Player Status
def showstatus(currentroom):
    print('==============================')
    print(capital_words_spaces('You are in a' + currentroom + "."))
    print('Inventory :' + str(inventory))
    # if "chest" in rooms[currentroom]:
    #     print('You see a ' + rooms[currentroom]['chest'])
    if "item" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom]['item'])
    if currentroom == 'SouthHallway':
        print('''
        You walk into the room and see two more tunnels.
        One straight ahead to the north and one to the west.
        Available Moves: go [direction]
        ''')
    if currentroom == 'HermitHut':
        print('Available Moves: go [direction], open [chest]')
    if currentroom == 'MainHall':
        print('''
        As you walk into the next room, you see 4 tunnels.
        One to the north, to the east, to the west, and the one you came through from the south.
        Available Moves: go [direction]
        ''')
    if currentroom == 'BearCave':
        print('Available Moves: go [direction], attack [beast], get [item]')
    if currentroom == 'DragonLair':
        print('Available Moves: go [direction], attack [beast], open [chest]')
    if currentroom == 'ArmorRoom':
        print('Available Moves: go [direction], open [chest]')
    if currentroom == 'NorthHallway':
        print('''You walk into a wide area.
        You see a tunnel continue to the north, something looks to be lighting up the next room.
        Be Careful.
        Available Moves: go [direction]
        ''')
    if currentroom == 'EchoRoom':
        print('''
        You enter a small room with.
        There is a tunnel behind you to the east.
        There is also a tunnel to the north.
        Available Moves: go [direction]
        ''')
    if currentroom == 'BlockedIn':
        print('Available Moves: go [direction], break [wall]')
    if currentroom == 'EscapeRoom':
        print('Available Moves: go [direction], get [item]')
    if currentroom == 'SwordChest' or 'ArmorChest' or 'DragonChest':
        print('Available Moves: go back, get [item]')
    print("Type 'help' for available commands, or 'q' to quit.")
    print('==============================')

showinstructions()                                                                  
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
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
    print("Available Moves: go [direction], open [chest]")
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
                del rooms['BearCave']['beast']
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
        print('''
        Is that a DRAGON?????
        It looks like he is blocking the only exit.
        Fight of Flight!
        ''')
        with open("dragon2.txt", "r") as drago:
            dragon = drago.read()
            print(dragon)
        print(player_name + ' the Brave versus Alduin the Dragon.\nWho will win?')
    print("Available Moves: go [direction], attack [beast]")
    move[0] = input('>').lower()
    if move[0] == 'attack dragon':
        if 'sword' in inventory and 'armor' in inventory: 
            kill_dragon ='''
            With sheer luck, you killed the dragon with the first blow.
            You now see a small chest in the corner.
            You also see what looks like the way out to the north.
            '''
            print(kill_dragon)
            del rooms['DragonLair']['beast']
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
            print('''You attacked a dragon with no weapon?
            Darwin Award Winner.
            Try Again!!!''')
            with open("darwin.txt", "r") as tool:
                darwin = tool.read()
                print(darwin)
            sys.exit()
        else:
            print('''
            You obviously did not think this plan out.
            Next time, think before you act.
            ''')
            sys.exit()
    if move[0] == 'go chest':
        chest_1(currentroom)
    if move[0] == 'go north':
        if 'beast' in rooms[currentroom] and 'dragon' in rooms[currentroom]['beast']:
            print('''
            You were unable to run past the dragon.
            You became lunch.
            Try again later.
            ''')
            sys.exit()
def chest_1(currentroom):
    if currentroom == "SwordChest":
        if 'item' in rooms[currentroom] and 'sword' in rooms[currentroom]['item']:
            with open("sword.txt", "r") as tool:
                sword = tool.read()
                print(sword)
            print(Fore.YELLOW + "It is dangerous to go alone, take this..." + Fore.RED)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if currentroom == "ArmorChest":
        if 'item' in rooms[currentroom] and 'armor' in rooms[currentroom]['item']:
            with open("shield1.txt", "r") as tool:
                armor = tool.read()
                print(armor)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
    if currentroom == "DragonChest":
        if 'item' in rooms[currentroom] and 'diamond' in rooms[currentroom]['item']:
            with open("diamonds.txt", "r") as tool:
                diamond = tool.read()
                print(diamond)
            if move[1] in rooms[currentroom]:
                currentroom = rooms[currentroom][move[1]]
def escape_room():
    if 'item' in rooms[currentroom] and 'horse' in rooms[currentroom]['item']:
        with open("horse.txt", "r") as tool:
            horse = tool.read()
            print(horse)
        rideoff = '''
        ! Against all odds, you made it out alive.
        You see a horse, now you can live your lifelong dream.
        Get that horse and ride off into the sunset.'''
        print('Congratulations,' + player_name + rideoff)
    print("Available Moves: go [direction], get [item]")
    if move[0] == 'get':
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            inventory.append(move[1])
            del rooms[currentroom]['item']
        with open("sunset.txt", "r") as tool:
                sunset = tool.read()
                print(sunset)
                sys.exit()     
def blocked_in(currentroom):
    print('It looks like the path ahead is blocked.\nDo you have the tools to break through the wall?')
    print("Available Moves: go [direction], break [wall]")
    while 'beast' in rooms[currentroom] and 'wall' in rooms[currentroom]['beast']:
        move = input('What is your move? ')
        move = move.lower().split(' ', 1)
        if move[1] == 'north':
            print(Fore.YELLOW + 'There is a wall blocking your way!' + Fore.RED)
            continue
        if move[0] == 'break':
            if 'pickaxe' in inventory:
                print('Using the pickaxe, you are able to clear your path out.')
                del rooms[currentroom]['beast']
            else:
                print(Fore.YELLOW + 'You do not have the right tools for the job.' + Fore.RED)
        else:
            break
def room_function():
    if currentroom == 'HermitHut':
        hermit_hut()
    if currentroom == 'StrangeRoom':
        strange_room()
    if currentroom == 'BearCave':
        bear_cave()
    if currentroom == 'DragonLair':
        monster_lair()
    if currentroom == 'EscapeRoom':
        escape_room() 
    if currentroom == 'SwordChest' or 'ArmorChest':
        chest_1(currentroom)
    if currentroom == 'ArmorRoom':
        armor_room()
    if currentroom == 'BlockedIn':
        blocked_in(currentroom)

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
        print(game_instructions)
    elif move[0] == 'q' :
        sys.exit()
    room_function()

  
    
   
    
    


