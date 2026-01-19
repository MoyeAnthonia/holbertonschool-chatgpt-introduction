#!/usr/bin/python3

def print_board(board):
    """Print the Tic Tac Toe board with row and column numbers."""
    print("  0   1   2")  # column numbers
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))  # row number
        if i < 2:
            print("  " + "-" * 9)


def check_winner(board):
    """Check if a player has won the game."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def get_input(player, coordinate):
    """
    Prompt the player for a row or column.
    Loops until a valid integer in 0-2 is entered.

    Returns:
        int: The valid coordinate.
    """
    while True:
        user_input = input(f"Enter {coordinate} (0-2) for player {player}: ").strip()
        try:
            value = int(user_input)
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid input. Must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Must be a number between 0 and 2.")


def tic_tac_toe():
    """Main Tic Tac Toe game loop."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    try:
        while True:
            print_board(board)

            # Check for draw
            if all(cell != " " for row in board for cell in row):
                print("It's a draw!")
                break

            # Get valid row
            row = get_input(player, "row")
            # Get valid column
            col = get_input(player, "column")

            # Check if spot is free
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[row][col] = player

            # Check for winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

    except KeyboardInterrupt:
        print("\nGame interrupted by user. Goodbye!")


if __name__ == "__main__":
    tic_tac_toe()
