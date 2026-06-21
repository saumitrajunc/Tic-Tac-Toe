"Board representation and game rules"

from __future__ import annotations

from typing import Literal, Optional # Ensures the value selected is either "X" or "O" 

Player = Literal["X", "O"] #Represents the player's symbol
Board = list[str] #Represents the board's state
GameResult = Optional[Literal["X", "O", "draw"]] #Reuslts of a finshied game: "X", "O", or "draw"

EMPTY = "." #Represents an empty cell on the board
WIN_LINES = [
    (0, 1, 2), #Top row
    (3, 4, 5), #Middle row
    (6, 7, 8), #Bottom row
    (0, 3, 6), #Left column
    (1, 4, 7), #Middle column
    (2, 5, 8), #Right column
    (0, 4, 8), #Diagonal from top-left to bottom-right
    (2, 4, 6), #Diagonal from top-right to bottom-left
]


def new_board() -> Board: #Creates a new board with 9 empty cells
    return [EMPTY] * 9 # Returns a list of 9 empty cells


# Prints the board in a readable format and formats it nicely
def print_board(board: Board) -> None: # Prints a board with nothing but only the cells that are empty
    for row in range(3):
        cells = board[row * 3 : row * 3 + 3]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")

def get_empty_cells(board: Board) -> list[int]: #Helps the AI find legal moves
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def make_move(board: Board, index: int, player: Player) -> Board: #Makes a move on the board and returns the new board
    next_board = board.copy()
    next_board[index] = player
    return next_board # Returns the new board with the move made


def check_winner(board: Board) -> GameResult: #Checks if there is a winner and returns the winner or a draw where it then returns a draw
    for a, b, c in WIN_LINES: # Check each winning line
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]

    if EMPTY not in board:
        return "draw" # Returns a draw if the board is full and there is no winner

    return None # Returns None if there is no winner or a draw


def other_player(player: Player) -> Player: # Swap turns between players
    return "O" if player == "X" else "X" # Returns the other player's symbol


def parse_move(raw: str, board: Board) -> Optional[int]: #Turn user input into a valid cell inde
    try:
        index = int(raw) # Converts the user input into an integer  
    except ValueError:
        print("Enter a number from 0 to 8.") # Prints an error message if the user input is not a number
        return None # Returns None if the user input is not a number

    if index not in range(9): # Checks if the index is within the range of the board
        print("That cell is outside the board. Use 0-8.") # Prints an error message if the index is outside the range of the board
        return None # Returns None if the index is outside the range of the board

    return index # Returns the index if the index is within the range of the board
