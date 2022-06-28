from config import board_pos_start
from config import board_pos


def game_rules():
    starting_board = f'''
        |       |
    {board_pos_start[0]}   |   {board_pos_start[1]}   |    {board_pos_start[2]}
        |       |
-------------------------
        |       |
    {board_pos_start[3]}   |   {board_pos_start[4]}   |   {board_pos_start[5]}
        |       |
-------------------------    
        |       |
    {board_pos_start[6]}   |   {board_pos_start[7]}   |   {board_pos_start[8]}      
        |       |                   
    '''
    print(starting_board)
    return


def game_board():
    board = f'''
            |       |
        {board_pos[0]}   |   {board_pos[1]}   |    {board_pos[2]}
            |       |
    -------------------------
            |       |
        {board_pos[3]}   |   {board_pos[4]}   |   {board_pos[5]}
            |       |
    -------------------------    
            |       |
        {board_pos[6]}   |   {board_pos[7]}   |   {board_pos[8]}      
            |       |                   
        '''
    print(board)
    return



