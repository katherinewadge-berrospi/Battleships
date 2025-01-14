from random import randint


# Welcome message
def display_welcome_message():
    """Displays the welcome message for the game."""
    print("\nWelcome to BattleShips!".upper())


# Get player name
def get_player_name():
    """Prompts the player to enter their name and returns it."""
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        print("Everyone has a name... try again.")


def get_dimensions():
    """Prompts the player to choose board dimensions and validates the input."""
    print("\nChoose the size of the board...")
    while True:
        try:
            rows = int(input("Number of rows (4 to 8): "))
            cols = int(input("Number of columns (4 to 8): "))
            if 4 <= rows <= 8 and 4 <= cols <= 8:
                return rows, cols
            print("Invalid input. Rows & columns must be between 4 and 8.")
        except ValueError:
            print("Invalid input. Please enter integers.")


def create_board(rows, cols, num_ships=None):
    """Creates a game board and randomly places ships on it."""
    if num_ships is None:
        num_ships = min(rows, cols)

    board = [["O" for _ in range(cols)] for _ in range(rows)]
    ship_positions = []

    while len(ship_positions) < num_ships:
        orientation = randint(0, 1)
        # Horizontal
        if orientation == 0:
            row, col = randint(0, rows - 1), randint(0, cols - 2)
            positions = [(row, col), (row, col + 1)]
        # Vertical
        else:
            row, col = randint(0, rows - 2), randint(0, cols - 1)
            positions = [(row, col), (row + 1, col)]

        if all(pos not in ship_positions for pos in positions):
            for pos in positions:
                board[pos[0]][pos[1]] = "#"
                ship_positions.append(pos)

    return board, ship_positions


def display_boards(player_name, player_board, opponent_visible_board, player_score, opponent_score, player_ships, opponent_ships, turn):
    """Displays the game state to the players and a score board."""
    print(f"\n|---Turn {turn}---|")
    print(f"\nShips remaining - {player_name}: {len(player_ships)} | Opponent: {len(opponent_ships)}")

    print(f"\n{player_name}'s board:")
    for row in player_board:
        print(" ".join(row))

    print("\nOpponent's board:")
    for row in opponent_visible_board:
        print(" ".join(row))

    print(f"\n{player_name}'s Score: {player_score}")
    print(f"Opponent's Score: {opponent_score}")


def player_turn(opponent_ships, opponent_board, opponent_visible_board, player_score):
    """Handles the player's turn."""
    while True:
        try:
            target_row = int(input(f"\nEnter the target row: "))
            target_col = int(input("Enter the target column: "))

            if opponent_visible_board[target_row][target_col] not in ("!", "X"):
                break
            print("You already targeted this position. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")

    if (target_row, target_col) in opponent_ships:
        print(f"Great hit! You sunk opponent's ship at ({target_row}, {target_col})!")
        opponent_board[target_row][target_col] = "!"
        opponent_visible_board[target_row][target_col] = "!"
        opponent_ships.remove((target_row, target_col))
        player_score += 3
    else:
        print(f"Miss! No ship at ({target_row}, {target_col}).")
        opponent_visible_board[target_row][target_col] = "X"
        player_score -= 1

    return player_score


def opponent_turn(player_ships, player_board, opponent_score):
    """Handles the opponent's turn."""
    while True:
        opponent_row, opponent_col = randint(0, len(player_board) - 1), randint(0, len(player_board[0]) - 1)
        if player_board[opponent_row][opponent_col] not in ("!", "X"):
            break

    if (opponent_row, opponent_col) in player_ships:
        print(f"The opponent hit your ship at ({opponent_row}, {opponent_col})!")
        player_board[opponent_row][opponent_col] = "!"
        player_ships.remove((opponent_row, opponent_col))
        opponent_score += 3
    else:
        print(f"The opponent missed at ({opponent_row}, {opponent_col}).")
        player_board[opponent_row][opponent_col] = "X"
        opponent_score -= 1

    return opponent_score


def main():
    """Main function to start and control the game."""
    display_welcome_message()
    player_name = get_player_name()
    rows, cols = get_dimensions()

    num_ships = min(rows, cols)
    player_board, player_ships = create_board(rows, cols, num_ships)
    opponent_board, opponent_ships = create_board(rows, cols, num_ships)
    opponent_visible_board = [["O" for _ in range(cols)] for _ in range(rows)]

    player_score = 0
    opponent_score = 0
    turn = 1


    # Checks if game over
    if not opponent_ships:
        print(f"\nCongratulations! You're the winner {player_name}! You sank all the ships!")

    print(" ")

    
    # Check if the game is over
    if not player_ships:
        print("Oh no! The opponent sank all your ships! You lose!")
        break

    print(" ")
    turn += 1

# Game over: final scores
print("Game Over!")
print(f"Final Scores:\n{player_name}: {player_score}\nOpponent: {opponent_score}")