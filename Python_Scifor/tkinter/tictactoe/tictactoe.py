import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Game")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        self.root.geometry("300x350")  
        self.root.resizable(False, False)
        self.root.configure(bg='lightblue')
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font='Arial 20 bold', width=6, height=3,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} won!!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!!")
                self.reset_game()
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Tic Tac Toe", "This spot is already taken!")

    def check_winner(self, player):
        winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                              (0, 3, 6), (1, 4, 7), (2, 5, 8),
                              (0, 4, 8), (2, 4, 6)]
        for condition in winning_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
