"AI move selection - random and Minimax AI"

from __future__ import annotations

import random

from board import Board, Player, check_winner, get_empty_cells, make_move


def random_move(board: Board) -> int: # Chooses a random LEGAL move from the empty cells
    return random.choice(get_empty_cells(board))


def minimax(
    board: Board, # Current board state
    is_maximizing: bool, # AI is maximizing, human is minimizing
    ai_player: Player,
    human_player: Player, 
    depth: int = 0, # Current depth of the minimax tree
    alpha: int = -10**9, # Alpha value for alpha-beta pruning
    beta: int = 10**9, # Beta value for alpha-beta pruning
) -> int:
    winner = check_winner(board) # Checks if there is a winner and returns the winner or a draw where it then returns a draw

    if winner == ai_player:
        return 10 - depth # Returns a score of 10 - depth if the AI wins
    if winner == human_player:
        return -10 + depth # Returns a score of -10 + depth if the human wins
    if winner == "draw":
        return 0 # Returns a score of 0 if the game is a draw

    if is_maximizing:
        best_score = -10**9 # Initializes the best score to a very low value
        for cell in get_empty_cells(board):
            next_board = make_move(board, cell, ai_player) # Makes a move on the board and returns the new board
            score = minimax(
                next_board,
                False,
                ai_player,
                human_player,
                depth + 1,
                alpha,
                beta,
            )
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha: # Prunes the tree if the beta value is less than or equal to the alpha value
                break
        return best_score # Returns the best score

    best_score = 10**9 # Initializes the best score to a very high value
    for cell in get_empty_cells(board):
        next_board = make_move(board, cell, human_player) # Makes a move on the board and returns the new board
        score = minimax(
            next_board,
            True,
            ai_player,
            human_player,
            depth + 1,
            alpha,
            beta,
        )
        best_score = min(best_score, score)
        beta = min(beta, score)
        if beta <= alpha:
            break
    return best_score # Returns the best score


def find_best_move(board: Board, ai_player: Player, human_player: Player) -> int: # Finds the best move for the AI
    best_score = -10**9
    best_move = get_empty_cells(board)[0] # Initializes the best move to the first empty cell

    for cell in get_empty_cells(board): # Checks each empty cell
        next_board = make_move(board, cell, ai_player)
        score = minimax(next_board, False, ai_player, human_player, depth=1)
        if score > best_score:
            best_score = score
            best_move = cell # Updates the best move to the current cell

    return best_move
