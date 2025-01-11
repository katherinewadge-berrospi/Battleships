# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

board_size = 6
max_turns = 15

def create_board(num_ships = 4):
    """
    Creates the initial board that the game is played on. 
    Parameters include the number of ships that need to be placed on the grid.
    Returns the board and a list of the ship positions.
    """
    board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    ship_positions = []

    while len(ship_positions) < num_ships:
        row = random.randint(0, board_size -1)
        col = random.randint(0, board_size -1)
    
    if (row, col) not in ship_positions:
        board[row][col] = "#"
        ship_positions.append((row, col))

    return board, ship_positions