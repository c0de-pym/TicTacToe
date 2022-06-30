# Some general comments,
# - If you are using python 3.5>= (which I assume you are)
#   I would highly reccomend using type annotations.
#   They can severly increase your productivity, tools like mypy can
#   Validate the types of your code
#   For further reading, see https://docs.python.org/3/library/typing.html
# - Consider using a formatting tool, to format your code,
#   if you want a very strict (which is better imho), formatter
#   search up "black"

import config
import gameplay
import TicTacToe_board

from utils import framing

gaming: bool = True

print(framing(gameplay.game_rules_description()))
TicTacToe_board.print_sqaure_positions()

# Better way to check for the opposite condition
# Rather than your old impl
if not gameplay.keep_playing():
    print("Bye")
    gaming = False

while gaming:
    valid_pos = config.board_pos_start.copy()
    board = config.board_pos.copy()

    player_one, player_two = gameplay.get_player_1_sign()

    TicTacToe_board.print_game_board(board)

    while not gameplay.win_check(board):
        p1 = gameplay.get_player_input(valid_pos, "Player 1")
        board[p1 - 1] = player_one
        valid_pos.remove(str(p1))

        if gameplay.win_check(board):
            TicTacToe_board.print_game_board(board)
            print("Player1 win!")
            break
        elif gameplay.is_game_draw(valid_pos):
            TicTacToe_board.print_game_board(board)
            print("That's a draw")
            break

        TicTacToe_board.print_game_board(board)
        p2 = gameplay.get_player_input(valid_pos, "Player 2")
        board[p2 - 1] = player_two
        valid_pos.remove(str(p2))

        if gameplay.win_check(board):
            TicTacToe_board.print_game_board(board)
            print("Player2 win!")
            break
        elif gameplay.is_game_draw(valid_pos):
            TicTacToe_board.print_game_board(board)
            print("That's a draw")

            break
        TicTacToe_board.print_game_board(board)

    if gameplay.keep_playing():
        board.clear()
        pass
    else:
        print("Bye")
        gaming = False
        continue
