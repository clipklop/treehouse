###


import os
import random

# draw a grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid movement (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    # get the player's location
    # if move == LEFT, x - 1
    # if move == RIGHT, x + 1
    # if move == UP, y - 1
    # if move == DOWN, y + 1
    return player

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player

    # if player's y == 0, the can't move up
    if y == 0:
        moves.remove("UP")

    # if player's y == 4, the can't move down
    if y == 4:
        moves.remove("DOWN")

    # if player's x == 0, the can't move left
    if x == 0:
        moves.remove("LEFT")

    # if player's x == 4, the can't move right
    if x == 4:
        moves.remove("RIGHT")
    return moves

monster, door, player = get_locations()

while True:
    valid_moves = get_moves(player)
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player)) # fill with player's position
    print("You can move {}".format(", ".join(valid_moves))) # fill with available moves
    print("Enter Q to quit")

    move = input("> ").upper()
    if move == 'Q':
        break
    if move in valid_moves:
        player = move_player(player, move)
    else:
        print("\n ** Wals are hard! Don't run into them! ** \n")
        continue

    # Good move? Change the player position
    # Bad move? Don't chnage anything!
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around