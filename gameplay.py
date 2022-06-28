import TicTacToe_board
import config


def game_rules_description():
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


def player1():
    print("Player 1")
    p1 = input("Please choose the position of your sight: ")
    while not p1.isdigit():
        print("Please enter digits")
        p1 = input("Please choose the position of your sight: ")
    while not (int(p1) in config.position_range):
        print(f"Please enter digits between {config.position_range}, excluding max")
        p1 = input("Please choose the position of your sight: ")
    return int(p1)


def player2():
    print('Player2')
    p2 = input("Please choose the position of your sight: ")
    while not p2.isdigit():
        print("Please enter digits")
        p2 = input("Please choose the position of your sight: ")
    while not (int(p2) in config.position_range):
        print(f"Please enter digits between {config.position_range}, excluding max")
        p2 = input("Please choose the position of your sight: ")
    return int(p2)


def win_check():
    board = config.board_pos
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
    print(TicTacToe_board.game_board())
    return win


def keep_playing():
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