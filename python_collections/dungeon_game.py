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
    x, y = player
    # if move == LEFT, x - 1
    if move == "LEFT":
        x -= 1
    # if move == RIGHT, x + 1
    if move == "RIGHT":
        x += 1
    # if move == UP, y - 1
    if move == "UP":
        y -= 1
    # if move == DOWN, y + 1
    if move == "DOWN":
        y += 1
    return x, y

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

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    monster, door, player = get_locations()

    while True:
        draw_map(player)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player)) # fill with player's position
        print("You can move {}".format(", ".join(valid_moves))) # fill with available moves
        print("Enter Q to quit")

        move = input("> ")
        move = move.upper()

        if move == 'q':
            break

        if move in valid_moves:
            # Good move? Change the player position
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                break
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                break
        else:
            # Bad move? Don't chnage anything!
            input("\n ** Wals are hard! Don't run into them! ** \n")
        clear_screen()

        # On the door? They win!
        # On the monster? They lose!
        # Otherwise, loop back around

clear_screen()
print("Welcome to the dungeon!")
input("Press Enter to start the game")
clear_screen()
game_loop()