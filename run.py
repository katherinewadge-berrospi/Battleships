# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

def get_dimensions():
    """
    Allows the user to pick the size of the board.
    Returns the chosen number of rows and columns. 
    """
    while True:
        try:
            rows = int(input("Enter the number of rows for the board (4 to 8): "))
            cols = int(input("Enter the number of columns for the board (4 to 8): "))
            if 4 <= rows <= 8 and 4 <= cols <= 8:
                return rows, cols
            else:
                print("Invalid input. Rows and columns must be between 4 and 8.")
        except ValueError:
            print("Invalid input. Please enter integers.")  


def create_board(rows, cols, num_ships=None):
    """
    Creates the initial board that the game is played on. 
    Parameters include the board dimensions and the number of ships.
    Returns the board and a list of the ship positions.
    """
    if num_ships is None:
        num_ships = min(rows, cols)
        
    board = [["O" for _ in range(cols)] for _ in range(rows)]
    ship_positions = []

    while len(ship_positions) < num_ships:
        row = randint(0, rows - 1)
        col = randint(0, cols - 1)

        # Checks if the position is already taken
        if (row, col) not in ship_positions:
            board[row][col] = "#"
            ship_positions.append((row, col))

    return board, ship_positions

rows, cols = get_board_dimensions()

num_ships = min(rows, cols)
# Initialising both boards and the ship positions
player_board, player_ships = create_board(rows, cols)
opponent_board, opponent_ships = create_board(rows, cols)
opponent_visible_board = [["O" for _ in range(cols)] for _ in range(rows)]

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
    if (target_row, target_col) in opponent_ships:
        print(f"Great hit! You sunk opponent's ship at ({target_row}, {target_col})!")
        opponent_board[target_row][target_col] = "!" 
        opponent_visible_board[target_row][target_col] = "!"
        opponent_ships.remove((target_row, target_col))
    # Marks a miss
    else:
        print(f"Miss! No ship at ({target_row}, {target_col}).")
        opponent_visible_board[target_row][target_col] = "X"  
    
    # Checks if game over
    if not opponent_ships:
        print(f"Congratulations! We have a winner! You sank all the ships!")

    print(" ")

    # Opponent's turn
    print("Opponent's turn!")
    while True:
        opponent_row, opponent_col = opponents_target()
        if player_board[opponent_row][opponent_col] not in ("!", "X"):
            break
    
    # Marks a successful hit
    if (opponent_row, opponent_col) in player_ships:
        print(f"The opponent hit your ship at ({opponent_row}, {opponent_col})!")
        player_board[opponent_row][opponent_col] = "!" 
        player_ships.remove((opponent_row, opponent_col))
     # Marks a miss
    else:
        print(f"The opponent missed at ({opponent_row}, {opponent_col}).")
        player_board[opponent_row][opponent_col] = "X" 
    
    # Check if the game is over
    if not player_ships:
        print("Oh no! The opponent sank all your ships! You lose!")
        break

    print(" ")
    turn += 1