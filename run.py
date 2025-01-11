# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

board_size = 6
max_turns = 15

def create_board():
    """
    Creates the initial board that the game is played on
    """
    board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    row = random.randint(0, board_size -1)
    col = random.randint(0, board_size -1)
    board[row][col] = "#"
    return board, (row, col)