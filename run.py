# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint


# Welcome message
welcome = "\nWelcome to BattleShips!"
choose = "\nChoose the size of the board..."
print(welcome.upper())

def get_player_name():
    """
    Players should enter their name.
    Returns the player's name.
    """
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        else:
            print("Everyone has a name... try again.")

# Get player name
player_name = get_player_name()
print(f"\nWelcome, {player_name}! Get ready for battle!")

print(choose)

def get_dimensions():
    """
    Allows the user to pick the size of the board.
    Returns the chosen number of rows and columns.
    """
    while True:
        try:
            rows = int(input("Number of rows (4 to 8):"))
            cols = int(input("Number of columns (4 to 8):"))
            if 4 <= rows <= 8 and 4 <= cols <= 8:
                return rows, cols
            else:
                print("Invalid input. Rows & columns must be between 4 and 8.")
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

        # Randomly decided ship's orientation:
        # 0 = horizontal, 1 = vertical
        orientation = randint(0, 1)

        # Horizontal ship
        if orientation == 0:
            row = randint(0, rows - 1)
            col = randint(0, cols - 2)
            # Two squares horizontally
            positions = [(row, col), (row, col + 1)]

        # Vertical ship
        else:
            row = randint(0, rows - 2)
            col = randint(0, cols - 1)
            # Two squares vertically
            positions = [(row, col), (row + 1, col)]

        # Checks there are no overlapping ships
        if all(pos not in ship_positions for pos in positions):
            for pos in positions:
                board[pos[0]][pos[1]] = "#"
                ship_positions.append(pos)

    return board, ship_positions


rows, cols = get_dimensions()

# Initialising both boards and the ship positions
num_ships = min(rows, cols)
player_board, player_ships = create_board(rows, cols)
opponent_board, opponent_ships = create_board(rows, cols)
opponent_visible_board = [["O" for _ in range(cols)] for _ in range(rows)]

# Initialising scores
player_score = 0
opponent_score = 0

# Game loop
turn = 1

while player_ships and opponent_ships:
    print(f"\n|---Turn {turn}---|")

    # Display number of ships remaining
    print(f"\nShips remaining - {player_name}: {len(player_ships)} | Opponent: {len(opponent_ships)}")

    # Displays both boards
    print(f"\n{player_name}'s board: ")
    for row in player_board:
        print(" ".join(row))

    print("\nOpponent's board: ")
    for row in opponent_visible_board:
        print(" ".join(row))

    # Display scores
    print(f"\n{player_name}'s Score: {player_score}")
    print(f"Opponent's Score: {opponent_score}")

    # Player's turn
    print(f"\n{player_name}'s turn!")
    while True:
        try:
            target_row = int(input(f"\nEnter the target row (0 - {rows - 1}): "))
            target_col = int(input(f"Enter the target column (0 - {cols - 1}): "))

            if 0 <= target_row < rows and 0 <= target_col < cols:
                if opponent_visible_board[target_row][target_col] not in ("!", "X"):
                    break
                else:
                    print("You already targeted this position. Try again.")
            else:
                print("Invalid input. Please enter values within the range.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

    # Marks a successful hit
    if (target_row, target_col) in opponent_ships:
        print(f"Great hit! You sunk opponent's ship at ({target_row}, {target_col})! You win 3 points.")
        opponent_board[target_row][target_col] = "!"
        opponent_visible_board[target_row][target_col] = "!"
        opponent_ships.remove((target_row, target_col))
        player_score += 3
    # Marks a miss
    else:
        print(f"Miss! No ship at ({target_row}, {target_col}). You lose 1 point.")
        opponent_visible_board[target_row][target_col] = "X"
        player_score -= 1

    # Checks if game over
    if not opponent_ships:
        print(f"\nCongratulations! You're the winner {player_name}! You sank all the ships!")

    print(" ")

    # Opponent's turn
    print("Opponent's turn!")
    while True:
        opponent_row, opponent_col = randint(0, rows - 1), randint(0, cols - 1)
        if player_board[opponent_row][opponent_col] not in ("!", "X"):
            break

    # Marks a successful hit
    if (opponent_row, opponent_col) in player_ships:
        print(f"The opponent hit your ship at ({opponent_row}, {opponent_col})! They win 3 points.")
        player_board[opponent_row][opponent_col] = "!"
        player_ships.remove((opponent_row, opponent_col))
        opponent_score += 3
    # Marks a miss
    else:
        print(f"The opponent missed at ({opponent_row}, {opponent_col}). They lose 1 point.")
        player_board[opponent_row][opponent_col] = "X"
        opponent_score -= 1

    # Check if the game is over
    if not player_ships:
        print("Oh no! The opponent sank all your ships! You lose!")
        break

    print(" ")
    turn += 1

# Game over: final scores
print("Game Over!")
print(f"Final Scores:\n{player_name}: {player_score}\nOpponent: {opponent_score}")