#!/usr/bin/python3
import sys
from colorama import Fore

def showinstructions():
    print(Fore.RED + "Welcome to TextCraft!")
    print('You wakeup in a strange and dark room. \nYou see one door leading out and a table in the middle of the room with a note on it.')
    print('''Commands:
        go [direction]
        get [item]
        open [chest]
        attack [beast]
        use [item]
        read [note]''')
# showinstructions()

def showstatus():
    print('====================')
    print('You are in the ' + currentroom)
    print('Inventory :' + str(inventory))
    # if "item" in rooms[currentroom]:
    #     print('You see a ' + rooms[currentroom]['item'])
    if currentroom == 'room2':
        print("You walk into the room and see two more tunnels.\nOne straight ahead and one to the left")
    if currentroom == 'room3':
        print("As you walk into the next room, you see 4 tunnels.\nOne to the north, to the east, to the west, and the one you came through from the south.")
    
    print("Type 'help' for available commands, or 'q' to quit.")
    print('====================')
# showstatus()

# def create_global_function():
#     global move
#     def move = (input('>'))

inventory = []


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
        'item' : 'sword'
    },
    'chest1' : {
        'item' : 'sword',
        'east' : 'hermit_hut'
    },
    'hallway_2' : {
        'north' : 'hallway_3',
        'south' : 'hallway_1',
        'east' : 'bear_cave',
        'west' : 'empty_room'
    },
    'bear_cave' : {
        'item' : 'pickaxe',
        'beast' : 'bear',
        'west' : 'hallway_2'
    },    
    'empty-room' : {
        'north' : 'armor_room',
        'east' : 'hallway_2'    
    },
    'armor_room' : {
        'west' : 'hallway_3',
        'south' : 'empty_room',
        'item' : 'armor'
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
        'item' : 'gold'
    },
    'blocked_in' : {
        'north' : 'escape_room',
        'south' : 'monster_lair'
    },
    'escape_room' : {
        'south' : 'blocked_in',
        'item' : 'horse'
    }
}

currentroom = 'strange_room'

showinstructions()

def strange_room():
    move[0] = input('>')
    if move[0] == "read note" and ('note') in inventory:
        with open("note.txt", "r") as letter1:
            letter = letter1.read()
            print(letter)


def hermit_hut():
    print("It is a dark room with a strange man standing behind a what looks like a chest.")
    # loops=0
    # while True:
    #     print(loops)
    chest_1() 

def chest_1():
    with open("chest.txt", "r") as tool:
        chest = tool.read()
        print(chest)
        if currentroom == 'hermit_hut':
            print(Fore.YELLOW + "It is dangerous to go alone, take this..." + Fore.RED)
    move[0] = input('>')
    if "open" in move[0]:
        if currentroom == "hermit_hut":
            with open("sword.txt", "r") as tool:
                sword = tool.read()
                print(sword)
    if "get" in move[0]:
        if "item" in rooms['chest1'] and move[0] in rooms['chest1']['item']:
            inventory.append(move[0])
            print("You picked up a " + move[0] + '!')
            del rooms['chest1']['item']
        else:
            print('Unable to get ' + move[1] + '!')

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
    


while True:
    showstatus()
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split(" ", 1)
    if move[0] == 'go' :
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
    if move[0] == 'open' :
        if move[1] in rooms[currentroom]:
            currentroom = rooms[currentroom][move[1]]
        # if move[1] in rooms[currentroom]:
        #     currentroom[item] != 'True' :
        #         print('Chest is Empty!')
        else:
            print('There is nothing to open!')
    if move[0] == 'help':
        print('''Commands:
        go [direction]
        get [item]
        open[chest]
        attack [monster]
        use [item]
        read [note]''')
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



