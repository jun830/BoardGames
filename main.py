import tkinter as tk
from tkinter import ttk
import Othello as O
import Chess as C
import Shogi as S

games = ["オセロ", "チェス", "将棋"]
class choice_game:
    def __init__(self, root, games):
        self.frame = tk.Frame(root)
        self.frame.pack()

        for i, g in enumerate(games):
            button = ttk.Button(self.frame, text = g)
            button.grid(row=0, column=i, sticky="NSEW")

if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("600x400")
    choice_game(main, games)
    main.mainloop()
