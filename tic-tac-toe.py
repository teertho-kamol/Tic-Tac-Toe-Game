import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.game_board = ["", "", "", "", "", "", "", "", ""]
        self.game_over = False

        self.create_game_board()

    def create_game_board(self):
        # Create game board buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text="", font=("Arial", 40), width=2, height=1,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Create reset button
        self.reset_button = tk.Button(self.master, text="Reset", font=("Arial", 20), command=self.reset)
        self.reset_button.grid(row=3, column=1)

    def button_click(self, i):
        if not self.game_over:
            if self.game_board[i] == "":
                self.game_board[i] = self.current_player
                self.buttons[i].config(text=self.current_player)

                if self.check_win():
                    self.game_over = True
                    self.show_message(f"Player {self.current_player} wins!")
                elif self.check_draw():
                    self.game_over = True
                    self.show_message("Draw!")
                else:
                    self.change_player()

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]

        for pattern in win_patterns:
            if self.game_board[pattern[0]] == self.game_board[pattern[1]] == self.game_board[pattern[2]] != "":
                return True
        return False

    def check_draw(self):
        return "" not in self.game_board

    def reset(self):
        self.current_player = "X"
        self.game_board = ["", "", "", "", "", "", "", "", ""]
        self.game_over = False

        for button in self.buttons:
            button.config(text="")

    def show_message(self, message):
        self.reset_button.config(text="Play Again")
        tk.messagebox.showinfo("Game Over", message)

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
