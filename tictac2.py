import tkinter as tk
from tkinter import messagebox


def create_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text="", font=('Times New Roman', 60), width=4, height=2,
                command=lambda row=i, col=j: click(row, col))
            buttons[i][j].grid(row=i, column=j)


def click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not check_winner() and not check_draw():
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True



root = tk.Tk()
root.title("Tic-Tac-Toe")
root.option_add("*Font", "Arial 16")
messagebox.showinfo("Welcome", "Welcome to Tic-Tac-Toe! Each player takes turns putting their X or O on the board. "
    "The first player to get three of their symbol in a row wins!")
buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"
create_board()
root.mainloop()
