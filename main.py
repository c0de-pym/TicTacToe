import config
import TicTacToe_board
import gameplay

gaming = True
print(gameplay.framing(gameplay.game_rules_description()))
print(TicTacToe_board.game_rules())
if gameplay.keep_playing():
    pass
else:
    print('Bye')
    gaming = False

while gaming:
    valid_pos = config.board_pos_start.copy()
    board = config.board_pos.copy()
    players_signs = gameplay.player1_choice_sign()
    player_one = players_signs[0]
    player_two = players_signs[1]
    TicTacToe_board.game_board(board)

    while not gameplay.win_check(board):
        p1 = gameplay.player1(valid_pos)
        board[p1-1] = player_one
        valid_pos.remove(str(p1))
        if gameplay.win_check(board):
            TicTacToe_board.game_board(board)
            print('Player1 win!')
            break
        elif gameplay.draw(valid_pos):
            TicTacToe_board.game_board(board)
            print('That\'s a draw')
            break
        TicTacToe_board.game_board(board)
        p2 = gameplay.player2(valid_pos)
        board[p2-1] = player_two
        valid_pos.remove(str(p2))
        if gameplay.win_check(board):
            TicTacToe_board.game_board(board)
            print('Player2 win!')
            break
        elif gameplay.draw(valid_pos):
            TicTacToe_board.game_board(board)
            print('That\'s a draw')
            break
        TicTacToe_board.game_board(board)

    if gameplay.keep_playing():
        board.clear()
        pass
    else:
        print('Bye')
        gaming = False
        continue
