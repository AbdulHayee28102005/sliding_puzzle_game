import tkinter as tk
from tkinter import messagebox
import random

class SlidePuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("Slide Puzzle")
        self.root.resizable(False, False)
        
        self.moves = 0
        self.board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ""]]
        self.empty_pos = (3, 3)
        
        self.shuffle_board()
        self.create_widgets()

    def shuffle_board(self):
        for _ in range(150):
            r, c = self.empty_pos
            possible_moves = []
            if r > 0: possible_moves.append((r - 1, c))
            if r < 3: possible_moves.append((r + 1, c))
            if c > 0: possible_moves.append((r, c - 1))
            if c < 3: possible_moves.append((r, c + 1))
            
            nr, nc = random.choice(possible_moves)
            self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
            self.empty_pos = (nr, nc)
        self.moves = 0

    def create_widgets(self):
        self.stats_frame = tk.Frame(self.root, pady=10)
        self.stats_frame.pack()
        
        self.label_moves = tk.Label(self.stats_frame, text="Moves: 0", font=("Helvetica", 14))
        self.label_moves.pack()
        
        self.grid_frame = tk.Frame(self.root, padx=10, pady=10)
        self.grid_frame.pack()
        
        self.buttons = []
        for r in range(4):
            row_buttons = []
            for c in range(4):
                val = self.board[r][c]
                btn = tk.Button(
                    self.grid_frame,
                    text=str(val),
                    font=("Helvetica", 20, "bold"),
                    width=4,
                    height=2,
                    command=lambda row=r, col=c: self.tile_clicked(row, col)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
        self.update_buttons()

    def tile_clicked(self, r, c):
        er, ec = self.empty_pos
        if (abs(r - er) == 1 and c == ec) or (abs(c - ec) == 1 and r == er):
            self.board[er][ec], self.board[r][c] = self.board[r][c], self.board[er][ec]
            self.empty_pos = (r, c)
            self.moves += 1
            self.label_moves.config(text=f"Moves: {self.moves}")
            self.update_buttons()
            
            if self.check_win():
                messagebox.showinfo("Congratulations!", f"You solved it in {self.moves} moves!")
                self.reset_game()

    def update_buttons(self):
        for r in range(4):
            for c in range(4):
                val = self.board[r][c]
                self.buttons[r][c].config(text=str(val))
                if val == "":
                    self.buttons[r][c].config(bg="gray", state="disabled")
                else:
                    self.buttons[r][c].config(bg="SystemButtonFace", state="normal")

    def check_win(self):
        expected = 1
        for r in range(4):
            for c in range(4):
                if r == 3 and c == 3:
                    return self.board[r][c] == ""
                if self.board[r][c] != expected:
                    return False
                expected += 1
        return True

    def reset_game(self):
        self.board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ""]]
        self.empty_pos = (3, 3)
        self.shuffle_board()
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = SlidePuzzle(root)
    root.mainloop()
