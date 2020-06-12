from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declaring Items

items = {
    'coins': Item('Galleons', 'Golden Coins'),
    'sword': Item('Sword', 'Steel blade'),
    'shield': Item('Shield', 'Wooden protection'),
    'wand': Item('Wand', 'Magical Wand'),
    'materia': Item('Materia', 'Powers unknown')
}

# Link items to rooms

room['outside'].add_item(items['coins'])
room['foyer'].add_item(items['sword'])
room['overlook'].add_item(items['shield'])
room['treasure'].add_item(items['materia'])
room['narrow'].add_item(items['wand'])


name = input('What is your name, Adventurer? ')
player = Player(name, room['outside'])
# player.current_room = room['outside']
print(player.current_room)
print(room['outside'].show_items())
running = True
while running:
    # Prints the current room name
    print(player.current_room.name)
    # Prints the current description
    print(player.current_room.description)
    # Prints current inventory
    print(player.current_room)

    # Waits for user input and decides what to do.
    input_var = input("type a direction ")

# A shorter way

   # if input_var in {'n', 'w', 's', 'e'}:
   #     if hasattr(player.current_room, f'{input_var}_to'):
   #         player.current_room = getattr(
   #             player.current_room, f'{input_var}_to')

# check if the current room is this attritbute

    if input_var == 'n':
        direction = player.current_room.n_to
        if direction == None:
            print("Can't go that way")
        else:
            # move the player to that room
            player = Player(name, direction)

            print(player)
            print(player.current_room.show_items())

    elif input_var == 'w':
        direction = player.current_room.w_to
        if direction == None:
            print("Can't go that way")
        else:
            player = Player(name, direction)

            print(player)
            print(player.current_room.show_items())

    elif input_var == 's':
        direction = player.current_room.s_to
        if direction == None:
            print("Can't go that way")
        else:
            player = Player(name, direction)

            print(player)
            print(player.current_room.show_items())

    elif input_var == 'e':
        direction = player.current_room.e_to
        if direction == None:
            print("Can't go that way")
        else:
            player = Player(name, direction)

            print(player)
            print(player.current_room.show_items())

    elif input_var == 'q':
        print('See you later')
        running = False
