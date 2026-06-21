"Simple UI for Tic-Tac-Toe"

from __future__ import annotations

import tkinter as tk # UI Library
from tkinter import messagebox

from ai import find_best_move
from board import Board, check_winner, make_move, new_board


class TicTacToeApp:
    def __init__(self, root: tk.Tk) -> None: # Initializes the game
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)

        self.human = "X" # Human player's symbol
        self.ai = "O" # AI player's symbol
        self.board: Board = new_board()
        self.buttons: list[tk.Button] = [] # Buttons for the game

        self.status = tk.Label(root, text="You are X. Click a square to play.", font=("Helvetica", 14))
        self.status.pack(pady=10)

        grid = tk.Frame(root) # Grid for the game
        grid.pack(padx=10, pady=5)

        for index in range(9): # Creates 9 buttons for the game
            button = tk.Button(
                grid,
                text="",
                width=4,
                height=2,
                font=("Helvetica", 24, "bold"),
                command=lambda i=index: self.on_click(i),
            )
            row, col = divmod(index, 3)
            button.grid(row=row, column=col, padx=4, pady=4)
            self.buttons.append(button)

        tk.Button(root, text="New Game", font=("Helvetica", 12), command=self.reset_game).pack(pady=10)

    def reset_game(self) -> None:
        self.board = new_board() # Creates a new board
        for button in self.buttons: # Resets the buttons
            button.config(text="", state=tk.NORMAL)
        self.status.config(text="You are X. Click a square to play.") # Resets the status

    def update_buttons(self) -> None: # Updates the buttons
        for index, button in enumerate(self.buttons): 
            cell = self.board[index]
            if cell == ".":
                button.config(text="", state=tk.NORMAL)
            else:
                button.config(text=cell, state=tk.DISABLED)

    def end_game(self, result: str) -> None: # Ends the game
        for button in self.buttons:
            button.config(state=tk.DISABLED)

        if result == "draw":
            self.status.config(text="Draw!") # Sets the status to "Draw!"
            messagebox.showinfo("Game Over", "It's a draw.") # Shows a message box with the result
        else:
            if result == self.human:
                message = "You win!" # Sets the status to "You win!"
            else:
                message = "AI wins!" # Sets the status to "AI wins!"
            self.status.config(text=message)
            messagebox.showinfo("Game Over", message) 

    def on_click(self, index: int) -> None: 
        if check_winner(self.board) is not None or self.board[index] != ".": # Checks if there is a winner or the cell is not empty
            return

        self.board = make_move(self.board, index, self.human)
        self.update_buttons()

        result = check_winner(self.board) # Checks if there is a winner
        if result is not None:
            self.end_game(result)
            return

        self.status.config(text="AI is thinking...") 
        self.root.update_idletasks()

        ai_move = find_best_move(self.board, self.ai, self.human)
        self.board = make_move(self.board, ai_move, self.ai)
        self.update_buttons()

        result = check_winner(self.board)
        if result is not None:
            self.end_game(result)
        else:
            self.status.config(text="Your turn (X).")


def main() -> None: # Runs the game
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
