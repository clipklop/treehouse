# ***
# ASCI-like characters 2D game: Dungeon game
# ***


import random, os


# draw grid
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

# more robust version of making a grid
# CELLS = list((x, y) for x in range(5) for y in range(5))


# clear the screen and redraw grid
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# draw player in the grid
# take input for movement
# move player unless invalid move (past edges of grid)
# check for win/loss

# pick random location for player, monster, exit door
def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    # get player's location
    x, y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player

    # if player's y == 0, they can't move up
    if y == 0:
        moves.remove("UP")
    # if player's y == 4, they can't move down
    if y == 4:
        moves.remove("DOWN")
    # if player's x == 0, they can't move left
    if x == 0:
        moves.remove("LEFT")
    # if player's x == 4, they can't move right
    if x == 4:
        moves.remove("DOWN")

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
    monster, player, door = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        #fill placeholders with the player position and available moves
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit the game.")

        move = input("> ").upper()

        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)

            # check if player found a door or a monster
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time. **\n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False

        else:
            input("\n ** Walls are hard! Do not run into them! **\n")
    else:
        if input("Play again? [Y/n]").lower() != "n":
            game_loop()


clear_screen()
print("Welcome to the dungeon!")
input("Press Enter to start the game")
clear_screen()
game_loop()