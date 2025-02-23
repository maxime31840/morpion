import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialisation des variables
        self.board = [""] * 9
        self.current_player = "X"
        
        # Création du tableau de boutons
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), 
                               command=lambda i=i: self.play(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def play(self, i):
        if self.board[i] == "":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Gagnant", f"Le joueur {self.current_player} a gagné!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Match Nul", "C'est un match nul!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Combinaisons gagnantes (lignes, colonnes et diagonales)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "":
                return True
        return False
    
    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"

# Création de la fenêtre principale
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
