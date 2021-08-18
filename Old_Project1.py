#!/usr/bin/python3

def showinstructions():
    print("Welcome to TextCraft!")
    print('You find yourself in a strange and dark room. \nThere is one door leading out. Your mission, if you choose to accept it, is to make it out of this room alive.')
    print('''Commands:
        go [direction]
        get [item]
        open[chest]
        attack [monster]
        use [item]''')
# showinstructions()

def showstatus():
    print('====================')
    print('You are in the ' + currentroom)
    print('Inventory :' + str(inventory))
    if "item" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom]['item'])
    print('====================')
# showstatus()

inventory = []

rooms = {
    'room1' : {
        'up' : 'room2'
    },
    'room2' : {
        'up' : 'room3',
        'left' : 'room2a'
    },
    'room2a' : {
        'right' : 'room2',
        'chest' : 'chest1'
    },
    'chest1' : {
        'item' : 'sword',
        'back' : 'room2a'
    },
    'room3' : {
        'up' : 'room4',
        'down' : 'room2',
        'right' : 'room3a'
    },
    'room3a' : {
        'up' : 'room3b',
        'left' : 'room3'
    },
    'room3b' : {
        'left' : 'room4',
        'down' : 'room3a'
    },
    'room4' : {
        'up' : 'room5',
        'down' : 'room3'
    },
    'room5' : {
        'up' : 'room6',
        'down' : 'room4',
        'left' : 'room5a'
    },
    'room5a' : {
        'right' : 'room5'
    },
    'room6' : {
        'up' : 'room7',
        'down' : 'room5'
    },
    'room7' : {
        'down' : 'room6'
    }
}

currentroom = 'room1'

showinstructions()

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
    if move[0] == 'q' :
        quit
    # else:
    #     print('Invalid Entry! Please Try Again...')
            

    if currentroom == 'room2a':
        print("It is dangerous to go alone, take this!")

