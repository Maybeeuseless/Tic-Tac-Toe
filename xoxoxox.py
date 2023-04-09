import tkinter as tk
import random


def check_win(board, player):
    win_positions = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]
                    ]
    for positions in win_positions:
        if positions == [player, player, player]:
            return True
    return False

def computer_move(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                empty_cells.append([i, j])
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        buttons[row][col].config(text="O", state="disabled")
        if check_win(board, "O"):
            turn_label.config(text='Вы проиграли')
            disable_buttons()
        else:
            on_click(board)

def on_click(row, col):
    global board, turn_label, buttons
    
    if board[row][col] == "":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        if check_win(board, "X"):
            turn_label.config(text="Поздравляю, вы выиграли!",fg='black')
            disable_buttons()
        else:
            computer_move(board)
            
def disable_buttons():
    global buttons
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True



root = tk.Tk()
root.title("Крестики-нолики")
board = [["" for _ in range(3)] for _ in range(3)]


turn_label = tk.Label(root, text='Игра началась', fg='black')
turn_label.grid(row=4,column=1)



buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=5, height=2,
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i+1, column=j)
        row.append(button)
    buttons.append(row)

root.mainloop()