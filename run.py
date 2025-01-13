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

        # Checks if the position is already taken
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
            # Allows user input
            row = int(input(f"Enter the target row (0 to {board_size - 1}): "))
            col = int(input(f"Enter the target column (0 to {board_size - 1}): "))

            # Checks if the input is within the bounds of the board
            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            else:
                print("Invalid input. Please enter values within the board's range.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")


def opponents_target():
    """
    Opponent has a turn, randomly selecting integers within the board size.
    Returns randomly selected co-ordinates.
    """
    return randint(0, board_size -1), randint(0, board_size -1)

# Initialising both boards and the ship positions
player_board, player_ships = create_board()
opponent_board, opponent_ships = create_board()

opponent_visible_board = [["O" for _ in range(board_size)] for _ in range(board_size)]

# Game loop
turn = 1

while player_ships and opponent_ships:
    print(f"|---Turn {turn}---|")

    # Displays both boards
    print("Your board: ")
    for row in player_board:
        print(" ".join(row))
    print("Opponent's board: ")
    for row in opponent_board:
        print(" ".join(row))
    
    # Player's turn
    print("Your turn!")
    target_row, target_col = target_placement()

     # Marks a successful hit
    if (target_row, target_column) in opponent_ships:
        print(f"Great hit! You sunk opponent's ship at ({target_row}, {target_col})!")
        board[target_row][target_col] = "!" 
        opponent_ships.remove((target_row, target_col))
    # Marks a miss
    else:
        print(f"Miss! No ship at ({target_row}, {target_col}).")
        opponent_board[target_row][target_col] = "M"  
    
    # Checks if game over
    if not opponent_ships:
        print(f"Congratulations! We have a winner! You sank all the ships!")

    # Opponent's turn
    print("Opponent's turn!")
    while True:
        opponent_row, opponent_col = opponents_target()
        if player_board[opponent_row][opponent_col] not in ("X", "M"):
            break
    
    # Marks a successful hit
    if (opponent_row, opponent_col) in player_ships:
        print(f"The opponent hit your ship at ({opponent_row}, {opponent_col})!")
        player_board[opponent_row][opponent_col] = "X" 
        player_ships.remove((opponent_row, opponent_col))
     # Marks a miss
    else:
        print(f"The opponent missed at ({opponent_row}, {opponent_col}).")
        player_board[opponent_row][opponent_col] = "M" 
    
    