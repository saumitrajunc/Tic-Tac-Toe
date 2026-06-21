"Tic-Tac-Toe with Minimax AI"

from __future__ import annotations

import sys
from typing import Optional

from ai import find_best_move, random_move
from board import (
    Player,
    check_winner,
    make_move,
    new_board,
    other_player,
    parse_move,
    print_board,
)


def play_game(
    *,
    human_player: Player = "X",
    ai_player: Optional[Player] = "O",
    use_random_ai: bool = False,
) -> None:
    board = new_board()
    current = "X"

    print("Cell numbers:")
    print(" 0 | 1 | 2")
    print("---+---+---")
    print(" 3 | 4 | 5")
    print("---+---+---")
    print(" 6 | 7 | 8")
    print()

    while check_winner(board) is None:
        print_board(board)
        print()

        if current == human_player or ai_player is None:
            move = None
            while move is None:
                move = parse_move(input(f"Player {current}, choose a cell (0-8): "), board)
        else:
            if use_random_ai:
                move = random_move(board)
                print(f"AI ({current}) picks a random move: {move}")
            else:
                move = find_best_move(board, ai_player, human_player)
                print(f"AI ({current}) plays optimally: {move}")

        board = make_move(board, move, current)
        current = other_player(current)

    print_board(board)
    print()

    result = check_winner(board)
    if result == "draw":
        print("It's a draw.")
    else:
        print(f"Player {result} wins!")


def run_cli_menu() -> None:
    print("Choose a mode:")
    print("1) Human vs Human")
    print("2) Human vs Optimal AI")
    print("3) Human vs Random AI")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        play_game(ai_player=None)
    elif choice == "3":
        play_game(use_random_ai=True)
    else:
        play_game()


def run_ui() -> bool:
    import os
    import subprocess

    ui_path = os.path.join(os.path.dirname(__file__), "UI.py")
    result = subprocess.run([sys.executable, ui_path], check=False)
    return result.returncode == 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli_menu()
    elif not run_ui():
        print("\nGraphical UI could not open. Starting terminal mode instead.\n")
        run_cli_menu()
