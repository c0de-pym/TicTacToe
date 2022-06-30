# You never actually used the TicTacToe_board module,
# So there was no point in importing it

import config


def game_rules_description():
    # store game description
    rules = """
Welcome in Tic Tac Toe game

Rules:
1. Player 1 chose "O" or "X".
2. Player 1 always starts.
3. Chose position of your sign form starting board by placing a number.
4. Try to put you sign in row
"""
    return rules


# Moved framing function -> "utils.py",
# since it isn't really related to the gamplay

# Renamed this function to be more clear, since
# player1_choice_sign isn't that helpful
def get_player_1_sign() -> tuple[str, str]:
    # assign to players their choice, tuple
    check: bool = True
    p1_sign: str = ""
    p2_sign: str = ""

    # It doesn't make that much sense to set check to False by deault
    # since you want to check by default anyways
    while check:
        p1_sign: str = input("Player1, please choose your sign 'O' or 'X': ")

        if p1_sign.lower() == "o":
            p1_sign = "O"
            p2_sign = "X"

            check = False
        elif p1_sign.lower() == "x":
            p1_sign = "X"
            p2_sign = "O"

            check = False
        else:
            # Instead of trying to get input again, we can just get it at the start of the file
            print('Please chose only between "X" and "O"')
            continue

    return p1_sign, p2_sign


# Since both players share the same game logic for getting position
# input, we can eliminate a lot of code, by just using one function
# instead of copying it twice (See the Don't Repeat Yourself principle)
def get_player_input(valid_pos: list[str], cur_player_name: str) -> int:
    # validate choice of player1 and store index of board and check occupation of position on board

    print(cur_player_name)

    position = input("Please choose the position of your sign: ")

    while True:
        if position.isdigit():
            position = int(position)

            if position in config.valid_positions:
                position = input("Please choose another digit between 1 and 9")
                continue
            else:
                print("Your number is out of range")
                position = input("Please chose correct digit between 1 and 9")

            if position in valid_pos:
                print("This position is occupied, try again")
                continue
            else:  # if we finally passed all checks
                break
        else:
            print("Your value has to be an integer")
            position = input("Please choose another digit between 1 and 9")

    return int(position)


# Rename function to be more clear as to what it does
def is_game_draw(valid_pos: list[str]) -> bool:
    # This function can be reduced to:
    return len(valid_pos) == 0


# It looks like there are a bunch of changes here,
# But it's just the black formatter converting ' -> "
def win_check(board: list[str]) -> bool:
    # checking, if there is winning pattern
    win = False

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        win = True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        win = True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        win = True
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        win = True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        win = True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        win = True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        win = True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        win = True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        win = True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        win = True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        win = True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        win = True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        win = True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        win = True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        win = True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        win = True

    return win


def keep_playing():
    # ask for playing, if yes we get True value output
    playing = input("Do you wanna play the game? y/n: ")
    game_on_off = False
    valid = True

    while valid:
        if playing.lower() == "y":
            game_on_off = True
            break
        elif playing.lower() == "n":
            game_on_off = False
            break
        else:
            playing = input("I don't understand, please enter y or n")
            continue

    return game_on_off
