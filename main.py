import config
import TicTacToe_board
import gameplay

gaming = True
while gaming:
    print(gameplay.framing(gameplay.game_rules_description()))
    print(TicTacToe_board.game_rules())

    if gameplay.keep_playing():
        pass
    else:
        print('Bye')
        gaming = False
        continue

    players_signs = gameplay.player1_choice_sign()
    player_one = players_signs[0]
    player_two = players_signs[1]
    print(player_one)
    print(player_two)
    board = config.board_pos
    TicTacToe_board.game_board()
    while not gameplay.win_check():
        board[gameplay.player1()-1] = player_one
        if gameplay.win_check():
            print('Player1 win!')
            break
        board[gameplay.player2()-1] = player_two
        if gameplay.win_check():
            print('Player2 win!')
            break
        TicTacToe_board.game_board()

    if gameplay.keep_playing():
        pass
    else:
        print('Bye')
        gaming = False
        continue
