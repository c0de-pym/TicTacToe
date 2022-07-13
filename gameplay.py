import TicTacToe_board
import config


def game_rules_description():
    # store game description
    rules = ('''
Welcome in Tic Tac Toe game

Rules:
1. Player 1 chose "O" or "X".
2. Player 1 always starts.
3. Chose position of your sign form starting board by placing a number.
4. Try to put you sign in row
''')
    return rules


def framing(framed_text):
    # creating frame around text
    next_line='\n'
    vertical_frame_left="║ "
    vertical_frame_right=" ║"
    find_max_row = framed_text
    rows = find_max_row.split("\n")
    max_row = 0
    for row in rows:
        if len(row) > max_row:
            max_row = len(row)
    chart_lenght = (max_row + 2) * "="
    line_num = 0
    for row in rows:
        if len(row) < len(chart_lenght):
            rows[line_num] =row + " " * (len(chart_lenght)-len(row)-2)
        line_num += 1
    framed_text = "\n".join(rows)
    output_frame = "╔" + chart_lenght +"╗" + next_line + vertical_frame_left + framed_text.replace(next_line, vertical_frame_right + next_line + vertical_frame_left) + vertical_frame_right + next_line + "╚" + chart_lenght + "╝"
    return output_frame


def player1_choice_sign():
    # assign to players their choice, tuple
    p1_sign = input("Player1, please choose your sign 'O' or 'X': ")
    check = False
    p2_sign = ""
    while not check:
        if p1_sign.lower() == 'o':
            p1_sign = "O"
            p2_sign = 'X'
            check = True
        elif p1_sign.lower() == 'x':
            p1_sign = "X"
            p2_sign = 'O'
            check = True
        else:
            print('Please chose only between "X" and "O"')
            p1_sign = input("Player1, please choose your sign 'O' or 'X': ")
            continue
    return p1_sign, p2_sign


def player1(valid_pos):
    # validate choice of player1 and store index of board and check occupation of position on board
    print("Player 1")
    p1 = input("Please choose the position of your sign: ")
    while not (p1 in valid_pos):
        if p1.isdigit():
            p1 = int(p1)
            if p1 in config.position_range:
                print('This position is occupied')
                p1 = input('Please choose another digit between 1 and 9')
                continue
            else:
                print('Your number is out of range')
                p1 = input("Please chose correct digit between 1 and 9")
                continue
        else:
            print('Your value has to be an integer')
            p1 = input('Please choose another digit between 1 and 9')
    return int(p1)


def player2(valid_pos):
    # validate choice of player1 and store index of board and check occupation of position on board
    print("Player 2")
    p2 = input("Please choose the position of your sign: ")
    while not (p2 in valid_pos):
        if p2.isdigit():
            p2 = int(p2)
            if p2 in config.position_range:
                print('This position is occupied')
                p2 = input('Please choose another digit between 1 and 9')
                continue
            else:
                print('Your number is out of range')
                p2 = input("Please chose correct digit between 1 and 9")
                continue
        else:
            print('Your value has to be an integer')
            p2 = input('Please choose another digit between 1 and 9')
    return int(p2)

def draw(valid_pos):
    # check if draw
    draw = False
    if len(valid_pos) == 0:
        draw = True
    return draw


def win_check(board):
    # checking, if there is winning pattern
    win = False
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        win = True
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        win = True
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        win = True
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        win = True
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        win = True
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        win = True
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        win = True
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        win = True
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        win = True
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        win = True
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        win = True
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        win = True
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        win = True
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        win = True
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        win = True
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        win = True
    return win


def keep_playing():
    # ask for playing, if yes we get True value output
    playing = input('Do you wanna play the game? y/n')
    game_on_off = False
    valid = True
    while valid:
        if playing.lower() == 'y':
            game_on_off = True
            break
        elif playing.lower() == 'n':
            game_on_off = False
            break
        else:
            playing = input('I don\'t understand, please enter y or n')
            continue
    return game_on_off


