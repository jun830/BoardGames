import tkinter as tk

class game:
    def __init__(self, root):
        self.board = [[ "","a","b","c","d","e","f","g","h", ""],
                      ["1", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"1"],
                      ["2", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"2"],
                      ["3", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"3"],
                      ["4", 0,  0 , 0 , 2 , 1 , 0 , 0 , 0 ,"4"],
                      ["5", 0,  0 , 0 , 1 , 2 , 0 , 0 , 0 ,"5"],
                      ["6", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"6"],
                      ["7", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"7"],
                      ["8", 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,"8"],
                      [ "","a","b","c","d","e","f","g","h", ""]]
        self.players = {1, 2}

        self.frame = tk.Frame(root)
        self.frame.pack()

        for i, b_i in enumerate(self.board):
            for j, b_j in enumerate(b_i):
                button = tk.Button(self.frame, text=" " if type(b_j) == int else b_j)
                button.grid(row=i, column=j, sticky="NSEW")

if __name__ == "__main__":
    root = tk.Tk()
    game(root)
    root.mainloop()
