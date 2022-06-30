from config import board_pos_start


def print_sqaure_positions() -> None:
    starting_board = f"""
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
    """
    print(starting_board)
    return


def print_game_board(valid_pos: list[str]):
    board = f"""
            |       |
        {valid_pos[0]}   |   {valid_pos[1]}   |   {valid_pos[2]}
            |       |
    -------------------------
            |       |
        {valid_pos[3]}   |   {valid_pos[4]}   |   {valid_pos[5]}
            |       |
    -------------------------    
            |       |
        {valid_pos[6]}   |   {valid_pos[7]}   |   {valid_pos[8]}      
            |       |                   
        """
    print(board)
    return
