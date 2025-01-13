# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

board_size = 6
max_turns = 15

def create_board(num_ships = 5):
    """
    Creates the initial board that the game is played on. 
    Parameters include the number of ships that need to be placed on the grid.
    Returns the board and a list of the ship positions.
    """
    board = [["O" for _ in range(board_size)] for _ in range(board_size)]
    ship_positions = []

    while len(ship_positions) < num_ships:
        row = randint(0, board_size -1)
        col = randint(0, board_size -1)
    
        if (row, col) not in ship_positions:
            board[row][col] = "#"
            ship_positions.append((row, col))

    return board, ship_positions

board, ship_positions = create_board()

for row in board:
    print(" ".join(row))

print("Ship positions: ", ship_positions)

def target_placement():
    """
    Allows the user to input the row and column for their target.
    Ensures the input is within the bounds of the board and an integer.
    Returns the row and column of the target.
    """
    while True:
        try:
            row = int(input(f"Enter the target row (0 to {board_size - 1}): "))
            col = int(input(f"Enter the target column (0 to {board_size - 1}): "))

            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            else:
                print("Invalid input. Please enter values within the board's range.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

board, ship_positions = create_board()
print("\Opponent's board:")
for row in board:
    print(" ".join(row))

while True:
    print("\nPlace your target!")
    target_row, target_col = target_placement()

    if (target_row, target_col) in ship_positions:
        print(f"Great hit! You sunk a ship at ({target_row}, {target_col})!")
        board[target_row][target_col] = "!"  # Mark hit
        ship_positions.remove((target_row, target_col))
    else:
        print(f"Oh no, missed! No ship at ({target_row}, {target_col}).")
        board[target_row][target_col] = "X"  # Mark miss

    print("\nUpdated board:")
    for row in board:
        print(" ".join(row))

    if not ship_positions:
        print("\nCongratulations! We have a winner! You sank all the ships!")
        break

def opponents_target():
    """
    Opponent has a turn, randomly selecting integers within the board size.
    Returns randomly selected co-ordinates.
    """
    return randint(0, board_size -1), randint(0, board_size -1)

player_board, player_ships = create_board()
opponent_board, opponent_ships = create_board()

opponent_visible_board = [["O" for _ in range(board_size)] for _ in range(board_size)]